# Checker brief — synthesis of Skill apps-script-sheets, pass 2026-10-22

You are the independent checker of a knowledge-synthesis pass. You will NOT write the new text. READ-ONLY on everything except the output files named below.

Protocol (read steps С2 and С5 and the section "Чего в Skill не бывает"): /tmp/second-brain-canon/meta/PROTOCOL_knowledge-synthesis.md

## Task 1 (now): decompose the OLD text into units

Input: /tmp/claude-0/-home-claude/c9c61862-c8c4-51a7-bc25-3486f29dd2a0/scratchpad/ass/OLD_CLUSTERS.md — the old text of the clusters touched by this pass, with original file name and line numbers (tab-separated prefix). The full live Skill is at /mnt/skills/plugins/apps-script-sheets/ if you need context, but decompose ONLY OLD_CLUSTERS.md.

Unit = one atomic statement. Classes: RULE (what to do and when), EXCEPTION, THRESHOLD (number, format, tool/field name), REASON, CASE (date, execution number, count of cases, address as proof), ADDRESS (pointer to where knowledge lives), CHECK (how to verify). Every sentence of the old text must be covered by at least one unit. Table rows (symptom tables) — one unit per row at least, more if the row carries several statements.

Output: /tmp/claude-0/-home-claude/c9c61862-c8c4-51a7-bc25-3486f29dd2a0/scratchpad/ass/units.tsv with columns:
id<TAB>file:line<TAB>class<TAB>verbatim quote (≤80 chars, copied exactly)<TAB>one-line paraphrase in Russian
ids: U001, U002, … in text order.

When done, reply with: number of units by class, and any sentence you found hard to split (list). Nothing else. Then wait: Task 2 (verifying the new text) will come as a follow-up message.
