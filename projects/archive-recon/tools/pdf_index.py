"""pdf_index.py — полнотекстовый индекс и оглавления PDF архива (archive-recon, 2026-10-13, запись Р-32 журнала LOG.md).

Где работает: на сервере владельца, над зеркалом папки Google Диска (rclone, только чтение). Ничего в зеркале не меняет.
Что делает с каждым PDF:
  1) md5 содержимого (тот же ключ, что у страницы поиска и у отметок владельца);
  2) число страниц, закладки PDF (оглавление: уровень, название, страница PDF), печатные метки страниц (page labels), если они есть;
  3) текст КАЖДОЙ страницы — в базу SQLite с полнотекстовым поиском FTS5 (таблица pages: md5, page, body);
  4) список страниц без текстового слоя (меньше 20 знаков) — кандидаты на распознавание сервисом OCR.
Выход (папка --out, вне репозитория: там чужие тексты и личные пути):
  fulltext.sqlite       — база поиска (таблица pages FTS5 + таблица files);
  outlines.json         — {md5: {path, pages, toc, labels_sample, notext_pages, chars}} — оглавления для сборки книг;
  index_report.json     — сводка: файлов, ошибок, страниц, страниц без текста, время.
Повторный запуск пропускает файлы, у которых совпали путь, размер и время изменения (таблица files).
Запуск:
  python3 pdf_index.py build  --root /srv/archive/aa-beruf --out /srv/archive/index
  python3 pdf_index.py search --out /srv/archive/index "tranexam*" --limit 20
  python3 pdf_index.py export --out /srv/archive/index        # пересобрать outlines.json из базы
Нужно: Python 3.8+, PyMuPDF (pip install pymupdf), SQLite с FTS5 (есть в стандартном python3 Debian/Ubuntu).
"""
import argparse, hashlib, json, os, sqlite3, sys, time

NOTEXT_CHARS = 20


def md5_of(path, buf=8 * 1024 * 1024):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def open_db(out):
    os.makedirs(out, exist_ok=True)
    db = sqlite3.connect(os.path.join(out, 'fulltext.sqlite'))
    db.execute("CREATE TABLE IF NOT EXISTS files(path TEXT PRIMARY KEY, size INTEGER, mtime REAL, md5 TEXT, pages INTEGER,"
               " toc TEXT, labels TEXT, notext TEXT, chars INTEGER, error TEXT, indexed_at TEXT)")
    db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS pages USING fts5(md5 UNINDEXED, page UNINDEXED, body,"
               " tokenize='unicode61 remove_diacritics 2')")
    return db


def index_file(db, root, rel, fitz):
    full = os.path.join(root, rel)
    st = os.stat(full)
    row = db.execute("SELECT size, mtime, md5 FROM files WHERE path=?", (rel,)).fetchone()
    if row and row[0] == st.st_size and abs(row[1] - st.st_mtime) < 1:
        return 'skip'
    md5 = md5_of(full)
    have = db.execute("SELECT 1 FROM pages WHERE md5=? LIMIT 1", (md5,)).fetchone()
    toc, labels, notext, chars, pages, err = [], {}, [], 0, 0, ''
    try:
        doc = fitz.open(full)
        pages = doc.page_count
        toc = doc.get_toc(simple=True)                       # [[уровень, название, страница PDF с 1]]
        for i in range(pages):
            page = doc.load_page(i)
            try:
                lab = page.get_label()
            except Exception:
                lab = ''
            if lab and lab != str(i + 1):
                labels[str(i + 1)] = lab
            if have:
                continue                                      # точная копия уже в базе: текст не дублируем
            t = page.get_text('text') or ''
            n = len(t.strip())
            chars += n
            if n < NOTEXT_CHARS:
                notext.append(i + 1)
            else:
                db.execute("INSERT INTO pages(md5, page, body) VALUES (?,?,?)", (md5, i + 1, t))
        doc.close()
    except Exception as e:                                    # битый PDF, заглушка, нехватка памяти — файл помечается, обход идёт дальше
        err = f'{type(e).__name__}: {e}'[:500]
    if have:
        prev = db.execute("SELECT notext, chars FROM files WHERE md5=? AND error='' LIMIT 1", (md5,)).fetchone()
        if prev:
            notext, chars = json.loads(prev[0] or '[]'), prev[1] or 0
    db.execute("INSERT OR REPLACE INTO files VALUES (?,?,?,?,?,?,?,?,?,?,?)",
               (rel, st.st_size, st.st_mtime, md5, pages, json.dumps(toc, ensure_ascii=False),
                json.dumps(labels, ensure_ascii=False), json.dumps(notext), chars, err, time.strftime('%Y-%m-%dT%H:%M:%S')))
    db.commit()
    return 'error' if err else 'ok'


