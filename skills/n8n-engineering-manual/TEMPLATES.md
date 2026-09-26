n8n Golden Templates T1–T4
Версия: v1.0 · Дата: 2026-07-24 · Инстанс liamin-n8n (n8n 2.20.9, Hetzner CPX32, PostgreSQL 16)
Спутник SKILL.md (n8n-engineering-manual). Сюда попадаешь из §5 или §7 манула. Каждый шаблон: копируемый артефакт + когда применять / когда нельзя + живой пример из аудита 82 воркфлоу (воркфлоу + нода).
Секреты, найденные аудитом, в этот документ сознательно не перенесены.
ГЛАВНОЕ ОГРАНИЧЕНИЕ, действующее на все шаблоны. EXECUTIONS_DATA_SAVE_ON_SUCCESS=none + PRUNE — успешные прогоны не хранят данные нод. Следствие: любая верификация в этих шаблонах — ТОЛЬКО по объекту воздействия (целевая таблица / Doc / БД), НИКОГДА по статусу execution и никогда по логу. Статус success ничего не доказывает.
________________


T1 — ИДЕМПОТЕНТНАЯ ЗАПИСЬ
Закрывает R3 (0 items тихо обрывают цепочку) и R6 (Sheets в роли БД).
Шаг 0. Выбор инструмента — до того, как начинается шаблон
Вопрос: что именно нужно?
* Просто «видели этот ключ раньше?», объём до ~10k, без TTL и метаданных → нода Remove Duplicates, режим removeItemsSeenInPreviousExecutions. Шаблон не нужен, одна нода. (T1-A)
* Нужно состояние: запрашиваемое, с TTL, со статусом, с историей → Data Table (T1-B)
* Данные читает человек глазами (витрина юнит-экономики, отчёт) → Google Sheets (T1-C)
ПРИНЦИП. Служебное состояние (курсоры-watermark, dedup-маркеры, реестры, sku-маппинг) не обязано жить в Sheets. Корень R6 — это налог за использование Sheets в роли БД. Разделение ролей «состояние → Data Table / витрина → Sheets» устраняет корень, а не лечит симптом.
Живой пример правильного выбора: Skills Drift Detector (Htrj0Kyj7eT5SEhR) хранит sync-состояние в Data Table, а не в Sheets — одно из немногих корректных применений Data Tables в инстансе.
T1-A. Remove Duplicates — самый дешёвый путь
* {
*   "type": "n8n-nodes-base.removeDuplicates",
*   "parameters": {
*     "operation": "removeItemsSeenInPreviousExecutions",
*     "dedupeValue": "={{ $json.raw_key }}",
*     "options": { "historySize": 10000 }
*   }
* }


Когда применять: поток однотипных item, нужен только факт «уже обрабатывали». Когда НЕЛЬЗЯ: нужен запрос по состоянию, TTL, ветка «вернуть из кэша», хранение статуса.
T1-B. Data Table — служебное состояние
Форма: Get → IF → [обработать новое / вернуть известное].
Обязательные условия (иначе тихий обрыв цепочки, R3):
1. На Get: alwaysOutputData: true НА УРОВНЕ CONFIG НОДЫ, не внутри parameters. Внутри parameters движок его тихо игнорирует. Без него no-match даёт 0 items и цепочка молча стоит.
2. Обе ветки IF обязаны отдавать одинаковую форму JSON. Иначе downstream $json.x ломается в зависимости от того, какая ветка сработала. Нужен нормализующий anchor-узел.
3. Многоколоночный фильтр — явно matchType: "allConditions" (иначе в части версий по умолчанию OR).
4. returnAll: false без явного limit → дефолт 50 → тихое обрезание.
КВИРК ИНСТАНСА (§4.14). Операция get с per-item фильтром keyValue={{$json.field}} ненадёжна при N>1 items — схлопывает в 1 без ошибки, даже с executeOnce:false. Поэтому берём ФОРМУ Get+IF, но реализуем как returnAll:true + матчинг по ключу в Code-ноде.
Идемпотентные маркеры требуют TTL-уборки: отдельный воркфлоу, удаляющий строки старше окна ретраев.
Живой пример: Skills Drift Detector (Htrj0Kyj7eT5SEhR), нода 05_Get_All_Synced — executeOnce:true + alwaysOutputData:true, корректный паттерн.
T1-C. Google Sheets — витрина (ПРЕДПОЧТИТЕЛЬНАЯ ФОРМА)
Одна нода записи, без delete+merge:
* {
*   "operation": "appendOrUpdate",
*   "columns": {
*     "matchingColumns": ["raw_key"],
*     "mappingMode": "autoMapInputData"
*   }
* }


