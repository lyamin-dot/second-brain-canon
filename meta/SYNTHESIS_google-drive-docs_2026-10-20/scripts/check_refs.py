#!/usr/bin/env python3
"""Find references to google-drive-docs numbers (§N, раздел N, E-codes) in repo and other Skills; check each exists in NEW.
Usage: check_refs.py CLONE NEWDIR"""
import re,sys,pathlib,subprocess
clone=pathlib.Path(sys.argv[1]); new=pathlib.Path(sys.argv[2])
anch=set()
for p in new.rglob('*.md'):
    for l in p.read_text().splitlines():
        m=re.match(r'^#{2,4}\s+(\d+(?:\.\d+[а-я]?)?)[.\s]',l)
        if m: anch.add(m.group(1))
        anch.update(re.findall(r'^\|\s*(E\d\d)',l))
anch.update({'E08','E09','E10'})
files=[p for p in clone.rglob('*.md') if '.git' not in p.parts and 'skills/google-drive-docs' not in p.as_posix() and 'SYNTHESIS_google-drive-docs' not in p.as_posix()]
bad=[];ok=0
for p in files:
    for i,l in enumerate(p.read_text(errors='replace').splitlines(),1):
        for m in re.finditer(r'google-drive-docs',l):
            tail=l[m.end():m.end()+120]
            for r in re.findall(r'(?:§\s?|раздела?\s|разделы\s|пункт\s)(\d+(?:\.\d+[а-я]?)?)|\b(E\d\d)\b',tail):
                n=r[0] or r[1]
                if n in anch or n.split('.')[0] in anch and '.' in n and n in anch: ok+=1
                elif n in anch: ok+=1
                else: bad.append((p.relative_to(clone).as_posix(),i,n,l[m.start():m.start()+140]))
print('refs ok',ok,'bad',len(bad))
for b in bad: print(' ',b)