def export(db, out):
    res = {}
    for path, md5, pages, toc, labels, notext, chars, err in db.execute(
            "SELECT path, md5, pages, toc, labels, notext, chars, error FROM files ORDER BY path"):
        lab = json.loads(labels or '{}')
        e = res.setdefault(md5, {'paths': [], 'pages': pages, 'toc': json.loads(toc or '[]'),
                                 'labels': lab, 'notext_pages': json.loads(notext or '[]'), 'chars': chars, 'error': err})
        e['paths'].append(path)
    with open(os.path.join(out, 'outlines.json'), 'w', encoding='utf8') as f:
        json.dump(res, f, ensure_ascii=False)
    return res


def build(args):
    try:
        import pymupdf as fitz                               # PyMuPDF 1.24+
    except ImportError:
        import fitz                                          # старые версии PyMuPDF
    db = open_db(args.out)
    t0 = time.time()
    cnt = {'ok': 0, 'skip': 0, 'error': 0}
    rels = []
    for dp, dn, fn in os.walk(args.root):
        for n in fn:
            if n.lower().endswith('.pdf'):
                rels.append(os.path.relpath(os.path.join(dp, n), args.root))
    rels.sort()
    for k, rel in enumerate(rels, 1):
        try:
            r = index_file(db, args.root, rel, fitz)
        except Exception as e:
            r = 'error'
            print(f'ERROR {rel}: {e}', file=sys.stderr)
        cnt[r] += 1
        if k % 25 == 0:
            print(f'{k}/{len(rels)} {cnt}', flush=True)
    res = export(db, args.out)
    pages_total = sum(v['pages'] or 0 for v in res.values())
    notext_total = sum(len(v['notext_pages']) for v in res.values())
    rep = {'finished': time.strftime('%Y-%m-%dT%H:%M:%S'), 'seconds': round(time.time() - t0), 'pdf_files': len(rels),
           'unique_md5': len(res), 'counts': cnt, 'with_toc': sum(1 for v in res.values() if v['toc']),
           'with_labels': sum(1 for v in res.values() if v['labels']), 'pages_total': pages_total,
           'pages_without_text': notext_total, 'errors': sum(1 for v in res.values() if v['error']),
           'db_bytes': os.path.getsize(os.path.join(args.out, 'fulltext.sqlite'))}
    with open(os.path.join(args.out, 'index_report.json'), 'w') as f:
        json.dump(rep, f, indent=1)
    print(json.dumps(rep, indent=1))


def search(args):
    db = open_db(args.out)
    q = ' '.join(args.query)
    rows = db.execute("SELECT md5, page, snippet(pages, 2, '[', ']', ' … ', 24), bm25(pages) AS r FROM pages "
                      "WHERE pages MATCH ? ORDER BY r LIMIT ?", (q, args.limit)).fetchall()
    paths = dict(db.execute("SELECT md5, path FROM files").fetchall())
    for md5, page, snip, r in rows:
        print(json.dumps({'md5': md5, 'page': page, 'score': round(r, 2), 'path': paths.get(md5, ''), 'snippet': snip}, ensure_ascii=False))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    b = sp.add_parser('build'); b.add_argument('--root', required=True); b.add_argument('--out', required=True)
    s = sp.add_parser('search'); s.add_argument('--out', required=True); s.add_argument('--limit', type=int, default=20); s.add_argument('query', nargs='+')
    e = sp.add_parser('export'); e.add_argument('--out', required=True)
    a = ap.parse_args()
    if a.cmd == 'build':
        build(a)
    elif a.cmd == 'search':
        search(a)
    else:
        print(len(export(open_db(a.out), a.out)), 'files in outlines.json')
