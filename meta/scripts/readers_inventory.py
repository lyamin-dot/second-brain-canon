#!/usr/bin/env python3
"""meta/scripts/readers_inventory.py — Опись читателей канона: кто и что читает, во что обходится старт.

Запуск: python3 readers_inventory.py <путь к клону> [--md]
Читает только клон (git, файлы). Ничего не пишет в репозиторий.

Колонки на проект / лабораторию:
  папка | вид | статус по реестру | Claude Project (да/нет) |
  мастер-промпт в meta/prompts (да/нет) | кто ещё ссылается на папку в meta/prompts |
  STATE.md байт (бюджет 8192) | PLAN.md байт (бюджет 10240) | LOG.md байт | INDEX.md байт |
  дата последнего коммита STATE/INDEX | коммитов в папку за 30 дней
"""
import os, re, subprocess, sys, datetime as dt

ROOT = sys.argv[1]
MD = "--md" in sys.argv
BUDGET = {"STATE.md": 8192, "PLAN.md": 10240}

def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout.strip()

def size(p):
    return os.path.getsize(p) if os.path.exists(p) else None

def last_commit(path):
    d = git("log", "-1", "--format=%cs", "--", path)
    return d or "—"

def commits_since(path, days=30):
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    out = git("log", f"--since={since}", "--format=%h", "--", path)
    return len(out.splitlines()) if out else 0

# реестр проектов: папка -> (статус, есть ли Claude Project)
reg = {}
with open(os.path.join(ROOT, "registry/projects.md"), encoding="utf-8") as f:
    for line in f:
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and (cells[1].startswith("projects/") or cells[1].startswith("labs/")):
            folder = cells[1].rstrip("/")
            status = cells[3][:40]
            cp = "да" if len(cells) >= 5 and "claude.ai/project" in cells[4] else "нет"
            reg[folder] = (status, cp)

# мастер-промпты: какие папки упоминают
prompts_dir = os.path.join(ROOT, "meta/prompts")
prompt_refs = {}
for fn in os.listdir(prompts_dir):
    text = open(os.path.join(prompts_dir, fn), encoding="utf-8").read()
    for m in set(re.findall(r"(projects|labs)/([a-z0-9\-]+)", text)):
        prompt_refs.setdefault(f"{m[0]}/{m[1]}", []).append(fn.replace(".md", ""))

rows = []
for kind in ("projects", "labs"):
    for name in sorted(os.listdir(os.path.join(ROOT, kind))):
        folder = f"{kind}/{name}"
        p = os.path.join(ROOT, folder)
        if not os.path.isdir(p): continue
        status, cp = reg.get(folder, ("НЕТ В РЕЕСТРЕ", "нет"))
        own_prompt = "да" if os.path.exists(os.path.join(prompts_dir, f"{name}.md")) else "нет"
        refs = sorted(r for r in prompt_refs.get(folder, []) if r != name)
        st = size(os.path.join(p, "STATE.md")); pl = size(os.path.join(p, "PLAN.md"))
        lg = size(os.path.join(p, "LOG.md")); ix = size(os.path.join(p, "INDEX.md"))
        keyfile = "STATE.md" if st is not None else "INDEX.md"
        rows.append(dict(folder=folder, kind="летопись" if kind == "projects" else "лаборатория",
            status=status, cp=cp, prompt=own_prompt, refs=",".join(refs) or "—",
            state=st, plan=pl, log=lg, index=ix,
            over=[k for k, b in BUDGET.items() if (size(os.path.join(p, k)) or 0) > b],
            last=last_commit(f"{folder}/{keyfile}"), c30=commits_since(folder)))

def fmt(v, budget=None):
    if v is None: return "—"
    s = f"{v:,}".replace(",", " ")
    return s + (" ⚠" if budget and v > budget else "")

hdr = ["папка", "вид", "статус (реестр)", "Claude Project", "свой промпт", "ссылки из других промптов",
       "STATE.md", "PLAN.md", "LOG.md", "INDEX.md", "последний коммит STATE/INDEX", "коммитов 30 дн"]
if MD:
    print("| " + " | ".join(hdr) + " |"); print("|" + "---|" * len(hdr))
for r in rows:
    vals = [r["folder"], r["kind"], r["status"], r["cp"], r["prompt"], r["refs"],
            fmt(r["state"], 8192), fmt(r["plan"], 10240), fmt(r["log"]), fmt(r["index"]), r["last"], str(r["c30"])]
    print(("| " + " | ".join(vals) + " |") if MD else "\t".join(vals))
