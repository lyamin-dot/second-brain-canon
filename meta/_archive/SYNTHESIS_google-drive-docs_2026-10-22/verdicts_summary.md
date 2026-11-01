# Verdicts summary (step C5, preservation check)

## Counts per verdict
| Cluster | units | В ТЕКСТЕ | ПО АДРЕСУ | ОСЛАБЛЕНО | ПОТЕРЯНО |
|---|---|---|---|---|---|
| A | 127 (124 + 3 added in check a) | 126 | 0 | 1 | 0 |
| B | 171 (169 + 2 added) | 170 | 0 | 0 | 1 |
| C | 114 (112 + 2 added) | 114 | 0 | 0 | 0 |
Old-text units (A 95, B 150, C 98) all В ТЕКСТЕ: 363 of 405 quotes are verbatim substrings of the new texts, the rest are in new words with a quote of the new text in the verdict table. Diff of old vs new by sentence shows the old text changed only where intended (executionMode paragraph, triggerNodeName paragraph, E02 row, danger-list sentence, C law line); everything else is byte-identical.

## ОСЛАБЛЕНО / ПОТЕРЯНО
- A-N24 ОСЛАБЛЕНО (meaning changed, protection not weakened). FINDINGS/AJ-34: "a retry after the pause does not repeat a write unless the workflow itself answered with a refusal; check the document first". New §3 and E24: retry without reading is allowed only when there was NO answer at all (no execution number, no refusal); after ANY workflow answer, including a refusal, read the document first. This is stricter than the source on refusals. Dispatcher decides whether it matches intent.
- B-N13 ПОТЕРЯНО (by design). FINDINGS: the contradiction between the new array-literal precaution (sheets.md 4.3) and sheets.md:85 / apps-script-sheets SKILL.md:88 must stay open and be listed in the writer report. New text records no pointer to it; the new rule only says "не проверено, проба - задача ...". I did not read the writer report. If the report lists it, nothing is lost; the two rules still stand side by side in the Skill without a cross-note until the probe.

## Address checks that need attention
- `meta/SYNTHESIS_google-drive-docs_2026-10-22.md` (cited in new_A_1 for executions 84315-84317, section "Случаи без адреса") does NOT exist yet in /tmp/canon.
- FINDINGS says Р-29 "допущение" is line 172; it is line 171 of projects/deklaration-v2/LOG.md (content matches the claim).
- Source conflict for array literal: journal projects/deklaration-wb/LOG.md line 88 says run 77603 failed; meta/PRODUCT_DATA_HIERARCHY.md:42 says "проверено 2026-10-09"; new text says "не проверен пробой" per Andrei's decision.
- SERVER_INDEX line 875 is a Drive document, not checked; it is quoted in the Х-20 row of LESSONS_WAITING_CANDIDATES.md.
- Tool name: FINDINGS says get_workflow_execution, new text and the Skill use get_execution.
- All other cited addresses exist: registry/tools.md, maintenance-queue.md AJ-14 and AJ-34, labs/sys/t-harvest-close-leftovers.md (item 2), t-array-separator-probe.md, t-n8n-backup-stopped.md (line 39), L1/L2/M1b/M1c reports, G10.md (Q4), LESSONS_waiting.md Х-21, archive-recon LOG Р-24 line 191 (point 4 about «.pdf»), ozon-ue files (lines 63, 67; "Уроки" point 3 with 400), wb-ue LOG Р-67, meta/prompts/sys.md (10-second wait), n8n-engineering-manual §1.1.0/1.1.2/1.1.3, R2.3, R4.5, R6.8, R6.12, R6.14, engine.md 4.9, apps-script-sheets book-traps 3.7 and 3.10, design.md paragraph.

## (a) Knowledge in the old texts missing from my tables
Seven small items were missing and are now added as X-rows (all В ТЕКСТЕ, quotes verified in both old and new): A-X01 (purpose clause of the section 3 law), A-X02 (E12 condition: new node or credential type change), A-X03 (E22 "n8n или rclone, около недели"), B-X01 (R6 parenthetical: column names, row positions, types, shared quota), B-X02 (what C.4.3.1 covers), C-X01 (PDF inventory: name, size, metadata suffice), C-X02 (backup rules valid for any Google Drive backup). Nothing else found missing.

