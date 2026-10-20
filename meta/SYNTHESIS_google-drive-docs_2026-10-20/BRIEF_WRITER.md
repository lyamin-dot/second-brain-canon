# Writer brief — synthesis of Skill `google-drive-docs`, 2026-10-20

You are the WRITER (roles С1, С3, С4, С4а, С6) of one group. Write Russian, in the style of this Skill.

## Paths
- ROOT = /tmp/claude-0/-home-claude/a29bdaac-a31a-5d18-b63d-19cf38409194/scratchpad/gdd
- CLONE = /tmp/claude-0/-home-claude/a29bdaac-a31a-5d18-b63d-19cf38409194/scratchpad/repo (git clone of lyamin-dot/second-brain-canon, main). READ-ONLY: never commit, push, checkout, or modify anything in CLONE.
- Old text of the whole Skill: ROOT/old/ (SKILL.md + references/). Identical to live Skill and to CLONE/skills/google-drive-docs/.
- Inputs: ROOT/inputs/map_gdd.md (catalogue map rows; section 5.4 = clusters of this Skill; section-2 rows = mechanisms with home and copies), ROOT/inputs/contradictions.md (resolved contradictions — apply the "Правильно"/verdict text), ROOT/inputs/queue.md (open edits AJ-9, AJ-14/X-30, AJ-23 to include).
- Write ONLY into ROOT/out/<G>/ (G = your group letter). Do not touch other groups' folders.
- Do not call any n8n write tool, Drive write tool, git write, memory write.

## Read first, fully, yourself
1. CLONE/meta/PROTOCOL_knowledge-synthesis.md — the law. Especially «Закон», «Что такое правило», «Чего в Skill не бывает» (incl. object particulars), steps С1–С7.
2. Your group's old files in ROOT/old/ fully, plus ROOT/old/SKILL.md (all groups: it holds the routing table «Что читать дальше» and the hard rules).
3. Form examples of already-synthesized Skills (read a part, to copy the FORM of basis lines, not the style): CLONE/skills/n8n-engineering-manual/SKILL.md, CLONE/meta/SYNTHESIS_n8n-engineering-manual_2026-10-20/BASIS_A.md, PARTICULARS_A.md, WRITER_REPORT_A.md.

## Groups (files)
- A: SKILL.md
- B: references/docs-read.md, references/docs-write.md
- C: references/sheets.md, references/infra.md
- D: references/mcp.md, references/failures.md

