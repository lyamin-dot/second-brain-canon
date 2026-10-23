#!/usr/bin/env python3
"""meta/scripts/trim_skill_for_probe.py

Собирает копию Skill second-brain-engineer для пробы «вредит ли размер постоянного слоя
исполнению» (meta/ROADMAP_post-retro_2026-10-23.md, шаг 3). Копия — не канон и в репозиторий
не кладётся; zip заливается в Customize только на время пробы, после — заливается полный Skill
из зеркала skills/second-brain-engineer/.

Два режима, оба механические (перенабора моделью нет):
  --mode trim     SKILL.md без пояснений: сняты предложения «Почему…», «Признак: …»,
                  строки «[основание: …]». references/ не меняются. Замер 2026-10-23: это
                  около 2,2 КБ из 32,9 — размер почти не меняется, проба на таком варианте
                  размер не проверяет.
  --mode inflate  SKILL.md, в который целиком влиты файлы references/, нужные шести заданиям
                  пробы (start, commands, save, search, permissions, write-moment, outside,
                  intermediary). Строки таблицы «Что читать дальше» остаются, файлы в references/
                  остаются тоже. Это копия, у которой правила заданий стоят в постоянном слое,
                  а не по действию — прямая проверка посылки раскладки по слоям.

Запуск из корня клона:
  python3 meta/scripts/trim_skill_for_probe.py --mode inflate --src skills/second-brain-engineer --out /tmp/probe
Результат: папка <out>/second-brain-engineer/ и zip <out>/second-brain-engineer_<MODE>_<дата>.zip;
на stdout — байты SKILL.md до и после и список влитых или снятых фрагментов.
Приёмка trim: каждая снятая строка или фрагмент напечатаны; остальное побайтно совпадает.
Приёмка inflate: SKILL.md после = SKILL.md до + сумма влитых файлов + разделители (печатается арифметика).
"""
import argparse, os, re, shutil, sys, zipfile, datetime

INFLATE_FILES = ['start.md', 'commands.md', 'save.md', 'search.md', 'permissions.md',
                 'write-moment.md', 'outside.md', 'intermediary.md']

def trim(text):
    removed = []
    out_lines = []
    for line in text.split('\n'):
        if line.startswith('[основание'):
            removed.append(line); continue
        new = line
        for pat in (r'\s?Почему(?:[^:\n]{0,60})?:[^\n]*?(?=(\s\[основание:)|$)',
                    r'\s?Признак:[^\n]*?(?=(\s\[основание:)|$)'):
            for m in list(re.finditer(pat, new)):
                removed.append(m.group(0).strip())
            new = re.sub(pat, '', new)
        new = re.sub(r'\s?\[основание:[^\]]*\]', '', new)
        out_lines.append(new)
    return '\n'.join(out_lines), removed

def inflate(src, text):
    parts = [text.rstrip('\n'), '\n\n---\n\n## ВЛИТО ДЛЯ ПРОБЫ (копии файлов references/, не канон)\n']
    added = []
    total = 0
    for f in INFLATE_FILES:
        p = os.path.join(src, 'references', f)
        body = open(p, encoding='utf-8').read()
        total += len(body.encode('utf-8'))
        parts.append(f'\n\n<!-- references/{f} -->\n\n' + body.rstrip('\n'))
        added.append((f, len(body.encode('utf-8'))))
    return ''.join(parts) + '\n', added, total

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['trim', 'inflate'], required=True)
    ap.add_argument('--src', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    name = os.path.basename(a.src.rstrip('/'))
    dst = os.path.join(a.out, name)
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(a.src, dst)
    sk = os.path.join(dst, 'SKILL.md')
    before = open(sk, encoding='utf-8').read()
    b0 = len(before.encode('utf-8'))
    if a.mode == 'trim':
        after, removed = trim(before)
        open(sk, 'w', encoding='utf-8').write(after)
        print(f'trim: SKILL.md {b0} -> {len(after.encode("utf-8"))} байт; снято фрагментов: {len(removed)}')
        for r in removed: print('  -', r[:110])
    else:
        after, added, total = inflate(a.src, before)
        open(sk, 'w', encoding='utf-8').write(after)
        b1 = len(after.encode('utf-8'))
        print(f'inflate: SKILL.md {b0} -> {b1} байт; влито {len(added)} файлов на {total} байт; разделители {b1 - b0 - total} байт')
        for f, n in added: print(f'  + references/{f} {n}')
    date = datetime.date.today().isoformat()
    zpath = os.path.join(a.out, f'{name}_{a.mode.upper()}_{date}.zip')
    with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(dst):
            for fn in files:
                full = os.path.join(root, fn)
                z.write(full, os.path.relpath(full, a.out))
    print('zip:', zpath)

if __name__ == '__main__':
    main()