Обязательно:
* matchingColumns заданы ВСЕГДА + приведение типов (parseInt / String). Строка != число не матчится, ошибки нет, растут дубли.
* Составной ключ собирать ЗАРАНЕЕ, в Code, в одну колонку. Мультивыбор matchingColumns матчит только по первой колонке, UI при этом молча сбрасывает остальные.
* Сверять реальный gid (sheetName.value), не подпись в UI: cachedResultName — старый снимок и врёт.
* Read-нода: executeOnce + узкий фильтр, иначе N items = N запросов = 429.
* Per-item шаги оборачивать в splitInBatches(batchSize:1), иначе pairedItem схлопывается → ExpressionError: Multiple matches found.
* Поля предыдущих нод после Sheets-ноды брать через $('Имя').item — вторая Sheets-нода в цепочке отдаёт только свою схему.
Живой эталон: WB RAW History Load V.3 CLEAN (Iis5dlRS1GWZqQXD), нода 11_Write_RAW_To_Sheets — appendOrUpdate по raw_key, БЕЗ delete+merge вообще. Аудит помечает это как более простое и безопасное решение той же задачи, что решается связкой find→IF→delete→wait→merge в сиблингах.
Живой контрпример утраты данных при неверном маппинге: SKU Category Weekly Snapshot (qZWrl0MkRnZBipXA), нода 06_Is_Snapshot_Duplicate возвращает новый объект из 2 полей вместо spread — каждую неделю в sku_category_history пишется почти пустая строка, счётчики категорий теряются молча. Правило отсюда: в Code-нодах внутри пайплайна ВСЕГДА spread ({ ...src, newField }), НИКОГДА не собирать item заново из перечисленных полей.
T1-D. Google Sheets + delete — только если перезапись диапазона обязательна
Форма (обе ветки IF подключены):
* Find (executeOnce:true, alwaysOutputData:true — top-level)
*   → IF (row_number exists?)
*        true  → Delete → Wait → Merge input(1)
*        false →                 Merge input(1)     ← ОБЯЗАТЕЛЬНО ПОДКЛЮЧЕНА
*   → appendOrUpdate


Решение по развилке «подключать false-ветку или задокументировать как безопасную»
Подключать. Обоснование:
1. Проверяемость. Безопасность варианта «не подключено» держится на режиме Merge (append не ждёт физически неподключённые входы). Но режим Merge при parameters:{} НЕ ВИДЕН через get_workflow_details — аудит был вынужден пометить это знаком вопроса дважды (11_Wait_For_Delete в OzonRawАналитика, 10B_Merge_Before_Write в WB RAW Finance Sync V.3). Архитектура, корректность которой нельзя подтвердить чтением, не может быть шаблоном.
2. Рецидив доказан. В OzonRawАналитика false-ветку уже чинили (закрыто 07-04), к 07-23 она снова отсутствует, при этом description воркфлоу утверждает обратное. Это класс R1b: пересборка графа снимает связи. Незадокументированная зависимость от режима Merge превращается в тихую поломку при следующем update_workflow.
3. Асимметрия цены. Подключить = один провод. Задокументировать = вечная сноска, которую надо помнить при каждой правке и которая уже один раз не сработала (см. п.2).
Дискриминатор: когда неподключённый выход IF — НЕ баг
Неподключённый выход допустим ТОЛЬКО если он терминал: ниже него никто не ждёт данных — ни вход Merge, ни петля цикла SplitInBatches.

