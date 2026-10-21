#!/usr/bin/env python3
"""Check addresses in BASIS/PARTICULARS files and basis lines in the new Skill.
Usage: check_addresses.py CLONE NEWDIR BASIS_FILES..."""
import re, sys, pathlib, subprocess
clone = pathlib.Path(sys.argv[1]); new = pathlib.Path(sys.argv[2]); files = sys.argv[3:]
path_re = re.compile(r'\b((?:projects|labs|meta|registry|core|skills|wiki|public|test)/[A-Za-z0-9_./\-]+\.(?:md|py|json|txt))')
rec_re = re.compile(r'([РТ]-\d+)[^`\n]{0,40}?(?:журнала|в)\s+`?((?:projects|labs)/[A-Za-z0-9_./\-]+\.md)')
missing_paths, missing_recs, ok_paths, ok_recs = set(), set(), set(), set()
def exists_in_history(p):
    r = subprocess.run(['git', '-C', str(clone), 'log', '--all', '--format=%h', '-1', '--', p], capture_output=True, text=True)
    return bool(r.stdout.strip())
for f in files:
    t = pathlib.Path(f).read_text()
    for p in set(path_re.findall(t)):
        p = p.rstrip('.')
        if (clone / p).exists(): ok_paths.add(p)
        elif exists_in_history(p): ok_paths.add(p + ' (history only)')
        else: missing_paths.add((p, f.split('/out/')[-1]))
    for rec, p in set(rec_re.findall(t)):
        fp = clone / p
        cands = [fp]
        if p.endswith('LOG.md'): cands.append(clone / p.replace('LOG.md', 'LOG_ARCHIVE.md'))
        hit = False
        for c in cands:
            if c.exists() and re.search(r'^' + rec + r' \|', c.read_text(), re.M):
                hit = True; break
        (ok_recs if hit else missing_recs).add((rec, p, f.split('/out/')[-1]))
print('paths ok', len(ok_paths), 'missing', len(missing_paths))
for m in sorted(missing_paths): print('  MISSING PATH', m)
print('records ok', len(ok_recs), 'missing', len(missing_recs))
for m in sorted(missing_recs): print('  MISSING REC', m)
# basis lines form
form = re.compile(r'Основание: (\d+ случа(?:й|я|ев)[^—\n]*— отчёт синтеза, правило [^.\n]+|решение Андрея[^\n]*)')
bad = []
for p in sorted(new.rglob('*.md')):
    for i, l in enumerate(p.read_text().splitlines(), 1):
        for m in re.finditer(r'Основание:[^\n]{0,160}', l):
            if not form.match(m.group(0)): bad.append((p.name, i, m.group(0)[:120]))
print('basis lines not in form:', len(bad))
for b in bad[:40]: print('  ', b)
