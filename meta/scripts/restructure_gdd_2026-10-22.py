#!/usr/bin/env python3
"""meta/scripts/restructure_gdd_2026-10-22.py — перенос оснований Skill google-drive-docs в references/basis.md
по правилам протокола синтеза (meta/PROTOCOL_knowledge-synthesis.md, внесены 2026-10-22):
  1. основание правила — в references/basis.md, в правиле ярлык [основание: <ярлык>];
  2. шапка SKILL.md для исполнителя — не больше трёх строк сверх строки редакции, устройство Skill — в basis.md.
Файлы references/ не разрезаются (разрез в контракт прохода не входил).

Запуск: python3 meta/scripts/restructure_gdd_2026-10-22.py SRC OUT
  SRC — папка Skill после синтеза кластеров, OUT — папка результата (создаётся).
Пишет OUT/../restructure_report.json — вход приёмки meta/scripts/accept_restructure_n8n.py (общая логика восстановления).
Модель текст исходника не набирает: всё, что не названо в ADDED, — байты исходника, перенесённые скриптом.
Образец — meta/scripts/restructure_n8n_2026-10-22.py.
"""
import os, re, sys, json

SRC, OUT = sys.argv[1], sys.argv[2]
ADDED, REMOVED, MOVED = [], [], []
BASIS = []
REPORT_OLD = 'meta/SYNTHESIS_google-drive-docs_2026-10-20.md'
REPORT_NEW = 'meta/SYNTHESIS_google-drive-docs_2026-10-22.md'

def read(p): return open(p, encoding='utf-8').read()
def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)
def add(line): ADDED.append(line); return line
def rem(line): REMOVED.append(line); return line

BASIS_RE = re.compile(r'(?:^|(?<=[.;»)!*] ))((?:\s*- )?\s*Основани[ея](?![»])(?:(?: [^:]{0,70})?:| —))')
SEC_RE = [re.compile(r'^#{2,3} (.+)'), re.compile(r'^\*\*([^*]{3,50})\*\*')]

def extract_basis(text, stem, counter):
    lines = text.split('\n'); out = []; i = 0; section = ''
    while i < len(lines):
        ln = lines[i]
        for r in SEC_RE:
            m = r.match(ln)
            if m: section = m.group(1).strip().rstrip('.*:'); break
        mm = BASIS_RE.search(ln)
        if not mm or ln.startswith('|'):
            out.append(ln); i += 1; continue
        start = mm.start(1)
        prefix, tail = ln[:start], ln[start:]
        lead = re.match(r'^\s*(?:- )?\s*', tail).group(0)
        prefix, tail = prefix + lead, tail[len(lead):]
        block = [tail]
        if tail.rstrip().endswith(':') and len(tail.rstrip()) < 90:
            j = i + 1
            while j < len(lines) and re.match(r'^\s*- ', lines[j]):
                block.append(lines[j]); j += 1
            i = j - 1
        counter[0] += 1
        label = f'{stem}-{counter[0]:02d}'
        sec = re.sub(r' {2,}', ' ', re.sub(r'[():]', '', section))[:70].strip()
        BASIS.append((label, sec, block))
        rid = re.findall(r'правил[оа] ([§A-Z]?[\w.-]*\w)', ' '.join(block))
        tag = f'{label} · правило {", ".join(dict.fromkeys(rid))}' if rid else label
        if prefix.strip() in ('', '-'):
            out.append(add(f'{prefix}[основание: {tag}]'))
        else:
            out.append(prefix.rstrip() + ' ' + add(f'[основание: {tag}]'))
        i += 1
    return '\n'.join(out)

RED_OLD, RED_NEW = 'Редакция 2026-10-20.', 'Редакция 2026-10-22.'
def bump(text):
    if RED_OLD in text:
        rem(RED_OLD); return text.replace(RED_OLD, add(RED_NEW), 1)
    return text

# ---------- 1. SKILL.md ----------
s = bump(read(os.path.join(SRC, 'SKILL.md')))
lines = s.split('\n'); keep = []
EDITOR_PREFIX = ('ГДЕ ЖИВЁТ ТЕКСТ.', 'Файл, которого нет в таблице, не читается никем')
for ln in lines:
    if ln.startswith(EDITOR_PREFIX): MOVED.append(ln); continue
    keep.append(ln)
