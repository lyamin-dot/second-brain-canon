meta/SYNTHESIS_google-drive-docs_2026-10-22/BRIEF_CHECKER.md

# Brief for the preservation checker (steps C2 and later C5 of meta/PROTOCOL_knowledge-synthesis.md)

Work dir /tmp/canon, folder $D = meta/SYNTHESIS_google-drive-docs_2026-10-22/. READ-ONLY except files you create in $D. No n8n, no Drive, no git.

Task 1 (now, BEFORE any new text exists — do not open new_*.md or writer_*.md files even if they appear): decompose the old cluster texts $D/old_A.md, $D/old_B.md, $D/old_C.md into atomic units. One unit = one atomic statement with a class and a verbatim quote ≤80 characters: ПРАВИЛО, ИСКЛЮЧЕНИЕ, ПОРОГ (number, format, tool/field name), ПРИЧИНА, СЛУЧАЙ (date, execution number, case count, address as proof), АДРЕС (link to where knowledge lives), ПРОВЕРКА. Every sentence (and every table row) must be covered by at least one unit. Save as TSV $D/units_A.tsv, units_B.tsv, units_C.tsv with columns: id (A-001…), source (file:line), class, quote. Also add the new-finding units from $D/FINDINGS.md to the same tables (ids A-N01…, class by the same scheme, quote from FINDINGS) — they must appear in the new text too.

Return ≤10 lines: unit counts per cluster.

Task 2 will come later as a follow-up message (verdicts against the new text).