Терминал, корректно: WB FBS Order Close v2 (DM26WhTJyCV0DhkP) 02E_IF_Has_Orders; WB Reviews Intake (mAaWSmoXDH9Ofgg3) 09_IF_Has_New / 17_IF_Has_Updates

Баг, ждёт Merge (ПРОВЕРЕНО ЖИВЫМ ЧТЕНИЕМ 2026-08-04 — АКТИВЕН СЕЙЧАС, не только на момент аудита): OzonRawАналитика (MPzPrtsnPtf0sVQo) 09_IF_RAW_Rows_Exist — connections содержит один массив (только true-ветка), false-ветка отсутствует; description воркфлоу заявляет «снова подключена, как в оригинале» — это НЕ соответствует действительности прямо сейчас, не только исторически. WB RAW Finance Sync V.3 (IvgysDKrq3UISYEY) 08_IF_RAW_Rows_Exist — тот же класс, тоже подтверждён живым чтением 04.08

Баг, ждёт цикл (ИСПРАВЛЕНО к 2026-07-26): Ozon_Hashtag_Generator (KQqajdrYKxle9JRe) 04_SkipIfEmpty — false-ветка внутри цикла SplitInBatches БЫЛА не подключена на момент аудита 07-23, первая же строка с пустым описанием останавливала весь цикл, остальные строки прогона не обрабатывались. Проверено живым чтением 2026-08-04: false-ветка сейчас подключена обратно в 03_LoopOverItems, цикл продолжается на пустых описаниях штатно. Пример сохранён как класс ошибки, не как текущее состояние

Требование видимости намерения
Если выход IF — сознательный терминал, он должен вести в NoOp с говорящим именем (STOP_No_Rows, No_New_Items), а не висеть в пустоте. Тогда «терминал» отличается от «забыли провод» прямо на графе, без чтения JSON и без археологии.
Живые эталоны: WB_WF_sku-mapping-loader (qrZw8bxIEpRAUwEe) 03_IF_Has_Rows → STOP_No_Rows; WB Reviews Full History Load (ss0QkY9V8YEMHf2B) 09_IF_Has_New → 11_No_New_Items.
Живой эталон самой связки T1-D: OzonRawАналитика_Monat (FnB2Imp7thMKuwnD) — та же архитектура, что в сломанном сиблинге, но оба выхода 09_IF_RAW_Rows_Exist присутствуют в connections.
Когда T1 применять / когда нельзя
* Применять: любая повторяемая запись в целевой объект, где повторный прогон возможен — ретрай, ручной перезапуск, backfill, пересечение окон расписания.
* Предпочитать T1-C (appendOrUpdate) над T1-D (delete+merge) всегда, когда бизнес-логика допускает upsert по ключу.
* НЕЛЬЗЯ применять T1-C, если требуется физическое удаление строк, исчезнувших из источника — upsert их не удалит; это случай T1-D.
* НЕЛЬЗЯ полагаться на append без matchingColumns. Живой пример дублирования: SKU Category Historical Backfill (VWyXmCPJevCnbkZT), ноды 05_Write_Snapshots_History и 07_Write_Detail_History, append с matchingColumns:[] — повторный запуск дублирует всю историю.
________________


T2 — HTTP-НОДА И ОБРАБОТКА ОШИБОК В ПРОДЕ
Закрывает R5, R11, R4.
Слой 1. Самолечение — на любую ноду с сетевым вызовом
* {
*   "retryOnFail": true,
*   "maxTries": 3,
*   "waitBetweenTries": 5000,
*   "options": { "timeout": 30000 }
* }


