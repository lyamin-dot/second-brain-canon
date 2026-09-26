---
name: "n8n-workflow-registry"
description: "Справочник деталей инстанса n8n Андрея, которые ниоткуда не выводятся: человеческие имена и ID книг Google Sheets, специфика внешних API (Ozon, Wildberries, Liqui Moly), формулы raw_key, состояние pgvector, ловушки отдельных воркфлоу. Живой состав воркфлоу — ID, имя, статус, расписание, связи, документы, типы credential — здесь НЕ живёт: он в файле registry/n8n-map.md репозитория second-brain-canon. Читай ТОЛЬКО когда нужна конкретная деталь: ID книги по её имени или по имени листа, форма запроса к внешнему API, формула ключа. Правила и механика n8n — в n8n-engineering-manual, читать его до правки любого воркфлоу."
---

# Справочник инстанса — детали, которые ниоткуда не выводятся

Редакция 2026-09-26. Правки этой редакции: адрес живого состава воркфлоу переведён с Google Doc N8N_REGISTRY на файл registry/n8n-map.md (фаза Ф2 проекта n8n-map); абзац про ключ к своему API исправлен — он называл ротированный ключ действующим и пропускал одного потребителя из четырёх; раздел про инструменты Docs сведён к тому, чего нет в google-drive-docs; добавлен раздел 2.2 — двадцать девять книг инстанса, у которых нет человеческого имени нигде; MASTER_MAP опознан как лист, а не отдельная книга; снята ссылка, указывавшая на этот же файл. Прежний заголовок несёл пометку «v3.0, усечён» — она описывала неизвестное прошлое обрезание и снята как непроверяемая.

## Как этим пользоваться

Вход по вопросу, а не чтением целиком: нашёл строку, забрал деталь, вышел.

Строки помечены источником. `[снимок ДД.ММ]` — сверено со строкой файла registry/n8n-map.md, то есть выведено из JSON инстанса. `[владелец ДД.ММ]` — со слов Андрея. Строка БЕЗ пометки набита руками, датой не подтверждена и может быть устаревшей. Это и есть причина не заводить здесь ничего, что выводится из объекта: непомеченная строка живёт ровно до того дня, когда объект изменится, и никто об этом не узнает.

Подтверждение прочтения — назвать найденную деталь и её пометку. Фиксированная фраза подтверждением не считается: она доказывает, что файл открыт, а не что в нём что-то нашли.

Чего здесь нет и где это лежит:

| Что нужно | Где |
|---|---|
| Живой состав воркфлоу: ID, имя, статус, черновик, расписание, таймзона, вызовы, документы, типы credential | registry/n8n-map.md репозитория second-brain-canon; формат строк — projects/n8n-map/PLAN.md раздел 4 |
| Пути вебхуков и признак их аутентификации | Google Doc N8N_REGISTRY, строки HOOK и HOOKCALL |
| Как устроен воркфлоу и почему именно так | его паспорт; адрес — строка PASSPORT в description воркфлоу |
| Механика n8n, корневые причины отказов, протокол правки | n8n-engineering-manual |
| Инструменты чтения и записи Google Docs, Sheets, Drive: ID, поля вызова, верификация | google-drive-docs |
| Чтение и запись файлов репозитория канона | second-brain-git |
| История инцидентов | INCIDENT_LOG |

Per-workflow таблиц здесь нет: они были третьим источником истины и дважды разошлись с объектом — устаревшие пометки на `ss0QkY9V8YEMHf2B` и `LM_DECL_MASTER` пришлось исправлять руками. Не заводить заново.

---

## 1. Инструменты Drive и Docs

Действующие инструменты записи и чтения Google Docs — append, replace, overwrite, apply-from-file, read — вместе с их ID, полями вызова и порядком верификации живут в google-drive-docs: таблица быстрого выбора инструмента и раздел 3. Здесь они не повторяются намеренно. Копия этого списка была бы третьим источником истины ровно того класса, от которого этот файл предупреждает выше, и один такой промах уже стоил разбора: паспорт Registry Sync до 26.09.2026 называл получателем перезаписи заархивированный `OYIhTm8h2ABMHQUW`.

