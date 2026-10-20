projects/n8n/STATE.md

# STATE_n8n — текущее состояние работ

Здесь только то, что меняет действие следующей сессии. Решения — `LOG.md`; правила и устройство проекта — `PLAN.md`; невзятое при переносе из N8N_INDEX — `NOT_TAKEN.md`.

Файл переписан заново 2026-10-17 автопилотом (запись Р-6 журнала): закрытое убрано, по каждому открытому вопросу принято решение. Прежний текст (перенос из N8N_INDEX 2026-10-06 с дополнениями до 2026-10-16, адреса строк источника «[строка N]») — blob ff350070fce505633eb4f168406a854da17882d8 в истории файла, коммит до 2026-10-17.

## Состояние инстанса

Сверено 2026-10-18 по снимку `registry/n8n-map.md` (коммит ee37e02, instance_last_change 2026-10-17T16:50): активных 76, архивных 98, неактивных 69; без errorWorkflow из активных только сам Error Notifier; с неопубликованным черновиком один — WB FBS Morning Forecast 6M9nS9iKQzMdztUs (черновик 2026-10-17 16:31 UTC сделала параллельная сессия, это воркфлоу проекта WB_LOGISTICS — публиковать или отбросить решает он); без явной таймзоны 62. Ожидание абзаца ниже выполнено.

По снимку `registry/n8n-map.md` 2026-10-17 (instance_last_change 2026-10-16T17:40) и правкам 2026-10-17 (Р-6): из активных без воркфлоу ошибок остался только сам Error Notifier; активных с неопубликованным черновиком не осталось. Числа после правок даёт снимок 2026-10-18 05:30 — пересчитать по полям 5 и 10 строк W, ждать: без errorWorkflow 1, с черновиком 0. Явной таймзоны нет у 68 активных из 82 (снимок 2026-10-17, до снятия пяти с публикации).

## СЛЕДУЮЩИЙ ШАГ

- После 2026-10-19 02:00 по серверу: проверить, что ночной прогон OzonRawАналитика MPzPrtsnPtf0sVQo прошёл без алерта — это первый прогон, который гарантированно идёт после удаления ключа API n8n. Доказательство — строки за 2026-10-18 в листе sales_raw_operations книги 1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4 (gsheets-read) и отсутствие алерта. Упал — убрать висячую ссылку на ключ из узла 03_Ozon_Transaction_List (правка узла по «да» Андрея).
- Ручные действия Андрея — раздел ниже, остались пункты 2 и 3.

## Ручные действия Андрея

1. СДЕЛАНО 2026-10-18, проверено по объекту: list_credentials по имени ключа API n8n вернул 0 записей. Остаток: узлы 03_Ozon_Transaction_List (MPzPrtsnPtf0sVQo, get_workflow_details 2026-10-18: в credentials.httpHeaderAuth стоит удалённый ключ API n8n) и 03_Ozon_Analytics_Request (SElTcMg3BpY6pmdo, неактивен) ещё ссылаются на удалённый ключ — висячая ссылка; узел аутентифицируется по genericAuthType httpCustomAuth (Ozon Seller API). Убрать ссылку при ближайшей правке этих узлов. Было: удалить ключ доступа API n8n в n8n → Credentials. Он висит лишней привязкой на узлах 03_Ozon_Transaction_List (MPzPrtsnPtf0sVQo) и 03_Ozon_Analytics_Request (SElTcMg3BpY6pmdo, неактивен), оба узла ходят с ключом «Ozon Seller API». Если его значение — живой ключ n8n API или WB, отозвать и там, где он выдан. После удаления — проверить, что ночной прогон OzonRawАналитика (02:00 по серверу) не прислал алерт. Гипотеза (не проверена): лишняя привязка после удаления ключа узел не роняет.
2. Перевыпустить ключ Serper в кабинете Serper и вставить новое значение в ключ доступа Serper в n8n; старый отозвать. Правок в воркфлоу ноль. Проверка — ручной прогон GDI35U36bBRzKZp5, результат по объекту.
3. Одна команда на сервере — найти литералы ключей в узлах и истории версий (закрывает вопрос «Anthropic: 1 ключ, 2 воркфлоу, не перепроверено» из аудита 2026-07-23):
   docker exec -i n8n-postgres-1 psql -U n8n -d n8n -c "select id, name, active from workflow_entity where nodes::text like '%sk-ant-%' or nodes::text ilike '%Api-Key%'"
   Имя пользователя и базы сверить с docker-compose. Второе условие ловит и законные упоминания имени заголовка — смотреть только строки, где рядом стоит значение ключа. Найденное — ID воркфлоу прислать сессии N8N; ключ Anthropic в n8n есть готовый, перевод узла на него — точечная правка.

