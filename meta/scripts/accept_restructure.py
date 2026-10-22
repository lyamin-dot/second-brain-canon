#!/usr/bin/env python3
"""meta/scripts/accept_restructure.py — приёмка переложения Skill (restructure_sbe_2026-10-22.py).
Запуск: python3 meta/scripts/accept_restructure.py SRC OUT REPORT.json
Проверяет, что исходник восстанавливается из результата: каждая непустая строка исходника либо стоит
в результате как есть, либо стоит с ярлыком [основание: X], а вырезанный хвост лежит в references/basis.md
ровно один раз; строки сверх исходника — только из перечня ADDED отчёта, снятые — только из REMOVED.
"""
import sys, os, re, json, collections
SRC, OUT, REP = sys.argv[1:4]
rep = json.load(open(REP, encoding='utf-8'))
ok = True
def fail(m):
    global ok; ok = False; print('FAIL:', m)
def files(d):
    r = {}
    for root, _, fs in os.walk(d):
        for f in fs:
            p = os.path.join(root, f); r[os.path.relpath(p, d)] = open(p, encoding='utf-8').read()
    return r
S, R = files(SRC), files(OUT)

# 1. basis.md → словарь ярлыков
basis = R['references/basis.md']
head, entries = basis.split('\n## Основания правил\n', 1)
labels = {}
cur = None
for ln in entries.split('\n'):
    m = re.match(r'^- ([A-Za-z-]+-\d\d) \((.*?)\): (.*)$', ln)
    if m:
        cur = m.group(1); labels[cur] = [m.group(3)]
    elif ln.startswith('  ') and cur:
        labels[cur].append(ln[2:])
    elif ln.strip() == '':
        cur = None
    else:
        fail(f'basis.md: строка вне формата: {ln[:60]}')
if len(labels) != len(rep['basis']): fail(f'ярлыков в basis.md {len(labels)}, в отчёте {len(rep["basis"])}')

# 2. восстановление результата
used = collections.Counter()
recon = collections.Counter()
LAB = re.compile(r'\[основание: ([A-Za-z-]+-\d\d)\]')
for k, t in R.items():
    text = head if k == 'references/basis.md' else t
    for ln in text.split('\n'):
        if not ln.strip(): continue
        m = re.match(r'^(\s*(?:- )?)\[основание: ([A-Za-z-]+-\d\d)\]$', ln)
        if m:
            lab = m.group(2); used[lab] += 1
            block = labels.get(lab)
            if block is None: fail(f'{k}: ярлык без записи в basis.md: {lab}'); continue
            recon[m.group(1) + block[0]] += 1
            for c in block[1:]: recon[c] += 1
            continue
        m = LAB.search(ln)
        if m and ln.rstrip().endswith(']'):
            lab = m.group(1); used[lab] += 1
            block = labels.get(lab)
            if block is None: fail(f'{k}: ярлык без записи в basis.md: {lab}'); continue
            recon[ln[:m.start()].rstrip() + ' ' + block[0]] += 1
            for c in block[1:]: recon[c] += 1
            continue
        recon[ln] += 1
for lab in labels:
    if used[lab] != 1: fail(f'ярлык {lab} использован {used[lab]} раз')

# 3. мультимножество
src = collections.Counter(l for t in S.values() for l in t.split('\n') if l.strip())
added = collections.Counter(l for l in rep['added'] if l.strip())
removed = collections.Counter(l for l in rep['removed'] if l.strip())
lost = src - (recon - added)
extra = (recon - added) - src
if lost != removed: fail(f'потеряно не по перечню REMOVED: {list((lost - removed).elements())[:3]} | лишнее в REMOVED: {list((removed - lost).elements())[:3]}')
if extra: fail(f'лишние строки сверх ADDED: {sum(extra.values())}: {list(extra)[:3]}')
print(f'строк исходника {sum(src.values())}; восстановлено {sum(recon.values())}; добавлено по перечню {sum(added.values())}; снято по перечню {sum(removed.values())}')

# 4. разделы и пункты
hd = lambda t: re.findall(r'(?m)^## (Р\d+)\. ', t)
src_h = collections.Counter(h for t in S.values() for h in hd(t))
res_h = collections.Counter(h for t in R.values() for h in hd(t))
if src_h != res_h: fail(f'разделы: {src_h} vs {res_h}')
pts = collections.Counter(int(n) for k, t in R.items() if k.startswith('references/') for n in re.findall(r'(?m)^\*\*(\d+)\. ', t))
if any(pts[i] != 1 for i in range(1, 18)): fail(f'пункты Р19 не по одному разу: {pts}')
# 5. строки таблицы ведут на существующие файлы
for f in re.findall(r'\| (references/[a-z-]+\.md)', R['SKILL.md']):
    if f not in R: fail(f'таблица ссылается на отсутствующий файл {f}')
print('SKILL.md:', len(R['SKILL.md'].encode()), 'Б')
print('ПРИНЯТО' if ok else 'НЕ ПРИНЯТО')
sys.exit(0 if ok else 1)
