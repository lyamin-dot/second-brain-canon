# ACCEPTANCE round 2 — n8n-workflow-registry

Checked after `git pull` (HEAD 44a2e2e); router = reg/new/SKILL.md. Quotes verified by python as exact substrings of the cited line (0 failures).

## Counts

- CONFIRMED: 20
- NOT_FIXED: 1
- NEW_PROBLEM: 1

## Items

### A. Router

- LOST U043–U045 — **CONFIRMED** — new/SKILL.md:17 «Подтверждение прочтения — назвать найденную деталь и её пометку. Фиксированная фраза подтверждением не считается» — verbatim old SKILL.md:22
- WEAKENED U005 — **CONFIRMED** — new/SKILL.md:3 «Читай ТОЛЬКО когда нужна конкретная такая деталь» — «ТОЛЬКО» restored; the added «и неизвестно, в каком файле её искать» is inherent to a router (if the file is known, the router is not needed) — accepted
- WEAKENED U007, U041, U394 — **CONFIRMED** — new/SKILL.md:3 «а также перед записью в карточку Wildberries или Ozon и перед работой с декларациями через API» — both triggers of old SKILL.md:20 / cards:3 restored
- WEAKENED U047 — **CONFIRMED** — new/SKILL.md:38 «расписание, таймзона, вызовы» — «таймзона» restored
- task-2 item 3 — **CONFIRMED** — new/SKILL.md:34 «снятый скрипт `processDeclPdfInbox` (запускать его нельзя)» — prohibition restored
- task-3 item 12 — **CONFIRMED** — new/SKILL.md:30 «решение не менять ключ — запись Р-69 журнала `projects/wb-ue/LOG.md`» — object: projects/wb-ue/LOG.md:393 «(7) Ключ raw_key НЕ меняется»
- task-4 item 3 — **CONFIRMED** — new/SKILL.md:49 «Таблиц по каждому воркфлоу. Они уже были» — narrowed back to old SKILL.md:37
- task-5 item 3 — **CONFIRMED** — new/SKILL.md:26 «раздел «3. Внешние API и доменные детали», подразделы «Ozon — общее»» — all labels now verbatim old headings (old SKILL.md:112, 114, 118, 129, 136, 145); line 28 «подраздел «Wildberries» раздела 3» also matches

### B. Carriers

- task-2 item 1 (formula provenance) — **NOT_FIXED** — projects/wb-ue/STATE.md:62 «Формула сейчас одинакова в узле `06_Add_RAW_Key` обоих воркфлоу» — as announced: «прочитано get_workflow_details 2026-10-09» still absent; to owner list. Note: unrelated commit 2b2a9de (wb-ue STATE, Р-70) added 10 lines, so round-1 addresses projects/wb-ue/STATE.md:46 and :52 (U200–U206) are now :56 and :62 — content unchanged
- U231 — **CONFIRMED** — meta/CASES_wb-api.md:15 «Перед PATCH читать поле `editable`» — old SKILL.md:149 verbatim (python full-line match); redirect line 9 points to it correctly
- U471 — **CONFIRMED** — meta/CASES_ozon-api.md:41 «`EAEU` для декларации РОСС Ozon принял» — old cards:50 verbatim. Remark: the old fact itself is stronger than its source (projects/deklaration-ozon/LOG.md:133: only a check-mode run passed, a live run «загрузил бы») — inherited, not introduced
- task-3 item 2 — **CONFIRMED** — meta/CASES_ozon-api.md:7 «строки 115, 116, 119–127, 130–134, 138, 139, и references/cards-and-declarations.md, строки 50, 52, 54, 55» — python: every listed line present verbatim; no other old line present
- task-3 item 3 — **CONFIRMED** — meta/CASES_wb-api.md:7 «строки 147–156, 158, 166, 167, и references/cards-and-declarations.md, строки 11–13, 15, 17, 22, 30, 32–36, 38, 40, 42–45» — python: listed = present, exactly
- task-3 item 4 — **CONFIRMED** — registry/documents.md:174 «строки 18, 30, 64, 69–71, 75, 79, 81–96, 98, 104–106, 108» — python: all listed present (26–27 also present, table header of line 30 — harmless omission)
- task-3 item 5 — **CONFIRMED** — meta/CASES_wb-api.md:9 ««раздел 1» в абзаце об ОКПД 2 — абзац «Запись заменяет карточку целиком» этого файла» — that paragraph is meta/CASES_wb-api.md:40; false «раздел 4» claim removed
- task-3 item 6 — **CONFIRMED** — meta/CASES_wb-api.md:9 ««таблица в начале файла» в разделе «Права ключей» — книга N8N_CREDENTIALS, `registry/documents.md`, раздел «Книги Google Sheets»» — also Ф5 for Ozon roles / WB ping
- task-3 item 7 — **CONFIRMED** — meta/CASES_wb-api.md:59 «в строке выше устарело слово «только чтение»» — agrees with CASES_wb-api-card-write.md cases 3 and 4 and PROTOCOL_wb-card-write.md:17
- task-3 item 8 — **CONFIRMED** — meta/CASES_wb-api.md:53 «по кейсу 4 того же файла кейсов `kizMarked` не принимается без `needKiz`, даже когда ОКПД 2 записан» — agrees with case 4
- task-3 item 9 — **CONFIRMED** — projects/wb-reviews/PLAN.md:50 «осталось только общее правило — модель эмбеддингов совпадает с моделью индексации базы» — agrees with n8n-engineering-manual SKILL.md:97
- task-3 item 10 — **CONFIRMED** — registry/documents.md:174 «Утверждение «не названы нигде» ниже — снимок 26.09» — both named books verified: registry/documents.md:168, labs/ozon-ue/INDEX.md:38
- task-3 item 11 — **CONFIRMED** — projects/n8n/PLAN.md:81 «SKU Category Historical Backfill работает в книге лаборатории ozon-ue» — object: registry/n8n-map.md:394–397 (VWyXmCPJevCnbkZT writes book 1eQPV1…); labs/ozon-ue has no PLAN.md (second-brain-git lab.md 4б.3: two roles)

### C. Fix commits

- fix commit 81a1bf8 — **NEW_PROBLEM** — registry/documents.md:174 «остальные строки тех же разделов — в маршрутизаторе Skill и в `projects/n8n/PLAN.md`» — minor overstatement: old SKILL.md:72 (ИСТОРИЯ ДИАГНОЗА) and :100 (proposed removal) are in neither; headings 66/77 are not router labels either (router says «2.1–2.3»). Suggest «… или вынесены Андрею списком «предлагаю снять»», as in meta/CASES_wb-api.md:7

C, all ten fix commits (9e7ea31, ee0d702, 5f8b3a2, c8fc472, 8e9d164, 2ca732d, f27f061, 81a1bf8, 16b762b, 44a2e2e) were read as diffs: each touches one line or adds one line. Every replaced line keeps its earlier content: the provenance, the label meaning, the «строка 35» note, the RAG redirect, the Н13–Н19 pointer, the card-content-sync pointer and the 29-card Р-46 note. The only routing lost is the false «раздел 4» claim, which was removed on purpose. The router diff against round 1 changes only the requested lines. Nothing lost or distorted apart from the single NEW_PROBLEM above.