* Движок режет: максимум 5 попыток, максимум 5000 мс между попытками.
* Без явного options.timeout дефолт — 5 минут. Зависший запрос держит воркер; на CPX32 это дорого.
* Работает на любой сетевой ноде (HTTP, Telegram, Postgres, AI), не только HTTP Request.
* Ретраит на ЛЮБУЮ ошибку без фильтра по коду. Нужен ретрай только на 429/5xx — не retryOnFail, а выход ошибки + IF по $json.error.httpCode.
Живой эталон: Deklaration_Hydraulisches_Oil_V.4 (EH2JaB8WGa0JsBqs), нода 03_Load_Product_Page — retryOnFail:true, maxTries:5, waitBetweenTries:5000 заданы явно.
АЛЬТЕРНАТИВА, ЧАСТО ЛУЧШЕ RETRY — самовосстанавливающийся флаг. Если воркфлоу идёт по расписанию часто, вместо retryOnFail дешевле идемпотентный флаг: при сбое объект просто не помечается обработанным и подхватывается следующим прогоном. Живой эталон: WB FBS Supply Accepted (7x9wPrugdbseaEp2) — флаг summary_sent_at в wb_fbs_supplies; при сбое 05_Fetch_Order_Ids поставка пропускается и повторяется через час. retryOnFail не нужен.
Слой 2. Выбор onError
Заменяет прежнюю формулировку R5 («на каждой HTTP-ноде в цепочке защиты — continueRegularOutput»). Та формулировка опасна: с точки зрения n8n ошибка при continueRegularOutput считается ОБРАБОТАННОЙ, и глобальный errorWorkflow по такой ноде НЕ СРАБОТАЕТ НИКОГДА.
Дерево выбора:
* Ошибку реально обрабатываю дальше по ветке (алерт, фолбэк, запись статуса) → onError: "continueErrorOutput" И ОБЯЗАТЕЛЬНО развести output(1) в реальную ноду. Одно без другого = тихий отказ, items испаряются.
* Ошибка не критична, поток должен идти дальше, и downstream ЯВНО читает code/error → onError: "continueRegularOutput". ВНИМАНИЕ: эта нода выпадает из-под глобального errorWorkflow. Осознанный размен.
* Осмысленной обработки нет → оставить дефолт (stopWorkflow) и дать errorWorkflow отработать. Это не лень, это правильный выбор.
* ХУДШИЙ ВАРИАНТ, ЗАПРЕЩЁН: continueErrorOutput с неподключённым output(1), либо выход ошибки, заведённый в no-op. Ошибка проглочена и наверх не всплывает.
Живые примеры:
Правильный continueRegularOutput: WB FBS Morning Forecast (6M9nS9iKQzMdztUs), 05_Fetch_WB_New — downstream 06_Calculate_Forecast имеет try/catch с явным фолбэком и выводит «— ошибка API» в Telegram-сообщение пользователю. Ошибка видима человеку. Так — можно
Неправильный continueRegularOutput: WB RAW Finance Sync V.3 (IvgysDKrq3UISYEY) — 07_Find_RAW_Rows_By_Date, 09_Delete_RAW_Rows, 11_Write_RAW_To_Sheets, все три на continueRegularOutput, никто ниже не читает code/error. errorWorkflow в settings ЗАДАН (M5BLqclKBjGTpz33) и не сработает никогда. Дыра в мониторинге при формально настроенном мониторинге — худший вид отказа
Голый continueErrorOutput: Projekt_OCR OEM_V.5 (DWyvoJYkCodJxMg1), 06_Extract_Text_From_PDF — connections.main = один массив, ветка ошибки не подключена. При сбое OCR строка молча исчезает из пайплайна без записи статуса
Тот же класс: LM_DECL_MASTER V.2 (VMPxWzXPefKT2R1B) — ноды 05A/05C_Error_Handler_* корректно ПОЛУЧАЮТ ошибку, но их собственный выход никуда не подключён. Статус PAGE_LOAD_ERROR никогда не записывается
Слой 3. Сохранность данных
* HTTP-нода перезаписывает json. Поля предыдущих нод брать через $('ИмяНоды').all()[i] ПО ПОЗИЦИИ, не через item.json.
* Первой нодой после HTTP — явная проверка code/error.
* neverError:true БЕЗ последующей явной проверки — запрещено. Он маскирует ошибку внешнего API под валидный item. Живой пример: OZON Fetch Reviews → Queue (IHn3Bmyh1VeHf4Ya), 02_Fetch_Ozon_Reviews с neverError:true; при 401/429/5xx downstream читает body?.reviews из тела ошибки → undefined → fallback [] → воркфлоу трактует сбой как «новых отзывов нет» и молчит. errorWorkflow не задан.
* Отдельная ловушка: neverError НЕ гасит ошибку внутри completeExpression пагинации. Если API вернул ошибку, response.body.data может быть undefined, и .length на undefined бросит ошибку в самом выражении. Замечено в WB Reviews Intake (mAaWSmoXDH9Ofgg3).
* Не полагаться на output Sheets-ноды как на источник полей — он может быть усечён. Живой эталон обхода: LM_DECL — Watch (OnEludZYMusvFxTS) — 07B_Append_History и 08_Build_Telegram_Msg читают данные напрямую из $('07A_Prepare_Update'), а не из выхода Sheets-ноды.
Слой 4. Глобальный error-workflow
* Программная установка setWorkflowSettings.errorWorkflow доступна только с n8n 2.29.0+. На 2.20.9 назначается ВРУЧНУЮ в настройках каждого воркфлоу. Это прямо упирается в задачу «mass-assign Error Notifier»: либо руками по числу воркфлоу, либо апгрейд. Третьего нет.
* Правила самого error-воркфлоу: никаких внешних вызовов, способных упасть; быстрый (выполняется синхронно и тормозит исходный сбой); канал уведомления ОТЛИЧНЫЙ от мониторимых.
* Минимальное содержимое алерта: имя воркфлоу, ID, ссылка на редактор, ссылка на прогон, lastNodeExecuted, реальный error.message, время.
ДЕФЕКТ ДЕЙСТВУЮЩЕГО. Error Notifier (M5BLqclKBjGTpz33) не включает $json.execution.error.message в текст алерта — только имя воркфлоу, время и lastNodeExecuted. Для диагностики всё равно приходится открывать UI. Пока это не исправлено, слой 4 работает наполовину, и T2 даёт меньше, чем должен.
Проверка после настройки: сделать заведомо падающий воркфлоу (HTTP на битый URL, без обработки), прогнать, убедиться что алерт дошёл. Проверять по факту прихода сообщения, не по логу.
Когда T2 применять / когда нельзя
* Слой 1 — на все сетевые ноды всех активных schedule-воркфлоу, без исключений.
* Слой 2 — везде, где есть внешний вызов; дефолт stopWorkflow — законный и часто лучший выбор.
* Слой 3 — обязателен везде, где после HTTP-ноды используются поля из нод выше.
* Слой 4 — на все активные воркфлоу; на деструктивные (delete, permanent delete, публикация вовне) — в первую очередь.
* НЕЛЬЗЯ ставить continueRegularOutput «чтобы не падало». Это единственный способ гарантированно ослепить мониторинг.
________________


