import re,sys
G='gdd/out/'; M='repo/skills/'
def blocks(path):
    t=open(path).read(); t=t[t.index('## Копии'):]; t=t[:t.index('\n## ',5)]
    return t
A=blocks(G+'A/WRITER_REPORT_A.md'); B=blocks(G+'B/WRITER_REPORT_B.md'); C=blocks(G+'C/WRITER_REPORT_C.md')
def q(s,label,which):  # extract «...» after label within item text
    i=s.index(label); j=s.index('«',i); k=s.index('»\n',j) if '»\n' in s[j:] else None
    return s[j+1:k]
def item(t,n):
    i=t.index('\n%d. '%n); j=t.find('\n%d. '%(n+1),i+1); return t[i:j if j>0 else len(t)]
def code(s,k):
    parts=re.findall(r'```\n(.*?)\n\s*```',s,re.S); return parts[k]
edits=[]
a1=item(A,1); edits.append(('n8n-workflow-passport/SKILL.md',q(a1,'Было:',0),q(a1,'Стало:',0)))
a3=item(A,3); edits.append(('n8n-workflow-registry/SKILL.md',q(a3,'Было:',0),q(a3,'Стало:',0)))
a4=item(A,4); old4='| Инструменты чтения и записи Google Docs, Sheets, Drive: ID, поля вызова, верификация | google-drive-docs |'; edits.append(('n8n-workflow-registry/SKILL.md',old4,q(a4,'Стало:',0)))
for n,f in [(1,'n8n-workflow-passport/SKILL.md'),(2,'n8n-workflow-passport/SKILL.md'),(3,'context-handoff/SKILL.md')]:
    b=item(B,n); edits.append((f,q(b,'Было:',0),q(b,'Стало',0)))
c1=item(C,1); 0 and edits.append(('apps-script-sheets/SKILL.md',code(c1,0).strip(),code(c1,1).strip()))
c2=item(C,2); anchor='Очищать — только свои диапазоны, перечисленные в скрипте явно.'; 0 and edits.append(('apps-script-sheets/SKILL.md',anchor,anchor+' '+code(c2,0).strip()))
c5=item(C,5); edits.append(('n8n-workflow-registry/SKILL.md',code(c5,0).strip(),code(c5,1).strip()))
dry = len(sys.argv)>1 and sys.argv[1]=='dry'
for f,o,n in edits:
    p=M+f; t=open(p).read(); c=t.count(o)
    print(f, 'count',c, '|', o[:60], '=>', n[:60])
    if c!=1: continue
    if not dry: open(p,'w').write(t.replace(o,n))
