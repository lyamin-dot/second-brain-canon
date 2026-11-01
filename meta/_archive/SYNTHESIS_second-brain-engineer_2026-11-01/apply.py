# Применяет edits.py к копии живого Skill. Каждый якорь обязан найтись ровно один раз.
# Использование: python apply.py <папка копии Skill> <файл отчёта было→стало>
import sys, io, runpy
E = runpy.run_path(sys.argv[2] if len(sys.argv) > 3 else "edits.py")["E"]
root, rep = sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else sys.argv[3]
files = {}
def get(f):
    if f not in files:
        files[f] = io.open(f"{root}/{f}", encoding="utf-8", newline="").read()
    return files[f]
out = io.open(rep, "w", encoding="utf-8")
fail = 0
for n, (op, f, key, new) in enumerate(E, 1):
    t = get(f)
    if op == "R":
        c = t.count(key)
        if c != 1:
            print(f"#{n} {f}: якорь найден {c} раз: {key[:70]!r}"); fail += 1; continue
        files[f] = t.replace(key, new); old, nw = key, new
    elif op == "E":
        add = "\n".join(new) + "\n"
        if not t.endswith("\n"): add = "\n" + add
        files[f] = t + add; old, nw = "(конец файла)", "\n".join(new)
    else:
        lines = t.split("\n")
        idx = [i for i, l in enumerate(lines) if l.startswith(key)]
        if len(idx) != 1:
            print(f"#{n} {f}: начало строки найдено {len(idx)} раз: {key[:70]!r}"); fail += 1; continue
        i = idx[0]; old = lines[i]
        if op == "L": lines[i] = new; nw = new
        elif op == "A": lines[i] = old + new; nw = lines[i]
        elif op == "I": lines[i+1:i+1] = new; nw = old + "\n" + "\n".join(new)
        files[f] = "\n".join(lines)
    out.write(f"## Правка {n} — {f} ({op})\n\nБЫЛО:\n\n```\n{old}\n```\n\nСТАЛО:\n\n```\n{nw}\n```\n\n")
out.close()
if fail:
    print(f"ОТКАЗ: {fail} якорей не прошли проверку, ничего не записано"); sys.exit(1)
for f, t in files.items():
    io.open(f"{root}/{f}", "w", encoding="utf-8", newline="").write(t)
print(f"OK: {len(E)} правок в {len(files)} файлах")