T3 — HTTP-НОДА К ANTHROPIC API
Конфигурация ноды:
* Body Content Type = JSON
* Specify Body = Use Expression
* Value (через fx), БЕЗ ведущего =, БЕЗ JSON.stringify():
* {{ {
*   "model": "claude-haiku-4-5-20251001",
*   "max_tokens": 600,
*   "system": $json.system_prompt,
*   "messages": [{ "role": "user", "content": $json.user_content }]
* } }}


* Raw + JSON.stringify() сломан после апгрейда 2.9.4 → 2.20.9: двойная сериализация.
* Модели: тест claude-haiku-4-5-20251001, prod claude-sonnet-4-6.
* Credential: genericCredentialType / httpHeaderAuth. Ключ в параметрах ноды — запрещено (R13).
* Сверху накатывается T2 слой 1 (retryOnFail + timeout) и слой 3 (проверка code/error).
ОБРАБОТКА ПУСТОГО / НЕВАЛИДНОГО ОТВЕТА МОДЕЛИ — обязательная часть шаблона. Внутри цикла SplitInBatches НЕЛЬЗЯ делать throw на пустой ответ: throw останавливает весь execution, то есть весь батч, а не одну строку. Вместо throw — вернуть item со статусом ошибки и пропустить дальше, разбор статуса сделать отдельной веткой.
Живой пример дефекта: KB TO — Annotation Preprocessor (wWFfPIAfLd7yunU8) и KB AC — Annotation Preprocessor (5Iyr82zmzCeievFv), нода 07_Extract_Result — throw Error при пустом ответе Claude останавливает весь цикл; один плохой ответ прерывает обработку всего батча.
Живой эталон конфигурации credential: OZON QA Response (R8w94X0mT0Fa2Oil) — genericCredentialType/httpHeaderAuth для Anthropic и Voyage, хардкода нет.
Когда применять / когда нельзя
* Применять: любой вызов Anthropic API из HTTP Request на этом инстансе.
* НЕЛЬЗЯ использовать Raw body с динамическим телом — двойная сериализация, тихо битый запрос.
* НЕЛЬЗЯ оставлять ключ в headerParameters. На момент аудита один и тот же живой ключ найден в двух воркфлоу (Ozon_Hashtag_Generator 05_ClaudeAPI и WB+Ozon News Filter 11_Claude_Filter) — ротация затронет оба одновременно, это надо учитывать при ротации.
________________