Что есть только здесь:

`Hpy9TCly6LKCjlqf` — GDrive Share File, активен [снимок 26.09]. Вход POST `{fileId, emailAddress?, role?}` → permissions.create плюс read-back. Создан 11.08.2026.
ОГРАНИЧЕНИЕ: ходит под сервисным аккаунтом и не может выдать файлу самое первое разрешение — если у сервисного аккаунта доступа к файлу ещё нет, permissions.create отвечает 404. Годится, только когда доступ хотя бы на чтение уже есть.

`kJTXJuHQAv1go52t` — Claude → Obsidian, активен [снимок 26.09].

Заархивированные версии инструментов Docs. Звать нельзя, через MCP они и не видны; список нужен, чтобы узнавать их ID в старых текстах и паспортах:

| ID | Что было | Состояние |
|---|---|---|
| `CELGBmo7vQFF1Ej7` | gdocs-append v1 | archived [снимок 26.09], заменён на `YfzWwu1VmIUCbUu0` 22.07.2026 |
| `qWk65OyxaoAu4jAl` | gdocs-replace v1 | archived [снимок 26.09], расхождение обнаружено 21.07.2026 |
| `OYIhTm8h2ABMHQUW` | gdocs-overwrite v1 | archived [снимок 26.09]; 30.07.2026 обнулил SYS_INDEX — разбор в INCIDENT_LOG |

---

## 2. Книги Google Sheets и документы

Снимок отвечает строками D на вопрос «какие воркфлоу и какими узлами трогают документ с этим ID». На обратный вопрос — «какой ID у книги, которую человек зовёт Price Master» или «в какой книге лежит лист seen_posts» — он не отвечает: человеческих имён в нём нет, а имя листа узел раскрывает не всегда. Этот раздел и есть ответ на обратный вопрос, поэтому ID отсюда не убираются.

### 2.1 Книги с человеческим именем

Ozon:
- **Reviews Queue** — `1mgtcD2wSm_-8hqfpv3v883KE34-Smy-kFxHvt6zMXj4`, листы `ozon_reviews_queue` и `ozon_qa_queue`; 20 узлов [снимок 26.09].
- **Price Master** — `1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk`, листы `Artikel` и `CURRENT`; 8 узлов [снимок 26.09].
- **SKU_Artikel_Map** — `1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU`, листы `SKU_Artikel_Map` и `MASTER_MAP`. MASTER_MAP — единый кросс-маппинг `sku + lm_id + ozon_sku + wb_nm_id`; это ЛИСТ внутри этой же книги, а не отдельный файл: узел `16_Write_WB_nmID` пишет в этот лист по тому же ID книги [снимок 26.09].

Liqui Moly:
- **LM_DECL_MASTER** — `1PO7vNyoY16tYqpU_KB5xuK4aSAbOU7YW_MM0scg5ksY`; 13 узлов; там, где узел раскрывает имя листа, это `LM_DECL` [снимок 26.09]. Лист `Decl_Monitor` — дашборд со светофором; ни одним узлом не трогается, поэтому в снимке его нет [снимок 26.09]. Прежняя редакция этого файла называла рабочим листом именно `Decl_Monitor` — это описывало дашборд для человека, а не то, куда пишут воркфлоу.

### 2.2 Книги без человеческого имени

Двадцать девять книг из сорока одной, которые трогают воркфлоу, не названы нигде: ни здесь, ни в `registry/documents.md`. Ниже те, что используются тремя и более узлами, опознанные по именам листов и воркфлоу. Человеческого имени у них нет — это долг, а не факт; кто знает имя, дописывает его сюда.

