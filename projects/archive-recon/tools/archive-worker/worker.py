"""archive-worker: OCR and full-text index of PDF books for archive-recon.

Runs as a long-lived service in its own container (plan: projects/archive-recon/SERVER_PLAN_ocr.en.md).
One book at a time: download -> md5 check -> text layer -> OCR of EVERY page -> index -> delete download.
Three texts per page: layer as is, OCR as is, OCR search text (hyphen joins in place).
HTTP on the internal network only: GET /status, /search, /page; POST /control/*.
Control accepts data and parameters only (whitelisted), never code.
"""
import hashlib, json, os, re, shutil, sqlite3, subprocess, sys, tempfile, threading, time, traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import pymupdf

VERSION = "1.0"
DATA = os.environ.get("DATA_DIR", "/data")
OUT = os.path.join(DATA, os.environ.get("OUT_SUBDIR", "ocr"))
DB = os.path.join(OUT, "index.sqlite")
WORK = os.path.join(OUT, "tmp")
SOURCE_DIR = os.environ.get("SOURCE_DIR")              # local test mode: PDFs from a folder instead of Drive
REMOTE = os.environ.get("REMOTE", "archive:Telegram")  # rclone remote:path of the queue folder
RCLONE_CONF = os.environ.get("RCLONE_CONFIG", "/secrets/rclone.conf")
RCLONE_KEY = os.environ.get("RCLONE_KEY", "/secrets/key.json")
PORT = int(os.environ.get("PORT", "8080"))
MIN_FREE_GB = float(os.environ.get("MIN_FREE_GB", "20"))
MAX_FAILS_IN_ROW = 3
LANG_RE = re.compile(r"^(eng|deu|rus)(\+(eng|deu|rus)){0,2}$")
DEFAULTS = {"default_dpi": "200", "keep_upper_hyphen": "1", "min_letters": "2",
            "paused": "0", "pause_reason": ""}

state = {"current": None, "page": None, "started": time.time()}


# ---------------------------------------------------------------- database
def connect(readonly=False):
    if readonly:
        c = sqlite3.connect("file:%s?mode=ro" % DB, uri=True, timeout=30, check_same_thread=False)
    else:
        c = sqlite3.connect(DB, timeout=30, check_same_thread=False)
    c.row_factory = sqlite3.Row
    c.execute("PRAGMA busy_timeout=30000")
    return c


def init_db():
    os.makedirs(WORK, exist_ok=True)
    c = connect()
    c.execute("PRAGMA journal_mode=WAL")
    c.executescript("""
    CREATE TABLE IF NOT EXISTS books(
      id INTEGER PRIMARY KEY, path TEXT UNIQUE NOT NULL, name TEXT, drive_id TEXT, size INTEGER, md5 TEXT,
      status TEXT NOT NULL DEFAULT 'queued', priority INTEGER NOT NULL DEFAULT 100,
      lang TEXT, lang_used TEXT, dpi INTEGER, pages INTEGER, layer_pages INTEGER, ocr_pages INTEGER,
      toc TEXT, error TEXT, started REAL, finished REAL);
    CREATE TABLE IF NOT EXISTS pages(
      book_id INTEGER NOT NULL, page INTEGER NOT NULL, label TEXT, layer TEXT, ocr TEXT, ocr_search TEXT,
      ocr_conf REAL, PRIMARY KEY(book_id, page));
    CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY, value TEXT);
    CREATE VIRTUAL TABLE IF NOT EXISTS fts_layer USING fts5(book_id UNINDEXED, page UNINDEXED, text,
      tokenize='unicode61 remove_diacritics 2');
    CREATE VIRTUAL TABLE IF NOT EXISTS fts_ocr USING fts5(book_id UNINDEXED, page UNINDEXED, text,
      tokenize='unicode61 remove_diacritics 2');
    """)
    for k, v in DEFAULTS.items():
        c.execute("INSERT OR IGNORE INTO settings VALUES(?,?)", (k, v))
    # a book left in 'working' by a restart continues where it stopped (pages already saved are kept)
    c.execute("UPDATE books SET status='queued' WHERE status='working'")
    c.commit()
    c.close()


