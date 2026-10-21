# Acceptance — synthesis of Skill n8n-workflow-passport (2026-10-21)

Inputs checked: old_SKILL.md (byte-identical to /tmp/sbc/skills/n8n-workflow-passport/SKILL.md and to /mnt/skills/plugins/n8n-workflow-passport/SKILL.md — diff empty), new_SKILL.md, REPORT.md; clone /tmp/sbc (HEAD 3a553aa, working tree clean); live Skills /mnt/skills/plugins.

## A1 — every rule / exception / threshold / check kept at the same strength or delegated to a home that holds it — REFUTED

Counterexample 1 (widened silently, false on the object, pointer wrong).
- Old line 91: «У проектов, чей INDEX перенесён в репозиторий — например лаборатория `labs/sys/` — секции ИНСТРУМЕНТЫ нет вовсе (second-brain-git 4б.3).»
- New line 99: «У проектов в репозитории секции ИНСТРУМЕНТЫ нет вовсе (second-brain-git, 4б.3).»
- The new statement covers every project in the repository. It is false: /tmp/sbc/projects/wb-ue/PLAN.md:18 «## ИНСТРУМЕНТЫ (архитектурные факты…)», /tmp/sbc/projects/wb-logistics/PLAN.md:30 «## ИНСТРУМЕНТЫ». second-brain-git references/lab.md 4б.3 is about the two file roles of a laboratory only, not about projects. REPORT.md «Расширено» does not list this widening (item 3 even repeats the false premise: «секцию ИНСТРУМЕНТЫ INDEX, которой у проектов в репозитории нет»).

Counterexample 2 (narrowed by delegation: the reason of un-publishing is lost for a workflow without a passport).
- Old line 149, stage 5 step 3: «Записать, что воркфлоу снят и почему, туда, где проект хранит невзятое и снятое (обычно NOT_TAKEN.md или журнал проекта).»
- New line 152 delegates this record to «n8n-engineering-manual, `references/write.md`, раздел 2.5». Section 2.5 (line 88) lists what is written there: «ID, назначение, паспорт, как вернуть (`publish_workflow`)» — no reason. The reason («причина») appears in 2.5 only for the passport line. So for a workflow that has no passport, the obligation «записать почему» is no longer anywhere.

Counterexample 3 (delegation to a home whose rule differs).
- New line 152: «Ставший ненужным воркфлоу — временный зонд, пробный, одноразовый или вытесненный новым — снимается с публикации, но не архивируется и не удаляется. Само правило … — n8n-engineering-manual, `references/write.md`, раздел 2.5.»
- write.md 2.5 line 86: «Устаревшая версия инструмента, вытесненная новой, под запрет архивировать не подпадает: её можно архивировать (решение Андрея 2026-10-20).» The passport text calls 2.5 «the rule itself» while stating the opposite for the superseded case. Not a loss against the old text (old line 144 said the same as the new), but the claim «delegated to a section that really contains it» fails for this branch.

Everything else checked held: search route (three paths, case-insensitive, first hit stops), «get_workflow_details не вызывать» limited to understanding, live-code exceptions (edit/audit/acceptance/failure analysis/order), drift direction, «паспорта нет» path, «назвать ЧТО прочитано», zone table, «зона экономит внимание, не токены», create_file parameters and underscores, E14 fallback, PASSPORT line upper case, who writes it, 255 limit, create_workflow_from_code, check only by search output, «паспорт создан» only after check, temporary probe, INDEX-line abolished, stage 3а three items, stage 4 steps 1–3 and responsibilities, zone-write rules, 2 KB table, append ban, re-read, passport line «СТАТУС: СНЯТ С ПУБЛИКАЦИИ …», «АРХИВИРОВАН» variant, owner-only archiving, never delete passport, name scheme, debt recomputed by one search_workflows call, «при следующем касании, не пачкой».

## A2 — dropped cases are in REPORT.md and every named address holds the stated fact — REFUTED

