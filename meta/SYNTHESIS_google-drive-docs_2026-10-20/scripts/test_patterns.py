import re,sys,json
pats={
"gdocs-read":r"\|Claude . Google Docs Read \(full\)\|active\|",
"gdocs-append v2":r"\|Claude . Google Docs Append v2 \(verified\)\|active\|",
"gdocs-replace v2":r"\|Claude . Google Docs Replace v2 \(verified\)\|active\|",
"gdocs-overwrite v2":r"\|Claude . Google Docs Overwrite v2 \(verified\)\|active\|",
"create_folder":r"\|Claude . Create Folder\|active\|",
"gsheets-read":r"\|Claude . Google Sheets Read\|active\|",
"gsheets-append":r"\|Claude . Google Sheets Append\|active\|",
}
lines=open(sys.argv[1],encoding='utf-8').read().split('\n')
for k,p in pats.items():
    m=[l for l in lines if re.search(p,l)]
    print(f"{k}: {len(m)} match -> {m[0].split('|')[1] if len(m)==1 else m}  | JSON: {json.dumps(p)}")
    assert p.isascii()
