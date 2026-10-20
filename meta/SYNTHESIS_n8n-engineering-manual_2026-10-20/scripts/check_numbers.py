#!/usr/bin/env python3
"""Check that every numbered anchor of the old Skill exists in the new Skill.
Usage: check_numbers.py OLD_DIR NEW_DIR
Anchors: A1, A2, section headings '## N.', '### N.N', R-roots '**R..', T-templates '### T..', §4.x items."""
import re, sys, pathlib

def anchors(d):
    d = pathlib.Path(d)
    txt = {}
    for p in sorted(d.rglob('*.md')):
        if 'INCIDENT_LOG' in p.name or 'roots_part' in p.name:
            continue
        txt[p.relative_to(d).as_posix()] = p.read_text()
    found = {}
    pats = [
        (r'^#{2,4}\s+(A[12])\b', 'axiom'),
        (r'^##\s+(\d+)\.', 'section'),
        (r'^###\s+(\d+\.\d+)\b', 'sub'),
        (r'^\*\*(R\d+[ab]?)\.', 'root'),
        (r'^#{2,4}\s+(T\d)\b', 'template'),
        (r'^\*\*(\d+\.\d+)\.?\s', 'item'),
        (r'^(4\.\d+)\.?\s', 'item'),
        (r'^#{3,4}\s+(4\.\d+)\b', 'item'),
    ]
    for f, t in txt.items():
        for line in t.splitlines():
            for pat, kind in pats:
                m = re.match(pat, line)
                if m:
                    found.setdefault(m.group(1), set()).add(f)
    return found

old, new = anchors(sys.argv[1]), anchors(sys.argv[2])
missing = sorted(set(old) - set(new))
moved = sorted(k for k in old if k in new and old[k] != new[k])
print('old anchors', len(old), 'new anchors', len(new))
print('MISSING:', missing)
print('MOVED FILE:', [(k, sorted(old[k]), sorted(new[k])) for k in moved])
print('NEW ONLY:', sorted(set(new) - set(old)))
