"""build_data.py — сборка файла данных страницы «Поиск по архиву» (archive-recon, 2026-10-13).

Вход (все файлы НЕ из репозитория — в них личные пути владельца и чужие тексты):
  data.json      массив DATA, вырезанный из прежней версии страницы (после refine.py)
  book_old.json  прежняя запись BOOK (Kursbuch Notfallsonografie) с разделами из оглавления
  books.json     описания книг: ISBN, название, авторы, издательство, год, главы с первой страницей
  links.json     ссылка на файл Google Диска: ключ "<md5>|<путь>" -> ID файла Диска
  meta/out*.json разбор первых страниц моделью: название, подзаголовок, авторы, источник, тип, личный документ
Выход: site/data.json — {meta, syn, data, books} для страницы.

Правила:
  1) Книга, разрезанная на файлы-главы, распознаётся по колонтитулу «Фамилия, Название (ISBN …)»
     в тексте файла; файл относится к главе по печатным номерам страниц книги в его тексте
     (первая найденная страница = начало файла, конец = начало + число страниц PDF − 1).
  2) Название из разбора моделью ставится, только если сейчас название равно имени файла
     и уверенность модели не низкая. Авторы и источник добавляются всегда, когда найдены.
  3) Тип: глава книги — по правилу 1; личный документ — по разбору моделью; руководства
     не переклассифицируются (их приёмку прошёл тест, запись Р-30 журнала); разборы
     «Fall N» журнала остаются статьями журнала.
Запуск: python build_data.py <рабочая папка>
"""
import json, re, sys, os, datetime, collections

W = sys.argv[1] if len(sys.argv) > 1 else '.'
P = lambda *a: os.path.join(W, *a)

D = json.load(open(P('data.json'), encoding='utf8'))
OLD = json.load(open(P('book_old.json'), encoding='utf8'))
BK = json.load(open(P('books.json'), encoding='utf8'))
LINKS = json.load(open(P('links.json'), encoding='utf8'))
M = {}
for fn in sorted(os.listdir(P('meta'))):
    if fn.startswith('out') and fn.endswith('.json'):
        for o in json.load(open(P('meta', fn), encoding='utf8')):
            M[o['id']] = o

ISBN = re.compile(r'\(ISBN ([\d\-]{13,17})\)')
PAGE = re.compile(r'(?:All rights reserved\.|Thieme Verlag KG|© 20\d\d\.? ?Thieme\.?)\s*(\d{1,3})\s+(?:Dieses|weitergegeben)'
                  r'|(?<![\d.])(\d{1,3})\s+[A-ZÄÖÜ][a-zäöüß]+, [A-ZÄÖÜ][^()]{3,60}\(ISBN')

def text(r):
    return (r.get('x') or '') + ' ' + (r.get('ft') or '')

# ---------- 1. книги из файлов-глав ----------
bykey = {b['isbn']: b for b in BK}
for b in BK:
    b['files'] = []
for i, r in enumerate(D):
    m = ISBN.search(text(r))
    if not m or m.group(1) not in bykey:
        continue
    b = bykey[m.group(1)]
    nums = [int(a or c) for a, c in PAGE.findall(text(r))]
    nums = [n for n in nums if 1 <= n <= b['last_page'] + 5]
    pages = int(r['p']) if str(r.get('p', '')).isdigit() else 1
    if nums:
        s = min(nums); e = s + pages - 1
    else:
        s = e = None
    b['files'].append({'i': i, 's': s, 'e': e})

def chapter_of(b, page):
    ch = None
    for c in b['chapters']:
        if c['page'] <= page:
            ch = c
    return ch

OLDSEC = {}
for c in OLD['chapters']:
    for f in c['files']:
        OLDSEC[f['n']] = f['sec']