## What to produce in ROOT/out/<G>/
1. new/<same relative names> — the new text of your files (e.g. out/B/new/references/docs-read.md).
2. BASIS_<G>.md — table: rule id | N independent cases | date of last | case address(es) | what (short). Rule ids: `<G>.<section>.<n>` e.g. `A.7.2`. Each address names the case itself (journal record `Р-NN журнала <path>`, queue position, task file, harvest finding `meta/HARVEST_<date>.md` item) and is verified to exist by grep in CLONE (say what you searched). Cases with no address outside the Skill: section «Случаи без адреса» with the full case text from the old Skill (the report will be their address).
3. PARTICULARS_<G>.md — object particulars removed from Skill: unit quote ≤80 | carrier | does carrier already hold it (what you grepped). If carrier lacks it: give exact text to append (repository file path) — the dispatcher appends; do not write CLONE.
4. WRITER_REPORT_<G>.md — sections: «Копии» (было → стало for OTHER Skills' copies you found, with file:line in CLONE/skills/<name>/), «Предлагаю снять» (units you dropped as obsolete/refuted, with reason — Andrei decides), «Расширено» (where new text says more than old), «Противоречия» (unit vs unit, both texts — do not resolve yourself), «Строки таблицы Что читать дальше» (rows group A must add/change for your files), «Нерешённые дома».

## Rules for the new text
- Every rule has 4 elements: what/when; why (mechanism, 1–2 sentences); sign/symptom if non-obvious; basis line. Basis line form exactly: «Основание: N случаев, последний <дата> — отчёт синтеза, правило <id>.» (singular forms: «1 случай»). A decision of Andrei as basis: one line with date and place of record, no report. Several bases of one section may be gathered as a list at section end.
- No case stories (who/when/execution numbers/bytes/what we thought first), no «ИСТОРИЯ ДИАГНОЗА» blocks, no revision history in headers. A refuted belief the session would plausibly return to stays as one line «Не путать: X — на деле Y.» Case text goes to BASIS.
- SKILL.md header (group A only): one line «Редакция 2026-10-20.» Keep YAML frontmatter; description may change only if the Skill's scope changes (it should not).
- Keep section numbers §0–§12 and their sub-numbers, the error codes E01–E21, the silent-failures register format, antipatterns starting with «НЕ». Other Skills and repo files reference these numbers. If a section disappears entirely, keep its number with a one-line pointer.
- Write anew per cluster (С4): first ask what single statement makes the cluster's rules its special cases; put it on top with its reason, then short specifics.
- С4а: each rule gets a trigger; trigger decides file: «any Google operation» → SKILL.md; a specific action (write to Doc, read Sheets, Drive via MCP, failure lookup) → its references file and a row in the routing table of SKILL.md. Report needed rows.
- Object particulars (protocol, «Чего в Skill не бывает»): IDs of workflows, documents, books, folders; credential names; facts about a specific book/sheet/workflow/server — leave the Skill. Platform properties true for any instance (Google Docs API, Sheets, Drive, n8n engine, MCP connector) stay.
- Workflow IDs (Andrei's decision, variant В): the Skill names the tool by its workflow NAME and says: ID is taken from the line of `registry/n8n-map.md` with that name (Git Read Lines with pattern = name, or grep with clone); if the name is masked «***» in the map — from `registry/tools.md`. Names (from the map): gdocs-read = «Claude → Google Docs Read (full)»; gdocs-append = «Claude → Google Docs Append v2 (verified)»; gdocs-replace = «Claude → Google Docs Replace v2 (verified)»; gdocs-overwrite = «Claude → Google Docs Overwrite v2 (verified)»; gdocs-apply-from-file = masked → registry/tools.md line GDOCS_APPLY_FROM_FILE; Create Folder = «Claude → Create Folder»; gsheets-read = «Claude → Google Sheets Read»; gsheets-append = «Claude → Google Sheets Append»; old v1 Append/Overwrite/Replace are archived; SYS Canary = masked. The general rule text lives in SKILL.md (group A, permanent layer next to the tool chooser table); other groups write the tool name and a short pointer «ID — по правилу §1».
- Copies of mechanisms whose HOME is another Skill (map section-2 rows; homes in n8n-engineering-manual, second-brain-git, apps-script-sheets, second-brain-engineer) → one line pointer to the home (Skill, file, section/number), keeping only what is specific to Google tools here. BEFORE pointing, grep the home in CLONE/skills/<name>/ (n8n-engineering-manual there is the NEW synthesized text with numbers preserved) and confirm it holds the content; if the home lacks a part, keep that part here and say so in «Нерешённые дома». A pointer counts as preservation only if the home holds the unit.
- Cluster homes across groups (the home group writes the full rule; others write a pointer line): 1 verification by independent re-read §7 — A; 2 call form of execute_workflow — home n8n-engineering-manual §1.1 (here only request bodies of gdocs tools + pointer); 3 contextData / reading cost — home n8n-engineering-manual R4 (AJ-9 antipattern: pointer); 4 n8n lines of the silent-failures register — home n8n-engineering-manual, D keeps pointers; 5 Sheets incl. X-30 — C; 6 service-account rights, who creates files, write-scope fallback — C; 7 empty read, completeness of traversal, absence — D; 8 \uXXXX — home second-brain-git 8.2, B pointer; 9 1–2 KB boundary, anchor, Guard K1, apply-from-file — B (A pointer); 10 LAST_UPDATED — A; 11 read_file_content, PDF — A; 12 updating this Skill — home second-brain-git 2.6 and second-brain-engineer Р13, A pointer; 13 checksum and channel — D (B pointer); 14 history — each group own files; ID rule — A.
- Apply resolved contradictions from inputs/contradictions.md (items 1, 4, 7, 11, 3а-5 and Andrei's 2026-10-20 decisions: unneeded workflow → unpublish, not archive; credentials bound by the session itself via setNodeCredential, not one update_workflow migration). Include queue inputs (AJ-9 pointer; X-30 rule in C; AJ-23 address `projects/n8n/INCIDENT_LOG.md` in D).
- Security class (repository is public): no webhook paths, credential names/numbers, e-mails, tokens, personal folder names in new text or reports.
- Do not judge importance: nothing is dropped silently. Size is not a goal.
- Self-check before finishing: every sentence of your old files is either in new text, in BASIS (case), in PARTICULARS (carrier) or in «Предлагаю снять».

Finish with a short reply: files written, sizes old → new, counts of «Предлагаю снять», «Расширено», «Противоречия», unresolved homes.
