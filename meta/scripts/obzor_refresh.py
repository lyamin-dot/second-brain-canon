#!/usr/bin/env python3
"""meta/scripts/obzor_refresh.py — пересборка страницы obzor по расписанию (фаза Ф3, projects/obzor/).

Запуск: python3 obzor_refresh.py <клон только для этой задачи> <страница.html>
Шаги: 1) git pull --ff-only клона; 2) obzor_build.py из этого же клона; 3) проверка объекта —
в JSON-блоке страницы built = сегодня и commit = голова клона. Любой провал — код возврата 1 и
строка «ОШИБКА: …»; публикацию делает вызывающий только при коде 0 (Skill second-brain-engineer, Р23).
Клон отдельный: рабочий клон сессий может нести незакоммиченные правки, и pull в нём упадёт.
"""
import datetime as dt, json, os, re, subprocess, sys

def fail(msg):
    print("ОШИБКА:", msg)
    sys.exit(1)

if len(sys.argv) != 3:
    fail("нужно два аргумента: <клон> <страница.html>")
ROOT, PAGE = sys.argv[1], sys.argv[2]
if not os.path.isdir(os.path.join(ROOT, ".git")):
    fail(f"нет клона: {ROOT}")
if not os.path.isfile(PAGE):
    fail(f"нет страницы: {PAGE}")

r = subprocess.run(["git", "-C", ROOT, "pull", "--ff-only", "-q"], capture_output=True, text=True, encoding="utf-8")
if r.returncode:
    fail("git pull: " + (r.stderr or r.stdout).strip())
head = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()

build = os.path.join(ROOT, "meta", "scripts", "obzor_build.py")
r = subprocess.run([sys.executable, "-X", "utf8", build, ROOT, PAGE], capture_output=True, text=True, encoding="utf-8")
print(r.stdout.strip())
if r.returncode:
    fail("obzor_build.py завершился кодом %d" % r.returncode)

m = re.search(r'<script id="data" type="application/json">(.*?)</script>', open(PAGE, encoding="utf-8").read(), re.S)
if not m:
    fail("в странице нет JSON-блока")
d = json.loads(m.group(1))
today = dt.date.today().isoformat()
if d.get("built") != today or d.get("commit") != head:
    fail(f"страница не обновлена: built={d.get('built')} commit={d.get('commit')}, ожидалось {today} {head}")
print(f"OK built={today} commit={head}")