| ID книги | Листы | Кто работает | Узлов |
|---|---|---|---|
| `1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4` | `sales_raw_operations`, `ozon_raw_accrual_TEST`, `ozon_accrual_types` | конвейер OZON_UE RAW целиком | 19 |
| `1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ` | `wb_fbs_orders_tracking`, `wb_fbs_monitor_params`, `wb_fbs_performance_log` | WB FBS Decision Engine, Evening Report, Morning Forecast, Order Close v2 | 19 |
| `1JwV7bbfLLxztE7gRrUEOUIvUk-xCOcwDkT88RA5bHPg` | `wb_reviews_archive` | WB Reviews Intake, Publication, History Load, Full History Load | 17 |
| `1XMy8XsF4tIyiPIhiW2dAt8Sihbsy4xQOXWQhjCJEHyE` | `kb_motor_oil`, `Шаблон` | KB Loader Motor Oil, KB MO Annotation Preprocessor, KB Sync Motor Oil Specs | 15 |
| `1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4` | `SKU_Artikel`, `cost_price_history` | OZON_UE Cost Price Snapshot и Backfill, Accrual-адаптер, SKU Category Backfill | 14 |
| `1AhgaspMQl3wLsVT7Iub0d195r8DwwUarhQAWwjBO8xE` | `wb_fbs_params`, `wb_fbs_supplies`, `wb_fbs_decision_log`, `wb_fbs_forecast_snapshot` | тот же конвейер WB FBS | 12 |
| `14QMHYMM4mZRnnq1wHQA4_SA8ZnOeE1xcVJDL2h9h1Pk` | имя листа узлы не раскрывают | WB RAW Finance Sync V.3, WB RAW History Load V.3 CLEAN | 6 |
| `17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU` | `Акт.цена`, `Акт.цена_backfill` | OZON_UE Cost Price Snapshot и Backfill | 4 |
| `1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI` | `dashboard`, `wb_reports_official` | WB Reports Official Sync, WB Monitor Telegram Reader | 4 |
| `1eujHu87IO0IlngLX164_O81LxPI5NNpq9S47E8anVSo` | имя листа узлы не раскрывают; здесь лежит `seen_posts` | WB+Ozon News Filter | 3 |
| `1gPjWlhld9LAzGScEU9l63OGfcXK48dujYX1A9Uh6gBk` | имя листа узлы не раскрывают | KB Loader Transmission Oil, KB TO Annotation Preprocessor | 3 |
| `1sPD5SAFCTygzUaEPg8RKRPHQyc0HCMIK-aMpnXqYu3k` | имя листа узлы не раскрывают | KB Loader Auto Chemistry, KB AC Annotation Preprocessor | 3 |
| `11j0yKZ0FvE9EbZiTzCStEACsgecliaElVccpUixmQcQ` | имя листа узлы не раскрывают | Контроль Price WB | 3 |
| `1cK5dues1ffnUdy6UGCDHiMzxp1ZucdyvawS5Dvx-o3M` | имя листа узлы не раскрывают | SYS Lint | 3 |

Все строки таблицы — [снимок 26.09]. Полный список из сорока одного документа с их узлами достаётся из снимка одной командой: `grep '^D|' registry/n8n-map.md`.

Отдельно: ID `1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ` лежит в `registry/documents.md` строкой 35 в повреждённом виде — 41 символ вместо 44. Верный ID — тот, что в таблице выше и в узлах воркфлоу.

---

## 3. Внешние API и доменные детали

### Ozon — отзывы и вопросы
- Поля `pros`, `cons`, `text` раздельные; статус `rejected` возможен.
- Публикация отзыва: POST `/v1/review/comment/create`, задержка 4 секунды между запросами.
- Маппинг `operation_type` → узел `06C_Map_Operation_Category`, обычный объект JS. Новый тип добавляется в словарь; неизвестные дают `'Не классифицировано: ' + opType`.
- Эндпоинты вопросов идут БЕЗ `/product/`: POST `/v1/question/list`, `/v1/question/answer/create`, `/v1/question/answer/delete`.
- Публичный ответ на карточке закрыт без тарифа Premium Plus (порядка 25 тысяч рублей в месяц); ответ через чат `/v3/chat/` виден только самому покупателю.
- Вебхука `TYPE_NEW_QUESTION` не существует.
- Стоп пагинации `/v1/review/list` — любое из трёх: пустой массив, `last_id` не изменился, длина меньше `limit`.
- Встроенная пагинация HTTP-узла для транзакций: `paginationCompleteWhen: other`, `completeExpression: ={{ $response.body.result.operations.length < 1000 }}`.
- Ограничение частоты примерно один запрос в секунду: Items per Batch = 1, Batch Interval = 4000 мс.

