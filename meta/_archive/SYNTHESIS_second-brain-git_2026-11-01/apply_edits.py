"""Накладывает правки «было → стало» на копию Skill.

Вызов: python -I apply_edits.py <файл правок> <папка Skill>
Каждый OLD обязан встретиться в своём файле ровно один раз до наложения,
NEW — ровно один раз после. Любое нарушение — стоп без записи.
"""
import sys
from pathlib import Path

edits_path, skill_dir = Path(sys.argv[1]), Path(sys.argv[2])
blocks, cur, mode = [], None, None
for line in edits_path.read_text(encoding="utf-8").split("\n"):
    if line.startswith("@@@ FILE "):
        cur = {"file": line[9:].strip(), "id": "", "old": [], "new": []}
        mode = None
    elif line.startswith("@@@ ID "):
        cur["id"] = line[7:].strip()
    elif line == "@@@ OLD":
        mode = "old"
    elif line == "@@@ NEW":
        mode = "new"
    elif line == "@@@ END":
        blocks.append(cur)
        cur, mode = None, None
    elif mode:
        cur[mode].append(line)

texts, ok = {}, True
for b in blocks:
    p = skill_dir / b["file"]
    if b["file"] not in texts:
        texts[b["file"]] = p.read_bytes().decode("utf-8")
    old, new = "\n".join(b["old"]), "\n".join(b["new"])
    n = texts[b["file"]].count(old)
    print(f'{b["id"][:4]:5} {b["file"]:28} было найдено: {n}', end="")
    if n != 1:
        print("  <-- СТОП")
        ok = False
        continue
    texts[b["file"]] = texts[b["file"]].replace(old, new)
    m = texts[b["file"]].count(new)
    print(f"; стало найдено: {m}" + ("" if m == 1 else "  <-- СТОП"))
    ok &= m == 1

if not ok:
    sys.exit("правки не записаны")
for f, t in texts.items():
    (skill_dir / f).write_bytes(t.encode("utf-8"))
print(f"записано файлов: {len(texts)}, правок: {len(blocks)}")
