#!/usr/bin/env python3
"""meta/scripts/obzor_build.py — данные страницы «что у меня в разработке» (проект projects/obzor/).

Запуск: python3 obzor_build.py <путь к клону> <страница.html> [--check]
Читает только клон. Пишет только JSON-блок <script id="data"> в файле страницы (страница —
закрытый артефакт, в репозиторий не кладётся: инвариант 1 projects/obzor/PLAN.md).
--check — ничего не пишет, печатает строки и ошибки разбора.

Источники:
  летописи      — блок obzor в начале projects/*/STATE.md (форма — projects/obzor/PLAN.md,
                  «Устройство», пункт 2; строки «> Поле: значение» после строки-метки OBZOR_MARK);
  лаборатории   — строки задач labs/*/INDEX.md (счёт задач, метки, «срок ДД.ММ», упоминание Андрея);
  веса          — строки «ИМЯ вес N» в registry/projects.md;
  дата коммита  — git log папки;
  проекты с INDEX в Google Docs — клоном не читаются: их строки и сроки переносятся из прежней
                  версии страницы как есть (поле src = "docs"), обновляет их сессия (gdocs-read).
"""
import json, os, re, subprocess, sys, datetime as dt

OBZOR_MARK = "<!-- obzor-блок"
STATES = {"в работе": "work", "работает": "run", "пауза": "pause", "идея": "idea", "закрыт": "closed"}
FIELDS = {"Состояние": "st", "Дата": "d", "Что это": "what", "Следующий шаг": "next", "Ждёт Андрея": "wait"}

ROOT, PAGE = sys.argv[1], sys.argv[2]
CHECK = "--check" in sys.argv
errors = []

def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True, encoding="utf-8").stdout.strip()

def last_commit(path):
    return git("log", "-1", "--format=%cs", "--", path) or None

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()

def weights():
    w = {}
    for m in re.finditer(r"^([A-Z][A-Z0-9_]+)\s+вес\s+(\d+)\b", read("registry/projects.md"), re.M):
        w[m.group(1).lower().replace("_", "-")] = int(m.group(2))
    return w

def block(name):
    """Блок obzor из STATE.md летописи: {поле: значение}, сроки — список [дата, текст]."""
    lines = read(f"projects/{name}/STATE.md").splitlines()
    try:
        i = next(k for k, l in enumerate(lines[:12]) if l.startswith(OBZOR_MARK))
    except StopIteration:
        errors.append(f"{name}: блока obzor нет в первых 12 строках STATE.md")
        return None
    row, dues = {"id": name}, []
    for l in lines[i + 1:]:
        if not l.startswith("> "):
            break
        k, _, v = l[2:].partition(":")
        k, v = k.strip(), v.strip()
        if k == "Срок":
            m = re.match(r"(\d{4}-\d{2}-\d{2})\s+[—-]\s+(.+)", v)
            if m: dues.append([m.group(1), m.group(2), name])
            else: errors.append(f"{name}: строка «Срок» не по форме ГГГГ-ММ-ДД — текст: {v}")
        elif k in FIELDS:
            row[FIELDS[k]] = "" if v == "—" else v
        else:
            errors.append(f"{name}: неизвестное поле «{k}»")
    st = row.get("st", "")
    if st not in STATES:
        errors.append(f"{name}: состояние «{st}» не из словаря {list(STATES)}")
    row["st"] = STATES.get(st, "pause")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row.get("d", "")):
        errors.append(f"{name}: поле «Дата» не ГГГГ-ММ-ДД")
        row["d"] = None
    for f in ("what", "next", "wait"):
        row.setdefault(f, "")
    return row, dues

def lab(name):
    """Строка лаборатории из таблицы задач labs/<name>/INDEX.md."""
    tasks = [l for l in read(f"labs/{name}/INDEX.md").splitlines() if re.match(r"\|\s*`t-[^`]+\.md`", l)]
    cells = [[c.strip() for c in l.strip().strip("|").split("|")] for l in tasks]
    marks = {}
    for c in cells:
        for m in ("БЛОКЕР", "РЫЧАГ", "РУТИНА", "ЗОМБИ"):
            if len(c) > 2 and m in c[2]: marks[m] = marks.get(m, 0) + 1
    dues = []
    for c in cells:
        m = re.search(r"срок (\d{2})\.(\d{2})", " ".join(c[2:3]))
        if m:
            y = dt.date.today().year
            d = dt.date(y, int(m.group(2)), int(m.group(1)))
            if d < dt.date.today() - dt.timedelta(days=180): d = d.replace(year=y + 1)
            dues.append([d.isoformat(), f"{c[2]} — {c[0].strip('`')}", f"labs/{name}"])
    # только счёт: текст сути задач может нести признаки доступа (И-7 second-brain-git, классы 1 и 2
    # закрыты и для страницы-артефакта), поэтому на страницу он не выносится
    andrey = sum(1 for c in cells if len(c) > 1 and "Андре" in c[1])
    return {"id": f"lab: {name}", "what": f"Лаборатория {name}, задач: {len(cells)}", "st": "work",
            "d": last_commit(f"labs/{name}/INDEX.md"), "g": last_commit(f"labs/{name}"),
            "next": ", ".join(f"{k}: {v}" for k, v in marks.items()) or "меток нет",
            "wait": f"задач, где названа рука или решение Андрея: {andrey} (labs/{name}/INDEX.md)" if andrey else ""}, dues

def main():
    html = open(PAGE, encoding="utf-8").read()
    m = re.search(r'(<script id="data" type="application/json">)(.*?)(</script>)', html, re.S)
    old = json.loads(m.group(2))
    w = weights()
    projects, dues = [], []
    for name in sorted(os.listdir(os.path.join(ROOT, "projects"))):
        if not os.path.exists(os.path.join(ROOT, "projects", name, "STATE.md")): continue
        r = block(name)
        if not r: continue
        row, du = r
        row["w"] = w.get(name)
        row["g"] = last_commit(f"projects/{name}")
        projects.append(row); dues += du
    for name in sorted(os.listdir(os.path.join(ROOT, "labs"))):
        if not os.path.exists(os.path.join(ROOT, "labs", name, "INDEX.md")): continue
        row, du = lab(name)
        row["w"] = w.get(name)
        projects.append(row); dues += du
    docs = [p for p in old["projects"] if p.get("src") == "docs"]
    ids = {p["id"] for p in docs}
    projects += docs
    dues += [x for x in old["dues"] if x[2] in ids]
    dues.sort()
    new = {"built": dt.date.today().isoformat(), "commit": git("rev-parse", "--short", "HEAD"),
           "docs_read": old.get("docs_read"), "projects": projects, "dues": dues}
    for e in errors: print("ОШИБКА:", e)
    print(f"строк: {len(projects)} (летописей {sum(1 for p in projects if not p['id'].startswith('lab:') and p.get('src') != 'docs')}, "
          f"лабораторий {sum(1 for p in projects if p['id'].startswith('lab:'))}, Docs {len(docs)}); сроков: {len(dues)}")
    if CHECK or errors:
        if errors: sys.exit(1)
        return
    js = json.dumps(new, ensure_ascii=False, indent=1)
    html = html[:m.start(2)] + "\n" + js + "\n" + html[m.end(2):]
    with open(PAGE, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)

main()
