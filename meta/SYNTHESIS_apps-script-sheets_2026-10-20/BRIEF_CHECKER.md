# Checker brief — synthesis of Skill `apps-script-sheets` (2026-10-20), TASK 1: decomposition (step С2)

READ-ONLY job. Do not modify anything except your own output file under ROOT/work/.
ROOT = /tmp/claude-0/-home-claude/d288ad51-fd39-5e51-b696-16569dae7e4d/scratchpad/ass
CLONE = /root/second-brain-canon (git clone at commit aeb4b23; read-only: never pull/checkout/commit/write).
OLD TEXT = ROOT/old/ (byte-identical to the live Skill).
The new text does NOT exist yet and you must not look for it (ROOT/new/ is off-limits for this task). Later you will get task 2 (verify the new text against your table) as a continuation.

Method: CLONE/meta/PROTOCOL_knowledge-synthesis.md, step С2 (read it). Decompose your group's old text into atomic units. Each unit = one atomic statement:
`U<n> | CLASS | file:line | verbatim quote ≤80 chars | paraphrase (one line) | FLAGS`
CLASS ∈ ПРАВИЛО (what to do and when), ИСКЛЮЧЕНИЕ, ПОРОГ (number, format, tool/field/function/API name, a constant or call that a code block enforces), ПРИЧИНА, СЛУЧАЙ (date, execution number, count of cases, «прецедент», a story of what happened), АДРЕС (reference to a place of knowledge: file, record, Skill section), ПРОВЕРКА (how to verify).
FLAGS (zero or more): ИСТ — history/case story or edit-history line; ОСОБ — a particular of a concrete object (ID of a book/document/workflow, sheet names of a concrete book, «book X has Y», state of a concrete workflow); КОПИЯ — a copy of a mechanism whose home is another Skill (see ROOT/in/inputs_map.md, section 2).
Rules: every sentence, every table row, every list item, every code-block element that encodes behaviour is covered by ≥1 unit. Code blocks: one unit per behaviour-bearing element (e.g. «var SEP = ','», «SpreadsheetApp.flush()», a try/catch that logs and continues), not per line of syntax. Do not merge two rules into one unit. Quote must be findable by `grep -F` on that line (copy exactly, may cut at 80 chars).
Then section «## NEW»: units of NEW knowledge assigned to your group (from ROOT/in/verdicts_section4.md and CLONE/meta/HARVEST_2026-10-18_edits/apps-script-sheets.md, plus for group A the AJ-16 rule summarized in ROOT/in/WRITER_BRIEF.md and in ROOT/in/queue_rows.md, plus AJ-14 Х-8 for group C and Х-9 for group A), same format, file:line pointing into their source file in CLONE (or ROOT/in/...). Exclude harvest edits #1, #7, #10, #12 (history, not applied) and #13 (not in Skill) — list them in one line «excluded: …».
Group assignment of NEW: A — AJ-5 #2, #3, AJ-16, Х-9; B — AJ-5 #4, #5; C — AH-22 (if not fully already in old 3.9 — still list its statements), Х-8; D — AJ-5 #6, #8, #9, #11.

Output: ROOT/work/units_<G>_<model>.md with header lines: group, files+line ranges covered, total units, count by class, count by flag. Then «## OLD» and «## NEW». Report back: path + counts (≤10 lines).

GROUPS:
- A — ROOT/old/SKILL.md lines 1–245 (frontmatter, header, «Что читать дальше», sections 0, 1, 2.1–2.7).
- B — ROOT/old/SKILL.md lines 246–386 (sections 4.1–4.9, 6).
- C — ROOT/old/references/book-traps.md (all lines).
- D — ROOT/old/references/signal.md, design.md, samples.md (all lines).
