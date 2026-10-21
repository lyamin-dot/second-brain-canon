#!/usr/bin/env python3
"""Checks for the apps-script-sheets synthesis.
Usage: check_ass.py OLD_DIR NEW_DIR
1. numbered anchors (## N., ### N.N) of OLD present in NEW, in the same file;
2. description length (frontmatter) <= 1024;
3. I-7 scan: Google IDs (25+ char base64url), n8n workflow IDs (16 alnum), webhook paths, emails, credential-like words;
4. history markers: 'ИСТОРИЯ ДИАГНОЗА', header lines 'Редакция' count, dates of executions 'исполнени[ея] \\d{4,}';
5. basis lines not in the allowed form."""
import re, sys, pathlib

def files(d):
    d = pathlib.Path(d)
    return {p.relative_to(d).as_posix(): p.read_text() for p in sorted(d.rglob('*.md'))}

def anchors(fs):
    out = {}
    for f, t in fs.items():
        for line in t.splitlines():
            m = re.match(r'^#{2,3}\s+(\d+(?:\.\d+)?)\.?\s', line)
            if m:
                out.setdefault(m.group(1), set()).add(f)
    return out

old, new = files(sys.argv[1]), files(sys.argv[2])
ao, an = anchors(old), anchors(new)
print('anchors old', len(ao), 'new', len(an))
print('MISSING:', sorted(set(ao) - set(an), key=lambda s: [int(x) for x in s.split('.')]))
print('MOVED:', [(k, sorted(ao[k]), sorted(an[k])) for k in ao if k in an and ao[k] != an[k]])
print('NEW ONLY:', sorted(set(an) - set(ao)))

sk = new.get('SKILL.md', '')
m = re.search(r'^description:\s*(.*)$', sk, re.M)
if m:
    d = m.group(1).strip().strip('"')
    print('description chars', len(d))

pats = {
    'google_id': r'\b[A-Za-z0-9_-]{25,}\b',
    'n8n_wf_id': r'`[A-Za-z0-9]{16}`',
    'webhook': r'/webhook',
    'email': r'[\w.+-]+@[\w-]+\.[\w.]+',
    'http': r'https?://',
    'history_diag': r'ИСТОРИЯ ДИАГНОЗА',
    'exec_no': r'исполнени\w*\s+\d{4,}',
}
for f, t in new.items():
    for i, line in enumerate(t.splitlines(), 1):
        for k, p in pats.items():
            for mm in re.finditer(p, line):
                s = mm.group(0)
                if k == 'google_id' and (s.isalpha() or '_' in s and s.replace('_', '').isalpha()):
                    continue
                print(f'{k}: {f}:{i}: {s[:60]}')
    red = [l for l in t.splitlines() if l.startswith('Редакция')]
    if len(red) > 1:
        print(f'header: {f} has {len(red)} Редакция lines')

ok = re.compile(r'^Основание: (\d+ случа\w+|правило конструкции|решение Андрея|предпочтение Андрея|слово Андрея|случая отказа нет|\d+ замер)')
for f, t in new.items():
    for i, line in enumerate(t.splitlines(), 1):
        if line.startswith('Основание') and not ok.match(line):
            print(f'basis-form?: {f}:{i}: {line[:120]}')
