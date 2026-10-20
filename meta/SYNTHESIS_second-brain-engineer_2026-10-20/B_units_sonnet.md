/home/claude/second-brain-canon/meta/SYNTHESIS_second-brain-engineer_2026-10-20/B_units_sonnet.md

Group B, OLD text = commit baa077c, skills/second-brain-engineer/references/. Quotes are verbatim fragments (may be abridged with '...' where noted).

| id | file | line | class | quote | gloss |
|---|---|---|---|---|---|
| B-U001 | start.md | 3 | ПРАВИЛО | первое сообщение в Claude Project, мастер-промпт которого несёт блок Второго мозга | Read this file in full before replying to first message in a Project whose master prompt has the Second Brain block |
| B-U002 | start.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md | Section numbers are shared with SKILL.md |
| B-U003 | start.md | 3 | АДРЕС | ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md | Cross-part references resolve via the "what to read next" table in SKILL.md |
| B-U004 | start.md | 3 | СЛУЧАЙ | Файл выделен из SKILL.md раскладкой по триггеру 2026-10-20: текст разделов перенесён без изменения | File split out of SKILL.md on 2026-10-20 by trigger layout; text moved unchanged |
| B-U005 | start.md | 7 | ПРАВИЛО | Первое сообщение в Claude Project, мастер-промпт которого несёт блок Второго мозга (Р2) | Trigger of R1: first message in a Project with the block |
| B-U006 | start.md | 7 | ПРАВИЛО | Исполняется до ответа на само сообщение: сначала старт, потом ответ. | Startup runs before answering: start first, then reply |
| B-U007 | start.md | 7 | ИСКЛЮЧЕНИЕ | Вне Project (Cowork, Claude Code) автоматически не применяется — см. Р16. | Outside a Project startup does not auto-apply; see R16 |
| B-U008 | start.md | 8 | ПРАВИЛО | Тег, носитель и папку проекта называет блок мастер-промпта. | Tag, carrier and folder come from the master-prompt block |
| B-U009 | start.md | 8 | ПРАВИЛО | При расхождении блока с `registry/projects.md` прав реестр | On block/registry mismatch the registry wins |
| B-U010 | start.md | 8 | ПРАВИЛО | а расхождение называется в строке старта. | The mismatch is named in the startup line |
| B-U011 | start.md | 11 | ПРАВИЛО | Одним чтением — `meta/PENDING_RULES.md` и `projects/<папка>/STATE.md`. | Repo project: read PENDING_RULES and STATE.md in one read |
| B-U012 | start.md | 11 | АДРЕС | Чем читать — решает `second-brain-git` 7.6 (клон или Git-канал) | Reading method decided by second-brain-git 7.6 |
| B-U013 | start.md | 11 | ПРАВИЛО | выбранный путь назвать одной строкой. | Name the chosen read path in one line |
| B-U014 | start.md | 11 | ПРАВИЛО | Строки PENDING_RULES с полем «кто подтвердил: Андрей» действуют как правила Skill | PENDING_RULES rows confirmed by Andrei act as Skill rules |
| B-U015 | start.md | 11 | АДРЕС | (инвариант И-6 `second-brain-git`) | Basis: invariant I-6 of second-brain-git |
| B-U016 | start.md | 12 | ПРАВИЛО | Вывести ровно одну строку: | Output exactly one line (repo project) |
| B-U017 | start.md | 13 | ПОРОГ | `Контекст загружен: <ТЕГ> ¦ repo: STATE <sha7>, PENDING_RULES <sha7> ¦ Следующий шаг: <из STATE.md>` | Repo-project startup line format |
| B-U018 | start.md | 14 | ПОРОГ | ТЕГ — имя проекта прописными буквами, как в весах `registry/projects.md` (WB_UE, N8N, WB_REVIEWS) | TAG = project name uppercase as in registry weights |
| B-U019 | start.md | 14 | ПОРОГ | sha7 — первые 7 знаков blob sha прочитанного файла. | sha7 = first 7 chars of blob sha of file read |
| B-U020 | start.md | 15 | ПРАВИЛО | Молчать, ждать вопроса. | Stay silent, await question (repo) |
| B-U021 | start.md | 15 | ПРАВИЛО | Записи на старте нет | No write at startup for repo projects |
| B-U022 | start.md | 15 | ПРИЧИНА | полей LAST_UPDATED и LAST_READ у файлов repo нет, свежесть даёт git log. | Reason: repo files have no such fields; freshness via git log |
| B-U023 | start.md | 17 | ПРАВИЛО | Лаборатория в repo (`labs/<папка>/`): | Lab startup variant applies to labs/<folder>/ |
| B-U024 | start.md | 18 | ПРАВИЛО | Одним чтением — `meta/PENDING_RULES.md` и `labs/<папка>/INDEX.md`. | Lab: read PENDING_RULES and INDEX.md in one read |
| B-U025 | start.md | 18 | ПРАВИЛО | Тела задач на старте не читаются (`second-brain-git` 4б). | Task bodies not read at startup |
| B-U026 | start.md | 19 | ПРАВИЛО | Вывести ровно одну строку: | Lab: output exactly one line |
| B-U027 | start.md | 20 | ПОРОГ | `Контекст загружен: <ТЕГ> ¦ repo: INDEX <sha7>, PENDING_RULES <sha7> ¦ Задач: <число строк таблицы задач>` | Lab startup line format |
| B-U028 | start.md | 21 | ПРАВИЛО | Молчать, ждать вопроса. | Lab: stay silent, await question |
| B-U029 | start.md | 23 | ПРАВИЛО | Блок мастер-промпта может добавить к старту свои шаги (например, чтение CORE по манифесту) и свой формат строки. | Prompt block may add own startup steps and own line format |
| B-U030 | start.md | 23 | ПРАВИЛО | Добавка выполняется после шагов выше | Additions run after the steps above |
| B-U031 | start.md | 23 | ИСКЛЮЧЕНИЕ | если формат строки задан промптом, выводится он, а не строка выше. | If prompt sets line format, it replaces the default line |
| B-U032 | start.md | 25 | ПРАВИЛО | Проект в Docs (изолированный контур, Р4 п.0): | Docs-project startup variant applies to isolated circuit |
| B-U033 | start.md | 26 | ПРАВИЛО | Прочитать INDEX проекта через gdocs-read — только Зону А, до разделителя ЗОНА Б. | Docs: read only Zone A via gdocs-read up to ZONE B divider |
| B-U034 | start.md | 26 | ПРАВИЛО | `read_file_content` для Docs запрещён (google-drive-docs §0). | read_file_content forbidden for Docs |
| B-U035 | start.md | 26 | АДРЕС | (google-drive-docs §0) | Address of the prohibition |
| B-U036 | start.md | 26 | ПРАВИЛО | Зона А читается диапазоном строк (`fromLine`/`toLine`, google-drive-docs §3.5) | Zone A read by line range |
| B-U037 | start.md | 26 | ПРОВЕРКА | полнота среза доказывается наличием строки SENTINEL внутри него, а не доверием к числу. | Completeness proven by SENTINEL line in slice, not by trusting a number |
| B-U038 | start.md | 27 | ПОРОГ | «Контекст загружен: [проект] ¦ [LAST_UPDATED] ¦ Следующий шаг: [шаг]» | Docs startup line format |
| B-U039 | start.md | 27 | ПРАВИЛО | Вывести ОДНУ строку | Docs: output ONE line |
| B-U040 | start.md | 27 | ПОРОГ | Если LAST_UPDATED старше 7 дней — добавить «⚠️ Данные не обновлялись 7+ дней». | Staleness threshold 7 days adds warning |
| B-U041 | start.md | 28 | ПРАВИЛО | Обновить LAST_READ_BY_CLAUDE через gdocs-replace. | Docs: update LAST_READ_BY_CLAUDE via gdocs-replace |
| B-U042 | start.md | 29 | ПРАВИЛО | Молчать, ждать вопроса. | Docs: stay silent, await question |
| B-U043 | start.md | 30 | ПРОВЕРКА | Строка одна. Не список, не «кратко». | Check: line is one, not a list nor "briefly" |
| B-U044 | start.md | 30 | ПРОВЕРКА | В repo — в строке sha обоих прочитанных файлов | Check: repo line carries sha of both files |
| B-U045 | start.md | 30 | ПРОВЕРКА | полнота чтения — по `second-brain-git` 7.1. | Read completeness per second-brain-git 7.1 |
| B-U046 | start.md | 30 | ПРОВЕРКА | Для Docs — gdocs-replace вернул occurrencesChanged=1 и строка LAST_READ_BY_CLAUDE видна при обратном чтении. | Check for Docs: occurrencesChanged=1 and line visible on read-back |
| B-U047 | commands.md | 3 | ПРАВИЛО | сообщение Андрея начинается с команды из таблицы раздела Р8, целиком | Read file in full when message starts with a command from the R8 table |
| B-U048 | commands.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md | Section numbers shared with SKILL.md |
| B-U049 | commands.md | 3 | АДРЕС | ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md | Cross-references via "what to read next" table |
| B-U050 | commands.md | 3 | СЛУЧАЙ | Файл выделен из SKILL.md раскладкой по триггеру 2026-10-20: текст разделов перенесён без изменения | Split out 2026-10-20, text unchanged |
| B-U051 | commands.md | 7 | ПРАВИЛО | Сообщение Андрея начинается со слова из таблицы. | Trigger: message begins with a table word |
| B-U052 | commands.md | 8 | ПРАВИЛО | Исполнить по таблице, даже если мастер-промпт проекта команду не перечисляет. | Execute per table even if master prompt doesn't list the command |
| B-U053 | commands.md | 8 | ИСКЛЮЧЕНИЕ | Мастер-промпт может переопределить команду для своего проекта — тогда прав промпт. | Master prompt may override a command for its project; prompt wins |
| B-U054 | commands.md | 8 | ПРАВИЛО | CORE ни одна команда целиком не читает | No command reads CORE in full |
| B-U055 | commands.md | 8 | ПРАВИЛО | перед записью вида, названного в таблице «По событию» `core/MANIFEST.md`, читаются файлы её строки. | Before a write of a kind named in MANIFEST "by event" table, read that row's files |
| B-U056 | commands.md | 13 | АДРЕС | !save ¦ Р7 (references/save.md). | !save command points to R7 in save.md |
| B-U057 | commands.md | 13 | ПРАВИЛО | !tasks: Открытые задачи текущего проекта по меткам | !tasks lists open tasks of current project by labels |
| B-U058 | commands.md | 13 | ПРАВИЛО | repo-проект — `STATE.md`; лаборатория — таблица `INDEX.md`; Docs — Зона А INDEX. | !tasks source per carrier |
| B-U059 | commands.md | 14 | ПОРОГ | Приоритет = метка × вес проекта (БЛОКЕР 4, РЫЧАГ 3, РУТИНА 2, ЗОМБИ 1 | !priority formula and label weights |
| B-U060 | commands.md | 14 | АДРЕС | веса — `registry/projects.md` | Project weights live in registry/projects.md |
| B-U061 | commands.md | 14 | ПРАВИЛО | Задача без метки — отдельной строкой «метки нет», не оценивается и метка не угадывается. | Unlabeled task: separate line "no label", not scored, label not guessed |
| B-U062 | commands.md | 14 | ПРАВИЛО | Без аргумента — текущий проект; со словом «все» — все активные проекты реестра. | !priority scope: default current project; "все" = all active registry projects |
| B-U063 | commands.md | 14 | ПОРОГ | !priority [high/low/Xh] | !priority argument forms |
| B-U064 | commands.md | 15 | ПРАВИЛО | !inbox: Необработанный Inbox: Google Doc, ID — `registry/documents.md`, строка INBOX; читать gdocs-read | !inbox reads unprocessed Inbox doc via gdocs-read |
| B-U065 | commands.md | 15 | АДРЕС | формат записей — `core/R-08.md` | Inbox entry format in core/R-08.md |
| B-U066 | commands.md | 15 | ПРАВИЛО | Каждая запись разбирается захватом (Р6) в проект, которому принадлежит. | Each inbox entry processed by capture R6 into its owning project |
| B-U067 | commands.md | 16 | ПРАВИЛО | !review: текущий проект — `STATE.md` (лаборатория — `INDEX.md`) и оглавление журнала | !review current project: STATE/INDEX plus log table of contents |
| B-U068 | commands.md | 16 | ПРАВИЛО | со словом «все» — `STATE.md` всех repo-проектов реестра, `INDEX.md` лабораторий и Зона А Docs-проектов. | !review "все": all repo STATE, lab INDEX, Docs Zone A |
| B-U069 | commands.md | 17 | ПРАВИЛО | !status: Блокеры с дедлайнами по всем активным проектам и реестр протоколов (документ SYS_PROTOCOL_REGISTRY, ID — `registry/documents.md`) целиком, таблицей, все строки. | !status: blockers with deadlines for all active projects plus full protocol registry as table, all rows |
| B-U070 | commands.md | 17 | ИСКЛЮЧЕНИЕ | Мастер-промпт проекта может задать своё значение (N8N — здоровье инстанса по снимку). | Master prompt may redefine !status (N8N: instance health from snapshot) |
| B-U071 | commands.md | 18 | ПРАВИЛО | !digest [период]: Дайджест CHANGELOG за период, по умолчанию 30 дней | !digest of CHANGELOG, default 30 days |
| B-U072 | commands.md | 18 | ПОРОГ | по умолчанию 30 дней | Default digest period 30 days |
| B-U073 | commands.md | 18 | АДРЕС | CHANGELOG — Google Doc, ID — `registry/documents.md`, читать gdocs-read | CHANGELOG doc ID in registry/documents.md, read via gdocs-read |
| B-U074 | commands.md | 19 | ПРАВИЛО | !map: Команда проекта N8N: карта связей проектов и воркфлоу как артефакт | !map is an N8N-project command: links map as artifact |
| B-U075 | commands.md | 19 | АДРЕС | разделы «Связи» в `projects/*/PLAN.md`, строки X и H снимка `registry/n8n-map.md` | !map sources: PLAN.md Links sections and X/H rows of n8n-map snapshot |
| B-U076 | commands.md | 19 | ИСКЛЮЧЕНИЕ | В других проектах — ответить, что карта строится в N8N, и не исполнять. | In other projects: answer that map is built in N8N, do not execute |
| B-U077 | commands.md | 20 | АДРЕС | харвест ¦ Р11. | харвест command points to R11 |
| B-U078 | commands.md | 20 | ИСКЛЮЧЕНИЕ | Команда проекта SYS; в других проектах — ответить, что она запускается в SYS, и не исполнять. | харвест is SYS-only; elsewhere answer it runs in SYS and don't execute |
| B-U079 | commands.md | 22 | ПРАВИЛО | Естественноязыковой эквивалент !status: любой вопрос «как дела с системой / что с протоколами / какой прогресс» = !status | Natural-language questions about system state equal !status |
| B-U080 | commands.md | 22 | ПРАВИЛО | с полным реестром, без отбора «интересных». | Full registry, no selection of "interesting" rows |
| B-U081 | commands.md | 23 | ПРОВЕРКА | Ответ на команду назвал прочитанные файлы (Р15) | Check: command answer names files read |
| B-U082 | commands.md | 23 | ПРОВЕРКА | у !priority каждая строка несёт метку и вес или пометку «метки нет». | Check: every !priority row has label and weight or "no label" |
| B-U083 | search.md | 3 | ПРАВИЛО | действие затрагивает другой проект или Андрей просит найти документ, паспорт, ссылку, целиком | Read file in full when action touches another project or user asks to find doc/passport/link |
| B-U084 | search.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md | Numbers shared with SKILL.md |
| B-U085 | search.md | 3 | АДРЕС | ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md | Cross-references via the table |
| B-U086 | search.md | 3 | СЛУЧАЙ | Файл выделен из SKILL.md раскладкой по триггеру 2026-10-20: текст разделов перенесён без изменения | Split out 2026-10-20 unchanged |
| B-U087 | search.md | 7 | ПРАВИЛО | Действие затрагивает другой проект / просьба найти документ, паспорт, ссылку. | R9 trigger |
| B-U088 | search.md | 8 | ПРАВИЛО | Затрагивает другой проект — сказать: «⚡ Это затрагивает [ПРОЕКТ]: [что]». | Say aloud which other project is touched |
| B-U089 | search.md | 8 | ПРАВИЛО | определить все связанные проекты → прочитать их INDEX целиком через gdocs-read (repo-проекты — STATE/PLAN) | Search step 1: identify related projects, read their INDEX in full |
| B-U090 | search.md | 8 | ПРАВИЛО | → извлечь ID и ссылки → только после этого внешние инструменты (n8n MCP, google_drive_search) | Search step 2: extract IDs, only then external tools |
| B-U091 | search.md | 8 | ПРАВИЛО | Перед проектированием нового шага, который может уже быть решён у соседа, — оглавление журнала соседа по теме | Before designing a step possibly solved by a neighbor, check neighbor log TOC |
| B-U092 | search.md | 8 | АДРЕС | (`second-brain-git` 7.6, в среде с клоном — `grep`) | Method: second-brain-git 7.6, grep in clone environment |
| B-U093 | search.md | 8 | ПРАВИЛО | решённое в одном проекте в другом не изобретается заново | Solved in one project is not reinvented in another |
| B-U094 | search.md | 8 | АДРЕС | (`meta/DECLARATION_COMMON.md`, раздел 4, пункт 5) | Basis address: DECLARATION_COMMON section 4 item 5 |
| B-U095 | search.md | 8 | ПРАВИЛО | Паспорта воркфлоу — по маршруту поиска Skill `n8n-workflow-passport`: строка PASSPORT в description воркфлоу (искать без учёта регистра), затем имя документа в папке DOCS проекта | Workflow passports: search PASSPORT line in description case-insensitive, then doc name in DOCS folder |
| B-U096 | search.md | 8 | АДРЕС | живой состав воркфлоу и их связи — снимок `registry/n8n-map.md` | Live workflow set and links in n8n-map snapshot |
| B-U097 | search.md | 8 | ПРАВИЛО | Не по одному «привычному» INDEX. | Do not search just one familiar INDEX |
| B-U098 | search.md | 9 | ПРОВЕРКА | «Документ не найден» произносится только после полного обхода всех релевантных INDEX | Say "doc not found" only after full walk of all relevant INDEX |
| B-U099 | search.md | 9 | ПРОВЕРКА | google_drive_search чтение INDEX не заменяет. | google_drive_search does not replace reading INDEX |
| B-U100 | permissions.md | 3 | ПРАВИЛО | перед изменением воркфлоу n8n, перед действием, требующим «да» Андрея или его рук, и перед выдачей наряда, целиком | Read in full before n8n workflow change, before action needing Andrei's yes/hands, before issuing a naryad |
| B-U101 | permissions.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md | Numbers shared with SKILL.md |
| B-U102 | permissions.md | 3 | АДРЕС | ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md | Cross-references via the table |
| B-U103 | permissions.md | 3 | СЛУЧАЙ | Файл выделен из SKILL.md раскладкой по триггеру 2026-10-20: текст разделов перенесён без изменения | Split out 2026-10-20 unchanged |
| B-U104 | permissions.md | 7 | ПРАВИЛО | Любое изменение воркфлоу. | R10 trigger: any workflow change |
| B-U105 | permissions.md | 8 | ПРАВИЛО | «Воркфлоу [имя], узел [имя]. Планирую: [описание]. Подтверждаешь?» → ждать явного «да». | Announce workflow/node/plan and wait for explicit yes |
| B-U106 | permissions.md | 8 | ПРАВИЛО | При отладке — сначала предложить копию воркфлоу. | When debugging, first offer a workflow copy |
| B-U107 | permissions.md | 8 | ИСКЛЮЧЕНИЕ | Исключение — пакет правок, на который Андрей дал одно разрешение и который записан списком задач в `STATE.md` или `LOG.md` проекта | Exception: batch of edits with one permission recorded as task list in STATE/LOG |
| B-U108 | permissions.md | 8 | ПРАВИЛО | в пределах списка узел и изменение называются вслух, повторного «да» не ждать | Within the batch: name node and change aloud, don't wait for repeated yes |
| B-U109 | permissions.md | 8 | ИСКЛЮЧЕНИЕ | правка вне списка — снова по общему правилу | Edit outside the batch list: general rule again |
| B-U110 | permissions.md | 8 | ПРАВИЛО | После правки — ADR в паспорт воркфлоу (Skill `n8n-workflow-passport`). | After edit write ADR to workflow passport |
| B-U111 | permissions.md | 8 | АДРЕС | Механика (параметры, credentials, шаблоны, ошибки, сбросы настроек при update_workflow) — `n8n-engineering-manual`, здесь не дублируется. | Mechanics live in n8n-engineering-manual, not duplicated |
| B-U112 | permissions.md | 9 | ПРОВЕРКА | «Да» Андрея есть в чате до вызова, либо задача названа в записанном пакете разрешения (адрес записи назван). | Check: yes in chat before call, or task named in recorded permission batch with address |
| B-U113 | permissions.md | 16 | ПРАВИЛО | Перед действием, которое требует «да» Андрея или его рук (удаление данных, изменение воркфлоу n8n, структуры INDEX или мастер-промпта, правка Skill, действие на 3 и более узла) | R13 trigger: actions requiring Andrei's yes or hands |
| B-U114 | permissions.md | 16 | ПРАВИЛО | перед записью, право на которую сессия не помнит, и перед выдачей наряда | R13 trigger also: write whose permission session doesn't remember; issuing a naryad |
| B-U115 | permissions.md | 16 | СЛУЧАЙ | Назначен при раскладке 2026-10-20. | Trigger assigned in 2026-10-20 layout |
| B-U116 | permissions.md | 16 | ПОРОГ | действие на 3 и более узла | Threshold in trigger: 3 or more nodes |
| B-U117 | permissions.md | 18 | ПРАВИЛО | Claude автономно: создать INDEX / папку проекта | Autonomous: create INDEX / project folder |
| B-U118 | permissions.md | 18 | ПРАВИЛО | зарегистрировать проект в `registry/projects.md` и ID его INDEX в `registry/documents.md` (прежние CORE Р.1 и Р.2) | Autonomous: register project and INDEX ID |
| B-U119 | permissions.md | 18 | ПРАВИЛО | зарегистрировать в `registry/documents.md` документ или таблицу, созданные в сессии (Р6) | Autonomous: register session-created doc/table |
| B-U120 | permissions.md | 18 | ПРАВИЛО | подготовить мастер-промпт; записать захваты при !save | Autonomous: prepare master prompt; write captures at !save |
| B-U121 | permissions.md | 18 | ПРАВИЛО | обновить LAST_UPDATED / LAST_READ_BY_CLAUDE / STATE.md; перенести закрытую задачу в АРХИВ | Autonomous: update markers/STATE, move closed task to ARCHIVE |
| B-U122 | permissions.md | 18 | ПРАВИЛО | записать баг / прогресс; дописать позицию в `registry/maintenance-queue.md` | Autonomous: write bug/progress; append item to maintenance-queue |
| B-U123 | permissions.md | 19 | ПРАВИЛО | Claude после «да»: изменение воркфлоу n8n | After yes: n8n workflow change |
| B-U124 | permissions.md | 19 | ПРАВИЛО | удаление данных из INDEX и repo | After yes: deleting data from INDEX and repo |
| B-U125 | permissions.md | 19 | ПРАВИЛО | изменение структуры INDEX или мастер-промпта (отдельным действием, текстом «было → стало») | After yes: INDEX/master-prompt structure change as separate action with before→after text |
| B-U126 | permissions.md | 19 | ПОРОГ | действие, затрагивающее >3 нод | After yes: action touching >3 nodes (note: R13 trigger says 3 or more) |
| B-U127 | permissions.md | 20 | ПРАВИЛО | Андрей обязан (блокирует систему): создать Claude Project и прислать URL | Andrei must: create Claude Project and send URL |
| B-U128 | permissions.md | 20 | ПРАВИЛО | привязать credentials в n8n; решить об удалении; подтвердить структурные изменения; перезалить Skill | Andrei must: bind credentials, decide deletion, confirm structural changes, re-upload Skill |
| B-U129 | permissions.md | 20 | ПРАВИЛО | сохранить старый текст мастер-промпта файлом до вставки нового | Andrei must save old master-prompt text as file before pasting new |
| B-U130 | permissions.md | 20 | ПРИЧИНА | текст живёт только в интерфейсе Anthropic, инструментом не читается и не откатывается | Reason: prompt lives only in Anthropic UI, not readable or revertible by tool |
| B-U131 | permissions.md | 20 | ПРАВИЛО | Наряд с DoD «промпт переключён» без этого файла не выдаётся. | No naryad with DoD "prompt switched" without that file |
| B-U132 | permissions.md | 21 | ПРАВИЛО | Правка Skill действует только после перезаливки. | Skill edit effective only after re-upload |
| B-U133 | permissions.md | 21 | АДРЕС | Живой Skill — тот, что лежит в Customize → Skills | Live Skill is the one in Customize → Skills |
| B-U134 | permissions.md | 21 | ПРАВИЛО | многофайловый Skill (SKILL.md и папка references/) заливает Андрей zip-архивом там же | Multi-file Skill uploaded by Andrei as zip there |
| B-U135 | permissions.md | 21 | ИСКЛЮЧЕНИЕ | кнопка Save skill в Cowork для него не годится — она заменяет только SKILL.md | Cowork Save skill button unsuitable: replaces only SKILL.md |
| B-U136 | permissions.md | 21 | АДРЕС | (`google-drive-docs`, раздел 12) | Address: google-drive-docs section 12 |
| B-U137 | permissions.md | 21 | ПРАВИЛО | Текст правки, выданный в чате, записанный в зеркало `skills/` репозитория или в файл Drive, ничего не меняет, пока zip не залит. | Edit text in chat/mirror/Drive file changes nothing until zip uploaded |
| B-U138 | permissions.md | 21 | ПРИЧИНА | сессия видит Skill только снимком из аккаунта (`/mnt/skills/`) и только читает его | Reason: session sees Skill only as account snapshot, read-only |
| B-U139 | permissions.md | 21 | ПРОВЕРКА | Признак: правка «внесена» по словам, а в снимке Skill старый текст. | Symptom: edit "applied" by words but snapshot has old text |
| B-U140 | permissions.md | 21 | ПРОВЕРКА | правка Skill закрывается приёмкой по снимку в той сессии, которая на него опирается — по якорю правки или побайтово | Skill edit closed by acceptance against snapshot, by anchor or byte-wise |
| B-U141 | permissions.md | 21 | АДРЕС | механика приёмки, зеркала и сверки перед заливкой — `second-brain-git` 2.6 | Acceptance/mirror/pre-upload check mechanics in second-brain-git 2.6 |
| B-U142 | permissions.md | 21 | АДРЕС | решение владельца В12 харвеста 2026-10-18 (`meta/HARVEST_2026-10-18_answers.md`: канон — живой Skill, зеркало — копия) | Basis: owner decision V12 of harvest 2026-10-18 |
| B-U143 | permissions.md | 21 | СЛУЧАЙ | запись Р-12 журнала `projects/kontext-reduktion/LOG.md` (многофайловый Skill — только zip) | Case: log entry R-12 (multi-file Skill only via zip) |
| B-U144 | permissions.md | 21 | СЛУЧАЙ | запись Р-32 того же журнала (заливка без сверки стёрла бы пункт живого Skill) | Case: log entry R-32 (upload without check would erase a live Skill item) |
| B-U145 | permissions.md | 22 | ПРАВИЛО | Андрей может безопасно: wb_inbox / oz_inbox; executions и ручные запуски в n8n; данные в строках Sheets. | Andrei may safely touch wb_inbox/oz_inbox, executions/manual runs, Sheets row data |
| B-U146 | permissions.md | 23 | ПРАВИЛО | Андрей не должен: менять структуру INDEX напрямую; переименовывать/удалять воркфлоу без согласования | Andrei must not change INDEX structure directly or rename/delete workflows without agreement |
| B-U147 | permissions.md | 23 | ПРАВИЛО | менять колонки Sheets; править середину функций Apps Script (только полная замена) | Andrei must not change Sheets columns or edit mid-function Apps Script (full replacement only) |
| B-U148 | permissions.md | 29 | ПРАВИЛО | Перед выдачей наряда или задания исполнителю (субагенту, посреднику) — выбор класса модели. | R18 trigger: before issuing naryad/task to executor, choose model class |
| B-U149 | permissions.md | 29 | СЛУЧАЙ | Назначен при раскладке 2026-10-20. | Trigger assigned in 2026-10-20 layout |
| B-U150 | permissions.md | 31 | ПРАВИЛО | Шаг с написанной процедурой и готовой гипотезой — модель среднего уровня | Step with written procedure and ready hypothesis: mid-level model |
| B-U151 | permissions.md | 31 | ПРАВИЛО | диагностика и проектирование без гипотезы — модель высокого уровня | Diagnosis/design without hypothesis: high-level model |
| B-U152 | permissions.md | 31 | АДРЕС | Роли наряда — `naryad`. | Naryad roles are in skill naryad |
| B-U153 | outside.md | 3 | ПРАВИЛО | работа над проектом вне Claude Project или вскрылся факт, требующий правки CORE, INDEX, Skill или мастер-промпта, целиком | Read in full when working outside a Project or a fact needs edit of CORE/INDEX/Skill/prompt |
| B-U154 | outside.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md | Numbers shared with SKILL.md |
| B-U155 | outside.md | 3 | АДРЕС | ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md | Cross-references via the table |
| B-U156 | outside.md | 3 | СЛУЧАЙ | Файл выделен из SKILL.md раскладкой по триггеру 2026-10-20: текст разделов перенесён без изменения | Split out 2026-10-20 unchanged |
| B-U157 | outside.md | 7 | ПРАВИЛО | Сессия в Cowork / Claude Code / GitHub Actions работает над проектом системы | R16 trigger: session in Cowork/Claude Code/GitHub Actions on system project |
| B-U158 | outside.md | 7 | ПРАВИЛО | либо любая сессия вскрыла факт, требующий правки CORE / SYS_INDEX / INDEX / Skill / мастер-промпта | R16 trigger: any session uncovering a fact requiring edit of CORE/INDEX/Skill/prompt |
| B-U159 | outside.md | 9 | ИСКЛЮЧЕНИЕ | Феникс (Р1) вне Project автоматически не срабатывает | Phoenix R1 does not auto-fire outside a Project |
| B-U160 | outside.md | 9 | АДРЕС | эстафета (`context-handoff`) — ручной мост, она не меняет ни один файл. | Handoff is a manual bridge, changes no file |
| B-U161 | outside.md | 10 | ПРАВИЛО | Запись доступна из любой среды: git-канал и gdocs-* вызываются по HTTP, исполняет сервер n8n. | Writing available from any environment via HTTP, executed by n8n server |
| B-U162 | outside.md | 10 | ПРИЧИНА | Ограничение — дисциплина, не инструмент. | The limit is discipline, not tooling |
| B-U163 | outside.md | 11 | ПРАВИЛО | Правка, которую сессия МОЖЕТ сделать (CORE, задачи лаборатории `labs/sys/`, INDEX Docs-проектов, файлы repo) — делается до конца сессии | Edits the session CAN make are done before session ends |
| B-U164 | outside.md | 11 | ПРАВИЛО | по правильному якорю, с верификацией Р15 | Done at the right anchor, verified per R15 |
| B-U165 | outside.md | 11 | СЛУЧАЙ | Документ SYS_INDEX заморожен 2026-09-23 (Р-109 журнала `projects/git-migration/LOG.md`) | SYS_INDEX frozen 2026-09-23, entry R-109 |
| B-U166 | outside.md | 11 | СЛУЧАЙ | его Зона А с 2026-09-14 живёт в `labs/sys/`, и правки туда больше не идут | Its Zone A lives in labs/sys/ since 2026-09-14; no edits go there |
| B-U167 | outside.md | 12 | ПРАВИЛО | Правка, которую сессия НЕ МОЖЕТ сделать (Skill, мастер-промпт — аккаунтный слой, правит только Андрей) — регистрируется позицией в `registry/maintenance-queue.md` | Edits the session CANNOT make are registered as a maintenance-queue item |
| B-U168 | outside.md | 12 | ПОРОГ | через Git Append File (запасной путь — Git Append; `second-brain-git` 8.3) | Tool: Git Append File, fallback Git Append |
| B-U169 | outside.md | 12 | ПОРОГ | № ¦ что внести ¦ куда ¦ источник ¦ дата смерти ¦ статус | Queue row column format |
| B-U170 | outside.md | 12 | ПРАВИЛО | Позиция без даты смерти не существует. | Item without death date does not exist |
| B-U171 | outside.md | 12 | ПРАВИЛО | Номер берётся из свежего чтения непосредственно перед вызовом | Number taken from a fresh read right before the call |
| B-U172 | outside.md | 12 | СЛУЧАЙ | однобуквенные префиксы A–Z в файле исчерпаны 2026-09-24 | Single-letter prefixes A–Z exhausted 2026-09-24 |
| B-U173 | outside.md | 12 | ПРАВИЛО | новые позиции берут двухбуквенный префикс | New items use two-letter prefix |
| B-U174 | outside.md | 12 | ПРАВИЛО | Текст позиции не должен содержать внутренних переводов строки | Item text must not contain internal newlines |
| B-U175 | outside.md | 12 | ПРИЧИНА | они разрывают строку таблицы, и колонки «Дата смерти» и «Статус» уезжают на другую физическую строку, из-за чего харвест видит позицию без даты смерти | Reason: newlines split table row so harvest sees item without death date |
| B-U176 | outside.md | 12 | ПРАВИЛО | Пересказ в чате и текст эстафеты регистрацией не являются. | Chat retelling and handoff text are not registration |
| B-U177 | outside.md | 12 | АДРЕС | Очередь читает харвест (Р11). | The queue is read by harvest R11 |
| B-U178 | outside.md | 13 | ПРИЧИНА | Харвест не сканирует внешние чаты: незарегистрированное обязательство для системы не существует. | Harvest doesn't scan external chats; unregistered commitment doesn't exist |
| B-U179 | outside.md | 14 | ПРОВЕРКА | Позиция видна при обратном чтении очереди по `second-brain-git` 8.1 | Check: item visible on queue read-back per 8.1 |
| B-U180 | outside.md | 14 | ПРАВИЛО | без клона — Git Read Lines с pattern по номеру позиции | Without clone: Git Read Lines with pattern by item number |
| B-U181 | outside.md | 14 | ПРОВЕРКА | в ответе назван её номер. | Check: item number named in reply |
| B-U182 | save.md | 3 | ПРАВИЛО | перед командой !save в проекте любого носителя (repo-проект, лаборатория, Docs) и перед записью в Зону А INDEX, целиком | Read in full before !save on any carrier and before writing to Zone A |
| B-U183 | save.md | 5 | СЛУЧАЙ | Правка 2026-10-09 (харвест 2026-10-08): в «Для всех носителей» добавлены два шага | History note: 2026-10-09 edit added two all-carrier steps |
| B-U184 | save.md | 5 | СЛУЧАЙ | строка SYSTEM-MAP в Р12 заменена — карта заменена снимком `registry/n8n-map.md` | History note: SYSTEM-MAP line in R12 replaced by snapshot |
| B-U185 | save.md | 7 | СЛУЧАЙ | Правка 2026-10-06: Р7 разделён по трём носителям и стал единственным местом порядка !save | History: 2026-10-06 R7 split by three carriers, sole place of !save order |
| B-U186 | save.md | 7 | ПРИЧИНА | мастер-промпты проектов его больше не пересказывают (Р2) | History: master prompts no longer retell it |
| B-U187 | save.md | 7 | СЛУЧАЙ | CHANGELOG получил форму записи и адрес; добавлен шаг ADR после правки воркфлоу; показ захватов перестал ждать отдельного подтверждения | History: CHANGELOG form/address, ADR step added, capture display no longer awaits confirmation |
| B-U188 | save.md | 7 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md; ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md. | Numbers shared; cross-refs via table |
| B-U189 | save.md | 9 | СЛУЧАЙ | Правка 2026-09-24, вторая (решение Р-111 журнала `projects/git-migration/LOG.md`, решения Р-3 и Р-5 журнала `projects/kontext-reduktion/LOG.md`) | History: 2026-09-24 second edit, decisions R-111, R-3, R-5 |
| B-U190 | save.md | 9 | ПРАВИЛО | CORE читается по таблице «Список» Манифеста плюс строке таблицы «По событию», которая называет !save | CORE read per MANIFEST List table plus the by-event row naming !save |
| B-U191 | save.md | 9 | ПРАВИЛО | `meta/header.md` не читается | meta/header.md is not read |
| B-U192 | save.md | 9 | ПРАВИЛО | сверка byteLength с текстом снята | byteLength vs text comparison dropped |
| B-U193 | save.md | 9 | ПРИЧИНА | воркфлоу считает byteLength из тех же байт, что и text, и сверка ничего не доказывала (second-brain-git 7.1) | Reason: workflow computes byteLength from same bytes, so check proved nothing |
| B-U194 | save.md | 13 | ПРАВИЛО | Команда !save; согласие Андрея на предложенный !save (Р6). | R7 trigger: !save command or Andrei's consent to proposed !save |
| B-U195 | save.md | 15 | ПРАВИЛО | Показать список [ЗАХВАЧЕНО] сессии одним блоком и сразу записывать: сама команда — согласие на запись этого списка. | Show captures list in one block and write immediately; command is consent |
| B-U196 | save.md | 15 | ПРАВИЛО | Строку, которую Андрей вычеркнет после, отменить новой записью, а не правкой задним числом. | A line Andrei strikes later is cancelled by a new entry, not edited retroactively |
| B-U197 | save.md | 16 | ПРАВИЛО | Для каждой строки определить проект (тег захвата) и его носитель (Р0). | For each line determine project (capture tag) and carrier |
| B-U198 | save.md | 16 | ПРАВИЛО | Строка чужого проекта пишется в канон того проекта, с пометкой «⚡» в записи. | Foreign-project line written to that project's canon with ⚡ mark |
| B-U199 | save.md | 18 | АДРЕС | Проект в repo и лаборатория — как писать, решает `second-brain-git`, здесь не пересказывается | For repo/lab how to write is decided by second-brain-git |
| B-U200 | save.md | 19 | АДРЕС | Проект в repo — `second-brain-git` 10 (маршрут по файлам — 10.3, транспорт — 8.3, порядок нескольких файлов — 8.6, форма записи журнала — 11) | Repo project: second-brain-git 10, 10.3, 8.3, 8.6, 11 |
| B-U201 | save.md | 19 | АДРЕС | Лаборатория — `second-brain-git` 4б (задача заводится и закрывается вместе с правкой `INDEX.md`) | Lab: second-brain-git 4б; task created/closed with INDEX.md edit |
| B-U202 | save.md | 19 | ПРАВИЛО | До первой записи в сессии прочитать нужную часть того Skill целиком. | Before first write in session read needed part of that Skill in full |
| B-U203 | save.md | 20 | ПРАВИЛО | Находка лаборатории без своей задачи — туда, куда велит мастер-промпт лаборатории (например, Зона Б её Docs-документа) | Lab finding without task goes where lab master prompt directs (e.g. Zone B) |
| B-U204 | save.md | 20 | ПРАВИЛО | промпт не велит — предложить Андрею завести задачу | If prompt doesn't direct, propose Andrei create a task |
| B-U205 | save.md | 20 | ПРИЧИНА | Это решение о месте, а не механика записи, поэтому оно здесь. | Reason it's here: it's a placement decision, not write mechanics |
| B-U206 | save.md | 22 | ПРАВИЛО | Проект в Docs (изолированный контур): | Docs-project !save steps follow |
| B-U207 | save.md | 23 | ПРАВИЛО | Прочитать `registry/documents.md` для актуальных ID. | Docs: read registry/documents.md for current IDs |
| B-U208 | save.md | 24 | ПРАВИЛО | новая ОТКРЫТАЯ задача → gdocs-replace по якорю прямо в ОТКРЫТЫЕ ЗАДАЧИ Зоны А (не в хвост!) | Docs: new open task via gdocs-replace by anchor into Zone A open tasks, not the tail |
| B-U209 | save.md | 24 | ПРАВИЛО | нарратив (РЕШЕНИЯ / ПРОГРЕСС / БАГИ / АРХИВ) → gdocs-append в Зону Б | Docs: narrative via gdocs-append into Zone B |
| B-U210 | save.md | 24 | ПРИЧИНА | gdocs-append кладёт в конец файла = Зона Б = невидимо на старте. | Reason: append goes to file end = Zone B = invisible at startup |
| B-U211 | save.md | 25 | ПРАВИЛО | Закрытие задачи, стоящей в Зоне А, — тем же вызовом перенести строку в АРХИВ ЗАДАЧ. | Docs: closing a Zone A task moves the line to ARCHIVE in same call |
| B-U212 | save.md | 25 | ПРАВИЛО | Закрытие фазы или решение уровня СЛЕДУЮЩЕГО ШАГА — тем же вызовом обновить строку СЛЕДУЮЩИЙ ШАГ Зоны А. | Docs: phase close/next-step decision updates NEXT STEP line in same call |
| B-U213 | save.md | 26 | ПРАВИЛО | Обновить LAST_UPDATED отдельным вызовом: инструменты записи шапку не трогают. | Docs: update LAST_UPDATED in a separate call |
| B-U214 | save.md | 26 | ПРИЧИНА | инструменты записи шапку не трогают | Reason: write tools don't touch the header |
| B-U215 | save.md | 29 | ПРАВИЛО | Перед записью любой строки о состоянии («работает», «выключен», «внесено», «удалено») — у неё есть способ проверки: номер исполнения, поле, строка объекта | Any state line needs a verification method (execution number, field, object row) |
| B-U216 | save.md | 29 | ПРАВИЛО | нет — строка пишется как «Гипотеза (не проверена):». | No method: write the line as "Hypothesis (not verified):" |
| B-U217 | save.md | 29 | ПРАВИЛО | Задача, которую Андрей назвал сделанной, закрывается только если объект прочитан в этой сессии | Task Andrei called done is closed only if object read this session |
| B-U218 | save.md | 29 | ПРАВИЛО | иначе она остаётся открытой с пометкой «по словам Андрея, объект не прочитан» | Otherwise stays open marked "per Andrei's words, object not read" |
| B-U219 | save.md | 29 | АДРЕС | Правило и основание — Р15. | Rule and basis: R15 |
| B-U220 | save.md | 30 | ПРАВИЛО | Документ или таблица Google, созданные в этой сессии и ещё не внесённые в `registry/documents.md`, — внести сейчас (правило — Р6). | Session-created Google doc/table not yet in registry/documents.md: register now |
| B-U221 | save.md | 30 | ИСКЛЮЧЕНИЕ | Опоздание до !save уже нарушение, но запись всё равно делается. | Being late until !save is already a violation, but write anyway |
| B-U222 | save.md | 31 | ПРАВИЛО | Перед записью решения в журнал проекта — поиск по оглавлению журнала того же проекта двумя-тремя словами темы | Before writing a decision to log, search log TOC with 2-3 topic words |
| B-U223 | save.md | 31 | АДРЕС | (`second-brain-git` 7.6, строка «оглавление журнала») | Address: second-brain-git 7.6 log TOC row |
| B-U224 | save.md | 31 | ПРАВИЛО | Нашлась запись на ту же тему — новая запись называет её в поле «почему»: «заменяет Р-N» | If same-topic entry found, new entry names it in "why": "replaces R-N" |
| B-U225 | save.md | 31 | ПРАВИЛО | (тогда статус прежней меняется по `second-brain-git` 11.1) | Replaces: status of old entry changes per 11.1 |
| B-U226 | save.md | 31 | ПРАВИЛО | либо «противоречит Р-N — вопрос Андрею» (тогда запись не пишется до ответа) | Or "contradicts R-N — question to Andrei"; entry not written until answered |
| B-U227 | save.md | 31 | ПРАВИЛО | Ничего не нашлось — в отчёте о save одна строка «пересечений с журналом нет». | Nothing found: one report line "no overlaps with log" |
| B-U228 | save.md | 31 | СЛУЧАЙ | запись Р-3 журнала `projects/archivarius/LOG.md`: вопросы, уже решённые раньше, задавались повторно | Case/basis: archivarius log R-3, previously settled questions re-asked |
| B-U229 | save.md | 31 | СЛУЧАЙ | (Р-104 и Р-107 журнала `projects/git-migration/LOG.md`) | Case: git-migration log R-104 and R-107 |
| B-U230 | save.md | 32 | ПРАВИЛО | Ответ сессии, стоивший исследования ... подшивается в репозиторий только вместе с названным читателем — задачей или проектом | Research-costly answer filed to repo only with a named reader (task or project) |
| B-U231 | save.md | 32 | ПРАВИЛО | внешнее исследование — заметкой `wiki/notes/RES-NNN.md` по `wiki/DESIGN.md`, со ссылкой на заметку из задачи или журнала читателя | External research as wiki/notes/RES-NNN.md per DESIGN.md, linked from reader task/log |
| B-U232 | save.md | 32 | ПРАВИЛО | Читателя нет — ответ остаётся в чате, и это не потеря | No reader: answer stays in chat, not a loss |
| B-U233 | save.md | 32 | ПРИЧИНА | корпус без читателя запрещён формулой Главной задачи (`labs/sys/t-knowledge-loop.md`) | Reason: corpus without reader forbidden by Main Task formula |
| B-U234 | save.md | 32 | СЛУЧАЙ | Основание — запись Р-3 журнала `projects/archivarius/LOG.md`. | Basis: archivarius log R-3 |
| B-U235 | save.md | 33 | ПРАВИЛО | После правки воркфлоу n8n в этой сессии — ADR в паспорт воркфлоу (Skill `n8n-workflow-passport`). | After n8n workflow edit this session, ADR into passport |
| B-U236 | save.md | 34 | ПРАВИЛО | Оценить CHANGELOG: было ли ЗАПУЩЕНО / СОЗДАНО / ЗАКРЫТО что-то, что теперь работает и используется | Assess CHANGELOG: was something launched/created/closed that now works and is used |
| B-U237 | save.md | 34 | ИСКЛЮЧЕНИЕ | отдельные задачи и баги не в счёт | Separate tasks and bugs don't count |
| B-U238 | save.md | 34 | ПРАВИЛО | Если да — прочитать `core/R-13.md` (строка «запись в CHANGELOG» таблицы «По событию» манифеста) | If yes, read core/R-13.md (by-event row) |
| B-U239 | save.md | 34 | ПРАВИЛО | дописать через gdocs-append в Google Doc CHANGELOG (ID — `registry/documents.md`, строка CHANGELOG) по форме | Append via gdocs-append to CHANGELOG doc per form |
| B-U240 | save.md | 36 | ПОРОГ | ДАТА ¦ СТАТУС ¦ ПРОЕКТ ¦ Что достигнуто | CHANGELOG entry first line format |
| B-U241 | save.md | 37 | ПОРОГ | Что изменилось: <в чём польза, что стало лучше> | CHANGELOG entry second line field |
| B-U242 | save.md | 38 | ПОРОГ | Темп: <быстро / нормально / медленно + почему> | CHANGELOG entry tempo field |
| B-U243 | save.md | 40 | ПОРОГ | СТАТУС только из словаря ЗАПУЩЕНО / СОЗДАНО / ЗАКРЫТО (один; «СОЗДАНО+ЗАПУЩЕНО» = ЗАПУЩЕНО) | STATUS only from vocabulary, one; combined = ЗАПУЩЕНО |
| B-U244 | save.md | 40 | ПОРОГ | ПРОЕКТ только из списка весов `registry/projects.md`, значения «A + B» запрещены, изолированные контуры с пометкой off-CORE | PROJECT only from weights list, "A + B" forbidden, isolated circuits marked off-CORE |
| B-U245 | save.md | 40 | ПРАВИЛО | Значение вне словаря приводится к ближайшему, и это говорится вслух. | Out-of-vocabulary value mapped to nearest, said aloud |
| B-U246 | save.md | 40 | ПРАВИЛО | Андрей ничего дополнительного не пишет. | Andrei writes nothing extra |
| B-U247 | save.md | 41 | ПРАВИЛО | Если сущность именованная и переиспользуемая (PROTOCOL_*, §-пункт Skill, воркфлоу n8n многократного применения) — строка в РЕЕСТР ПРОТОКОЛОВ | Named reusable entity gets a row in protocol registry |
| B-U248 | save.md | 41 | АДРЕС | отдельный документ SYS_PROTOCOL_REGISTRY, ID в `registry/documents.md` (не SYS_INDEX: тот заморожен 2026-09-23) | Registry is separate doc SYS_PROTOCOL_REGISTRY; not frozen SYS_INDEX |
| B-U249 | save.md | 41 | ПОРОГ | протокол ¦ дата рождения ¦ применений ¦ последнее применение ¦ статус 🟢 доказан / 🟡 внедрён / 🔴 не используется | Protocol-registry row columns and status vocabulary |
| B-U250 | save.md | 42 | ПРАВИЛО | Если сессия вскрыла факт, требующий правки CORE / задачи `labs/sys/` / Skill / мастер-промпта — Р16. | Fact requiring edit of CORE/task/Skill/prompt: go to R16 |
| B-U251 | save.md | 43 | ПРОВЕРКА | Каждая запись — независимым обратным чтением: repo — `second-brain-git` 8.1 (blob sha записанного равен намеренному) | Check: each write by independent read-back; repo blob sha equals intended |
| B-U252 | save.md | 43 | ПРОВЕРКА | Docs — gdocs-read, якорь найден ровно один раз, содержимое совпадает. | Check Docs: anchor found exactly once, content matches |
| B-U253 | save.md | 43 | ПРОВЕРКА | В отчёте названы файл, способ обратного чтения и совпавшая величина (Р15). | Check: report names file, read-back method, matched value |
| B-U254 | save.md | 43 | ПРОВЕРКА | `success: true` и exec-ID проверкой не являются. | success:true and exec-ID are not verification |
| B-U255 | save.md | 47 | ПРАВИЛО | Правило A — аккумуляторы вне hot-path: ИДЕИ, ВОПРОСЫ, объёмный каталог ИНСТРУМЕНТЫ живут в Зоне Б, в Зоне А — указатели. | Rule A: accumulators in Zone B, pointers in Zone A |
| B-U256 | save.md | 48 | АДРЕС | Правило B — маршрутизация захвата: см. Р7 п.4. | Rule B: capture routing see R7 item 4 |
| B-U257 | save.md | 49 | ПРАВИЛО | Правило Навигации — поведенческие правила, специфичные для проекта, вносятся в Зону А INDEX как проектный контент, не в замороженный промпт. | Navigation rule: project-specific behavior rules go to Zone A, not frozen prompt |
| B-U258 | save.md | 50 | ПРАВИЛО | Правило второго раза — рецидив бага/паттерна в одном проекте: записать КЛАСС в НАКОПЛЕННЫЙ ОПЫТ → Ошибки и решения | Second-time rule: on recurrence record the CLASS in accumulated experience |
| B-U259 | save.md | 50 | ПОРОГ | симптом + причина класса + превентив + момент-триггер | Class entry fields: symptom, class cause, preventive, trigger moment |
| B-U260 | save.md | 51 | АДРЕС | Карта воркфлоу проекта — снимок `registry/n8n-map.md` (состав, расписания, связи между воркфлоу), паспорта — `n8n-workflow-passport`. | Workflow map = n8n-map snapshot; passports in n8n-workflow-passport |
| B-U261 | save.md | 51 | ПРАВИЛО | Отдельная карта SYSTEM-MAP по протоколу PROTOCOL_system-map больше не ведётся и не читается как действующая | SYSTEM-MAP no longer maintained nor read as current |
| B-U262 | save.md | 51 | СЛУЧАЙ | её заменил снимок (`projects/n8n/STATE.md`, строка долга Н-26.08-02, сверено 2026-10-06) | Case: replaced by snapshot, debt row N-26.08-02, checked 2026-10-06 |
| B-U263 | save.md | 51 | АДРЕС | Прежние карты и сам протокол (ID — `registry/protocols.md`) — исторические источники. | Old maps and protocol are historical sources; ID in registry/protocols.md |
| B-U264 | harvest.md | 3 | ПРАВИЛО | слово «харвест» в проекте SYS | Read file when "харвест" appears in SYS project |
| B-U265 | harvest.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md; ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md. | Numbers shared; cross-refs via table |
| B-U266 | harvest.md | 5 | СЛУЧАЙ | Правка 2026-10-09 (харвест 2026-10-08). Процедура дополнена 2026-10-08 (чтение repo-проектов, лабораторий, файлов STATE.md, PLAN.md и meta/, сверка с живыми Skills, форма большого пакета). | History: 2026-10-09 edit, procedure extended 2026-10-08 |
| B-U267 | harvest.md | 5 | СЛУЧАЙ | проверка Р11 пересказывала условие сдвига даты своими словами и мягче, чем шаги 5 и 6 процедуры («выданы правки» вместо «ответ на каждую находку») — заменена ссылкой на шаги | Case: R11 check paraphrased date-shift condition softer than steps 5-6; replaced by reference |
| B-U268 | harvest.md | 5 | ПРИЧИНА | перечень частей процедуры — тот же пересказ, который устаревает при каждой её правке | Reason: list of procedure parts is a retelling that goes stale on each edit |
| B-U269 | harvest.md | 9 | ПРАВИЛО | Слово «харвест» в проекте SYS. | R11 trigger: word харвест in SYS |
| B-U270 | harvest.md | 9 | ИСКЛЮЧЕНИЕ | В проекте, не являющемся SYS, сессия отвечает, что команда запускается в SYS, и не исполняет её | Outside SYS: answer it runs in SYS, don't execute |
| B-U271 | harvest.md | 9 | АДРЕС | `meta/PROTOCOL_harvest.md`, раздел «Кто читает и когда»: «Других запусков нет» | Basis: PROTOCOL_harvest "who reads and when": no other launches |
| B-U272 | harvest.md | 9 | ПРАВИЛО | Слово «обслуживание» цикла не открывает | The word "обслуживание" does not open the cycle |
| B-U273 | harvest.md | 9 | СЛУЧАЙ | цикл обслуживания CORE Раздела 12 снят решением владельца 2026-09-07 (Р-89, Р-90 и Р-91 журнала `projects/git-migration/LOG.md`) | Maintenance cycle of CORE Section 12 removed 2026-09-07, entries R-89..91 |
| B-U274 | harvest.md | 9 | ПРАВИЛО | На это слово сессия отвечает, что цикла больше нет, и называет команду «харвест». | On that word reply that cycle is gone and name command харвест |
| B-U275 | harvest.md | 10 | ПРАВИЛО | Процедура живёт в `meta/PROTOCOL_harvest.md` репозитория `second-brain-canon` — и нигде больше. | Procedure lives only in meta/PROTOCOL_harvest.md |
| B-U276 | harvest.md | 10 | ПРАВИЛО | Прочитать файл целиком одним чтением по `second-brain-git` 7.6 (в среде с клоном — `cat`, без клона — Git Read с сужением ответа) и исполнить его шаги по порядку. | Read file in one full read and execute steps in order |
| B-U277 | harvest.md | 10 | ПРАВИЛО | Что процедура читает и в каком порядке — только в ней; этот Skill отвечает за то, когда её запускать и с чьего согласия вносить найденное. | What procedure reads is only in it; Skill owns when to run and whose consent for changes |
| B-U278 | harvest.md | 10 | АДРЕС | Посредников для больших объёмов процедура раздаёт по Р21. | Procedure assigns intermediaries for large volumes per R21 |
| B-U279 | harvest.md | 10 | СЛУЧАЙ | Механизм меток `[verified: дата]` с перепроверкой правил старше 90 суток (прежний пункт Р17) снят решением владельца 2026-09-27 | Verified-label mechanism with 90-day recheck removed 2026-09-27 |
| B-U280 | harvest.md | 10 | ПОРОГ | правил старше 90 суток | Threshold of removed mechanism: rules older than 90 days |
| B-U281 | harvest.md | 10 | ПРИЧИНА | меток в Skills не было, счёт всегда давал ноль (Р-113 журнала `projects/git-migration/LOG.md`) | Reason: no labels existed, count always zero; entry R-113 |
| B-U282 | harvest.md | 10 | ПРАВИЛО | Шаги в этом Skill не пересказываются: пересказ стал бы вторым носителем процедуры. | Steps not retold in Skill: retelling would be a second carrier |
| B-U283 | harvest.md | 11 | ПРАВИЛО | Разовая работа, вскрытая харвестом, — задача в `labs/sys/` по §4б `second-brain-git`. | One-off work found by harvest becomes a labs/sys task per 4б |
| B-U284 | harvest.md | 11 | ПРАВИЛО | Повторяющаяся — не добавляется в процедуру молча, а предлагается владельцу правкой `meta/PROTOCOL_harvest.md` текстом «было → стало». | Recurring work not silently added to procedure; proposed to owner as before→after edit |
| B-U285 | harvest.md | 12 | АДРЕС | Харвест не сканирует внешние чаты и не знает о незарегистрированных обязательствах — Р16. | Harvest doesn't scan external chats; see R16 |
| B-U286 | harvest.md | 13 | ПРОВЕРКА | Строка «последний харвест» файла `meta/PROTOCOL_harvest.md` сдвинута по условию шагов 5 и 6 самой процедуры | Check: "last harvest" line shifted per steps 5 and 6 of procedure |
| B-U287 | harvest.md | 13 | ПРОВЕРКА | сдвиг подтверждён обратным чтением по blob sha (Р15) | Check: shift confirmed by blob-sha read-back |
| B-U288 | onboarding.md | 3 | ПРАВИЛО | «Создай проект», «заведи INDEX», новый Claude Project; перед выдачей любого мастер-промпта или его блока Второго мозга Андрею | Read file when creating project/INDEX/new Project and before giving any master prompt/block |
| B-U289 | onboarding.md | 3 | АДРЕС | Номера пунктов — прежние, общие со SKILL.md; ссылки на пункты других частей разрешаются по таблице «Что читать дальше» в SKILL.md. | Numbers shared; cross-refs via table |
| B-U290 | onboarding.md | 7 | ПРАВИЛО | Регламент Второго мозга живёт в этом Skill, а не в мастер-промптах. | Regulation lives in the Skill, not in master prompts |
| B-U291 | onboarding.md | 7 | ПРАВИЛО | Мастер-промпт несёт только четыре вещи: адрес проекта, триггер старта, слова, которые обязаны вызвать этот Skill, и особенности проекта. | Master prompt carries only four things |
| B-U292 | onboarding.md | 7 | СЛУЧАЙ | к 2026-10-06 регламент стоял в шести местах — пять мастер-промптов и этот Skill — и копии разошлись | Case: by 2026-10-06 regulation in six places, copies diverged |
| B-U293 | onboarding.md | 7 | СЛУЧАЙ | четыре формата строки старта, `!map` в одних промптах и снятая в других, адрес CHANGELOG то в промпте, то в реестре, Skill отправлял баг n8n в замороженный документ | Case: concrete divergences (4 start formats, !map, CHANGELOG address, bug to frozen doc) |
| B-U294 | onboarding.md | 7 | ПРИЧИНА | Одно место — одна правка на все проекты. | Reason: one place = one edit for all projects |
| B-U295 | onboarding.md | 9 | ПРАВИЛО | Блок меняется только отдельным действием после явного «да» Андрея в чате, текстом «было → стало» (Р13). | Block changes only as separate action after explicit yes, with before→after text |
| B-U296 | onboarding.md | 9 | ПРАВИЛО | В блок не вписываются правила, которые уже есть в Skill: дубль — дефект (Р3). | Don't put rules already in Skill into the block: duplicate is a defect |
| B-U297 | onboarding.md | 11 | АДРЕС | Р2а. Агентская копия мастер-промпта (английская) — блок ставится последним в промпте | R2a English agent copy of block, placed last in prompt |
| B-U298 | onboarding.md | 14 | ПОРОГ | <second_brain> ... Second Brain project: <ТЕГ>. Canon: <projects/<папка>/ ¦ labs/<папка>/> | Agent block: tag and canon line |
| B-U299 | onboarding.md | 16 | ПОРОГ | The Second Brain regulation lives in Skill second-brain-engineer, not in this prompt. | Agent block: regulation lives in Skill |
| B-U300 | onboarding.md | 17 | ПОРОГ | at session start, before replying to the first message — section Р1 (start) | Agent block trigger 1: start R1 |
| B-U301 | onboarding.md | 18 | ПОРОГ | when a message starts with !save, !tasks, !priority, !inbox, !review, !status, !digest, !map or «харвест» | Agent block trigger 2: nine command words R8 |
| B-U302 | onboarding.md | 19 | ПОРОГ | when the conversation produces a new task, idea, question, decision, bug, result or external event — section Р6 | Agent block trigger 3: capture R6 |
| B-U303 | onboarding.md | 20 | ПОРОГ | before any change to an n8n workflow — section Р10. | Agent block trigger 4: workflow change R10 |
| B-U304 | onboarding.md | 21 | ПОРОГ | Repo reads and writes — Skill second-brain-git. Never run these steps from memory of an earlier session. | Agent block: git Skill; don't run from memory |
| B-U305 | onboarding.md | 22 | ПОРОГ | Project specifics (override the Skill for this project only): <список или «none»> | Agent block: project specifics line |
| B-U306 | onboarding.md | 26 | АДРЕС | Р2б. Человеческая копия (русская) — тот же блок по смыслу | R2b Russian human copy, same block in meaning |
| B-U307 | onboarding.md | 29 | ПОРОГ | ## Второй мозг / Проект Второго мозга: <ТЕГ>. Канон: ... | Human block: heading, tag, canon line |
| B-U308 | onboarding.md | 31 | ПОРОГ | Регламент Второго мозга живёт в Skill second-brain-engineer, а не в этом промпте. Загрузи этот Skill и действуй по нему: | Human block: regulation in Skill |
| B-U309 | onboarding.md | 32 | ПОРОГ | на старте сессии, до ответа на первое сообщение, — раздел Р1 (старт); | Human block trigger 1 |
| B-U310 | onboarding.md | 33 | ПОРОГ | когда сообщение начинается с !save, !tasks, !priority, !inbox, !review, !status, !digest, !map или «харвест» | Human block trigger 2 |
| B-U311 | onboarding.md | 34 | ПОРОГ | когда в разговоре появляется новая задача, идея, вопрос, решение, баг, результат или внешнее событие, — раздел Р6 (захват); | Human block trigger 3 |
| B-U312 | onboarding.md | 35 | ПОРОГ | перед любым изменением воркфлоу n8n — раздел Р10. | Human block trigger 4 |
| B-U313 | onboarding.md | 36 | ПОРОГ | Чтение и запись репозитория — Skill second-brain-git. Не исполняй эти шаги по памяти прошлых сессий. | Human block: git Skill; not from memory |
| B-U314 | onboarding.md | 37 | ПОРОГ | Особенности проекта (меняют правила Skill только для этого проекта): <список или «нет»> | Human block: project specifics line |
| B-U315 | onboarding.md | 40 | ПРАВИЛО | Docs-проект (изолированный контур, Р4 п.0) получает тот же блок; в строке канона вместо папки — «Google Doc <ИМЯ>_INDEX, ID — registry/documents.md». | Docs project gets same block; canon line names Google Doc and ID location |
| B-U316 | onboarding.md | 42 | ПРАВИЛО | Ссылки на общие документы системы (USER_PROFILE, INBOX, CHANGELOG) в блок и в промпт не вписываются | Links to shared system docs not written into block or prompt |
| B-U317 | onboarding.md | 42 | ПРИЧИНА | их ID живут в `registry/documents.md` и берутся оттуда в момент использования. | Reason: IDs live in registry/documents.md, taken at time of use |
| B-U318 | onboarding.md | 44 | ПРАВИЛО | Особенность проекта — правило, которого нет в Skill или которое для этого проекта отличается: своя строка старта, своё значение команды, свой маршрут находки, своё правило записи. | Definition of project specific: rule absent from Skill or differing for the project |
| B-U319 | onboarding.md | 44 | ИСКЛЮЧЕНИЕ | Тон, роль, предмет и правила домена проекта — не особенности блока, а остальная часть мастер-промпта. | Tone, role, subject and domain rules are not block specifics but rest of prompt |
| B-U320 | onboarding.md | 50 | ПРАВИЛО | Перед выдачей любого мастер-промпта или его блока Второго мозга Андрею. | R3 trigger: before handing any master prompt/block to Andrei |
| B-U321 | onboarding.md | 51 | ПРАВИЛО | Прогнать все пункты. Один не выполнен — промпт не выдавать. | Run all checklist items; any failed means don't hand over |
| B-U322 | onboarding.md | 52 | ПРОВЕРКА | Тег — как в весах `registry/projects.md`; носитель и папка совпадают со строкой проекта в реестре. | Checklist: tag, carrier, folder match registry |
| B-U323 | onboarding.md | 53 | ПРОВЕРКА | Блок называет Skill second-brain-engineer и четыре триггера: старт (Р1), слова-команды (Р8, все девять слов), захват (Р6), изменение воркфлоу (Р10). | Checklist: block names Skill and four triggers incl. all nine words |
| B-U324 | onboarding.md | 54 | ПРОВЕРКА | Регламент Второго мозга в промпте не пересказан: нет формата строки старта, маршрута !save, таблицы команд, формата захвата, порядка записи. | Checklist: regulation not retold in prompt |
| B-U325 | onboarding.md | 54 | ПРИЧИНА | Пересказ — дефект: копия разойдётся со Skill. | Reason: a retelling copy will diverge from Skill |
| B-U326 | onboarding.md | 55 | ПРОВЕРКА | Особенности проекта — только то, чего в Skill нет или что для проекта отличается; каждая особенность — одна строка с причиной. | Checklist: specifics only non-Skill/differing, one line each with reason |
| B-U327 | onboarding.md | 56 | ПРОВЕРКА | Docs-ID CORE и ID замороженных документов как источников состояния в промпте отсутствуют. | Checklist: no CORE Docs ID or frozen-doc IDs in prompt |
| B-U328 | onboarding.md | 57 | ПРОВЕРКА | Тон и роль — в проектной части промпта: неформально, на «ты», с иронией. | Checklist: tone/role in project part: informal, "ты", ironic |
| B-U329 | onboarding.md | 58 | ПРОВЕРКА | Чеклист показан Андрею вместе с промптом, каждый пункт отмечен. | Check: checklist shown to Andrei with prompt, each item marked |
| B-U330 | onboarding.md | 64 | ПРАВИЛО | «Создай проект», «заведи INDEX», новый Claude Project. | R4 trigger |
| B-U331 | onboarding.md | 66 | ПРАВИЛО | Выбрать носитель `[НОВОЕ 2026-09-07]`: по умолчанию — repo (`second-brain-git`, раздел «Новый проект»). | Step 0: choose carrier, default repo |
| B-U332 | onboarding.md | 66 | ИСКЛЮЧЕНИЕ | Docs-INDEX заводится только для изолированного контура, который по PLAN_git-migration в repo не мигрирует (Tutor, DOSSIER, Justus и аналоги), или по прямому слову Андрея. | Docs-INDEX only for isolated circuits not migrating (Tutor, DOSSIER, Justus) or on Andrei's direct word |
| B-U333 | onboarding.md | 66 | ПРАВИЛО | Выбор назвать вслух до создания чего-либо. | Name carrier choice aloud before creating anything |
| B-U334 | onboarding.md | 66 | СЛУЧАЙ | [НОВОЕ 2026-09-07] | Marker: step 0 added 2026-09-07 |
| B-U335 | onboarding.md | 67 | ПОРОГ | Имя: repo — нижний регистр через дефис (`wb-logistics`); Docs — ДОМЕН_ТИП (`WB_LOGISTICS`). | Naming: repo lowercase hyphenated, Docs DOMAIN_TYPE |
| B-U336 | onboarding.md | 67 | ПРАВИЛО | Вес — из `registry/projects.md`, секция «Проекты с INDEX в Google Docs» (прежний CORE Р.1). | Weight from registry/projects.md Docs section |
| B-U337 | onboarding.md | 68 | ПРАВИЛО | repo: дальше по `second-brain-git` «Новый проект», затем п.6–7 здесь. | Repo: follow second-brain-git "New project", then items 6-7 |
| B-U338 | onboarding.md | 69 | ПРАВИЛО | Docs: создать INDEX в INDEX_FOLDER (`1UV-7hP0L2jiwPAtulPZ1gket-mdz0ktT`) по шаблону Р5 | Docs: create INDEX in INDEX_FOLDER per R5 template |
| B-U339 | onboarding.md | 69 | ПОРОГ | `1UV-7hP0L2jiwPAtulPZ1gket-mdz0ktT` | INDEX_FOLDER ID |
| B-U340 | onboarding.md | 69 | ПРОВЕРКА | верифицировать {id, title, mimeType} и обратным чтением через gdocs-read | Verify {id,title,mimeType} and by gdocs-read read-back |
| B-U341 | onboarding.md | 70 | ПРАВИЛО | Docs: зарегистрировать проект в registry/projects.md (секция «Проекты с INDEX в Google Docs» — вес и карточка) и идентификатор его INDEX в registry/documents.md по контракту записи second-brain-git. | Docs: register project and INDEX ID per write contract |
| B-U342 | onboarding.md | 70 | ПРАВИЛО | Перед записью прочитать секцию проектов в registry/projects.md целиком — проект может быть зарегистрирован под другим именем | Before writing read projects section in full; project may be under another name |
| B-U343 | onboarding.md | 70 | ПРОВЕРКА | поиск подстроки отсутствие не доказывает. | Substring search doesn't prove absence |
| B-U344 | onboarding.md | 71 | ПРАВИЛО | Docs: убедиться, что Зона А заканчивается строкой SENTINEL и разделителем ЗОНА Б по шаблону Р5 | Docs: ensure Zone A ends with SENTINEL and ZONE B divider |
| B-U345 | onboarding.md | 71 | ПРИЧИНА | без них старт Р1 не может доказать, что Зона А прочитана до конца | Reason: without them R1 can't prove Zone A read fully |
| B-U346 | onboarding.md | 72 | ПРАВИЛО | Подготовить мастер-промпт по методу Р22 (references/prompt-craft.md) с блоком Второго мозга (Р2), прогнать Р3, выдать Андрею. | Prepare master prompt per R22 with block, run R3, hand to Andrei |
| B-U347 | onboarding.md | 72 | ПРАВИЛО | Андрей создаёт Claude Project сам и присылает URL. | Andrei creates the Claude Project himself and sends URL |
| B-U348 | onboarding.md | 73 | ПРАВИЛО | URL Claude Project — в карточку проекта в registry/projects.md по контракту записи repo. | Project URL goes into registry card via repo write contract |
| B-U349 | onboarding.md | 74 | ПРОВЕРКА | Каждый шаг закрыт независимым чтением (Docs: gdocs-read; repo: git-read с blob sha) до начала следующего. | Check: each step closed by independent read before next |
| B-U350 | onboarding.md | 74 | ПРОВЕРКА | Ответ инструмента проверкой не является. | Tool response is not verification |
| B-U351 | onboarding.md | 80 | ПОРОГ | [ИМЯ_ПРОЕКТА]_INDEX / LAST_UPDATED: YYYY-MM-DD / LAST_READ_BY_CLAUDE: — / ПРОЕКТ / СТАТУС / ВЕС | INDEX template header fields |
| B-U352 | onboarding.md | 86 | ПОРОГ | СТАТУС: [Активен / Заморожен / Не начат] | Template status vocabulary |
| B-U353 | onboarding.md | 90 | ПОРОГ | ЗОНА А — читается при каждом старте сессии | Template Zone A heading |
| B-U354 | onboarding.md | 92 | ПОРОГ | ЦЕЛЬ / СЛЕДУЮЩИЙ ШАГ / СВЯЗИ / ИНСТРУМЕНТЫ / ОТКРЫТЫЕ ЗАДАЧИ / ИДЕИ / ВОПРОСЫ БЕЗ ОТВЕТА | Template Zone A section list |
| B-U355 | onboarding.md | 94 | ПОРОГ | СВЯЗИ            Формат: [ПРОЕКТ] → [что зависит / что предоставляет] | Template links format |
| B-U356 | onboarding.md | 95 | ПРАВИЛО | ИНСТРУМЕНТЫ      только актуальные; объёмный каталог — в Зоне Б | Template: tools only current, big catalog in Zone B |
| B-U357 | onboarding.md | 96 | ПОРОГ | ОТКРЫТЫЕ ЗАДАЧИ  [ ] БЛОКЕР / РЫЧАГ / РУТИНА / ЗОМБИ: ... | Template open-task label format |
| B-U358 | onboarding.md | 97 | ПРАВИЛО | ИДЕИ             → указатель «полный список — Зона Б» | Template: ideas as pointer to Zone B |
| B-U359 | onboarding.md | 98 | ПРАВИЛО | ВОПРОСЫ БЕЗ ОТВЕТА → указатель «полный список — Зона Б» | Template: open questions as pointer to Zone B |
| B-U360 | onboarding.md | 100 | ПОРОГ | --- SENTINEL ЗОНА А ¦ [ИМЯ_ПРОЕКТА] ¦ YYYY-MM-DD ¦ [6 случайных знаков] --- | Template SENTINEL line format |
| B-U361 | onboarding.md | 101 | ПОРОГ | ЗОНА Б — читается только по запросу или при !review | Template Zone B heading and read rule |
| B-U362 | onboarding.md | 103 | ПОРОГ | РЕШЕНИЯ (лог)         [дата] [решение] — [контекст] | Template Zone B decisions format |
| B-U363 | onboarding.md | 104 | ПОРОГ | ПРОГРЕСС              [дата] [что сделано] → [результат] | Template progress format |
| B-U364 | onboarding.md | 105 | ПОРОГ | БАГИ / ИНЦИДЕНТЫ      [дата] [проблема] → [решение] | Template bugs format |
| B-U365 | onboarding.md | 106 | ПОРОГ | АРХИВ ЗАДАЧ           [дата] [задача] → [результат]; при закрытии [ ]→[x] переносить сюда с датой | Template archive format; closed tasks move here with date |
| B-U366 | onboarding.md | 107 | ПОРОГ | ИДЕИ (полный список) / ВОПРОСЫ БЕЗ ОТВЕТА (полный список) | Template Zone B full lists |
| B-U367 | onboarding.md | 110 | ПОРОГ | НАКОПЛЕННЫЙ ОПЫТ | Template accumulated-experience section |
| B-U368 | onboarding.md | 112 | ПОРОГ | Инструменты и паттерны   [YYYY-MM-DD] [инструмент/паттерн] — описание | Template tools-patterns format |
| B-U369 | onboarding.md | 113 | ПОРОГ | Ошибки и решения         [YYYY-MM-DD] [симптом] → [решение] | Template errors format |
| B-U370 | onboarding.md | 114 | ПРАВИЛО | Устаревшее (кандидаты на удаление)  удаляется только после подтверждения Андрея | Template: obsolete items deleted only after Andrei confirms |
| B-U371 | onboarding.md | 116 | ПРАВИЛО | Поля ENTRIES_COUNT нет — не искать; в старых INDEX оно ещё стоит и ничего не значит. | No ENTRIES_COUNT field; don't look; old INDEX still carry it, meaningless |
| B-U372 | onboarding.md | 116 | ПРАВИЛО | ЗОМБИ — метка статуса задачи в Зоне А, отдельного блока нет. | ЗОМБИ is a task status label, no separate block |
| B-U373 | onboarding.md | 116 | ПРАВИЛО | Строка SENTINEL — последняя строка Зоны А, прямо перед заголовком «ЗОНА Б» | SENTINEL is last line of Zone A just before ZONE B heading |
| B-U374 | onboarding.md | 116 | ПРОВЕРКА | по ней Р1 доказывает, что срез Зоны А дочитан до конца. | R1 uses SENTINEL to prove Zone A slice read to the end |
| B-U375 | onboarding.md | 116 | ПРИЧИНА | Шесть случайных знаков делают строку уникальной в документе. | Reason: six random chars make the line unique |
| B-U376 | onboarding.md | 116 | СЛУЧАЙ | Форма снята с живого INDEX (TRADING_INDEX, строка «--- SENTINEL ЗОНА А ¦ TRADING ¦ 2026-07-24 ¦ uhhju6 ---») | Case: form taken from live TRADING_INDEX |
| B-U377 | onboarding.md | 116 | ПРАВИЛО | INDEX без этой строки проверку Р1 не проходит. | INDEX without SENTINEL fails R1 check |

Total units: 377

Per class:
- ПРАВИЛО: 180
- АДРЕС: 47
- СЛУЧАЙ: 29
- ИСКЛЮЧЕНИЕ: 15
- ПОРОГ: 55
- ПРИЧИНА: 19
- ПРОВЕРКА: 32

Per file:
- start.md: 46
- commands.md: 36
- search.md: 17
- permissions.md: 53
- outside.md: 29
- save.md: 82
- harvest.md: 24
- onboarding.md: 90