## ОТКРЫТЫЕ ЗАДАЧИ

[x] ЗАКРЫТО 2026-10-18 по объекту — исполнение 81691 Error Notifier (2026-10-17 16:26 UTC, алерт о падении nvNYvvmuOqGyHXfL, исполнение 81689): в ответе Telegram ok:true, message_id 7487, текст содержит «Ошибка: GUARD: anchor occurrences=0…» и «Прогон: https://…/executions/81689» (get_workflow_execution, узел Send a text message). Было: Error Notifier M5BLqclKBjGTpz33 с 2026-10-17 сохраняет успешные прогоны (Р-6). Закрыть задачу «формат алерта» (правка 2026-10-08: строки «Ошибка:» до 500 знаков и «Прогон:», версия bf4cc77f) по первому сохранённому прогону Notifier: search_workflow_executions по M5BLqclKBjGTpz33, в выходе узла Send a text message текст содержит обе строки.

[ ] [2026-10-17] Таймзона: 68 активных без явной таймзоны работают по серверной Europe/Berlin. Массово не ставить (Р-6, отвергнуто). Правило при касании воркфлоу: если расписание или текст рассчитаны на московское время (пример — Order Intake kNg2uEoYlaGOLC82, описание «Telegram только в 06:00 и 16:00 МСК»), ставить Europe/Moscow и пересчитать часы расписания; иначе ставить Europe/Berlin явно.

[ ] [2026-10-17] Перевод Google-узлов с OAuth2 на сервисный аккаунт — по одному воркфлоу при касании, руками в редакторе (Р-6, пункт 8). Первыми — потребители «Google Drive account» XagmJHhXQU748dYW (протухал в сентябре): GDrive Trash Sweeper LFDK2oAFdGWQ3Nxd, create_folder uapccJY1O4ykyDi7, Claude → Obsidian kJTXJuHQAv1go52t, DOSSIER W3KjaXVqWD2c02IK, bFJsM3aFlIHIFeAd, KEucSnA2duWI3eRA. Перед переводом — файлам и папкам дать доступ сервисному аккаунту (n8n-engineering-manual §8).

[ ] ЗАМОРОЖЕНО — проект OZON_REVIEWS (решение Андрея 2026-10-06): все четыре воркфлоу OZON_REVIEWS неактивны. При разморозке, по порядку: (1) вернуть строку заголовков листа ozon_reviews_queue книги OZON Reviews System (1mgtcD2wSm_-8hqfpv3v883KE34-Smy-kFxHvt6zMXj4) — эталон: первые 28 колонок строки 1 листа ozon_reviews_archive, имя 29-й колонки не установлено; (2) в OZON Reviews Archive HH7pDL2VZfU9C9Np, узел 10_Delete_From_Queue, startIndex = row_number вместо row_number − 1 (сейчас удаляет строку над архивированной); (3) только потом включать. Публикация в Ozon отвечает PermissionDenied «not available with existing subscription». Подробности — прежний текст файла, blob ff350070.

## Инструменты, оставленные неактивными (возврат — publish_workflow)

- SYS Lint TXNstdVL8xlIygBp — линтер замороженного SYS_INDEX; баг «состояние записано: нет» не чинится.
- SYS Maintenance Gap Monitor 5Rs6pNDSm4weWDVj — авторизация узла 02E_Fetch_Harvest стоит в черновике (Р-5); при включении публиковать черновик.
- Projekt_OCR OEM_V.5 DWyvoJYkCodJxMg1 — поле lang=deu+eng в черновике (Р-5); узел 08_Unify_Output_For_Sheets отключён — проверить перед включением.
- Контроль Price WB Hf92DOmQPqbQWW5G — на узле 10_WB_Prices_Info нет ключа; привязать перед включением.
- LM_DECL_MASTER ukuFBDUD4mRYVGBu и VMPxWzXPefKT2R1B — выбор между ними не нужен, декларации ведёт deklaration-v2.
- Сняты 2026-10-17 (Р-6): OzonRawАналитика_Monat FnB2Imp7thMKuwnD, WB Reviews History Load GTrCbV5GmyhJKcNd, KB Loader — Auto Chemistry 2vWu3qaUkYFlDt4v (черновик сломан: в узлах Check If Exists и Insert to pgvector запрос без «=» — перед публикацией вернуть «=»), Claude → Google Apps Script Read e9ScqWtLPgSsHf0A (не работает в принципе: Apps Script API не пускает сервисный аккаунт), gen-test-source-H260803 urqZj1RHOOAWKCdr.

## Правила, вынесенные из закрытых задач

