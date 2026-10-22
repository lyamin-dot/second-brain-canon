# Acceptance brief — Skill apps-script-sheets, synthesis pass 2026-10-22

You did NOT do this work. Your job: try to REFUTE each claim below by checking the objects themselves. READ-ONLY everywhere; write only your output file. Do not run git push or any network write except reading Google documentation pages (WebFetch/WebSearch allowed).

Objects:
- OLD = live Skill: /mnt/skills/plugins/apps-script-sheets/ (equal to repo mirror skills/apps-script-sheets/ at commit 19103d2 in clone /tmp/second-brain-canon)
- NEW = /tmp/claude-0/-home-claude/c9c61862-c8c4-51a7-bc25-3486f29dd2a0/scratchpad/ass/new/
- BASIS = /tmp/claude-0/-home-claude/c9c61862-c8c4-51a7-bc25-3486f29dd2a0/scratchpad/ass/BASIS_TABLE.md (rule id → case addresses)
- Findings source: /tmp/second-brain-canon/meta/HARVEST_2026-10-22.md, section «### apps-script-sheets — 13»; queue rows AJ-40, AJ-45, AJ-37, AJ-32 in /tmp/second-brain-canon/registry/maintenance-queue.md
- Protocol: /tmp/second-brain-canon/meta/PROTOCOL_knowledge-synthesis.md (section «Чего в Skill не бывает»)

Claims to refute:
A1. Each of the 13 findings (J1#13, J3#1, J3#7, L2#14, L2#17б, L2#19, S1#17, S1#18, S1#19, S2#14, S3#2, M1c#8-5, M1c#8-22) is present in NEW as a rule, example or table row whose meaning matches the finding — or, where NEW is narrower than the finding, the narrowing is justified by the finding's own source file.
A2. The four addresses named in AJ-32 (SKILL.md, path labs/sys/t-knowledge-synthesis.md), AJ-45 (SKILL.md, ЭСТАФЕТА of labs/ozon-ue/t-goods-book-script.md) and AJ-37 (SKILL.md and references/signal.md, second-brain-engineer point 14) now point to places that exist (check the clone; for point 14 the repo mirror skills/second-brain-engineer/references/design-acceptance.md; for the deleted section use `git show 2f30998:labs/ozon-ue/t-goods-book-script.md`). No old wrong address remains anywhere in NEW.
A3. Every numbered heading of OLD (§0.1 … §9.9, table sections) exists in NEW in the same file with the same number; the only new numbers are §3.13 and §9.10. Every OLD sentence is still present verbatim in NEW except the four replaced addresses, the «Редакция» lines, the book-traps §3.7 heading, the routing-table rows and file-header «Читать:» lines that were extended (verify by diff).
A4. Text inserted into NEW contains no Google file IDs, workflow IDs, webhook paths, e-mail addresses, credential names, book code, names of specific books/shops, or case stories (who/when/what was thought) — case data only in «Основание» lines.
A5. Every address in BASIS exists in the clone and its content supports the row (read each cited line).
A6. Documentation claims in NEW are true per Google documentation: Sheets API ValueRenderOption FORMULA says nothing about locale; Apps Script scripts.run requires the calling app and the script to share a (standard) Google Cloud project, otherwise 403 PERMISSION_DENIED; Apps Script execution log is kept a short time (logging guide); ClockTriggerBuilder.nearMinute ±15 minutes and atHour runs within that hour.
A7. No rule inserted in NEW contradicts another rule already in NEW (check especially §4.9 vs references/signal.md §9.9, §9.10 vs §9.5, book-traps §3.7 new paragraph vs SKILL.md §2.1/§2.7/§4.8, design.md new paragraphs vs §5 law and §9.9).
A8. references/samples.md is byte-identical to OLD.

Output: /tmp/claude-0/-home-claude/c9c61862-c8c4-51a7-bc25-3486f29dd2a0/scratchpad/ass/ACCEPTANCE.md — for each claim: REFUTED / NOT REFUTED, with the exact evidence address (file:line or URL) for every finding. Reply with the per-claim verdict and each refutation in one line.