Spot-checked as HOLDING (15): registry/protocols.md:16 PROTOCOL_system-map «НЕ ДЕЙСТВУЕТ с 2026-10-09 (харвест 2026-10-08, противоречие В16…)»; projects/deklaration-wb/LOG.md Р-5 (line 38–39: fGHfVrI58Ws1wfTw, узел 02_Fetch_WB_Cards «[имя ключа — запись Р-5 projects/deklaration-wb/LOG.md]» id [id ключа — там же]); Р-6 (line 47–48: temporary workflows not archived, cancels Р-15 ozon); projects/deklaration-ozon/LOG.md Р-20 (line 176: «техдокументация — часть каждой фазы», 2026-10-02) and Р-15 (line 125: archive probes); projects/git-migration/LOG.md Р-126 (owner said deactivated, search showed active:true); projects/archivarius/TRIAGE.md:147 У-126 (DO NOTHING/DO UPDATE, 182, 14 defects, WB_REVIEWS_INDEX 314, 2509–2512); projects/archivarius/LOG.md Р-38 exists; registry/maintenance-queue.md AJ-33 (j0DU23IXnp7xggX9, 234 chars vanished), AJ-34 point (3) (ПРИЁМКА placeholder, «Гипотеза (не проверена)», eight passports), AH-27; meta/PENDING_RULES.md row numbered 6 (file line 7); projects/n8n-map/PLAN.md section 3 (9 workflows, no credentials) and section 4 exists; projects/n8n/STATE.md section «Паспорта воркфлоу (2026-10-21, автопилот)» (18 active without PASSPORT); projects/wb-ue/PLAN.md:36 and labs/ozon-ue/INDEX.md:28 DOCS_FOLDER; core/R-06a.md 0.4.1 Skills exception; projects/deklaration-wb/PLAN.md:45 requires only presence of the PASSPORT line (REPORT correction is right). Dropped particulars of old lines 29, 40, 44, 50, 83, 114, 134, 136, 144, 148, 267–276 are all present in REPORT.md.

Counterexample 1.
- REPORT.md line 33: «Факт о четырёх воркфлоу Канала добавлен строкой в раздел «От соседнего проекта» того же файла» (projects/n8n/STATE.md).
- Checked: grep of /tmp/sbc/projects/n8n/STATE.md for «Git Read», «Git Log», «Git Append», «канал» — no such line; section «От соседнего проекта» (lines 53–59) has four entries, none about the Git channel passports. Git working tree is clean, so the line has not been written in the clone. (The fact itself still lives in REPORT.md line 16 and old line 44/274, so it is not lost — but the address stated in the report does not hold it.)

Counterexample 2.
- REPORT.md line 18 cites «`projects/n8n/STATE.md` (раздел «Правила, вынесенные из закрытых задач»)» as one of the 3 plans requiring that Андрей writes the PASSPORT line by hand.
- Checked: that section (STATE.md line 49) says the opposite: «Описание воркфлоу длиннее 255 знаков … операция setWorkflowMetadata не принимает: при правке описания через MCP сначала укоротить, сохранив строку PASSPORT, либо править в редакторе.» That permits MCP editing. The hand-only requirement is in another section of the same file — line 65, section «Паспорта воркфлоу (2026-10-21, автопилот)»: «Строку вписывает Андрей руками: описание через MCP заменяется целиком». STATE is also not a plan, while new line 93 counts «3 плана проектов, 2026-10-09».

Counterexample 3 (pending, low weight).
- New line 12 and every «Основание» point to `meta/SYNTHESIS_n8n-workflow-passport_2026-10-21.md`; REPORT.md line 7 points to folder `meta/SYNTHESIS_n8n-workflow-passport_2026-10-21/`. Neither exists in /tmp/sbc (`ls meta | grep -c SYNTHESIS_n8n-workflow-passport` = 0). Acceptable only if they are committed with the mirror; until then «every address in the new text exists» is false.

## A3 — pointers to other Skills lead to the mechanism attributed — REFUTED

Holding: google-drive-docs SKILL.md «ID воркфлоу — только из прочитанной строки реестра» (§1); references/docs-write.md 3.0 (1–2 KB caution line, «Условие пересмотра числа»), 3.2 (single-line anchor law, multiline `search` banned, «блок + перевод строки + тот же маркер», >2 KB via apply-from-file `replace`), 3.3 (create_folder contract), 3.6 (apply-from-file `replace` with `search`); references/docs-read.md:36 «ЦЕНА ЧТЕНИЯ»; references/failures.md:22 E14 (copy_file + gdocs-overwrite); n8n-engineering-manual references/write.md 2.2/2.3 (pre/post-flight with get_workflow_details), 2.5 (unpublish, active:false check, «деактивировал, в том числе от владельца»); references/roots.md R1a (R1a.5: «Отсутствие поля credentials у узла ещё не значит «ключа нет»»); R3 exists; SKILL.md line 16 «ПОДТВЕРЖДЕНИЕ ПОСЛЕ ПРОЧТЕНИЯ … Фиксированная фраза подтверждением не считается»; second-brain-engineer SKILL.md Р15 (line 94, write counted only after object read; line 87 «Считать запись выполненной по ответу инструмента (Р15)» forbidden); naryad references/issuer.md:162 «Утверждение документа о коде — посылка, а не факт».