- Описание воркфлоу длиннее 255 знаков (18 воркфлоу на 2026-10-16) операция setWorkflowMetadata не принимает: при правке описания через MCP сначала укоротить, сохранив строку PASSPORT, либо править в редакторе.
- Имя «***» в снимке — маскировка имени, содержащего путь своего вебхука (projects/n8n-map/PLAN.md, раздел 4); настоящее имя — get_workflow_details. Не дефект, не расследовать.
- Успешные прогоны по расписанию и вебхуку не сохраняются (EXECUTIONS_DATA_SAVE_ON_SUCCESS=none, замер архива 2026-10-09: данные прогонов 342 МБ, хранение 14 дней); исключения — воркфлоу ступени 1 Р-4 и сохранение у отдельных воркфлоу (vKjqExap1mJjM6Ap, J0v5swjXLfiANJa2, M5BLqclKBjGTpz33 и девять по Р-4). «Нет прогонов» доказательством простоя не является; доказательство — объект.

## От соседнего проекта

- ⚡ Это затрагивает N8N (2026-10-14, OZON_UE, задача `labs/ozon-ue/t-money-telegram.md`): узел HTTP Request с ключом googleApi и адресом `.../values:batchGet?ranges=<ИМЯ>&ranges=<ИМЯ>` принимает имена именованных диапазонов книги вместо адресов A1 (исполнение 79874 воркфлоу YkUb5SnLtEaTctoH); один несуществующий диапазон роняет весь запрос ответом 400 (исполнение 79873). Принято 2026-10-17: кандидат в Skill google-drive-docs, references/sheets.md — внести харвестом вместе с правками n8n-engineering-manual ниже.
- ⚡ Это затрагивает N8N (2026-10-14, WB_UE, запись Р-59 журнала `projects/wb-ue/LOG.md`, воркфлоу DcIqwTVqBqMQyigs): renameNode переименовал узел с ключом Telegram, привязка уцелела (расходится с n8n-engineering-manual R1a и пред-полётным пунктом 4б «переименование рвёт привязку»); addNode с полем credentials привязал ключ новому HTTP-узлу при пустом autoAssignedCredentials; setWorkflowSettings записал timezone и errorWorkflow. Каждое наблюдение однократное. Принято 2026-10-17: кандидат в правку R1a — харвестом; до правки при переименовании узла с ключом сверять поле credentials после записи.

- ⚡ Это затрагивает N8N (2026-10-18, SYS, запись Р-2 журнала `projects/gas-bridge/LOG.md`): (1) в update_workflow есть операция setNodeCredential — привязка ключа к узлу по id через MCP работает (воркфлоу 38BkuLXhxXLTPpqQ, j0DU23IXnp7xggX9); (2) create_workflow_from_code поставил на вебхук автопривязкой ключ «Voyage AI», хотя в коде было newCredential('git-channel-webhook-auth') — после создания сверять autoAssignedCredentials; (3) узел HTTP Request кладёт сырой ответ в contextData, вынос запроса в опубликованный подворкфлоу оставляет contextData вызывающего пустым (исполнения 82240 и 82241). Правка Skill — позиция AJ-15 очереди.
- ⚡ Это затрагивает N8N (2026-10-20, SYS, тестовые сессии теста чтения references/, `labs/sys/t-knowledge-synthesis.md`): (1) GDrive Trash Sweeper `LFDK2oAFdGWQ3Nxd` упал 2026-10-20 в 02:00 по всемирному времени, исполнение 82795, статус error (проверено диспетчером get_workflow_execution); причина по чтению тестовой сессии — ключ доступа «Google Drive account» отвергнут в узле 02ListTrashStaging, Error Notifier прислал сообщение 7494; это пункт ОТКРЫТЫХ ЗАДАЧ о переводе потребителей этого ключа на сервисный аккаунт. Попутно: триггер назван «01_Daily_0400_MSK», а таймзона у воркфлоу не задана — срабатывает в 04:00 по Берлину. (2) Гипотеза (не проверена диспетчером): восемь воркфлоу, реально работающих по расписанию, без строки PASSPORT в описании — WB FBS Order Intake `kNg2uEoYlaGOLC82`, WB FBS Order Close v2 `DM26WhTJyCV0DhkP`, WB FBS Supply Accepted `7x9wPrugdbseaEp2`, Ozon RAW Accrual Sync `aVpgEnYBAgIIss4k` (паспорт есть, строки нет), Получение SKU Ozon `J0v5swjXLfiANJa2`, OZON_UE Accrual Types Sync `c7TIdv32dHV3MBRU`, OZON Money Telegram `YkUb5SnLtEaTctoH`, OzonRawАналитика `MPzPrtsnPtf0sVQo`; метод — search_workflows и поиск строки PASSPORT в description. Паспортизировать пачкой или «при касании» (правило Skill n8n-workflow-passport) — решение Андрея.