def setting(c, key):
    r = c.execute("SELECT value FROM settings WHERE key=?", (key,)).fetchone()
    return r["value"] if r else DEFAULTS.get(key)


def set_setting(c, key, value):
    c.execute("INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, str(value)))


# ---------------------------------------------------------------- text helpers
CTRL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")


def clean_for_index(t):
    return CTRL_RE.sub(" ", t or "")


def join_hyphens(text, keep_upper=True, min_letters=2):
    """Join words split by a hyphen at a line break, in place. Other line breaks stay.
    Tesseract often puts an empty line after a short line, so one empty line between the parts is allowed."""
    if not text:
        return text
    n = max(1, int(min_letters))
    pat = re.compile(r"([^\W\d_]{%d,})-[ \t]*\n(?:[ \t]*\n)?[ \t]*([^\W\d_]{%d,})" % (n, n))

    def rep(m):
        a, b = m.group(1), m.group(2)
        if keep_upper and b[0].isupper():
            return a + "-" + b
        return a + b
    return pat.sub(rep, text)


# ---------------------------------------------------------------- source (Drive via rclone, or a local folder)
def rclone(*args, timeout=3600):
    cmd = ["rclone", "--config", RCLONE_CONF, "--drive-service-account-file", RCLONE_KEY,
           "--drive-scope", "drive.readonly"] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def list_source():
    """Return [{path, name, size, md5, drive_id}] for every PDF in the queue folder."""
    out = []
    if SOURCE_DIR:
        for root, _, files in os.walk(SOURCE_DIR):
            for f in sorted(files):
                p = os.path.join(root, f)
                with open(p, "rb") as fh:
                    head = fh.read(5)
                if head != b"%PDF-":
                    continue
                out.append({"path": os.path.relpath(p, SOURCE_DIR), "name": f, "size": os.path.getsize(p),
                            "md5": md5_file(p), "drive_id": None})
        return out
    r = rclone("lsjson", "--recursive", "--files-only", "--hash", REMOTE, timeout=600)
    if r.returncode != 0:
        raise RuntimeError("rclone lsjson failed: " + r.stderr.strip()[-500:])
    for e in json.loads(r.stdout):
        if e.get("MimeType") != "application/pdf":   # filter by type: some PDFs have no .pdf extension
            continue
        out.append({"path": e["Path"], "name": e["Name"], "size": e.get("Size"),
                    "md5": (e.get("Hashes") or {}).get("md5"), "drive_id": e.get("ID")})
    return out


def fetch(book, dest):
    if SOURCE_DIR:
        shutil.copyfile(os.path.join(SOURCE_DIR, book["path"]), dest)
    else:
        r = rclone("copyto", REMOTE.rstrip("/") + "/" + book["path"], dest)
        if r.returncode != 0:
            raise RuntimeError("rclone copyto failed: " + r.stderr.strip()[-500:])
    if book["md5"] and md5_file(dest) != book["md5"]:
        raise RuntimeError("md5 mismatch after download")


def md5_file(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sync_queue(c):
    """Add PDFs from the source folder that are not in the queue yet. Returns number added."""
    added = 0
    for f in list_source():
        cur = c.execute("INSERT OR IGNORE INTO books(path,name,drive_id,size,md5) VALUES(?,?,?,?,?)",
                        (f["path"], f["name"], f["drive_id"], f["size"], f["md5"]))
        added += cur.rowcount
    c.commit()
    return added


# ---------------------------------------------------------------- OCR
def ocr_page(page, dpi, lang):
    """Render one page and run tesseract once (txt + tsv). Returns (text, mean word confidence)."""
    with tempfile.TemporaryDirectory(dir=WORK) as td:
        img = os.path.join(td, "p.png")
        page.get_pixmap(dpi=dpi).save(img)
        base = os.path.join(td, "o")
        r = subprocess.run(["tesseract", img, base, "-l", lang, "txt", "tsv"],
                           capture_output=True, text=True, timeout=600)
        if r.returncode != 0:
            raise RuntimeError("tesseract failed: " + r.stderr.strip()[-300:])
        with open(base + ".txt", encoding="utf-8") as f:
            text = f.read()
        confs = []
        with open(base + ".tsv", encoding="utf-8") as f:
            next(f, None)
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) == 12 and parts[11].strip():
                    try:
                        cv = float(parts[10])
                    except ValueError:
                        continue
                    if cv >= 0:
                        confs.append(cv)
        return text, (sum(confs) / len(confs) if confs else None)


EN_WORDS = set("the and of to in is that for with are as by this from".split())
DE_WORDS = set("der die das und ist nicht mit von den des ein eine zu im auf".split())


def detect_lang(doc, dpi):
    """Probe 3 pages (25/50/75 % of the book, to avoid covers) with eng+deu+rus,
    then choose by script and function words: Cyrillic share -> rus, German vs English words -> deu/eng."""
    n = doc.page_count
    probes = sorted({max(0, min(n - 1, int(n * f))) for f in (0.25, 0.5, 0.75)})
    text = " ".join(ocr_page(doc[i], dpi, "eng+deu+rus")[0] for i in probes)
    letters = [ch for ch in text if ch.isalpha()]
    if len(letters) < 50:
        return "eng+deu+rus", "too little text on probe pages"
    cyr = sum(1 for ch in letters if "Ѐ" <= ch <= "ӿ") / len(letters)
    words = re.findall(r"[^\W\d_]+", text.lower())
    en = sum(w in EN_WORDS for w in words)
    de = sum(w in DE_WORDS for w in words) + text.count("ß") + sum(text.count(x) for x in "äöüÄÖÜ")
    latin = "deu" if de > en else "eng"
    if cyr > 0.85:
        lang = "rus"
    elif cyr > 0.10:
        lang = "rus+" + latin
    else:
        lang = latin if min(en, de) < 0.25 * max(en, de, 1) else "eng+deu"
    return lang, "cyrillic %.2f, en words %d, de signals %d, probe pages %s" % (cyr, en, de, [p + 1 for p in probes])


# ---------------------------------------------------------------- book processing
def free_gb():
    return shutil.disk_usage(OUT).free / 2**30


def process_book(c, book):
    bid = book["id"]
    c.execute("UPDATE books SET status='working', started=?, error=NULL WHERE id=?", (time.time(), bid))
    c.commit()
    state["current"] = book["name"]
    dest = os.path.join(WORK, "book-%d.pdf" % bid)
    try:
        fetch(book, dest)
        doc = pymupdf.open(dest)
        if doc.needs_pass and not doc.authenticate(""):
            raise RuntimeError("PDF needs a password")
        n = doc.page_count
        dpi = book["dpi"] or int(setting(c, "default_dpi"))
        keep_upper = setting(c, "keep_upper_hyphen") == "1"
        min_letters = int(setting(c, "min_letters"))
        try:
            toc = json.dumps(doc.get_toc(simple=True), ensure_ascii=False)
        except Exception:
            toc = None
        lang = book["lang"]
        note = "set by control"
        if not lang:
            lang, note = detect_lang(doc, dpi)
        c.execute("UPDATE books SET pages=?, toc=?, lang_used=?, error=? WHERE id=?",
                  (n, toc, lang, "lang: " + note, bid))
        c.commit()
        done = {r["page"] for r in c.execute("SELECT page FROM pages WHERE book_id=? AND ocr IS NOT NULL", (bid,))}
        for i in range(n):
            pno = i + 1
            if pno in done:
                continue
            if setting(c, "paused") == "1":
                raise InterruptedError("paused")
            if free_gb() < MIN_FREE_GB:
                pause(c, "free space %.1f GiB below %.0f" % (free_gb(), MIN_FREE_GB))
                raise InterruptedError("paused")
            state["page"] = pno
            page = doc[i]
            try:
                label = page.get_label() or None
            except Exception:
                label = None
            layer = page.get_text() or ""
            text, conf = ocr_page(page, dpi, lang)
            search = join_hyphens(text, keep_upper, min_letters)
            c.execute("INSERT OR REPLACE INTO pages VALUES(?,?,?,?,?,?,?)",
                      (bid, pno, label, layer, text, search, conf))
            c.execute("DELETE FROM fts_layer WHERE book_id=? AND page=?", (bid, pno))
            c.execute("DELETE FROM fts_ocr WHERE book_id=? AND page=?", (bid, pno))
            if layer.strip():
                c.execute("INSERT INTO fts_layer VALUES(?,?,?)", (bid, pno, clean_for_index(layer)))
            c.execute("INSERT INTO fts_ocr VALUES(?,?,?)", (bid, pno, clean_for_index(search)))
            c.commit()
        layer_pages = c.execute("SELECT count(*) FROM pages WHERE book_id=? AND length(trim(layer))>0", (bid,)).fetchone()[0]
        ocr_pages = c.execute("SELECT count(*) FROM pages WHERE book_id=? AND ocr IS NOT NULL", (bid,)).fetchone()[0]
        c.execute("UPDATE books SET status='done', finished=?, layer_pages=?, ocr_pages=?, dpi=? WHERE id=?",
                  (time.time(), layer_pages, ocr_pages, dpi, bid))
        c.commit()
        doc.close()
        return True
    except InterruptedError:
        c.execute("UPDATE books SET status='queued' WHERE id=?", (bid,))
        c.commit()
        return None
    except Exception as e:
        c.execute("UPDATE books SET status='error', finished=?, error=? WHERE id=?",
                  (time.time(), ("%s: %s" % (type(e).__name__, e))[:1000], bid))
        c.commit()
        traceback.print_exc()
        return False
    finally:
        state["current"] = state["page"] = None
        if os.path.exists(dest):
            os.remove(dest)


def pause(c, reason):
    set_setting(c, "paused", "1")
    set_setting(c, "pause_reason", reason)
    c.commit()
    print("PAUSED:", reason, flush=True)


def worker_loop():
    c = connect()
    fails = 0
    last_sync = 0
    while True:
        try:
            if time.time() - last_sync > 3600:
                added = sync_queue(c)
                last_sync = time.time()
                if added:
                    print("queue: %d new file(s)" % added, flush=True)
            if setting(c, "paused") == "1":
                time.sleep(10)
                continue
            if free_gb() < MIN_FREE_GB:
                pause(c, "free space %.1f GiB below %.0f" % (free_gb(), MIN_FREE_GB))
                continue
            book = c.execute("SELECT * FROM books WHERE status='queued' ORDER BY priority, id LIMIT 1").fetchone()
            if not book:
                time.sleep(30)
                continue
            print("book %d: %s" % (book["id"], book["name"]), flush=True)
            res = process_book(c, book)
            if res is False:
                fails += 1
                if fails >= MAX_FAILS_IN_ROW:
                    pause(c, "%d books failed in a row" % fails)
                    fails = 0
            elif res is True:
                fails = 0
        except Exception:
            traceback.print_exc()
            time.sleep(60)


# ---------------------------------------------------------------- control (data and parameters only)
class Bad(Exception):
    pass


def control(c, action, body):
    if action == "pause":
        pause(c, "by control")
    elif action == "resume":
        set_setting(c, "paused", "0")
        set_setting(c, "pause_reason", "")
    elif action == "rescan":
        return {"added": sync_queue(c)}
    elif action == "settings":
        for k, v in body.items():
            if k == "default_dpi":
                set_setting(c, k, check_dpi(v))
            elif k == "keep_upper_hyphen":
                if v not in (True, False, 0, 1, "0", "1"):
                    raise Bad("keep_upper_hyphen must be true or false")
                set_setting(c, k, "1" if v in (True, 1, "1") else "0")
            elif k == "min_letters":
                if not isinstance(v, int) or not 1 <= v <= 5:
                    raise Bad("min_letters must be an integer 1-5")
                set_setting(c, k, v)
            else:
                raise Bad("unknown setting: %s" % k)
    elif action == "rebuild_search":
        keep_upper = setting(c, "keep_upper_hyphen") == "1"
        min_letters = int(setting(c, "min_letters"))
        rows = c.execute("SELECT book_id, page, ocr FROM pages WHERE ocr IS NOT NULL").fetchall()
        for r in rows:
            s = join_hyphens(r["ocr"], keep_upper, min_letters)
            c.execute("UPDATE pages SET ocr_search=? WHERE book_id=? AND page=?", (s, r["book_id"], r["page"]))
        c.execute("DELETE FROM fts_ocr")
        c.execute("INSERT INTO fts_ocr SELECT book_id, page, ocr_search FROM pages WHERE ocr IS NOT NULL")
        c.commit()
        return {"pages": len(rows)}
    elif action == "book":
        bid = body.get("id")
        if not isinstance(bid, int) or not c.execute("SELECT 1 FROM books WHERE id=?", (bid,)).fetchone():
            raise Bad("unknown book id")
        op, val = body.get("op"), body.get("value")
        if op == "requeue":       # redo from scratch: drop pages and OCR again
            for t in ("pages", "fts_layer", "fts_ocr"):
                c.execute("DELETE FROM %s WHERE book_id=?" % t, (bid,))
            c.execute("UPDATE books SET status='queued', error=NULL, finished=NULL WHERE id=?", (bid,))
        elif op == "enqueue":     # continue (e.g. after an error), keep saved pages
            c.execute("UPDATE books SET status='queued', error=NULL WHERE id=?", (bid,))
        elif op == "skip":
            c.execute("UPDATE books SET status='skipped' WHERE id=?", (bid,))
        elif op == "priority":
            if not isinstance(val, int) or not 0 <= val <= 1000:
                raise Bad("priority must be an integer 0-1000 (smaller goes first)")
            c.execute("UPDATE books SET priority=? WHERE id=?", (val, bid))
        elif op == "lang":
            if val is not None and not (isinstance(val, str) and LANG_RE.match(val)):
                raise Bad("lang must be eng, deu, rus or their combination joined by +, or null for auto")
            c.execute("UPDATE books SET lang=? WHERE id=?", (val, bid))
        elif op == "dpi":
            c.execute("UPDATE books SET dpi=? WHERE id=?", (None if val is None else check_dpi(val), bid))
        else:
            raise Bad("op must be requeue, enqueue, skip, priority, lang or dpi")
    else:
        raise Bad("unknown control action")
    c.commit()
    return {"ok": True}


def check_dpi(v):
    if not isinstance(v, int) or not 150 <= v <= 400:
        raise Bad("dpi must be an integer 150-400")
    return v


# ---------------------------------------------------------------- read API
def fts_query(q):
    """Turn free text into a safe FTS5 query: every word quoted, implicit AND."""
    words = re.findall(r"[^\W_]+", q)
    if not words:
        raise Bad("empty query")
    return " ".join('"%s"' % w for w in words[:20])


def search(c, q, limit=10, book=None):
    fq = fts_query(q)
    hits = {}
    for table, src in (("fts_ocr", "ocr"), ("fts_layer", "layer")):
        sql = ("SELECT book_id, page, bm25(%s) AS s, snippet(%s, 2, '[', ']', ' … ', 12) AS snip "
               "FROM %s WHERE %s MATCH ?" % (table, table, table, table))
        args = [fq]
        if book is not None:
            sql += " AND book_id=?"
            args.append(book)
        sql += " ORDER BY s LIMIT ?"
        args.append(limit * 3)
        for r in c.execute(sql, args):
            key = (int(r["book_id"]), int(r["page"]))
            h = hits.setdefault(key, {"book_id": key[0], "page": key[1], "sources": [], "score": 0.0, "snippets": {}})
            h["sources"].append(src)
            h["score"] = min(h["score"], r["s"])
            h["snippets"][src] = r["snip"]
    out = sorted(hits.values(), key=lambda h: h["score"])[:limit]
    for h in out:
        b = c.execute("SELECT name FROM books WHERE id=?", (h["book_id"],)).fetchone()
        p = c.execute("SELECT label FROM pages WHERE book_id=? AND page=?", (h["book_id"], h["page"])).fetchone()
        h["name"] = b["name"] if b else None
        h["label"] = p["label"] if p else None
        h["source"] = "both" if len(h["sources"]) == 2 else h["sources"][0]
        del h["sources"]
    return {"query": q, "hits": out}


def status(c):
    books = [dict(r) for r in c.execute(
        "SELECT id, name, status, priority, pages, layer_pages, ocr_pages, lang, lang_used, dpi, error, started, finished "
        "FROM books ORDER BY priority, id")]
    counts = {}
    for b in books:
        counts[b["status"]] = counts.get(b["status"], 0) + 1
    return {"version": VERSION, "paused": setting(c, "paused") == "1", "pause_reason": setting(c, "pause_reason"),
            "current": state["current"], "current_page": state["page"], "free_gib": round(free_gb(), 1),
            "settings": {k: setting(c, k) for k in ("default_dpi", "keep_upper_hyphen", "min_letters")},
            "counts": counts, "books": books}


def page_text(c, book, page):
    r = c.execute("SELECT p.*, b.name FROM pages p JOIN books b ON b.id=p.book_id WHERE book_id=? AND page=?",
                  (book, page)).fetchone()
    if not r:
        raise Bad("no such page")
    b = c.execute("SELECT pages, toc FROM books WHERE id=?", (book,)).fetchone()
    return {"book_id": book, "name": r["name"], "page": page, "pages": b["pages"], "label": r["label"],
            "ocr_conf": r["ocr_conf"], "layer": r["layer"], "ocr": r["ocr"], "ocr_search": r["ocr_search"]}


class Handler(BaseHTTPRequestHandler):
    def reply(self, code, obj):
        data = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        c = connect(readonly=True)
        try:
            if u.path == "/health":
                self.reply(200, {"ok": True, "version": VERSION})
            elif u.path == "/status":
                self.reply(200, status(c))
            elif u.path == "/search":
                limit = min(max(int(q.get("limit", "10")), 1), 50)
                book = int(q["book"]) if q.get("book") else None
                self.reply(200, search(c, q.get("q", ""), limit, book))
            elif u.path == "/page":
                self.reply(200, page_text(c, int(q["book"]), int(q["page"])))
            elif u.path == "/toc":
                r = c.execute("SELECT id, name, pages, toc FROM books WHERE id=?", (int(q["book"]),)).fetchone()
                if not r:
                    raise Bad("unknown book id")
                self.reply(200, {"book_id": r["id"], "name": r["name"], "pages": r["pages"],
                                 "toc": json.loads(r["toc"]) if r["toc"] else []})
            else:
                self.reply(404, {"error": "not found"})
        except (Bad, KeyError, ValueError) as e:
            self.reply(400, {"error": str(e) or "bad request"})
        except Exception as e:
            traceback.print_exc()
            self.reply(500, {"error": type(e).__name__})
        finally:
            c.close()

    def do_POST(self):
        u = urlparse(self.path)
        if not u.path.startswith("/control/"):
            return self.reply(404, {"error": "not found"})
        try:
            n = int(self.headers.get("Content-Length", "0"))
            if n > 65536:
                raise Bad("body too large")
            body = json.loads(self.rfile.read(n) or b"{}")
            if not isinstance(body, dict):
                raise Bad("body must be a JSON object")
            c = connect()
            try:
                self.reply(200, control(c, u.path[len("/control/"):], body))
            finally:
                c.close()
        except (Bad, ValueError) as e:
            self.reply(400, {"error": str(e) or "bad request"})
        except Exception as e:
            traceback.print_exc()
            self.reply(500, {"error": type(e).__name__})

    def log_message(self, fmt, *args):
        pass


def main():
    init_db()
    print("archive-worker %s, db %s, source %s, free %.1f GiB" % (VERSION, DB, SOURCE_DIR or REMOTE, free_gb()), flush=True)
    if "--once" in sys.argv:            # test mode: process the queue to the end, then exit
        c = connect()
        sync_queue(c)
        while True:
            b = c.execute("SELECT * FROM books WHERE status='queued' ORDER BY priority, id LIMIT 1").fetchone()
            if not b:
                break
            print("book %d: %s -> %s" % (b["id"], b["name"], process_book(c, b)), flush=True)
        return
    threading.Thread(target=worker_loop, daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
