#!/usr/bin/env python3
"""archive_scan.py - inventory of a document archive (PDFs, videos, any files).

projects/archive-recon/tools/archive_scan.py, version 1.2.
Restored 2026-10-10 from the description in decision R-15, point 1, of
projects/archive-recon/LOG.md (the original file of 2026-09-27 was lost) - this is a
rewrite, not a copy; the output columns follow the description, not the lost source.

Walks a folder completely and writes, for every file: path, size, dates, md5, document
type together with the rule that decided it, DOI (first two pages, the "Bibliografie" /
"Zitierweise" box up to page 40, file name incl. Springer names like s44180-021-0018-7.pdf),
AWMF register number, guideline class and variant, year together with its source, mind-map
card status, duplicates of three kinds (byte copy, same DOI, similar title with almost equal
page count).

Outputs (into --out): files.csv, folders.csv, guidelines.csv, duplicates.csv, summary.txt,
cache scan_cache.sqlite, and with --save-text the folder texts/.
The outputs hold personal paths and third-party texts: never put them into a public repo.

Needs: Python 3.8+, PyMuPDF (pip install pymupdf). For --ocr: Tesseract with deu and eng.
Everything else is the standard library. See README.md (in Russian).
"""
import argparse
import collections
import csv
import datetime
import difflib
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

VERSION = "1.2"
EXTRACT_VERSION = 3          # bump when the raw extraction changes: invalidates the cache
NOW_YEAR = datetime.date.today().year

EXT_KIND = {}
for _kind, _exts in {
    "pdf": [".pdf"],
    "video": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".m4v", ".webm", ".mpg", ".mpeg", ".flv", ".3gp"],
    "audio": [".mp3", ".wav", ".m4a", ".ogg", ".flac", ".aac"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".heic", ".svg"],
    "office": [".doc", ".docx", ".odt", ".rtf", ".xls", ".xlsx", ".ods", ".csv", ".ppt", ".pptx", ".odp"],
    "gdrive_pointer": [".gdoc", ".gsheet", ".gslides", ".gscript", ".gform", ".gdraw", ".gmap", ".gtable"],
    "shortcut": [".lnk", ".url"],
    "mindmap": [".mom", ".mm", ".xmind"],
    "text": [".txt", ".md"],
    "archive": [".zip", ".rar", ".7z", ".gz", ".tar"],
}.items():
    for _e in _exts:
        EXT_KIND[_e] = _kind

OFFLINE_ATTRS = 0x1000 | 0x400000 | 0x40000   # OFFLINE, RECALL_ON_DATA_ACCESS, RECALL_ON_OPEN

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>\u2028\u2029]+")
DOI_CUT_RE = re.compile(r"(?i)(https?://|www\.|\bPMID|\bEpub|\bPubl|\bAbstract)")
SPRINGER_RE = re.compile(r"(?i)^(s\d{5}-\d{3}-\d{3,5}-[0-9a-z])(?![0-9a-z])")
SPRINGER_PREFIXES = ["10.1007", "10.1186", "10.1038"]
BIB_HEAD_RE = re.compile(r"(?im)^\s*(Bibliografie|Bibliographie|Zitierweise|Zitierung|Zitation|Citation|"
                         r"Cite this article|How to cite)\b")
AWMF_CTX_RE = re.compile(r"(?is)(AWMF|Register(?:nummer|-?Nr)|Registernr)[^\n]{0,80}?(?<!\d)(\d{3})\s*[-/\u2013]\s*(\d{3})(?!\d)")
AWMF_NAME_RE = re.compile(r"(?<!\d)(\d{3})-(\d{3})([a-z]{0,2})(?![0-9])")
GL_CLASS_RE = re.compile(r"(?<![A-Za-z0-9])S([123])(k|e)?(?![A-Za-z0-9])")
GL_VARIANTS = [
    ("report", re.compile(r"(?i)leitlinienreport")),
    ("addendum", re.compile(r"(?i)addendum")),
    ("patient", re.compile(r"(?i)patientenleitlinie|patienteninformation")),
    ("consultation", re.compile(r"(?i)konsultationsfassung")),
    ("short", re.compile(r"(?i)kurzversion|kurzfassung|kurzleitlinie|(?<![a-z])kurz[.\s_-]")),
    ("long", re.compile(r"(?i)langversion|langfassung")),
]
IGNORED_NAMES = {"desktop.ini", "thumbs.db", ".ds_store"}     # system litter: counted, not inventoried
CARD_RE = re.compile(r"(?i)(?<![a-z])mm(?![a-z])")
MM_MARKER_RE = re.compile(r"(?i)ohne\s*mm|mm\s*fehlt|kein(?:e)?\s*mm")


def lp(path):
    """Long-path-safe form of a path on Windows."""
    if os.name != "nt":
        return path
    path = os.path.abspath(path)
    if path.startswith("\\\\?\\"):
        return path
    if path.startswith("\\\\"):
        return "\\\\?\\UNC\\" + path[2:]
    return "\\\\?\\" + path


def iso(ts):
    try:
        return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    except (OSError, OverflowError, ValueError):
        return ""


