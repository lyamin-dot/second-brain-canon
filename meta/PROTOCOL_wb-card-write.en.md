meta/PROTOCOL_wb-card-write.en.md

# WB card write via API — agent copy (compact)
Human version (RU, authoritative wording): meta/PROTOCOL_wb-card-write.md. Edit both together. Decisions: projects/deklaration-wb/LOG.md R-7, R-11, R-12, R-14, R-15, R-16 (written Р-NN, Cyrillic Р).

## TRUTH (field | WB char id | source)
- decl_no | 15001135 | LM_DECL (book LM_DECL_MASTER) = Price Master Artikel!X = WB_Compare!E ref_decl
- decl date_from | 15001137 | LM_DECL_MASTER sheet «Декларации».date_from, checked against the PDF extract: registration date, NOT 'date_to minus 1 year' (terms seen: 181, 216, 339 days; R-16). Write ONLY as DD.MM.YYYY; 'MM-DD-YY' makes WB create a document without a period -> 'Вы не приложили документ' (R-14)
- decl date_to | 15001138 | same sheet .date_to; NEVER write an expired decl
- tnved | 15000001 | from declaration extract; per-SKU reference = Price Master ARTIKEL_PROPS col N tnved_decl (col O tnved_decl_src = origin or why empty; LOG R-13). Empty -> no reference -> do not touch. Col C tnved = main-cabinet card value, NOT reference
- okpd2 | 15004292 | documents only (decl extract, Natl. catalog, importer). Analogy ban temporarily lifted 2026-10-09 ONLY for 11 IP autochem cards (R-12); any other card -> ask Andrei. 2026-10-10 Andrei also allowed okpd2 20.59.41.000 for 1345 and 1745 (manual KIZ; experiment, outcome in LOG R-16)
- kizMarked | card field | seller's legal statement; set only on Andrei's explicit word for named cards
- needKiz | card field, read-only | WB derives from subject+tnved+okpd2; API cannot set; without okpd2 WB won't accept via API (manual UI tick works). Reference = MAIN cabinet need_kiz (hand-checked)
- Current cabinet values are NOT truth. Never copy main -> IP.

## READ STATE
- WB_Cards_Staging (main, robot fGHfVrI58Ws1wfTw 04:10 MSK), WB_Cards_Staging_IP (IP, robot vIteQxGrqI7kLkb0 04:25 MSK), WB_Compare (formulas). Rules: meta/PRODUCT_DATA_HIERARCHY.md 4б, 4в.

## TOOLS (IP cabinet only; no batch tool for main yet)
- nIRKnhKyI5LibFW3 batch. 01_Params: mode 'проверка'|'запись', chunk=10, kizMarked, D{key:[no,from,to]}, rows[[nmID,sku,grp,declKey|'',tnved|'',okpd2|'']] ('' = untouched). Reads whole cabinet, keeps other chars, POST /content/v2/cards/update in chunks, 7 s apart. 04_Gate_Zapis ONLY=[n..] re-sends chosen chunks. Output: 03_Build.report (before->after), problems; 06_Report per-chunk status.
- 4dWCd1l1QiUQBPQQ single card. 01_Params: mode, nmID, set{charId:[vals]}, kizMarked. Waits 45 s, diffs.
- Keys: write «WB Kontent_ИП_Wr» OBHpKT8vPkAzVjH9; read WB_Контент_ИП_R.

## STEPS
1. Compute targets from sheets (not memory).
2. List disputes: no reference; expired reference; sources disagree (LM_DECL vs «Декларации».articles); other valid decl on card.
3. mode='проверка', run, check 03_Build (found count, problems empty, report).
4. Show summary + disputes to Andrei; write only after his OK.
5. mode='запись', run; 06_Report: 200 + empty error = accepted; random 400/500 "Internal server error" -> retry only failed chunks via ONLY.
6. Reset mode='проверка', ONLY=[]; append exec ids to 01_Params comment.
7. Verify NEXT DAY via staging sheets/WB_Compare (IP applies with hours delay; 45 s / 4 min reads show old card — not a rejection).
8. LOG.md entry + STATE.md next step.

## TRAPS
- Full overwrite drops okpd2 typed manually in UI (API doesn't return it) -> may drop needKiz (07.10: 29 main cards). Don't rewrite main-cabinet «Автохимия»/«Смазки автомобильные» without document okpd2.
- okpd2 in mandatory-marking list may switch needKiz on -> block if seller not registered in Честный знак for that group (IP oils 08.10).
- Each decl write recreates WB document (new id); interim verdict (supplier_not_registered) may turn ok hours later.
- Char values = array of strings: ["3403990000"], ["01.06.2026"].
- Sparse cards (e.g. 1053: 2 chars) are sent as is; tool invents nothing.
