# units_C — group C (sheets.md, infra.md), old text
Format: U<n> | CLASS | file:line | verbatim quote | paraphrase

## sheets.md
U1 | АДРЕС | sheets.md:3 | Номера разделов — прежние, общие с SKILL.md. | Section numbers are shared with SKILL.md
U2 | ПРАВИЛО | sheets.md:3 | Читать: перед любой работой с Google Sheets. | Trigger to read this file: before any Sheets work
U3 | ПРАВИЛО | sheets.md:6 | запись идёт только на отдельный лист, который создаёт сессия или робот | If another person works on the file (per Andrei), write only to a separate sheet created by session/robot
U4 | ПРАВИЛО | sheets.md:6 | в существующие листы такого файла не пишут | Never write to existing sheets of such a file
U5 | ПРИЧИНА | sheets.md:6 | Технической защиты чужой работы нет | No technical protection of another's work exists
U6 | ПРИЧИНА | sheets.md:6 | историю версий Google воркфлоу не читает | Workflow does not read Google version history
U7 | ПРИЧИНА | sheets.md:6 | защищённые диапазоны сервисный аккаунт может не соблюдать (§6.2 (е)) | SA may ignore protected ranges (see infra 6.2 e)
U8 | СЛУЧАЙ | sheets.md:6 | Решение владельца 2026-07-23, подтверждено 2026-10-12 | Owner decision 2026-07-23, confirmed 2026-10-12 (WB_REVIEWS_INDEX; Р-30 archivarius/LOG.md)
U9 | АДРЕС | sheets.md:6 | запись Р-30 журнала `projects/archivarius/LOG.md` | Address of the decision evidence
U10 | ПРАВИЛО | sheets.md:8 | Чтение Google Sheets — только gsheets-read | Sheets reading only via gsheets-read
U11 | ПОРОГ | sheets.md:8 | n8n `kRz5VVlxA1LiY7KG` | gsheets-read workflow ID
U12 | ПОРОГ | sheets.md:10 | sheetName?, range?, render?, maxRows? | gsheets-read request body {fileId, mode meta or range, sheetName?, range?, render?, maxRows?}
U13 | ПОРОГ | sheets.md:10 | `{success, fileId, mode, spreadsheetTitle, sheets, sheetName, range, render, row | gsheets-read response fields
U14 | ПРАВИЛО | sheets.md:11 | `executionMode: manual` (в production тело ответа не возвращается | Call with executionMode manual
U15 | ПРИЧИНА | sheets.md:11 | в production тело ответа не возвращается и execution не виден — R4 | In production the response body is not returned and execution invisible (root R4)
U16 | ПОРОГ | sheets.md:11 | `triggerNodeName: "01_Webhook"` | Trigger node name for gsheets-read
U17 | АДРЕС | sheets.md:11 | форма `inputs` — §3 основного файла | Form of inputs: SKILL.md §3
U18 | ПОРОГ | sheets.md:11 | Вебхук закрыт [тип ключа вебхука — вычищено по И-7] | gsheets-read webhook protected with [тип ключа вебхука — вычищено по И-7]
U19 | СЛУЧАЙ | sheets.md:11 | как и все вебхуки инстанса по снимку registry/n8n-map.md 2026-09-26, включая `gd | All instance webhooks closed per snapshot 2026-09-26, incl. gdocs-read previously open
U20 | СЛУЧАЙ | sheets.md:12 | ПРЕДУПРЕЖДЕНИЕ, проверка владельцем (позиция AH-19 очереди) | Warning, owner-check pending (queue pos. AH-19; to be replaced by task t-webhook-key-reuse per queue item 3.2)
U21 | СЛУЧАЙ | sheets.md:12 | по данным исполнений 74338 и 74345 (2026-10-03) | Evidence: executions 74338, 74345 on 2026-10-03
U22 | ПРИЧИНА | sheets.md:12 | вебхук gsheets-read закрыт не тем ключом, что gdocs-read и остальные вебхуки Кан | gsheets-read webhook key differs from the other Channel webhooks
U23 | ПОРОГ | sheets.md:12 | credential типа [тип ключа вебхука — вычищено по И-7], заведённым под [токен маркетплейса — вычищено по И-7] [назначение — вычищено по И-7] | The key is a [тип ключа вебхука — вычищено по И-7] credential made for the [marketplace token — redacted per I-7] (security-class particular)
U24 | ПРИЧИНА | sheets.md:12 | Если в нём лежит действующий [токен маркетплейса — вычищено по И-7], этот токен служит паролем вебхука. | If it holds a live marketplace token, that token is the webhook password
U25 | ПРИЧИНА | sheets.md:12 | На вызов из сессии через MCP это не влияет (MCP проходит мимо [тип ключа вебхука — вычищено по И-7]) | MCP calls bypass [тип ключа вебхука — вычищено по И-7], unaffected
U26 | ПРАВИЛО | sheets.md:12 | этот credential не трогать и не переименовывать | Do not touch or rename that credential until owner replaces the key
U27 | ПРИЧИНА | sheets.md:12 | от него зависит и вебхук, и, возможно, обращения к WB | Both webhook and possibly WB calls depend on it
U28 | ПРАВИЛО | sheets.md:12 | После решения владельца сюда записывается, какой ключ закрывает вебхук. | After owner decision, record which key closes the webhook here
U29 | ПРАВИЛО | sheets.md:14 | СНАЧАЛА `mode:"meta"` — список листов с их размерами. | First mode meta
U30 | ПРАВИЛО | sheets.md:14 | Диапазон вслепую не запрашивать. | Never request a range blind
U31 | ПРАВИЛО | sheets.md:14 | Затем `mode:"range"` на конкретный лист. | Then mode range on a concrete sheet
U32 | ПОРОГ | sheets.md:16 | `fileId` всегда; `mode` всегда (иное значение → throw); `sheetName` при `mode:"r | Required fields; invalid mode -> throw
U33 | ПРАВИЛО | sheets.md:16 | Имя листа экранируется внутри воркфлоу, руками кавычки не подставлять. | Sheet name escaped in workflow; don't add quotes by hand
U34 | ПОРОГ | sheets.md:18 | A1 без имени листа (`A1:G12`). Без него читается весь лист. | range is A1 without sheet name; omitted -> whole sheet
U35 | ПОРОГ | sheets.md:20 | `UNFORMATTED_VALUE` — числа числами (по умолчанию) | render default UNFORMATTED_VALUE
U36 | ПОРОГ | sheets.md:20 | `FORMATTED_VALUE` — как отображается в интерфейсе | render FORMATTED_VALUE
U37 | ПОРОГ | sheets.md:20 | `FORMULA` — текст формул вместо результатов | render FORMULA
U38 | ПРАВИЛО | sheets.md:20 | Формулу (VLOOKUP, IMPORTRANGE) не отдаёт ни один текстовый экспорт и ни один дру | Only render FORMULA returns formulas; no text export does
U39 | ПОРОГ | sheets.md:22 | Даты приходят сериальными числами Google Sheets, не строками. | Dates arrive as serial numbers
U40 | ПРАВИЛО | sheets.md:24 | Ложная ошибка тяжёлой книги. | Heavy-book false "Document ... is missing" error
U41 | ПРИЧИНА | sheets.md:24 | На книге, которая пересчитывается минутами (sku_cost_Шаблон), обращение к ней мо | Heavy recalculating book may answer "missing" though file exists
U42 | СЛУЧАЙ | sheets.md:24 | прогон книги «Деньги» 2026-09-30 ждал ответа 349 секунд | Case: book "Деньги" 2026-09-30, 349 s wait, then error
U43 | СЛУЧАЙ | sheets.md:24 | gsheets-read (исполнение 72163, 11 секунд) файл видели; повторный прогон прошёл | Case: execution 72163 saw the file in 11 s; retry succeeded
U44 | АДРЕС | sheets.md:24 | (`labs/ozon-ue/t-cost-history-copy.md`) | Evidence address of heavy-book case
U45 | ПРОВЕРКА | sheets.md:24 | Перед выводом «файл удалён» — повторить запрос и проверить файл get_file_metadat | Before concluding "file deleted": repeat request and check get_file_metadata
U46 | ПРАВИЛО | sheets.md:26 | Оформления `gsheets-read` не отдаёт ни в одном режиме | gsheets-read returns no formatting in any mode
U47 | ПОРОГ | sheets.md:26 | числовые форматы, ширины колонок, высоты строк, заливка, шрифт, правила условног | List of absent formatting items
U48 | ПРАВИЛО | sheets.md:26 | Оформление снимается только дампом через Apps Script, который запускает владелец | Formatting only via Apps Script dump run by owner
U49 | ПРАВИЛО | sheets.md:26 | скрипт пишет снимок на отдельный лист или в отдельную книгу, и этот снимок читае | Snapshot to separate sheet/book, read via range
U50 | АДРЕС | sheets.md:26 | Порядок — Skill `apps-script-sheets`, пункт 1 «Порядок работы» (позиция AG-18 оч | Procedure address: apps-script-sheets item 1
U51 | ПРОВЕРКА | sheets.md:29 | `success:true`, `truncated:false` — диапазон прочитан целиком. | State 1: fully read
U52 | ПРОВЕРКА | sheets.md:30 | `success:true`, `truncated:true` — в диапазоне больше строк, чем `maxRows` (по у | State 2: truncated, maxRows default 500
U53 | ПРАВИЛО | sheets.md:30 | Возвращённые строки НЕ являются всем диапазоном — сузить диапазон или поднять `m | Narrow range or raise maxRows when truncated
U54 | ПОРОГ | sheets.md:30 | Число реальных строк — в `reason` и `rowCount`. | Real row count is in reason and rowCount
U55 | ПРОВЕРКА | sheets.md:31 | `success:true`, `rows:[]` с текстом EMPTY RANGE в `reason` — диапазон прочитан у | State 3: empty range = success
U56 | ПРИЧИНА | sheets.md:31 | Sheets API не присылает поле `values`, когда данных нет. | API omits values when no data
U57 | ПРАВИЛО | sheets.md:28 | Три состояния ответа, которые НЕЛЬЗЯ путать | The three states must not be confused
U58 | ПРАВИЛО | sheets.md:32 | При `success:false` смотреть `reason` | On failure read reason
U59 | ПОРОГ | sheets.md:32 | выключенный Sheets API в GCP-проекте `[проект Google Cloud — вычищено по И-7]` (SERVICE_DISABLED — | reason distinguishes disabled Sheets API in GCP project [проект Google Cloud — вычищено по И-7] (SERVICE_DISABLED not a sharing issue)
U60 | ПОРОГ | sheets.md:32 | файл не найден или не расшарен на SA, и отказ по правам | reason also distinguishes not-found/not-shared and permission denial
U61 | ПРАВИЛО | sheets.md:35 | `read_file_content` (MCP) — §0 п.2 действует и для таблиц | Forbidden: read_file_content for sheets
U62 | ПРИЧИНА | sheets.md:35 | порог обрезки большого файла неизвестен (§0, абзац «Порог обрезки»), а адресации | Truncation threshold unknown and no sheet/range addressing
U63 | ПРАВИЛО | sheets.md:36 | Экспорт в `text/csv` через `download_file_content` | Forbidden: text/csv export via download_file_content
U64 | ПРИЧИНА | sheets.md:36 | Google экспортирует ТОЛЬКО ПЕРВЫЙ ЛИСТ, без предупреждения. | CSV export gives only first sheet silently
U65 | ПРИЧИНА | sheets.md:36 | На многолистовом файле это тихая потеря остальных листов. | Silent loss of other sheets
U66 | ПОРОГ | sheets.md:36 | `read_file_content` по таблице отдаёт лишь образец около 5 строк на лист | read_file_content gives ~5-row sample per sheet
U67 | СЛУЧАЙ | sheets.md:36 | (`projects/deklaration-ozon/LOG.md`, Т-3) | Evidence address T-3
U68 | ПОРОГ | sheets.md:36 | Все листы книги целиком одним файлом даёт только экспорт .xlsx | Only .xlsx export gives all sheets in one file
U69 | ПРАВИЛО | sheets.md:37 | Добавлять в `gsheets-read` запись. | Forbidden: adding write to gsheets-read
U70 | ПРИЧИНА | sheets.md:37 | чтение и запись в одном вебхуке с произвольным `fileId` расширяют blast radius ( | Read+write in one webhook with arbitrary fileId widens blast radius
U71 | ПРАВИЛО | sheets.md:39 | `download_file_content` с `exportMimeType: application/vnd.openxmlformats-office | One-off full dump: export xlsx
U72 | ПРАВИЛО | sheets.md:39 | `openpyxl` (`data_only=False` — формулы, `data_only=True` — значения) | Read with openpyxl; data_only flag meaning
U73 | ПРИЧИНА | sheets.md:39 | инструмент возвращает файл base64-строкой В ОТВЕТ и сам файла на диске не создаё | Tool returns base64 in response, no file on disk
U74 | СЛУЧАЙ | sheets.md:39 | (позиция AG-18 очереди) | Queue pos. AG-18 as evidence
U75 | ПОРОГ | sheets.md:39 | такое наблюдалось в среде с bash при ответе выше примерно 50 КБ, порог не гарант | Bash env put large response in file above ~50 KB, not guaranteed
U76 | АДРЕС | sheets.md:39 | (`registry/tools.md`, абзац «Чтение больших ответов») | Address for large-response reading
U77 | ПРИЧИНА | sheets.md:39 | Если ответ пришёл в контекст, путь закрыт: base64 через контекст портится (§2.2 | If response in context the path is closed: base64 corrupts through context
U78 | ПРАВИЛО | sheets.md:39 | перед тем как ставить этот путь шагом плана, его проверяют в своей среде одним в | Test the path with one call before planning it
U79 | ИСКЛЮЧЕНИЕ | sheets.md:39 | в Claude Project без bash он неисполним | In a Claude Project without bash the path is infeasible
U80 | ПРАВИЛО | sheets.md:41 | `gsheets-read` — когда нужно посмотреть (структура, диапазон, формула). | Choice: gsheets-read to look
U81 | ПРАВИЛО | sheets.md:41 | Среда с bash и .xlsx на диске — когда нужно посчитать по всему массиву в десятки | Choice: bash+xlsx for computing over tens of thousands of rows
U82 | ПРАВИЛО | sheets.md:41 | Дамп Apps Script — когда нужно оформление. | Choice: Apps Script dump for formatting
U83 | ПОРОГ | sheets.md:43 | gsheets-append (n8n `LNlWIEdH0tkzmqPB`) | gsheets-append workflow ID
U84 | СЛУЧАЙ | sheets.md:45 | заведён 2026-09-26 сессией через MCP, активен. Контракт снят чтением воркфлоу 20 | Created 2026-09-26, active; contract read 2026-09-27 v 6db5d98c; name «Claude → Google Sheets Append»
U85 | ПОРОГ | sheets.md:47 | body `{fileId, sheetName, rows}` → `{success, fileId, sheetName, rowsRequested, | gsheets-append request/response fields
U86 | ПОРОГ | sheets.md:48 | `rows` — непустой массив строк, каждая строка — массив значений ячеек (`[["2026- | rows format
U87 | ПРАВИЛО | sheets.md:48 | `sheetName` — имя листа как есть, кавычки воркфлоу ставит сам | sheetName as is, no quotes
U88 | ПОРОГ | sheets.md:49 | воркфлоу падает на узле 02_Parse_Payload («Missing fileId», «Missing sheetName», | Invalid field -> crash at node 02_Parse_Payload with listed messages, no response
U89 | ПРОВЕРКА | sheets.md:49 | в режиме manual причина видна в статусе исполнения | In manual mode the cause is visible in execution status
U90 | ПРАВИЛО | sheets.md:50 | `executionMode: "manual"`, форма — §3 основного файла | Call via execute_workflow manual, form per SKILL.md §3
U91 | ПРАВИЛО | sheets.md:50 | имя узла-триггера брать из get_workflow_details | triggerNodeName taken from get_workflow_details
U92 | ПРАВИЛО | sheets.md:50 | `inputs: {webhookData: {method: "POST", body: {…}}}` без поля `type` | inputs form, no type field
U93 | ПОРОГ | sheets.md:50 | Вебхук закрыт [тип ключа вебхука — вычищено по И-7], вызов из сессии через MCP проходит мимо него. | Append webhook [тип ключа вебхука — вычищено по И-7]; MCP bypasses
U94 | ПОРОГ | sheets.md:52 | `values:append` к диапазону `'<лист>'!A1` с параметрами `valueInputOption=USER_E | Mechanism of append request
U95 | ПОРОГ | sheets.md:52 | под тем же сервисным аккаунтом (googleApi), что gsheets-read | Same service account as gsheets-read
U96 | ПРАВИЛО | sheets.md:52 | Книга должна быть расшарена на сервисный аккаунт с правом редактора; иначе `succ | Book must be shared with SA as editor else permission denied
U97 | ПРОВЕРКА | sheets.md:52 | `success:true` ставится только при наличии в ответе Google объекта `updates`; бе | success true only if updates present; else APPEND DID NOT HAPPEN
U98 | ПРАВИЛО | sheets.md:55 | Строка, начинающаяся с `=`, становится живой формулой | USER_ENTERED trap: = makes formula
U99 | ПРИЧИНА | sheets.md:55 | число и дата разбираются по локали книги (у книг Андрея `ru_RU`: «1,5» — число, | Locale parsing of numbers/dates; claim ru_RU for Andrei's books (disputed by queue item 3.3)
U100 | ПРИЧИНА | sheets.md:55 | строка вида «+49…» может стать числом | "+49..." may become number
U101 | ПРАВИЛО | sheets.md:55 | Текст, который должен остаться текстом, передавать с ведущим апострофом (`"'=A1" | Pass text with leading apostrophe
U102 | ПРИЧИНА | sheets.md:56 | Место дозаписи выбирает Google: он ищет «таблицу» от ячейки A1 листа и пишет пос | Google picks append place: table from A1, after last row
U103 | ПРИЧИНА | sheets.md:56 | Если на листе есть пустая строка внутри данных, запись может лечь в середину лис | Empty row inside data -> write mid-sheet
U104 | ПРИЧИНА | sheets.md:56 | `INSERT_ROWS` вставляет новые строки, а не перезаписывает ниже лежащие | INSERT_ROWS inserts rather than overwrites
U105 | ПРОВЕРКА | sheets.md:56 | фактический адрес всегда смотреть в `updatedRange` | Always check actual address in updatedRange
U106 | ПРИЧИНА | sheets.md:57 | Узел запроса (03_HTTP_Append) стоит с `retryOnFail`, а `values:append` не идемпо | Node 03_HTTP_Append has retryOnFail; append not idempotent
U107 | ПРИЧИНА | sheets.md:57 | если первый запрос дошёл до Google, но ответ потерялся по таймауту, повтор допиш | Lost response -> retry duplicates rows
U108 | ПРАВИЛО | sheets.md:57 | после любого `success:false` с причиной «request failed…» сначала читать лист, п | After request failed read sheet first, don't retry blind
U109 | АДРЕС | sheets.md:57 | (тот же класс, что E16) | Same class as E16 (failures.md)
U110 | ПРОВЕРКА | sheets.md:59 | Проверка — не ответ воркфлоу, а чтение: gsheets-read `mode:"range"` по диапазону | Verification by read-back of updatedRange
U111 | ПРОВЕРКА | sheets.md:59 | сверка числа строк с `rowsRequested` и значений с отправленными | Compare row count to rowsRequested and values to sent
U112 | ПРИЧИНА | sheets.md:59 | Узел запроса — `n8n-nodes-base.httpRequest`: ответ Google оседает в contextData, | httpRequest response lands in contextData but small; leak cheap
U113 | СЛУЧАЙ | sheets.md:61 | Паспорта у воркфлоу нет, строки PASSPORT в description нет. | gsheets-append has no passport / PASSPORT line
U114 | ПРАВИЛО | sheets.md:63 | Создание таблиц — два пути, оба скриптовые | Table creation: two script-based paths
U115 | ПРАВИЛО | sheets.md:65 | «структура таблицы создаётся кодом, а не руками в интерфейсе» | Rule: structure by code not by hand 
U116 | ПРАВИЛО | sheets.md:66 | Скрипт вставляется в script.google.com и запускается владельцем вручную (Run). | Path 1 Apps Script: pasted in script.google.com, owner runs
U117 | ПРАВИЛО | sheets.md:66 | Путь для книги, которую дальше перестраивает тот же скрипт: витрины, оформление, | Path 1 is for books rebuilt by the same script
U118 | ПРАВИЛО | sheets.md:67 | Сессия создаёт пустую книгу от имени владельца коннектором Drive в нужной папке | Path 2: session creates empty book via Drive connector as owner
U119 | ПРАВИЛО | sheets.md:67 | расшаривает её на сервисный аккаунт с правом редактора | Share book to SA as editor
U120 | ПРАВИЛО | sheets.md:67 | листы, шапки и служебные колонки создаёт сам воркфлоу, который с этой книгой раб | Sheets/headers/service columns created by workflow at first run
U121 | ПРОВЕРКА | sheets.md:67 | проверять результат чтением, а не ответом create_file | Verify create_file by reading (exact call parameters not recorded)
U122 | ПРАВИЛО | sheets.md:67 | Путь для книги, которую ведёт робот n8n. | Path 2 is for books run by n8n robot
U123 | СЛУЧАЙ | sheets.md:67 | Так создана книга «Описания карточек» проекта card-content-sync (`projects/card- | Case: «Описания карточек» created 2026-10-05, Р-6
U124 | ПРИЧИНА | sheets.md:67 | Создать файл сам сервисный аккаунт не может (Forbidden, §2.1 абзац «Кто создаёт | SA cannot create files (Forbidden)
U125 | ПРОВЕРКА | sheets.md:68 | Проверка в обоих путях одна: чтение созданного через gsheets-read `mode:"meta"` | Verification same for both paths: read meta and range of headers
U126 | СЛУЧАЙ | sheets.md:69 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-09 раздел назывался «только через Apps Script» и за | History: before 2026-10-09 only Apps Script, second path applied 2026-10-05, recognized 2026-10-08 (В8) - history block
U127 | ПРАВИЛО | sheets.md:71 | ПЕРЕД ЛЮБОЙ ПЕРЕДЕЛКОЙ СУЩЕСТВУЮЩЕЙ КНИГИ читать парный Skill `apps-script-sheet | Before reworking an existing book read apps-script-sheets
U128 | ПРАВИЛО | sheets.md:72 | `setFormula` пишет формулу буквально, без перевода в локаль книги (ru_RU: раздел | Trap: setFormula literal, no locale translation (ru_RU claim disputed by queue item 3.3)
U129 | ПРАВИЛО | sheets.md:73 | редактор Apps Script запускает первую функцию файла, а не выбранную мысленно | Trap: editor runs first function in file
U130 | ПРАВИЛО | sheets.md:74 | очистка листа без предварительного поиска ссылок на него убивает чужие формулы м | Trap: clearing sheet without finding references kills formulas silently
U131 | ПРИЧИНА | sheets.md:71 | каждая из которых уже стоила полного прогона | Each of three traps already cost a full run
U132 | ПОРОГ | sheets.md:77 | условное правило форматирования называется `whenFormulaSatisfied`, не `whenFormu | Name whenFormulaSatisfied not whenFormula
U133 | ПРАВИЛО | sheets.md:78 | единое пространство имён, одна `onOpen`, константы с префиксом | One namespace, one onOpen, prefixed constants
U134 | ПРАВИЛО | sheets.md:79 | при чтении параметров даёт тихий ноль — всегда валидировать пороги | parseFloat(x)||0 gives silent zero; always validate thresholds, throw on invalid, never substitute 0
U135 | ПРАВИЛО | sheets.md:80 | условное форматирование пересоздавать через Apps Script (`setupConditionalFormat | Recreate conditional formatting via Apps Script, not UI
U136 | ПРАВИЛО | sheets.md:83 | Get Row(s) без фильтров; колонка A:A может прийти как `'A: field'` — проверять о | Get Row(s) no filters; column A may come as 'A: field' check both
U137 | ПОРОГ | sheets.md:84 | У чтения Sheets версии 4.7 опции ограничения числа строк нет | Sheets read v4.7 has no row-limit option
U138 | ПОРОГ | sheets.md:84 | только `filtersUI`, `combineFilters` и в `options` — `dataLocationOnSheet`, `out | Option list of v4.7 read
U139 | СЛУЧАЙ | sheets.md:84 | (описание узла прочитано 2026-10-11 и 2026-10-12) | Node description read 2026-10-11/12
U140 | ПРАВИЛО | sheets.md:84 | Порцию ограничивать отдельным узлом Limit после чтения | Limit batch via separate Limit node after read
U141 | СЛУЧАЙ | sheets.md:84 | без него 83 строки листа дали 83 параллельных вызова внешнего API (WB_REVIEWS_IN | Case: 83 rows -> 83 parallel API calls
U142 | ПРАВИЛО | sheets.md:84 | Между узлами, которые сопоставляют элементы по позиции через `$items`, режим узл | Don't change Limit mode between nodes pairing by $items
U143 | ПРАВИЛО | sheets.md:84 | Delete Start Row — через expression. | Delete Start Row via expression
U144 | СЛУЧАЙ | sheets.md:85 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-12 здесь стояло «returnAllMatches+limit конфликтуют | History block: refuted limit option claim (У-161); real fact: node has no limit option
U145 | ПРАВИЛО | sheets.md:86 | `documentId`/`sheetName` через expression `={{ 'ID' }}`. | documentId/sheetName via expression
U146 | ПРАВИЛО | sheets.md:86 | Разделитель формул — `;`. | Formula separator ;
U147 | ПРАВИЛО | sheets.md:86 | Прямая ссылка `=sheet!$K$4` вместо VLOOKUP. | Direct reference instead of VLOOKUP
U148 | ПОРОГ | sheets.md:86 | IMPORTRANGE ломается на таблицах >18000 строк — писать напрямую из n8n. | IMPORTRANGE breaks above 18000 rows; write directly from n8n
U149 | ПРИЧИНА | sheets.md:87 | Режим Map Automatically (`autoMapInputData`) у записи (update, appendOrUpdate) п | autoMapInputData writes every field with same-named column and replaces formula with value
U150 | ПРИЧИНА | sheets.md:87 | поля, которого во входе нет, не трогает — частичное обновление выглядит как част | Missing fields are untouched; partial update looks like partial loss
U151 | ПРОВЕРКА | sheets.md:87 | различает их вопрос «целы ли поля того же источника» (корень R6 n8n-engineering- | Distinguish by whether same-source fields intact (R6)
U152 | ПРИЧИНА | sheets.md:87 | опция `handlingExtraData` по умолчанию `insertInNewColumn` (описание узла 4.7 пр | Extra-data field creates new column by default
U153 | ПРАВИЛО | sheets.md:87 | Колонки с формулами во вход записи не включать | Don't include formula columns in write input
U154 | ПРАВИЛО | sheets.md:87 | брать Map Each Column Below (`defineBelow`) — он пишет только сопоставленные кол | Use defineBelow when computed fields must not be written
U155 | ПОРОГ | sheets.md:87 | `defineBelow` через `create_workflow_from_code` сохраняется. | defineBelow survives create_workflow_from_code
U156 | СЛУЧАЙ | sheets.md:87 | Проба 2026-10-12, воркфлоу `dEMUvxBGI6JIp4vQ`, исполнение 79035 | Probe 2026-10-12 workflow dEMUvxBGI6JIp4vQ exec 79035
U157 | АДРЕС | sheets.md:87 | (запись Р-31 журнала `projects/archivarius/LOG.md`, строка 7 `meta/PENDING_RULES | Evidence addresses
U158 | СЛУЧАЙ | sheets.md:87 | прецедент — посчитанное поле перезаписано в листе (WB_REVIEWS_INDEX) | Precedent: computed field overwritten in sheet
U159 | ПРИЧИНА | sheets.md:88 | `cellFormat` по умолчанию `USER_ENTERED` — те же ловушки, что у gsheets-append ( | Node cellFormat default USER_ENTERED, same traps as append
U160 | ПРАВИЛО | sheets.md:89 | Ошибка «Column to Match On required» у Update Row: не задана колонка сопоставлен | Error cause: matching column not set
U161 | ПОРОГ | sheets.md:89 | для update `matchingColumns` обязателен в обоих режимах (описание узла 4.7) | matchingColumns required in both modes for update
U162 | ПРАВИЛО | sheets.md:89 | Задать её; переключение на Map Automatically, которым ошибку обошли | Set the column; switching to Map Automatically (used to bypass the error) changes which fields are written | Set it; switching to Map Automatically changes written fields
U163 | СЛУЧАЙ | sheets.md:89 | прецеденте (N8N_JOURNAL_2026) | Precedent source N8N_JOURNAL_2026
U164 | СЛУЧАЙ | sheets.md:90 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-12 здесь стояло «defineBelow может не генерироватьс | History: refuted claim defineBelow may not be generated; refuted by probe 2026-10-12
U165 | ПРАВИЛО | sheets.md:91 | COUNTIFS/SUMIFS с границами суток (`">="&A2` / `"<"&(A2+1)`) | Daily aggregation with day boundaries
U166 | ПРАВИЛО | sheets.md:92 | после структурных правок — Refresh columns list → Save → Publish | Schema cache: refresh columns -> Save -> Publish after structural edits
U167 | ПРАВИЛО | sheets.md:93 | 429 при appendOrUpdate → Wait 2с и повторить | On 429 Wait 2s and retry (DISPUTED: contradictions 3a-5: pause >=60 s via continueErrorOutput; retryOnFail and 2 s do not survive the minute window)
U168 | ПРАВИЛО | sheets.md:93 | удаление >5 строк — splitInBatches(5)+Wait(2s) | Delete >5 rows: splitInBatches(5)+Wait 2s
U169 | ПРАВИЛО | sheets.md:93 | защита заголовка `if(min(rows)<=1)throw` | Header protection throw if min(rows)<=1
U170 | ПРАВИЛО | sheets.md:93 | `appendOrUpdate` всегда с явными `matchingColumns` (иначе тихие дубли) | appendOrUpdate always explicit matchingColumns
U171 | ПРИЧИНА | sheets.md:93 | составной `matchingColumns` матчит только первую колонку и перезаписывает вторую | Composite matchingColumns matches only first column and overwrites second
U172 | СЛУЧАЙ | sheets.md:93 | проба 2026-10-12: вход A/y обновил строку A/x, и строк A/y стало две; исполнение | Probe: input A/y updated row A/x, two A/y rows; exec 79035
U173 | ПРАВИЛО | sheets.md:93 | составной ключ собирать в одну колонку | Assemble composite key in a single column
U174 | ПРАВИЛО | sheets.md:94 | Частые правки нескольких файлов подряд — пауза 1–2с между batchUpdate-вызовами, | Pause 1-2 s between batchUpdate calls; retry on 429 (preventive pause kept per 3a-5)
U175 | ПРАВИЛО | sheets.md:97 | Локаль таблицы проверять ДО генерации формул | Check locale before generating formulas
U176 | ПРИЧИНА | sheets.md:97 | функции RU (`ЕСЛИ`) или EN (`IF`) — по локали конкретной таблицы, иначе `#NAME?` | RU vs EN function names by sheet locale else #NAME?
U177 | ПРАВИЛО | sheets.md:98 | нет нативного OR — использовать арифметику `(усл1)+(усл2)>0` | FILTER: no native OR, use arithmetic
U178 | ПРИЧИНА | sheets.md:98 | пустой результат без обёртки даёт ошибку в ячейке | Empty FILTER result without wrapper gives error
U179 | ИСКЛЮЧЕНИЕ | sheets.md:98 | Обёртка `IFERROR(...,"текст")` допустима только для пустого результата, который | IFERROR wrapper only for empty result truly meaning no data
U180 | ПРИЧИНА | sheets.md:98 | она же прячет ошибку «Result was not automatically expanded» при нехватке строк, | IFERROR hides "not automatically expanded" error; cost silently zero
U181 | ПРАВИЛО | sheets.md:98 | рядом с обёрнутым FILTER ставится контрольная ячейка с числом строк источника | Put control cell with source row count next to wrapped FILTER
U182 | АДРЕС | sheets.md:98 | Skill apps-script-sheets, references/book-traps.md, раздел о склейке IMPORTRANGE | Address of book trap
U183 | ПРАВИЛО | sheets.md:99 | `TEXTJOIN(IF(...))` при автозаполнении не вычисляется как массив без `ARRAYFORMU | TEXTJOIN(IF) needs ARRAYFORMULA wrapping
U184 | ПОРОГ | sheets.md:102 | Единственный рабочий путь PDF→Doc из Apps Script — Drive API v2: `Drive.Files.in | PDF->Doc only Drive API v2 Files.insert convert:true
U185 | ПРИЧИНА | sheets.md:102 | v3 не работает для конвертации | v3 doesn't convert
U186 | ПРАВИЛО | sheets.md:102 | Требует подключения сервиса Drive v2 в проекте Apps Script. | Requires enabling Drive v2 service in Apps Script project

## infra.md
U187 | ПРАВИЛО | infra.md:3 | Читать: перед работой с бэкапом и при отказе записи, похожем на проблему прав. | Trigger to read infra.md
U188 | АДРЕС | infra.md:3 | Номера разделов — прежние, общие с SKILL.md. | Shared section numbers
U189 | ПОРОГ | infra.md:6 | PostgreSQL → Google Drive ежедневно, remote gdrive. | Backup PostgreSQL -> Drive daily, remote gdrive (STALE: backup stopped 2026-09-14, task t-n8n-backup-stopped, queue item 3.1)
U190 | ПРИЧИНА | infra.md:7 | Бэкап базы и оригиналы документов лежат в одном Google-аккаунте. | Backup and originals in one Google account
U191 | ПРИЧИНА | infra.md:7 | Успешное учение восстановления этого не меняет: потерю аккаунта бэкап не пережив | Successful restore drill doesn't change; account loss kills backup
U192 | СЛУЧАЙ | infra.md:7 | (SYS_JOURNAL_2026, 2026-07) | Evidence address
U193 | ПРАВИЛО | infra.md:7 | Шаг 0 любого восстановления — убедиться, что свежий бэкап есть, и знать, кто и г | Step 0 of restore: confirm fresh backup exists, know who/where
U194 | СЛУЧАЙ | infra.md:7 | На 2026-10-10 это нигде в репозитории не записано, кроме строки выше: по словам | As of 2026-10-10 nowhere recorded; task t-server-knowledge (STALE; superseded by t-n8n-backup-stopped)
U195 | ПРАВИЛО | infra.md:8 | apt-пакет rclone может быть собран без backend Mega — ставить официальным instal | apt rclone may lack Mega backend; install official script, pin version
U196 | ПРИЧИНА | infra.md:9 | Shared client_id rclone планово выводится Google из обращения | Shared rclone client_id being phased out by Google
U197 | ПРАВИЛО | infra.md:9 | использовать собственный client_id для gdrive-remote, иначе бэкапы молча останов | Use own client_id else backups stop silently
U198 | ПРОВЕРКА | infra.md:9 | `rclone config show <remote>:` — пустые client_id/client_secret означают использ | Check: empty client_id/secret = shared (threatened); filled or SA = fine
U199 | ПОРОГ | infra.md:14 | search_files, get_file_metadata, create_file, update_file, copy_file, trash_file | Connector tool list
U200 | ПРАВИЛО | infra.md:14 | read_file_content (последний — только по §0 п.2) | read_file_content only per §0 item 2
U201 | ПОРОГ | infra.md:14 | Авторизация — OAuth на стороне claude.ai, может протухать (см. E14 в §8) | Connector auth OAuth, may expire (E14)
U202 | ПРАВИЛО | infra.md:14 | лечится переподключением коннектора и новым чатом | Fix: reconnect connector and new chat
U203 | ПОРОГ | infra.md:15 | n8n-вебхуки (append/replace/overwrite/gdocs-read/gdocs-apply-from-file/gsheets-r | n8n webhooks use SA googleApi
U204 | ПРИЧИНА | infra.md:15 | SA-ключи не протухают по времени. | SA keys don't expire
U205 | ИСКЛЮЧЕНИЕ | infra.md:15 | Исключение — create_folder (`uapccJY1O4ykyDi7`): по снимку registry/n8n-map.md 2 | Exception: create_folder workflow uapccJY1O4ykyDi7 runs on googleDriveOAuth2Api (owner OAuth)
U206 | ПРАВИЛО | infra.md:15 | при отказе искать надо протухший OAuth, а не доступ SA | For create_folder failure look for expired OAuth not SA access
U207 | ПРАВИЛО | infra.md:16 | Это разные, независимые токены: один путь может лежать при полностью рабочем вто | Two independent tokens; determine which path failed first
U208 | ПРИЧИНА | infra.md:19 | Файл, не расшаренный на SA, даёт тихие отказы: 404 (overwrite) / 403 (replace) — | Unshared file gives silent 404 (overwrite)/403 (replace), confusable with typo
U209 | ПРАВИЛО | infra.md:20 | (а) При тихом неприменении записи — первым делом проверить get_file_permissions | (a) Silent non-application: check get_file_permissions first
U210 | ПРОВЕРКА | infra.md:21 | (б) Верификация — только read-back; `executionId: 'started'` не гарантия успеха. | (b) Verify by read-back only; executionId 'started' not proof
U211 | ПРАВИЛО | infra.md:22 | (в) Новые файлы вне уже расшаренных папок — проверять доступ SA ДО первой записи | (c) Check SA access before first write for new files outside shared folders
U212 | ПРИЧИНА | infra.md:22 | Создать файл в папке DOCS сервисный аккаунт не может вовсе (Forbidden): файл соз | SA cannot create files in DOCS; owner creates, robot overwrites
U213 | АДРЕС | infra.md:22 | — §2.1, абзац «Кто создаёт файл для робота» | Address §2.1
U214 | ПРИЧИНА | infra.md:22 | Корень «Мой диск» не расшарен никому, кроме владельца | My Drive root unshared except owner
U215 | СЛУЧАЙ | infra.md:22 | (get_file_permissions для `root` 2026-10-12: единственная запись — owner) | Case: root permissions 2026-10-12 only owner
U216 | ПРИЧИНА | infra.md:22 | файл в корне для воркфлоу не существует и даёт «not found or not shared to SA», | File in root invisible to workflow: «not found or not shared to SA»
U217 | СЛУЧАЙ | infra.md:22 | (Зона Б N8N_INDEX) | Evidence Zone B N8N_INDEX
U218 | СЛУЧАЙ | infra.md:22 | Копия, сделанная copy_file из документа, расшаренного сервисному аккаунту, наблю | Observed: copy_file copy keeps SA editor access via donor, folder unshared
U219 | ПРИЧИНА | infra.md:22 | а файл, созданный иначе, требует расшарки | File created otherwise needs sharing
U220 | СЛУЧАЙ | infra.md:22 | два наблюдения, SYS_JOURNAL_2026 строки 3265 и 4326; не перепроверено | Two observations, lines 3265 and 4326, not rechecked
U221 | ПРОВЕРКА | infra.md:22 | после copy_file права проверяются get_file_permissions | After copy_file check get_file_permissions
U222 | ПРАВИЛО | infra.md:23 | (г) При нескольких write-узлах в одном воркфлоу мигрировать credential на ВСЕХ у | (d) Migrate credential on ALL write nodes in one update_workflow (resolved: via setNodeCredential operations, atomic; owner decision 2026-10-20: session binds keys itself with setNodeCredential; cachedResultName probe not needed)
U223 | ПРИЧИНА | infra.md:23 | частичная миграция даёт частичный молчаливый отказ | Partial migration -> partial silent failure
U224 | ПРАВИЛО | infra.md:24 | (д) trash/delete через Drive API под SA возвращает HTTP 200 без реального эффект | (e) trash/delete under SA returns 200 with no effect; only under owner credential with read check
U225 | ИСКЛЮЧЕНИЕ | infra.md:24 | Инструмент коннектора trash_file работает от имени владельца и под это ограничен | Connector trash_file works as owner, exempt
U226 | АДРЕС | infra.md:24 | им же `second-brain-git` 8.3 убирает файл-источник Git Append File из папки _git | second-brain-git 8.3 uses trash_file to remove Git Append File source from _git_staging
U227 | ПРАВИЛО | infra.md:25 | (е) Защищённый диапазон листа не считать защитой от записи сервисного аккаунта | (f) Protected range is not protection from SA writes
U228 | СЛУЧАЙ | infra.md:25 | по записи 2026-07-19 сервисный аккаунт с правом редактора писал в защищённые яче | Case 2026-07-19 SA wrote to protected cells
U229 | ПРИЧИНА | infra.md:25 | Это расходится с обычным поведением Google, причина не установлена; не перепрове | Contradicts normal Google behavior, cause unknown, unverified since
U230 | ПРАВИЛО | infra.md:25 | Ячейки, которые робот не должен трогать, защищаются тем, что они не входят ни в | Protect robot-untouchable cells by excluding them from every write range
U231 | ПРАВИЛО | infra.md:26 | Credential в кэше «does not exist» → переключить на другой и вернуть обратно → S | Cached credential "does not exist": switch to another and back, Save, Publish

## NEW (from inputs)
N1 | ПРАВИЛО | queue AJ-14 / X-30 | ручной ввод и вывод робота держать на разных листах | Keep manual input and robot output on separate sheets
N2 | ПРИЧИНА | queue X-30 / PLAN.md:212 | робот, пересобирающий лист целиком, стирает ручные колонки | Robot rebuilding the whole sheet erases manual columns (root R18)
N3 | ПРИЧИНА | queue X-30 | раздельные листы снимают вопрос конструкцией, а не дисциплиной | Separate sheets remove the issue by construction, not discipline
N4 | АДРЕС | queue AJ-14 | карта, раздел 2, строка 109; projects/deklaration-v2/PLAN.md, строка 212 | Evidence addresses of X-30 (also root R18; concern recorded for ARTIKEL_PROPS in projects/deklaration-wb/STATE.md goal 5)
N5 | ПРАВИЛО | contradictions 3а-5 | при 429 по квоте повтор допустим после ожидания дольше минутного окна — ветка ошибки узла (continueErrorOutput) ведёт в Wait не меньше 60 секунд и затем в повтор | 429 quota retry only after Wait >=60 s via continueErrorOutput error branch; retryOnFail and 2 s pause don't survive window (replaces sheets.md:93 "Wait 2с")
N6 | ПРАВИЛО | contradictions 3а-5 | Корневое лечение — меньше вызовов (пакеты, служебное состояние вне Sheets). Пауза 1–2 секунды между вызовами как профилактика — остаётся. | Root cure fewer calls (batches, state outside Sheets); 1-2 s pause as prevention remains
N7 | ПРИЧИНА | contradictions 3а-5 | квота ReadRequestsPerMinutePerUser = 60 в минуту, общий счётчик для всех воркфлоу на одном сервисном аккаунте | Quota 60/min per user shared across workflows on one SA
N8 | ПРАВИЛО | contradictions 4 + decision 2026-10-20 | ключи доступа сессия привязывает сама операцией setNodeCredential | Credential migration: all nodes in one update_workflow of setNodeCredential ops (atomic); owner decision 2026-10-20 removes need for probe (infra.md:23)
N9 | ПРАВИЛО | queue 3.1 | устарело: бэкап базы n8n остановился 2026-09-14, задача labs/sys/t-n8n-backup-stopped.md | infra.md:6-7 stale: backup stopped 2026-09-14 (task t-n8n-backup-stopped); must not read "ежедневно" as current fact
N10 | АДРЕС | queue 3.2 | позицию AH-19 снять как дубль задачи labs/sys/t-webhook-key-reuse.md | sheets.md:12 warning address should become task t-webhook-key-reuse.md instead of queue position AH-19
N11 | ИСКЛЮЧЕНИЕ | queue 3.3 | ru_RU / разделитель «;» неверно как общее утверждение: у WB_RAW_Аналитика «;», у Price Master «,» | sheets.md:55,72 locale claim ru_RU is not universal (harvest finding В10)
N12 | ПРАВИЛО | contradictions 1 (decision) | устаревший инструмент снимается с публикации ... не архивируется | Deprecated tool is unpublished (active:false), not archived; (disputed text is in SKILL.md:61 - group A; not in sheets/infra)
N13 | ПРАВИЛО | contradictions 11 | вставка многострочного текста на место однострочного якоря допустима | Not in C files (home SKILL.md:101, group A) - listed for completeness
N14 | ПРАВИЛО | contradictions 7 | Инструмента «дописать в конец Зоны А» нет | Not in C files (home docs-write / handoff) - listed for completeness