### Ozon — начисления (accrual)
- POST `/v1/finance/accrual/by-day`, тело `{date, last_id}` → ответ `{accruals:[...], last_id}`. Пагинация останавливается, когда `last_id` пришёл пустой строкой, НЕ по длине массива.
- `accrued_category` принимает `POSTING`, `ITEM`, `NON_ITEM`; у каждой своя вложенная форма объекта.
- Наблюдаемая формула нэттинга: `sale_amount + sale_commission + delivery.total_accrued = total_amount`.
- `container_fees` ни разу не приходило непустым; статус поля неизвестен.
- Ловушка совместимости с `/v3/posting/fbs/get` (вход `{posting_number}`): валидный `posting_number` даёт только `unit_number` из записей с `accrued_category=POSTING`. Взятый из `ITEM` или `NON_ITEM` даёт 404 в 85–91 проценте случаев.

### Формулы raw_key
Ключ строки RAW-слоя, свой на каждый источник:
- Ozon, транзакции — `business_date|operation_id`
- Ozon, начисления — `accrual_id`
- Wildberries — `rrd_id|sale_dt|report_id`

Почему форматы намеренно разные и почему RAW-слои не объединяются — n8n-engineering-manual, раздел 3. Здесь только сами формулы.

### Wildberries
- Ответ на вопрос: PATCH `/api/v1/questions`, тело `{id, answer:{text}, state:"wbRu"}`. Поле `state` обязательно — без него ответ не появляется на сайте.
- `/orders/status`: поле называется `orders`, не `orderIds`; тело `{orders:[...]}` передаётся объектом, без stringify.
- `supplierStatus=confirm` включает и отгруженные заказы — фильтровать дополнительно по tracking status `shipped`.
- Пагинация статистики: курсор `rrdid`, между страницами узел Wait на 70 секунд из-за ограничения частоты.
- Finance API v1: POST `finance-api.wildberries.ru/api/finance/v1/sales-reports/detailed`, токен категории «Финансы». Даты с зоной: `2026-05-26T00:00:00+03:00`. Пагинация: `rrdId` в теле, старт 0, до ответа 204. Денежные поля приходят строками. Credential — Header Auth, имя `Authorization`, значение `Bearer TOKEN`.
- Домены-ловушки, которые НЕ работают: `statistics-api` (старый v5), `common-api`, `finance-api/.../{reportId}`.
- Семантика статусов FBS: отмена клиентом видна только в `wbStatus` (`declined`, `canceled_by_client`), при этом `supplierStatus` часто остаётся `new`. Детект отмены нужен отдельной ветвью по `wbStatus`, иначе висящий хвост вечно блокирует переход «поставка отгружена».
- Времени приёмки на уровне заказа не существует: `/orders/status` отдаёт только текущий статус, `/supplier/orders` — только `date` и `lastChangeDate`. Время приёмки есть только на уровне поставки: `scanDt` в GET `/supplies` плюс `/supplies/{id}/order-ids`.
- Воркфлоу WB Reviews Response использует RAG для категорий `QA_OIL_MATCH` и `QA_SPEC`.
- Личный Telegram Андрея: `chatId` захардкожен, `6054723832`. Группа логистики: `chat_id = -1004269834495`.

### pgvector, база знаний liquimoly_kb
Коллекции и наполнение: `motor_oil` — около 183 записей, загрузка неполная; `auto_chemistry` — 146, полная; `transmission_oil` — 42, полная; `antifreeze` — не загружен.

Модель эмбеддингов — `voyage-3`, размерность 1024. НЕ `voyage-3-lite` с размерностью 512: ошибка необратима и стоит переиндексации всей базы. То же предупреждение стоит в n8n-engineering-manual разделом 1 — единственный намеренный дубль в семействе, потому что цена ошибки выше цены дубля.

### Liqui Moly — декларации
`processDeclPdfInbox` версии 1.1 конвертирует PDF деклараций через Drive API v2 (`Files.insert`, `convert:true`). Только v2: для конвертации из Apps Script v3 не работает.