s = '\n'.join(keep)
# основание правила «файл без строки таблицы» уходит вместе с ним (строка сразу после «Этот файл читается всегда…»)
HEAD = 'Этот файл читается всегда.'
idx = [k for k, l in enumerate(s.split('\n')) if l.startswith(HEAD)]
assert len(idx) == 1
ls_ = s.split('\n'); k = idx[0]
if ls_[k + 1].startswith('Основание: решение Андрея 2026-09-24'):
    MOVED.append(ls_[k + 1]); del ls_[k + 1]
old_head = ls_[k]; rem(old_head)
ls_[k] = add(old_head + ' Действие, для которого свой файл не прочитан, — то же нарушение, что действие без этого Skill. Ярлык [основание: …] в правиле ведёт в references/basis.md; там же — почему Skill устроен так (раздел «Устройство Skill»).')
s = re.sub(r'\n{3,}', '\n\n', '\n'.join(ls_))
rows = s.split('\n'); nr = []
for ln in rows:
    nr.append(ln)
    if ln.startswith('| ошибка, пустой или странный ответ инструмента Google'):
        nr.append(add('| править этот Skill, спорить с правилом, найти адрес случая за ярлыком [основание: …]; синтез и харвест | references/basis.md | основания, устройство Skill |'))
s = '\n'.join(nr)
write(os.path.join(OUT, 'SKILL.md'), extract_basis(s, 'MAIN', [0]))

# ---------- 2. references ----------
STEMS = {'docs-read.md': 'DR', 'docs-write.md': 'DW', 'failures.md': 'FL', 'infra.md': 'INF', 'mcp.md': 'MCP', 'sheets.md': 'SH'}
for fn, stem in STEMS.items():
    t = bump(read(os.path.join(SRC, 'references', fn)))
    write(os.path.join(OUT, 'references', fn), extract_basis(t, stem, [0]))

# ---------- 3. basis.md ----------
b = [add('# google-drive-docs — основания правил и устройство Skill'), '',
     add(f'Редакция 2026-10-22. Кто читает: синтез (`meta/PROTOCOL_knowledge-synthesis.md`), харвест, сессия, которая правит Skill или оспаривает правило. Исполнитель правил этот файл не читает: условие, действие, «почему» и «не путать» остались в правиле. Ярлык `[основание: X]` в тексте правила разрешается строкой `- X (...)` ниже; продолжение многострочного основания — строки с отступом в два пробела. «Отчёт синтеза, правило X» в строке основания — `{REPORT_OLD}`, таблица «правило → случаи», по номеру правила; основания правил, внесённых 2026-10-22, — `{REPORT_NEW}`. Текст оснований и абзацы устройства перенесены скриптом байт в байт (`meta/scripts/restructure_gdd_2026-10-22.py`).'), '',
     add('## Устройство Skill'), '',
     add('Переложение 2026-10-22 (синтез по харвесту 2026-10-22, решение Андрея перенести основания всего Skill): основания вынесены сюда ярлыками; ярлык в правиле несёт номер правила в отчёте синтеза, если основание его называет; файлы references/ не разрезались.'), '',
     add('### Правила для того, кто правит Skill (из шапки SKILL.md до 2026-10-22, дословно; действуют)'), '']
for ln in MOVED: b += [ln, '']
b += [add('## Основания правил'), '']
for label, section, block in BASIS:
    b.append(add(f'- {label} ({section}): ') + block[0])
    for cont in block[1:]: b.append('  ' + cont)
write(os.path.join(OUT, 'references', 'basis.md'), '\n'.join(b).rstrip('\n') + '\n')

json.dump({'added': ADDED, 'removed': REMOVED, 'basis': BASIS, 'moved': MOVED},
          open(os.path.join(OUT, '..', 'restructure_report.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('basis entries:', len(BASIS), '| added:', len(ADDED), '| removed:', len(REMOVED), '| moved:', len(MOVED))
for f in ['SKILL.md'] + ['references/' + x for x in sorted(os.listdir(os.path.join(OUT, 'references')))]:
    print(f'{os.path.getsize(os.path.join(OUT, f)):7d}  {f}')
