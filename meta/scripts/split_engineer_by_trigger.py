#!/usr/bin/env python3
"""Раскладка second-brain-engineer/SKILL.md по полю ТРИГГЕР (план meta/PLAN_skill-layers_2026-10-20_v3.md, раздел 2, шаг 2).
Чистый перенос: каждая строка исходника попадает ровно в один файл результата без изменения.
Добавленные строки перечислены в ADDED и проверяются приёмкой поштучно.
Вход: путь к исходной папке Skill, путь к папке результата."""
import sys, re, os, shutil, collections

SRC, OUT = sys.argv[1], sys.argv[2]
lines = open(os.path.join(SRC, 'SKILL.md'), encoding='utf-8').read().split('\n')
# split('\n') keeps a trailing '' if the file ends with newline
body = lines[:-1] if lines[-1] == '' else lines

heads = [i for i, l in enumerate(body) if re.match(r'^## Р\d+\. ', l)]
names = [re.match(r'^## (Р\d+)\. ', body[i]).group(1) for i in heads]
assert names == ['Р0', 'Р1', 'Р6', 'Р8', 'Р9', 'Р10', 'Р13', 'Р14', 'Р15', 'Р16', 'Р18', 'Р21'], names
header = body[:heads[0]]
sec = {}
for k, i in enumerate(heads):
    j = heads[k + 1] if k + 1 < len(heads) else len(body)
    sec[names[k]] = body[i:j]

ADDED = []
def add(s):
    ADDED.append(s)
    return s

DATE = '2026-10-20'

# --- треугольники ТРИГГЕР для трёх разделов без строки ---
def insert_trigger(block, text):
    assert block[1] == '', block[:2]
    assert not any(l.startswith('**ТРИГГЕР.**') for l in block)
    return [block[0], '', add(text), ''] + block[2:]

sec['Р13'] = insert_trigger(sec['Р13'], f'**ТРИГГЕР.** Перед действием, которое требует «да» Андрея или его рук (удаление данных, изменение воркфлоу n8n, структуры INDEX или мастер-промпта, правка Skill, действие на 3 и более узла), перед записью, право на которую сессия не помнит, и перед выдачей наряда. Назначен при раскладке {DATE}.')
sec['Р14'] = insert_trigger(sec['Р14'], f'**ТРИГГЕР.** Любое действие. Назначен при раскладке {DATE}.')
sec['Р18'] = insert_trigger(sec['Р18'], f'**ТРИГГЕР.** Перед выдачей наряда или задания исполнителю (субагенту, посреднику) — выбор класса модели. Назначен при раскладке {DATE}.')

# --- Р15: пункт «Идентификатор, число или дата в канон» уходит в references/write-moment.md ---
p15 = sec['Р15']
a = [i for i, l in enumerate(p15) if l.startswith('- **Идентификатор, число или дата в канон**')]
assert len(a) == 1
a = a[0]
b = a + 1
while b < len(p15) and p15[b].startswith('  '):
    b += 1
moved_p15 = p15[a:b]
assert len(moved_p15) == 3, len(moved_p15)
assert p15[b].startswith('- Запись верифицируется ТОЛЬКО независимым перечитыванием'), p15[b]
pointer = add('- **Идентификатор, число или дата в канон** — правило лежит в references/write-moment.md и читается перед такой записью (таблица «Что читать дальше»).')
sec['Р15'] = p15[:a] + [pointer] + p15[b:]

# --- шапка: правило раскладки и строки таблицы ---
h = list(header)
i_how = [i for i, l in enumerate(h) if l.startswith('Как устроен Skill (нарезка')]
assert len(i_how) == 1
i_how = i_how[0]
rule = add('Правило раскладки по триггеру: раздел, чья строка ТРИГГЕР называет конкретное событие или действие, лежит в references/ и назван в таблице ниже; в этом файле — только разделы, чей ТРИГГЕР — «любое действие», «любое утверждение» или «любая запись», захват (Р6), который срабатывает почти в каждом ответе, и чтение через посредника (Р21): его триггер нужно узнать до вызова инструмента, а не по пришедшему ответу, и проверка 2026-10-20 показала, что из references/ этот раздел не открывают. Новое правило обязано назвать триггер, и триггер определяет файл; правило без триггера в Skill не входит. Основание — решение Андрея 2026-10-20, план `meta/PLAN_skill-layers_2026-10-20_v3.md`, раздел 2.')
h = h[:i_how + 1] + ['', rule] + h[i_how + 1:]