### Ключ к собственному API n8n
Воркфлоу обращаются к `/api/v1/` своего же инстанса через credential типа Header Auth с заголовком `X-N8N-API-KEY`. Действующее значение живёт в credential `monitor_key_v2`, без даты истечения. Прежний `monitor_key` ротирован 21.07.2026 [владелец 21.07]; всякое указание на его срок истечения 25–26.07.2026 устарело и исполнению не подлежит.

Списка мест использования здесь нет намеренно: прежняя редакция такой список держала, он устаревал быстрее, чем его правили, и пропускал одного потребителя из четырёх — SYS Lint. Перед ротацией список берётся из снимка: строки `A` дают воркфлоу, обращающиеся к `/api/v1/`, строки `C` — тип credential на их узлах. На 26.09.2026 таких воркфлоу четыре: Workflow Health Monitor — Daily (`LguGCDYJvMQSahcj`, активен), Workflow Health Monitor — Intraday (`tABmSQXQalGnjRJw`, неактивен), SYS Lint (`TXNstdVL8xlIygBp`, активен) и N8N Registry Sync (`gFFiBPm1OomOzJOj`, активен) [снимок 26.09]. У всех четырёх в снимке есть узлы с типом `httpHeaderAuth` [снимок 26.09]. Привязать тип к КОНКРЕТНОМУ узлу снимок не может: строки `C` считают типы по воркфлоу целиком. Поэтому утверждение «ключ лежит открытым текстом в параметрах узла» из снимка не выводится ни в ту, ни в другую сторону — проверяется только глазами в редакторе.

НЕ путать этот ключ с MCP-ключом, которым Claude обращается к n8n: тот не истекает и к воркфлоу отношения не имеет. И не путать ни один из двух с `git-channel-webhook-auth` — секретом вебхуков Канала: тип auth у всех трёх один, назначение разное, и подмена одного другим даёт не отказ доступа, а утечку не того секрета.

### Ловушки отдельных воркфлоу
**SKU Category Historical Backfill** — защиты от дублей нет вообще. Перед каждым запуском вручную очистить листы `sku_category_history` и `sku_category_history_detail` до заголовков. Триггер никогда не переводить на реальное расписание. Эти два листа ни один узел по имени не раскрывает, поэтому в снимке их нет и книгу по ним не найти.

**News Filter** (`WB+Ozon News Filter`) — дедупликация через Google Sheets, лист `seen_posts`; книга — `1eujHu87IO0IlngLX164_O81LxPI5NNpq9S47E8anVSo` [снимок 26.09].

**OZON_UE RAW** — два источника в одной книге `1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4`, не путать:
- Старый продакшен: лист `sales_raw_operations`, 29 колонок, воркфлоу `OzonRawАналитика` (`MPzPrtsnPtf0sVQo`), паспорт `1_E2KCZOVYaf68xVECwv9ZaGGn4bdz3jsh5D3lhsqdyM`. Источник сломан 08.09.2026 — Ozon отключил `/v3/finance/transaction/list`. Воркфлоу не трогать, только читать при сверке. ВНИМАНИЕ: воркфлоу при этом активен и стоит на расписании 02:00 [снимок 26.09], то есть каждую ночь ходит в отключённый эндпоинт.
- Новый, тестовый: лист `ozon_raw_accrual_TEST`, 16 колонок, воркфлоу `Ozon RAW Accrual Sync` (`aVpgEnYBAgIIss4k`), паспорт `1hcAxLuj3YBSPUrOe8bYNbFD6ib8r7y56Pv1Ad8j1j8w`. К продакшену не готов на 17.09.2026: `TEST_DATE` захардкожен, пишет в тестовый лист, схема несовместима со старой без адаптера. ВНИМАНИЕ: воркфлоу активен, стоит на расписании 02:00 и вызывается как саб-воркфлоу узлом `03_Call_RAW_Sync` воркфлоу `5MDOGVCTxwDjHqy3` [снимок 26.09].
- Третий лист той же книги, `ozon_accrual_types`, обслуживает воркфлоу `OZON_UE Accrual Types Sync` [снимок 26.09].
