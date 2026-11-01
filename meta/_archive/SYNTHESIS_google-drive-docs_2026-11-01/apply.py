"""Применяет правки edits.py к копии живого Skill.
Запуск: python -I apply.py <папка живого Skill> <папка результата> <папка для текстов было/стало>
Каждый текст «было» обязан встретиться в файле ровно столько раз, сколько назначено (обычно один); иначе стоп без записи."""
import os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edits

src, dst, dump = sys.argv[1:4]
if os.path.exists(dst):
    shutil.rmtree(dst)
shutil.copytree(src, dst)
os.makedirs(dump, exist_ok=True)

def rd(p):
    with open(os.path.join(dst, p), encoding='utf-8', newline='') as f:
        return f.read()

def wr(p, t):
    with open(os.path.join(dst, p), 'w', encoding='utf-8', newline='') as f:
        f.write(t)

def apply(stage, lst):
    for i, (p, old, new, n) in enumerate(lst, 1):
        t = rd(p)
        c = t.count(old)
        if c != n:
            sys.exit(f'СТОП {stage}#{i} {p}: «было» найдено {c} раз, ожидалось {n}: {old[:80]!r}')
        if new.count(old) and old in new and t.replace(old, new).count(new) != n:
            sys.exit(f'СТОП {stage}#{i}: проверка замены')
        wr(p, t.replace(old, new))
        print(f'{stage}#{i:02} {p}: найдено {c} — заменено')

apply('этап0', edits.STAGE0)

# §5 infra.md: старый текст раздела — между маркерами, каждый ровно один раз
p = 'references/infra.md'
t = rd(p)
a, b = t.count(edits.INFRA5_OLD_START), t.count(edits.INFRA5_OLD_END)
if (a, b) != (1, 1):
    sys.exit(f'СТОП §5: маркеры найдены {a} и {b} раз')
s = t.index(edits.INFRA5_OLD_START)
e = t.index(edits.INFRA5_OLD_END) + len(edits.INFRA5_OLD_END)
old5 = t[s:e]
with open(os.path.join(dump, 'infra5_old.md'), 'w', encoding='utf-8', newline='') as f:
    f.write(old5)
with open(os.path.join(dump, 'infra5_new.md'), 'w', encoding='utf-8', newline='') as f:
    f.write(edits.INFRA5_NEW)
wr(p, t[:s] + edits.INFRA5_NEW + t[e:])
print('этап1 §5 references/infra.md: раздел найден 1 раз — заменён')

apply('этап1', edits.STAGE1)
print('ГОТОВО')