Counterexample 1.
- New line 99: «У проектов в репозитории секции ИНСТРУМЕНТЫ нет вовсе (second-brain-git, 4б.3).» second-brain-git references/lab.md:20 «4б.3. Роли файлов лаборатории — две, других нет.» — it governs laboratories only; it says nothing about projects, and projects/wb-ue/PLAN.md and projects/wb-logistics/PLAN.md do have ИНСТРУМЕНТЫ sections.

Counterexample 2.
- New line 152 attributes «Само правило» (including «вытесненный новым … не архивируется») to write.md 2.5; 2.5 line 86 allows archiving a superseded version (see A1, counterexample 3). Also 2.5 does not hold «почему» in the NOT_TAKEN record (A1, counterexample 2).

## A4 — no case stories, no edit-history header, no ИСТОРИЯ ДИАГНОЗА, no particulars of objects — HOLDS, with one marginal counterexample

- Header is one line «Редакция 2026-10-21.» (new line 8); no ИСТОРИЯ ДИАГНОЗА block; no workflow IDs (scan for 16+ char tokens finds only file names, passport-name examples and template node names, all present in the old template).
- Marginal: new line 34, «Не путать» line, keeps an instance count and period: «так было при проверке девяти воркфлоу в августе–сентябре 2026». This is a particular of a past check (count of workflows) inside the Skill; the same fact is already in REPORT.md line 14. Severity low; a strict reading of «no instance counts» refutes A4 on this line only.

## A5 — headings, markers, name scheme, template, external references preserved — HOLDS

- Headings present: «Стадия 1» (39), «Стадия 2» (67), «Стадия 3» (82), «Стадия 3а» (103), «Стадия 4» (114), «Правило записи зон» (129), «Стадия 5» (150), «Шаблон паспорта» (170), «Где хранятся паспорта» (261).
- Template block: extracted fenced block old 164–245 vs new 172–253 — diff empty (all six markers %%ЗОНА_А/Б/В_НАЧАЛО/КОНЕЦ%% included). Name scheme `[ПРОЕКТ]_WF_[имя-воркфлоу]` and examples preserved.
- External references (`grep -rn n8n-workflow-passport /tmp/sbc /mnt/skills/plugins`): «стадия 1», «стадия 1 «Найти паспорт»», «стадия 3, пункт 5», «стадия 3а», «стадия 4», «стадия 5», «шаблон паспорта», «форма строки — Skill n8n-workflow-passport» (write.md 2.5), «пункт 3», «раздел 3» — all resolve. «§8», «§3», «§1» references (core/MANIFEST.md, meta/MAP_core-sections.md, projects/n8n-map/PLAN.md, projects/n8n/NOT_TAKEN.md) were already broken: the old text has a single «§» (old line 77) and it refers to google-drive-docs, not to this Skill. Renamed «Долги на 26.09.2026» has no external reference. The style quote cited by meta/SKILLS_MAP.md:112 («Этот файл построен как жизнь одного документа…») is still present (new line 10).

## Other findings (hypotheses)

H1. New line 89 «Безопасен для записи сессией только пустой `description`» can be read as permission for the session to write the PASSPORT line into an empty description, while the same bullet says «Кто вписывает: Андрей, руками». AJ-33 itself ends «Правило не меняется: строку вписывает Андрей.» The wording is listed in «Расширено» item 1, but the two sentences pull in opposite directions; suggest «единственный случай, когда запись сессией не испортит описание; правило не меняется — вписывает Андрей».
H2. New line 257 «механизм — n8n-engineering-manual, корень R3» (and the unchanged template comment): roots.md R3 (lines 100–108) lists `alwaysOutputData` switched off as a cause of the chain stopping; it does not contain the claim «пустой item, на котором падают чтения полей». Pre-existing in the old template, not created by the rewrite.
H3. New line 93 dates the owner requirement «3 плана проектов, 2026-10-09»; the plans checked carry no 2026-10-09 date for this requirement (card-content-sync PLAN:42, DECLARATION_SCAN:96), and the hand-only line in STATE is dated 2026-10-21.
H4. Line-number references to the old file (projects/archivarius/TRIAGE.md:335 «SKILL.md:44», meta/SKILLS_MAP.md «:91», «:96-98», «:8–:12») now point to different lines; they are historical and dated, so likely harmless.
H5. REPORT.md «Расширено» item 3 states as fact that repository projects have no ИНСТРУМЕНТЫ section; its own support (projects/wb-ue/PLAN.md:36) sits inside a «## ИНСТРУМЕНТЫ» section (line 18) of that PLAN.
H6. New text has three «Не путать» lines (lines 27, 34, 92), each on a different topic; the protocol allows one per false version, so this is consistent, but line 27 (SYSTEM-MAP) is a superseded carrier, not a refuted diagnosis.