books_out = []
for b in BK:
    chapters = [dict(num=c['num'], title=c['title'], page=c['page'], files=[]) for c in b['chapters']]
    cidx = {c['num']: c for c in chapters}
    front = []
    seen_span = {}
    for f in sorted(b['files'], key=lambda f: (f['s'] if f['s'] is not None else -1, D[f['i']]['n'])):
        r = D[f['i']]
        if f['s'] is None or f['s'] < b['chapters'][0]['page']:
            front.append(r['h']) if r['h'] not in front else None
            r['d'] = 'chapter'
            r['bk'] = {'isbn': b['isbn'], 'front': 1}; r['au'] = b['authors']; r['src'] = b['publisher']
            r['t'] = f"{b['title']} · Titelei, Inhaltsverzeichnis (Datei {r['n']})"
            continue
        c = chapter_of(b, f['s'])
        # главы, задетые файлом
        touched = [x['num'] for x in b['chapters'] if x['page'] <= f['e'] and
                   (nxt := next((y['page'] for y in b['chapters'] if y['page'] > x['page']), 10**6)) > f['s']]
        span = (f['s'], f['e'])
        dup = seen_span.get(span)
        seen_span.setdefault(span, r['n'])
        entry = {'h': r['h'], 'n': r['n'], 's': f['s'], 'e': f['e'], 'sec': OLDSEC.get(r['n'], '') if b['isbn'] == OLD['isbn'] else ''}
        if dup:
            entry['dup'] = dup
        cidx[c['num']]['files'].append(entry)
        r['d'] = 'chapter'
        r['bk'] = {'isbn': b['isbn'], 'ch': c['num'], 's': f['s'], 'e': f['e']}
        chs = '–'.join(dict.fromkeys([touched[0], touched[-1]])) if touched else c['num']
        r['t'] = f"{b['title']} · Kap. {chs} {c['title']} · S. {f['s']}–{f['e']} (Datei {r['n']})"
        r['y'] = r.get('y') or b['year']
        r['au'] = b['authors']
        r['src'] = b['publisher']
    # покрытие страниц главы
    pages_sorted = [x['page'] for x in b['chapters']] + [b['last_page'] + 1]
    for k, c in enumerate(chapters):
        lo, hi = pages_sorted[k], pages_sorted[k + 1] - 1
        cov = set()
        for f in c['files']:
            cov.update(range(max(lo, f['s']), min(hi, f['e']) + 1))
        # файлы предыдущей главы, заходящие в эту
        for c2 in chapters[:k]:
            for f in c2['files']:
                cov.update(range(max(lo, f['s']), min(hi, f['e']) + 1))
        c['len'] = hi - lo + 1
        c['have'] = len(cov)
    books_out.append(dict(isbn=b['isbn'], title=b['title'], subtitle=b.get('subtitle', ''), authors=b['authors'],
                          publisher=b['publisher'], year=b['year'], edition=b.get('edition', ''),
                          last_page=b['last_page'], front=front, chapters=chapters,
                          toc_file=b.get('toc_file', '')))

# ---------- 2. разбор моделью: названия, авторы, типы ----------
TYPEMAP = {'journal_article': 'journal_article', 'cme_article': 'cme_article', 'guideline': 'guideline',
           'presentation': 'presentation', 'sop_standard': 'sop_standard', 'book': 'book',
           'course_material': 'course', 'notes': 'notes', 'personal': 'personal', 'other': 'other_pdf'}
changed = collections.Counter()
for i, r in enumerate(D):
    o = M.get(i)
    if r['d'] == 'mindmap_card':
        r['d'] = 'notes'
    if not o or r['d'] == 'chapter':
        continue
    if o.get('authors'):
        r['au'] = o['authors']
    if o.get('source'):
        r['src'] = o['source']
    if r['t'].strip() == r['n'].strip() and o.get('title') and o.get('confidence') != 'low':
        t = o['title'].strip()
        if o.get('subtitle'):
            t += ': ' + o['subtitle'].strip()
        r['t'] = t
        changed['title'] += 1
    cur = r['d']
    new = TYPEMAP.get(o.get('type'), cur)
    if o.get('personal'):
        new = 'personal'
    elif cur == 'guideline' or new == 'guideline':
        new = cur                                   # руководства не трогаем
    elif cur == 'journal_article' and new == 'course':
        new = cur                                   # «Fall N» — публикации журнала
    elif new == 'book' and not (str(r.get('p', '')).isdigit() and int(r['p']) >= 100):
        new = cur
    elif cur == 'scan_no_text' and new == 'other_pdf' and len(text(r).strip()) < 50:
        new = cur
    if new != cur:
        changed[(cur, new)] += 1
    r['d'] = new
for r in D:
    if r['d'] == 'certificate':
        r['d'] = 'personal'; changed[('certificate', 'personal')] += 1

# ---------- 3. ссылки, чистка полей ----------
nolink = 0
for r in D:
    g = LINKS.get(r['h'] + '|' + r['pa'])
    if g:
        r['g'] = g
    else:
        nolink += 1
    for k in ('mm', 'mc', 'dx', 'dd', 'dt', 'sm_dd', 'sm_dt'):
        r.pop(k, None)
    if r['d'] == 'personal':
        r['tp'] = []

