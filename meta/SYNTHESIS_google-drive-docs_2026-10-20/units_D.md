# units_D — old text of group D (references/mcp.md, references/failures.md), decomposed 2026-10-20 before seeing the new text
Format: U<n> | CLASS | file:line | verbatim quote (<=80) | paraphrase. File prefix m = mcp.md, f = failures.md.

## references/mcp.md
U1 | АДРЕС | m:3 | Номера разделов — прежние, общие с SKILL.md. | Section numbers (2.x) are shared with SKILL.md; cross-references use them
U2 | ПРАВИЛО | m:3 | Читать: перед первым вызовом MCP-коннектора Google Drive в сессии. | Read mcp.md before the first Drive connector call in a session
U3 | ПОРОГ | m:9 | `contentMimeType` два рабочих значения | create_file contentMimeType has two working values: text/plain and text/html
U4 | ПРАВИЛО | m:9 | выбор между ними делает ВЛАДЕЛЕЦ, а не сессия | The owner, not the session, chooses between plain and html
U5 | ПОРОГ | m:11 | `text/plain` — ОБЫЧНЫЙ документ. | text/plain = ordinary doc
U6 | ПРИЧИНА | m:11 | Конвертируется в нативный Google Doc, но плоским текстом | text/plain converts to native Doc but flat: no headings, tables, emphasis, page breaks
U7 | ПРАВИЛО | m:11 | Годится для черновика, рабочей записи, текста на вычитку | plain fits draft, working record, proofreading text, material to be edited further (cheap, fast)
U8 | ПОРОГ | m:12 | `text/html` — КРАСИВЫЙ документ. | text/html = beautiful doc, converts to native Doc with real headings, tables, lists, colour, call-outs, page breaks
U9 | ПРАВИЛО | m:12 | Годится для печати и для чтения человеком. | html fits print and human reading
U10 | ПРАВИЛО | m:12 | Стили задавать блоком `<style>` с классами в `<head>` | Set styles with a <style> block with classes in <head>
U11 | ПРИЧИНА | m:12 | переживает конвертацию и даёт вдвое меньший объём вызова | The <style> block survives conversion and halves call size versus inline styles on every tag
U12 | СЛУЧАЙ | m:12 | Проверено 2026-09-17 документом REPORT_git-migration_2026-09-17 | Verified 2026-09-17 on document REPORT_git-migration_2026-09-17 (block T-108 of registry/documents.md)
U13 | АДРЕС | m:12 | (блок T-108 реестра `registry/documents.md`) | Address: registry/documents.md block T-108
U14 | ПРАВИЛО | m:14 | ПРАВИЛО ВОПРОСА (внесено 2026-09-17 решением владельца). | Question rule, introduced 2026-09-17 by owner decision
U15 | ПРАВИЛО | m:14 | задаёт ОДИН короткий вопрос — «обычный или красивый?» — и ждёт ответа | Before creating a document a human will read the session asks ONE short question "plain or beautiful?" and waits
U16 | ПРАВИЛО | m:14 | Вопрос задаётся один раз на документ, не на каждый шаг и не на каждую правку. | Asked once per document, not per step/edit
U17 | ПРАВИЛО | m:14 | Формулировка короткая, без объяснения разницы, если владелец о ней не спросил. | Wording short, no explanation of the difference unless owner asks
U18 | ПРАВИЛО | m:16 | Вопрос НЕ задаётся, и молча берётся `text/plain`, когда выполнено хотя бы одно: | No question, silently text/plain, when at least one of (а)-(г) holds
U19 | ИСКЛЮЧЕНИЕ | m:17 | (а) владелец уже назвал вид в самой задаче | (а) owner already named the kind in the task ("для печати", "красиво", "оформи", "черновиком", "просто текстом", "на вычитку")
U20 | ИСКЛЮЧЕНИЕ | m:18 | (б) документ создаётся для машинного чтения, а не для человека; | (б) document is for machine reading
U21 | ИСКЛЮЧЕНИЕ | m:19 | (в) это служебная запись, лог, промежуточный или временный файл; | (в) service record, log, intermediate or temporary file
U22 | ИСКЛЮЧЕНИЕ | m:20 | (г) владельца нет на связи и ответа ждать не от кого | (г) owner unreachable: text/plain, and the chosen kind is named in the report with a direct line
U23 | ПРИЧИНА | m:22 | красивый документ дороже в сборке и в объёме вызова, а нужен не всегда | Reason for question rule: beautiful costs more in assembly and call volume and is not always needed
U24 | СЛУЧАЙ | m:22 | «очень часто мне достаточно обычного» (владелец, 2026-09-17) | Owner quote 2026-09-17 as basis
U25 | ПРИЧИНА | m:22 | Решать за владельца, что ему нужен красивый, — такой же дефект | Deciding for the owner either way (beautiful or plain) is the same defect; both decisions are his, costs one line of question
U26 | ПРАВИЛО | m:24 | `application/vnd.google-apps.document` как contentMimeType вместе с textContent даёт пустой | Do not use application/vnd.google-apps.document as contentMimeType together with textContent (empty/unopenable doc), for either kind
U27 | ИСКЛЮЧЕНИЕ | m:24 | Без textContent этот тип штатно создаёт пустой документ | Without textContent that type officially creates an empty doc (per tool description) — not a failure, but not a way to write text
U28 | ПОРОГ | m:26 | Параметры: title, contentMimeType, textContent, parentId. | create_file parameters list
U29 | ПОРОГ | m:26 | `disableConversionToGoogleType:true` + `text/markdown` | For .md: disableConversionToGoogleType:true + text/markdown
U30 | ПРИЧИНА | m:26 | .md не поддерживают append/replace — Docs API | .md files do not support append/replace (Docs API)
U31 | ПОРОГ | m:26 | overwrite работает с любым mimeType | overwrite works with any mimeType
U32 | ПРОВЕРКА | m:28 | Верификация: ответ `{id, title, mimeType}`; id пуст — провал. | create_file verification: response {id,title,mimeType}; empty id = failure
U33 | ПРОВЕРКА | m:28 | верификация ОБЯЗАТЕЛЬНО дополняется чтением через gdocs-read | For text/html, verification MUST add a gdocs-read read-back
U34 | ПРОВЕРКА | m:28 | в тексте не должно остаться сырой разметки (`<table`, `style=`, `<div`) | Text must contain no raw markup (<table, style=, <div)
U35 | ПРАВИЛО | m:28 | Если разметка в тексте есть — конвертация не состоялась, документ негоден и пересоздаётся. | If markup present: conversion failed, document unfit, recreate
U36 | ПРОВЕРКА | m:28 | Ответ `{mimeType: "application/vnd.google-apps.document"}` сам по себе конвертацию содержимого НЕ доказывает. | The response mimeType alone does not prove content conversion
U37 | ПРАВИЛО | m:29 | Содержимое после create_file сверяется со входом программно, а не на глаз | After create_file content is compared with the input programmatically, not by eye
U38 | СЛУЧАЙ | m:29 | create_file дважды портил текст без ошибки | create_file corrupted text twice without error: CJK glyphs inside a Russian word (RUNBOOK, 2026-07-21)
U39 | СЛУЧАЙ | m:29 | номер наряда «Н-0-бис» лёг как «НЭбис» (2026-08-05) | Second case: work-order number "Н-0-бис" came out as "НЭбис" (2026-08-05)
U40 | ПРИЧИНА | m:29 | Порча числа, даты или идентификатора при чтении неотличима от верного значения. | Corruption of number/date/ID is indistinguishable from a correct value on reading
U41 | ПРОВЕРКА | m:29 | прочитать созданное gdocs-read, найти символы вне ожидаемых алфавитов (например диапазон CJK) | Read back with gdocs-read, find symbols outside expected alphabets (e.g. CJK range)
U42 | ПРОВЕРКА | m:29 | значения, похожие на ID, номера и даты, сравнить со входом посимвольно | Values resembling IDs, numbers, dates compared with input character by character
U43 | СЛУЧАЙ | m:29 | Наблюдения 2026-07-21 и 2026-08-05; не перепроверено с 2026-08-05. | Observations dated; not re-verified since 2026-08-05
U44 | ПРАВИЛО | m:31 | КТО СОЗДАЁТ ФАЙЛ ДЛЯ РОБОТА. | Who creates a file for the robot: owner via create_file
U45 | СЛУЧАЙ | m:31 | Сервисный аккаунт n8n не создаёт файлы в папке DOCS: узел Drive «createFromText» ответил Forbidden | n8n service account does not create files in DOCS folder: Drive node createFromText answered Forbidden
U46 | СЛУЧАЙ | m:31 | (прогон 73643, `projects/deklaration-ozon/LOG.md`, запись о создании CSV) | Evidence: execution 73643, projects/deklaration-ozon/LOG.md, CSV creation entry
U47 | ПРАВИЛО | m:31 | Рабочий порядок: файл создаётся create_file от имени владельца в нужной папке | Working order: create_file as owner in the needed folder; folder/file shared to service account as editor; robot only overwrites content by saved ID
U48 | АДРЕС | m:31 | Тот же порядок для книги Google Sheets — §4.1. | Same order for a Sheets book: see §4.1
U49 | ПРАВИЛО | m:33 | create_file НЕ обновляет существующие файлы: при совпадении имени создаёт дубль. | create_file does not update existing files; same name makes a duplicate
U50 | ПРОВЕРКА | m:33 | Перед созданием проверять существование (get_file_metadata / search_files) | Check existence before creating (get_file_metadata / search_files)
U51 | ПРАВИЛО | m:33 | обновление содержимого — только gdocs-* по сохранённому fileId | Content updates only via gdocs-* by saved fileId
U52 | ПОРОГ | m:33 | update_file содержимое не меняет: он умеет только переименовать файл (title) и перенести | Connector update_file does not change content; only rename (title) and move (parentId)
U53 | ПРИЧИНА | m:35 | ЛОВУШКА КРАСИВОГО ДОКУМЕНТА: форматирование, полученное через `text/html`, gdocs-overwrite v2 НЕ сохраняет | Trap: overwrite v2 writes only plain text and does not preserve html formatting
U54 | ПРАВИЛО | m:35 | Правка красивого документа через overwrite молча превращает его в обычный | Editing a beautiful doc via overwrite silently turns it plain: text stays, formatting gone, no error
U55 | ПРАВИЛО | m:35 | Красивый документ правится пересозданием через create_file с новым HTML либо руками владельца | Beautiful doc is edited by recreating via create_file with new HTML, or by owner's hands in the Docs UI
U56 | ИСКЛЮЧЕНИЕ | m:35 | Точечные правки текста в красивом документе (gdocs-replace) оформление не трогают и безопасны. | Point text edits via gdocs-replace do not touch formatting and are safe
U57 | АДРЕС | m:35 | gdocs-overwrite v2 НЕ сохраняет — он пишет только plain text (§3.4) | Address: §3.4 for overwrite v2 plain-text behaviour
U58 | ПОРОГ | m:37 | Известное поведение: text/plain теряет .txt в имени. | Known behaviour: text/plain drops .txt from file name
U59 | ПОРОГ | m:39 | `fileSize: "1"` — это кеш-заглушка, не признак пустого документа. | create_file response right after the call may carry fileSize "1": cache stub, not sign of empty doc
U60 | ПРОВЕРКА | m:39 | Верификация только чтением. | Verification only by reading
U61 | ПРАВИЛО | m:42 | google_drive_fetch — прежний инструмент чтения, давал пустой ответ без ошибки | google_drive_fetch (old read tool) gave empty answers without error on large/growing files (INDEX, CORE, OPS)
U62 | ПРАВИЛО | m:42 | В нынешнем коннекторе его нет; его место занял read_file_content | Current connector lacks it; read_file_content took its place, and the §0 point 2 ban applies to it
U63 | ИСКЛЮЧЕНИЕ | m:42 | с единственным исключением для отчётов вики | Single exception for wiki reports (to the read_file_content ban)
U64 | ПРАВИЛО | m:43 | РАЗМЕР НЕ ОПРЕДЕЛЯТЬ ПО fileSize из get_file_metadata. | Do not determine size by fileSize from get_file_metadata
U65 | ПРИЧИНА | m:43 | Для нативных Google Docs fileSize отражает внутреннее представление | For native Docs fileSize reflects internal representation, not exported text size
U66 | ПОРОГ | m:43 | в байтах UTF-8 экспорт ≈ 3× fileSize (2,86–3,20 на CORE и SYS_INDEX 2026-08-05 | Cyrillic: export ≈ 3x fileSize in UTF-8 bytes (2.86–3.20 on CORE and SYS_INDEX 2026-08-05)
U67 | СЛУЧАЙ | m:43 | 2,81 на SYS_INDEX 2026-10-12 — 160 087 байт при fileSize 57 065 | Case: 2.81 on SYS_INDEX 2026-10-12, 160087 bytes at fileSize 57065
U68 | ПОРОГ | m:43 | в символах ≈ 2× (1,88–2,03; 2026-10-12 — 1,84) | In characters ≈ 2x (1.88–2.03; 2026-10-12 1.84)
U69 | ПРИЧИНА | m:43 | Число без единицы ошибается вдвое. | A ratio without unit errs twofold
U70 | ПРИЧИНА | m:44 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-12 здесь стояло «экспорт ≈ 3× fileSize» без единицы | Diagnosis history: until 2026-10-12 text said ≈3x without unit (lesson У-68 of projects/archivarius/LOG.md)
U71 | АДРЕС | m:44 | (урок У-68 журнала `projects/archivarius/LOG.md`) | Address: projects/archivarius/LOG.md lesson У-68
U72 | ПРАВИЛО | m:44 | contentSnippet и fileSize из metadata — кеш, для верификации содержимого непригодны. | contentSnippet and fileSize from metadata are cache, unfit for content verification
U73 | ПРАВИЛО | m:44 | Рабочий способ узнать размер — gdocs-read с `fromLine:1, toLine:1` (§3.5) | Working way to learn size: gdocs-read with fromLine:1,toLine:1 returns byteLength and totalLines of whole doc with one line of text
U74 | ПРАВИЛО | m:45 | ПУСТОЙ РЕЗУЛЬТАТ ЧТЕНИЯ = СТОП. | Empty read result = STOP: say "read returned empty" explicitly and stop
U75 | ПРАВИЛО | m:45 | ЗАПРЕЩЕНО отвечать реконструкцией по памяти | Forbidden to answer by reconstruction from memory
U76 | ПРИЧИНА | m:45 | тихий отказ инструмента плюс конфабуляция модели неотличимы от лжи | Reason: silent tool failure plus confabulation is indistinguishable from lying
U77 | ИСКЛЮЧЕНИЕ | m:46 | `gdocs-read` с `fromLine` больше `totalLines` возвращает `success:true`, `text:""`, `returnedChars:0` | Exception: fromLine > totalLines returns success:true, text "", returnedChars 0, totalLines filled
U78 | ПРАВИЛО | m:46 | Различать по паре `fromLine` против `totalLines`, а не по одному `text`. | Distinguish by pair fromLine vs totalLines, not by text alone
U79 | ПРАВИЛО | m:46 | Всё прочее пустое чтение остаётся стопом. | Any other empty read remains a stop
U80 | ПРИЧИНА | m:46 | Документ при этом прочитан целиком и корректно — пуст только запрошенный срез. | Document read fully; only requested slice is empty
U81 | ПОРОГ | m:47 | портит символы начиная примерно с 20–25 КБ | Byte relay through session context (base64 -> decode in other tool) corrupts characters from about 20–25 KB
U82 | ПРАВИЛО | m:47 | использовать второй независимый путь чтения (gdocs-read), не пересказ байтов через контекст | For checks/read-back use second independent read path (gdocs-read), not byte retelling via context
U83 | ПРАВИЛО | m:48 | Не читать файл во время активной записи в него | Do not read a file during active write into it (same session) — read/write race possible, indistinguishable from other silent empty answers
U84 | ПРАВИЛО | m:48 | при подозрении на гонку — подождать и перечитать | On suspected race wait and reread
U85 | ПРИЧИНА | m:49 | Файл, лежащий в Корзине Drive (Trash), на всех путях чтения | Trashed file answers "not found"/empty on all read paths (metadata/search/gdocs-read) — indistinguishable from nonexistent and from not shared to SA
U86 | ПРОВЕРКА | m:49 | проверить Корзину вручную через UI Drive | If object must exist but is nowhere found, check Trash manually via Drive UI
U87 | ПРАВИЛО | m:50 | ЦЕНА ПОЛНОГО ТЕКСТА PDF. | read_file_content on a PDF brings the whole text into context
U88 | СЛУЧАЙ | m:50 | одна статья среднего размера (Thieme CME, PDF 1,5 МБ) заняла около 25 000 токенов | One average article (Thieme CME, 1.5 MB PDF) took about 25,000 tokens, nearly the whole allowed single-result volume (projects/archive-recon/LOG.md, Т-1)
U89 | ПРАВИЛО | m:50 | полный текст PDF читается только прицельно | Read full PDF text only targeted, when content of exactly that article is needed
U90 | ПРАВИЛО | m:50 | Для обхода и описи многих файлов (тип, тема, годится ли) хватает имени, размера и метаданных | For surveying many files use name, size, metadata (get_file_metadata, search_files with excludeContentSnippets:true)
U91 | ПРАВИЛО | m:50 | массовую механическую работу — опись папок, нарезку текста — делает скрипт в среде с bash | Mass mechanical work (folder inventory, text slicing) done by a script in a bash environment, not by model calls file by file
U92 | ПОРОГ | m:53 | Прежнее имя инструмента — google_drive_search, прежний синтаксис (`name contains` | Old tool google_drive_search with old syntax (name contains, 'ID' in parents) does not work in current connector
U93 | ПОРОГ | m:53 | `title contains 'x'`, `title = 'x'`, `fullText contains 'x'`, `parentId = 'ID'` | search_files syntax: title contains / title = / fullText contains / parentId =
U94 | ПОРОГ | m:53 | `mimeType = '…'`, `modifiedTime > '2026-09-01T00:00:00Z'`, `owner = 'me'` | search_files syntax: mimeType, modifiedTime >, owner = 'me'
U95 | ПОРОГ | m:53 | строки — в одинарных кавычках; условия соединяются `and`, `or`, `not` | Strings in single quotes; conditions joined by and/or/not
U96 | СЛУЧАЙ | m:53 | Проверено 2026-09-26 запросами `parentId = '<папка INDEX>'` вместе с `fullText contains 'SENTINEL'` | Verified 2026-09-26 with parentId+fullText contains 'SENTINEL' and title contains 'google-drive-docs' queries
U97 | ПОРОГ | m:54 | отрывок текста до примерно 5 000 знаков | By default each found record carries a text snippet up to about 5,000 chars
U98 | ПРАВИЛО | m:54 | Когда нужен только ID или список файлов — `excludeContentSnippets: true` | When only ID/list needed use excludeContentSnippets:true
U99 | ПОРОГ | m:54 | `snippetVerbosity: "BRIEF"` (около 1 000 знаков) | When snippet needed use snippetVerbosity "BRIEF" (about 1,000 chars)
U100 | ПРАВИЛО | m:54 | Отрывок — кеш индекса, для проверки содержимого не годится (п.2 выше). | Snippet is index cache, unfit for content checks
U101 | ПОРОГ | m:55 | Свежесозданные не-native файлы (PDF, бинарники) не находятся сразу | Freshly created non-native files (PDF, binaries) are not found at once (indexing delay)
U102 | ПРАВИЛО | m:55 | искать через get_file_metadata по ID или search_files по parentId | Find them via get_file_metadata by ID or search_files by parentId
U103 | ПРАВИЛО | m:57 | ПОЛНОТА ОБХОДА. | Completeness of traversal: a folder walk/list is complete only if the parts that failed to open (subfolders, response pages, error files) are listed explicitly and that list is empty
U104 | ПРИЧИНА | m:57 | Отсутствие такого перечня — не «ничего не пропущено», а «неизвестно, что пропущено». | Absence of the list means "unknown what is missed", not "nothing missed"
U105 | СЛУЧАЙ | m:57 | опись папки «ANTIBIOTIKA» скриптом archive_scan.py версии 1.0 вернула 50 файлов | Case: ANTIBIOTIKA inventory by archive_scan.py v1.0 returned 50 files and silently omitted five subfolders; v1.1 writes section "FOLDERS THAT COULD NOT BE READ"; accepted only with empty section
U106 | АДРЕС | m:57 | (`projects/archive-recon/LOG.md`, Т-3) | Address: projects/archive-recon/LOG.md, Т-3
U107 | ПРАВИЛО | m:57 | неоткрывшиеся части выводятся отдельным списком | For own scripts/workflows: unopened parts output as separate list
U108 | ПРАВИЛО | m:57 | оборванная на середине пагинация (ответ с признаком следующей страницы, которую не прочитали) роняет прогон | Pagination interrupted midway (next-page marker unread) fails the run instead of a warning in report text
U109 | ПРАВИЛО | m:57 | «пусто» и «нашлось N» от него — не доказательство полноты (§7) | search_files response carries no list of unopened parts, so "empty"/"found N" is not proof of completeness (§7)
U110 | ПРОВЕРКА | m:60 | Верификация после create_file, получение ID. | get_file_metadata is used for post-create_file verification and getting ID
U111 | ПРАВИЛО | m:60 | файл в другом аккаунте / не расшарен на аккаунт коннектора — проверять owner | If file "not found" while others read: other account / not shared to connector account — check owner
U112 | ПРАВИЛО | m:61 | Ответ «ineligible for generative AI contexts» — отказ коннектора выдавать этот файл модели | "ineligible for generative AI contexts" is the connector's refusal to give the file to the model, not absence of file
U113 | ПРАВИЛО | m:61 | Сессия его не обходит; существует ли файл, проверяет Андрей в интерфейсе Drive | Session does not bypass; Andrei checks existence in Drive UI
U114 | СЛУЧАЙ | m:61 | (SYS_JOURNAL_2026, одно наблюдение; не перепроверено) | Evidence: SYS_JOURNAL_2026, one observation, not re-verified
U115 | ПОРОГ | m:62 | copy_file систематически создаёт снимок на 1–3 КБ больше оригинала | copy_file systematically makes a copy 1–3 KB larger than original (metadata overhead): normal, not data corruption

## references/failures.md
U116 | ПРАВИЛО | f:3 | Читать: при ошибке или пустом ответе инструмента и перед сверкой крупного документа. | Read failures.md on tool error/empty answer and before reconciling a large document
U117 | АДРЕС | f:3 | Номера разделов — прежние, общие с SKILL.md. | Section numbers (8, 9, 10) shared with SKILL.md
U118 | ПОРОГ | f:9 | Doc пустой/не открывается после create_file | E01: Doc empty/not opening after create_file -> contentMimeType text/plain
U119 | ПОРОГ | f:10 | reason/context из manual-прогона; разделители `\n\n` / `\r\n` | E02: replace does not replace -> take reason/context from manual run; separators \n\n / \r\n
U120 | ПОРОГ | f:11 | replace нужен многострочный | E03: multiline replace needed -> gdocs-overwrite v2; text larger than about 1–2 KB -> gdocs-apply-from-file (§3.6)
U121 | ПОРОГ | f:12 | n8n:execute_workflow через MCP, не curl | E04: webhook blocked -> n8n:execute_workflow via MCP, not curl
U122 | ПОРОГ | f:13 | переподключить коннектор claude.ai + новый чат | E05: MCP path auth error -> reconnect connector in claude.ai + new chat (n8n path on SA does not expire)
U123 | ПОРОГ | f:14 | запись не пишет без ошибки | E06: write does not write without error -> read-back of file
U124 | ПОРОГ | f:15 | Credential кэш «does not exist» | E07: credential cache "does not exist" -> switch and switch back, Publish
U125 | АДРЕС | f:16 | Sheets: `'A: field'` / returnAllMatches / IMPORTRANGE | E08–E10: Sheets 'A: field' / returnAllMatches / IMPORTRANGE -> see §4.2
U126 | ПОРОГ | f:17 | text/plain+textContent, повторить; проверить права папки | E11: create_file without id -> text/plain+textContent, retry; check folder rights
U127 | ПОРОГ | f:18 | write-нода без credential после update | E12: write node without credential after update (new node without binding, or credential type change) -> bind SA (googleApi) manually, Save, Publish
U128 | ПРАВИЛО | f:18 | существующие привязки update не сбрасывает (§9) | Existing bindings are not reset by update (§9)
U129 | ПОРОГ | f:19 | проверить имя поля body (newContent, не text) | E13: file wiped to empty, modifiedTime fresh -> check body field name (newContent, not text), see §3
U130 | ПОРОГ | f:20 | create_file падает, чтение работает | E14: create_file fails while reading works -> MCP write-scope expired -> fallback gdocs-overwrite v2, or reconnect + new chat
U131 | ПОРОГ | f:21 | metadata/read «not found», другие файлы читаются | E15: metadata/read "not found" while others read -> file not shared to connector account / SA
U132 | ПОРОГ | f:22 | gdocs-replace v2 вернул success:false, но occurrencesChanged>0 | E16: replace v2 returned success:false but occurrencesChanged>0
U133 | ПРАВИЛО | f:22 | замена в документе состоялась, не прошла проверка после неё | Replacement happened; the post-check failed (reread text empty; new text not found; on deletion anchor still found)
U134 | ПРАВИЛО | f:22 | верифицировать перечитыванием, НЕ повторять вызов | Verify by reread, DO NOT repeat the call
U135 | ПРИЧИНА | f:22 | До 2026-10-12 причиной называлось «indexOf по пустой строке при replace=""» | History: until 2026-10-12 cause was named "indexOf on empty string when replace=''" — code version 2026-09-25 does not work so (§3.2 (д))
U136 | ПОРОГ | f:23 | «файл маленький» по metadata, а хвост обрезан | E17: "file small" by metadata but tail truncated -> fileSize unreliable for native Docs, read via gdocs-read (§2.2 п.2)
U137 | ПОРОГ | f:24 | replace затёр больше, чем ожидалось | E18: replace wiped more than expected -> non-unique anchor: count occurrences BEFORE call (§3.2); rollback = reverse replace + full reread
U138 | ПОРОГ | f:25 | gdocs-read вернул `text:""` при `success:true` | E19: gdocs-read returned text "" with success:true -> compare fromLine with totalLines: slice past the end is not a read failure (§2.2 п.3, §3.5)
U139 | ПОРОГ | f:26 | якорь виден в экспорте text/plain, а replace даёт 0 вхождений | E20: anchor visible in text/plain export but replace gives 0 occurrences -> do not guess anchor blindly; first look at the string's bytes via gdocs-read
U140 | ПРИЧИНА | f:26 | гипотеза — неразрывный пробел или иной невидимый символ | Hypothesis: non-breaking space or other invisible character
U141 | СЛУЧАЙ | f:26 | (строки шапки LAST_UPDATED, N8N_JOURNAL_2026; наблюдения 2026-07, не перепроверено) | Evidence: LAST_UPDATED header lines, N8N_JOURNAL_2026; observations 2026-07, not re-verified
U142 | ПОРОГ | f:27 | gdocs-overwrite v2: success:false «content mismatch on first/last 100 chars» | E21: overwrite v2 success:false "content mismatch on first/last 100 chars", bytesSent and bytesRead close
U143 | ПРАВИЛО | f:27 | запись, вероятно, состоялась — не повторять, читать файл | Write probably happened — do not repeat, read file
U144 | ПРОВЕРКА | f:27 | проверить, что newContent передан строкой, а не объектом (§3.4 | Check newContent was passed as string, not object (§3.4)
U145 | СЛУЧАЙ | f:27 | исполнение 51779, 2026-08-30 | Evidence: execution 51779, 2026-08-30
U146 | ПОРОГ | f:31 | Формат: инструмент/ситуация | §9 registry format: tool/situation | silent mode | mandatory safeguard
U147 | ПРАВИЛО | f:33 | gdocs-replace: `occurrencesChanged:0` без ошибки при промахе | gdocs-replace silent: occurrencesChanged:0 without error on miss; non-unique search yields N > expected -> read-back always; on deletion count occurrences before call (§3.2)
U148 | ПРАВИЛО | f:34 | gdocs-replace v2: `success:false` при `occurrencesChanged>0` | replace v2 success:false with occurrencesChanged>0 = replacement happened, post-check failed -> do not repeat, verify by reread (E16, §3.2 (д))
U149 | ПРАВИЛО | f:35 | HTTP 500 «Unknown Error» от Drive API export — не то же самое, что «запись не прошла» | Read-back inside write workflow: HTTP 500 "Unknown Error" from Drive API export is not the same as "write failed" -> reread file manually in a separate call
U150 | ПРАВИЛО | f:36 | Файл не расшарен на SA: 404/403 без явной связи с правами → get_file_permissions до первой записи | File not shared to SA: 404/403 without explicit link to rights -> get_file_permissions before first write
U151 | ПРАВИЛО | f:37 | Частичная миграция credential: один узел пишет, второй молча падает на авторизации | Partial credential migration: one node writes, another silently fails auth -> migrate all nodes in one update
U152 | ПРАВИЛО | f:38 | google_drive_fetch: пустой ответ на крупных/растущих файлах систематически | google_drive_fetch: empty answer on large/growing files systematically -> do not use, only gdocs-read
U153 | ПРАВИЛО | f:39 | get_file_metadata и search_files: fileSize и contentSnippet — кеш | fileSize and contentSnippet are cache, do not reflect real size/content of native Doc -> not for size estimation or verification; take size from gdocs-read fromLine:1,toLine:1 (§3.5)
U154 | ПРИЧИНА | f:39 | это стоит полного документа в контексте, но другого достоверного способа нет | The size-by-gdocs-read way costs the full document in context but is the only reliable way
U155 | ПРАВИЛО | f:40 | gdocs-read с `fromLine` за концом документа: `success:true` и пустой `text` | gdocs-read with fromLine past end: success:true and empty text looks like silent refusal but is not -> compare fromLine with totalLines before alarm (§2.2 п.3)
U156 | ПРАВИЛО | f:41 | Пустое чтение + модель: конфабуляция правдоподобного ответа | Empty read + model: confabulation of plausible answer over empty result -> STOP, explicit message, no reconstruction from memory
U157 | ПРАВИЛО | f:42 | `'started'` не гарантия выполнения | n8n execute_workflow (MCP, production): 'started' not a guarantee; execution not visible in get_execution/search_executions; HTTP response not returned -> read-back of target object
U158 | ПРАВИЛО | f:43 | цепочка может тихо оборваться в середине (IF без ветки) | n8n execution `success`: chain may silently break midway (IF without branch) -> in manual mode compare number of write-node runs when debugging
U159 | ПРАВИЛО | f:44 | HTTP-нода с `neverError:true`: код ошибки API проходит как валидный item | HTTP node with neverError:true: API error code passes as valid item -> explicit check of code/error after request
U160 | ПРАВИЛО | f:45 | Schedule/webhook после update+publish может не тикать при `active:true` | Schedule/webhook after update+publish may not tick at active:true
U161 | ПРОВЕРКА | f:45 | сверка updatedAt с временем последнего исполнения годится, только если у воркфлоу сохраняются успешные прогоны | Comparing updatedAt with last execution time works only if successful runs are saved
U162 | ПОРОГ | f:45 | при `EXECUTIONS_DATA_SAVE_ON_SUCCESS=none` отсутствие исполнения в списке ничего не значит | With EXECUTIONS_DATA_SAVE_ON_SUCCESS=none absence in the list means nothing
U163 | АДРЕС | f:45 | живость — по корням R2 и R4 Skill n8n-engineering-manual (счётчики `workflow_statistics`) | Liveness: roots R2 and R4 of n8n-engineering-manual (workflow_statistics counters)
U164 | ПРАВИЛО | f:46 | Запись воркфлоу кодом целиком (Workflow SDK, `create_workflow_from_code`) | Writing a workflow by whole code (SDK create_workflow_from_code): already-bound node credentials are NOT reset
U165 | ПРИЧИНА | f:46 | теряется другое — настройки воркфлоу (часовой пояс, воркфлоу ошибок) | Lost instead: workflow settings (timezone, error workflow), retry count and wait between retries on nodes, IF/Switch expressions turn into string literals, webhookId may change
U166 | СЛУЧАЙ | f:46 | На 2026-10-12 `update_workflow` принимает точечные операции и этих потерь в пробах не давал | As of 2026-10-12 update_workflow accepts point operations and in probes did not give these losses — except unverified Switch and webhook node
U167 | ПРАВИЛО | f:46 | Смена ТИПА credential у узла сбрасывает его фильтры и маппинг. | Changing credential TYPE on a node resets its filters and mapping
U168 | ПРОВЕРКА | f:46 | полная сверка воркфлоу после записи до publish | Full workflow reconciliation after write before publish
U169 | АДРЕС | f:46 | разбор и список — корень R1b в Skill n8n-engineering-manual | Breakdown and list: root R1b of n8n-engineering-manual
U170 | ПРОВЕРКА | f:46 | Привязку проверять полем `credentials` в get_workflow_details | Check binding by field `credentials` in get_workflow_details; since 2026-10-08 it returns id and key name of node
U171 | АДРЕС | f:46 | (позиция AH-27 очереди) | Position AH-27 of queue
U172 | ПРИЧИНА | f:47 | ИСТОРИЯ ДИАГНОЗА: считалось, что credential после update_workflow сбрасывается на заглушку. | Diagnosis history: believed credential resets to stub after update_workflow; refuted
U173 | СЛУЧАЙ | f:47 | проверка 2026-07-19 в журнале инцидентов n8n-engineering-manual (INCIDENT_LOG) | Refutation: check 2026-07-19 in the incident log; "key reset" version refuted 2026-07-03 and removed as task motive (projects/wb-reviews/LOG.md, Р-2, decision Д-2)
U174 | СЛУЧАЙ | f:47 | в card-content-sync (Р-9) эта версия увела диагноз, а причиной был порядок диапазонов | In card-content-sync (Р-9) that version misled the diagnosis; cause was order of ranges
U175 | ПРАВИЛО | f:47 | Строка E12 таблицы §8 описывает новый узел без привязки, а не сброс существующей. | Row E12 describes a new node without binding, not a reset of an existing one
U176 | ПРАВИЛО | f:48 | SDK `.to([a,b])`: второй получатель молчит навсегда → `.to(a).add(source).to(b)` | SDK .to([a,b]): second receiver silent forever -> use .to(a).add(source).to(b)
U177 | ПРАВИЛО | f:49 | Disabled нода пропускает данные насквозь, не блокируя поток → проверять downstream явно. | Disabled node passes data through without blocking -> check downstream explicitly
U178 | ПРАВИЛО | f:50 | HTTP Request может перезаписать `json`, теряя поля → `$('Node').all()[i]` | HTTP Request may overwrite json losing fields -> use $('Node').all()[i] for original data
U179 | ПРАВИЛО | f:51 | `executeOnce` на любом месте цепочки, в том числе после Merge, обрабатывает только первый элемент | executeOnce anywhere in chain incl. after Merge processes only first item and silently drops the rest -> do not set on node that must process every item; breakdown n8n-engineering-manual references/engine.md §4.3
U180 | ПРИЧИНА | f:51 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-12 здесь стояло «executeOnce в середине цепочки выполняется на каждый item» | Diagnosis history: until 2026-10-12 text said executeOnce mid-chain runs per item; refuted by probe 2026-10-12 (entry Р-31 of projects/archivarius/LOG.md)
U181 | ПРАВИЛО | f:52 | Правка jsonBody прямо в браузере может оборваться на `=` без ошибки до publish | Editing jsonBody in the browser may break at `=` without error before publish -> in saved node JSON expression field stored as "={{ … }}"; verify via get_workflow_details
U182 | ПОРОГ | f:52 | В поле редактора то же выражение пишется `{{ … }}` без `=` | In editor field the same expression is written {{ … }} without =; one rule on three writing places: n8n-engineering-manual references/engine.md §4.8
U183 | ПРАВИЛО | f:53 | Байтовый релей через контекст (base64 между инструментами) теряет байты начиная примерно с 25 КБ | Byte relay via context loses bytes from about 25 KB -> compute hashes/checksums on the side (Apps Script/server), not via context
U184 | ПРАВИЛО | f:54 | «Битые» строки, которые меняются от чтения к чтению неизменного источника | "Broken" lines changing between reads of an unchanged source are a read-channel defect, not data -> do not fix data; verify by file on disk, in parts, or by owner's eyes in UI
U185 | СЛУЧАЙ | f:54 | выгрузка листа 182 строки около 2026-07-23, строки 114, 146, 176; WB_REVIEWS_INDEX | Case: sheet export 182 rows around 2026-07-23, rows 114, 146, 176; WB_REVIEWS_INDEX; not re-verified
U186 | ПРАВИЛО | f:55 | create_file: дубль при уже существующем имени файла → проверка существования до create. | create_file: duplicate when name exists -> check existence before create
U187 | ПРАВИЛО | f:56 | `/mnt/skills/user/` в сессии: считалось, что это снимок на старт чата | /mnt/skills/user/ in session: believed a snapshot at chat start (replacement invisible in current chat); refuted 2026-09-24: in SYS cloud session files in /mnt/skills/ updated in same chat by next owner message after Skill saved by another session
U188 | СЛУЧАЙ | f:56 | Второе наблюдение 2026-09-26, тоже облачная сессия на основе Claude Code | Second observation 2026-09-26: after two owner uploads (second-brain-git and second-brain-engineer) /mnt/skills/ copies matched issued files byte for byte by next message
U189 | ПРАВИЛО | f:56 | после замены Skill перечитать файл в той сессии, которая на него опирается | Behaviour depends on environment -> after Skill replacement reread the file in the session that relies on it and compare by edit anchor or bytewise; do not assume nor refute "not visible in current chat" without reading
U190 | ПРАВИЛО | f:57 | файл в Корзине Drive отвечает «not found»/пусто на всех путях одинаково | get_file_metadata/search_files/gdocs-read: trashed file answers "not found"/empty on all paths identically -> if file must exist but is nowhere found, check Trash via UI manually (cannot be distinguished programmatically)
U191 | ИСКЛЮЧЕНИЕ | f:57 | Граница правила: оно действует, только когда файл ДОЛЖЕН существовать. | Boundary: rule applies only when the file MUST exist
U192 | ИСКЛЮЧЕНИЕ | f:57 | то «not found» после действия — достигнутый результат, а не отказ | If target is absence (move to Trash, delete, revoke access), "not found" afterward is achieved result not failure: do not check Trash nor ask owner; just name in report which answer and which tool
U193 | ПРАВИЛО | f:58 | Чтение файла во время активной записи в него той же сессией: может вернуть пустой ответ | Reading a file during active write by same session may return empty (race) -> do not read during active write; on suspicion wait and reread
U194 | ПРАВИЛО | f:59 | `get_execution(includeData:true)` через параллельного субагента: байтовые метрики | get_execution(includeData:true) via parallel subagent: byte metrics (byteLength) may diverge from direct read without error -> take control numbers (byteLength/checkSum) only by direct gdocs-read call, not via subagent
U195 | ПРАВИЛО | f:60 | сырой ответ узла экспорта оседает в `executionData.contextData` и приходит в контекст сессии ПОЛНОСТЬЮ | get_execution(includeData:true) on Doc read/write workflow: raw export-node response settles in executionData.contextData and arrives in session context FULLY
U196 | ПОРОГ | f:60 | Ни `nodeNames`, ни `truncateData`, ни диапазон строк `fromLine`/`toLine` этого не режут | Neither nodeNames, nor truncateData, nor fromLine/toLine range cuts it
U197 | ПРИЧИНА | f:60 | свойство принадлежит типу узла загрузки (`n8n-nodes-base.httpRequest`) | Property belongs to the load-node type (n8n-nodes-base.httpRequest); not fixed by call parameters
U198 | СЛУЧАЙ | f:60 | exec 67942 (полное чтение) и exec 68199 (`fromLine:1, toLine:1` | Observations: exec 67942 (full read) and exec 68199 (fromLine:1,toLine:1 — text one line of 21 chars, contextData the whole doc 38,299 B)
U199 | ПРАВИЛО | f:60 | чтение документа Google Docs стоит сессии полного размера документа при любом запрошенном диапазоне | Reading a Google Doc costs the session the full document size at any requested range
U200 | ПРАВИЛО | f:60 | не планировать работу исходя из экономии, которой нет, и не обещать её в правилах | Do not plan on savings that do not exist nor promise them in rules; safeguard is in expectations, not call parameters
U201 | АДРЕС | f:60 | Карта узлов по воркфлоу — `registry/tools.md`. | Address: node map per workflow in registry/tools.md
U202 | ПРАВИЛО | f:61 | Единого порога, после которого среда кладёт ответ инструмента в файл | No single threshold after which the environment puts a tool response into a file instead of context
U203 | СЛУЧАЙ | f:61 | в один день 58 тысяч символов ушли в файл, а 82 тысячи байт пришли в контекст | Case: one day 58k chars went to file while 82k bytes came into context (SYS_JOURNAL_2026, 2026-09-08; task labs/sys/t-get-execution-context.md)
U204 | ПРАВИЛО | f:61 | любое число про объём ответа — оценка, а не замер | Any number on response volume is an estimate not measurement; tool parameters and plan steps (e.g. .xlsx path in §4.0) not built on it — path verified by one call in own environment
U205 | ПРАВИЛО | f:62 | Retry на 429/500/503 (Drive/Docs/Sheets в целом) — общего встроенного паттерна нет | Retry on 429/500/503: no general built-in pattern outside Sheets nodes (§4.2): implement explicitly, wait = 2^attempt + random, max 3 attempts
U206 | ПРАВИЛО | f:66 | `download_file_content` с `exportMimeType text/plain` → ответ сохраняется целиком на диск | Large-doc check order: download_file_content with exportMimeType text/plain -> response saved whole to disk -> compare programmatically (length, head/tail, substring counts, line diff)
U207 | ПРИЧИНА | f:66 | Текст в контексте вместо файла на диске не даёт надёжной побайтовой сверки | Text in context instead of file on disk gives no reliable byte comparison
U208 | ПРАВИЛО | f:67 | Нормализация перед сравнением обязательна — иначе ложные расхождения | Normalisation before comparison mandatory: export gives \r\n, may add BOM, turn empty paragraph into extra newline
U209 | ПОРОГ | f:67 | markdown-escape служебных символов (`\#`, `\*\*`, `\-`, `\_`, `\[`, `1\.`) в экспорте | Markdown escapes (\#, \*\*, \-, \_, \[, 1\.) in export are normalisable noise, not data loss
U210 | ПРИЧИНА | f:67 | Это поведение зависит от содержимого документа, не универсально | Behaviour depends on document content, not universal — sometimes export adds no escapes at all
U211 | ПРАВИЛО | f:68 | Правка последнего непустого абзаца документа необратимо схлопывает пустые абзацы в его хвосте | Editing the last non-empty paragraph irreversibly collapses empty paragraphs in its tail; expected checksum after such edit computed on normalised tail, do not try to restore empty paragraphs
U212 | СЛУЧАЙ | f:68 | наряды Н-26.08-03…06, 2026-08-27, «проверено дважды, восстановление не работает» | Evidence: work orders Н-26.08-03…06, 2026-08-27, "checked twice, restoration does not work"; SYS_INDEX
U213 | ПРАВИЛО | f:69 | Контрольная сумма и длина записываются вместе с названием канала | Checksum and length are recorded with channel name: same content via different channels gives different bytes
U214 | ПОРОГ | f:69 | download_file_content добавляет в начало метку порядка байт (BOM, 3 байта), gdocs-read её не добавляет | download_file_content prepends BOM (3 bytes), gdocs-read does not
U215 | ПРАВИЛО | f:69 | канонический канал для чисел сверки — gdocs-read | Canonical channel for reconciliation numbers is gdocs-read (JOURNAL_incidents, capture Ж)
U216 | ПРАВИЛО | f:69 | Сравнивать допустимо только числа одного канала. | Only numbers of the same channel may be compared
U217 | ПРАВИЛО | f:70 | byteLength/checkSum доказывают «полученное = лежащее в файле сейчас», но НЕ «отправленное | Checksum proves "received = in file now", NOT "sent at write = landed in file"
U218 | ПРИЧИНА | f:70 | экспорт нативного Doc закономерно может немного менять байтовый размер | Native Doc export may legitimately change byte size slightly (extra empty paragraphs), so checksum is not write safeguard
U219 | ПРОВЕРКА | f:70 | Верификация записи — построчная сверка содержания | Write verification = line-by-line content comparison, not checksum match alone
U220 | ПОРОГ | f:71 | `download_file_content` в диапазоне примерно 5–50 КБ возвращает base64 инлайн в контекст | download_file_content in about 5–50 KB range returns base64 inline in context, not auto-decoded -> context wasted on unreadable bytes
U221 | ПРАВИЛО | f:71 | В этом диапазоне читать через gdocs-read, не download_file_content. | In that range read via gdocs-read, not download_file_content
U222 | ПРАВИЛО | f:5 | ## 8. ТАБЛИЦА ОШИБОК | Section heads §8 error table / §9 silent-failure registry / §10 big-file verification keep numbering (cross-references from other files)
U223 | АДРЕС | m:5 | ## 2. MCP — коннектор Google Drive | mcp.md carries SKILL §2 (2.1 create_file, 2.2 reading rules, 2.3 search_files, 2.4 get_file_metadata); other files cite §2.2 п.1-3 and §2.1

U224 | АДРЕС | m:1 | # google-drive-docs — MCP-коннектор Google Drive | Title of mcp.md: part of Skill google-drive-docs, MCP connector
U225 | АДРЕС | m:7 | ### 2.1 create_file | Subsection 2.1 create_file heading (number cited elsewhere)
U226 | АДРЕС | m:41 | ### 2.2 ПРАВИЛА ЧТЕНИЯ ЧЕРЕЗ MCP | Subsection 2.2 reading rules heading (cited as §2.2 п.1-3, п.5)
U227 | АДРЕС | m:52 | ### 2.3 search_files | Subsection 2.3 heading
U228 | АДРЕС | m:59 | ### 2.4 get_file_metadata | Subsection 2.4 heading
U229 | АДРЕС | f:1 | # google-drive-docs — ошибки, тихие отказы, крупные файлы | Title of failures.md
U230 | АДРЕС | f:7 | Симптом | Error table columns: code, symptom, solution
U231 | АДРЕС | f:29 | ## 9. РЕЕСТР ТИХИХ ОТКАЗОВ | Section 9 heading (silent failure registry)
U232 | АДРЕС | f:64 | ## 10. ВЕРИФИКАЦИЯ БОЛЬШИХ ФАЙЛОВ | Section 10 heading (big-file verification)

## NEW (inputs belonging to group D)
N1 | ПРАВИЛО | AJ-9 | НЕ рассчитывать, что `nodeNames`, `truncateData` или режим `tail` в `get_execution` отсекут | Antipattern AJ-9 (home SKILL.md section 11; pointer from D): do not count on nodeNames/truncateData/tail cutting executionData.contextData; they cut only runData
N2 | ПОРОГ | AJ-9 | у `n8n-nodes-base.httpRequest` там лежит весь сырой ответ, у `n8n-nodes-base.github` — пусто | Whether contextData holds freight is decided by load-node type: httpRequest holds whole raw response, github is empty
N3 | СЛУЧАЙ | AJ-9 | исполнения 49582 — 138 КБ при режиме `tail`, 62042 — около 40 КБ, 63960 — полтора размера файла | Evidence executions 49582 (138 KB in tail mode), 62042 (~40 KB), 63960 (1.5x file size) — for the contextData antipattern (case counts; home task labs/sys/t-get-execution-context.md)
N4 | АДРЕС | AJ-9 | Какие воркфлоу Канала чистые, а какие грязные — таблица в `second-brain-git` 7.6 | Address: second-brain-git 7.6 table clean/dirty workflows; for Google Docs reading — §9 of failures.md (f:60-61 stays the copy-home pointer; map says failures.md:60 is a COPY, NEM roots.md:60 is the home)
N5 | ПРАВИЛО | AJ-23 | в журнале инцидентов n8n (`projects/n8n/INCIDENT_LOG.md`) | AJ-23 item (3): in failures.md line 47 replace "в журнале инцидентов n8n-engineering-manual (INCIDENT_LOG)" with "в журнале инцидентов n8n (`projects/n8n/INCIDENT_LOG.md`)" — the incident-log address now projects/n8n/INCIDENT_LOG.md
N6 | ПРАВИЛО | map-GDD | Грязные воркфлоу (узел httpRequest) оставляют сырой ответ в contextData; nodeNames это не режет | Map item 5 (contextData cost of reading): failures.md:60 is a COPY whose home is n8n-engineering-manual roots.md:60; D may keep it as copy/pointer, must not lose the Doc-read cost statement f:199
N7 | ПРАВИЛО | map-GDD | Пустое чтение = стоп, не реконструировать по памяти | Map item 34 (empty read = stop): copies m:45, f:41 — duplicates; home disputed, must remain at least one full statement (U74-U76)
N8 | ПРАВИЛО | map-GDD | Полнота обхода/списка: неоткрывшиеся части перечислены явно и перечень пуст | Map item 35: m:57 holds the rule; home in second-brain-engineer (утверждение об отсутствии) is an adjacent rule; rule U103-U109 stays or is addressed
N9 | ПРАВИЛО | map-GDD | Контрольная сумма/длина снимаются с названием канала; download_file_content добавляет BOM | Map item 88: f:69 is a copy of home SBE; U213-U216
N10 | ПРАВИЛО | map-GDD | Квота Sheets 60/мин на потребителя credential; retryOnFail на 429 вреден | Map item 81 and contradiction 3а-5: the Sheets 429 retry (sheets.md:93) lives in group C; failures.md:62 (Retry on 429/500/503, wait = 2^attempt + random, max 3) is a neighbouring statement that must not contradict: for Sheets quota 429 wait >= 60 s via continueErrorOutput, not retryOnFail and not 2 s (resolved contradiction 3а-5, version A)
N11 | ПРАВИЛО | contradiction-1 | устаревший инструмент снимается с публикации тем же действием | Contradiction 1: deprecated tool is unpublished (active:false) with the same action it is declared deprecated, verified by reading active:false; not archived. Home SKILL.md:61 (group A); relevant to D only if failures/mcp mention archiving (they do not) — expect none
