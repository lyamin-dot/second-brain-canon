# ACCEPTANCE — n8n-workflow-registry → router

Checked 2026-10-21 against /tmp/sbc after `git pull` (HEAD 56aeb1b). Old text = mirror at commit b91fb1e (byte-identical to old/ files, verified with diff). Reachability: a carrier counts if the router names it, or a file the router names (including the Skills it names: n8n-engineering-manual, google-drive-docs, second-brain-git, second-brain-engineer, n8n-workflow-passport) names it; journals only when such a chain leads there. Python verified that every AT_CARRIER and WEAKENED quote is an exact substring of the cited line, and that every router quote is on the cited router line (0 failures).

## Counts

- IN_ROUTER: 41
- AT_CARRIER: 392
- HISTORY: 33
- PROPOSED_REMOVAL: 14
- WEAKENED: 7
- LOST: 3
- total: 490

## Verdict table

```tsv
id	verdict	address	quote
U001	IN_ROUTER	router:2	name: "n8n-workflow-registry"
U002	IN_ROUTER	router:3	Маршрутизатор к деталям инстанса n8n Андрея, которые ниоткуда не выводятся
U003	IN_ROUTER	router:3	Живой состав воркфлоу — registry/n8n-map.md
U004	IN_ROUTER	router:3	Живой состав воркфлоу — registry/n8n-map.md
U005	WEAKENED	router:3	Читай, когда нужна такая деталь и неизвестно, в каком файле её искать
U006	IN_ROUTER	router:28	прежний файл `references/cards-and-declarations.md`
U007	WEAKENED	router:3	перед записью в карточку Wildberries или Ozon
U008	IN_ROUTER	router:3	правила и механика n8n — n8n-engineering-manual
U009	IN_ROUTER	router:6	# Где лежат детали инстанса
U010	HISTORY	SKILL.md:8	Редакция 2026-09-26.
U011	HISTORY	SKILL.md:8	адрес живого состава воркфлоу переведён с Google Doc N8N_REGISTRY на файл regist
U012	HISTORY	SKILL.md:8	абзац про ключ к своему API исправлен — он называл ротированный ключ действующим
U013	HISTORY	SKILL.md:8	раздел про инструменты Docs сведён к тому, чего нет в google-drive-docs
U014	HISTORY	SKILL.md:8	добавлен раздел 2.2 — двадцать девять книг инстанса, у которых нет человеческого
U015	HISTORY	SKILL.md:8	MASTER_MAP опознан как лист, а не отдельная книга
U016	HISTORY	SKILL.md:8	Прежний заголовок несёл пометку «v3.0, усечён» — она описывала неизвестное прошл
U017	HISTORY	SKILL.md:10	Правка 2026-10-09 по харвесту 2026-10-08.
U018	HISTORY	SKILL.md:10	в раздел 3 «Wildberries» добавлены факты записи карточек
U019	HISTORY	SKILL.md:10	добавлены подразделы «Ozon — общее», «Ozon — декларации и описание карточек», «П
U020	HISTORY	SKILL.md:10	«Внешние источники: что недоступно и откуда» (А27 с дополнением из Б7)
U021	HISTORY	SKILL.md:10	формула `raw_key` Wildberries исправлена по коду узла
U022	HISTORY	SKILL.md:10	MASTER_MAP перестал называться живым кросс-маппингом (В12)
U023	HISTORY	SKILL.md:10	скрипт `processDeclPdfInbox` описан как снятый (В18)
U024	HISTORY	SKILL.md:10	к строке о книге ключей N8N_CREDENTIALS добавлено правило имени и исключение вла
U025	HISTORY	SKILL.md:10	добавлена проверка ID Google по длине (А38)
U026	HISTORY	SKILL.md:10	добавлена проверка страницы товара Liqui Moly по артикулу (А51)
U027	HISTORY	SKILL.md:10	Позиции AH-25 и AH-29 этой правкой закрываются по содержанию.
U028	HISTORY	SKILL.md:12	Правка 2026-10-13 по стадии Б отбора уроков Архивариуса
U029	HISTORY	SKILL.md:12	добавлен абзац «Отзыв ключа» — удаление credential ключ не отзывает
U030	HISTORY	SKILL.md:12	в «Ozon — общее» — лимит частоты на Client-Id
U031	HISTORY	SKILL.md:12	строка о статусах FBS переписана по спецификации Wildberries (прежняя называла н
U032	HISTORY	SKILL.md:12	добавлены строки о методах ответа на отзывы и о метриках отгрузки по собственном
U033	HISTORY	SKILL.md:12	подраздел pgvector переписан — имя базы, таблицы и пользователя, верное число за
U034	HISTORY	SKILL.md:12	Платформенные факты сверены 2026-10-13 чтением документации; что не перепроверен
U035	IN_ROUTER	router:15	Прочитать в названном файле только нужный раздел
U036	AT_CARRIER	registry/documents.md:176	`[снимок ДД.ММ]` — сверено со строкой файла registry/n8n-map.md
U037	AT_CARRIER	registry/documents.md:176	`[владелец ДД.ММ]` — со слов Андрея
U038	AT_CARRIER	registry/documents.md:176	Строка БЕЗ пометки набита руками, датой не подтверждена и может быть устаревшей.
U039	AT_CARRIER	registry/documents.md:176	непомеченная строка живёт ровно до того дня, когда объект изменится, и никто об 
U040	AT_CARRIER	registry/documents.md:176	причина не заводить здесь ничего, что выводится из объекта
U041	WEAKENED	router:3	перед записью в карточку Wildberries или Ozon
U042	IN_ROUTER	router:3	Самих деталей здесь нет — только адрес файла репозитория second-brain-canon
U043	LOST	-	-
U044	LOST	-	-
U045	LOST	-	-
U046	IN_ROUTER	router:19	## Таблица
U047	WEAKENED	router:37	Живой состав воркфлоу: ID, имя, статус, черновик, расписание, вызовы, документы, типы credential
U048	IN_ROUTER	router:37	формат строк — `projects/n8n-map/PLAN.md`, раздел 4
U049	IN_ROUTER	router:38	Пути вебхуков и признак их аутентификации
U050	IN_ROUTER	router:38	Google Doc N8N_REGISTRY, строки HOOK и HOOKCALL
U051	IN_ROUTER	router:39	Какой credential привязан к какому узлу, активен ли в узле, на какой хост уходит
U052	IN_ROUTER	router:39	книга N8N_CREDENTIALS (ID — `registry/documents.md`)
U053	AT_CARRIER	registry/documents.md:182	Лист «Авто» перезаписывает воркфлоу Credential Inventory qolCVtDpTo2YlnGb по руч
U054	AT_CARRIER	registry/documents.md:182	лист «Ключи» — ручное знание по ID credential
U055	AT_CARRIER	registry/documents.md:182	лист «Правило имени» — правило имени нового ключа «<Сервис> · <Юрлицо> · <R или 
U056	AT_CARRIER	registry/documents.md:182	(R — только чтение, RW — чтение и запись)
U057	AT_CARRIER	registry/documents.md:182	Исключение владельца от 2026-10-06: ключи Wildberries называются с русским слово
U058	AT_CARRIER	registry/documents.md:182	например `WB_Контент_ИП_R`
U059	AT_CARRIER	registry/documents.md:182	токенов Wildberries много, и по общему правилу их не различить
U060	AT_CARRIER	meta/CASES_wb-api.md:46	(projects/deklaration-wb/STATE.md)
U061	AT_CARRIER	registry/documents.md:182	Лист «Правило имени» этого исключения пока не содержит — правит владелец.
U062	AT_CARRIER	registry/documents.md:182	Читать через gsheets-read, диапазон с номером строки (A1:Z1100)
U063	IN_ROUTER	router:40	Как устроен воркфлоу и почему именно так
U064	IN_ROUTER	router:40	адрес — строка PASSPORT в описании воркфлоу
U065	IN_ROUTER	router:41	Механика n8n, корневые причины отказов, протокол правки воркфлоу
U066	IN_ROUTER	router:42	Чтение и запись Google Docs, Sheets, Drive; откуда брать ID воркфлоу
U067	AT_CARRIER	skills/google-drive-docs/SKILL.md:76	ID берётся в момент вызова из строки `registry/n8n-map.md`
U068	IN_ROUTER	router:43	Чтение и запись файлов репозитория канона
U069	IN_ROUTER	router:44	| История инцидентов | `projects/n8n/INCIDENT_LOG.md` |
U070	AT_CARRIER	projects/n8n/PLAN.md:52	Per-workflow таблиц здесь нет
U071	AT_CARRIER	projects/n8n/PLAN.md:52	они были третьим источником истины и дважды разошлись с объектом
U072	AT_CARRIER	projects/n8n/PLAN.md:52	устаревшие пометки на `ss0QkY9V8YEMHf2B` и `LM_DECL_MASTER` пришлось исправлять 
U073	AT_CARRIER	projects/n8n/PLAN.md:52	Не заводить заново.
U074	IN_ROUTER	router:24	(«1. Инструменты Drive и Docs»)
U075	AT_CARRIER	projects/n8n/PLAN.md:54	живут в google-drive-docs: таблица быстрого выбора инструмента (§1), разделы 3.1
U076	AT_CARRIER	projects/n8n/PLAN.md:54	их ID — по правилу §1 того же Skill, из строки `registry/n8n-map.md` по имени во
U077	AT_CARRIER	projects/n8n/PLAN.md:54	Здесь они не повторяются намеренно.
U078	AT_CARRIER	projects/n8n/PLAN.md:54	Копия этого списка была бы третьим источником истины
U079	AT_CARRIER	projects/n8n/PLAN.md:54	паспорт Registry Sync до 26.09.2026 называл получателем перезаписи заархивирован
U080	AT_CARRIER	projects/n8n/PLAN.md:56	`Hpy9TCly6LKCjlqf` — GDrive Share File, активен [снимок 26.09]
U081	AT_CARRIER	projects/n8n/PLAN.md:56	Вход POST `{fileId, emailAddress?, role?}` → permissions.create плюс read-back.
U082	AT_CARRIER	projects/n8n/PLAN.md:56	Создан 11.08.2026.
U083	AT_CARRIER	projects/n8n/PLAN.md:57	ходит под сервисным аккаунтом и не может выдать файлу самое первое разрешение
U084	AT_CARRIER	projects/n8n/PLAN.md:57	permissions.create отвечает 404
U085	AT_CARRIER	projects/n8n/PLAN.md:57	Годится, только когда доступ хотя бы на чтение уже есть.
U086	AT_CARRIER	projects/n8n/PLAN.md:59	`kJTXJuHQAv1go52t` — Claude → Obsidian, активен [снимок 26.09]
U087	AT_CARRIER	projects/n8n/PLAN.md:61	Звать нельзя, через MCP они и не видны
U088	AT_CARRIER	projects/n8n/PLAN.md:61	список нужен, чтобы узнавать их ID в старых текстах и паспортах
U089	AT_CARRIER	projects/n8n/PLAN.md:65	`CELGBmo7vQFF1Ej7` | gdocs-append v1
U090	AT_CARRIER	projects/n8n/PLAN.md:65	заменён на `YfzWwu1VmIUCbUu0` 22.07.2026
U091	AT_CARRIER	projects/n8n/PLAN.md:66	`qWk65OyxaoAu4jAl` | gdocs-replace v1
U092	AT_CARRIER	projects/n8n/PLAN.md:66	расхождение обнаружено 21.07.2026
U093	AT_CARRIER	projects/n8n/PLAN.md:67	`OYIhTm8h2ABMHQUW` | gdocs-overwrite v1
U094	AT_CARRIER	projects/n8n/PLAN.md:67	30.07.2026 обнулил SYS_INDEX — разбор в `projects/n8n/INCIDENT_LOG.md`
U095	IN_ROUTER	router:23	(«2. Книги Google Sheets и документы», 2.1–2.3)
U096	AT_CARRIER	registry/documents.md:184	Снимок отвечает строками D на вопрос «какие воркфлоу и какими узлами трогают док
U097	AT_CARRIER	registry/documents.md:184	На обратный вопрос — «какой ID у книги, которую человек зовёт Price Master»
U098	AT_CARRIER	registry/documents.md:184	поэтому ID отсюда не убираются
U099	IN_ROUTER	router:23	(«2. Книги Google Sheets и документы», 2.1–2.3)
U100	AT_CARRIER	registry/documents.md:186	**Reviews Queue** — `1mgtcD2wSm_-8hqfpv3v883KE34-Smy-kFxHvt6zMXj4`
U101	AT_CARRIER	registry/documents.md:186	листы `ozon_reviews_queue` и `ozon_qa_queue`; 20 узлов [снимок 26.09]
U102	AT_CARRIER	registry/documents.md:187	**Price Master** — `1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk`
U103	AT_CARRIER	registry/documents.md:187	листы `Artikel` и `CURRENT`; 8 узлов [снимок 26.09]
U104	AT_CARRIER	registry/documents.md:188	**SKU_Artikel_Map** — `1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU`
U105	AT_CARRIER	registry/documents.md:188	листы `SKU_Artikel_Map` и `MASTER_MAP`
U106	AT_CARRIER	registry/documents.md:188	MASTER_MAP — таблица соответствия `sku + lm_id + ozon_sku + wb_nm_id`
U107	AT_CARRIER	registry/documents.md:188	это ЛИСТ внутри этой же книги, а не отдельный файл: узел `16_Write_WB_nmID` пише
U108	AT_CARRIER	registry/documents.md:188	Источником истины MASTER_MAP НЕ является: это снимок, собранный скриптом 19.06.2
U109	AT_CARRIER	registry/documents.md:188	у нашего артикула 1908 в MASTER_MAP стоит `ozon_sku` = 0, а в Price Master, лист
U110	AT_CARRIER	registry/documents.md:188	Живой источник соответствия артикулов — **Price Master, лист `Artikel`**.
U111	AT_CARRIER	registry/documents.md:188	По решению владельца 2026-10-02 MASTER_MAP выводится из употребления после того,
U112	AT_CARRIER	registry/documents.md:188	labs/ozon-ue/t-master-map-ozon-sku.md, запись 2026-10-03; шаг 5 задачи labs/ozon
U113	HISTORY	SKILL.md:72	ИСТОРИЯ ДИАГНОЗА: прежняя редакция называла MASTER_MAP «единым кросс-маппингом»
U114	AT_CARRIER	registry/documents.md:188	у нашего артикула 1908 в MASTER_MAP стоит `ozon_sku` = 0
U115	AT_CARRIER	registry/documents.md:190	**LM_DECL_MASTER** — `1PO7vNyoY16tYqpU_KB5xuK4aSAbOU7YW_MM0scg5ksY`
U116	AT_CARRIER	registry/documents.md:190	13 узлов; там, где узел раскрывает имя листа, это `LM_DECL` [снимок 26.09]
U117	AT_CARRIER	registry/documents.md:190	Лист `Decl_Monitor` — дашборд со светофором; ни одним узлом не трогается
U118	HISTORY	SKILL.md:75	Прежняя редакция этого файла называла рабочим листом именно `Decl_Monitor`
U119	IN_ROUTER	router:23	(«2. Книги Google Sheets и документы», 2.1–2.3)
U120	AT_CARRIER	registry/documents.md:192	Двадцать девять книг из сорока одной, которые трогают воркфлоу, не названы нигде
U121	AT_CARRIER	registry/documents.md:192	Ниже те, что используются тремя и более узлами
U122	AT_CARRIER	registry/documents.md:192	кто знает имя, дописывает его сюда
U123	AT_CARRIER	registry/documents.md:192	это долг, а не факт
U124	AT_CARRIER	registry/documents.md:196	`1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4` | `sales_raw_operations`
U125	AT_CARRIER	registry/documents.md:197	`1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ` | `wb_fbs_orders_tracking`
U126	AT_CARRIER	registry/documents.md:198	`1JwV7bbfLLxztE7gRrUEOUIvUk-xCOcwDkT88RA5bHPg` | `wb_reviews_archive`
U127	AT_CARRIER	registry/documents.md:199	`1XMy8XsF4tIyiPIhiW2dAt8Sihbsy4xQOXWQhjCJEHyE` | `kb_motor_oil`
U128	AT_CARRIER	registry/documents.md:200	`1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4` | `SKU_Artikel`
U129	AT_CARRIER	registry/documents.md:201	`1AhgaspMQl3wLsVT7Iub0d195r8DwwUarhQAWwjBO8xE` | `wb_fbs_params`
U130	AT_CARRIER	registry/documents.md:202	`14QMHYMM4mZRnnq1wHQA4_SA8ZnOeE1xcVJDL2h9h1Pk` | имя листа узлы не раскрывают
U131	AT_CARRIER	registry/documents.md:203	`17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU` | `Акт.цена`
U132	AT_CARRIER	registry/documents.md:204	`1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI` | `dashboard`
U133	AT_CARRIER	registry/documents.md:205	`1eujHu87IO0IlngLX164_O81LxPI5NNpq9S47E8anVSo` | имя листа узлы не раскрывают; з
U134	AT_CARRIER	registry/documents.md:206	`1gPjWlhld9LAzGScEU9l63OGfcXK48dujYX1A9Uh6gBk` | имя листа
U135	AT_CARRIER	registry/documents.md:207	`1sPD5SAFCTygzUaEPg8RKRPHQyc0HCMIK-aMpnXqYu3k` | имя листа
U136	AT_CARRIER	registry/documents.md:208	`11j0yKZ0FvE9EbZiTzCStEACsgecliaElVccpUixmQcQ` | имя листа
U137	AT_CARRIER	registry/documents.md:209	`1cK5dues1ffnUdy6UGCDHiMzxp1ZucdyvawS5Dvx-o3M` | имя листа
U138	AT_CARRIER	registry/documents.md:211	Все строки таблицы — [снимок 26.09].
U139	AT_CARRIER	registry/documents.md:211	Полный список из сорока одного документа с их узлами достаётся из снимка одной к
U140	PROPOSED_REMOVAL	proposed_removals.md:2	SKILL.md line 100 (ID in registry/documents.md damaged)
U141	PROPOSED_REMOVAL	proposed_removals.md:2	SKILL.md line 100 (ID in registry/documents.md damaged)
U142	PROPOSED_REMOVAL	proposed_removals.md:2	SKILL.md line 100 (ID in registry/documents.md damaged)
U143	IN_ROUTER	router:23	проверка ID Google по длине
U144	AT_CARRIER	registry/documents.md:213	ID попадает в канон только из объекта или из поиска этой же сессии — не по памят
U145	AT_CARRIER	registry/documents.md:213	перепечатанная руками копия уже повредилась (строка 35 выше)
U146	AT_CARRIER	registry/documents.md:213	Дешёвая проверка перед записью любого ID Google — длина
U147	AT_CARRIER	registry/documents.md:214	документ Google Docs и книга Google Sheets — 44 знака
U148	AT_CARRIER	registry/documents.md:215	папка Google Drive — 33 знака
U149	AT_CARRIER	registry/documents.md:217	Другая длина — ID повреждён или это не ID Google
U150	AT_CARRIER	registry/documents.md:217	ID Claude Project длиной 36 знаков с дефисами
U151	AT_CARRIER	registry/documents.md:217	Длина ловит пропуск и лишний знак, но не замену одного знака другим; сверка по о
U152	AT_CARRIER	registry/documents.md:217	Происхождение: projects/n8n-map/PLAN.md, зонд Z-10; projects/deklaration-ozon/LO
U153	IN_ROUTER	router:25	(«3. Ozon — общее»
U154	AT_CARRIER	meta/CASES_ozon-api.md:13	Ozon кладёт ошибку в тело ответа при коде HTTP 200.
U155	AT_CARRIER	meta/CASES_ozon-api.md:13	`{"code":9,"message":"obsolete method cannot be used"}` у отключённого `/v3/fina
U156	AT_CARRIER	meta/CASES_ozon-api.md:13	исполнение при этом success с нулём строк
U157	AT_CARRIER	meta/CASES_ozon-api.md:13	`PermissionDenied` «not available with existing subscription» на публикации отве
U158	AT_CARRIER	meta/CASES_ozon-api.md:13	тело ответа проверяется на поля `code` и `message`, а итог — по объекту
U159	AT_CARRIER	meta/CASES_ozon-api.md:13	Общее правило «результат по объекту, не по статусу» — корень R4
U160	AT_CARRIER	meta/CASES_ozon-api.md:14	Лимит частоты Seller API считается на Client-Id, а не на воркфлоу
U161	AT_CARRIER	meta/CASES_ozon-api.md:14	у второго кабинета (другое юрлицо) свой Client-Id, значит и свой счётчик
U162	AT_CARRIER	meta/CASES_ozon-api.md:14	Общий лимит — 50 запросов в секунду на все методы с одного Client-Id, с 22.05.20
U163	AT_CARRIER	meta/CASES_ozon-api.md:14	превышение даёт 429 «You have reached request rate limit per second»
U164	AT_CARRIER	meta/CASES_ozon-api.md:14	Источник — официальный канал новостей Seller API в Telegram (t.me/s/OzonSellerAP
U165	AT_CARRIER	meta/CASES_ozon-api.md:14	у отдельных методов свой, более низкий потолок, и он назван в тексте ответа 429
U166	AT_CARRIER	meta/CASES_ozon-api.md:14	`/v1/analytics/data` в августе 2026 отвечал «rate limit exceeded for `seller-api
U167	AT_CARRIER	meta/CASES_ozon-api.md:14	С 24.02.2026 операции с товарами (`/v3/product/import`, `/v1/product/update/offe
U168	AT_CARRIER	meta/CASES_ozon-api.md:14	ограничены 30 000 товаров в минуту на все четыре метода вместе
U169	AT_CARRIER	meta/CASES_ozon-api.md:14	запрос, в котором товаров больше остатка, отклоняется целиком с текстом «You hav
U170	AT_CARRIER	meta/CASES_ozon-api.md:14	пересказ avoshop.ru от 18.02.2026, первоисточник Ozon не прочитан
U171	AT_CARRIER	meta/CASES_ozon-api.md:14	429 при одном запросе за прогон — не дефект этого воркфлоу и паузой внутри него 
U172	AT_CARRIER	meta/CASES_ozon-api.md:14	диагностика начинается с текста ошибки (какой лимит назван) и с суммы запросов в
U173	AT_CARRIER	meta/CASES_ozon-api.md:14	пауза между пакетами внутри воркфлоу уменьшает только его собственный вклад
U174	AT_CARRIER	meta/CASES_ozon-api.md:14	1 случай, 2026-08-25 — шесть из шести плановых прогонов OZON RAW Konversion Sync
U175	AT_CARRIER	meta/CASES_ozon-api.md:14	на том же Client-Id было ещё 12 активных воркфлоу
U176	AT_CARRIER	meta/CASES_ozon-api.md:14	(отчёт REPORT_H-25.08-01, раздел 2, ID — registry/documents.md; урок У-77 журнал
U177	AT_CARRIER	meta/CASES_ozon-api.md:16	Поля `pros`, `cons`, `text` раздельные; статус `rejected` возможен.
U178	AT_CARRIER	meta/CASES_ozon-api.md:17	Публикация отзыва: POST `/v1/review/comment/create`, задержка 4 секунды между за
U179	AT_CARRIER	meta/CASES_ozon-api.md:18	Маппинг `operation_type` → узел `06C_Map_Operation_Category`, обычный объект JS.
U180	AT_CARRIER	meta/CASES_ozon-api.md:18	Новый тип добавляется в словарь; неизвестные дают `'Не классифицировано: ' + opT
U181	AT_CARRIER	meta/CASES_ozon-api.md:19	Эндпоинты вопросов идут БЕЗ `/product/`: POST `/v1/question/list`, `/v1/question
U182	AT_CARRIER	meta/CASES_ozon-api.md:20	Публичный ответ на карточке закрыт без тарифа Premium Plus (порядка 25 тысяч руб
U183	AT_CARRIER	meta/CASES_ozon-api.md:20	ответ через чат `/v3/chat/` виден только самому покупателю
U184	AT_CARRIER	meta/CASES_ozon-api.md:21	Вебхука `TYPE_NEW_QUESTION` не существует.
U185	AT_CARRIER	meta/CASES_ozon-api.md:22	Стоп пагинации `/v1/review/list` — любое из трёх: пустой массив, `last_id` не из
U186	AT_CARRIER	meta/CASES_ozon-api.md:23	Встроенная пагинация HTTP-узла для транзакций: `paginationCompleteWhen: other`
U187	AT_CARRIER	meta/CASES_ozon-api.md:23	`completeExpression: ={{ $response.body.result.operations.length < 1000 }}`
U188	AT_CARRIER	meta/CASES_ozon-api.md:24	Ограничение частоты примерно один запрос в секунду: Items per Batch = 1, Batch I
U189	AT_CARRIER	meta/CASES_ozon-api.md:28	POST `/v1/finance/accrual/by-day`, тело `{date, last_id}` → ответ `{accruals:[..
U190	AT_CARRIER	meta/CASES_ozon-api.md:28	Пагинация останавливается, когда `last_id` пришёл пустой строкой, НЕ по длине ма
U191	AT_CARRIER	meta/CASES_ozon-api.md:29	`accrued_category` принимает `POSTING`, `ITEM`, `NON_ITEM`; у каждой своя вложен
U192	AT_CARRIER	meta/CASES_ozon-api.md:30	Наблюдаемая формула нэттинга: `sale_amount + sale_commission + delivery.total_ac
U193	AT_CARRIER	meta/CASES_ozon-api.md:31	`container_fees` ни разу не приходило непустым; статус поля неизвестен.
U194	AT_CARRIER	meta/CASES_ozon-api.md:32	Ловушка совместимости с `/v3/posting/fbs/get` (вход `{posting_number}`)
U195	AT_CARRIER	meta/CASES_ozon-api.md:32	валидный `posting_number` даёт только `unit_number` из записей с `accrued_catego
U196	AT_CARRIER	meta/CASES_ozon-api.md:32	Взятый из `ITEM` или `NON_ITEM` даёт 404 в 85–91 проценте случаев.
U197	AT_CARRIER	skills/n8n-engineering-manual/SKILL.md:120	`raw_key` — композитный ключ строки RAW, свой на каждый источник
U198	AT_CARRIER	meta/CASES_ozon-api.md:36	Ozon, транзакции — `business_date|operation_id`
U199	AT_CARRIER	meta/CASES_ozon-api.md:37	Ozon, начисления — `accrual_id`
U200	AT_CARRIER	projects/wb-ue/STATE.md:52	`[business_date, report_id, rrd_id].join('_')`
U201	AT_CARRIER	projects/wb-ue/STATE.md:52	Формула сейчас одинакова в узле `06_Add_RAW_Key` обоих воркфлоу
U202	AT_CARRIER	projects/wb-ue/STATE.md:46	History Load (`Iis5dlRS1GWZqQXD`)
U203	PROPOSED_REMOVAL	proposed_removals.md:3	SKILL.md line 140, sentences "Решено убрать из ключа report_id
U204	AT_CARRIER	projects/wb-ue/STATE.md:52	`report_id` синтетический (пример из прогона 67799: `97472420260914`)
U205	AT_CARRIER	projects/wb-ue/STATE.md:52	одна и та же строка WB в дневной и недельной выгрузке получает разные `raw_key`
U206	AT_CARRIER	projects/wb-ue/STATE.md:52	уникальность проверена на всех 87228 строках, коллизий ноль
U207	PROPOSED_REMOVAL	proposed_removals.md:3	Когда внесут, эту строку переписать
U208	HISTORY	SKILL.md:141	прежняя редакция давала формулу `rrd_id|sale_dt|report_id`; опровергнуто чтением
U209	IN_ROUTER	router:29	почему форматы ключей разные — Skill `n8n-engineering-manual`, раздел 3
U210	IN_ROUTER	router:28	Wildberries: запись карточки, декларация в карточке, маркировка, форматы дат
U211	IN_ROUTER	router:28	прежний файл `references/cards-and-declarations.md`
U212	AT_CARRIER	meta/CASES_wb-api.md:13	Ответ на вопрос: PATCH `/api/v1/questions`, тело `{id, answer:{text}, state:"wbR
U213	AT_CARRIER	meta/CASES_wb-api.md:13	Поле `state` обязательно — без него ответ не появляется на сайте.
U214	AT_CARRIER	meta/CASES_wb-api.md:14	Отзывы и вопросы — оба API на `feedbacks-api.wildberries.ru`, токен категории «В
U215	AT_CARRIER	meta/CASES_wb-api.md:14	Credential — Header Auth, заголовок `Authorization`, значение — токен без слова 
U216	AT_CARRIER	meta/CASES_wb-api.md:14	у Finance API ниже значение с `Bearer`, и оно тоже работает
U217	AT_CARRIER	meta/CASES_wb-api.md:14	Первый ответ на отзыв — POST `/api/v1/feedbacks/answer`, тело `{id, text}`, отве
U218	AT_CARRIER	meta/CASES_wb-api.md:14	Правка уже опубликованного ответа — PATCH `/api/v1/feedbacks/answer` с тем же те
U219	AT_CARRIER	meta/CASES_wb-api.md:14	Адрес `/api/v1/feedbacks` принимает только чтение: PATCH на него даёт 405 с заго
U220	AT_CARRIER	meta/CASES_wb-api.md:14	Список отзывов — GET `/api/v1/feedbacks`, обязательные параметры `isAnswered`, `
U221	AT_CARRIER	meta/CASES_wb-api.md:14	воркфлоу WB Reviews Intake берёт `take` = 100 и `skip` = номер страницы × 100 и 
U222	AT_CARRIER	meta/CASES_wb-api.md:14	Отвеченные отзывы и вопросы Intake читает только за последние 60 дней (`dateFrom
U223	AT_CARRIER	meta/CASES_wb-api.md:14	без окна узел сборки отвеченных падал по памяти
U224	AT_CARRIER	meta/CASES_wb-api.md:14	Лимит частоты — 3 запроса в секунду, всплеск 6, на один аккаунт продавца на все 
U225	AT_CARRIER	meta/CASES_wb-api.md:14	его делят все воркфлоу отзывов и вопросов
U226	AT_CARRIER	meta/CASES_wb-api.md:14	Методы и лимит сверены 2026-10-13 со спецификацией Wildberries `09-communication
U227	AT_CARRIER	meta/CASES_wb-api.md:14	2026-06-02 при запуске Intake и Publication PATCH на `/feedbacks` дал 405 и был 
U228	AT_CARRIER	meta/CASES_wb-api.md:14	узел `04A_Rollback_Review` с 2026-06-02 бил PATCH в `/api/v1/feedbacks` и получа
U229	AT_CARRIER	meta/CASES_wb-api.md:14	(WB_REVIEWS_INDEX, строки 927, 476, 1075, 1080; projects/wb-reviews/NOT_TAKEN.md
U230	AT_CARRIER	projects/wb-reviews/PLAN.md:24	WB допускает РОВНО ОДНУ правку опубликованного ответа
U231	WEAKENED	projects/wb-reviews/PLAN.md:26	Rollback может проверять editable перед PATCH и не тратить правку впустую
U232	AT_CARRIER	projects/wb-reviews/PLAN.md:26	body.data.answer = {text, state, editable}
U233	AT_CARRIER	projects/wb-reviews/PLAN.md:25	WB вернул 204 No Content — то есть УСПЕХ на несуществующий отзыв
U234	AT_CARRIER	projects/wb-reviews/PLAN.md:29	Заголовков x-ratelimit-limit и x-ratelimit-reset WB не отдаёт
U235	IN_ROUTER	router:27	правка ответа на отзыв и поле `editable` — `projects/wb-reviews/PLAN.md`
U236	AT_CARRIER	meta/CASES_wb-api.md:16	`/orders/status`: поле называется `orders`, не `orderIds`; тело `{orders:[...]}`
U237	AT_CARRIER	meta/CASES_wb-api.md:17	`supplierStatus=confirm` включает и отгруженные заказы — фильтровать дополнитель
U238	AT_CARRIER	meta/CASES_wb-api.md:18	Пагинация статистики: курсор `rrdid`, между страницами узел Wait на 70 секунд из
U239	AT_CARRIER	meta/CASES_wb-api.md:19	Finance API v1: POST `finance-api.wildberries.ru/api/finance/v1/sales-reports/de
U240	AT_CARRIER	meta/CASES_wb-api.md:19	Даты с зоной: `2026-05-26T00:00:00+03:00`.
U241	AT_CARRIER	meta/CASES_wb-api.md:19	Пагинация: `rrdId` в теле, старт 0, до ответа 204.
U242	AT_CARRIER	meta/CASES_wb-api.md:19	Денежные поля приходят строками.
U243	AT_CARRIER	meta/CASES_wb-api.md:19	Credential — Header Auth, имя `Authorization`, значение `Bearer TOKEN`.
U244	AT_CARRIER	meta/CASES_wb-api.md:20	Знак строки финансового отчёта задаёт поле `doc_type` («Возврат»), а не название
U245	AT_CARRIER	meta/CASES_wb-api.md:20	при возврате `revenue` и `for_pay` положительные
U246	AT_CARRIER	meta/CASES_wb-api.md:20	(projects/wb-ue/LOG.md, Р-11)
U247	AT_CARRIER	meta/CASES_wb-api.md:20	Wildberries молча переименовывает операции: с 01.09.2026 «Логистика» стала «Дост
U248	AT_CARRIER	meta/CASES_wb-api.md:20	неизвестное название падает в категорию «прочее» и пропадает из витрины
U249	AT_CARRIER	meta/CASES_wb-api.md:20	Тождество выплаты: `forPay = retailAmount − vw − vwNds − acquiringFee − ppvzRewa
U250	AT_CARRIER	meta/CASES_wb-api.md:20	выполнено на всех 289 продажах недели 14–20.09.2026 (там же, Р-33)
U251	AT_CARRIER	meta/CASES_wb-api.md:20	`commissionPercent` — номинал тарифа: в выплате он не участвует, и вычитать коми
U252	AT_CARRIER	meta/CASES_wb-api.md:21	Домены-ловушки, которые НЕ работают: `statistics-api` (старый v5), `common-api`,
U253	AT_CARRIER	meta/CASES_wb-api.md:22	Семантика статусов FBS (POST `/api/v3/orders/status`).
U254	AT_CARRIER	meta/CASES_wb-api.md:22	`supplierStatus` меняет действие продавца: `new` — новое задание, `confirm` — на
U255	AT_CARRIER	meta/CASES_wb-api.md:22	`wbStatus` — статус системы Wildberries: рабочие `waiting` (в работе), `sorted` 
U256	AT_CARRIER	meta/CASES_wb-api.md:22	отмены — `canceled` (отмена сборочного задания), `declined_by_client` (покупател
U257	AT_CARRIER	meta/CASES_wb-api.md:22	Отмена покупателем или самим Wildberries видна только в `wbStatus`, а `supplierS
U258	AT_CARRIER	meta/CASES_wb-api.md:22	Детект отмены нужен отдельной ветвью по `wbStatus` со ВСЕМИ значениями отмены из
U259	AT_CARRIER	meta/CASES_wb-api.md:22	иначе висящий хвост вечно блокирует переход «поставка отгружена»
U260	AT_CARRIER	meta/CASES_wb-api.md:22	Значение, которого нет ни среди отмен, ни среди рабочих статусов, — сигнал в отч
U261	AT_CARRIER	meta/CASES_wb-api.md:22	новый статус Wildberries иначе уходит не в ту ветвь
U262	AT_CARRIER	meta/CASES_wb-api.md:22	Значения сверены 2026-10-13 со спецификацией Wildberries `03-orders-fbs.yaml`
U263	AT_CARRIER	meta/CASES_wb-api.md:22	2026-06-29 около двадцати отказов `declined_by_client` и `canceled_by_client` ви
U264	AT_CARRIER	meta/CASES_wb-api.md:22	ветку отмен в Order Close v2 (`DM26WhTJyCV0DhkP`) добавили 2026-06-30
U265	AT_CARRIER	meta/CASES_wb-api.md:22	2026-07-06 заказ 5271100427, отменённый самим Wildberries, тем же путём держал п
U266	AT_CARRIER	meta/CASES_wb-api.md:22	(projects/wb-logistics/LOG.md, записи Р-75, Р-83 и Р-89; урок У-120 журнала proj
U267	HISTORY	SKILL.md:157	ИСТОРИЯ ДИАГНОЗА: прежняя редакция называла значение `declined` — в спецификации
U268	HISTORY	SKILL.md:157	Запись 2026-07-06 называет отмены Wildberries «canceled/cancel»: `canceled` — зн
U269	AT_CARRIER	meta/CASES_wb-api.md:24	Времени приёмки на уровне заказа не существует: `/orders/status` отдаёт только т
U270	AT_CARRIER	meta/CASES_wb-api.md:24	Время приёмки есть только на уровне поставки: `scanDt` в GET `/supplies` плюс `/
U271	AT_CARRIER	projects/wb-logistics/PLAN.md:76	Метрики «отгружено», «среднее время до отгрузки» и очередь «в работе» строятся п
U272	AT_CARRIER	projects/wb-logistics/PLAN.md:76	(значения `new`, `in_transit`, `shipped`, `cancelled`, projects/wb-logistics/STA
U273	AT_CARRIER	projects/wb-logistics/PLAN.md:76	а не по живому статусу Wildberries и не по исчезновению заказа из выборки API
U274	AT_CARRIER	projects/wb-logistics/PLAN.md:76	прогон Order Close 14988 29.06.2026 в 22:05 видел ноль заказов `complete` через 
U275	AT_CARRIER	projects/wb-logistics/PLAN.md:76	отставание наблюдалось до суток (наблюдение 2026-06-29, не перепроверено
U276	AT_CARRIER	projects/wb-logistics/PLAN.md:76	Счёт «отгружено = пропало из выборки» молча залипает около нуля
U277	AT_CARRIER	projects/wb-logistics/PLAN.md:76	Приёмку Wildberries считать по `scanDt` поставки
U278	AT_CARRIER	projects/wb-logistics/PLAN.md:76	решение Андрея 2026-10-04
U279	AT_CARRIER	projects/wb-logistics/PLAN.md:76	2026-06-30 — Evening Report показал «Отгружено 0» при 72 отгруженных по Order Cl
U280	AT_CARRIER	projects/wb-logistics/PLAN.md:76	(projects/wb-logistics/LOG.md, записи Р-84 и Р-85
U281	AT_CARRIER	projects/wb-reviews/STATE.md:31	(сейчас ["QA_OIL_MATCH","QA_SPEC"])
U282	AT_CARRIER	projects/wb-logistics/PLAN.md:78	Личный Telegram Андрея: `chatId` захардкожен, `6054723832`.
U283	AT_CARRIER	projects/wb-logistics/PLAN.md:78	Группа логистики: `chat_id = -1004269834495`.
U284	AT_CARRIER	projects/n8n-map/PLAN.md:193	Права ключей Ozon — методом POST /v1/roles (роли и expires_at)
U285	AT_CARRIER	projects/n8n-map/PLAN.md:193	категории ключей WB — GET /ping по доменам категорий
U286	AT_CARRIER	projects/n8n-map/PLAN.md:193	common-api отвечает 200 любому ключу и категорией не считается
U287	AT_CARRIER	projects/n8n-map/PLAN.md:193	право записи WB — только из кабинета или из факта применённой записи
U288	AT_CARRIER	skills/n8n-engineering-manual/references/write.md:33	Право ключа проверяется до боевого режима, а не в нём.
U289	AT_CARRIER	meta/CASES_wb-api.md:28	Второй кабинет (другое юрлицо) — свой ключ: ключ основного кабинета на чужой каб
U290	AT_CARRIER	meta/CASES_wb-api.md:29	Источники: projects/n8n-map/PLAN.md, фаза Ф5; projects/deklaration-ozon/LOG.md, 
U291	AT_CARRIER	meta/CASES_wb-api.md:29	Где записаны права каждого ключа — лист «Ключи» книги N8N_CREDENTIALS (таблица в
U292	AT_CARRIER	meta/CASES_external-access.md:9	Две точки, откуда сессия может обратиться наружу, видят разное: сервер n8n (Герм
U293	AT_CARRIER	meta/CASES_external-access.md:9	Факты API, которые нельзя прочитать в документации, сначала снимает зонд — време
U294	AT_CARRIER	meta/CASES_external-access.md:13	`pub.fsa.gov.ru` (реестр деклараций) | таймаут 20 секунд на корне, API и входе (
U295	AT_CARRIER	meta/CASES_external-access.md:13	| не проверялось |
U296	AT_CARRIER	meta/CASES_external-access.md:14	`mobile.api.crpt.ru` («Честный знак») | 451 — геоблокировка; через российский пр
U297	AT_CARRIER	meta/CASES_external-access.md:15	`docs.ozon.ru`, swagger.json Ozon | таймаут 30–60 секунд (исполнения 73350, зонд
U298	AT_CARRIER	meta/CASES_external-access.md:15	| прокси 403 |
U299	AT_CARRIER	meta/CASES_external-access.md:16	swagger Wildberries | yaml — 404, страница — 498
U300	AT_CARRIER	meta/CASES_external-access.md:17	`dev.wildberries.ru` (документация) | — | не открылась
U301	AT_CARRIER	meta/CASES_external-access.md:18	публичный API своего инстанса n8n (`/api/v1/`) | доступен воркфлоу по `localhost
U302	AT_CARRIER	meta/CASES_external-access.md:18	прокси 403 (зонд Z-12) — такие факты снимает воркфлоу на сервере
U303	AT_CARRIER	meta/CASES_external-access.md:20	Источники: projects/deklaration-ozon/LOG.md, Т-1, Т-4, Т-10, Р-21; projects/card
U304	AT_CARRIER	meta/CASES_external-access.md:20	Что недоступно сегодня, может открыться завтра: перед тем как строить обход, пов
U305	AT_CARRIER	projects/wb-reviews/PLAN.md:52	База `liquimoly_kb` в PostgreSQL 16 с расширением pgvector 0.8.2, хост `postgres
U306	AT_CARRIER	projects/wb-reviews/PLAN.md:52	(WB_REVIEWS_INDEX, строки 962 и 1803)
U307	AT_CARRIER	projects/wb-reviews/PLAN.md:52	Читатель — WB Reviews Response (RAG, строка подраздела «Wildberries»).
U308	AT_CARRIER	projects/wb-reviews/PLAN.md:52	Направление «Допуски OEM» проекта wb-reviews Андрей прекратил 2026-10-12
U309	AT_CARRIER	projects/wb-reviews/PLAN.md:52	база знаний к нему не сводится и живёт, пока Response её читает
U310	AT_CARRIER	projects/wb-reviews/PLAN.md:54	`motor_oil` — 182 записи, загружены полностью 2026-07-29 (исполнение 33576)
U311	AT_CARRIER	projects/wb-reviews/PLAN.md:54	плюс одна осиротевшая строка, которая останется навсегда: её артикула нет в лист
U312	AT_CARRIER	projects/wb-reviews/PLAN.md:54	`auto_chemistry` — 146, полная; `transmission_oil` — 42, полная; `antifreeze` — 
U313	AT_CARRIER	projects/wb-reviews/PLAN.md:54	Числа — на 2026-07-29, не перепроверены.
U314	HISTORY	SKILL.md:187	прежняя редакция писала «`motor_oil` — около 183 записей, загрузка неполная»; оп
U315	AT_CARRIER	projects/wb-reviews/PLAN.md:56	**Правка текстового ключа порождает сироту.**
U316	AT_CARRIER	projects/wb-reviews/PLAN.md:56	Загрузчики пишут в `products_kb` по ключу `article_number` — это название товара
U317	AT_CARRIER	projects/wb-reviews/PLAN.md:56	Исправленный в листе-источнике текст ключа (лишний пробел, кириллическая «Т» вме
U318	AT_CARRIER	projects/wb-reviews/PLAN.md:56	ни один перезалив её не трогает, и RAG продолжает находить устаревшие данные
U319	AT_CARRIER	projects/wb-reviews/PLAN.md:56	Порядок до и после перезалива: сравнить число строк категории в базе (SELECT COU
U320	AT_CARRIER	projects/wb-reviews/PLAN.md:56	разницу выписать поимённо — списком значений `article_number`, а не числом; DELE
U321	AT_CARRIER	projects/wb-reviews/PLAN.md:56	затем чтение обратно — COUNT и отсутствие удалённых значений
U322	AT_CARRIER	projects/wb-reviews/PLAN.md:56	Строку, про которую нельзя доказать, что это мусор базы, а не ошибка источника, 
U323	AT_CARRIER	projects/wb-reviews/PLAN.md:56	1 случай, 2026-07-29 — перед перезаливом `motor_oil` вместо равенства 182 = 182 
U324	AT_CARRIER	projects/wb-reviews/PLAN.md:56	список удалённых сохранён в коде воркфлоу KB Snapshot — Motor Oil (one-off) `Ind
U325	AT_CARRIER	projects/wb-reviews/PLAN.md:56	(WB_REVIEWS_INDEX, строки 323 и 368;
U326	AT_CARRIER	projects/wb-reviews/PLAN.md:58	У `kb_user` нет права CREATE TABLE в схеме `public`
U327	AT_CARRIER	projects/wb-reviews/PLAN.md:58	менять структуру базы (DDL — создание и изменение таблиц, индексов) воркфлоу не 
U328	AT_CARRIER	projects/wb-reviews/PLAN.md:58	Наблюдение 2026-06-27, не перепроверено (WB_REVIEWS_INDEX, строка 1102; урок У-1
U329	AT_CARRIER	projects/wb-reviews/PLAN.md:58	Согласуется с поведением PostgreSQL начиная с версии 15: право CREATE на схему `
U330	AT_CARRIER	projects/wb-reviews/PLAN.md:60	Модель эмбеддингов — `voyage-3`, размерность 1024.
U331	AT_CARRIER	projects/wb-reviews/PLAN.md:60	НЕ `voyage-3-lite` с размерностью 512: ошибка необратима и стоит переиндексации 
U332	AT_CARRIER	projects/wb-reviews/PLAN.md:60	То же предупреждение стоит в n8n-engineering-manual разделом 1 — единственный на
U333	AT_CARRIER	meta/DECLARATION_SCAN.md:35	«LM_DECL — Scan» `vKjqExap1mJjM6Ap` — опубликован
U334	IN_ROUTER	router:33	`meta/DECLARATION_SCAN.md`
U335	AT_CARRIER	projects/deklaration-ozon/NOT_TAKEN.md:11	Конвейер PDF снят 2026-09-30 (`LOG.md`, Р-2)
U336	AT_CARRIER	projects/deklaration-ozon/NOT_TAKEN.md:11	Если конвейер понадобится снова
U337	AT_CARRIER	skills/google-drive-docs/references/sheets.md:140	`Drive.Files.insert(metadata, blob, {convert:true})`
U338	AT_CARRIER	skills/google-drive-docs/references/sheets.md:140	версия 3 для конвертации не работает
U339	IN_ROUTER	router:33	`projects/deklaration-ozon/NOT_TAKEN.md`
U340	AT_CARRIER	meta/DECLARATION_SCAN.md:108	Что раньше переносило выписки из DECL_PDF_INBOX в DECL_PDF_ARCHIVE
U341	AT_CARRIER	skills/n8n-engineering-manual/references/engine.md:100	не принимается без проверки поля идентичности на самой странице
U342	AT_CARRIER	meta/prompts/deklaration-v2.md:37	`<span itemprop="sku">N</span>`
U343	AT_CARRIER	meta/prompts/deklaration-v2.md:37	Taking the first search hit unchecked (the old Serper method)
U344	IN_ROUTER	router:33	проверка страницы по полю `sku`
U345	AT_CARRIER	projects/n8n/PLAN.md:71	Воркфлоу обращаются к `/api/v1/` своего же инстанса через credential типа Header
U346	AT_CARRIER	projects/n8n/PLAN.md:71	Действующее значение живёт в credential `monitor_key_v2`, без даты истечения.
U347	AT_CARRIER	projects/n8n/PLAN.md:71	Прежний `monitor_key` ротирован 21.07.2026 [владелец 21.07]
U348	AT_CARRIER	projects/n8n/PLAN.md:71	всякое указание на его срок истечения 25–26.07.2026 устарело и исполнению не под
U349	AT_CARRIER	projects/n8n/PLAN.md:73	Списка мест использования здесь нет намеренно
U350	AT_CARRIER	projects/n8n/PLAN.md:73	он устаревал быстрее, чем его правили, и пропускал одного потребителя из четырёх
U351	AT_CARRIER	projects/n8n/PLAN.md:73	Перед ротацией список берётся из снимка: строки `A` дают воркфлоу, обращающиеся 
U352	AT_CARRIER	projects/n8n/PLAN.md:73	На 26.09.2026 таких воркфлоу четыре: Workflow Health Monitor — Daily (`LguGCDYJv
U353	AT_CARRIER	projects/n8n/PLAN.md:73	Workflow Health Monitor — Intraday (`tABmSQXQalGnjRJw`, неактивен)
U354	AT_CARRIER	projects/n8n/PLAN.md:73	SYS Lint (`TXNstdVL8xlIygBp`, активен) и N8N Registry Sync (`gFFiBPm1OomOzJOj`, 
U355	AT_CARRIER	projects/n8n/PLAN.md:73	У всех четырёх в снимке есть узлы с типом `httpHeaderAuth`
U356	AT_CARRIER	projects/n8n/PLAN.md:73	Привязать тип к КОНКРЕТНОМУ узлу снимок не может: строки C считают типы по воркф
U357	AT_CARRIER	projects/n8n/PLAN.md:73	Привязку к узлу даёт лист «Авто» книги N8N_CREDENTIALS: строка на каждую пару «c
U358	AT_CARRIER	projects/n8n/PLAN.md:73	n8n не стирает прежний credential из узла при смене типа аутентификации: в узле 
U359	AT_CARRIER	projects/n8n/PLAN.md:73	Перед ротацией список потребителей ключа — строки листа «Авто» с его ID и «Актив
U360	AT_CARRIER	projects/n8n/PLAN.md:73	Лежит ли значение ключа открытым текстом в параметрах узла, не показывает ни сни
U361	AT_CARRIER	projects/n8n/PLAN.md:75	НЕ путать этот ключ с MCP-ключом, которым Claude обращается к n8n: тот не истека
U362	AT_CARRIER	projects/n8n/PLAN.md:75	не путать ни один из двух с `git-channel-webhook-auth` — секретом вебхуков Канал
U363	AT_CARRIER	projects/n8n/PLAN.md:75	тип auth у всех трёх один, назначение разное, и подмена одного другим даёт не от
U364	AT_CARRIER	projects/n8n/PLAN.md:77	Credential в n8n хранит копию значения ключа, а не сам ключ.
U365	AT_CARRIER	projects/n8n/PLAN.md:77	Удаление credential стирает эту копию из n8n и проходит без ошибки, но ключ прод
U366	AT_CARRIER	projects/n8n/PLAN.md:77	Ключ отзывает только тот, кто его выдал.
U367	AT_CARRIER	projects/n8n/PLAN.md:77	отозвать его можно только в Settings → n8n API: кнопка Delete рядом с ключом, за
U368	AT_CARRIER	projects/n8n/PLAN.md:77	Там же ключ создаётся (Create an API key), с меткой (Label) и сроком действия (E
U369	AT_CARRIER	projects/n8n/PLAN.md:77	Ключ, выданный внешним сервисом (Ozon, Wildberries, Voyage AI), отзывается у это
U370	AT_CARRIER	projects/n8n/PLAN.md:77	Порядок при утечке или ротации ключа к API n8n: создать новый ключ в Settings → 
U371	AT_CARRIER	projects/n8n/PLAN.md:77	удалить старый ключ в Settings → n8n API → только после этого удалить или переим
U372	AT_CARRIER	projects/n8n/PLAN.md:77	Проверено чтением документации n8n 2026-10-13
U373	AT_CARRIER	projects/n8n/PLAN.md:77	На инстансе не проверялось — проба требовала удалить действующий ключ, Андрей от
U374	AT_CARRIER	projects/n8n/PLAN.md:77	1 случай, 2026-07 — запись корпуса N8N_JOURNAL_2026, строка 2804
U375	AT_CARRIER	projects/n8n/PLAN.md:81	**SKU Category Historical Backfill** — защиты от дублей нет вообще.
U376	AT_CARRIER	projects/n8n/PLAN.md:81	Перед каждым запуском вручную очистить листы `sku_category_history` и `sku_categ
U377	AT_CARRIER	projects/n8n/PLAN.md:81	Триггер никогда не переводить на реальное расписание.
U378	AT_CARRIER	projects/n8n/PLAN.md:81	Эти два листа ни один узел по имени не раскрывает, поэтому в снимке их нет и кни
U379	AT_CARRIER	projects/n8n/PLAN.md:83	**News Filter** (`WB+Ozon News Filter`) — дедупликация через Google Sheets, лист
U380	AT_CARRIER	projects/n8n/PLAN.md:83	книга — `1eujHu87IO0IlngLX164_O81LxPI5NNpq9S47E8anVSo` [снимок 26.09]
U381	AT_CARRIER	registry/documents.md:196	`1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4` | `sales_raw_operations`
U382	PROPOSED_REMOVAL	proposed_removals.md:4	SKILL.md lines 216–219 (OZON_UE RAW two sources)
U383	AT_CARRIER	registry/documents.md:219	`1_E2KCZOVYaf68xVECwv9ZaGGn4bdz3jsh5D3lhsqdyM`
U384	AT_CARRIER	labs/sys/t-ozon-ue-parked-active.md:11	Ozon отключил эндпоинт `/v3/finance/transaction/list`
U385	AT_CARRIER	labs/sys/t-ozon-ue-parked-active.md:11	«воркфлоу не трогать, только читать при сверке»
U386	AT_CARRIER	labs/sys/t-ozon-ue-parked-active.md:33	активен, ежедневно в 02:00
U387	PROPOSED_REMOVAL	proposed_removals.md:4	SKILL.md lines 216–219 (OZON_UE RAW two sources)
U388	AT_CARRIER	registry/documents.md:219	`1hcAxLuj3YBSPUrOe8bYNbFD6ib8r7y56Pv1Ad8j1j8w`
U389	PROPOSED_REMOVAL	proposed_removals.md:4	SKILL.md lines 216–219 (OZON_UE RAW two sources)
U390	AT_CARRIER	labs/sys/t-ozon-ue-parked-active.md:12	вызывается как саб-воркфлоу узлом `03_Call_RAW_Sync` воркфлоу `5MDOGVCTxwDjHqy3`
U391	PROPOSED_REMOVAL	proposed_removals.md:4	SKILL.md lines 216–219 (OZON_UE RAW two sources)
U392	IN_ROUTER	router:28	прежний файл `references/cards-and-declarations.md`
U393	IN_ROUTER	router:28	прежний файл `references/cards-and-declarations.md`
U394	WEAKENED	router:3	перед записью в карточку Wildberries или Ozon
U395	AT_CARRIER	meta/CASES_wb-api.md:3	факты, установленные исполнениями
U396	IN_ROUTER	router:28	порядок записи и разобранные случаи — `meta/PROTOCOL_wb-card-write.md`
U397	AT_CARRIER	meta/CASES_wb-api.md:7	текст строк не правился
U398	HISTORY	cards-and-declarations.md:5	Внесено 2026-10-09 по харвесту 2026-10-08 (находки А4, А33, Б2, Б8; позиции очер
U399	AT_CARRIER	meta/CASES_wb-api.md:33	**Ответ 200 ничего не доказывает.**
U400	AT_CARRIER	meta/CASES_wb-api.md:33	POST `/content/v2/cards/update` отвечает 200 и меняет `updatedAt` карточки, но д
U401	AT_CARRIER	meta/CASES_wb-api.md:33	так шесть карточек отказали поштучно 2026-10-05, хотя журнал ошибок был пуст
U402	AT_CARRIER	meta/CASES_wb-api.md:33	(projects/deklaration-ozon/LOG.md, Т-7)
U403	AT_CARRIER	meta/CASES_wb-api.md:33	Итог записи проверяется двумя способами, оба обязательны
U404	AT_CARRIER	meta/CASES_wb-api.md:34	перечитать карточку через POST `/content/v2/get/cards/list` и сравнить поле за п
U405	AT_CARRIER	meta/CASES_wb-api.md:35	прочитать журнал ошибок асинхронной записи — POST `/content/v2/cards/error/list`
U406	AT_CARRIER	meta/CASES_wb-api.md:35	Метод GET на этот адрес отвечает 405.
U407	AT_CARRIER	meta/CASES_wb-api.md:35	Записи журнала сгруппированы по пакетам и `vendorCode`, поля `nmID` в них нет
U408	AT_CARRIER	meta/CASES_wb-api.md:35	(projects/deklaration-wb/PLAN.md, абзац «Факты записи»)
U409	AT_CARRIER	meta/CASES_wb-api.md:37	**Одна ошибочная карточка отклоняет всю склейку.**
U410	AT_CARRIER	meta/CASES_wb-api.md:37	Склейка — группа карточек с общим `imtID`.
U411	AT_CARRIER	meta/CASES_wb-api.md:37	Если в ней есть карточка с ошибкой, Wildberries не применяет запись ни к одной к
U412	AT_CARRIER	meta/CASES_wb-api.md:37	(projects/deklaration-ozon/LOG.md, Р-30)
U413	AT_CARRIER	meta/CASES_wb-api.md:39	**Запись заменяет карточку целиком.** Характеристика, не переданная в запросе, с
U414	AT_CARRIER	meta/CASES_wb-api.md:39	запись идёт только по схеме «прочитал свежую карточку в том же прогоне → поправи
U415	AT_CARRIER	meta/CASES_wb-api.md:39	узел перед отправкой сравнивает отправляемое с прочитанным
U416	AT_CARRIER	meta/CASES_wb-api.md:39	(projects/deklaration-wb/PLAN.md, абзац «Ловушка записи»)
U417	AT_CARRIER	meta/CASES_wb-api.md:39	Поле `kizMarked`, не переданное в запросе, принимается равным false — передавать
U418	AT_CARRIER	meta/CASES_wb-api.md:39	(projects/deklaration-ozon/LOG.md, Р-44)
U419	PROPOSED_REMOVAL	proposed_removals.md:5	cards-and-declarations.md lines 19–20
U420	PROPOSED_REMOVAL	proposed_removals.md:5	cards-and-declarations.md lines 19–20
U421	PROPOSED_REMOVAL	proposed_removals.md:5	cards-and-declarations.md lines 19–20
U422	PROPOSED_REMOVAL	proposed_removals.md:5	cards-and-declarations.md lines 19–20
U423	HISTORY	cards-and-declarations.md:20	ИСТОРИЯ ДИАГНОЗА: записи Р-9 и Р-10 того же журнала считали, что Wildberries мол
U424	PROPOSED_REMOVAL	proposed_removals.md:5	cards-and-declarations.md lines 19–20
U425	AT_CARRIER	meta/CASES_wb-api.md:41	**Случайные отказы пачки.** Ответ 400 или 500 «Internal server error» на пачку к
U426	AT_CARRIER	meta/CASES_wb-api.md:41	(projects/deklaration-wb/LOG.md, Р-12 пункт 6)
U427	AT_CARRIER	meta/PROTOCOL_wb-card-write.md:53	Значения характеристик передаются массивом строк: например ["3403990000"]
U428	IN_ROUTER	router:28	`meta/PROTOCOL_wb-card-write.md`
U429	AT_CARRIER	projects/card-content-sync/PLAN.md:100	предел поля у WB — 2 000 символов
U430	IN_ROUTER	router:26	описание — `projects/card-content-sync/PLAN.md`
U431	AT_CARRIER	meta/CASES_wb-api.md:43	Характеристики 15001135 «Номер декларации соответствия», 15001136 «Номер сертифи
U432	AT_CARRIER	meta/CASES_wb-api.md:43	Характеристики для ссылки на запись реестра нет.
U433	AT_CARRIER	meta/CASES_wb-api.md:43	у карточки есть блок `documents`: `items[{type, number, startDate, endDate, verd
U434	AT_CARRIER	meta/CASES_wb-api.md:43	это собственная сверка Wildberries документа с реестром
U435	AT_CARRIER	meta/CASES_wb-api.md:43	(projects/deklaration-ozon/LOG.md, Р-21)
U436	AT_CARRIER	meta/CASES_wb-api.md:43	При каждой записи декларации Wildberries создаёт документ заново, с новым id
U437	AT_CARRIER	meta/CASES_wb-api.md:43	промежуточный вердикт вроде `supplier_not_registered` через несколько часов може
U438	AT_CARRIER	meta/CASES_wb-api.md:43	Даты документа Wildberries сверяет с реестром — расхождение даёт `document_dates
U439	AT_CARRIER	meta/CASES_wb-api.md:45	Встречаются разные, и разбирать их надо явно, по всем встреченным формам; неузна
U440	AT_CARRIER	meta/CASES_wb-api.md:46	ММ-ДД-ГГ: `01-27-27` значит 27.01.2027
U441	AT_CARRIER	meta/CASES_wb-api.md:46	(meta/PRODUCT_DATA_HIERARCHY.md, раздел 4)
U442	AT_CARRIER	meta/CASES_wb-api.md:46	Воркфлоу «LM_DECL — WB Sync ИП» эту форму не понимал, пока разбор не исправили
U443	AT_CARRIER	meta/CASES_wb-api.md:47	ДД.ММ.ГГГГ — в характеристиках 15001137 и 15001138 у карточек, снятых зондом 202
U444	AT_CARRIER	meta/CASES_wb-api.md:48	в блоке `documents` даты приходят в виде ГГГГ-ММ-ДД с временем (код узла `03_Bui
U445	AT_CARRIER	meta/CASES_wb-api.md:49	Основной «LM_DECL — WB Sync» разбирает три формата (projects/deklaration-wb/STAT
U446	AT_CARRIER	meta/CASES_wb-api.md:51	**ОКПД 2 — характеристика 15004292.** ОКПД 2, введённый руками в личном кабинете
U447	AT_CARRIER	meta/CASES_wb-api.md:51	поэтому полная перезапись карточки (раздел 1) его стирает
U448	AT_CARRIER	meta/CASES_wb-api.md:51	Для предметов «Автохимия» и «Смазки автомобильные» вместе с ним Wildberries сним
U449	AT_CARRIER	meta/CASES_wb-api.md:51	повторная запись `kizMarked=true` без ОКПД 2 не принимается
U450	AT_CARRIER	meta/CASES_wb-api.md:51	так 2026-10-07 потеряли отметку маркировки 29 карточек основного кабинета
U451	AT_CARRIER	meta/CASES_wb-api.md:51	(projects/deklaration-ozon/LOG.md, Р-44 и Т-9)
U452	AT_CARRIER	meta/CASES_wb-api.md:51	ОКПД 2, записанный через API, API показывает, и он переживает следующую запись
U453	AT_CARRIER	meta/CASES_wb-api.md:51	(projects/deklaration-wb/LOG.md, Р-7 и Р-11)
U454	AT_CARRIER	meta/CASES_wb-api.md:54	Wildberries решает по паре «предмет + ТН ВЭД»: справочник `/content/v2/directory
U455	AT_CARRIER	meta/CASES_wb-api.md:54	маркировка нужна только при ОКПД 2 из перечня постановления Правительства № 1683
U456	AT_CARRIER	meta/CASES_wb-api.md:54	(projects/deklaration-ozon/LOG.md, Р-44 пункт 2)
U457	AT_CARRIER	meta/CASES_wb-api.md:54	Справочник ОКПД 2 — `/api/content/v2/directory/okpd`
U458	AT_CARRIER	meta/CASES_wb-api.md:54	взято из позиции очереди AH-25; вызовом в журналах не подтверждено
U459	AT_CARRIER	meta/CASES_wb-api.md:57	`needKiz` («Нужна маркировка КИЗ») — только чтение: Wildberries выводит его сам 
U460	AT_CARRIER	meta/CASES_wb-api.md:57	Через API без ОКПД 2 признак не включается; ручная галка сотрудника в личном каб
U461	AT_CARRIER	meta/CASES_wb-api.md:59	`kizMarked` («Подтверждаю, что на товар нанесена маркировка») — записывается, но
U462	AT_CARRIER	meta/CASES_wb-api.md:59	Ставить только по прямому слову владельца на названные им карточки
U463	AT_CARRIER	meta/CASES_wb-api.md:59	(projects/deklaration-wb/LOG.md, Р-7 «отвергнуто»; meta/PROTOCOL_wb-card-write.m
U464	AT_CARRIER	meta/CASES_wb-api.md:61	Блокировку карточки «подлежит обязательной маркировке» снимает не запись в карто
U465	AT_CARRIER	meta/CASES_wb-api.md:61	(projects/deklaration-wb/LOG.md, Р-7 пункт 3)
U466	AT_CARRIER	projects/deklaration-ozon/PLAN.md:35	POST /v2/product/certificate/create одним вызовом, товары передаются списком
U467	AT_CARRIER	projects/deklaration-ozon/PLAN.md:35	метод /v1/product/certificate/create отключён Ozon 2026-08-31 (вызов даёт 404)
U468	IN_ROUTER	router:26	(абзац «Факты API Ozon»)
U469	AT_CARRIER	projects/deklaration-ozon/PLAN.md:35	для типа DECLARATION стандарт — только NATIONAL или EAEU
U470	AT_CARRIER	projects/deklaration-ozon/LOG.md:133	блокер 11C это не ловит, потому что EAEU входит в варианты Ozon
U471	WEAKENED	projects/deklaration-ozon/LOG.md:133	ставит accordance_type: 'EAEU' жёстко для любого номера
U472	AT_CARRIER	projects/deklaration-ozon/PLAN.md:33	`LOG.md` Р-16; до правки EAEU стоял для любого номера — Т-5
U473	AT_CARRIER	projects/deklaration-ozon/PLAN.md:33	выбирает по номеру: «РОСС …» → NATIONAL, иначе EAEU
U474	AT_CARRIER	projects/deklaration-ozon/PLAN.md:35	Сертифицируемые типы товаров — POST /v2/product/certification/list
U475	AT_CARRIER	meta/CASES_ozon-api.md:41	`page_size` у `/v1/product/certificate/list` — не больше 100.
U476	AT_CARRIER	meta/CASES_ozon-api.md:41	У `/v1/product/certificate/products/list` поле `limit` от 1 до 1000, `page_size`
U477	AT_CARRIER	meta/CASES_ozon-api.md:41	по товару он отдаёт только `product_id`, `sku`, `product_status_code`, причину о
U478	AT_CARRIER	meta/CASES_ozon-api.md:41	(projects/deklaration-ozon/LOG.md, Т-4)
U479	AT_CARRIER	projects/deklaration-ozon/PLAN.md:35	/v2/product/info/list в API нет (есть /v3)
U480	AT_CARRIER	meta/CASES_ozon-api.md:42	Статус документа `approved` не значит, что товары одобрены: Ozon проверяет кажды
U481	AT_CARRIER	meta/CASES_ozon-api.md:42	итог перечитывается отдельным режимом «статус»
U482	AT_CARRIER	meta/CASES_ozon-api.md:42	(projects/deklaration-ozon/LOG.md, Р-36)
U483	AT_CARRIER	meta/CASES_ozon-api.md:42	Вкладки кабинета «На проверке», «Отклонены», «Одобрены» фильтруют статус докумен
U484	AT_CARRIER	meta/CASES_ozon-api.md:42	зависание видно только по колонке «Одобрено товаров»
U485	AT_CARRIER	meta/CASES_ozon-api.md:42	(projects/deklaration-ozon/PLAN.md)
U486	AT_CARRIER	meta/CASES_ozon-api.md:43	Факты этого раздела сняты с полного swagger.json, прочитанного в браузере 2026-1
U487	AT_CARRIER	meta/CASES_ozon-api.md:43	из сессии документацию Ozon прочитать нельзя (SKILL.md, «Внешние источники»)
U488	AT_CARRIER	projects/card-content-sync/PLAN.md:108	Описание — атрибут 4191 «Аннотация»
U489	AT_CARRIER	projects/card-content-sync/PLAN.md:109	переносы строк — только тегами `<br/>`
U490	IN_ROUTER	router:26	описание — `projects/card-content-sync/PLAN.md`
```

### Notes on WEAKENED and LOST units

- U005 (WEAKENED): old: read ONLY when a concrete detail is needed; router: read when the detail is needed AND the file is unknown, plus always before a card write — condition changed both ways
- U007 (WEAKENED): router description drops "перед работой с декларациями через API" trigger (old SKILL:3 via :20 and cards:3)
- U041 (WEAKENED): trigger narrowed: old "и перед работой с декларациями через API" missing from router description
- U043 (LOST): old SKILL.md:22 "Подтверждение прочтения — назвать найденную деталь и её пометку. Фиксированная фраза подтверждением не считается" — not in the router and not in any carrier (n8n-engineering-manual SKILL.md:16 has a similar rule, but only for reading that Skill). Not listed in proposed_removals.md.
- U044 (LOST): old SKILL.md:22 "Подтверждение прочтения — назвать найденную деталь и её пометку. Фиксированная фраза подтверждением не считается" — not in the router and not in any carrier (n8n-engineering-manual SKILL.md:16 has a similar rule, but only for reading that Skill). Not listed in proposed_removals.md.
- U045 (LOST): old SKILL.md:22 "Подтверждение прочтения — назвать найденную деталь и её пометку. Фиксированная фраза подтверждением не считается" — not in the router and not in any carrier (n8n-engineering-manual SKILL.md:16 has a similar rule, but only for reading that Skill). Not listed in proposed_removals.md.
- U047 (WEAKENED): router row drops "таймзона" from the roster list
- U231 (WEAKENED): old: must read editable before PATCH (rule); carrier: Rollback "может" check (option) — must→may
- U394 (WEAKENED): same narrowing as U041
- U471 (WEAKENED): old: Ozon ACCEPTED EAEU for a РОСС declaration; carrier (LOG Т-5): only our check-mode run passed, a live run WOULD have loaded it — the fact of Ozon acceptance is not in carriers (old text itself may overstate)

## Task 2 — knowledge of the old text not covered by any unit

Method: every old line was split into fragments; each fragment not covered by a unit quote was searched in carriers. Items below are knowledge with no unit of its own.

1. old/SKILL.md:140 «прочитано get_workflow_details 2026-10-09» — WEAKENED — provenance of the formula (method and date of reading the node) not carried; carrier projects/wb-ue/STATE.md:52 states the formula without it
   - evidence projects/wb-ue/STATE.md:52 «Формула сейчас одинакова в узле `06_Add_RAW_Key` обоих воркфлоу»
2. old/SKILL.md:198 «вместе со связкой Seed, Worker, Watch» — AT_CARRIER for the removed bundle — projects/deklaration-ozon/NOT_TAKEN.md:17
   - evidence projects/deklaration-ozon/NOT_TAKEN.md:17 «Паспорта снятых воркфлоу: Watch»
3. old/SKILL.md:198 «запускать его нельзя» — WEAKENED — explicit prohibition not carried; carriers only say the conveyor is removed (projects/deklaration-ozon/NOT_TAKEN.md:11)
   - evidence projects/deklaration-ozon/NOT_TAKEN.md:11 «Конвейер PDF снят 2026-09-30»
4. old/SKILL.md:18 «то есть выведено из JSON инстанса» — AT_CARRIER registry/documents.md:176 (line carried verbatim)
   - evidence registry/documents.md:176 «то есть выведено из JSON инстанса»
5. old/SKILL.md:84 «WB FBS Decision Engine, Evening Report, Morning Forecast, Order Close v2» — units for table rows 83–96 quote only ID and first sheet; the columns «Листы», «Кто работает», «Узлов» are AT_CARRIER verbatim at registry/documents.md:196–209
   - evidence registry/documents.md:197 «WB FBS Decision Engine, Evening Report, Morning Forecast, Order Close v2»
6. old/SKILL.md:12 «на этот абзац ссылается n8n-engineering-manual, roots.md R13» — IN_ROUTER — roots.md:256 still cites «Ключ к собственному API n8n», router:34 resolves it
7. old/references/cards-and-declarations.md:26 «переносы строк — обычный перевод строки» — AT_CARRIER projects/card-content-sync/PLAN.md:102 (unit U429 cites only the 2 000 limit)
   - evidence projects/card-content-sync/PLAN.md:102 «абзацы разделены `\n`»
8. old/references/cards-and-declarations.md:59 «поштучный `/v1/product/info/description` не нужен» — AT_CARRIER projects/card-content-sync/PLAN.md:108 (equivalence of attribute 4191 and the per-item method)
   - evidence projects/card-content-sync/PLAN.md:108 «Значение атрибута 4191 совпадает с ответом /v1/product/info/description»
9. old/references/cards-and-declarations.md:51 «версия 1 отвечает 400 «obsolete method cannot be used»» — AT_CARRIER projects/deklaration-ozon/PLAN.md:35
   - evidence projects/deklaration-ozon/PLAN.md:35 «v1 этого метода отвечает 400 «obsolete method cannot be used»»
10. old/SKILL.md:217 «29 колонок» — PROPOSED_REMOVAL (lines 216–219); column counts 29/16 and «схема несовместима со старой без адаптера» exist nowhere else

## Task 3 — added explanatory lines at carriers: false or overstated

Checked every line starting «Перенесено 2026-10-21 из Skill», every «Не путать:», every redirect line, the passport-ID line at registry/documents.md:219 and the new section headings. True and verified (not listed): CASES_ozon-api.md:9; CASES_wb-api.md:60 and :52 (sources exist and say what is claimed); wb-logistics/PLAN.md:74; wb-reviews/PLAN.md:50 first half (RAG categories are at projects/wb-reviews/STATE.md:31); n8n/PLAN.md:48; CASES_external-access.md:7; registry/documents.md:219; line ranges of n8n/PLAN.md, wb-reviews, wb-logistics, external-access. Carried text is verbatim (python full-line match for 160 old lines).

1. meta/CASES_ozon-api.md:7 «отчёт `meta/SYNTHESIS_n8n-workflow-registry_2026-10-21.md`» — FALSE — the cited report does not exist in /tmp/sbc; same in meta/CASES_wb-api.md:7, meta/CASES_external-access.md:7, projects/n8n/PLAN.md:48, registry/documents.md:174, projects/wb-reviews/PLAN.md:50, projects/wb-logistics/PLAN.md:74 and router:10
2. meta/CASES_ozon-api.md:7 «references/cards-and-declarations.md, строки 52–55» — OVERSTATED — cards line 53 (/v3/product/info/list) is not in this file; it lives in projects/deklaration-ozon/PLAN.md:35
3. meta/CASES_wb-api.md:7 «SKILL.md, строки 147–167, и references/cards-and-declarations.md, строки 11–45» — OVERSTATED — SKILL 149 (wb-reviews), 159/161 (wb-logistics), 160 (wb-reviews/STATE), 163–165 (n8n-map Ф5) and cards 19–20 (removed), 24 (PROTOCOL), 26 (card-content-sync) are not in this file
4. registry/documents.md:174 «SKILL.md, строки 18–108» — OVERSTATED — only 18, 26–27, 30 and 64–108 are here; 20–24, 28–29, 31–35 are router rows, 37–58 went to projects/n8n/PLAN.md
5. meta/CASES_wb-api.md:9 ««раздел 1», «раздел 4» и «references/cards-and-declarations.md» — разделы этого файла ниже» — FALSE for «раздел 4»: the only «раздел 4» left in this file (line 46) points to meta/PRODUCT_DATA_HIERARCHY.md, not to this file; the old internal «раздел 4» (Ozon description) was not carried here
6. meta/CASES_wb-api.md:29 «(таблица в начале файла)» — NOT REDIRECTED — dangling internal reference: there is no N8N_CREDENTIALS table at the start of this file (it is at registry/documents.md:182); line 9 does not mention it. Also the «Источники» list (Ф5, Р-22, Р-30, Р-6) was the source of the Ozon roles / WB ping lines that are not in this file
7. meta/CASES_wb-api.md:58 «противоречит кейсам 3 и 4 `meta/CASES_wb-api-card-write.md`» — OVERSTATED — of the quoted line only «только чтение» is contradicted (case 3: a passed needKiz is kept). «Через API без ОКПД 2 не включается; ручная галка включает» agrees with case 4 and PROTOCOL:17 («Включить признак через API по коду ОКПД 2 нельзя … ручная галка … включает»)
8. meta/CASES_wb-api.md:51 «повторная запись `kizMarked=true` без ОКПД 2 не принимается» — GAP — the «Не путать» at line 52 covers only the 29-card cause; this clause is also contradicted by case 4 (kizMarked not accepted even WITH ОКПД 2; it depends on needKiz) and gets no warning
9. projects/wb-reviews/PLAN.md:50 «предупреждения о модели эмбеддингов в Skill `n8n-engineering-manual` больше нет» — OVERSTATED — n8n-engineering-manual SKILL.md:97 still carries the general warning (model must equal the indexing model, else full reindex); only the concrete model name and dimension were removed
   - evidence skills/n8n-engineering-manual/SKILL.md:97 «модель эмбеддингов, которой пишутся и ищутся векторы базы знаний, совпадает с моделью»
10. registry/documents.md:192 «не названы нигде: ни здесь, ни в `registry/documents.md`» — NOT REDIRECTED / now false — the line sits inside registry/documents.md, and 1sBYaluh1NDk… is named at registry/documents.md:168 (WB_ANALITIKA_book), 1eQPV1KQ2FE4… at labs/ozon-ue/INDEX.md:38 (sku_cost_Шаблон); added line 174 explains only «строка 35»
   - evidence registry/documents.md:168 «WB_ANALITIKA_book: 1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI»
11. projects/n8n/PLAN.md:79 «### Ловушки отдельных воркфлоу без своего проекта в репозитории» — QUESTIONABLE — SKU Category Historical Backfill works on book 1eQPV1… (registry/documents.md:200 «SKU Category Backfill»), which belongs to lab labs/ozon-ue (INDEX.md:38)
12. router:29 «(там же — запись Р-69 о том, что ключ не меняется)» — OVERSTATED — Р-69 is a record of projects/wb-ue/LOG.md; STATE.md holds only a summary pointing to it (STATE.md:21 «подробно и почему — Р-69»), and the formula at STATE.md:52 sits in a section the summary declares history
   - evidence projects/wb-ue/STATE.md:21 «Решено сессией вместо Андрея (подробно и почему — Р-69): raw_key не менять»

## Task 4 — claims beyond the old text (EXTENDED)

1. router:16 «Перед решением, которое на ней стоит, сверить с объектом» — EXTENDED — new mandatory verification of every detail against the object (n8n-map row or Drive search; workflow itself, Р15) before a decision; old text only marked lines [снимок]/[владелец]/unmarked
2. router:17 «Новая деталь экземпляра сюда не дописывается» — EXTENDED — old allowed and asked additions here («кто знает имя, дописывает его сюда», SKILL.md:79); the router forbids any new instance detail and routes missing carriers to Andrei
3. router:48 «Таблиц по каждому воркфлоу, списков ID, снимков состояния» — EXTENDED — old forbade only per-workflow tables (SKILL.md:37) and explicitly kept ID lists («ID отсюда не убираются», SKILL.md:64)
4. router:3 «Читай, когда нужна такая деталь и неизвестно, в каком файле её искать» — EXTENDED/narrowed trigger — old «Читай ТОЛЬКО когда нужна конкретная деталь»; also the trigger «перед работой с декларациями через API» was dropped
5. meta/CASES_wb-api.md:5 «при расхождении прав тот файл, а не этот» — EXTENDED — new precedence rule; old cards:3 only said the protocol is not retold
6. meta/CASES_wb-api.md:5 «верное для любого кабинета» — EXTENDED/overstated — file holds workflow-specific lines (WB Reviews Intake take=100 and 60-day window, line 14; Order Close v2 branch, line 22); same claim at meta/CASES_ozon-api.md:5 while lines 18, 23, 24 there are node/config-specific
7. meta/CASES_external-access.md:5 «сначала эта таблица, затем один дешёвый зонд» — EXTENDED — mandatory reading order is new; old (SKILL.md:181) only said «перед тем как строить обход, повторить один дешёвый зонд»

## Task 5 — router paths and quoted section names

All other paths named by the router exist in /tmp/sbc; all quoted section names were found: «Решение Андрея 2026-10-20: Skill — инструкции для всех» (labs/sys/t-knowledge-synthesis.md:179), «Книги Google Sheets — имена, листы, кто работает; проверка ID по длине» (registry/documents.md:172), «Детали инстанса n8n — перенесено из Skill n8n-workflow-registry» (projects/n8n/PLAN.md:46), «Факты API Ozon» (projects/deklaration-ozon/PLAN.md:35), «Декларации» (meta/CASES_ozon-api.md:39), «Карточки и маркировка» (meta/CASES_wb-api.md:31), «Права ключей» (meta/CASES_wb-api.md:26), фаза Ф5 (projects/n8n-map/PLAN.md:193), «База знаний liquimoly_kb (pgvector)» (projects/wb-reviews/PLAN.md:48), пункт 4.8.13 (n8n-engineering-manual references/engine.md:100), пункт 9a (meta/prompts/deklaration-v2.md:37), «Ключ к собственному API n8n» (projects/n8n/PLAN.md:69), «Ловушки отдельных воркфлоу без своего проекта в репозитории» (projects/n8n/PLAN.md:79), раздел 4 (projects/n8n-map/PLAN.md:95), раздел 3 (n8n-engineering-manual SKILL.md:111), second-brain-git 7.6 (SKILL.md:169), second-brain-engineer Р15 (SKILL.md:94).

1. router:10 «`meta/SYNTHESIS_n8n-workflow-registry_2026-10-21.md`» — MISSING FILE in /tmp/sbc
2. router:28 «прежний файл `references/cards-and-declarations.md`» — not a path in /tmp/sbc root; exists only as mirror skills/n8n-workflow-registry/references/cards-and-declarations.md, which disappears with the router. Still cited as live by meta/prompts/deklaration-v2.md:68, projects/deklaration-v2/PLAN.md:312, skills/n8n-engineering-manual/references/roots.md:290
   - evidence meta/prompts/deklaration-v2.md:68 «references/cards-and-declarations.md and SKILL.md sections «Права ключей маркетплейсов»»
3. router:25 ««3. Ozon — общее»» — old-section label not verbatim: old headings are «## 3. Внешние API и доменные детали» + «### Ozon — общее»; likewise «3. Wildberries» and «Ozon — начисления» (old «Ozon — начисления (accrual)»). Cosmetic — the label still finds the row
4. router:30 «лист «Ключи» книги N8N_CREDENTIALS» — sheet of a Google book — not verifiable in /tmp/sbc

