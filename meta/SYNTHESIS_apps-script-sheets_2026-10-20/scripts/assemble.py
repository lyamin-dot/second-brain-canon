#!/usr/bin/env python3
"""Assemble the commit of the apps-script-sheets synthesis into CLONE from existing files (route 9.4(b)).
Usage: assemble.py ROOT CLONE"""
import sys, pathlib, shutil, subprocess
root = pathlib.Path(sys.argv[1]); clone = pathlib.Path(sys.argv[2]); w = root / 'work'
D = clone / 'meta/SYNTHESIS_apps-script-sheets_2026-10-20'
# 1. mirror = new text (copied, not typed)
m = clone / 'skills/apps-script-sheets'
for p in (root / 'new').rglob('*.md'):
    dst = m / p.relative_to(root / 'new'); dst.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, dst)
# 2. report + folder
shutil.copyfile(w / 'REPORT.md', clone / 'meta/SYNTHESIS_apps-script-sheets_2026-10-20.md')
D.mkdir(parents=True, exist_ok=True); (D / 'scripts').mkdir(exist_ok=True)
names = ['units_A_sonnet.md', 'units_A_opus.md', 'units_B_sonnet.md', 'units_C_sonnet.md', 'units_D_sonnet.md',
         'verdicts_A_sonnet.md', 'verdicts_A_opus.md', 'verdicts_B_sonnet.md', 'verdicts_C_sonnet.md', 'verdicts_D_sonnet.md',
         'BASIS_A.md', 'BASIS_B.md', 'BASIS_C.md', 'BASIS_D.md', 'PARTICULARS_A.md', 'PARTICULARS_B.md', 'PARTICULARS_C.md', 'PARTICULARS_D.md',
         'WRITER_REPORT_A.md', 'WRITER_REPORT_B.md', 'WRITER_REPORT_C.md', 'WRITER_REPORT_D.md',
         'A_round1_diff.md', 'B_round1_diff.md', 'C_round1_diff.md', 'D_round1_diff.md', 'ACCEPTANCE_opus.md', 'RETEST.md']
for n in names: shutil.copyfile(w / n, D / n)
for src, dst in [('WRITER_BRIEF.md', 'BRIEF_WRITER.md'), ('CHECKER_BRIEF.md', 'BRIEF_CHECKER.md'), ('VERIFY_BRIEF.md', 'BRIEF_VERIFY.md')]:
    shutil.copyfile(root / 'in' / src, D / dst)
for p in (w / 'scripts').glob('*.py'): shutil.copyfile(p, D / 'scripts' / p.name)
# 3. carriers and statuses (idempotent scripts)
subprocess.run([sys.executable, str(w / 'scripts/apply_carriers.py'), str(clone)], check=True)
subprocess.run([sys.executable, str(w / 'scripts/apply_status.py'), str(clone)], check=True)
# 4. task file: append result section
t = clone / 'labs/sys/t-knowledge-synthesis.md'
txt = t.read_text()
sec = (w / 'TASK_SECTION.md').read_text()
if sec.splitlines()[0] not in txt:
    t.write_text(txt.rstrip('\n') + '\n\n' + sec)
# 5. INDEX row: one phrase appended to the row of this task
ix = clone / 'labs/sys/INDEX.md'
lines = ix.read_text().split('\n')
k = [i for i, l in enumerate(lines) if l.startswith('| `t-knowledge-synthesis.md` |')]
assert len(k) == 1
add = '; синтез `apps-script-sheets` готов 2026-10-21 без потерь (`meta/SYNTHESIS_apps-script-sheets_2026-10-20.md`), мост gas-bridge внесён, зеркало обновлено, ждёт заливки zip'
row = lines[k[0]]
if 'SYNTHESIS_apps-script-sheets' not in row:
    a = ' | РЫЧАГ | 2026-10-18 |'
    assert row.endswith(a)
    lines[k[0]] = row[:-len(a)] + add + a
    ix.write_text('\n'.join(lines))
print('assembled')
