#!/usr/bin/env python3
"""naryad synthesis checks: anchors, external refs, И-7 scan, header, basis form.
Usage: check_naryad.py NEWDIR CLONE SKILLSDIR"""
import re,sys,pathlib
new=pathlib.Path(sys.argv[1]); clone=pathlib.Path(sys.argv[2]); sk=pathlib.Path(sys.argv[3])
txt={p.relative_to(new).as_posix():p.read_text() for p in new.rglob('*.md')}
allnew='\n'.join(txt.values())
need=['3.1','3.1а','3.2','3.3','3.4','3.5','3.6','3.7','3.8','3.9']
miss=[n for n in need if not re.search(r'(?m)^(#+\s*)?'+re.escape(n)+r'[\s.]',allnew)]
for n in ['4','5','6','7','8']:
    if not re.search(r'(?m)^#+\s*'+n+r'\.?\s',allnew) and not re.search(r'(?m)^'+n+r'\.\s+Контракт',allnew): miss.append(n)
for w in ['Ограничители','Приёмка','Пересмотр','Чего этот Skill НЕ определяет','Границы','Контракт Руководителя','Контракт Прораба','Контракт Исполнителя']:
    if w not in allnew: miss.append(w)
print('missing anchors:',miss)
# numbered questions in 3.1 (1-4), 3.1а (1-3), revision (1-8)
rev=txt.get('references/revision.md','')
print('revision questions:',sorted(set(re.findall(r'(?m)^(\d)\.\s',rev))))
# external refs
pat=re.compile(r'naryad[^\n]{0,80}?(§\s?\d+(?:\.\d+[а-я]?)?(?:\([а-я]\))?)')
bad=[];ok=0
for root in [clone,sk]:
    for p in root.rglob('*.md'):
        s=p.as_posix()
        if '.git/' in s or '/skills/naryad' in s or 'plugins/naryad' in s or 'SYNTHESIS_naryad' in s: continue
        for i,l in enumerate(p.read_text(errors='replace').splitlines(),1):
            for m in pat.finditer(l):
                n=re.sub(r'[§\s]','',m.group(1)); base=re.sub(r'\(.*','',n)
                if re.search(r'(?m)^(#+\s*)?'+re.escape(base)+r'[\s.]',allnew) or re.search(r'(?m)^#+\s*'+re.escape(base)+r'\.?\s',allnew): ok+=1
                else: bad.append((s.split('second-brain-canon/')[-1].split('clone_ro/')[-1],i,n))
print('external § refs ok',ok,'bad',len(bad))
for b in bad[:30]: print('  ',b)
pats={'google_id':r'\b[A-Za-z0-9_-]{28,}\b','n8n_wf':r'\b(?=[A-Za-z0-9]{16}\b)(?=[^ ]*\d)(?=[^ ]*[A-Z])[A-Za-z0-9]{16}\b','webhook':r'/webhook','email':r'[\w.+-]+@[\w-]+\.[a-z]{2,}','hist':r'ИСТОРИЯ ДИАГНОЗА|Version 1\.|Правка 1\.\d+|Supersedes'}
for f,t in txt.items():
    for i,l in enumerate(t.splitlines(),1):
        for k,p in pats.items():
            for mm in re.finditer(p,l): print(f'{k}: {f}:{i}: {mm.group(0)[:50]}')
    red=[l for l in t.splitlines() if l.startswith('Редакция')]
    if f=='SKILL.md': print('Редакция lines in SKILL.md:',len(red))
ok=re.compile(r'Основание: (\d+ случа\w+|\d+ замер|решение|слово|предпочтение)')
for f,t in txt.items():
    for i,l in enumerate(t.splitlines(),1):
        for m in re.finditer(r'Основание[^:]{0,3}:[^\n]{0,60}',l):
            if not ok.match(m.group(0)): print('basis-form?',f,i,m.group(0)[:90])
d=re.search(r'^description:\s*"(.*)"\s*$',txt['SKILL.md'],re.M)
print('description chars', len(d.group(1)) if d else None)