i_save = [i for i, l in enumerate(h) if l.startswith('| выполнить !save')]
assert len(i_save) == 1
i_save = i_save[0]
rows = [
    '| начать сессию: первое сообщение в Claude Project, мастер-промпт которого несёт блок Второго мозга (добавки старта проекта — в его мастер-промпте) | references/start.md | Р1 |',
    '| ответить на команду: сообщение Андрея начинается с !save, !tasks, !priority, !inbox, !review, !status, !digest, !map или слова «харвест» | references/commands.md; для !save затем references/save.md, для харвеста — references/harvest.md | Р8 |',
    '| действие затрагивает другой проект; Андрей просит найти документ, паспорт воркфлоу или ссылку; перед проектированием шага, который мог быть решён у соседа | references/search.md | Р9 |',
    '| изменить воркфлоу n8n; действие, требующее «да» Андрея или его рук (удаление, изменение структуры INDEX или мастер-промпта, правка Skill); выдать наряд или задание исполнителю | references/permissions.md | Р10, Р13, Р18 |',
    '| записать в канон идентификатор, число или дату: ID, sha, номер исполнения, порог, счёт, размер файла, дату записи | references/write-moment.md | Р15 (пункт «Идентификатор, число или дата в канон») |',
    '| работать над проектом вне Claude Project (Cowork, Claude Code, GitHub Actions); вскрылся факт, требующий правки CORE, задачи лаборатории, INDEX, Skill или мастер-промпта | references/outside.md | Р16 |',
]
h = h[:i_save + 1] + [add(r) for r in rows] + h[i_save + 1:]

# --- файлы результата ---
def ref_head(title, when):
    return [add(f'# second-brain-engineer — {title}'), '',
            add(f'Часть Skill second-brain-engineer. Читать: {when}, целиком. Номера пунктов — прежние, общие со SKILL.md; ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md. Файл выделен из SKILL.md раскладкой по триггеру {DATE}: текст разделов перенесён без изменения.'), '']

files = collections.OrderedDict()
files['SKILL.md'] = h + sec['Р0'] + sec['Р6'] + sec['Р14'] + sec['Р15'] + sec['Р21']
files['references/start.md'] = ref_head('старт сессии', 'первое сообщение в Claude Project, мастер-промпт которого несёт блок Второго мозга, — до ответа на это сообщение') + sec['Р1']
files['references/commands.md'] = ref_head('команды', 'сообщение Андрея начинается с команды из таблицы раздела Р8') + sec['Р8']
files['references/search.md'] = ref_head('взаимосвязи и поиск документов', 'действие затрагивает другой проект или Андрей просит найти документ, паспорт, ссылку') + sec['Р9']
files['references/permissions.md'] = ref_head('полномочия, права доступа и калибровка исполнителя', 'перед изменением воркфлоу n8n, перед действием, требующим «да» Андрея или его рук, и перед выдачей наряда') + sec['Р10'] + sec['Р13'] + sec['Р18']
wm_head = ref_head('идентификатор, число или дата в канон', 'перед записью в канон идентификатора, числа или даты')
wm = wm_head + [add('## Р15 (пункт). Идентификатор, число или дата в канон'), '',
                add(f'**ТРИГГЕР.** Запись в канон (файл repo, INDEX, реестр, позиция Очереди, журнал) идентификатора, числа или даты: ID, sha, номера исполнения, порога, счёта, размера, даты записи. Назначен при раскладке {DATE}: пункт вынесен из раздела Р15 SKILL.md, остальной Р15 действует оттуда.'),
                add('**ДЕЙСТВИЕ.**')] + moved_p15
files['references/write-moment.md'] = wm
files['references/outside.md'] = ref_head('работа вне Claude Project и регистрация обязательств', 'работа над проектом вне Claude Project или вскрылся факт, требующий правки CORE, INDEX, Skill или мастер-промпта') + sec['Р16']

if os.path.exists(OUT):
    shutil.rmtree(OUT)
shutil.copytree(SRC, OUT)
for name, ls in files.items():
    txt = '\n'.join(ls)
    if not txt.endswith('\n'):
        txt += '\n'
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(txt)
with open(os.path.join(OUT, '..', 'ADDED.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(ADDED) + '\n')
print('written', list(files))
print('added lines', len(ADDED))
