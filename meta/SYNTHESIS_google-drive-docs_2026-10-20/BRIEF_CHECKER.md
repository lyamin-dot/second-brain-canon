# Checker brief — synthesis of Skill `google-drive-docs`, 2026-10-20

You are the independent CHECKER (roles С2 and С5) of one group. You do not write the new Skill text. READ-ONLY everywhere except your output folder.

## Paths
- ROOT = /tmp/claude-0/-home-claude/a29bdaac-a31a-5d18-b63d-19cf38409194/scratchpad/gdd
- CLONE = /tmp/claude-0/-home-claude/a29bdaac-a31a-5d18-b63d-19cf38409194/scratchpad/repo (read-only git clone; never commit/push/modify).
- Old text: ROOT/old/. Inputs: ROOT/inputs/queue.md, ROOT/inputs/contradictions.md.
- Groups: A = SKILL.md; B = references/docs-read.md + references/docs-write.md; C = references/sheets.md + references/infra.md; D = references/mcp.md + references/failures.md.
- Write ONLY into ROOT/out/<G>/. Do NOT open ROOT/out/<G>/new/ during task 1.

## Task 1 (С2) — decompose the old text BEFORE seeing the new text
Read CLONE/meta/PROTOCOL_knowledge-synthesis.md, step С2 and С5 (and «Чего в Skill не бывает»). Read your group's old files fully.
Write ROOT/out/<G>/units_<G>.md: one line per atomic statement:
`U<n> | CLASS | file:line | verbatim quote ≤80 chars | paraphrase`
CLASS ∈ ПРАВИЛО, ИСКЛЮЧЕНИЕ, ПОРОГ (number, format, tool/field name, ID), ПРИЧИНА, СЛУЧАЙ (date, execution number, count of cases, address as evidence), АДРЕС (link to a place of knowledge), ПРОВЕРКА. Every sentence of the old files is covered by at least one unit; tables row by row. Quotes must be exact substrings of the line (check with a script).
Then section «NEW» with units from inputs that belong to your group (AJ-9 antipattern → A/D; X-30 → C; AJ-23 → D; contradictions items 1, 4, 7, 11, 3а-5 → whichever file holds the disputed text), prefixed N<n>.
Reply briefly: number of units by class. Then wait — you will get task 2 as a continuation.

## Task 2 (С5) — verify the new text (sent later)
You will receive the location of the new text. For every unit give one verdict:
- В ТЕКСТЕ — with an exact quote ≤80 from the new text (any group's new file, if the home is there; say which);
- ПО АДРЕСУ — the address is named in the new text and you verified it exists (BASIS file of the group, a pointer to another Skill's home section in CLONE/skills/<name>/ that you grepped and that really holds the unit, a registry file holding the particular);
- ОСЛАБЛЕНО — meaning changed: condition narrowed/widened, must → should, number changed;
- ПОТЕРЯНО.
Admission: ПРАВИЛО, ИСКЛЮЧЕНИЕ, ПОРОГ, ПРОВЕРКА only В ТЕКСТЕ — except an object particular (workflow/document ID, a specific book/sheet/workflow fact) which is admitted ПО АДРЕСУ when its carrier holds it (check the carrier: registry/n8n-map.md by workflow name, registry/tools.md, registry/documents.md, project canon), and except a copy whose home is another Skill (ПО АДРЕСУ if the home text holds it). ПРИЧИНА — in text, generalized form allowed. СЛУЧАЙ and АДРЕС — in text or ПО АДРЕСУ (BASIS table counts as address).
Also: (a) knowledge in the old text missing from your unit table; (b) list «Расширено» — what the new text claims beyond the old; (c) any case story, ИСТОРИЯ ДИАГНОЗА block, revision history, object particular or security-class item (webhook path, credential name, e-mail) left in the new text.
Write ROOT/out/<G>/verdicts_<G>.md: `id | class | verdict | quote or address | note`, then sections (a), (b), (c), and a count line. Use a script to confirm quotes are exact substrings.
