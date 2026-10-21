# n8n-workflow-passport old text decomposition

| id | lines | class | quote | paraphrase |
|---|---|---|---|---|
| P001 | 2 | THRESHOLD | name: "n8n-workflow-passport" | Skill name is n8n-workflow-passport |
| P002 | 3 | THRESHOLD | Паспорт воркфлоу n8n — документ Google Docs | Passport = a Google Docs document per n8n workflow |
| P003 | 3 | THRESHOLD | отвечающий на вопрос «как устроено, с чем связано и почему именно так» | Passport answers: how it is built, what it is linked to, why this way |
| P004 | 3 | RULE | Этот Skill описывает весь жизненный цикл паспорта | Skill covers the whole passport lifecycle |
| P005 | 3 | RULE | как его найти перед работой с воркфлоу, как читать по зонам, как создать | Lifecycle: find before work, read by zones, create |
| P006 | 3 | RULE | как дозаписать ADR после правки, когда фаза работы ... считается закрытой | Lifecycle: append ADR after edit, phase-closed condition |
| P007 | 3 | RULE | что делать с паспортом, когда воркфлоу больше не нужен | Lifecycle: what to do with passport when workflow no longer needed |
| P008 | 3 | RULE | ОБЯЗАТЕЛЬНО читать при задачах: создать паспорт, обновить документацию | MUST read Skill for tasks: create passport, update docs after workflow change |
| P009 | 3 | RULE | найти паспорт существующего воркфлоу, завести папку DOCS проекта | MUST read for: find existing passport, create project DOCS folder |
| P010 | 3 | RULE | Также читать при исполнении протокола изменения воркфлоу | Also read when executing the workflow-change protocol |
| P011 | 3 | ADDRESS | протокола изменения воркфлоу из n8n-engineering-manual | The change protocol lives in n8n-engineering-manual |
| P012 | 3 | ADDRESS | шаблон паспорта и контракт создания здесь | Passport template and creation contract live in this Skill |
| P013 | 3 | THRESHOLD | Триггеры: «создай паспорт», «обнови документацию», «где паспорт воркфлоу», «задокументируй воркфлоу» | Trigger phrases for the Skill (four phrases) |
| P014 | 3 | THRESHOLD | любое завершённое изменение воркфлоу, требующее ADR-блока | Trigger: any completed workflow change requiring an ADR block |
| P015 | 6 | THRESHOLD | # Паспорт воркфлоу — жизненный цикл документа | Title heading: passport lifecycle |
| P016 | 8 | CASE | Редакция 2026-09-26. | Edition dated 2026-09-26 |
| P017 | 8 | CASE | адрес живого состава воркфлоу переведён с Google Doc N8N_REGISTRY на файл registry/n8n-map.md | 09-26 change: live workflow roster address moved from Google Doc N8N_REGISTRY to registry/n8n-map.md |
| P018 | 8 | CASE | снят раздел «Приоритет создания» — все три названных в нём воркфлоу паспорта уже имеют | 09-26: removed "Priority of creation" section because all three named workflows already have passports |
| P019 | 8 | CASE | маршрут поиска паспорта перестроен, потому что прежний путь 3 указывал на секцию, где строк «Паспорт → ID» нет | 09-26: search route rebuilt; old path 3 pointed to a section lacking "Passport -> ID" rows |
| P020 | 8 | CASE | прежний путь 2 работает только для шести воркфлоу Канала из девяти | 09-26: old path 2 worked only for six of nine Channel workflows |
| P021 | 8 | CASE | механизм дозаписи ADR дополнен инструментом для блоков крупнее двух килобайт | 09-26: ADR append mechanism extended with a tool for blocks over 2 KB |
| P022 | 8 | REASON | прежний единственный путь на таком объёме отказывает | Reason: the old single path fails at such size |
| P023 | 8 | CASE | из шаблона убрано `alwaysOutputData: true` как обязательное | 09-26: alwaysOutputData: true removed from template as mandatory |
| P024 | 8 | REASON | это антипаттерн по правилам SDK и корень R3 | Reason: it is an SDK anti-pattern and root cause R3 |
| P025 | 8 | CASE | восстановлены подчёркивания в схеме имени файла | 09-26: underscores restored in the file-name scheme |
| P026 | 8 | CASE | правило «ID воркфлоу в паспорт не вносить» уточнено | 09-26: rule "do not put workflow ID in passport" clarified |
| P027 | 8 | REASON | оно противоречило блоку СВЯЗИ, который без ID нечитаем | Reason: it contradicted the СВЯЗИ block, unreadable without IDs |
| P028 | 10 | CASE | Правка 2026-10-09 по харвесту 2026-10-08. | Edit dated 2026-10-09 based on harvest of 2026-10-08 |
| P029 | 10 | CASE | строка о SYSTEM-MAP заменена снимком registry/n8n-map.md | 10-09: SYSTEM-MAP line replaced by registry/n8n-map.md snapshot |
| P030 | 10 | REASON | SYSTEM-MAP больше не действует (харвест, противоречие В16) | Reason: SYSTEM-MAP no longer valid (harvest, contradiction В16) |
| P031 | 10 | CASE | абзац «get_workflow_details не отдаёт даже факт наличия credential» переписан | 10-09: paragraph claiming get_workflow_details does not even give credential presence rewritten |
| P032 | 10 | CASE | с 2026-10-08 инструмент отдаёт у узлов id и имя credential (позиция очереди AH-27) | Since 2026-10-08 tool returns credential id and name per node (queue item AH-27) |
| P033 | 10 | CASE | прежнее утверждение сохранено блоком ИСТОРИЯ ДИАГНОЗА | Old claim preserved as an ИСТОРИЯ ДИАГНОЗА block |
| P034 | 10 | CASE | стадия 3, пункт 5 — кто вписывает строку PASSPORT: владелец руками | Stage 3 point 5: owner writes the PASSPORT line by hand |
| P035 | 10 | REASON | как требуют четыре проекта, а запись описания агентом через MCP ограничена 255 знаками (находка А42) | Reason: four projects require it; agent description write via MCP limited to 255 chars (finding А42) |
| P036 | 10 | CASE | добавлена стадия 3а «Фаза не закрыта без паспорта» и правило «временный зонд паспорта не получает» (А42) | 10-09: added stage 3a and rule that temporary probe gets no passport (А42) |
| P037 | 10 | CASE | стадия 5 переписана: ставший ненужным воркфлоу снимается с публикации, а не архивируется (А7, предпочтение владельца 2026-10-08) | 10-09: stage 5 rewritten: unneeded workflow is unpublished not archived (А7, owner preference 2026-10-08) |
| P038 | 12 | CASE | Правка 2026-10-13 по стадии Б отбора уроков Архивариуса | Edit dated 2026-10-13 from stage Б of Archivarius lesson selection |
| P039 | 12 | ADDRESS | запись Р-38 журнала projects/archivarius/LOG.md; противоречие 11 карты projects/archivarius/TRIAGE.md | Sources: entry Р-38 of projects/archivarius/LOG.md; contradiction 11 of projects/archivarius/TRIAGE.md |
| P040 | 12 | CASE | Стадия 1: запрет «get_workflow_details в этом случае не вызывать» при найденном паспорте ограничен | 10-13: stage 1 ban on calling get_workflow_details when passport found was narrowed |
| P041 | 12 | RULE | ограничен пониманием воркфлоу и ответом на вопрос о нём | Ban applies only to understanding the workflow and answering questions about it |
| P042 | 12 | RULE | Правка, аудит, приёмка, разбор отказа и наряд, построенный на утверждении паспорта, читают живой код | Edit, audit, acceptance, failure analysis, and orders built on passport claims read live code |
| P043 | 12 | REASON | паспорт — заявление, а не доказательство (урок У-126; Skill naryad, references/issuer.md) | Reason: passport is a claim not proof (lesson У-126) |
| P044 | 12 | ADDRESS | Skill naryad, references/issuer.md | See Skill naryad, references/issuer.md |
| P045 | 12 | REASON | Прежняя формулировка противоречила n8n-engineering-manual (references/write.md 2.2 и 2.3) | Reason: old wording contradicted n8n-engineering-manual references/write.md 2.2 and 2.3 |
| P046 | 12 | RULE | который перед каждой правкой и после неё требует `get_workflow_details` | Manual requires get_workflow_details before and after every edit |
| P047 | 14 | RULE | Этот файл построен как жизнь одного документа: находят, читают, рождают, дозаписывают, закрывают | File structure follows doc life: find, read, create, append, close |
| P048 | 14 | RULE | Ищи стадию, на которой стоишь | Locate the stage you are at |
| P049 | 16 | THRESHOLD | ## Что паспорт знает, а что нет | Heading: what the passport knows and does not |
| P050 | 18 | THRESHOLD | Table header: Вопрос / Носитель ответа | Table maps question to answer carrier |
| P051 | 20 | RULE | Что существует: ID, имя, статус, черновик, расписание, таймзона, вызовы, документы, типы credential | Existence facts (ID, name, status, draft, schedule, timezone, calls, documents, credential types) are NOT in the passport |
| P052 | 20 | ADDRESS | файл registry/n8n-map.md репозитория second-brain-canon | Carrier of existence facts: registry/n8n-map.md in second-brain-canon |
| P053 | 20 | ADDRESS | формат строк — projects/n8n-map/PLAN.md раздел 4 | Row format described in projects/n8n-map/PLAN.md section 4 |
| P054 | 21 | RULE | Как работает, с чем связано, почему именно так, какие ловушки | Passport carries: how it works, links, why, traps |
| P055 | 21 | THRESHOLD | **паспорт воркфлоу** | Carrier is the workflow passport |
| P056 | 22 | RULE | Пути вебхуков и признак их аутентификации | Webhook paths and their auth flag are carried elsewhere |
| P057 | 22 | ADDRESS | Google Doc N8N_REGISTRY, строки HOOK и HOOKCALL | Google Doc N8N_REGISTRY, rows HOOK and HOOKCALL |
| P058 | 23 | RULE | Как воркфлоу складываются в систему: кто кого вызывает, кто в какой документ пишет | System composition (who calls whom, who writes which doc) carried by the snapshot |
| P059 | 23 | ADDRESS | registry/n8n-map.md — строки X (вызовы саб-воркфлоу), H (вызовы вебхуков), D (документы) | Rows X (sub-workflow calls), H (webhook calls), D (documents) in registry/n8n-map.md |
| P060 | 23 | RULE | Прежний документ SYSTEM-MAP заменён этим снимком и не ведётся | SYSTEM-MAP replaced by the snapshot and not maintained |
| P061 | 23 | ADDRESS | (projects/n8n/STATE.md) | SYSTEM-MAP replacement recorded in projects/n8n/STATE.md |
| P062 | 23 | RULE | указания «сначала читать SYSTEM-MAP» в старых планах проектов устарели | Instructions in old plans to read SYSTEM-MAP first are obsolete |
| P063 | 24 | RULE | Механика n8n, корневые причины отказов, протокол правки | Mechanics, root causes, edit protocol carried elsewhere |
| P064 | 24 | ADDRESS | n8n-engineering-manual | Carrier: n8n-engineering-manual |
| P065 | 25 | RULE | ID книг Sheets, специфика внешних API, формулы ключей | Sheets book IDs, external API specifics, key formulas carried elsewhere |
| P066 | 25 | ADDRESS | n8n-workflow-registry | Carrier: n8n-workflow-registry |
| P067 | 27 | RULE | Что в паспорт НЕ вносится: собственные ID и имя воркфлоу | Do NOT put the workflow's own ID and name in the passport |
| P068 | 27 | REASON | они выводятся из снимка и в паспорте разойдутся с объектом | Reason: derived from snapshot; in passport they diverge from the object |
| P069 | 27 | RULE | Что вносится обязательно: ID и имена того, что воркфлоу ВЫЗЫВАЕТ и КУДА пишет | MUST include IDs and names of what the workflow calls and writes to |
| P070 | 27 | REASON | без них блок СВЯЗИ нечитаем | Reason: without them the СВЯЗИ block is unreadable |
| P071 | 27 | CASE | Прежняя редакция запрещала «ID и Название» без этой оговорки и сама себе противоречила | Old edition banned "ID and Name" without qualification and contradicted itself |
| P072 | 27 | REASON | блок СВЯЗИ шаблона требует назвать вызываемые воркфлоу | Reason: template СВЯЗИ block requires naming called workflows |
| P073 | 29 | RULE | Что вносится обязательно: **имя привязанного credential** у каждого узла | MUST include the bound credential name for every node |
| P074 | 29 | CASE | С 2026-10-08 `get_workflow_details` отдаёт у узла поле `credentials` с id и именем ключа | Since 2026-10-08 get_workflow_details returns node field credentials with id and key name |
| P075 | 29 | CASE | воркфлоу `fGHfVrI58Ws1wfTw`, узел `02_Fetch_WB_Cards`: `[имя ключа — запись Р-5 projects/deklaration-wb/LOG.md]`, id `[id ключа — там же]` | Example: fGHfVrI58Ws1wfTw, node 02_Fetch_WB_Cards, [имя ключа — запись Р-5 projects/deklaration-wb/LOG.md], id [id ключа — там же] |
| P076 | 29 | CASE | проверено ещё раз 2026-10-09 на HTTP-узле и узлах Google Sheets воркфлоу `IvgysDKrq3UISYEY` | Rechecked 2026-10-09 on HTTP node and Google Sheets nodes of IvgysDKrq3UISYEY |
| P077 | 29 | RULE | имя теперь можно списать из объекта, а не только глазами в редакторе | Name can now be copied from the object, not only read by eye in the editor |
| P078 | 29 | ADDRESS | (projects/deklaration-wb/LOG.md, Р-5) | Evidence: projects/deklaration-wb/LOG.md, Р-5 |
| P079 | 29 | RULE | Снимок registry/n8n-map.md по-прежнему держит только ТИП credential | The snapshot still holds only credential TYPE |
| P080 | 29 | RULE | Паспорт держит имя ради причины: ПОЧЕМУ у узла именно этот ключ | Passport keeps the name for the reason: WHY this node has this key |
| P081 | 29 | REASON | этого объект не скажет (кабинет, юрлицо, право чтения или записи) | Reason: object does not say why (cabinet, legal entity, read/write right) |
| P082 | 29 | RULE | Расхождение имени в паспорте с объектом — дрейф паспорта, правится по объекту | Name mismatch is passport drift; fix passport per the object |
| P083 | 30 | CASE | ИСТОРИЯ ДИАГНОЗА: прежняя редакция утверждала, что get_workflow_details «не отдаёт даже факт наличия credential» | Diagnosis history: old edition claimed get_workflow_details gives no credential presence |
| P084 | 30 | CASE | делала паспорт единственным носителем имени ключа | Old edition made passport the sole carrier of key name |
| P085 | 30 | CASE | Так и было при проверке девяти воркфлоу в августе–сентябре 2026 (projects/n8n-map/PLAN.md, раздел 3) | True when checked on nine workflows Aug-Sep 2026 (PLAN.md section 3) |
| P086 | 30 | CASE | опровергнуто чтениями 2026-10-08 и 2026-10-09 — поле вернулось | Refuted by reads of 2026-10-08 and 10-09: field came back |
| P087 | 30 | CASE | На всех ли типах узлов оно есть, не проверено | Unverified: whether the credentials field exists on all node types |
| P088 | 32 | THRESHOLD | --- (horizontal rule separator) | Separator line |
| P089 | 34 | THRESHOLD | ## Стадия 1. Найти паспорт — первое действие перед любой работой с воркфлоу | Heading: Stage 1, find passport, first action before any workflow work |
| P090 | 36 | RULE | Перед правкой, отладкой, разбором или запуском воркфлоу сначала ищется паспорт | Before edit, debug, analysis or run, search the passport first |
| P091 | 36 | REASON | get_workflow_details возвращает сырой JSON, в котором воркфлоу лежит дважды — черновиком и опубликованной версией | Reason: get_workflow_details returns raw JSON with workflow twice (draft and published) |
| P092 | 36 | REASON | на крупном воркфлоу это десятки килобайт контекста | Reason: tens of KB of context on a large workflow |
| P093 | 36 | REASON | Паспорт даёт готовые факты | Reason: passport gives ready facts |
| P094 | 38 | RULE | Маршрут поиска, первое найденное останавливает поиск | Search route: first found stops the search |
| P095 | 40 | THRESHOLD | **Путь 1. Строка паспорта в `description` воркфлоу.** | Path 1: passport line in workflow description |
| P096 | 40 | RULE | Видна в выдаче `search_workflows`, отдельного чтения воркфлоу не нужно | Visible in search_workflows output; no separate read needed |
| P097 | 40 | RULE | Искать БЕЗ учёта регистра | Search case-insensitively |
| P098 | 40 | CASE | на 26.09.2026 из 64 живых воркфлоу со строкой паспорта 57 пишут `PASSPORT:`, а 7 — `Passport:` | On 2026-09-26: of 64 live workflows with passport line, 57 use PASSPORT: and 7 Passport: |
| P099 | 40 | REASON | Регистрочувствительный поиск теряет эти семь | Reason: case-sensitive search loses those seven |
| P100 | 42 | THRESHOLD | **Путь 2. Имя документа в папке DOCS.** | Path 2: document name in DOCS folder |
| P101 | 42 | THRESHOLD | Паспорта названы по схеме `[ПРОЕКТ]_WF_[имя-воркфлоу]` (стадия 3) | Name scheme [PROJECT]_WF_[workflow-name] |
| P102 | 42 | RULE | поиск по имени в Drive находит паспорт без всякого реестра | Search by name in Drive finds passport without any registry |
| P103 | 42 | CASE | `N8N_WF_registry-sync`, `WB_WF_telegram-router` | Name examples: N8N_WF_registry-sync, WB_WF_telegram-router |
| P104 | 42 | CASE | Прежняя редакция запрещала искать по папке словами «папка не говорит, какой документ к какому воркфлоу относится» | Old edition banned folder search claiming the folder does not map docs to workflows |
| P105 | 42 | REASON | это противоречило её же правилу именования: схема имени говорит именно это | Reason: contradicted its own naming rule, the name scheme says exactly that |
| P106 | 44 | THRESHOLD | **Путь 3. Строка воркфлоу в `registry/tools.md`** | Path 3: workflow row in registry/tools.md |
| P107 | 44 | RULE | только для воркфлоу Git-канала, и только для части из них | Path 3 applies only to Git-channel workflows and only some of them |
| P108 | 44 | CASE | На 26.09.2026 `registry/tools.md` называет шесть ID паспортов | On 2026-09-26 registry/tools.md names six passport IDs |
| P109 | 44 | CASE | у Git Read, Git Append, Git Append File и Git Log паспорт не назван ни там, ни в `description` | Git Read, Git Append, Git Append File, Git Log: passport named neither there nor in description |
| P110 | 46 | RULE | Паспорт найден — открыть по ID через `gdocs-read` | If found, open by ID via gdocs-read |
| P111 | 46 | RULE | читать ТОЛЬКО нужную зону по маркерам (стадия 2), не весь документ | Read only the needed zone by markers, not the whole doc |
| P112 | 46 | RULE | Чтобы понять воркфлоу или ответить на вопрос о нём, `get_workflow_details` в этом случае не вызывать | To understand the workflow or answer a question about it, do not call get_workflow_details |
| P113 | 46 | REASON | паспорт отвечает дешевле | Reason: passport answers cheaper |
| P114 | 48 | RULE | Живой код читается и при найденном паспорте, когда по прочитанному последует действие или вердикт | Live code is read even with passport when action or verdict follows |
| P115 | 49 | RULE | правка воркфлоу — пред-полётный чек-лист и пост-полётная сверка идут по `get_workflow_details`, паспорт их не заменяет | Editing: pre-flight checklist and post-flight check use get_workflow_details; passport does not replace |
| P116 | 49 | ADDRESS | n8n-engineering-manual (references/write.md 2.2 и 2.3) | n8n-engineering-manual references/write.md 2.2 and 2.3 |
| P117 | 50 | RULE | аудит, приёмка, разбор отказа, наряд, ЗАДАЧА которого опирается на утверждение паспорта | Audit, acceptance, failure analysis, order whose task rests on a passport claim: read live code |
| P118 | 50 | RULE | Паспорт здесь — заявление, а не доказательство | Passport is a claim, not evidence |
| P119 | 50 | CASE | 2026-07-29 документ проекта (реестр заданий) назвал эталоном загрузчик с DO NOTHING при конфликте ключа | 2026-07-29: project doc named a DO NOTHING loader as reference |
| P120 | 50 | CASE | живой код делал DO UPDATE, и буквальное исполнение пропустило бы все 182 записи | Live code did DO UPDATE; literal execution would have skipped all 182 records |
| P121 | 50 | CASE | аудит 2026-07-27 и 2026-07-28 нашёл 14 дефектов, и ни один не был найден чтением документов | Audit 2026-07-27/28 found 14 defects, none by reading documents |
| P122 | 50 | ADDRESS | WB_REVIEWS_INDEX, строки 314 и 2509–2512; строка У-126 карты projects/archivarius/TRIAGE.md | Evidence sources: WB_REVIEWS_INDEX lines 314 and 2509-2512; row У-126 of projects/archivarius/TRIAGE.md |
| P123 | 50 | ADDRESS | Как такой наряд выдавать — Skill naryad, references/issuer.md | How to issue such an order: Skill naryad, references/issuer.md |
| P124 | 52 | RULE | Расхождение паспорта с живым кодом — дрейф паспорта: правится паспорт по коду (стадия 4), а не наоборот | Passport vs live code mismatch is drift; fix passport per code (stage 4), not vice versa |
| P125 | 54 | RULE | Паспорт не найден ни одним путём — читать `get_workflow_details`, прямо сказать Андрею, что документации нет, и выполнить стадию 3 | No passport found: read get_workflow_details, tell Andrei plainly no docs exist, run stage 3 |
| P126 | 54 | RULE | Молча работать без паспорта нельзя | Never work silently without a passport |
| P127 | 54 | REASON | следующая сессия повторит тот же поиск | Reason: next session will repeat the same search |
| P128 | 56 | RULE | Перед действием с воркфлоу назвать, ЧТО прочитано и откуда: зону паспорта и дату его последнего изменения | Before acting, state what was read and from where: passport zone and last-change date |
| P129 | 56 | RULE | либо честно «паспорта нет, читал get_workflow_details» | Or honestly state: no passport, read get_workflow_details |
| P130 | 56 | RULE | Фиксированная фраза подтверждением не считается | A fixed phrase does not count as confirmation |
| P131 | 56 | REASON | она доказывает, что файл открыт, а не что в нём что-то прочитано | Reason: it proves the file was opened, not that something was read |
| P132 | 60 | THRESHOLD | ## Стадия 2. Читать — только нужную зону | Heading: Stage 2, read only the needed zone |
| P133 | 62 | RULE | Паспорт состоит из трёх зон, каждая открыта и закрыта уникальным маркером | Passport has three zones, each opened and closed by a unique marker |
| P134 | 62 | RULE | в обычном тексте маркеры не встречаются | Markers do not occur in ordinary text |
| P135 | 64 | THRESHOLD | Table header: Ситуация / Читать | Table maps situation to zones to read |
| P136 | 66 | RULE | Касание воркфлоу, понять что это — ЗОНА А | Touch workflow / understand what it is: read ZONE А |
| P137 | 67 | RULE | Изменение или отладка — ЗОНА А и ЗОНА Б | Change or debug: read ZONE А and Б |
| P138 | 68 | RULE | Вопрос «почему выбрали такой подход» — ЗОНА В | Question why this approach: read ZONE В |
| P139 | 69 | RULE | Создание нового паспорта или полная миграция — все три | Create new passport or full migration: read all three |
| P140 | 71 | RULE | Диапазон строк у `gdocs-read` ограничивает то, над чем сессия рассуждает, а не то, за что платит | gdocs-read line range limits what session reasons on, not what it pays for |
| P141 | 71 | REASON | узлы загрузки этого воркфлоу оставляют полный текст документа в `contextData` при любом запрошенном диапазоне | Reason: load nodes leave full doc text in contextData for any range |
| P142 | 71 | ADDRESS | (google-drive-docs раздел 9) | See google-drive-docs section 9 |
| P143 | 71 | RULE | Обещать экономию контекста выбором зоны нельзя — зона экономит внимание, не токены | Do not promise context savings via zone choice; zone saves attention not tokens |
| P144 | 75 | THRESHOLD | ## Стадия 3. Родить паспорт | Heading: Stage 3, create passport |
| P145 | 77 | RULE | Убедиться, что папка DOCS проекта существует | Step 1: ensure project DOCS folder exists |
| P146 | 77 | ADDRESS | ID папки — в секции ИНСТРУМЕНТЫ INDEX проекта, ключ `DOCS_FOLDER` | Folder ID is in the project INDEX section ИНСТРУМЕНТЫ, key DOCS_FOLDER |
| P147 | 77 | RULE | Папки нет → создать её инструментом create_folder (воркфлоу «Claude → Create Folder») | No folder: create via create_folder tool (workflow Claude -> Create Folder) |
| P148 | 77 | ADDRESS | ID — по правилу §1 Skill google-drive-docs, контракт — его §3.3 | Workflow ID per rule section 1 of Skill google-drive-docs; contract in its section 3.3 |
| P149 | 78 | RULE | Создать файл: `create_file` с `title: "[ПРОЕКТ]_WF_[имя-воркфлоу]"` | Step 2: create file via create_file with title per scheme |
| P150 | 78 | THRESHOLD | `contentMimeType: "text/plain"`, `textContent` по шаблону ниже, `parentId` — ID папки DOCS | create_file params: contentMimeType text/plain, textContent from template, parentId = DOCS folder ID |
| P151 | 78 | RULE | Подчёркивания в схеме имени обязательны | Underscores in the name scheme are mandatory |
| P152 | 78 | REASON | они и делают имя находимым | Reason: they make the name findable |
| P153 | 78 | CASE | `WB_WF_finance-sync`, `N8N_WF_gdocs-append`, `OZON_WF_intake` | Name examples: WB_WF_finance-sync, N8N_WF_gdocs-append, OZON_WF_intake |
| P154 | 79 | EXCEPTION | `create_file` отказал → фолбэк: копия существующего документа через `copy_file`, затем наполнение через `gdocs-overwrite` | If create_file refuses: fallback copy_file then gdocs-overwrite |
| P155 | 79 | ADDRESS | Разбор отказа — google-drive-docs, таблица ошибок, код E14 | Refusal analysis: google-drive-docs error table, code E14 |
| P156 | 80 | RULE | Взять ID из ответа `create_file` | Step 4: take ID from create_file response |
| P157 | 81 | RULE | Строка `PASSPORT: <ID Google Doc>` в конце `description` воркфлоу | Step 5: PASSPORT: <ID> line at end of workflow description |
| P158 | 81 | REASON | Это главный адрес паспорта: он виден в выдаче поиска и не зависит от того, где лежит INDEX проекта | Reason: it is the main passport address, visible in search, independent of INDEX location |
| P159 | 81 | RULE | Писать в ВЕРХНЕМ регистре | Write PASSPORT in UPPER case |
| P160 | 81 | REASON | смешение регистров уже стоило семи воркфлоу, которые находятся только поиском без учёта регистра | Reason: mixed case already cost seven workflows found only by case-insensitive search |
| P161 | 82 | RULE | Кто вписывает: **Андрей, руками, в настройках воркфлоу в редакторе.** | Andrei writes the PASSPORT line by hand in editor workflow settings |
| P162 | 82 | REASON | Так требуют планы четырёх проектов | Reason: four project plans require this |
| P163 | 82 | ADDRESS | projects/deklaration-wb/PLAN.md, projects/card-content-sync/PLAN.md, meta/DECLARATION_SCAN.md, projects/n8n/STATE.md | Four plans: deklaration-wb/PLAN.md, card-content-sync/PLAN.md, meta/DECLARATION_SCAN.md, n8n/STATE.md |
| P164 | 82 | RULE | Сессия даёт ему готовую строку на вставку и название воркфлоу | Session gives him a ready line to paste and the workflow name |
| P165 | 83 | REASON | Почему не сессия через MCP: `update_workflow` умеет менять описание операцией `setWorkflowMetadata`, но поле `description` ограничено 255 знаками | Why not session via MCP: update_workflow setWorkflowMetadata exists but description capped at 255 chars |
| P166 | 83 | CASE | Описания длиннее 255 знаков на инстансе есть (у `IvgysDKrq3UISYEY` — 282 знака) | Descriptions over 255 exist: IvgysDKrq3UISYEY has 282 |
| P167 | 83 | REASON | строка PASSPORT стоит в конце: запись агентом длинного описания либо откажет, либо отрежет именно адрес паспорта | Reason: PASSPORT line is at the end; agent write of long description fails or truncates the address |
| P168 | 83 | CASE | Вызов `create_workflow_from_code` тоже сокращает описание до 255 знаков | create_workflow_from_code also truncates description to 255 |
| P169 | 83 | CASE | Сведения взяты из описания инструментов MCP 2026-10-09; вызовом не проверялось | Facts from MCP tool descriptions of 2026-10-09; not verified by an actual call |
| P170 | 84 | RULE | Воркфлоу создаётся в этой же сессии → описание держать коротким, чтобы вместе со строкой PASSPORT оно уложилось в 255 знаков | If workflow created in same session: keep description short to fit with PASSPORT line in 255 chars |
| P171 | 84 | RULE | передать его параметром `description` вызова `create_workflow_from_code` | Pass it as description param of create_workflow_from_code |
| P172 | 84 | EXCEPTION | паспорт к этому моменту обычно ещё не создан — тогда строку позже вписывает Андрей | Usually passport does not exist yet then; Andrei adds the line later |
| P173 | 85 | CHECK | Проверка: строка видна в выдаче `search_workflows` по имени воркфлоу | Check: line visible in search_workflows output by workflow name |
| P174 | 85 | RULE | Слово «вписал» проверкой не считается — только выдача поиска | The word "written" is not a check; only search output |
| P175 | 86 | CASE | ИСТОРИЯ ДИАГНОЗА: прежняя редакция запрещала запись описания через MCP | Old edition banned description write via MCP |
| P176 | 86 | REASON | `update_workflow` пересобирает все узлы из переданного кода и может молча снять аутентификацию вебхука (корень R12) | Old reason: update_workflow rebuilt all nodes and could silently drop webhook auth (root R12) |
| P177 | 86 | CASE | Это было верно для прежней формы инструмента, которая принимала код воркфлоу целиком | True for old tool form taking whole workflow code |
| P178 | 86 | CASE | нынешний `update_workflow` принимает отдельные операции, и операция над описанием узлы не трогает | Current update_workflow takes separate operations; description op does not touch nodes |
| P179 | 86 | REASON | Запрет остаётся по другой причине — предел 255 знаков и требование владельца | Ban stays for different reason: 255-char limit and owner requirement |
| P180 | 87 | RULE | Только после проверки сказать «паспорт создан» | Step 6: say "passport created" only after verification |
| P181 | 87 | EXCEPTION | Проверка упала → ID остаётся в чате как резервная копия, об ошибке сказать прямо, паспорт созданным не считать | If check fails: ID stays in chat as backup, state error plainly, do not count passport as created |
| P182 | 89 | RULE | Временный зонд — воркфлоу только для чтения, созданный, чтобы один раз снять факты, — паспорта не получает | Temporary probe (read-only, one-time facts) gets no passport |
| P183 | 89 | RULE | Его итог — запись в журнал проекта (что снято, номер исполнения, ID зонда) | Probe result goes to project log: what captured, execution number, probe ID |
| P184 | 89 | EXCEPTION | Если зонд оказался нужен снова и стал инструментом (стадия 5), паспорт создаётся при первой его правке | If probe becomes a tool, passport is created at its first edit |
| P185 | 91 | RULE | Строка в секции ИНСТРУМЕНТЫ INDEX проекта больше не ведётся | The INDEX ИНСТРУМЕНТЫ line is no longer maintained |
| P186 | 91 | REASON | она дублировала строку в `description` | Reason: it duplicated the description line |
| P187 | 91 | CASE | на 26.09.2026 все найденные строки «Паспорт → ID» лежали не в ИНСТРУМЕНТАХ, а в хронике Зоны Б | On 2026-09-26 all found Passport->ID rows were in Zone Б chronicle, not ИНСТРУМЕНТЫ |
| P188 | 91 | REASON | искать их там, где предписано, было бесполезно | Reason: searching where prescribed was useless |
| P189 | 91 | EXCEPTION | У проектов, чей INDEX перенесён в репозиторий — например лаборатория `labs/sys/` — секции ИНСТРУМЕНТЫ нет вовсе | Projects with INDEX in repo (e.g. labs/sys/) have no ИНСТРУМЕНТЫ section |
| P190 | 91 | ADDRESS | (second-brain-git 4б.3) | See second-brain-git 4б.3 |
| P191 | 95 | THRESHOLD | ## Стадия 3а. Фаза не закрыта без документации | Heading: Stage 3a, phase not closed without documentation |
| P192 | 97 | CASE | Требование Андрея от 2026-10-02: техническая документация — часть поставки, а не отдельный шаг на потом | Andrei's requirement 2026-10-02: tech docs are part of delivery |
| P193 | 97 | ADDRESS | (projects/deklaration-ozon/LOG.md, Р-20) | Source: projects/deklaration-ozon/LOG.md, Р-20 |
| P194 | 97 | RULE | Фаза плана или наряд, который создаёт или меняет воркфлоу, не считается закрытым, пока нет трёх вещей | Phase/order creating or changing a workflow is not closed until three things exist |
| P195 | 98 | RULE | паспорт по стадии 3 или новый ADR по стадии 4 | Thing 1: passport (stage 3) or new ADR (stage 4) |
| P196 | 99 | RULE | строка PASSPORT в `description`, видимая в выдаче `search_workflows` | Thing 2: PASSPORT line in description visible in search_workflows |
| P197 | 100 | RULE | инструкция для человека, если воркфлоу запускает человек (форма, ручной запуск) | Thing 3: human instruction if a human launches the workflow |
| P198 | 100 | ADDRESS | где она лежит, решает план проекта | Where the instruction lives is decided by the project plan |
| P199 | 102 | EXCEPTION | Временного зонда это не касается — у него нет паспорта (стадия 3) | Temporary probe is exempt from stage 3a |
| P200 | 106 | THRESHOLD | ## Стадия 4. Дозаписать после каждой правки воркфлоу | Heading: Stage 4, append after every workflow edit |
| P201 | 108 | RULE | Это продолжение протокола изменений из n8n-engineering-manual | Stage 4 continues the change protocol of n8n-engineering-manual |
| P202 | 108 | RULE | Выполняется в той же сессии, где была правка. Не переносится на потом | Performed in same session as the edit; not deferred |
| P203 | 110 | RULE | **Шаг 1.** Назвать паспорт, которого касается правка | Step 1: name the passport the edit concerns |
| P204 | 112 | RULE | **Шаг 2.** Паспорта нет → создать по стадии 3 прямо сейчас | Step 2: no passport: create per stage 3 immediately |
| P205 | 112 | RULE | Паспорт есть → три действия, все три | Passport exists: three actions, all three |
| P206 | 113 | RULE | вставить ADR-блок перед маркером `%%ЗОНА_В_КОНЕЦ%%` (механизм ниже) | Action 1: insert ADR block before %%ЗОНА_В_КОНЕЦ%% marker |
| P207 | 114 | RULE | сверить строки ЗОНЫ А — ТРИГГЕР, СВЯЗИ, CREDENTIALS — и ЗОНЫ Б — СХЕМА, ИЗВЕСТНЫЕ ОГРАНИЧЕНИЯ | Action 2: reconcile Zone А lines (ТРИГГЕР, СВЯЗИ, CREDENTIALS) and Zone Б (СХЕМА, ИЗВЕСТНЫЕ ОГРАНИЧЕНИЯ) |
| P208 | 114 | REASON | ADR без этой сверки означает дрейф, а не обновление | Reason: ADR without reconciliation means drift, not update |
| P209 | 114 | RULE | Особое внимание составу узлов: правка, добавляющая узлы, делает СХЕМУ неверной молча | Pay special attention to node set: adding nodes silently makes СХЕМА wrong |
| P210 | 114 | CASE | 26.09.2026 у воркфлоу `gFFiBPm1OomOzJOj` узлов стало восемь вместо пяти, и схема в паспорте описывала прежнюю цепочку | 2026-09-26 gFFiBPm1OomOzJOj grew to eight nodes from five; passport schema described old chain |
| P211 | 115 | RULE | проверить результат перечитыванием документа, а не ответом инструмента | Action 3: verify by re-reading the doc, not by tool response |
| P212 | 117 | RULE | **Шаг 3.** Сессия не закрывается без выполненного шага 2 либо явного отказа Андрея с указанной причиной | Step 3: session not closed without step 2 or explicit Andrei refusal with reason |
| P213 | 119 | RULE | Claude следит, чтобы шаги не были пропущены | Claude ensures steps are not skipped |
| P214 | 119 | RULE | Андрей отвечает за содержание ADR — контекст, альтернативы, последствия | Andrei owns ADR content: context, alternatives, consequences |
| P215 | 121 | THRESHOLD | ### Правило записи зон | Subheading: zone write rule |
| P216 | 123 | RULE | ЗОНА А и ЗОНА Б — правятся через `gdocs-replace` короткими УНИКАЛЬНЫМИ ОДНОСТРОЧНЫМИ якорями | Zones А and Б edited via gdocs-replace with short unique single-line anchors |
| P217 | 123 | ADDRESS | Skill `google-drive-docs`, `references/docs-write.md`, раздел 3.2 | Why multi-line anchor is banned and how to choose: google-drive-docs references/docs-write.md section 3.2 |
| P218 | 123 | EXCEPTION | Строка не уникальна → не дробить правку, а дописать новый блок с датой внутри зоны | Line not unique: do not split the edit, append a dated new block inside the zone |
| P219 | 125 | RULE | ЗОНА В — только дозапись. Старые ADR-блоки не редактировать и не удалять | Zone В is append-only; do not edit or delete old ADR blocks |
| P220 | 127 | RULE | Новый ADR вставляется ПЕРЕД маркером `%%ЗОНА_В_КОНЕЦ%%`. Инструмент выбирается по размеру блока | New ADR is inserted BEFORE the end marker; tool chosen by block size |
| P221 | 130 | THRESHOLD | Table header: Размер ADR-блока / Чем вставлять | Table maps ADR block size to tool |
| P222 | 131 | RULE | до примерно 2 КБ: `gdocs-replace`: якорь `%%ЗОНА_В_КОНЕЦ%%` заменяется на (ADR-блок + перенос строки + тот же маркер) | Up to ~2 KB: gdocs-replace, anchor replaced with ADR + newline + same marker |
| P223 | 132 | RULE | крупнее примерно 2 КБ: `gdocs-apply-from-file` в режиме `replace`, `search` = `%%ЗОНА_В_КОНЕЦ%%` | Over ~2 KB: gdocs-apply-from-file, mode replace, search = end marker |
| P224 | 132 | RULE | текст ADR вместе с маркером кладётся файлом на Drive | ADR text with marker is placed as a file on Drive |
| P225 | 132 | REASON | Через тело вызова текст не проходит, ограничение размера не действует | Reason: text does not pass through call body, so size limit does not apply |
| P226 | 134 | RULE | Граница около 2 КБ — осторожная линия, а не измеренный предел | The ~2 KB boundary is a cautious line not a measured limit |
| P227 | 134 | ADDRESS | её причина и условие пересмотра — Skill `google-drive-docs`, `references/docs-write.md`, раздел 3.0 | Its reason and revision condition: google-drive-docs references/docs-write.md section 3.0 |
| P228 | 134 | CASE | ADR от 26.09.2026 для воркфлоу `gFFiBPm1OomOzJOj` весил 5 570 байт и пошёл только вторым путём | ADR of 2026-09-26 for gFFiBPm1OomOzJOj weighed 5,570 bytes and went only by the second path |
| P229 | 136 | RULE | Простой `gdocs-append` для ADR ЗАПРЕЩЁН | Plain gdocs-append for ADR is FORBIDDEN |
| P230 | 136 | REASON | он пишет в конец документа, ПОСЛЕ маркера, и блок выпадает из читаемой зоны | Reason: writes to doc end after marker; block falls out of the readable zone |
| P231 | 136 | CASE | Наблюдался 30.06.2026 — паспорт Evening Report, три ADR вне зоны | Observed 2026-06-30: Evening Report passport, three ADRs outside the zone |
| P232 | 138 | CHECK | После вставки перечитать документ | After insertion re-read the document |
| P233 | 138 | REASON | склейка строк не ловится ответом `success: true` | Reason: line merging is not caught by success: true response |
| P234 | 142 | THRESHOLD | ## Стадия 5. Воркфлоу больше не нужен | Heading: Stage 5, workflow no longer needed |
| P235 | 144 | CASE | Правило владельца от 2026-10-08 | Owner rule dated 2026-10-08 |
| P236 | 144 | RULE | ставший ненужным воркфлоу — временный зонд, пробный, одноразовый или вытесненный новым — снимается с публикации, но не архивируется и не удаляется | Unneeded workflow (probe, trial, one-off, superseded) is unpublished, not archived or deleted |
| P237 | 144 | REASON | Это инструменты, которые наверняка понадобятся снова; их оставляют и называют как инструменты | Reason: tools will surely be needed again; keep and name them as tools |
| P238 | 144 | ADDRESS | (projects/deklaration-wb/LOG.md, Р-6; meta/PENDING_RULES.md, строка 6) | Sources: deklaration-wb/LOG.md Р-6; meta/PENDING_RULES.md line 6 |
| P239 | 144 | RULE | Пометки «временный — архивировать после снимка» в описаниях воркфлоу и в журналах проектов не исполняются | Marks "temporary, archive after snapshot" in descriptions and logs are not executed |
| P240 | 144 | CASE | Прежняя практика архивировать зонды (например, projects/deklaration-ozon/LOG.md, Р-15) этим правилом отменена | Old practice of archiving probes (e.g. deklaration-ozon/LOG.md Р-15) is cancelled by this rule |
| P241 | 146 | THRESHOLD | Порядок: | Order of steps heading |
| P242 | 147 | RULE | Снять с публикации | Step 1: unpublish |
| P243 | 148 | CHECK | Проверить снятие чтением объекта: `search_workflows` или `get_workflow_details` показывает `active: false` | Step 2 check: read object; search_workflows or get_workflow_details shows active: false |
| P244 | 148 | RULE | Слово «деактивировал» проверкой не считается | The word "deactivated" is not a check |
| P245 | 148 | CASE | 2026-10-01 владелец сообщил, что снял воркфлоу, а поиск показал `active: true` — снятие не состоялось | 2026-10-01 owner said he unpublished, search showed active: true; unpublishing had not happened |
| P246 | 148 | ADDRESS | (projects/git-migration/LOG.md, Р-126) | Source: projects/git-migration/LOG.md, Р-126 |
| P247 | 149 | RULE | Записать, что воркфлоу снят и почему, туда, где проект хранит невзятое и снятое | Step 3: record that workflow was unpublished and why where project keeps not-taken/removed |
| P248 | 149 | ADDRESS | обычно NOT_TAKEN.md или журнал проекта | Usually NOT_TAKEN.md or project log |
| P249 | 150 | RULE | Если у воркфлоу есть паспорт — вставить перед `%%ЗОНА_В_КОНЕЦ%%` строку | Step 4: if passport exists insert a status line before the end marker |
| P250 | 153 | THRESHOLD | СТАТУС: СНЯТ С ПУБЛИКАЦИИ [дата] — [причина; чем вытеснен, если вытеснен] | Status line format: СТАТУС: СНЯТ С ПУБЛИКАЦИИ [date] - [reason; superseded by] |
| P251 | 156 | EXCEPTION | Если владелец всё же решил архивировать воркфлоу — та же строка со словом `АРХИВИРОВАН` | If owner decides to archive: same line with word АРХИВИРОВАН |
| P252 | 156 | RULE | Решение об архивации принимает только владелец, сессия её не предлагает по умолчанию | Only owner decides archiving; session does not propose it by default |
| P253 | 158 | RULE | Паспорт не удалять никогда | Never delete the passport |
| P254 | 158 | REASON | ЗОНА В с историей решений остаётся, и именно по ней потом узнают, почему воркфлоу сняли | Reason: Zone В with decision history remains and tells later why workflow was removed |
| P255 | 158 | RULE | Состояние `active` или `archived` само по себе выводится из снимка | active/archived state is derived from the snapshot |
| P256 | 158 | REASON | строка в паспорте нужна ради причины, а не ради статуса | Reason: the passport line is for the cause, not the status |
| P257 | 162 | THRESHOLD | ## Шаблон паспорта | Heading: passport template |
| P258 | 165 | THRESHOLD | ПАСПОРТ ВОРКФЛОУ | Template title line |
| P259 | 166 | THRESHOLD | Создан: ГГГГ-ММ-ДД | Header field Создан with date format YYYY-MM-DD |
| P260 | 167 | THRESHOLD | Последнее изменение: ГГГГ-ММ-ДД | Header field Последнее изменение with date format |
| P261 | 169 | THRESHOLD | %%ЗОНА_А_НАЧАЛО%% | Zone А start marker |
| P262 | 170 | THRESHOLD | ━━━━━ (separator line) | Decorative separator line of zone header |
| P263 | 171 | THRESHOLD | ЗОНА А — что это и с чем связано | Zone А title: what it is and what it is linked to |
| P264 | 172 | RULE | Читается при каждом касании воркфлоу | Zone А is read on every touch of the workflow |
| P265 | 175 | THRESHOLD | НАЗНАЧЕНИЕ | Field НАЗНАЧЕНИЕ |
| P266 | 176 | THRESHOLD | [Что делает и зачем] | НАЗНАЧЕНИЕ content: what it does and why |
| P267 | 178 | THRESHOLD | ТРИГГЕР | Field ТРИГГЕР |
| P268 | 179 | THRESHOLD | [Webhook / Schedule / MCP / Ручной / Псевдо-ручной] | ТРИГГЕР type values: Webhook, Schedule, MCP, Manual, Pseudo-manual |
| P269 | 180 | THRESHOLD | [Детали: путь вебхука, расписание, параметры запуска] | ТРИГГЕР details: webhook path, schedule, launch parameters |
| P270 | 182 | THRESHOLD | ВХОДНЫЕ ДАННЫЕ | Field ВХОДНЫЕ ДАННЫЕ |
| P271 | 183 | THRESHOLD | [Источник, формат, обязательные поля] | Inputs content: source, format, required fields |
| P272 | 185 | THRESHOLD | ВЫХОДНЫЕ ДАННЫЕ | Field ВЫХОДНЫЕ ДАННЫЕ |
| P273 | 186 | THRESHOLD | [Куда пишет и что возвращает, ключевые поля, условия записи] | Outputs content: where it writes, what it returns, key fields, write conditions |
| P274 | 188 | THRESHOLD | СВЯЗИ | Field СВЯЗИ |
| P275 | 189 | THRESHOLD | Запускается из: [воркфлоу-инициатор / внешний триггер / MCP] | СВЯЗИ line: Launched from (initiator / external trigger / MCP) |
| P276 | 190 | THRESHOLD | Запускает: [воркфлоу и его ID] при [условии] | СВЯЗИ line: Launches (workflow and ID) on condition |
| P277 | 191 | THRESHOLD | [воркфлоу и его ID] при ошибке | СВЯЗИ line: launches (workflow and ID) on error |
| P278 | 192 | THRESHOLD | Читает: [источник → лист / документ / API] | СВЯЗИ line: Reads (source to sheet/doc/API) |
| P279 | 193 | THRESHOLD | Пишет: [назначение → лист / документ / API] | СВЯЗИ line: Writes (destination to sheet/doc/API) |
| P280 | 194 | RULE | Правило: связи описываются только в паспорте инициатора | Links are described only in the initiator's passport |
| P281 | 194 | RULE | Получатель про входящую связь не знает — это не его ответственность | Recipient does not record the incoming link; not its responsibility |
| P282 | 195 | REASON | Один источник истины на каждую связь | Reason: one source of truth per link |
| P283 | 198 | THRESHOLD | CREDENTIALS | Field CREDENTIALS |
| P284 | 199 | THRESHOLD | [Узел → имя credential → тип] | CREDENTIALS format: node, credential name, type |
| P285 | 200 | THRESHOLD | Пример: | Example follows |
| P286 | 201 | CASE | 08A_Generate_Review → Anthropic API Key → Header Auth | Example row: 08A_Generate_Review, Anthropic API Key, Header Auth |
| P287 | 202 | CASE | 07_Write_RAW → Google Sheets OAuth → OAuth2 | Example row: 07_Write_RAW, Google Sheets OAuth, OAuth2 |
| P288 | 203 | RULE | Имя списывается из get_workflow_details (поле credentials узла) | Credential name is copied from get_workflow_details credentials field |
| P289 | 204 | RULE | здесь — ещё и почему у узла именно этот ключ (кабинет, юрлицо, право) | Passport also records why the node has this key (cabinet, legal entity, right) |
| P290 | 205 | THRESHOLD | %%ЗОНА_А_КОНЕЦ%% | Zone А end marker |
| P291 | 207 | THRESHOLD | %%ЗОНА_Б_НАЧАЛО%% | Zone Б start marker |
| P292 | 208 | THRESHOLD | ━━━━━ (separator line) | Decorative separator line of zone Б header |
| P293 | 209 | THRESHOLD | ЗОНА Б — как устроено внутри | Zone Б title: how it is built inside |
| P294 | 210 | RULE | Читается при изменении или отладке воркфлоу | Zone Б read on change or debug |
| P295 | 213 | THRESHOLD | СХЕМА (ключевые точки) | Field СХЕМА (key points) |
| P296 | 214 | RULE | Только развилки, критические настройки, циклы — не все узлы | СХЕМА shows only forks, critical settings, loops; not all nodes |
| P297 | 215 | RULE | Отступ показывает цепочку: дочерний узел правее родителя | Indentation shows chain: child node to the right of parent |
| P298 | 216 | THRESHOLD | Пример: | Example follows |
| P299 | 217 | CASE | Триггер → Получить данные (HTTP) → Есть данные? (Filter) → Нормализовать → Дедуплицировать → Записать | Example chain: Trigger, Fetch (HTTP), Has data? (Filter), Normalize, Dedupe, Write |
| P300 | 221 | RULE | Ветвь «нечего делать» — сознательный терминал: ноль items штатно останавливает цепочку | The "nothing to do" branch is a deliberate terminal; zero items normally stop the chain |
| P301 | 222 | RULE | НЕ ставить alwaysOutputData ради «чтобы не обрывалось» | Do NOT set alwaysOutputData just so the chain does not break |
| P302 | 223 | REASON | это создаёт пустой item, на котором падают чтения полей — корень R3 n8n-engineering-manual | Reason: creates an empty item on which field reads fail; root R3 |
| P303 | 224 | EXCEPTION | Флаг оправдан только когда пустой случай обрабатывает отдельная ветвь, и тогда рядом стоит явная проверка на пустоту | Flag justified only when a separate branch handles the empty case with an explicit emptiness check beside it |
| P304 | 227 | THRESHOLD | ИЗВЕСТНЫЕ ОГРАНИЧЕНИЯ | Field ИЗВЕСТНЫЕ ОГРАНИЧЕНИЯ |
| P305 | 228 | THRESHOLD | [Что нельзя менять без последствий, зависимости, гонки, ручные шаги владельца] | Content: what cannot be changed without consequences, dependencies, races, owner manual steps |
| P306 | 229 | THRESHOLD | %%ЗОНА_Б_КОНЕЦ%% | Zone Б end marker |
| P307 | 231 | THRESHOLD | %%ЗОНА_В_НАЧАЛО%% | Zone В start marker |
| P308 | 232 | THRESHOLD | ━━━━━ (separator line) | Decorative separator line of zone В header |
| P309 | 233 | THRESHOLD | ЗОНА В — история решений | Zone В title: decision history |
| P310 | 234 | RULE | Читается при вопросе "почему именно так" | Zone В read on question "why this way" |
| P311 | 237 | THRESHOLD | [ГГГГ-ММ-ДД] РЕШЕНИЕ: [что выбрано — параметр, узел, схема] | ADR field РЕШЕНИЕ with date: what was chosen |
| P312 | 238 | THRESHOLD | КОНТЕКСТ: [какая проблема стояла] | ADR field КОНТЕКСТ: what problem stood |
| P313 | 239 | THRESHOLD | АЛЬТЕРНАТИВЫ: [что отвергли и почему] | ADR field АЛЬТЕРНАТИВЫ: what was rejected and why |
| P314 | 240 | THRESHOLD | ПОСЛЕДСТВИЯ: [на что влияет и что ограничивает] | ADR field ПОСЛЕДСТВИЯ: what it affects and constrains |
| P315 | 241 | THRESHOLD | ПРИЁМКА: [чем доказано, что правка работает — по объекту, не по статусу] | ADR field ПРИЁМКА: proof the edit works, by object not by status |
| P316 | 243 | RULE | [каждый новый блок вставляется ПЕРЕД маркером ниже, по «Правилу записи зон»] | Each new block is inserted before the marker below per the zone write rule |
| P317 | 244 | THRESHOLD | %%ЗОНА_В_КОНЕЦ%% | Zone В end marker |
| P318 | 247 | CASE | Поле ПРИЁМКА добавлено этой редакцией | Field ПРИЁМКА was added by this edition |
| P319 | 247 | REASON | без него ADR фиксирует замысел, но не факт, что правка легла | Reason: without it ADR records intent but not that the edit landed |
| P320 | 247 | RULE | Доказательство — объект воздействия или номер исполнения, не ответ инструмента | Proof is the target object or execution number, not tool response |
| P321 | 251 | THRESHOLD | ## Где хранятся паспорта | Heading: where passports are stored |
| P322 | 253 | RULE | Папка DOCS заводится отдельно для каждого проекта | A DOCS folder is created separately per project |
| P323 | 253 | ADDRESS | Её ID регистрируется в секции ИНСТРУМЕНТЫ соответствующего INDEX строкой `DOCS_FOLDER: [ID папки Google Drive]` | Its ID is registered in INDEX section ИНСТРУМЕНТЫ as DOCS_FOLDER: [ID] |
| P324 | 255 | THRESHOLD | Имя файла — `[ПРОЕКТ]_WF_[имя-воркфлоу]` | File name scheme [PROJECT]_WF_[workflow-name] |
| P325 | 257 | THRESHOLD | Table header: Имя файла / Расшифровка | Table of name examples |
| P326 | 259 | CASE | `N8N_WF_gdocs-append` — Second Brain, воркфлоу append | N8N_WF_gdocs-append = Second Brain, append workflow |
| P327 | 260 | CASE | `WB_WF_finance-sync` — Wildberries, финансовая синхронизация | WB_WF_finance-sync = Wildberries finance sync |
| P328 | 261 | CASE | `OZON_WF_intake` — Ozon, загрузка отзывов | OZON_WF_intake = Ozon review intake |
| P329 | 263 | RULE | Схема имени — не косметика | Name scheme is not cosmetic |
| P330 | 263 | REASON | она единственное, что позволяет найти паспорт поиском по Drive, когда строки в `description` нет | Reason: only thing enabling Drive search for passport when description has no line |
| P331 | 267 | THRESHOLD | ## Долги на 26.09.2026 | Heading: debts as of 2026-09-26 |
| P332 | 269 | RULE | Это снимок чисел, а не правило | This is a snapshot of numbers, not a rule |
| P333 | 269 | CHECK | Числа выводятся заново одним вызовом `search_workflows`: строка паспорта ищется в `description` без учёта регистра | Numbers re-derived with one search_workflows call: passport line searched in description case-insensitively |
| P334 | 271 | CASE | Строка паспорта есть у 64 живых воркфлоу из 113. У 49 её нет | Passport line exists at 64 of 113 live workflows; 49 lack it |
| P335 | 272 | CASE | У 6 живых воркфлоу `description` пуст вовсе — для них путь 1 невозможен | 6 live workflows have empty description; path 1 impossible |
| P336 | 273 | CASE | Регистр не единый: `PASSPORT:` у 57, `Passport:` у 7 | Case inconsistent: PASSPORT: 57, Passport: 7 |
| P337 | 274 | CASE | Четыре воркфлоу Git-канала — Git Read, Git Append, Git Append File, Git Log — не имеют строки паспорта ни в `description`, ни названного ID паспорта в `registry/tools.md` | Four Git-channel workflows have no passport line nor named passport ID in registry/tools.md |
| P338 | 274 | RULE | Либо паспорта нет, либо он недостижим; и то и другое — долг | Either no passport or unreachable; both are debt |
| P339 | 276 | CASE | Прежняя редакция держала здесь таблицу «три критических паспорта создать в первую очередь»: gdocs-append v2, WB Reviews Response, WB RAW Finance Sync | Old edition held a table of three critical passports to create first: gdocs-append v2, WB Reviews Response, WB RAW Finance Sync |
| P340 | 276 | CASE | Все три паспорта существуют, строки в `description` у всех трёх стоят — таблица предписывала уже сделанную работу. Снята | All three passports exist with description lines; table prescribed done work; removed |
| P341 | 276 | CASE | она называла воркфлоу «WB RAW Finance Sync», тогда как ID `IvgysDKrq3UISYEY` принадлежит «WB RAW Finance Sync V.3», а воркфлоу с прежним именем заархивирован | Table named "WB RAW Finance Sync" but ID IvgysDKrq3UISYEY belongs to "WB RAW Finance Sync V.3"; old-name workflow is archived |
| P342 | 278 | RULE | Порядок создания остальных прежний: при следующем касании воркфлоу, а не пачкой заранее | Remaining passports are created at next touch of each workflow, not in a batch in advance |

## Coverage

Total units: 342

- ADDRESS: 29
- CASE: 65
- CHECK: 4
- EXCEPTION: 9
- REASON: 41
- RULE: 121
- THRESHOLD: 73

Old-file lines with text not covered: 1, 4, 19, 58, 65, 73, 93, 104, 129, 140, 152, 154, 160, 164, 173, 196, 211, 218, 219, 220, 225, 235, 245, 249, 258, 265
