# Checker brief — synthesis of Skill `naryad` (2026-10-21), TASK 1: decomposition (step С2)

READ-ONLY job. Write only your own output file under ROOT/work/.
ROOT = /tmp/claude-0/-home-claude/f4320b56-b253-5144-a6e1-60bcd32f6fe2/scratchpad/naryad
CLONE = /home/claude/clone_ro (git clone at c0b3ce3; read-only).
OLD TEXT = ROOT/old/ (the live Skill; ROOT/old/SKILL.md has line structure restored by script, otherwise identical to ROOT/old_raw/SKILL.md).
The new text does NOT exist yet and you must not look at ROOT/new/. Later you get task 2 (verify the new text against your table) as a continuation.

Method: CLONE/meta/PROTOCOL_knowledge-synthesis.md, step С2 (read it). Decompose your group's old text into atomic units:
`U<n> | CLASS | file:line | verbatim quote ≤80 chars | paraphrase (one line) | FLAGS`
CLASS ∈ ПРАВИЛО, ИСКЛЮЧЕНИЕ, ПОРОГ (number, format, field name, tool name, ID pattern), ПРИЧИНА, СЛУЧАЙ (date, order ID as precedent, count of cases, story), АДРЕС (reference to a place of knowledge), ПРОВЕРКА.
FLAGS: ИСТ — history/case story/edit-history line; ОСОБ — particular of a concrete object; КОПИЯ — copy of a mechanism homed in another Skill (ROOT/in/inputs_map.md, section 2).
Every sentence, table row, list item, template field is covered by ≥1 unit. Do not merge two rules into one unit. Quote must be findable by `grep -F` on that line.
Then «## NEW»: new knowledge for your group from ROOT/in/WRITER_BRIEF.md section «Decisions already taken» and ROOT/in/queue_rows.md: A — AI-5, AI-16 (narrow), AJ-18 (already in text: just mark), ГДЕ-premise note; B — contradiction 8 (counter → pointer); C — none unless found. Same format, file:line into the source file.
Output ROOT/work/units_<G>_<model>.md: header (group, files+line ranges, total, count by class, by flag), «## OLD», «## NEW». Report back path + counts (≤10 lines).
GROUPS: A — ROOT/old/SKILL.md; B — ROOT/old/references/issuer.md, foreman.md; C — ROOT/old/references/destructive-orders.md, executor.md, revision.md.
