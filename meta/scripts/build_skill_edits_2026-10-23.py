# meta/scripts/build_skill_edits_2026-10-23.py
#!/usr/bin/env python3
"""Apply Skill edits 2026-10-23 to copies of live Skills and build upload zips.
Every replacement must match exactly once in the live text, otherwise stop.
Run: python3 -I build_skill_edits_2026-10-23.py <out_dir> <clone>/meta/DRAFT_descriptions_2026-10-22.md
Source of truth for each text: Р10 and the write.md stop — composed 2026-10-23 (report meta/TEST_skill-layers_2026-10-22_report.md);
items 6, 7, 11, 13, 14, 18, 20, Г1 — meta/EDITS_skills_2026-10-22.md; descriptions — meta/DRAFT_descriptions_2026-10-22.md
(n8n-engineering-manual description extended by diagnosis phrases 2026-10-23).
The full replacement texts live in the Skills themselves after upload and in the mirror skills/ once it is updated."""
import os, re, shutil, sys, zipfile, yaml

LIVE = "/mnt/skills/plugins"
OUT = sys.argv[1]
DRAFT = sys.argv[2]
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

def copy(skill):
    dst = os.path.join(OUT, "src", skill)
    if not os.path.exists(dst):
        shutil.copytree(os.path.join(LIVE, skill), dst)
    return dst

def rep(skill, rel, old, new):
    p = os.path.join(copy(skill), rel)
    t = open(p, encoding="utf-8").read()
    n = t.count(old)
    if n != 1:
        sys.exit(f"STOP {skill}/{rel}: anchor count {n}: {old[:70]!r}")
    open(p, "w", encoding="utf-8").write(t.replace(old, new))
    print(f"ok  {skill}/{rel}: {old[:60]!r}")

def set_desc(skill, desc):
    if '"' in desc or "\\" in desc:
        sys.exit(f"STOP {skill}: quote or backslash in description")
    if len(desc) > 1024:
        sys.exit(f"STOP {skill}: description {len(desc)} > 1024")
    p = os.path.join(copy(skill), "SKILL.md")
    t = open(p, encoding="utf-8").read()
    head, fm, body = t.split("---", 2)
    lines = fm.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("description:")]
    if len(idx) != 1:
        sys.exit(f"STOP {skill}: description line count {len(idx)}")
    lines[idx[0]] = f'description: "{desc}"'
    fm2 = "\n".join(lines)
    if yaml.safe_load(fm2)["description"] != desc:
        sys.exit(f"STOP {skill}: yaml roundtrip")
    open(p, "w", encoding="utf-8").write(head + "---" + fm2 + "---" + body)
    print(f"desc {skill}: {len(desc)}")

# Edits applied (anchor -> anchor plus added text; exact texts are in the uploaded Skills):
# 1. second-brain-engineer/SKILL.md: new section «Р10. Воркфлоу n8n — вопрос до вызова» inserted before «## Р14. Запреты».
# 2. second-brain-engineer/references/permissions.md: Р10 ДЕЙСТВИЕ question form replaced by pointer to SKILL.md Р10.
# 3. n8n-engineering-manual/references/write.md: «СТОП ПЕРЕД ПЕРВЫМ МЕНЯЮЩИМ ВЫЗОВОМ» paragraph before «## 2. Запись через MCP».
# 4. item 6  — second-brain-engineer/references/catalog-hygiene.md, after «особенностью не является и в Skill идёт.»
# 5. item 7  — apps-script-sheets/SKILL.md, after «Гейт обязателен — и тогда, когда сессия пишет код мостом сама.»
# 6. item 11 — avtopilot/SKILL.md, between ««запускай».» and «Молчание согласием не считается.»
# 7. item 20 — second-brain-engineer/references/permissions.md, after «поручение не переносится на другие задачи и сессии.»
# 8. item 18 — apps-script-sheets/SKILL.md, after «§1, абзац «Книга скрипту не принадлежит».»
# 9. item 13 — second-brain-engineer/references/design.md, point 18 before «Пункты 9, 14 и 15»; SKILL.md table «пункты 1–8, 10–13 и 18».
# 10. item 14 — new file second-brain-engineer/references/scheduled-scripts.md (Р23) and table row before the basis.md row.
# 11. Г1 — second-brain-git/references/delivery.md, table 9.3 row «Git Append File» after the «Git Append» row.
# 12. descriptions — «Стало:» lines of the draft for every Skill that exists live (clasp-apps-script skipped: not live).

def apply_descriptions():
    draft = open(DRAFT, encoding="utf-8").read()
    for sec in re.split(r"^### ", draft, flags=re.M)[1:]:
        name = sec.split(" ", 1)[0]
        m = re.search(r"^Стало: (.*)$", sec, re.M)
        if not m or not os.path.isdir(os.path.join(LIVE, name)):
            print(f"skip {name}")
            continue
        desc = m.group(1).strip()
        if name == "n8n-engineering-manual":
            anchor = "«посмотреть, почему не работает». "
            if desc.count(anchor) != 1:
                sys.exit("STOP n8n desc anchor")
            desc = desc.replace(anchor, anchor + "Диагностика — это и вопрос без правки: «отработал зелёным, а данных нет», «почему ноль совпадений», «почему пропали настройки после записи». ")
        set_desc(name, desc)

def check_and_zip():
    for skill in sorted(os.listdir(os.path.join(OUT, "src"))):
        d = os.path.join(OUT, "src", skill)
        for root, _, files in os.walk(d):
            for f in files:
                full = os.path.join(root, f)
                livef = os.path.join(LIVE, skill, os.path.relpath(full, d))
                old_lines = set(open(livef, encoding="utf-8").read().split("\n")) if os.path.exists(livef) else set()
                for line in open(full, encoding="utf-8").read().split("\n"):
                    if line in old_lines:
                        continue
                    for bad in ("/webhook/", "Bearer ", "@", "http://", "https://"):
                        if bad in line:
                            sys.exit(f"STOP I-7 new line in {skill}/{f}: {bad}")
        z = os.path.join(OUT, f"{skill}.zip")
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(d):
                for f in sorted(files):
                    full = os.path.join(root, f)
                    zf.write(full, os.path.join(skill, os.path.relpath(full, d)))
        print("zip", z)
