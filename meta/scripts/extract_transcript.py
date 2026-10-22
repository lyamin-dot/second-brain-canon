# meta/scripts/extract_transcript.py
#!/usr/bin/env python3
"""Выписка из переписки субагента Claude Code: загруженные Skill, чтения, вызовы записи.
Вход: путь к .jsonl (~/.claude/projects/<проект>/<сессия>/subagents/agent-<id>.jsonl); выход: markdown в stdout.
Номер строки = номер строки файла переписки. Классификация «запись» для Bash — эвристика по тексту команды;
вердикт даёт проверяющий по самой переписке (наряд Н-22.10-01, 2026-10-22)."""
import json, sys, re
WRITE_HINTS = re.compile(r'git (commit|push(?! --dry-run)|add|checkout|reset|rm|mv|pull|merge|rebase)\b|(?<![0-9&>])>{1,2}\s*(?!&|/dev/null)[\w./~$"\']|\btee\b|sed -i|\brm |\bmv |\bcp ', re.I)
READ_CMD = re.compile(r'\b(cat|sed -n|head|tail|grep|rg|less|awk|git show|git log|git diff|ls|find|wc)\b')

def short(s, n=300):
    s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    return s.replace('\n', ' ⏎ ')[:n]

p = sys.argv[1]
skills, reads, writes, other = [], [], [], []
for ln, line in enumerate(open(p, encoding='utf-8'), 1):
    try:
        o = json.loads(line)
    except Exception:
        continue
    if o.get('type') != 'assistant':
        continue
    for b in o.get('message', {}).get('content') or []:
        if not isinstance(b, dict) or b.get('type') != 'tool_use':
            continue
        n, i = b.get('name'), b.get('input', {})
        if n == 'Skill':
            skills.append((ln, i.get('skill')))
        elif n == 'Read':
            reads.append((ln, n, i.get('file_path')))
        elif n in ('Grep', 'Glob'):
            reads.append((ln, n, short(i)))
        elif n in ('Write', 'Edit', 'NotebookEdit'):
            writes.append((ln, n, i.get('file_path')))
        elif n == 'Bash':
            c = i.get('command', '')
            (writes if WRITE_HINTS.search(c) else reads if READ_CMD.search(c) else other).append((ln, 'Bash', short(c)))
        elif n.startswith('mcp__n8n__'):
            k = n.split('__')[-1]
            tgt = writes if k in ('update_workflow', 'create_workflow_from_code', 'publish_workflow', 'archive_workflow', 'unpublish_workflow', 'restore_workflow_version') else other
            if k == 'execute_workflow':
                body = (i.get('inputs') or {}).get('webhookData', {}).get('body')
                tgt = writes if body and any(x in json.dumps(body) for x in ('fileId', '"text"', 'files', 'expectedSha', 'newText')) else reads
            tgt.append((ln, n, short(i, 400)))
        elif 'Google_Drive' in n or 'github' in n:
            tgt = writes if re.search(r'create|update|trash|push|delete|copy|share', n) else reads
            tgt.append((ln, n, short(i, 300)))
        else:
            other.append((ln, n, short(i, 200)))

def sec(t, rows):
    print(f'### {t}\n')
    print('\n'.join(f'- стр. {r[0]}: ' + ' | '.join(str(x) for x in r[1:]) for r in rows) or '- нет')
    print()

print(f"## {p.split('/')[-1]}\n")
sec('Загруженные Skill', skills)
sec('Чтения', reads)
sec('Записи (вызовы, меняющие состояние)', writes)
sec('Прочие вызовы', other)
