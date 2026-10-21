# Writer brief — synthesis of Skill `apps-script-sheets` (2026-10-20)

ROOT = /tmp/claude-0/-home-claude/d288ad51-fd39-5e51-b696-16569dae7e4d/scratchpad/ass
CLONE = /root/second-brain-canon (git clone of lyamin-dot/second-brain-canon at commit aeb4b23). READ-ONLY: never run git pull/checkout/commit/push there, never write into it. `git log`, `grep`, `cat`, `git show` are fine.
OLD TEXT = ROOT/old/ (byte-identical copy of the live Skill = mirror skills/apps-script-sheets/ at aeb4b23).
NEW TEXT goes to ROOT/new/ (same layout: SKILL.md, references/*.md). Write ONLY your group's part (see GROUPS below). All other outputs go to ROOT/work/.

## What synthesis is (read first, it is the law you execute)
Read CLONE/meta/PROTOCOL_knowledge-synthesis.md in full (sections «Закон», «Что такое правило», «Чего в Skill не бывает», «Где живёт история», steps С1, С3, С4, С4а). Summary:
- Rewrite the text anew as RULES. Each rule has 4 elements: what to do / not do and when; why (mechanism in 1–2 sentences); sign/symptom if non-obvious; basis.
- BASIS line form (Andrei's decision 2026-10-20): in the Skill only «Основание: N случаев, последний <дата> — отчёт синтеза, правило <id>». The addresses of every case go into your BASIS file (table «rule id → cases»), which becomes part of the synthesis report `meta/SYNTHESIS_apps-script-sheets_2026-10-20.md`. A basis that is Andrei's decision/word: one line with date and place, no report reference. Rule ids: short stable ids like «ASS.2.1.локаль», «ASS.0.1», «ASS.3.9.ключ».
- NO case stories (who/when/execution number/bytes/what was thought first), NO edit-history lines in headers (header = one line «Редакция 2026-10-20.»), NO «ИСТОРИЯ ДИАГНОЗА» blocks — a refuted diagnosis stays only as one line «Не путать: X — на деле Y» when the false version is plausible and a session would return to it; its story goes to the BASIS file/journal.
- NO state or particulars of a concrete object (Andrei 2026-10-20: «Skill — инструкции для всех»): IDs of books/documents/workflows, sheet names of a concrete book, the separator of a concrete book, the control example of a concrete table, «book X has Y». Such a unit gets verdict ПО АДРЕСУ: find the fact in its carrier (registry/documents.md for IDs of books/docs; registry/n8n-map.md for workflows; the canon of the book's project under projects/<name>/ for its private facts; meta/CASES_*.md for cases). If the fact is present — drop it from the Skill. If absent — list it in your PARTICULARS file as «перенести: <carrier>, <exact text to add>» (the dispatcher writes carriers; you never write to CLONE). A property of the platform valid for every instance (Apps Script, Google Sheets engine, locale behaviour) is NOT a particular — keep it as a rule. Examples ARE allowed if they illustrate a general rule without depending on a concrete object (e.g. a formula pattern with placeholders).
- Copies of mechanisms whose home is another Skill (google-drive-docs, n8n-engineering-manual, second-brain-git, second-brain-engineer) — replace by a one-line pointer to the home (Skill name + section), unless the map verdict says ОСТАВИТЬ. See ROOT/in/inputs_map.md (section 2 rows with verdicts per copy; «ASS:<line> — ОСТАВИТЬ / ЗАМЕНИТЬ ССЫЛКОЙ»). Pointers to google-drive-docs use its section numbers §0–§12 (its synthesis preserves them).
- Nothing is removed from knowledge by you. A unit you think is obsolete goes to «предлагаю снять» list in your WRITER_REPORT with reason; it still counts as needing preservation until Andrei decides — so keep it in text (or by address) meanwhile.
- Preserve section/point numbers: 0, 0.1, 0.2, 1, 2, 2.1–2.7, 3, 3.1–3.12, 4, 4.1–4.9, 5, 6, 8, 9, 9.1–9.8. New points allowed only as NEW numbers appended (e.g. 9.9, 2.8) — never renumber. Other Skills and repo files reference these numbers (e.g. n8n-engineering-manual references R6.6/T4.10.4 point to this Skill; google-drive-docs references/sheets.md points to book-traps.md and §2.1).
- Keep the Skill's own STYLE (map signature): «## 0. ДВА ПРАВИЛА БЕЗ ИСКЛЮЧЕНИЙ», numbered work order, trap paragraphs with JavaScript code to paste, the read-confirmation lock «⚠️ ПОДТВЕРЖДЕНИЕ ПОСЛЕ ПРОЧТЕНИЯ: номер параграфа + дословная цитата правила», error tables «Симптом | Причина | Где». Do not convert it to another Skill's style. Russian language, no abbreviations unexplained (Andrei's preference: write as for a reader who knows nothing).
- Size is information, not a goal. Do not shorten at the cost of losing knowledge.
- Trigger/file (step С4а): this Skill is routed by the table «Что читать дальше» in SKILL.md; each rule lives in the file of the table row whose action triggers it; rules triggered by «any Apps Script rework» stay in SKILL.md. Do not move whole sections between files unless the trigger demands; if you propose a change of the table rows, say so explicitly in WRITER_REPORT (a changed row set triggers a retest).
- Code of books never goes into the repo (second-brain-git И-7 class 4): samples are only techniques/fragments not bound to a book. Also no secrets, webhook paths, credential names, e-mail addresses, personal data (И-7 classes 1–2).

## Inputs (read what concerns your group)
- ROOT/in/inputs_map.md — map excerpts: zone, style, section-2 rows (copies + verdicts), clusters 5.5 (homes), history lines.
- ROOT/in/verdicts_section4.md — harvest verdicts for this Skill (AJ-5 edits #1–#13, AJ-16, AJ-14 Х-8, Х-9).
- CLONE/meta/HARVEST_2026-10-18_edits/apps-script-sheets.md (+ .json) — texts of AJ-5 edits («было → стало»). Edits #1, #7, #10, #12 (header history) — NOT applied. Edit #13 — not in Skill (state of a workflow). Others: merge into their cluster by synthesis (not by appending).
- ROOT/in/queue_rows.md — queue rows AH-22 (already in live Skill as 3.9 — synthesize), AI-26 (clasp — check its status cell; superseded by AJ-16/gas-bridge), AJ-5, AJ-16.
- AJ-16 (gas-bridge): CLONE/projects/gas-bridge/PLAN.md (section «Контракт вызова»), STATE.md, LOG.md records Р-2 and Р-4. Rule to write: for a book listed in table `gas_allowlist` the session reads and edits the script code itself through the bridge workflow (ID taken from the row of CLONE/registry/n8n-map.md by workflow name — never written into the Skill); for other books — the old order (Andrei sends the live text, edits are given as full file text). Emergency path clasp: when n8n is unavailable, only Andrei edits code via clasp (journal Р-4). Stage B of the bridge (running functions) is NOT decided — the Skill must not promise the session it can run functions. The sign «book is in gas_allowlist» must be something read in this session.
- Contradiction resolved by rule (harvest question 1, Price Master separator «,» vs «;»): in the Skill — «the separator of each book is determined by a probe»; the value for a concrete book lives with that book's carrier; a contradiction in the canon goes as a capture to the book's project (list it in PARTICULARS as «захват: <project>, <text>»).
- AJ-14 Х-8 (Google Sheets book limit 10 million cells; the grid of all sheets counts, empty rows too; measure via gsheets-read mode meta) — case: CLONE/projects/wb-ue/LOG.md line ~400. AJ-14 Х-9 (all files of an Apps Script project share one scope: of same-named functions setupAll/onOpen/withRetry_ the one loaded last works) — case: CLONE/projects/sku-cost/PLAN.md lines 132–136. Check these addresses exist.
- Other Skills (for pointers only): /mnt/skills/plugins/<name>/.
- Verify every basis address you write exists in CLONE (grep the record header «^Р-NN |» in the named journal, queue position row, TRIAGE lesson, file+line). Docs (Google Docs) cannot be read from CLONE: mark «не проверено, Docs» and prefer a repo address if one exists.

## GROUPS (each writer writes only its own part)
- A — ROOT/old/SKILL.md lines 1–245: frontmatter + header, table «Что читать дальше», sections 0, 1, 2 (2.1–2.7; new 2.8 allowed for Х-9 if that is its home — cluster 3). Output: ROOT/new/parts/SKILL_A.md (from line 1 up to, NOT including, the line «## 4. ОБЯЗАТЕЛЬНЫЕ ЧАСТИ ЛЮБОГО ТАКОГО СКРИПТА»). The description (frontmatter) must stay ≤1024 characters (Customize limit). AJ-16 lives here (cluster 1). AJ-5 #2 (route row to §9.1–9.9 and freshness) and #3 (locale per book, separator by probe) live here.
- B — ROOT/old/SKILL.md lines 246–386: sections 4 (4.1–4.9) and 6 (error table). Output: ROOT/new/parts/SKILL_B.md starting exactly with the line «## 4. ОБЯЗАТЕЛЬНЫЕ ЧАСТИ ЛЮБОГО ТАКОГО СКРИПТА». AJ-5 #4, #5 live here.
- C — ROOT/old/references/book-traps.md (section 3, 3.1–3.12, control example, error table §3). Output: ROOT/new/references/book-traps.md. AH-22 (3.9), AJ-14 Х-8 (cluster 8, 3.7) live here.
- D — ROOT/old/references/signal.md, design.md, samples.md (sections 9, 5, 8). Outputs: ROOT/new/references/{signal,design,samples}.md. AJ-5 #6, #8 (new 9.9 «Свежесть»), #9, #11 live here. samples.md: IDs of documents/books/workflows → ПО АДРЕСУ (cluster 10).

## Homes of clusters spread across groups (the home group writes the full rule; others put a one-line pointer)
1 live script text, the book doesn't belong to the script, FORMULA before write, edits as full text — A (section 1, with AJ-16); copy in 3.8 — C pointer.
2 formatting & input rules via dump — A.
3 locale, first function, setValue with «=», confirmation lock — A (2.1, 2.2, 2.5); Х-9 — A.
4 references map 0.1 and 4.6 — B owns 4.6; 0.1 rule text stays in A (section 0) with pointer to 4.6 for the functions.
5 key, header, headers, IFERROR and FILTER — C (3.9–3.12).
6 schedule 4.9 — B; time zone 2.7 — A.
7 owner's columns 4.2 — B.
8 heavy book & backup — C for 3.7 (+Х-8), B for 4.3 with pointer.
9 check 4.5, liveness sign, thresholds 9.5, freshness 9.9 — D for section 9, B for 4.5 with pointer.
10 IDs of documents in samples — D, ПО АДРЕСУ.
11 history — each group in its own files.
Mechanism homed outside this Skill — by column «дом» of map section 2; in text a pointer.

## Your outputs (ROOT/work/, file names with your group letter G)
1. The new text file(s) listed above.
2. BASIS_G.md — table «rule id | N | date of last | address of each case (verified) | short». Plus a section «Случаи без адреса»: cases from the old text with no address outside the Skill — write them out fully here (this report becomes their address).
3. PARTICULARS_G.md — table «unit (quote ≤80) | carrier | present in carrier? (what you grepped) | action: снято / перенести: <text> / захват: <project>: <text>».
4. WRITER_REPORT_G.md — what clusters you synthesized and the law found for each; copies replaced by pointers; harvest edits applied (by number) and not applied with reason; «предлагаю снять» (unit, reason); «расширено» (where the new text claims more than the old); «противоречия» (both texts, for Andrei); pointers you rely on in other groups/Skills; any proposed change of the «Что читать дальше» rows; open doubts.
Do not write anything outside ROOT/new and ROOT/work. Report back a 10-line summary with file paths.