## (b) New text claims BEYOND old text + FINDINGS ("расширено")
A:
1. "не переносят с другого воркфлоу" and E23 "чаще всего 01_Webhook Канала git" (inference from one case).
2. get_execution must carry workflowId (n8n-engineering-manual 1.1.3 - checked) and nodeNames narrowed to the response node; wait ~10 s on running and do not start a new execute_workflow, "for a write tool that is a second write" (sys.md start block - checked; the rationale is the writer's).
3. includeData:false when only the status is needed (docs-write.md line 114 - checked); control numbers byteLength/checkSum cannot be taken via a subagent (failures.md section 9 line 55 - checked).
4. "три одновременных вызова не измерены и считаются за риск"; "пауза около 20 секунд снимает отказ" (interpretation); stricter retry rule (A-N24).
5. E26: "затем размер файла на Drive сверяется с исходным" (from Q4 "размеры сверены"); "повторять и подбирать параметры не нужно".
6. E27: "без них - не установлено"; examples "журнал, отчёт воркфлоу".
7. E-table intro adds E24 to the "не повторять, а перечитать" list; insert_A_1 adds the trigger pointer (E23) into docs-write.md.
B:
1. New 4.0 law paragraph (each read path returns its own part and does not report incompleteness; completeness is proven by the fields truncated/rowCount/reason; special case of 2.2) - synthesis of existing rules.
2. 4.2 intro: reading rules also apply to Sheets API requests from an HTTP node.
3. Heavy-book rule: "если лист собран из другой книги (IMPORTRANGE или скриптом), читать книгу-источник"; cause "узел упирается в таймаут Google, а не в объём данных"; "тот же корень, что ложная ошибка 4.0"; check zero rows against mode:"meta".
4. Named ranges: examples of cells (сводка, метка прогона, дата данных); "или имя переименовано"; parse by range field not position (R6.14, exists); rationale about A1 shift (supported by t-money-telegram).
5. 4.3: scope enumerated (Google Sheets node, gsheets-append, values.update/append), fallback "если формулу пишет воркфлоу - строить без литерала массива" (not in Andrei's decision wording), "различает ли Google путь записи - не установлено".
C:
1. 2.3 selection rule: also "take by fileId, not by name" (Х-21 generalised) and "scripts: type field in the inventory"; calls it a special case of completeness.
2. infra.md 5: a new section law ("a backup proves only the property that was checked: exists / fresh / readable / survives account loss / continues to be made; none follows from another" with causes) - synthesis beyond old text.
3. Backup bullet: "для дампа базы - проверка конца файла и пробное восстановление"; "прерванная выгрузка ложится тем же файлом с той же свежей датой" (causal claim); "в разы больше или меньше" (source only: threefold growth); example verdicts "бэкап испорчен / база выросла".

## Round 2 (step C6)
Compared round1 vs round2 (round2.diff, 91 lines; changed: E27 row and its basis line, E-table basis address, backup reason line, pagination address, 4.0 law, 4.2 intro, heavy-book reason, array-literal note, SERVER_INDEX case address). Re-ran all round-1 В ТЕКСТЕ quotes against the round-2 spliced Skill.
1. B-N13: now В ТЕКСТЕ. 4.3 says "До пробы это наблюдение стоит в противоречии с §4.1 (разделитель колонок `\` в `ru_RU`...) и с Skill apps-script-sheets, §2.1; решает проба, не сессия." Targets exist (sheets.md 4.1 at line 76; apps-script-sheets 2.1). Contradiction is open and marked, not resolved. (It names apps-script-sheets §2.1, not SKILL.md:88; same file, acceptable.)
2. A-N24: confirmed unchanged, stays ОСЛАБЛЕНО (stricter than AJ-34, decision with the dispatcher).
3. Units affected by corrections:
 - A-N05 (СЛУЧАЙ/ПРИЧИНА: "observed once unchanged") ОСЛАБЛЕНО, intentional and source-faithful: E27 now says the claim "перенос дату не меняет" was written once as an argument without a probe. FINDINGS' own text says "It was an argument, not a probe", and the Р-29 допущение (line 171) confirms it. The words "наблюдение 1" are gone from the text; "не проверено пробой" remains. A-N01, A-N02, A-N04 stay В ТЕКСТЕ.
 - A-097 (АДРЕС labs/sys/t-knowledge-synthesis.md) now В ТЕКСТЕ with the corrected address projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md; it exists (the old path does not exist in /tmp/canon, so the correction fixes a dead address).
 - C-040 pagination address engine.md -> engine-http.md: both files exist; section 4.9 is in engine-http.md. Still В ТЕКСТЕ (address improved).
 - C-N03..C-N06 and the SERVER_INDEX case: added Р-35 of projects/archive-recon/LOG.md, point 5 (497 by type, 483 by name, 14 without extension); verified. Still В ТЕКСТЕ.
 - C backup reason: "может лечь ... (вывод, не наблюдено)" is a hedge on the writer's own addition (round-1 list b), not a source unit; no loss.
 - B-N-heavy-book reason: "(гипотеза, для узла n8n не замерено)" hedges the writer's own causal claim (list b); B-N01..N04 unchanged.
 - 4.0 law and 4.2 intro narrowed: these were writer additions (list b); the narrowing makes them more accurate; no source unit lost.
No other unit lost or weakened. Totals after round 2: A 127 (126 В ТЕКСТЕ + 1 ОСЛАБЛЕНО from round 1) with A-N05 ОСЛАБЛЕНО added = 2 ОСЛАБЛЕНО; B 171 all В ТЕКСТЕ; C 114 all В ТЕКСТЕ; ПОТЕРЯНО 0.