# ---------- 3а. правки по приёмочному тесту 2026-10-13 ----------
PERSONAL_EXTRA = ['19.03 Fortbildung']           # заявка с мобильным номером и домашним адресом (тест 2026-10-13)
for r in D:
    if r['n'] in PERSONAL_EXTRA:
        r['d'] = 'personal'; r['tp'] = []
    if r['d'] == 'personal':
        r['x'] = ''; r['ft'] = ''          # в личных бумагах IBAN, телефоны, PIN — текст в данные страницы не кладётся
    if r['d'] != 'personal' and len(text(r).strip()) < 80:
        r['nt'] = 1                        # текста нет или почти нет — по содержанию не ищется
    if r['n'].startswith('s44180-021-0018-7'):
        r['d'] = 'guideline'; r['fam'] = 'Antikoagulation und Regionalanästhesie / perioperativ'
    if r['n'].startswith('Transfusion roter Blutkörperchen bei schwerkranken'):
        r['gv'] = 'translation'
    if r['n'] == 'LL Reanimation 2021':
        r['gv'] = ''                       # «überarbeitete Version», не краткая версия
# файл целиком внутри другого файла той же книги; начало главы в файле предыдущей главы
for b in books_out:
    allf = [f for c in b['chapters'] for f in c['files']]
    for f in allf:
        for o in allf:
            if o is f or o.get('dup') == f['n'] or f.get('dup') == o['n']:
                continue
            if o['s'] <= f['s'] and o['e'] >= f['e'] and (o['e'] - o['s']) > (f['e'] - f['s']):
                f['in'] = o['n']; break
    for k, c in enumerate(b['chapters']):
        own = {f['n'] for f in c['files']}
        c['spill'] = [] if c['files'] else [f['n'] for c2 in b['chapters'][:k] for f in c2['files'] if f['e'] >= c['page'] and f['n'] not in own]
# изданий вне архива архив не знает; известные на дату проверки
OUTSIDE = {
 'Reanimation ERC/GRC': 'Вне архива есть Leitlinien ERC 2025 (вышли в октябре 2025).',
 'Reanimation AHA (ACLS, CPR)': 'Вне архива есть AHA Guidelines 2025 (вышли в октябре 2025).',
 'Blutung und Gerinnung bei Trauma (European guideline)': 'Вне архива есть 6-е издание European guideline 2023 (Rossaint и соавт., Critical Care 2023).',
 'AWMF 012-019': 'Вне архива: S3-Leitlinie Polytrauma обновлена в 2022 году под новым номером реестра AWMF 187-023.',
 'AWMF 113-001': 'Вне архива: рекомендации по стационарной терапии COVID-19 много раз обновлялись после 2020 года; актуальную редакцию смотреть в реестре AWMF.',
}

# ---------- 4. синонимы и сводка ----------
SYN = json.load(open(P('syn.json'), encoding='utf8'))
SYN = [[t for t in g if t != 'aki'] for g in SYN]          # «aki» находил «Akinesie» и фамилию AKIN
for g in SYN:
    if 'gerinnung' in g: g += ['koagulopathie', 'coagulopathy']
    if 'lungenversagen' in g: g += ['respiratorische insuffizienz', 'acute respiratory distress']
SYN.append(['massivblutung', 'massive bleeding', 'massive haemorrhage', 'massive hemorrhage', 'major bleeding', 'massivtransfusion'])
WS = ['septisch', 'septic', 'akin']                         # ищутся только с начала слова (не внутри «aseptisch»)
notext = sum(1 for r in D if r.get('nt'))
meta = dict(
    built=datetime.date.today().isoformat(),
    scanned='2026-10-10',
    files=len(D),
    personal=sum(1 for r in D if r['d'] == 'personal'),
    books=sum(1 for r in D if r['d'] == 'book'),
    chapters=sum(1 for r in D if r['d'] == 'chapter'),
    notext=notext,
    folder='AA Beruf')
meta['checked'] = '2026-10-13'
json.dump(dict(meta=meta, syn=SYN, ws=WS, outside=OUTSIDE, data=D, books=books_out), open(P('site', 'data.json'), 'w', encoding='utf8'),
          ensure_ascii=False, separators=(',', ':'))
print(json.dumps(meta, ensure_ascii=False))
print('без ссылки:', nolink)
for k, v in changed.most_common():
    print(k, v)
for b in books_out:
    have = sum(1 for c in b['chapters'] if c['files'])
    print(b['title'], 'глав', len(b['chapters']), 'с файлами', have,
          'файлов', sum(len(c['files']) for c in b['chapters']), 'титул', len(b['front']))
