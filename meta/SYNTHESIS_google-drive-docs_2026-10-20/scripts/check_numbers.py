#!/usr/bin/env python3
"""Check that every numbered anchor of the old google-drive-docs Skill exists in the new one.
Usage: check_numbers.py OLD_DIR NEW_DIR
Anchors: headings '## N.' and '### N.N' (incl. 4.0а), error codes E01..E21 in table rows."""
import re, sys, pathlib
def anchors(d):
    d = pathlib.Path(d); found = {}
    for p in sorted(d.rglob('*.md')):
        f = p.relative_to(d).as_posix()
        for line in p.read_text().splitlines():
            m = re.match(r'^#{2,4}\s+(\d+(?:\.\d+[а-я]?)?)[.\s]', line)
            if m: found.setdefault('§' + m.group(1), set()).add(f)
            for e in re.findall(r'^\|\s*(E\d\d(?:[–-]E\d\d)?)\s*\|', line):
                found.setdefault(e, set()).add(f)
    return found
old, new = anchors(sys.argv[1]), anchors(sys.argv[2])
print('old anchors', len(old), 'new anchors', len(new))
print('MISSING:', sorted(set(old) - set(new)))
print('MOVED FILE:', [(k, sorted(old[k]), sorted(new[k])) for k in sorted(old) if k in new and old[k] != new[k]])
print('NEW ONLY:', sorted(set(new) - set(old)))
