#!/usr/bin/env python3
"""meta/scripts/restructure_sbe_2026-10-22.py — переложение Skill second-brain-engineer по трём правилам
протокола синтеза (meta/PROTOCOL_knowledge-synthesis.md, внесены 2026-10-22):
  1. основание правила — по адресу в references/basis.md, в правиле ярлык [основание: <ярлык>];
  2. шапка SKILL.md для исполнителя — три строки, объяснение устройства — в basis.md;
  3. зерно references/ — момент действия: design.md разделён, Р21 — в references/intermediary.md.

Запуск: python3 meta/scripts/restructure_sbe_2026-10-22.py SRC OUT
  SRC — папка Skill (зеркало или живой), OUT — папка результата (создаётся).
Пишет также OUT/../restructure_report.json: добавленные и удалённые строки — вход приёмки
(meta/scripts/accept_restructure.py). Модель текст не набирает: всё, что не названо в ADDED, —
байты исходника, перенесённые скриптом.
"""
import os, re, sys, json, shutil

SRC, OUT = sys.argv[1], sys.argv[2]
ADDED, REMOVED = [], []          # строки, порождённые сессией / строки исходника, снятые с заменой
BASIS = []                       # (label, section, [lines])

def read(p): return open(p, encoding='utf-8').read()
def write(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(t)
def add(line): ADDED.append(line); return line

BASIS_RE = re.compile(r'(?:^|(?<=[.;»)!] ))((?:- )?\s*Основани[ея](?![»])(?: [^:]{0,70})?:)')

def extract_basis(text, stem, counter):
    """Вырезает хвосты «Основание: …» из каждой строки; возвращает новый текст."""
    lines = text.split('\n'); out = []; i = 0
    section = ''
    while i < len(lines):
        ln = lines[i]
        m = re.match(r'^## (.+)', ln) or re.match(r'^\*\*(\d+\. [^.*]+)', ln)
        if m: section = m.group(1).strip()
        mm = BASIS_RE.search(ln)
        if not mm:
            out.append(ln); i += 1; continue
        start = mm.start(1)
        prefix, tail = ln[:start], ln[start:]
        lead = re.match(r'^\s*', tail).group(0)          # отступ вложенного списка остаётся в правиле
        prefix, tail = prefix + lead, tail[len(lead):]
        block = [tail]
        # список оснований: строка кончается двоеточием, дальше строки «- …» до пустой
        if tail.rstrip().endswith(':'):
            j = i + 1
            while j < len(lines) and lines[j].startswith('- '):
                block.append(lines[j]); j += 1
            i = j - 1
        counter[0] += 1
        label = f'{stem}-{counter[0]:02d}'
        BASIS.append((label, section, block))
        indent = prefix if prefix.strip() == '' else ''
        if prefix.strip() == '':
            out.append(add(f'{indent}[основание: {label}]'))
        else:
            out.append(prefix.rstrip() + ' ' + add(f'[основание: {label}]'))   # исходная строка восстанавливается приёмкой из basis.md
        i += 1
    return '\n'.join(out)

# ---------- 1. SKILL.md ----------
skill = read(os.path.join(SRC, 'SKILL.md'))
head, rest = skill.split('\n## Что читать дальше\n', 1)
table, body = rest.split('\n---\n', 1)

# шапка: оставить фронтматтер, заголовок, редакцию, формат блока; абзацы устройства — в basis
hl = head.split('\n')
keep, moved = [], []
for ln in hl:
    if ln.startswith(('**Один регламент', '**Как устроен этот текст', '**Как устроен Skill', 'Правило раскладки по триггеру')):
        moved.append(ln)
    else:
        keep.append(ln)
keep_text = '\n'.join(keep).rstrip('\n')
keep_text = re.sub(r'\n{3,}', '\n\n', keep_text)
if keep_text.endswith('\n---'): keep_text = keep_text[:-4].rstrip('\n')   # разделитель шапки ставится заново ниже
keep_text = keep_text.replace('Редакция 2026-10-20.', add('Редакция 2026-10-22.'))
REMOVED.append('Редакция 2026-10-20.')
new_head = keep_text + '\n\n' + add('Этот файл читается всегда. Остальное лежит в references/ и читается перед своим действием целиком, по таблице ниже; номера разделов сквозные и не перенумеровываются (на них ссылаются другие файлы и другие Skills). Действие, для которого свой файл не прочитан, — то же нарушение, что действие без этого Skill. Почему Skill устроен так и откуда взялись слои — references/basis.md, раздел «Устройство Skill» (читает тот, кто Skill правит, не тот, кто исполняет).') + '\n\n---\n'

# таблица: заменить строку design.md тремя, строку правки Skill, добавить Р21 и basis
tl = table.split('\n'); nt = []
for ln in tl:
    if ln.startswith('| спроектировать новый Skill / протокол'):
        REMOVED.append(ln)
        nt.append(add('| спроектировать новый Skill, протокол или архитектурное решение; снять или заменить действующую процедуру, монитор или журнал | references/design.md | Р19, пункты 1–8 и 10–13 |'))
        nt.append(add('| построить проверку, приёмку, аудит или замер, по итогу которых принимается решение; массовый механический перенос или опись | references/design-acceptance.md | Р19, пункты 9, 14, 15, 17 |'))
        nt.append(add('| завести новый Skill; подготовить правку Skill; ревизия каталога; повтор после внесения правила (нельзя ли исполнить правило кодом) | references/catalog-hygiene.md | Р19 пункт 16, Р20 |'))
    elif ln.startswith('| подготовить любую правку Skill'):
        REMOVED.append(ln)
        nt.append(add('| подготовить любую правку Skill — урок, поправку, перенос правила | `meta/PROTOCOL_knowledge-synthesis.md` в репозитории second-brain-canon; затем references/catalog-hygiene.md | синтез, Р20 |'))
    elif ln.startswith('| выяснить, почему правило'):
        nt.append(add('| перед вызовом инструмента, чей ответ нельзя сузить до попадания в контекст: `get_workflow_details` воркфлоу целиком, выдача исполнения грязного воркфлоу, длинная выдача внешнего API; когда от большого объекта нужен ответ, а не текст. Решение принимается до вызова, не по пришедшему ответу | references/intermediary.md | Р21 |'))
        nt.append(add('| править Skill, спорить с правилом, найти адрес случая за ярлыком [основание: …]; синтез и харвест | references/basis.md | основания правил, устройство Skill |'))
        nt.append(ln)
    else:
        nt.append(ln)
new_table = '\n'.join(nt)

# тело: Р21 — в intermediary.md
body_main, r21 = body.split('\n## Р21. ', 1)
r21 = '## Р21. ' + r21
body_main = body_main.rstrip('\n').rstrip('-').rstrip('\n') + '\n'
REMOVED.append('---')   # разделитель перед Р21: Р21 ушёл в intermediary.md

counter = [0]
new_skill = new_head + '\n## Что читать дальше\n' + new_table + '\n---\n' + extract_basis(body_main, 'SKILL', counter)
write(os.path.join(OUT, 'SKILL.md'), new_skill)

inter = add('# second-brain-engineer — чтение через посредника') + '\n\n' + add('Часть Skill second-brain-engineer. Читать: перед вызовом инструмента, чей ответ нельзя сузить до попадания в контекст (описание воркфлоу целиком при сумме узлов больше 100, выдача исполнения грязного воркфлоу, длинная выдача внешнего API), и когда от большого объекта нужен ответ, а не текст. Номер раздела — прежний, общий со SKILL.md; ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md.') + '\n\n' + extract_basis(r21, 'intermediary', [0])
write(os.path.join(OUT, 'references', 'intermediary.md'), inter)

# ---------- 2. design.md → три файла ----------
d = read(os.path.join(SRC, 'references', 'design.md'))
dhead, drest = d.split('\n## Р19. ', 1)
r19, r20 = ('## Р19. ' + drest).split('\n---\n\n## Р20. ', 1)
r20 = '## Р20. ' + r20
pts = re.split(r'(?m)^(?=\*\*\d+\. )', r19)
r19head, points = pts[0], pts[1:]
num = lambda p: int(re.match(r'\*\*(\d+)\.', p).group(1))
check = ''
if '**ПРОВЕРКА.**' in points[-1]:
    points[-1], check = points[-1].split('\n**ПРОВЕРКА.**', 1); check = '**ПРОВЕРКА.**' + check
keep_pts = [p for p in points if num(p) in (1,2,3,4,5,6,7,8,10,11,12,13)]
acc_pts  = [p for p in points if num(p) in (9,14,15,17)]
hyg_pts  = [p for p in points if num(p) == 16]
sep = add('Пункты 9, 14, 15 и 17 (замер, приёмка, критерий приёмки, массовая работа скриптом) — references/design-acceptance.md; пункт 16 (правило в код) и Р20 — references/catalog-hygiene.md. Нумерация пунктов сквозная.') + '\n\n'
design = dhead + '\n' + r19head + ''.join(keep_pts).rstrip('\n') + '\n\n' + sep + check
acc = add('# second-brain-engineer — проверка, приёмка и замер') + '\n\n' + add('Часть Skill second-brain-engineer, пункты 9, 14, 15 и 17 раздела Р19. Читать: строится проверка, приёмка, аудит или замер, по итогу которых принимается решение; планируется массовый механический перенос или опись. Остальные пункты Р19 — references/design.md; номера пунктов сквозные.') + '\n\n' + ''.join(acc_pts)
hyg = add('# second-brain-engineer — гигиена каталога Skill и правило в код') + '\n\n' + add('Часть Skill second-brain-engineer: пункт 16 раздела Р19 и раздел Р20. Читать: планируется новый Skill; готовится правка Skill (синтез, правка харвеста, позиция Очереди); ревизия каталога; повтор правила после внесения — первый вопрос, нельзя ли исполнить правило кодом. Номера пунктов сквозные.') + '\n\n' + ''.join(hyg_pts) + '\n---\n' + r20
write(os.path.join(OUT, 'references', 'design.md'), extract_basis(design, 'design', [0]))
write(os.path.join(OUT, 'references', 'design-acceptance.md'), extract_basis(acc, 'design-acceptance', [0]))
write(os.path.join(OUT, 'references', 'catalog-hygiene.md'), extract_basis(hyg, 'catalog-hygiene', [0]))

# ---------- 3. остальные references: только вырезать основания ----------
for f in sorted(os.listdir(os.path.join(SRC, 'references'))):
    if f == 'design.md': continue
    stem = f[:-3]
    write(os.path.join(OUT, 'references', f), extract_basis(read(os.path.join(SRC, 'references', f)), stem, [0]))

# ---------- 4. basis.md ----------
b = [add('# second-brain-engineer — основания правил и устройство Skill'), '',
     add('Редакция 2026-10-22. Кто читает: синтез (`meta/PROTOCOL_knowledge-synthesis.md`), харвест, сессия, которая правит Skill или оспаривает правило. Исполнитель правил этот файл не читает: ему нужны условие, действие, «почему» и «не путать», и они остались в правиле. Ярлык `[основание: X]` в тексте правила разрешается строкой `- X (...)` ниже; продолжение многострочного основания — строки с отступом в два пробела. Сам текст оснований перенесён скриптом байт в байт (`meta/scripts/restructure_sbe_2026-10-22.py`).'), '',
     add('## Устройство Skill'), '']
for ln in moved: b += [ln, '']
b += [add('Поправка 2026-10-22 (контракт автопилота, `projects/kontext-reduktion/PLAN.md`): исключение для Р21 снято — раздел перенесён в references/intermediary.md со строкой таблицы «Что читать дальше». Что правило в файле по действию не нарушается, — гипотеза до поведенческого теста после заливки (`meta/TEST_skill-layers_2026-10-22.md`); нарушение в тесте возвращает Р21 в SKILL.md. Шапка SKILL.md сокращена до трёх строк по правилу протокола синтеза «Объяснения устройства Skill в шапке»; design.md разделён по моменту действия на design.md, design-acceptance.md и catalog-hygiene.md.'), '']
b += [add('## Основания правил'), '']
for label, section, block in BASIS:
    first = block[0]
    b.append(add(f'- {label} ({section}): ') + first)
    for cont in block[1:]: b.append('  ' + cont)
write(os.path.join(OUT, 'references', 'basis.md'), '\n'.join(b).rstrip('\n') + '\n')

json.dump({'added': ADDED, 'removed': REMOVED, 'basis': BASIS, 'moved_head': moved},
          open(os.path.join(OUT, '..', 'restructure_report.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('basis entries:', len(BASIS), '| added lines:', len(ADDED), '| removed lines:', len(REMOVED))
for f in ['SKILL.md'] + ['references/' + x for x in sorted(os.listdir(os.path.join(OUT, 'references')))]:
    print(f'{os.path.getsize(os.path.join(OUT, f)):7d}  {f}')
