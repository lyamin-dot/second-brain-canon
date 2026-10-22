#!/usr/bin/env python3
"""meta/scripts/reading_cost.py — модель цены чтения сессии по видам сессий.

Считает, сколько байт обязана прочитать сессия каждого вида, складывая файлы,
которые называют таблицы «Что читать дальше» Skills и мастер-промпт SYS.
Это разовый расчёт, не монитор: запускается по слову, результат — таблица в канон.

Запуск из корня клона репозитория second-brain-canon:
    python3 meta/scripts/reading_cost.py [--skills <папка Skills>] [--project <папка проекта>] [--md]

По умолчанию Skills берутся из зеркала skills/ репозитория (только собственные Skills Андрея).
Живой каталог (/mnt/skills/plugins) содержит ещё Skills Anthropic: их описания тоже лежат
в каждом чате, поэтому слой описаний у живого каталога больше — передать --skills /mnt/skills/plugins.

Коэффициент токенов — 0,37 токена на байт (замер цены русского текста, second-brain-git 8.2);
это оценка на выходе модели, а не замер чтения; сами байты — факт.
"""
import argparse, os, re, sys

TOK = 0.37

def size(path):
    return os.path.getsize(path) if os.path.exists(path) else None

def description_bytes(skills_root):
    total, n = 0, 0
    for d in sorted(os.listdir(skills_root)):
        p = os.path.join(skills_root, d, 'SKILL.md')
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8').read()
        m = re.search(r'^description:\s*(.*?)$', t, re.M)
        if m:
            total += len(m.group(1).encode()); n += 1
    return total, n

def manifest_list(repo):
    t = open(os.path.join(repo, 'core/MANIFEST.md'), encoding='utf-8').read()
    sec = t.split('## Список', 1)[1].split('## ', 1)[0]
    return re.findall(r'^\|\s*\d+\s*\|\s*(core/[^|\s]+)\s*\|', sec, re.M)

def session_types(repo, sk, project):
    S = lambda name, *rel: [os.path.join(sk, name, *rel)]
    core = ['core/MANIFEST.md'] + manifest_list(repo)
    base = (S('second-brain-engineer', 'SKILL.md') + S('second-brain-git', 'SKILL.md')
            + core + ['labs/sys/INDEX.md', 'meta/PENDING_RULES.md'])
    sbg = lambda f: S('second-brain-git', 'references', f)
    sbe = lambda f: S('second-brain-engineer', 'references', f)
    return [
        ('S1 старт сессии SYS (до первого ответа)', base),
        ('S2 SYS + первая запись в репозиторий (лаборатория)', base + sbg('write.md') + sbg('lab.md')),
        ('S2б то же + отказ GitHub или параллельная сессия', base + sbg('write.md') + sbg('lab.md') + sbg('delivery.md')),
        ('S3 SYS + !save', base + sbe('commands.md') + sbe('save.md') + sbg('write.md') + sbg('lab.md')),
        ('S4 SYS + правка воркфлоу n8n', base + sbe('permissions.md') + S('n8n-engineering-manual', 'SKILL.md')
            + S('n8n-engineering-manual', 'references', 'write.md')),
        ('S4б то же + диагностика «почему не работает»', base + sbe('permissions.md') + S('n8n-engineering-manual', 'SKILL.md')
            + S('n8n-engineering-manual', 'references', 'write.md') + S('n8n-engineering-manual', 'references', 'roots.md')
            + [p for p in S('n8n-engineering-manual', 'references', 'roots-silent.md') if os.path.exists(p)]),
        # с 2026-10-22 roots.md — закон, указатель и таблица «симптом → корень»; корни — в файлах по моменту действия;
        # в S4б считается худший случай — самый большой файл корней (roots-silent.md); S4в — проектирование логики
        ('S4в SYS + проектирование логики воркфлоу (механика движка)', base + sbe('permissions.md') + S('n8n-engineering-manual', 'SKILL.md')
            + S('n8n-engineering-manual', 'references', 'engine.md')
            + [p for f in ('engine-flow.md', 'engine-http.md') for p in S('n8n-engineering-manual', 'references', f) if os.path.exists(p)]),
        ('S5 SYS + выдача наряда', base + sbe('permissions.md') + S('naryad', 'SKILL.md') + S('naryad', 'references', 'issuer.md')),
        ('S6 SYS + проектирование (метод Р19)', base + sbe('design.md')),
        ('S7 SYS + харвест', base + sbe('commands.md') + sbe('harvest.md') + ['meta/PROTOCOL_harvest.md',
            'meta/PROTOCOL_lesson-triage.md', 'meta/PROTOCOL_knowledge-synthesis.md']),
        (f'S8 старт repo-проекта ({project}: STATE + PLAN)', S('second-brain-engineer', 'SKILL.md') + S('second-brain-git', 'SKILL.md')
            + sbe('start.md') + core + ['meta/PENDING_RULES.md', f'{project}/STATE.md', f'{project}/PLAN.md']),
        ('S9 старт Docs-проекта (INDEX в Google Docs не считается — живёт в Drive)', S('second-brain-engineer', 'SKILL.md')
            + sbe('start.md') + S('google-drive-docs', 'SKILL.md') + S('google-drive-docs', 'references', 'docs-read.md') + core),
        ('S10 работа с книгой Google Sheets через Apps Script', S('second-brain-engineer', 'SKILL.md') + sbe('start.md') + core
            + S('google-drive-docs', 'SKILL.md') + S('google-drive-docs', 'references', 'sheets.md')
            + S('apps-script-sheets', 'SKILL.md') + S('apps-script-sheets', 'references', 'book-traps.md')),
    ]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--skills', default='skills')
    ap.add_argument('--project', default='projects/kontext-reduktion')
    ap.add_argument('--md', action='store_true', help='печатать таблицу Markdown')
    a = ap.parse_args()
    repo = os.getcwd()
    desc, n = description_bytes(a.skills)
    rows = []
    for name, files in session_types(repo, a.skills, a.project):
        parts, missing, total = [], [], desc
        for f in files:
            s = size(f)
            if s is None:
                missing.append(f); continue
            total += s
            parts.append((os.path.relpath(f, a.skills) if f.startswith(a.skills) else f, s))
        rows.append((name, total, parts, missing))
    print(f'Описания Skills ({n} файлов SKILL.md в {a.skills}): {desc} Б — входят в каждый вид сессии')
    if a.md:
        print('\n| Вид сессии | Байт | ≈ токенов (0,37/Б) | Файлы (байт) |\n|---|---|---|---|')
        for name, total, parts, missing in rows:
            fl = '; '.join(f'{p} {s}' for p, s in parts)
            if missing: fl += '; НЕТ ФАЙЛА: ' + ', '.join(missing)
            print(f'| {name} | {total:,} | {round(total*TOK/1000):,} тыс. | описания {desc}; {fl} |'.replace(',', ' '))
    else:
        for name, total, parts, missing in rows:
            print(f'\n{name}: {total} Б ≈ {round(total*TOK)} токенов')
            for p, s in parts: print(f'   {s:7d}  {p}')
            for m in missing: print(f'   НЕТ ФАЙЛА {m}')

if __name__ == '__main__':
    main()
