#!/usr/bin/env python3
"""Status updates of the apps-script-sheets synthesis. Usage: apply_status.py CLONE.
Each status cell gets a new first word; the previous text goes after a semicolon (second-brain-git 10.5)."""
import sys, pathlib
R = pathlib.Path(sys.argv[1])
REP = 'meta/SYNTHESIS_apps-script-sheets_2026-10-20.md'
out = []

def status(pos, new_head):
    p = R / 'registry/maintenance-queue.md'
    lines = p.read_text().split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(f'| {pos} |')]
    assert len(hits) == 1, (pos, hits)
    cells = lines[hits[0]].split('|')
    old = cells[6].strip()
    if old.startswith(new_head.split(' — ')[0]) and REP in old:
        out.append(f'skip {pos}'); return
    cells[6] = f' {new_head}; прежний статус: {old} '
    lines[hits[0]] = '|'.join(cells)
    p.write_text('\n'.join(lines)); out.append(f'status {pos}')

status('AJ-5', f'ЖДЁТ заливки zip apps-script-sheets 2026-10-21 — правки 2, 3, 4, 5, 6, 8, 9, 11 внесены синтезом своих кластеров в зеркало skills/apps-script-sheets/ (новый пункт 9.9 «Свежесть»), правки 1, 7, 10, 12 не вносятся (история), правка 13 не в Skill; отчёт {REP}')
status('AJ-16', f'ЖДЁТ заливки zip apps-script-sheets 2026-10-21 — мост gas-bridge и аварийный путь clasp внесены синтезом в зеркало skills/apps-script-sheets/SKILL.md, раздел 1 «Порядок работы»; отчёт {REP}')
status('AH-22', f'ВНЕСЕНО 2026-10-21 — живой Skill apps-script-sheets, references/book-traps.md, пункт 3.9 (проверено чтением снимка живого Skill 2026-10-21); синтез 2026-10-20 переписал его правилом, {REP}')
status('AJ-14', f'ЖДЁТ синтеза 2026-10-21 — Х-8 (предел книги 10 миллионов ячеек) и Х-9 (одна область видимости файлов проекта Apps Script) внесены в зеркало skills/apps-script-sheets/ (references/book-traps.md пункт 3.7 и SKILL.md новый пункт 2.8), синтез apps-script-sheets, ждёт заливки zip, отчёт {REP}')

# gas-bridge debt 2: neighbour line (second-brain-git 10.6)
p = R / 'projects/gas-bridge/STATE.md'
t = p.read_text()
item = (f'- ⚡ Это затрагивает GAS-BRIDGE (от SYS, 2026-10-21): долг 2 закрывается заливкой — синтез Skill apps-script-sheets внёс мост в раздел 1 «Порядок работы» (чтение мостом любого скрипта, доступного аккаунту Андрея; запись — только при доступе `write` в `gas_allowlist`; запуск функций сессии не обещан; clasp — аварийный путь Андрея), текст — зеркало `skills/apps-script-sheets/SKILL.md`, отчёт `{REP}`; ждёт заливки zip Андреем (позиция AJ-16). После заливки и приёмки по снимку долг 2 вычеркнуть.\n')
if 'синтез Skill apps-script-sheets внёс мост' not in t:
    if '## От соседнего проекта\n' in t:
        t = t.replace('## От соседнего проекта\n', '## От соседнего проекта\n\n' + item, 1)
    else:
        t = t.rstrip('\n') + '\n\n## От соседнего проекта\n\n' + item
    p.write_text(t); out.append('state gas-bridge')

# map, section 6
p = R / 'meta/SKILLS_MAP.md'
t = p.read_text()
a = '| apps-script-sheets | не начат | — |'
if a in t:
    t = t.replace(a, f'| apps-script-sheets | идёт: синтез готов, текст в зеркале `skills/apps-script-sheets/`, ждёт заливки zip (позиции AJ-5, AJ-16) — отчёт `{REP}`; адреса этой карты вида `apps-script-sheets/SKILL.md:<строка>` ведут в текст на коммите aeb4b23 | 2026-10-21 |', 1)
    p.write_text(t); out.append('map')
print('\n'.join(out))
