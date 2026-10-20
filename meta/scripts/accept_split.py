#!/usr/bin/env python3
"""Приёмка раскладки: SRC — исходная папка Skill, OUT — результат, ADDED — перечень добавленных строк."""
import sys, os, re, collections
SRC, OUT, ADDED = sys.argv[1:4]
ok = True
def fail(m):
    global ok; ok = False; print('FAIL:', m)

def files(d):
    r = {}
    for root, _, fs in os.walk(d):
        for f in fs:
            p = os.path.join(root, f)
            r[os.path.relpath(p, d)] = open(p, encoding='utf-8').read()
    return r
S, R = files(SRC), files(OUT)
added = [l for l in open(ADDED, encoding='utf-8').read().split('\n') if l.strip()]

# 1. старые файлы references/ не тронуты
for k in S:
    if k != 'SKILL.md' and S[k] != R.get(k):
        fail(f'изменён или пропал старый файл {k}')
new = sorted(set(R) - set(S))
print('новые файлы:', new)

# 2. мультимножество непустых строк
src_c = collections.Counter(l for l in S['SKILL.md'].split('\n') if l.strip())
res_c = collections.Counter()
for k in ['SKILL.md'] + new:
    res_c.update(l for l in R[k].split('\n') if l.strip())
add_c = collections.Counter(added)
lost = src_c - (res_c - add_c)
extra = (res_c - add_c) - src_c
if lost: fail(f'потеряно строк исходника: {sum(lost.values())}: {list(lost)[:3]}')
if extra: fail(f'лишние строки сверх перечня: {sum(extra.values())}: {list(extra)[:3]}')
if res_c - src_c != add_c: fail('добавленные строки не совпадают с перечнем ADDED')
print('строк исходника:', sum(src_c.values()), '| в результате:', sum(res_c.values()), '| добавлено по перечню:', len(added))

# 3. разделы: каждый ровно один раз, номера прежние
hd = lambda t: re.findall(r'(?m)^## (Р\d+)\. ', t)
src_h = hd(S['SKILL.md'])
res_h = []
for k in ['SKILL.md'] + new:
    res_h += hd(R[k])
if sorted(src_h) != sorted(res_h): fail(f'разделы: {src_h} vs {res_h}')
print('разделы исходника:', src_h)

# 4. таблица «Что читать дальше» называет каждый новый файл, и каждый названный файл существует
sk = R['SKILL.md']
table = [l for l in sk.split('\n') if l.startswith('| ') and 'references/' in l]
named = set(re.findall(r'references/[a-z\-]+\.md', '\n'.join(table)))
for n in new:
    if n not in named: fail(f'новый файл не назван в таблице: {n}')
for n in named:
    if n not in R: fail(f'таблица называет несуществующий файл: {n}')

# 5. у каждого раздела строка ТРИГГЕР; в SKILL.md — только «любое ...», кроме разрешённых исключений
PERM = re.compile(r'любое действие|любое утверждение|любая запись', re.I)
for k in ['SKILL.md'] + new:
    blocks = re.split(r'(?m)^(?=## Р)', R[k])[1:]
    for b in blocks:
        name = re.match(r'## (Р\d+)', b).group(1)
        trg = [l for l in b.split('\n') if l.startswith('**ТРИГГЕР.**')]
        if not trg: fail(f'{k} {name}: нет строки ТРИГГЕР'); continue
        perm = bool(PERM.search(trg[0]))
        if k == 'SKILL.md' and not perm:
            print(f'ИСКЛЮЧЕНИЕ регулярного выражения: {name} в SKILL.md без фразы «любое …» — по таблице плана')
        if k != 'SKILL.md' and perm:
            fail(f'{k} {name}: триггер постоянного слоя вне SKILL.md')

for k in ['SKILL.md'] + new:
    print(f'{k}: {len(R[k].encode())} байт')
print('ПРИЁМКА:', 'ПРОЙДЕНА' if ok else 'НЕ ПРОЙДЕНА')
sys.exit(0 if ok else 1)