T4 — ЧЕКЛИСТ ПЕРЕД ПУБЛИКАЦИЕЙ
Пункты 1–6 — ГЕЙТЫ: провалил → не публикуем. Пункты 7–12 — качество.
ГЕЙТ 1. validate_workflow
Ноль ошибок схемы и формы.
ГЕЙТ 2. Антипаттерн-скан
Ловит то, чего validate_workflow не видит:
* Set-нода с 0 или 1 потребителем → удалить, выражение вписать в потребителя.
* Code-нода делает то, для чего есть нативная: ручной цикл пагинации → опция Pagination; ручной sleep → нода Wait; regex-парсинг → XML/JSON.parse; ретрай по статусу → retryOnFail.
* Identity-ноды (return $input.all()) — всегда признак кривой формы воркфлоу.
* Merge: число проводов = numberOfInputs. Проверить off-by-one: parameters.useDataOfInput считается с 1, а connections.<source>.main[index] — с 0. (R9)
* Fan-out: параллельности НЕТ, ветки идут последовательно сверху вниз по координате Y. (R10)
* $json в глубине ветвлений → заменить на $('Node').item.json.
* $env — не работает вообще, бросает в рантайме.
* Switch без fallbackOutput молча теряет items. (R8)
* Дубль провода: два одинаковых connection-объекта на один целевой узел = каждый item проходит пайплайн дважды. Живой пример: Deklaration_TransmissionOil_V.4 (GDI35U36bBRzKZp5), connections["02B_Extract_Product_URL"].
* Орфаны и мёртвый груз: ноды без входящих связей и disabled-ноды, оставленные внутри цепочки.
ГЕЙТ 3. Обработка ошибок разведена по T2
Для всего по расписанию и всего продакшн-важного. Отдельно проверить: нет ни одной ноды с continueErrorOutput и неподключённым output(1).
ГЕЙТ 4. Секретов в текстовых полях нет
Проверять и headerParameters, и тело запроса, и константы внутри Code-нод — на момент аудита секреты жили во всех трёх местах. Bearer <token> → httpBearerAuth (хранит без префикса); прочие заголовки → httpHeaderAuth; несколько заголовков или заголовки+query → httpCustomAuth. (R13)
ГЕЙТ 5. Webhook-триггер имеет аутентификацию
Ни один webhook не публикуется с «No credentials required». Оценивать blast radius: webhook, принимающий произвольный fileId или произвольный id объекта, опаснее webhook, работающего по фиксированному объекту. (R12)
ГЕЙТ 6. Сверка полей, уязвимых к R1b — после КАЖДОГО update_workflow, не только первого
Открыть UI и сверить глазами:
* credentials на затронутых нодах;
* fx-режим в IF/Switch (выражения могли стать строковыми литералами);
* matchingColumns и реальный gid листа (sheetName.value, не подпись);
* connections.<IF>.main — должно быть 2 массива для каждого IF, чьи обе ветки используются.
Последний пункт — прямое следствие рецидива: в OzonRawАналитика false-ветку чинили 07-04, к 07-23 она снова отсутствует, а description утверждает, что исправлено. Одноразовая проверка этот класс не ловит.
НИКОГДА не использовать update_workflow для миграции credential — перетирает cachedResultName ссылок на листы Sheets, тихая потеря конфига.
КАЧЕСТВО 7. Тест
prepare_test_pin_data + test_workflow дали ожидаемый результат. Автопиннятся триггеры, ноды с credentials, HTTP Request. Выполняются по-настоящему: Code, Edit Fields, If, Data Tables, файловые операции, вызовы сабворкфлоу. ПРИ ПОБОЧНЫХ ЭФФЕКТАХ — СПРОСИТЬ АНДРЕЯ ДО ЗАПУСКА.
КАЧЕСТВО 8. Timezone
settings.timezone задан явно для всего, что по расписанию (Europe/Moscow), cron сразу в часах МСК. Не полагаться на смещение +3 при tz сервера Berlin. (R7)
Живой дефект: WB FBS Decision Engine (S4rZMUkI21dVu3ML) — timezone не задан, при этом воркфлоу принимает решения относительно дедлайна 16:00 МСК. Живой эталон: WB FBS Morning Forecast (6M9nS9iKQzMdztUs) — timezone и errorWorkflow оба заданы.
КАЧЕСТВО 9. Именование и description
Имя воркфлоу с глагола, description заполнен, ноды переименованы из дефолтных в NN_Название.
ОТДЕЛЬНО: description НЕ является доказательством. Аудит нашёл минимум три случая расхождения с кодом (OzonRawАналитика — «ветка подключена» при отсутствующей ветке; OZON Reviews Archive — «ТЕСТ ARCHIVE_DAYS=0» при ARCHIVE_DAYS=30 в коде). Проверять по connections и коду, description читать как гипотезу.
КАЧЕСТВО 10. Публикация
* Вкладка редактора закрыта до MCP-записи (race, last-write-wins, иногда молча). Живое подтверждение: SYS Canary (B5jkqW0bUScxmTi7), description — «предыдущий раз затёрт сохранением из устаревшей вкладки браузера».
* update_workflow НЕ ПУБЛИКУЕТ. Черновик живёт до publish_workflow.
* Для активного воркфлоу — полный тумблер unpublish_workflow → publish_workflow (R2), иначе триггер не перерегистрируется: воркфлоу active, versionId==activeVersionId, конфиг цел, executions нет.
* После publish сверить activeVersion с nodes. Пример расхождения (ИСТОРИЧЕСКИЙ, исправлен к 2026-07-22): DOSSIER Build CORPUS+REGISTRY (W3KjaXVqWD2c02IK) — на момент аудита 07-23 правка была в UI, нажат Save, не Publish; активная версия ограничивала прогон одним файлом вместо двенадцати. Проверено живым чтением 2026-08-04: лимит снят, activeVersion синхронизирована с draft, description подтверждает фикс («Снят Limit(1) после успешной калибровки… полный прогон на 12 из 13»). Пример сохранён как класс ошибки (Save≠Publish), не как текущее состояние этого воркфлоу. Тот же класс: OZON RAW Analytics History Load, WB Reviews History Load.
КАЧЕСТВО 11. Верификация результата — только по объекту воздействия
Целевая таблица / Doc / БД: появилась ли строка, изменился ли created_at. НЕ по статусу execution и НЕ по логу: успешные прогоны данных нод не хранят. Считать число прогонов write-ноды, а не итоговый статус. (R4)
КАЧЕСТВО 12. После публикации — никаких автономных действий
Ни publish, ни unpublish, ни update, ни archive, ни «запущу посмотреть». Проблему вынести, фикс предложить, ждать явного «да» на каждый шаг.
