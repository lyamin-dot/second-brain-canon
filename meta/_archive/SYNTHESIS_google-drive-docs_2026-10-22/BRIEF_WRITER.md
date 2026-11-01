meta/SYNTHESIS_google-drive-docs_2026-10-22/BRIEF_WRITER.md

# Brief for the cluster writer (steps C1, C3, C4, C4a of meta/PROTOCOL_knowledge-synthesis.md)

Work dir: /tmp/canon (clone of lyamin-dot/second-brain-canon). Report folder: meta/SYNTHESIS_google-drive-docs_2026-10-22/ (= $D). READ-ONLY everywhere except the files you are told to create in $D. No n8n, no Drive, no git commit/push.

Read first, in full: meta/PROTOCOL_knowledge-synthesis.md (the law: rule instead of story; four elements of a rule; what never goes into a Skill — case stories, object particulars, history blocks); the live Skill /mnt/skills/plugins/google-drive-docs/ (SKILL.md and all references/ — to keep its STYLE and to find every place your mechanism lives; also find copies with grep across /mnt/skills/plugins and /tmp/canon); $D/FINDINGS.md (new lessons with decisions already taken by Andrei — they are binding); your old cluster file $D/old_<X>.md (exact line ranges are in its === headers). The previous pass report meta/SYNTHESIS_google-drive-docs_2026-10-20.md explains basis lines of the form «отчёт синтеза, правило X.Y.Z» (they point to that report) — keep such references valid.

Task: rewrite your cluster ANEW as rules (law on top if one exists, particular rules below), merging the new findings. Every unit of the old text must survive (in text, or by an address that you verified exists). Each rule: what/when, why, symptom (if not obvious), basis (count of independent cases, date of last, address of each case). KEEP basis lines inline in the old style («Основание: …» on its own line) — a script will move all bases to references/basis.md afterwards; do NOT create basis.md. Do not touch line 85 of references/sheets.md (section 4.1). Do not write concrete object particulars (workflow trigger names, book names, IDs, execution numbers inside the rule body — execution numbers go only into the basis line). Write in Russian, in the Skill's own style, no abbreviations a reader would not know. Size is information, not a goal.

C4a: for each rule decide the trigger; if a rule's trigger is a concrete action that lives in another file of this Skill, you may move it there — then deliver an extra block «insert after anchor line <exact existing line>».

Deliverables in $D:
1. new_<X>_<n>.md — one file per replaced range: first line `REPLACES <file> lines <a>-<b>`, then the full new text of that range (must start/end at the same section boundaries so it can be spliced by line numbers).
2. insert_<X>_<n>.md (only if needed) — first line `INSERT AFTER <file> :: <exact anchor line text>`, then text.
3. writer_<X>_report.md — sections: «Как покрыты находки» (each finding → where, quoted); «Предлагаю снять» (unit + reason; nothing is removed by you — removal is Andrei's); «Расширено» (what the new text claims beyond old text + findings); «Противоречия» (both texts); «Копии в других Skills» (path:line, verdict: replace by pointer / keep / contradiction — you do not edit other Skills); «Триггеры и файлы».
Return a short summary (≤15 lines) with file names.