def norm_text(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def clean_doi(raw):
    d = DOI_CUT_RE.split(raw)[0]
    d = d.rstrip(".,;:)]}>'\"")
    return d.lower()


def find_dois(text):
    out = []
    for m in DOI_RE.finditer(text or ""):
        d = clean_doi(m.group(0))
        if len(d) > 8 and d not in out:
            out.append(d)
    return out


def md5_stream(path):
    h = hashlib.md5()
    with open(lp(path), "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ----------------------------------------------------------------------------- walking

def walk_tree(root):
    """Walk completely. Returns (files, folders, unreadable, skipped, ignored).
    Nothing is skipped silently: every folder that did not open and every entry that is
    neither a regular file nor a folder is listed; ignored system files are counted."""
    files, folders, unreadable, skipped = [], {}, [], []
    ignored = collections.Counter()
    stack = [root]
    while stack:
        d = stack.pop()
        rel_d = "." if d == root else os.path.relpath(d, root)
        info = folders.setdefault(rel_d, {"subfolders": 0, "files": 0, "read_ok": True, "error": ""})
        try:
            with os.scandir(lp(d)) as it:
                entries = sorted(it, key=lambda e: e.name.lower())
        except OSError as ex:
            info["read_ok"] = False
            info["error"] = "%s: %s" % (type(ex).__name__, ex)
            unreadable.append((rel_d, info["error"]))
            continue
        for e in entries:
            p = os.path.join(d, e.name)
            rel = os.path.relpath(p, root)
            try:
                is_junction = getattr(e, "is_junction", lambda: False)()
                if e.is_symlink() or is_junction:
                    skipped.append((rel, "symlink or junction (not followed)"))
                elif e.is_dir(follow_symlinks=False):
                    info["subfolders"] += 1
                    stack.append(p)
                elif e.is_file(follow_symlinks=False):
                    if e.name.lower() in IGNORED_NAMES or e.name.startswith("~$"):
                        ignored[e.name.lower() if e.name.lower() in IGNORED_NAMES else "~$*"] += 1
                        continue
                    info["files"] += 1
                    files.append(p)
                else:
                    skipped.append((rel, "neither regular file nor folder"))
            except OSError as ex:
                skipped.append((rel, "could not classify: %s" % ex))
    files.sort(key=lambda p: p.lower())
    return files, folders, unreadable, skipped, ignored


# ----------------------------------------------------------------------------- cache

class Cache:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS raw (path TEXT PRIMARY KEY, size INTEGER, "
                        "mtime_ns INTEGER, ver INTEGER, text_pages INTEGER, data TEXT)")
        self.db.execute("CREATE TABLE IF NOT EXISTS crossref (doi TEXT PRIMARY KEY, status TEXT, "
                        "data TEXT, ts TEXT)")
        self.db.commit()

    def get_raw(self, rel, size, mtime_ns, text_pages):
        r = self.db.execute("SELECT data FROM raw WHERE path=? AND size=? AND mtime_ns=? AND ver=? "
                            "AND text_pages=?", (rel, size, mtime_ns, EXTRACT_VERSION, text_pages)).fetchone()
        return json.loads(r[0]) if r else None

    def put_raw(self, rel, size, mtime_ns, text_pages, data):
        self.db.execute("INSERT OR REPLACE INTO raw VALUES (?,?,?,?,?,?)",
                        (rel, size, mtime_ns, EXTRACT_VERSION, text_pages, json.dumps(data)))
        self.db.commit()

    def get_cr(self, doi):
        r = self.db.execute("SELECT status, data FROM crossref WHERE doi=?", (doi,)).fetchone()
        return (r[0], json.loads(r[1])) if r else None

    def put_cr(self, doi, status, data):
        self.db.execute("INSERT OR REPLACE INTO crossref VALUES (?,?,?,?)",
                        (doi, status, json.dumps(data), datetime.datetime.now().isoformat(timespec="seconds")))
        self.db.commit()


# ----------------------------------------------------------------------------- PDF extraction

def extract_pdf(path, size, text_pages):
    import pymupdf
    out = {"pages": None, "encrypted": False, "meta_title": "", "meta_year": None, "chars_p12": 0,
           "landscape": False, "p12": "", "first": "", "bib": [], "error": "", "md5": None}
    try:
        if size <= 300 * 1024 * 1024:
            with open(lp(path), "rb") as f:
                data = f.read()
            out["md5"] = hashlib.md5(data).hexdigest()
            doc = pymupdf.open(stream=data, filetype="pdf")
        else:
            out["md5"] = md5_stream(path)
            doc = pymupdf.open(lp(path))
    except Exception as ex:                                  # corrupt, unreadable, offline
        out["error"] = "open: %s" % str(ex)[:200]
        if out["md5"] is None:
            try:
                out["md5"] = md5_stream(path)
            except OSError as ex2:
                out["error"] += "; md5: %s" % str(ex2)[:100]
        return out
    try:
        if doc.needs_pass:
            out["encrypted"] = True
        n = doc.page_count
        out["pages"] = n
        meta = doc.metadata or {}
        t = (meta.get("title") or "").strip()
        out["meta_title"] = t if len(t) > 8 and not re.match(r"(?i)^(microsoft word|untitled|unbenannt)", t) else ""
        m = re.search(r"((?:19|20)\d{2})", meta.get("creationDate") or "")
        out["meta_year"] = int(m.group(1)) if m else None
        if n and not out["encrypted"]:
            r0 = doc[0].rect
            out["landscape"] = r0.width > r0.height
            p12, first, bib = [], [], []
            for i in range(min(n, max(40, text_pages))):
                try:
                    t = doc[i].get_text("text") or ""
                except Exception:
                    t = ""
                if i < 2:
                    p12.append(t)
                if i < text_pages:
                    first.append(t)
                if i < 40:
                    for mh in BIB_HEAD_RE.finditer(t):
                        if len(bib) < 6:
                            bib.append(t[mh.start():mh.start() + 700])
            out["p12"] = "\n\f".join(p12)[:12000]
            out["first"] = "\n\f".join(first)[:40000]
            out["bib"] = bib
            out["chars_p12"] = len(re.sub(r"\s", "", out["p12"]))
    except Exception as ex:
        out["error"] = "parse: %s" % str(ex)[:200]
    finally:
        doc.close()
    return out


def ocr_pdf(path, pages, tess):
    """OCR the first pages with Tesseract (deu+eng). Returns (text, error)."""
    import pymupdf
    try:
        with open(lp(path), "rb") as f:
            doc = pymupdf.open(stream=f.read(), filetype="pdf")
    except Exception as ex:
        return "", "ocr open: %s" % str(ex)[:150]
    parts, err = [], ""
    with tempfile.TemporaryDirectory() as td:
        for i in range(min(doc.page_count, pages)):
            img = os.path.join(td, "p%d.png" % i)
            try:
                doc[i].get_pixmap(dpi=250).save(img)
                r = subprocess.run([tess, img, "stdout", "-l", "deu+eng"], capture_output=True,
                                   timeout=300)
                parts.append(r.stdout.decode("utf-8", "replace"))
                if r.returncode != 0 and not r.stdout:
                    err = "tesseract rc=%d: %s" % (r.returncode, r.stderr.decode("utf-8", "replace")[:120])
            except Exception as ex:
                err = "ocr page %d: %s" % (i + 1, str(ex)[:120])
    doc.close()
    return "\n\f".join(parts)[:40000], err


# ----------------------------------------------------------------------------- CrossRef

class Crossref:
    def __init__(self, cache, email):
        self.cache, self.email = cache, email
        self.requests = 0
        self.last = 0.0

    def get(self, doi):
        hit = self.cache.get_cr(doi)
        if hit:
            return hit[0], hit[1]
        url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
        if self.email:
            url += "?mailto=" + urllib.parse.quote(self.email)
        ua = "archive_scan/%s%s" % (VERSION, " (mailto:%s)" % self.email if self.email else "")
        status, data = "error", {}
        for attempt in range(4):
            wait = 0.12 - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            self.requests += 1
            try:
                req = urllib.request.Request(url, headers={"User-Agent": ua})
                with urllib.request.urlopen(req, timeout=30) as r:
                    msg = json.loads(r.read().decode("utf-8"))["message"]
                status, data = "ok", self._parse(msg)
                break
            except urllib.error.HTTPError as ex:
                if ex.code == 404:
                    status = "not_found"
                    break
                time.sleep(float(ex.headers.get("Retry-After") or 2 * (attempt + 1)) if ex.code == 429
                           else 2 * (attempt + 1))
            except Exception:
                time.sleep(2 * (attempt + 1))
        if status in ("ok", "not_found"):
            self.cache.put_cr(doi, status, data)
        return status, data

    @staticmethod
    def _parse(msg):
        title = " ".join((msg.get("title") or [""])[:1] + (msg.get("subtitle") or [])[:1]).strip()
        authors = []
        for a in msg.get("author") or []:
            nm = " ".join(x for x in (a.get("family"), a.get("given")) if x) or a.get("name", "")
            if nm:
                authors.append(nm)
        year = None
        for key in ("issued", "published-print", "published-online", "published"):
            dp = (msg.get(key) or {}).get("date-parts") or [[None]]
            if dp[0] and dp[0][0]:
                year = int(dp[0][0])
                break
        return {"title": title, "authors": authors, "journal": (msg.get("container-title") or [""])[0],
                "year": year, "type": msg.get("type", "")}


# ----------------------------------------------------------------------------- derivations

def doi_candidates(name, raw):
    """[(doi, source)] in priority order: file name, citation box, first two pages."""
    c = []
    stem = os.path.splitext(name)[0]
    m = SPRINGER_RE.match(stem)
    if m:
        c.append(("10.1007/" + m.group(1).lower(), "filename-springer"))
    for d in find_dois(name.replace("_", "/") if "10.1" in name else ""):
        c.append((d, "filename"))
    for snip in raw.get("bib") or []:
        for d in find_dois(snip):
            c.append((d, "bib-box"))
    for d in find_dois(raw.get("p12", "") + "\n" + raw.get("ocr", "")):
        c.append((d, "pages1-2"))
    seen, out = set(), []
    for d, s in c:
        if d not in seen:
            seen.add(d)
            out.append((d, s))
    return out


def awmf_info(name, text):
    """(awmf_nr, source, class, variant)"""
    nr, src = "", ""
    m = AWMF_CTX_RE.search(text or "")
    if m:
        nr, src = "%s-%s" % (m.group(2), m.group(3)), "text"
    else:
        m = AWMF_NAME_RE.search(name)
        if m and (name.startswith(m.group(0)) or re.search(r"(?i)awmf|leitlinie|\bS[123][ke]?\b|\bLL\b", name)):
            nr, src = "%s-%s" % (m.group(1), m.group(2)), "filename"
    head = name + "\n" + (text or "")[:2000]
    cm = GL_CLASS_RE.search(head)
    gclass = ("S" + cm.group(1) + (cm.group(2) or "")) if cm else ""
    variant = ""
    for v, rx in GL_VARIANTS:
        if rx.search(head):
            variant = v
            break
    return nr, src, gclass, variant or ("unspecified" if nr else "")


def year_info(rel, name, raw, cr_year, doi_list):
    """(year, source, 'src:year;...')"""
    ok = lambda y: 1950 <= y <= NOW_YEAR + 1
    cand = []
    if cr_year and ok(cr_year):
        cand.append(("crossref", cr_year))
    text = (raw.get("p12") or "") + "\n" + (raw.get("ocr") or "")
    for src, rx in (("text-published", r"(?i)(?:published|publiziert|erschienen|online\s+ver[oö]ffentlicht)[^\n]{0,40}?((?:19|20)\d{2})"),
                    ("text-stand", r"(?i)(?:stand|aktueller\s+stand|letzte\s+aktualisierung)[:\s]{0,3}[^\n]{0,25}?((?:19|20)\d{2})"),
                    ("text-copyright", r"(?i)(?:\u00a9|\(c\)|copyright)\s*[^\n]{0,30}?((?:19|20)\d{2})"),
                    ("text-valid-until", r"(?i)g[uü]ltig\s+bis[^\n]{0,25}?((?:19|20)\d{2})")):
        m = re.search(rx, text)
        if m and ok(int(m.group(1))):
            cand.append((src, int(m.group(1))))
    stem = os.path.splitext(name)[0]
    m = re.search(r"(?<!\d)((?:19|20)\d{2})(?:0[1-9]|1[0-2])(?:[0-3]\d)(?!\d)", stem)
    if m and ok(int(m.group(1))):
        cand.append(("filename-date", int(m.group(1))))
    m = re.search(r"(?i)CME\s*\d{1,2}[.\-/](\d{2})(?!\d)", stem)
    cme_year = 2000 + int(m.group(1)) if m else None
    for m in re.finditer(r"(?<!\d)((?:19|20)\d{2})(?!\d)", stem):
        if ok(int(m.group(1))):
            cand.append(("filename", int(m.group(1))))
            break
    for d, _s in doi_list:
        m = re.match(r"10\.\d+/s\d{5}-(\d{3})-", d)
        if m and ok(2000 + int(m.group(1)) % 100):
            cand.append(("doi-springer", 2000 + int(m.group(1)) % 100))
            break
    parts = rel.replace("\\", "/").split("/")[:-1]
    for part in reversed(parts):
        m = re.search(r"(?<!\d)((?:19|20)\d{2})(?!\d)", part)
        if m and ok(int(m.group(1))):
            cand.append(("folder", int(m.group(1))))
            break
    if cme_year and ok(cme_year):
        cand.append(("filename-cme-cycle", cme_year))
    if raw.get("meta_year") and ok(raw["meta_year"]):
        cand.append(("pdf-metadata", raw["meta_year"]))
    first = (raw.get("p12") or "").split("\f")[0]
    ys = [int(y) for y in re.findall(r"(?<!\d)((?:19|20)\d{2})(?!\d)", first) if 1990 <= int(y) <= NOW_YEAR + 1]
    if ys:
        cand.append(("text-firstpage-most-common", collections.Counter(ys).most_common(1)[0][0]))
    # the order of appending is the priority order, except that cme-cycle sits below folder
    allc = ";".join("%s:%d" % c for c in cand)
    return (cand[0][1], cand[0][0], allc) if cand else ("", "", "")


def classify(name, ext, kind, raw, dois, awmf_nr, pages):
    """(doc_type, rule). First matching rule wins; the rule is reported."""
    if kind != "pdf":
        return {"video": ("video", "ext:" + ext), "audio": ("audio", "ext:" + ext),
                "image": ("image", "ext:" + ext), "gdrive_pointer": ("gdrive_pointer", "ext:" + ext),
                "shortcut": ("shortcut", "ext:" + ext), "mindmap": ("mindmap_card", "ext:" + ext),
                "archive": ("archive", "ext:" + ext), "text": ("text", "ext:" + ext),
                "office": ("office_document", "ext:" + ext)}.get(kind, ("other", "ext:" + ext))
    stem = os.path.splitext(name)[0]
    text = (raw.get("p12") or "") + "\n" + (raw.get("ocr") or "")
    low = text.lower()
    if CARD_RE.search(MM_MARKER_RE.sub("", stem)):
        return "mindmap_card", "name:MM"
    if awmf_nr and re.search(r"(?i)awmf", low):
        return "guideline", "text:AWMF-register-number"
    if re.search(r"(?i)leitlinie|guideline", stem) or (awmf_nr and AWMF_NAME_RE.match(stem)):
        return "guideline", "name:Leitlinie/AWMF-number"
    if re.search(r"(?i)zertifikat|teilnahmebescheinigung|bescheinigung|certificate", stem) or \
            re.search(r"(?i)teilnahmebescheinigung|zertifikat", low[:1500]):
        return "certificate", "name-or-text:Zertifikat"
    if re.search(r"(?i)\bCME\b", stem) or re.search(r"(?i)kernaussagen|cme-punkte|zertifizierte fortbildung|cme-fortbildung", low):
        return "cme_article", "name-or-text:CME"
    if raw.get("landscape") and pages and pages <= 80 and not dois:
        return "presentation", "layout:landscape-no-doi"
    if dois or (re.search(r"(?i)\babstract\b", low) and re.search(r"(?i)\b(introduction|methods|einleitung|methodik)\b", low)):
        return "journal_article", "doi-or-abstract"
    if re.search(r"(?i)\b(sop|standard|verfahrensanweisung|algorithmus|checkliste)\b", stem):
        return "sop_standard", "name:SOP/Standard"
    if pages and pages >= 120:
        return "book", "pages>=120"
    if raw.get("chars_p12", 0) < 50 and not raw.get("ocr"):
        return "scan_no_text", "no-text-layer"
    return "other_pdf", "default"


def belongs(cr_title, raw, name):
    """Does the CrossRef title occur in the file's own first pages? yes / maybe / no / unknown"""
    pool_src = "%s %s %s %s" % (raw.get("p12", ""), raw.get("ocr", ""), raw.get("meta_title", ""), name)
    pool = set(w for w in norm_text(pool_src).split() if len(w) >= 4)
    words = set(w for w in norm_text(cr_title).split() if len(w) >= 4)
    if len(words) < 2 or len(pool) < 5:
        return "unknown"
    frac = len(words & pool) / float(len(words))
    return "yes" if frac >= 0.7 else "maybe" if frac >= 0.4 else "no"


def title_nums(name):
    """Digit tokens of the file name apart from years/dates: 'Seite 2 3' differs from 'Seite 4 5'."""
    s = re.sub(r"(?i)\b(kopie|copy|kopia)\b|\(\d+\)", " ", os.path.splitext(name)[0])
    s = re.sub(r"(?<!\d)(?:19|20)\d{2}[-._]?\d{0,2}[-._]?\d{0,2}(?!\d)", " ", s)
    return tuple(re.findall(r"\d+", s))


def title_key(name, cr_title):
    # the PDF metadata title is not used: chapters of one book share it
    if cr_title:
        return norm_text(cr_title)
    s = os.path.splitext(name)[0]
    s = re.sub(r"(?i)\b(kopie|copy|kopia)\b|\(\d+\)", " ", s)
    s = re.sub(r"(?<!\d)(?:19|20)\d{2}[-._]?\d{0,2}[-._]?\d{0,2}(?!\d)", " ", s)
    return norm_text(s)


def art_key(stem):
    s = MM_MARKER_RE.sub(" ", stem)
    s = CARD_RE.sub(" ", s)
    return norm_text(s)


# ----------------------------------------------------------------------------- main

FILE_COLS = ["path", "folder", "name", "ext", "kind", "size", "created", "modified", "online_only", "md5",
             "doc_type", "doc_type_rule", "pages", "text_layer", "ocr_done", "encrypted",
             "doi", "doi_source", "doi_candidates", "doi_belongs", "crossref_status",
             "crossref_authors", "crossref_journal", "crossref_year", "crossref_title",
             "awmf_nr", "awmf_source", "guideline_class", "guideline_variant",
             "year", "year_source", "year_candidates", "mm_status", "mm_card",
             "dup_copy_group", "dup_doi_group", "dup_title_group", "title_key", "text_file", "error"]


def parse_args():
    ap = argparse.ArgumentParser(description="Inventory of a document archive (archive_scan %s)." % VERSION)
    ap.add_argument("root", help="folder to scan")
    ap.add_argument("--out", required=True, help="folder for the outputs (NOT inside a git repo)")
    ap.add_argument("--crossref", action="store_true", help="authors, journal, year, title by DOI from CrossRef")
    ap.add_argument("--email", default=os.environ.get("CROSSREF_EMAIL", ""),
                    help="e-mail for the CrossRef polite pool (or env CROSSREF_EMAIL); never put it in the code")
    ap.add_argument("--ocr", action="store_true", help="OCR (Tesseract deu+eng) of the first pages of scans")
    ap.add_argument("--tesseract", default="", help="path to tesseract(.exe) if not in PATH")
    ap.add_argument("--save-text", action="store_true", help="save the text of the first pages into OUT/texts")
    ap.add_argument("--text-pages", type=int, default=3, help="how many first pages to save / OCR (default 3)")
    ap.add_argument("--hash-video", action="store_true", help="also compute md5 of video files (slow)")
    return ap.parse_args()


def find_tesseract(explicit):
    cands = [explicit] if explicit else []
    cands += [shutil.which("tesseract") or "", r"C:\Program Files\Tesseract-OCR\tesseract.exe",
              r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"]
    for c in cands:
        if c and os.path.isfile(c):
            return c
    return ""


def main():
    a = parse_args()
    root = os.path.abspath(a.root)
    if not os.path.isdir(lp(root)):
        sys.exit("Root folder does not exist or does not open: %s" % root)
    os.makedirs(a.out, exist_ok=True)
    out = os.path.abspath(a.out)
    if os.path.commonpath([out, root]) == root:
        print("WARNING: --out lies inside the scanned folder; its own outputs will be scanned next time.")
    try:
        import pymupdf  # noqa: F401
    except ImportError:
        sys.exit("PyMuPDF is missing: pip install pymupdf")
    tess = ""
    if a.ocr:
        tess = find_tesseract(a.tesseract)
        if not tess:
            sys.exit("--ocr needs Tesseract (not found). Install it with the German language or pass --tesseract.")
        langs = subprocess.run([tess, "--list-langs"], capture_output=True).stdout.decode("utf-8", "replace")
        missing = [l for l in ("deu", "eng") if l not in langs.split()]
        if missing:
            sys.exit("Tesseract lacks language data: %s" % ", ".join(missing))
    if a.crossref and not a.email:
        print("NOTE: --crossref without --email works but is slower; pass --email you@example.org.")
    text_dir = os.path.join(out, "texts")
    if a.save_text:
        os.makedirs(text_dir, exist_ok=True)

    t0 = time.time()
    cache = Cache(os.path.join(out, "scan_cache.sqlite"))
    print("Walking %s ..." % root)
    files, folders, unreadable, skipped, ignored = walk_tree(root)
    print("%d files in %d folders; %d folders did not open." % (len(files), len(folders), len(unreadable)))

    # ---- stage 1: per-file raw data (cached)
    raws, stats = {}, collections.Counter()
    for i, p in enumerate(files, 1):
        rel = os.path.relpath(p, root)
        ext = os.path.splitext(p)[1].lower()
        kind = EXT_KIND.get(ext, "other")
        if i % 25 == 0 or i == len(files):
            el = time.time() - t0
            sys.stderr.write("\r[%d/%d] %.0fs, ETA %.0fs   " % (i, len(files), el, el / i * (len(files) - i)))
            sys.stderr.flush()
        try:
            st = os.stat(lp(p))
        except OSError as ex:
            raws[rel] = {"kind": kind, "ext": ext, "size": 0, "mtime_ns": 0, "stat_error": str(ex)[:150]}
            continue
        raw = cache.get_raw(rel, st.st_size, st.st_mtime_ns, a.text_pages)
        stats["cache_hit" if raw else "cache_miss"] += 1
        if raw is None:
            raw = {}
            if kind == "pdf":
                raw = extract_pdf(p, st.st_size, a.text_pages)
            elif (kind == "video" and not a.hash_video) or kind == "gdrive_pointer":
                raw = {"md5": None}      # video: slow; Drive pointers (.gdoc...) cannot be read as files
            else:
                try:
                    raw = {"md5": md5_stream(p)}
                except OSError as ex:
                    raw = {"md5": None, "error": "md5: %s" % str(ex)[:150]}
        if kind == "gdrive_pointer":
            raw = {"md5": None}
        if kind == "video" and a.hash_video and raw.get("md5") is None:
            try:
                raw["md5"] = md5_stream(p)
            except OSError as ex:
                raw["error"] = "md5: %s" % str(ex)[:150]
        if kind == "pdf" and a.ocr and raw.get("chars_p12", 1 << 30) < 50 and not raw.get("encrypted") \
                and "ocr" not in raw and raw.get("pages"):
            raw["ocr"], err = ocr_pdf(p, a.text_pages, tess)
            if err:
                raw["error"] = (raw.get("error", "") + "; " + err).strip("; ")
            stats["ocr_run"] += 1
        cache.put_raw(rel, st.st_size, st.st_mtime_ns, a.text_pages, raw)
        raw.update({"kind": kind, "ext": ext, "size": st.st_size, "mtime_ns": st.st_mtime_ns,
                    "ctime": st.st_ctime, "mtime": st.st_mtime,
                    "attrs": getattr(st, "st_file_attributes", 0)})
        raws[rel] = raw
    sys.stderr.write("\n")

    # ---- mind-map card index per folder
    by_folder = collections.defaultdict(list)
    for rel, raw in raws.items():
        name = os.path.basename(rel)
        stem = os.path.splitext(name)[0]
        is_card = raw["ext"] == ".mom" or (raw["kind"] in ("pdf", "image", "mindmap") and
                                           bool(CARD_RE.search(MM_MARKER_RE.sub("", stem))))
        by_folder[os.path.dirname(rel)].append((name, art_key(stem), is_card))

    # ---- stage 2: CrossRef
    cr = Crossref(cache, a.email) if a.crossref else None
    rows = []
    for rel in sorted(raws, key=str.lower):
        raw = raws[rel]
        name = os.path.basename(rel)
        folder = os.path.dirname(rel) or "."
        kind, ext = raw["kind"], raw["ext"]
        r = dict.fromkeys(FILE_COLS, "")
        r.update(path=rel, folder=folder, name=name, ext=ext, kind=kind, size=raw["size"],
                 created=iso(raw.get("ctime", 0)), modified=iso(raw.get("mtime", 0)),
                 online_only="yes" if raw.get("attrs", 0) & OFFLINE_ATTRS else "",
                 md5=raw.get("md5") or "", error=(raw.get("stat_error") or "") + (raw.get("error") or ""))
        pages = raw.get("pages")
        dois = doi_candidates(name, raw) if kind == "pdf" else []
        text_for_awmf = (raw.get("p12") or "") + "\n" + (raw.get("ocr") or "")
        if kind == "pdf":
            nr, nsrc, gclass, gvar = awmf_info(name, text_for_awmf)
            r.update(awmf_nr=nr, awmf_source=nsrc, guideline_class=gclass, guideline_variant=gvar)
            r.update(pages=pages if pages is not None else "", encrypted="yes" if raw.get("encrypted") else "",
                     text_layer="no" if raw.get("chars_p12", 0) < 50 else "yes",
                     ocr_done="yes" if raw.get("ocr") else "")
        # chosen DOI
        chosen, csrc, cr_data, cr_status, bel = "", "", {}, "", ""
        if dois:
            r["doi_candidates"] = ";".join(d for d, _s in dois)
            if cr:
                tried = 0
                best = None
                for d, s in dois:
                    if tried >= 3:
                        break
                    variants = [d]
                    if s == "filename-springer":
                        stem_ = d.split("/", 1)[1]
                        variants = [pre + "/" + stem_ for pre in SPRINGER_PREFIXES]
                    for v in variants:
                        status, data = cr.get(v)
                        tried += 1
                        b = belongs(data["title"], raw, name) if status == "ok" else ""
                        if best is None:
                            best = (v, s, status, data, b)
                        if status == "ok" and b in ("yes", "maybe"):
                            best = (v, s, status, data, b)
                            break
                        if status == "ok" and best[2] != "ok":
                            best = (v, s, status, data, b)
                    if best and best[4] in ("yes", "maybe"):
                        break
                chosen, csrc, cr_status, cr_data, bel = best[0], best[1], best[2], best[3], best[4]
                if cr_status == "not_found":
                    bel = "not_found"
            else:
                chosen, csrc = dois[0]
                bel = "not_checked"
                if csrc == "filename-springer":
                    csrc = "filename-springer(prefix guessed)"
            r.update(doi=chosen, doi_source=csrc, doi_belongs=bel, crossref_status=cr_status)
            if cr_data:
                r.update(crossref_authors="; ".join(cr_data["authors"][:12]) + ("; et al." if len(cr_data["authors"]) > 12 else ""),
                         crossref_journal=cr_data["journal"], crossref_year=cr_data["year"] or "",
                         crossref_title=cr_data["title"])
        use_cr_year = cr_data.get("year") if bel in ("yes", "maybe") else None
        y, ysrc, ycand = year_info(rel, name, raw, use_cr_year, dois)
        r.update(year=y, year_source=ysrc, year_candidates=ycand)
        dt, rule = classify(name, ext, kind, raw, [d for d, _s in dois] if bel != "no" else [],
                            r["awmf_nr"], pages)
        r.update(doc_type=dt, doc_type_rule=rule)
        # mind-map status
        stem = os.path.splitext(name)[0]
        if kind == "pdf" and dt != "mindmap_card":
            key = art_key(stem)
            cards = [(n, k) for (n, k, ic) in by_folder.get(os.path.dirname(rel), []) if ic]
            match = [n for (n, k) in cards if k and key and (k == key or
                                                             (min(len(k), len(key)) >= 8 and (k.startswith(key) or key.startswith(k))))]
            if not match and cards:
                arts = [n for (n, k, ic) in by_folder.get(os.path.dirname(rel), []) if not ic and n.lower().endswith(".pdf")]
                if len(arts) == 1:
                    match = [cards[0][0]]
            if match:
                r.update(mm_status="done", mm_card=match[0])
            elif MM_MARKER_RE.search(rel):
                r["mm_status"] = "missing"
            else:
                r["mm_status"] = "none"
        elif dt == "mindmap_card":
            r["mm_status"] = "card"
        else:
            r["mm_status"] = "n/a"
        r["title_key"] = title_key(name, r["crossref_title"]) if kind == "pdf" else ""
        r["_nums"] = () if r["crossref_title"] else title_nums(name)
        # saved text
        if a.save_text and kind == "pdf" and (raw.get("first") or raw.get("ocr")) and raw.get("md5"):
            tname = "%s__%s.txt" % (raw["md5"][:12], re.sub(r'[^\w\-. ]+', "_", os.path.splitext(name)[0])[:60])
            body = raw.get("first") or ""
            if raw.get("ocr"):
                body = (body + "\n\f[OCR]\n" + raw["ocr"]).strip()
            with open(os.path.join(text_dir, tname), "w", encoding="utf-8") as f:
                f.write("# path: %s\n# first %d pages\n\n%s\n" % (rel, a.text_pages, body))
            r["text_file"] = tname
        rows.append(r)
    if cr:
        print("CrossRef: %d requests this run." % cr.requests)

    # ---- duplicates
    groups = []                                   # (kind, group_id, [rows], similarity)
    by_md5 = collections.defaultdict(list)
    for r in rows:
        if r["md5"]:
            by_md5[r["md5"]].append(r)
    n = 0
    for md5, rs in by_md5.items():
        if len(rs) > 1:
            n += 1
            gid = "C%03d" % n
            for r in rs:
                r["dup_copy_group"] = gid
            groups.append(("copy", gid, rs, "1.00"))
    by_doi = collections.defaultdict(list)
    for r in rows:
        if r["doi"] and r["doi_belongs"] not in ("no", "not_found"):
            by_doi[r["doi"]].append(r)
    n = 0
    for doi, rs in by_doi.items():
        if len({x["md5"] for x in rs}) > 1:
            n += 1
            gid = "D%03d" % n
            for r in rs:
                r["dup_doi_group"] = gid
            groups.append(("same_doi", gid, rs, ""))
    pdfs = [r for r in rows if r["kind"] == "pdf" and r["pages"] != "" and len(r["title_key"]) >= 12]
    pdfs.sort(key=lambda r: int(r["pages"]))
    pairs = []
    for i, r in enumerate(pdfs):
        for s in pdfs[i + 1:]:
            if int(s["pages"]) - int(r["pages"]) > 2:
                break
            if r["md5"] == s["md5"] or (r["doi"] and r["doi"] == s["doi"]) or r["_nums"] != s["_nums"]:
                continue
            sm = difflib.SequenceMatcher(None, r["title_key"], s["title_key"])
            if sm.real_quick_ratio() >= 0.9 and sm.quick_ratio() >= 0.9 and sm.ratio() >= 0.9:
                pairs.append((r, s, sm.ratio()))
    parent = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for r, s, _ in pairs:
        parent[find(r["path"])] = find(s["path"])
    comp = collections.defaultdict(list)
    byp = {r["path"]: r for r in rows}
    sims = {}
    for r, s, ratio in pairs:
        sims[r["path"]] = max(sims.get(r["path"], 0), ratio)
        sims[s["path"]] = max(sims.get(s["path"], 0), ratio)
    for pth in list(parent):
        comp[find(pth)].append(byp[pth])
    n = 0
    for rs in comp.values():
        if len(rs) > 1:
            n += 1
            gid = "T%03d" % n
            for r in rs:
                r["dup_title_group"] = gid
            groups.append(("similar_title", gid, rs, "%.2f" % min(sims[r["path"]] for r in rs)))

    # ---- guidelines
    gl_rows = []
    gl = [r for r in rows if r["doc_type"] == "guideline" or r["awmf_nr"]]
    grp = collections.defaultdict(list)
    for r in gl:
        grp[(r["awmf_nr"], r["guideline_variant"])].append(r)
    for (nr, var), rs in sorted(grp.items()):
        years = [int(x["year"]) for x in rs if x["year"] != ""]
        newest = max(years) if years else None
        for r in sorted(rs, key=lambda x: (-(int(x["year"]) if x["year"] != "" else 0), x["path"])):
            if not r["year"]:
                st_ = "unknown_year"
            elif len({x["md5"] for x in rs}) == 1:
                st_ = "single_version"
            elif int(r["year"]) == newest:
                st_ = "newest"
            else:
                st_ = "older"
            gl_rows.append({"awmf_nr": nr, "guideline_class": r["guideline_class"], "variant": var,
                            "year": r["year"], "year_source": r["year_source"], "version_status": st_,
                            "versions_in_group": len(rs), "title": r["crossref_title"] or r["title_key"],
                            "md5": r["md5"], "dup_copy_group": r["dup_copy_group"], "path": r["path"]})

    # ---- outputs
    def write_csv(fname, cols, data):
        with open(os.path.join(out, fname), "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(data)

    write_csv("files.csv", FILE_COLS, rows)
    tot_sz, tot_files, per_folder = collections.Counter(), collections.Counter(), collections.defaultdict(int)
    for r in rows:
        parts = [] if r["folder"] == "." else r["folder"].replace("\\", "/").split("/")
        for k in range(len(parts) + 1):
            key = "." if k == 0 else "/".join(parts[:k])
            tot_files[key] += 1
            tot_sz[key] += int(r["size"] or 0)
    frows = []
    for rel_d, info in sorted(folders.items(), key=lambda kv: kv[0].lower()):
        frows.append({"path": rel_d, "depth": 0 if rel_d == "." else rel_d.replace("\\", "/").count("/") + 1,
                      "files_direct": info["files"], "subfolders": info["subfolders"],
                      "files_total": tot_files.get(rel_d.replace("\\", "/"), 0),
                      "size_total": tot_sz.get(rel_d.replace("\\", "/"), 0),
                      "read_ok": "yes" if info["read_ok"] else "NO", "error": info["error"]})
    write_csv("folders.csv", ["path", "depth", "files_direct", "subfolders", "files_total", "size_total",
                              "read_ok", "error"], frows)
    write_csv("guidelines.csv", ["awmf_nr", "guideline_class", "variant", "year", "year_source", "version_status",
                                 "versions_in_group", "title", "md5", "dup_copy_group", "path"], gl_rows)
    dup_rows = []
    for kind_, gid, rs, sim in groups:
        for r in rs:
            dup_rows.append({"dup_kind": kind_, "group": gid, "similarity": sim, "path": r["path"],
                             "size": r["size"], "pages": r["pages"], "md5": r["md5"], "doi": r["doi"],
                             "year": r["year"], "title_key": r["title_key"]})
    write_csv("duplicates.csv", ["dup_kind", "group", "similarity", "path", "size", "pages", "md5", "doi",
                                 "year", "title_key"], dup_rows)

    # ---- summary
    L = []
    pdf_rows = [r for r in rows if r["kind"] == "pdf"]
    L.append("archive_scan %s - summary" % VERSION)
    L.append("run: %s, %.0f s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), time.time() - t0))
    L.append("root: %s" % root)
    L.append("options: crossref=%s ocr=%s save_text=%s text_pages=%d hash_video=%s" %
             (a.crossref, a.ocr, a.save_text, a.text_pages, a.hash_video))
    L.append("")
    L.append("FOLDERS THAT COULD NOT BE READ")
    if unreadable:
        L.append("!!! THE WALK IS NOT COMPLETE - %d folder(s) did not open; files inside them are NOT in the inventory:" % len(unreadable))
        for p_, e_ in unreadable:
            L.append("  %s  [%s]" % (p_, e_))
    else:
        L.append("(none)")
    L.append("")
    L.append("ENTRIES SKIPPED (not followed / not classified)")
    L.extend(["  %s  [%s]" % s_ for s_ in skipped] or ["(none)"])
    L.append("")
    L.append("IGNORED SYSTEM FILES (not in the inventory): " +
             (", ".join("%s %d" % kv for kv in ignored.most_common()) or "(none)"))
    L.append("")
    L.append("TOTALS")
    L.append("files: %d   folders: %d   total size: %.2f GB" % (len(rows), len(folders), sum(int(r["size"] or 0) for r in rows) / 1e9))
    L.append("pdf: %d   scans without text layer: %d   OCR done: %d   encrypted: %d" % (
        len(pdf_rows), sum(1 for r in pdf_rows if r["text_layer"] == "no"),
        sum(1 for r in pdf_rows if r["ocr_done"] == "yes"), sum(1 for r in pdf_rows if r["encrypted"])))
    L.append("online-only (not downloaded) files: %d" % sum(1 for r in rows if r["online_only"]))
    L.append("by kind: " + ", ".join("%s %d" % kv for kv in collections.Counter(r["kind"] for r in rows).most_common()))
    L.append("by extension: " + ", ".join("%s %d" % kv for kv in collections.Counter(r["ext"] or "(none)" for r in rows).most_common(25)))
    L.append("cache: %d hits, %d misses" % (stats["cache_hit"], stats["cache_miss"]))
    L.append("")
    L.append("FIRST-LEVEL FOLDERS (files in total)")
    for rel_d in sorted((k for k in folders if k != "." and os.sep not in k and "/" not in k), key=str.lower):
        L.append("  %-40s %5d" % (rel_d, tot_files.get(rel_d, 0)))
    L.append("  %-40s %5d" % ("(files directly in root)", folders["."]["files"] if "." in folders else 0))
    L.append("")
    L.append("DOI")
    dset = {r["doi"] for r in pdf_rows if r["doi"]}
    L.append("pdf with a DOI: %d   distinct DOIs: %d   by source: %s" % (
        sum(1 for r in pdf_rows if r["doi"]), len(dset),
        ", ".join("%s %d" % kv for kv in collections.Counter(r["doi_source"] for r in pdf_rows if r["doi"]).most_common())))
    if a.crossref:
        ok_ = {r["doi"] for r in pdf_rows if r["crossref_status"] == "ok"}
        L.append("CrossRef: distinct DOIs found there: %d   not found: %d   request errors: %d" % (
            len(ok_), len({r["doi"] for r in pdf_rows if r["crossref_status"] == "not_found"}),
            sum(1 for r in pdf_rows if r["doi"] and r["crossref_status"] == "error")))
        L.append("DOI belongs to its file: " + ", ".join("%s %d" % kv for kv in collections.Counter(
            r["doi_belongs"] for r in pdf_rows if r["doi"]).most_common()))
    L.append("")
    L.append("DOCUMENT TYPES (type: count; main rules)")
    for t_, c_ in collections.Counter(r["doc_type"] for r in rows).most_common():
        rules = collections.Counter(r["doc_type_rule"] for r in rows if r["doc_type"] == t_).most_common(3)
        L.append("  %-16s %4d   %s" % (t_, c_, ", ".join("%s %d" % x for x in rules)))
    L.append("")
    L.append("YEAR SOURCES (pdf)")
    L.append("  " + ", ".join("%s %d" % kv for kv in collections.Counter(r["year_source"] or "(no year)" for r in pdf_rows).most_common()))
    L.append("")
    L.append("GUIDELINES")
    awmf = {r["awmf_nr"] for r in gl if r["awmf_nr"]}
    multi = collections.Counter()
    for (nr, var), rs in grp.items():
        if nr and len({x["md5"] for x in rs}) > 1:
            multi[nr] += 1
    L.append("files typed guideline or with AWMF number: %d   AWMF numbers: %d   with several versions: %d" % (
        len(gl), len(awmf), len(multi)))
    L.append("")
    L.append("MIND-MAP STATUS (pdf): " + ", ".join("%s %d" % kv for kv in collections.Counter(r["mm_status"] for r in pdf_rows).most_common()))
    L.append("")
    L.append("DUPLICATES")
    for k_ in ("copy", "same_doi", "similar_title"):
        gs = [g for g in groups if g[0] == k_]
        L.append("  %-14s groups %d, files %d" % (k_, len(gs), sum(len(g[2]) for g in gs)))
    errs = [r for r in rows if r["error"]]
    L.append("")
    L.append("FILES WITH ERRORS: %d" % len(errs))
    for r in errs[:60]:
        L.append("  %s  [%s]" % (r["path"], r["error"][:160]))
    with open(os.path.join(out, "summary.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    print("Done: %s" % out)
    if unreadable:
        print("\n!!! %d FOLDER(S) COULD NOT BE READ - the inventory is NOT complete. See summary.txt." % len(unreadable))
        sys.exit(2)


if __name__ == "__main__":
    main()
