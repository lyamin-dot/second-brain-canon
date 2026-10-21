# Units — group A (checker Opus), synthesis apps-script-sheets 2026-10-20, step С2

group: A
files covered: ROOT/old/SKILL.md lines 1–245 (frontmatter, header and edit history 6–31, «Как устроен Skill» 33, table «Что читать дальше» 35–40, §0 44–48, §1 52–66, §2.1–2.7 70–242)
NEW sources: CLONE/meta/HARVEST_2026-10-18_edits/apps-script-sheets.md (edits #2, #3); ROOT/in/queue_rows.md (AJ-16); ROOT/in/WRITER_BRIEF.md (AJ-16, separator contradiction); CLONE/projects/gas-bridge/PLAN.md, LOG.md, STATE.md (AJ-16); CLONE/projects/sku-cost/PLAN.md (Х-9)
total units: 298 (OLD 252, NEW 46); every quote verified by script as a substring of its cited line, all quotes ≤80 chars
OLD by class: ПРАВИЛО 81, ПОРОГ 57, ПРИЧИНА 38, СЛУЧАЙ 38, АДРЕС 16, ПРОВЕРКА 15, ИСКЛЮЧЕНИЕ 7
OLD by flag: ИСТ 46, ОСОБ 14, КОПИЯ 8
NEW by class: ПРАВИЛО 23, СЛУЧАЙ 9, ПРИЧИНА 6, ПОРОГ 4, АДРЕС 3, ИСКЛЮЧЕНИЕ 1
NEW by flag: ОСОБ 10, ИСТ 8, КОПИЯ 1
Lines without a unit: only headings, separators and code syntax (2, 6, 35, 36, 52, 70, 72, 90–91, 96 [covered by U145], 103–125 converter loop internals, 127, 144, 162, 185, 196, 211, 230).
Checker notes for task 2: (1) U61 «ru_RU» is refuted by NEW N3–N7 — the new text must drop it, not keep it. (2) U70 reason is corrected by N36 (gas-bridge LOG Р-1): the cause was the credential binding, not an API denial. (3) U69/U115–U117 must be narrowed to books outside gas_allowlist (N15–N17), not deleted. (4) U110 «Andrei runs setupAll» stays true under AJ-16 (N27–N28: stage B not decided).

Format: `U<n> | CLASS | file:line | verbatim quote ≤80 | paraphrase | FLAGS`
File prefix «SKILL.md» = ROOT/old/SKILL.md. FLAGS: ИСТ, ОСОБ, КОПИЯ (with map verdict in brackets).

## OLD

### Frontmatter (line 3) and header (6–10)
U1 | ПРАВИЛО | SKILL.md:3 | ОБЯЗАТЕЛЬНО читай перед любой переделкой Google Sheets через Apps Script | Trigger of the whole Skill: any rework of a Google Sheet by Apps Script. |
U2 | ПОРОГ | SKILL.md:3 | оформление, условное форматирование, спарклайны, графики, правка формул | Trigger words list 1: formatting, conditional formatting, sparklines, charts, formula edits. |
U3 | ПОРОГ | SKILL.md:3 | сборка дашборда или книги по сырым данным, конструкция сигнала и подбор порогов | Trigger words list 2: dashboard/book from raw data, signal design, threshold choice. |
U4 | ПОРОГ | SKILL.md:3 | вынос текста для n8n | Trigger word: moving alert text out for n8n. |
U5 | ПОРОГ | SKILL.md:3 | Ловушки локали формул (разделители и десятичная запятая), модального окна, дат | Named traps 1: formula locale, modal dialog, dates and time zone. |
U6 | ПОРОГ | SKILL.md:3 | merge и закрепления, именованных диапазонов, управляющих ячеек, тяжёлой книги | Named traps 2: merge+freeze, named ranges, control cells, heavy book. |
U7 | ПОРОГ | SKILL.md:3 | колонки-формулы, ключа сравнения и склейки IMPORTRANGE, расписания и триггеров | Named traps 3: formula column, comparison key, IMPORTRANGE join, schedule/triggers. |
U8 | АДРЕС | SKILL.md:3 | лежат в references/ и читаются перед своим действием по таблице «Что читать даль | Book traps, design, signal live in references/, read before their action via routing table. |
U9 | АДРЕС | SKILL.md:8 | Парный Skill: `google-drive-docs` (чтение и запись Drive, gsheets-read, gdocs-*) | Paired Skill google-drive-docs owns Drive read/write, gsheets-read, gdocs-*. |
U10 | ПРАВИЛО | SKILL.md:8 | Этот файл — про то, что происходит **внутри** книги, когда её перестраивает | Zone of this Skill: what happens inside the book when Apps Script rebuilds it. |
U11 | ПРАВИЛО | SKILL.md:10 | ПОДТВЕРЖДЕНИЕ ПОСЛЕ ПРОЧТЕНИЯ: номер параграфа + дословная цитата правила | After reading: confirm with paragraph number + verbatim quote of a rule relevant to task. | КОПИЯ(ОСТАВИТЬ — замок у каждого Skill)
U12 | ИСКЛЮЧЕНИЕ | SKILL.md:10 | Фиксированная фраза не принимается. | A fixed phrase does not count as confirmation. | КОПИЯ(ОСТАВИТЬ)

### Edit-history header (12–31)
U13 | АДРЕС | SKILL.md:12 | Правка 2026-10-13 по стадии Б Архивариуса (запись Р-38 журнала `projects/archiva | Edit 2026-10-13 from Archivarius stage B, journal record Р-38. | ИСТ
U14 | СЛУЧАЙ | SKILL.md:13 | правило проверки данных принадлежит ячейке; `getDataValidation` для ячейки без | History: §1 got the data-validation-per-cell rule (lesson У-145); duplicates line 58. | ИСТ
U15 | СЛУЧАЙ | SKILL.md:14 | формулой становится строка на `=`, записанная и `setValue`, и `setValues` | History: §2.5 extended to setValues and «=== РАЗДЕЛ ===» headers (У-146). | ИСТ
U16 | СЛУЧАЙ | SKILL.md:14 | `asText_` больше не превращает отрицательное число в текст | History: asText_ fixed to not turn negative numbers into text (substance in line 217/220). | ИСТ
U17 | СЛУЧАЙ | SKILL.md:15 | Таблица ошибок §6 дополнена; в таблице «Что читать дальше» references/book-traps | History: §6 extended; routing row for book-traps now covers 3.1–3.12. | ИСТ
U18 | СЛУЧАЙ | SKILL.md:16 | references/book-traps.md: новый §3.12 — колонка по заголовку и повторяющиеся | History: new §3.12 (column by header, duplicate headers, У-156). | ИСТ
U19 | АДРЕС | SKILL.md:18 | Правка 2026-10-09 по харвесту 2026-10-08: | Edit 2026-10-09 from harvest 2026-10-08. | ИСТ
U20 | СЛУЧАЙ | SKILL.md:19 | живой текст скрипта — только присланный Андреем, обход через резервную копию `.g | History: §1 live-script rule and .gs backup bypass (finding А15). | ИСТ
U21 | СЛУЧАЙ | SKILL.md:19 | книга скрипту не принадлежит — лист читается целиком в режиме FORMULA перед | History: §1 «book doesn't belong to script» (А18). | ИСТ
U22 | СЛУЧАЙ | SKILL.md:19 | правки после первого прогона — полным текстом файла, а не патчами | History: full-file edits instead of patches (contradiction В9). | ИСТ
U23 | СЛУЧАЙ | SKILL.md:20 | §4.2: колонки владельца — запись только в пустую ячейку, без `clear()` всего лис | History: §4.2 owner columns (А18) — group B substance. | ИСТ
U24 | СЛУЧАЙ | SKILL.md:21 | §4.5: сверка по всем неделям, формулой в таблице, с `ROUND(…;2)` (А17) | History: §4.5 reconciliation changes (А17, Б4) — group B substance. | ИСТ
U25 | СЛУЧАЙ | SKILL.md:22 | §4.7: тяжёлый необязательный пункт меню — последним (Б4). Новый §4.9 | History: §4.7, new §4.9 schedule check, onEdit not on formula — group B substance. | ИСТ
U26 | СЛУЧАЙ | SKILL.md:23 | references/book-traps.md: §3.4 переписан — открытый диапазон со строки данных | History: book-traps §3.4 rewrite and new §3.8–3.11 (А16, А32, AH-22, А34, Б4, Б10). | ИСТ
U27 | СЛУЧАЙ | SKILL.md:24 | references/design.md: процентный формат умножает на 100, суффикс «п.п.» — нет (Б | History: design.md percent format note. | ИСТ
U28 | СЛУЧАЙ | SKILL.md:26 | Редакция 2026-09-28. | Edition date 2026-09-28. | ИСТ
U29 | АДРЕС | SKILL.md:27 | Из очереди `registry/maintenance-queue.md`: AH-3 — тяжёлая книга (§3.7, §4.3, §4 | Queue positions AH-3…AH-10 as basis addresses of §3.7/4.3/4.8/2.1/4.1/2.2/2.7/2.3/3.6/3.3. | ИСТ
U30 | СЛУЧАЙ | SKILL.md:28 | Вне очереди, по опыту книг «Цена», «Деньги», «Товары» 2026-09-28 | History: rules from books «Цена/Деньги/Товары» 2026-09-28 (quotes in loc_, setFormulas, named range, etc.). | ИСТ ОСОБ
U31 | СЛУЧАЙ | SKILL.md:29 | Вне очереди, по задачам РЫЧАГ Зоны А INDEX OZON_UE: гард по левой границе данных | History: §3.3 left-border guard from OZON_UE tasks. | ИСТ
U32 | СЛУЧАЙ | SKILL.md:30 | Исправлены ошибки прежней редакции: ссылка на `showMap` в §1 (стояло §4.5, верно | History: fixed showMap ref, setFormula ban, gate wording. | ИСТ
U33 | ПРАВИЛО | SKILL.md:31 | Устранены повторы: каждое правило сказано в одном месте, остальные места ссылают | Structure rule: each rule stated once, other places point to it. | ИСТ
U34 | СЛУЧАЙ | SKILL.md:31 | Раздел 7 «Антипаттерны» снят — все его пункты повторяли правила §0–§9 | History: section 7 removed as duplicate. | ИСТ
U35 | АДРЕС | SKILL.md:31 | Раздел 8 «Образцы» перенесён в references/samples.md | Section 8 lives in references/samples.md; error rows of §3/§9 in their reference files. | ИСТ

### «Как устроен Skill» (33) and routing table (35–40)
U36 | АДРЕС | SKILL.md:33 | нарезка по событию — решение Р-19 журнала `projects/kontext-reduktion/LOG.md` | Basis of event-slicing: decision Р-19 of kontext-reduktion journal (after Р-18). | ИСТ
U37 | ПРАВИЛО | SKILL.md:33 | Этот файл читается всегда | SKILL.md is always read. |
U38 | ПРИЧИНА | SKILL.md:33 | нужны любому скрипту над книгой | Two rules, work order, traps, mandatory parts, error table are needed by any script. |
U39 | ПРАВИЛО | SKILL.md:33 | читается один раз за сессию — перед первым действием своего вида, целиком | Reference files: read once per session, before first action of their kind, in full. |
U40 | ПРАВИЛО | SKILL.md:33 | Номера параграфов сохранены прежними | Paragraph numbers are stable; any «§N» resolves via the table. |
U41 | ПРАВИЛО | SKILL.md:37 | писать или чинить формулы витрины: периоды, знаки затрат, границы диапазонов | Route: writing/fixing dashboard formulas (periods, cost signs, range borders, «strange zero», control cells, array formulas) → book-traps. |
U42 | ПРАВИЛО | SKILL.md:37 | писать в колонку рядом с формулами; сравнивать или склеивать по ключу, IMPORTRAN | Route: writing next to formulas, key compare/join, IMPORTRANGE → book-traps. |
U43 | ПРАВИЛО | SKILL.md:37 | читать лист-источник скриптом по именам заголовков | Route: reading a source sheet by header names → book-traps. |
U44 | ПРАВИЛО | SKILL.md:37 | работать с тяжёлой книгой вроде sku_cost_Шаблон | Route: heavy book → book-traps (example names a concrete book). | ОСОБ
U45 | ПОРОГ | SKILL.md:37 | references/book-traps.md | 3.1–3.12 | book-traps covers §3.1–3.12. |
U46 | ПРАВИЛО | SKILL.md:38 | оформлять: цветовые шкалы, дельты, форматы единиц, спарклайны, графики, текст | Route: formatting, sparklines, charts, n8n alert text, row heights, column order → design.md. |
U47 | ПОРОГ | SKILL.md:38 | references/design.md | 5 | design.md covers §5. |
U48 | ПРАВИЛО | SKILL.md:39 | строить или менять сигнал витрины: база сравнения, знак, семьи строк, пол | Route: building/changing a signal (base, sign, families, materiality floor, threshold, rule-change check) → signal.md. |
U49 | ПОРОГ | SKILL.md:39 | references/signal.md | 9.1–9.8 | signal.md covers §9.1–9.8 (NEW #2 extends to 9.9). |
U50 | ПРАВИЛО | SKILL.md:40 | начинать новую витрину или новую книгу по сырым данным; искать рабочий образец | Route: new dashboard/book from raw data, looking for code sample or constructor doc → samples.md. |
U51 | ПОРОГ | SKILL.md:40 | references/samples.md | 8 | samples.md covers §8. |

### §0 (44–48)
U52 | ПРАВИЛО | SKILL.md:44 | ДВА ПРАВИЛА БЕЗ ИСКЛЮЧЕНИЙ | Section 0 rules have no exceptions. |
U53 | ПРАВИЛО | SKILL.md:46 | Ни одна ячейка не стирается, пока не построена карта ссылок на неё. | No cell is erased before a reference map to it is built. |
U54 | ПРАВИЛО | SKILL.md:46 | Перед любой очисткой, перестройкой или сдвигом разметки листа | Trigger of 0.1: any clear, rebuild, or layout shift of a sheet. |
U55 | ПРАВИЛО | SKILL.md:46 | обойти ВСЕ листы книги и найти формулы, которые на этот лист ссылаются | Scan ALL sheets for formulas referencing this sheet. |
U56 | АДРЕС | SKILL.md:46 | (§4.6, `findRefs`) | The tool for 0.1 is findRefs, §4.6. |
U57 | ПРИЧИНА | SKILL.md:46 | Вывод «лист пуст, можно занимать», сделанный по прочитанному диапазону, ничего н | «Sheet empty, can take it» from a read range is worthless... |
U58 | ПРИЧИНА | SKILL.md:46 | диапазон почти всегда у́же листа | ...because the read range is almost always narrower than the sheet. |
U59 | ПРАВИЛО | SKILL.md:48 | Формула, записанная через `setFormula` или `setFormulas`, попадает в ячейку БУКВ | setFormula/setFormulas write formula text literally. |
U60 | ПРАВИЛО | SKILL.md:48 | Перевода в локаль книги не происходит. | No translation into the book locale happens. |
U61 | ПОРОГ | SKILL.md:48 | У книг Андрея локаль `ru_RU`. | Claim: Andrei's books have ru_RU locale (refuted by NEW #3: locale differs per book). | ОСОБ
U62 | АДРЕС | SKILL.md:48 | Подробно — §2.1. | Details in §2.1. |

### §1 Work order (52–66)
U63 | ПРАВИЛО | SKILL.md:54 | `gsheets-read` mode `meta` → список листов | Recon step 1: gsheets-read meta → list of sheets. |
U64 | ПРАВИЛО | SKILL.md:54 | Затем `mode:"range"` с `render:"FORMULA"` по каждому рабочему листу | Then range read with render FORMULA of each working sheet. |
U65 | ПРАВИЛО | SKILL.md:54 | Читать ШИРЕ, чем кажется нужным: колонки до Z, а не до J. | Read wider than needed: columns to Z, not J. |
U66 | ПРИЧИНА | SKILL.md:54 | Стоимость лишней колонки — ноль, стоимость пропущенной — §3.1. | Extra column costs nothing; missed column costs §3.1. |
U67 | ПОРОГ | SKILL.md:54 | признак `truncated` (больше 500 строк — вернулась только часть) | Response sign truncated: >500 rows → only part returned. | КОПИЯ(ОСТАВИТЬ указатель)
U68 | АДРЕС | SKILL.md:54 | Контракт ответа и признак `truncated` | Response contract lives in google-drive-docs §4.0. | КОПИЯ(ОСТАВИТЬ указатель)
U69 | ПРАВИЛО | SKILL.md:55 | **Живой текст скрипта — только тот, что прислал Андрей.** | Live script text = only what Andrei sent (to be narrowed by AJ-16 to books outside gas_allowlist). |
U70 | ПРИЧИНА | SKILL.md:55 | Apps Script API не даёт сервисному аккаунту доступа к личным скриптам | Reason given: Apps Script API denies service account access to personal scripts (gas-bridge LOG Р-1 says the real cause was the credential binding). |
U71 | СЛУЧАЙ | SKILL.md:55 | воркфлоу gscript-read так и не заработал, `projects/wb-ue/STATE.md` | Workflow gscript-read never worked (state of a concrete workflow). | ИСТ ОСОБ
U72 | ПРАВИЛО | SKILL.md:55 | Обход — Андрей кладёт резервную копию `.gs` в Drive, и сессия читает её целиком | Bypass: Andrei puts a .gs backup in Drive, session reads it fully via gdocs-read. |
U73 | АДРЕС | SKILL.md:55 | `projects/wb-ue/LOG.md`, запись о сервисном аккаунте и Apps Script API | Basis address of the bypass. | ИСТ
U74 | ПРАВИЛО | SKILL.md:55 | Техническая документация книги отстаёт от кода: править по техдоку вместо кода | Never edit from technical documentation instead of code; docs lag code. |
U75 | СЛУЧАЙ | SKILL.md:55 | так 2026-09-30 правка `oz_goods_book.gs` зашла в тупик | Case: 2026-09-30 oz_goods_book.gs edit dead-ended (labs/ozon-ue/t-goods-book-script.md). | ИСТ ОСОБ
U76 | СЛУЧАЙ | SKILL.md:55 | по журналу OZON_UE_INDEX 2026-09-27 и 2026-09-29 расхождение кода с документацие | Case: code/doc mismatch gave 19 003 ₽ in wrong article (OZON_UE_INDEX). | ИСТ ОСОБ
U77 | ПРАВИЛО | SKILL.md:55 | Своя рабочая копия из прошлой сессии — тоже не живой текст | Own working copy from a past session is not live text. |
U78 | ПРИЧИНА | SKILL.md:55 | Андрей мог править файл руками. | Because Andrei may have edited the file by hand. |
U79 | ПРАВИЛО | SKILL.md:56 | **Книга скрипту не принадлежит.** | The book does not belong to the script. |
U80 | ПРИЧИНА | SKILL.md:56 | Андрей правит книгу руками параллельно скрипту. | Andrei edits the book by hand in parallel. |
U81 | ПРАВИЛО | SKILL.md:56 | перед добавлением метрики лист читается целиком в режиме `FORMULA` | Before adding a metric read the whole sheet in FORMULA mode. |
U82 | ПРАВИЛО | SKILL.md:56 | включая строки за пределами известной разметки | Including rows beyond the known layout. |
U83 | ПРАВИЛО | SKILL.md:56 | изменившаяся подпись строки — не признак правки скрипта, спросить дешевле | A changed row label is not evidence of a script edit; asking is cheaper. |
U84 | СЛУЧАЙ | SKILL.md:56 | (`projects/wb-ue/LOG.md`, Р-50) | Basis: wb-ue journal Р-50. | ИСТ
U85 | АДРЕС | SKILL.md:56 | Как скрипт обходится с колонками владельца — §4.2. | Owner columns handling — §4.2. |
U86 | ПРАВИЛО | SKILL.md:57 | `gsheets-read` не отдаёт ни в одном режиме: в его ответе есть только значения и | Formatting (number formats, widths, heights, fill, font, CF rules, charts) is not returned by gsheets-read in any mode. | КОПИЯ(ЗАМЕНИТЬ ССЫЛКОЙ одну из двух; дом GDD, ASS держит список методов дампа)
U87 | ПОРОГ | SKILL.md:57 | числовые форматы, ширины колонок, высоты строк, заливку, шрифт, правила условног | List of formatting kinds not returned. |
U88 | ПРАВИЛО | SKILL.md:57 | первым шагом идёт скрипт-дамп, который Андрей запускает сам | Formatting task: first step is a dump script that Andrei runs. |
U89 | ПОРОГ | SKILL.md:57 | `getNumberFormats`, `getBackgrounds`, `getColumnWidth`, `getRowHeight` | Dump methods part 1. |
U90 | ПОРОГ | SKILL.md:57 | `getConditionalFormatRules`, `getCharts` | Dump methods part 2. |
U91 | ПРАВИЛО | SKILL.md:57 | пишет снимок на отдельный лист или в отдельную книгу, а сессия потом читает этот | Dump writes a snapshot to a separate sheet/book; session reads it via gsheets-read. |
U92 | ПРАВИЛО | SKILL.md:57 | Шаг «прочитать оформление через gsheets-read» в план и в эстафету не ставится | Never put «read formatting via gsheets-read» in a plan or handoff. |
U93 | ПРИЧИНА | SKILL.md:57 | он неисполним | Because it is impossible. |
U94 | СЛУЧАЙ | SKILL.md:57 | (позиция AG-18 очереди, сессия OZON_UE 2026-09-26) | Basis: queue AG-18, OZON_UE session 2026-09-26. | ИСТ
U95 | ПРАВИЛО | SKILL.md:58 | **Проверка данных (выпадающий список, правило ввода) принадлежит ячейке, а не | Data validation belongs to a cell, not a column. |
U96 | ПРАВИЛО | SKILL.md:58 | `gsheets-read` её тоже не отдаёт — её читает тот же скрипт-дамп через | gsheets-read doesn't return validation; the dump reads it via getDataValidations(). |
U97 | ПОРОГ | SKILL.md:58 | Для ячейки без правила `getDataValidation()` возвращает `null` | getDataValidation() returns null for a cell without a rule. |
U98 | ПОРОГ | SKILL.md:58 | `getDataValidations()` ставит `null` на место каждой такой ячейки | getDataValidations() puts null in each such position. |
U99 | АДРЕС | SKILL.md:58 | документация Apps Script, класс Range, прочитано 2026-10-13 | Source: Apps Script docs, class Range, read 2026-10-13. |
U100 | ПРИЧИНА | SKILL.md:58 | Строка-подсказка, шапка и служебные строки правила обычно не несут | Hint/header/service rows usually carry no rule, so null there ≠ free input. |
U101 | ПРАВИЛО | SKILL.md:58 | правила читать по нескольким строкам с реальными данными | Read validation rules on several real-data rows. |
U102 | СЛУЧАЙ | SKILL.md:58 | Основание: 1 случай, 2026-07-23 — зонд правил на служебной строке-подсказке дал | Basis: 1 case 2026-07-23, probe on hint row gave false «free input». | ИСТ
U103 | АДРЕС | SKILL.md:58 | WB_REVIEWS_INDEX, строка 1937; урок У-145 журнала `projects/archivarius/LOG.md` | Case addresses: WB_REVIEWS_INDEX line 1937; lesson У-145. | ИСТ
U104 | ПРАВИЛО | SKILL.md:59 | **Карта зависимостей.** Прогнать `findRefs` и `showMap` (оба — §4.6). | Step 2: run findRefs and showMap (§4.6). |
U105 | ПРАВИЛО | SKILL.md:59 | Только после этого принимать решения о разметке. | Only then decide on layout. |
U106 | ПРАВИЛО | SKILL.md:60 | Согласовать с Андреем: что чиним, что строим, где что лежит. | Step 3: agree the project with Andrei. |
U107 | ПРАВИЛО | SKILL.md:60 | Гейт обязателен | The gate is mandatory. |
U108 | ПРИЧИНА | SKILL.md:60 | правку формул в рабочей книге откатить можно только историей версий и только всю | Formula edits can only be undone by version history of the whole book, with everything changed since. |
U109 | ПРАВИЛО | SKILL.md:61 | Один файл, идемпотентный, со всеми обязательными частями из §4. | Step 4: one file, idempotent, all mandatory parts of §4. |
U110 | ПРАВИЛО | SKILL.md:62 | Андрей вставляет и запускает `setupAll`. | Step 5: Andrei pastes and runs setupAll (running stays Andrei's under AJ-16 too). |
U111 | ПРАВИЛО | SKILL.md:62 | Скрипт не падает на первой ошибке (§4.4) | Script doesn't stop at first error (§4.4). |
U112 | ПРИЧИНА | SKILL.md:62 | один прогон показывает все проблемы и время каждого шага | One run shows all problems and timing of each step. |
U113 | ПРОВЕРКА | SKILL.md:63 | Читать результат самому через `gsheets-read`, не по отчёту скрипта. | Step 6: verify by reading the result yourself, not by script report. | КОПИЯ(ОСТАВИТЬ — одна строка)
U114 | ПРИЧИНА | SKILL.md:63 | Отчёт скрипта — гипотеза. | Script report is a hypothesis. |
U115 | ПРАВИЛО | SKILL.md:65 | Правки после первого прогона давать **полным текстом файла на вставку** | Edits after the first run are given as full file text to paste. |
U116 | ПРАВИЛО | SKILL.md:65 | Андрей выделяет всё в редакторе Apps Script и вставляет файл целиком | Andrei selects all in editor and pastes the whole file. |
U117 | ПРАВИЛО | SKILL.md:65 | Перед выдачей — сверка с живым текстом, который прислал Андрей (пункт 1 выше) | Before handing out: diff against the live text Andrei sent, not own copy. |
U118 | ПРАВИЛО | SKILL.md:65 | в сопроводительном сообщении — короткий перечень изменённых функций | Accompanying message lists the changed functions. |
U119 | ПРИЧИНА | SKILL.md:65 | чтобы правку можно было проверить глазами | So the edit can be checked by eye. |
U120 | СЛУЧАЙ | SKILL.md:65 | Так выданы `oz_goods_book.gs` и `oz_price_book.gs` 2026-10-06, и так хочет Андре | Basis: two books 2026-10-06 + Andrei's preference. | ИСТ ОСОБ
U121 | СЛУЧАЙ | SKILL.md:66 | ИСТОРИЯ ДИАГНОЗА: до 2026-10-09 здесь стояло обратное правило | Refuted earlier rule «point patches было→стало» (5th full reupload of 1300 lines argument). | ИСТ
U122 | СЛУЧАЙ | SKILL.md:66 | Отменено предпочтением владельца и практикой 2026-10-06 (противоречие В9 харвест | Reversed by owner preference and practice 2026-10-06 (contradiction В9). | ИСТ
U123 | ПРИЧИНА | SKILL.md:66 | ручная вставка нескольких патчей в разные места файла дороже и опаснее одной | Manual multi-patch pasting is costlier/riskier than one full paste... |
U124 | ПРИЧИНА | SKILL.md:66 | пропущенный или вставленный не туда патч не виден до прогона | ...a missed/misplaced patch is invisible until run. |

### §2.1 Locale (72–142)
U125 | ПРАВИЛО | SKILL.md:74 | Распространённое и ложное убеждение: «Apps Script принимает формулы в американск | Not-confuse: Apps Script does NOT translate US-notation formulas into the locale. |
U126 | ПОРОГ | SKILL.md:75 | разделитель аргументов — `;`, а не `,` | ru_RU argument separator is «;». |
U127 | ПОРОГ | SKILL.md:76 | разделитель колонок в массивах — `\`, а не `,` | ru_RU array column separator is «\». |
U128 | ПОРОГ | SKILL.md:77 | разделитель строк в массивах — `;` (как в US) | Array row separator «;» (as in US). |
U129 | ПОРОГ | SKILL.md:78 | десятичный разделитель в числе — `,`, а не `.`: `0.95` в формуле даёт ошибку раз | Decimal separator «,»; 0.95 gives a parse error. |
U130 | ПРОВЕРКА | SKILL.md:80 | Формула с запятыми даёт `#ERROR!` в каждой ячейке. | Symptom: formula with commas → #ERROR! in every cell. |
U131 | ПРОВЕРКА | SKILL.md:80 | полторы тысячи ошибок разом, ровно по числу записанных формул | Symptom: error count equals number of formulas written. |
U132 | ПРОВЕРКА | SKILL.md:80 | Формула с дробным литералом даёт `#ERROR! (Formula parse error)` и тянет за собо | Symptom: decimal literal → parse error that cascades to dependents. |
U133 | СЛУЧАЙ | SKILL.md:80 | книга «Цена» 2026-09-28 уронила так 3 304 формулы из 3 304 (позиция AH-5) | Case: book «Цена» lost 3304/3304 formulas (AH-5). | ИСТ ОСОБ
U134 | ПРАВИЛО | SKILL.md:82 | Код пишет формулы в американской записи | Code writes formulas in US notation. |
U135 | ПРИЧИНА | SKILL.md:82 | так их проще читать и сверять | Easier to read and compare. |
U136 | ПРАВИЛО | SKILL.md:82 | каждая формула перед записью проходит через контекстный конвертер | Every formula passes a context-aware converter before writing. |
U137 | ПРАВИЛО | SKILL.md:82 | Разделитель определяется опытом, не списком локалей | Separator is determined by experiment (probe), not by locale list. |
U138 | ПОРОГ | SKILL.md:85 | var SEP = ','; | Default SEP is «,» until probe. |
U139 | ИСКЛЮЧЕНИЕ | SKILL.md:87 | Зонд пишет в книгу и ждёт пересчёта: только лёгкая книга и только первым шагом | Probe writes and waits for recalculation: light book only, first write step only (§4.8). |
U140 | ПОРОГ | SKILL.md:88 | function detectSeparator_(ss) { | Probe function name detectSeparator_. |
U141 | ПОРОГ | SKILL.md:89 | var tmp = ss.insertSheet('_probe_' + new Date().getTime()); | Probe uses a temporary sheet _probe_<timestamp>. |
U142 | ПОРОГ | SKILL.md:92 | tmp.getRange('A1').setFormula('=SUM(1,2)'); | Probe writes =SUM(1,2). |
U143 | ПОРОГ | SKILL.md:93 | SpreadsheetApp.flush(); | Flush before reading probe result. |
U144 | ПРОВЕРКА | SKILL.md:94 | ok = (tmp.getRange('A1').getDisplayValue() === '3'); | Comma works iff display value is «3». |
U145 | ПРАВИЛО | SKILL.md:95 | } finally { | Temp sheet deleted in finally (line 96 ss.deleteSheet(tmp)) even on error. |
U146 | ПОРОГ | SKILL.md:98 | return ok ? ',' : ';'; | Probe returns «,» or «;». |
U147 | ПОРОГ | SKILL.md:102 | if (SEP === ',') return f; | Converter is identity when SEP is «,». |
U148 | ПРАВИЛО | SKILL.md:106 | "строка" и 'имя листа' не трогаем | Converter skips string literals and quoted sheet names. |
U149 | ПРАВИЛО | SKILL.md:110 | // удвоенная кавычка внутри | Doubled quote inside a literal/name is kept, not treated as end. |
U150 | ПОРОГ | SKILL.md:117 | if (ch === '(' || ch === '{') { stack.push(ch); out += ch; continue; } | Bracket stack tracks () vs {}. |
U151 | ПОРОГ | SKILL.md:120 | out += (stack.length && stack[stack.length - 1] === '{') ? '\\' : ';'; | Comma → «\» inside {}, else «;». |
U152 | ПОРОГ | SKILL.md:124 | if (ch === '.' && /[0-9]/.test(f.charAt(i - 1)) && /[0-9]/.test(f.charAt(i + 1)) | Decimal point between digits → comma. |
U153 | ПОРОГ | SKILL.md:131 | rng.setFormula(loc_(formula)); | setF_ writes via loc_. |
U154 | ПОРОГ | SKILL.md:132 | return rng; | setF_ returns the range. |
U155 | ПРАВИЛО | SKILL.md:136 | Контекст обязателен. | Conversion must be context-aware. |
U156 | ПРИЧИНА | SKILL.md:136 | Наивная замена всех запятых ломает `TEXT(x,"#,##0")` | Naive replace breaks TEXT format strings. |
U157 | ПРАВИЛО | SKILL.md:136 | Имя листа в одинарных кавычках (`'Деньги, 2.0'!A1`) тоже не трогается | Quoted sheet names untouched. |
U158 | ПРИЧИНА | SKILL.md:136 | Возврат диапазона нужен, чтобы работала цепочка `setF_(...).setNumberFormat(...) | Returning range enables chaining. |
U159 | ИСКЛЮЧЕНИЕ | SKILL.md:138 | Дробь без ведущего нуля (`.5`) конвертер не видит | Converter misses .5 (no leading zero). |
U160 | ПРАВИЛО | SKILL.md:138 | Писать всегда `0.5`. | Always write 0.5. |
U161 | ПРАВИЛО | SKILL.md:138 | Имя листа с точкой или запятой писать только в одинарных кавычках | Sheet names with dot/comma only in single quotes. |
U162 | ПРИЧИНА | SKILL.md:138 | `Sheet2.1!A1` без кавычек конвертер испортит в `Sheet2,1!A1` | Unquoted name gets corrupted. |
U163 | СЛУЧАЙ | SKILL.md:140 | Конвертер проверен в node 2026-09-28 на пяти формулах | Converter tested in node on five formulas (list). | ИСТ
U164 | ПРОВЕРКА | SKILL.md:142 | каждая запись формулы в файле — это `setF_(…)` либо `setFormulas(…)` массива | Check: every formula write is setF_ or setFormulas of loc_-ed array. |
U165 | ИСКЛЮЧЕНИЕ | SKILL.md:142 | прямой `.setFormula(` без `loc_` допустим только в зонде | Direct setFormula without loc_ only in the probe. |
U166 | ПРАВИЛО | SKILL.md:142 | Колонку формул писать одним вызовом `setFormulas` на диапазон, а не циклом | Write a formula column with one setFormulas call, not per-cell loop. |
U167 | СЛУЧАЙ | SKILL.md:142 | так пишут все три книги §8 (замера цикла по ячейкам нет) | Basis: all three §8 books do so; no measurement of loop. | ИСТ

### §2.2 First function; no modal (144–160)
U168 | ПОРОГ | SKILL.md:146 | Выпадающий список «Выполнить» подставляет функцию, идущую в файле первой. | Editor «Run» picks the first function in the file. |
U169 | ПРИЧИНА | SKILL.md:146 | Если первой стоит `onOpen`, первое нажатие построит меню и ничего больше не сдел | onOpen first → first click only builds menu, looks like success. |
U170 | ПРОВЕРКА | SKILL.md:146 | Второе нажатие упадёт с `Cannot call SpreadsheetApp.getUi() from this context` | Symptom of second click. |
U171 | ПРАВИЛО | SKILL.md:148 | Главная функция (`setupAll`) — первая в файле. | setupAll is first in file. |
U172 | ПРАВИЛО | SKILL.md:148 | `onOpen` обёрнута в `try/catch`. | onOpen wrapped in try/catch. |
U173 | ПРАВИЛО | SKILL.md:150 | Итог прогона выводится НЕ модальным окном. | Run summary is not shown in a modal dialog. |
U174 | ПРИЧИНА | SKILL.md:150 | `SpreadsheetApp.getUi().alert()` держит выполнение, пока в таблице не нажато «ОК | alert() blocks execution until OK. |
U175 | ПОРОГ | SKILL.md:150 | на шестиминутном потолке пишет `Exceeded maximum execution time` | Waiting counts toward 6-minute limit → Exceeded maximum execution time. |
U176 | СЛУЧАЙ | SKILL.md:150 | Книги «Цена» и «Деньги» 2026-09-28: два сорванных прогона | Case: two failed runs (08:47→08:53, 11:34→11:40) vs normal 34–53 s. | ИСТ ОСОБ
U177 | СЛУЧАЙ | SKILL.md:150 | версию «виновато чтение тяжёлой книги» опроверг журнал времени шагов | Not-confuse: «heavy-book read is to blame» refuted by step timing log (AH-6). | ИСТ
U178 | ПРАВИЛО | SKILL.md:150 | Полный текст — в журнал, первая строка — всплывающей подсказкой | Full text to log, first line as toast. |
U179 | ПОРОГ | SKILL.md:154 | Logger.log(msg);   // полный отчёт: редактор скриптов → «Выполнения» | Full report in Logger, viewed in editor → Executions. |
U180 | ПОРОГ | SKILL.md:155 | toast(String(msg).split('\n')[0], 'Ozon', 15) | Toast with first line, 15 s (title 'Ozon' is a book-specific label). |
U181 | ПРАВИЛО | SKILL.md:156 | catch (e) {} | Toast failure is swallowed (no UI context must not crash). |
U182 | ПРАВИЛО | SKILL.md:160 | Первую строку отчёта строить так, чтобы её хватало для решения | First line of report must suffice for a decision. |
U183 | ПОРОГ | SKILL.md:160 | «Готово за 37 с» или «Готово С ОШИБКАМИ за 44 с» | First-line format examples. |

### §2.3 Merge and freeze (162–193)
U184 | ПРОВЕРКА | SKILL.md:164 | Симптом: `Чтобы объединить или разделить ячейки, необходимо выделить весь диапаз | Symptom of merging part of an existing merge. |
U185 | ПРИЧИНА | SKILL.md:164 | предыдущая версия скрипта объединила `A1:L1`, новая пытается объединить `A1:H1` | Cause: new merge is part of old merge. |
U186 | ПРАВИЛО | SKILL.md:166 | В начале перестройки — `breakApart()` по ВСЕМУ листу, а не по очищаемой части. | breakApart the whole sheet at start of rebuild. |
U187 | ПОРОГ | SKILL.md:166 | `breakApart` не стирает содержимое: значение остаётся в левой верхней ячейке | breakApart keeps value in top-left cell. |
U188 | ПОРОГ | SKILL.md:169 | sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns()).breakApart(); | Whole-sheet breakApart code. |
U189 | ПРИЧИНА | SKILL.md:172 | объединение, пересекающее границу очищаемой области | Merge crossing clear-area border gives same error on clear... |
U190 | ПРАВИЛО | SKILL.md:172 | Разъединение по всему листу закрывает и этот случай. | ...whole-sheet unmerge covers it. |
U191 | ПРИЧИНА | SKILL.md:174 | **Копирование формулы тащит за собой объединение исходной ячейки.** | Copying a formula carries the source merge. |
U192 | ПРИЧИНА | SKILL.md:174 | `copyTo(..., PASTE_FORMULA, false)` вправо по листу с закреплённой колонкой A | copyTo right across frozen column A fails whole step (merge across freeze forbidden). |
U193 | ПРАВИЛО | SKILL.md:174 | `breakApart()` по всему листу нужен и перед `copyTo`, а не только перед `clear` | breakApart also before copyTo. |
U194 | ПРИЧИНА | SKILL.md:176 | `setFrozenColumns(n)` падает, если на листе есть строки, объединённые через | setFrozenColumns fails with rows merged across the freeze border. |
U195 | СЛУЧАЙ | SKILL.md:176 | книга «Цена», редакция 1, 2026-09-28, позиция AH-8 | Case: book «Цена» ed.1, AH-8. | ИСТ ОСОБ
U196 | СЛУЧАЙ | SKILL.md:176 | Решение, проверенное на трёх книгах | Basis: solution checked on three books. | ИСТ
U197 | ПРАВИЛО | SKILL.md:176 | закреплять только строки до шапки таблицы включительно, колонки не закреплять | Freeze rows up to header inclusive; don't freeze columns. |
U198 | ПРАВИЛО | SKILL.md:176 | строки инструкции собрать в группу | Group the instruction rows (collapsible). |
U199 | ПОРОГ | SKILL.md:179 | var HEAD_ROW = 10;          // строка шапки таблицы; строки 2–8 — инструкция лис | Example layout: header row 10, instruction rows 2–8 (layout of concrete books). | ОСОБ
U200 | ПРАВИЛО | SKILL.md:181 | Вызывать ПЕРВЫМ при пересборке листа: снимает закрепление и группу прошлого прог | unfreeze_ first on rebuild. |
U201 | ПРИЧИНА | SKILL.md:182 | иначе глубина группы растёт с каждым запуском | Otherwise group depth grows each run. |
U202 | ПОРОГ | SKILL.md:184 | sh.setFrozenRows(0); sh.setFrozenColumns(0); | Unfreeze code. |
U203 | ПОРОГ | SKILL.md:186 | for (var i = 0; i < 5 && sh.getRowGroupDepth(2) > 0; i++) g.shiftRowGroupDepth(- | Remove group depth, max 5 iterations. |
U204 | ПРАВИЛО | SKILL.md:189 | Вызывать ПОСЛЕДНИМ, когда лист построен. | freezeHead_ last. |
U205 | ПОРОГ | SKILL.md:191 | sh.setFrozenRows(HEAD_ROW); | Freeze to HEAD_ROW. |
U206 | ПОРОГ | SKILL.md:192 | sh.getRange('2:8').shiftRowGroupDepth(1); | Group instruction rows. |

### §2.4 Named ranges (196–208)
U207 | ПРИЧИНА | SKILL.md:198 | При удалении имени Google переписывает ВСЕ формулы, которые на него ссылались, в | Deleting a name rewrites all referencing formulas to #REF! in their text. |
U208 | ПРИЧИНА | SKILL.md:198 | Создание имени заново их не чинит | Recreating the name doesn't fix them. |
U209 | ИСКЛЮЧЕНИЕ | SKILL.md:200 | пересоздавать именованный диапазон (remove + set) можно только если все формулы | Recreate (remove+set) only if all users are rewritten after. |
U210 | ПРИЧИНА | SKILL.md:200 | Любая формула, оставленная от прежней версии, превратится в мёртвый `#REF!`. | Leftover formulas die. |
U211 | ПРАВИЛО | SKILL.md:202 | Существующее имя не удалять, а перенаправлять: `namedRange.setRange(новыйДиапазо | Redirect existing name via setRange, don't delete. |
U212 | ПРАВИЛО | SKILL.md:202 | Порядок в `setupAll`: сначала разметка, потом именованные диапазоны, потом ВСЕ | Order: layout → named ranges → all formulas. |
U213 | ПОРОГ | SKILL.md:207 | if (ex) ex.setRange(rng); else ss.setNamedRange(name, rng); | setName_ code: redirect or create. |

### §2.5 setValue «=» (211–224)
U214 | ПРАВИЛО | SKILL.md:213 | Строка, начинающаяся с `=`, записанная через `setValue` или `setValues`, станови | String starting with «=» via setValue/setValues becomes a formula. | КОПИЯ(ОСТАВИТЬ — разные инструменты, взаимные указатели)
U215 | АДРЕС | SKILL.md:213 | «If it begins with '=' it is interpreted as a formula», класс Range, прочитано | Source: Apps Script docs, Range, 2026-10-13. |
U216 | ПРОВЕРКА | SKILL.md:214 | выгрузка карты таблицы: текст формулы считается в контексте нового листа | Case kind 1: map export — formula text evaluated on new sheet... |
U217 | ПРОВЕРКА | SKILL.md:214 | вместо `=$B$2-6` в отчёте оказывается `#VALUE!` | ...symptom #VALUE! instead of formula text. |
U218 | ПРОВЕРКА | SKILL.md:215 | заголовок или подпись вида «=== РАЗДЕЛ ===»: формулой это не разбирается | Case kind 2: «=== РАЗДЕЛ ===» header → #ERROR! instead of text. |
U219 | СЛУЧАЙ | SKILL.md:215 | WB_REVIEWS_INDEX, строка 1932, 2026-07-23; урок У-146 журнала | Case address: WB_REVIEWS_INDEX line 1932, lesson У-146. | ИСТ
U220 | ПРИЧИНА | SKILL.md:215 | узел чтения получает мусорные имена полей | If in header row read by n8n — garbage field names. |
U221 | АДРЕС | SKILL.md:215 | `n8n-engineering-manual`, references/roots.md, корень R6. | Pointer to NEM root R6. |
U222 | ПРАВИЛО | SKILL.md:217 | Ведущий апостроф плюс текстовый формат. | Fix: leading apostrophe plus text format. |
U223 | ПОРОГ | SKILL.md:217 | При чтении через API апостроф не возвращается. | API read doesn't return the apostrophe. |
U224 | ИСКЛЮЧЕНИЕ | SKILL.md:217 | Апостроф ставится только строкам | Apostrophe only for strings, not numbers. |
U225 | ПРИЧИНА | SKILL.md:217 | `-5` превратилось бы в `'-5`, а затраты в книгах Андрея отрицательные (§3.2) | A number checked as string would become text; costs are negative. |
U226 | ИСКЛЮЧЕНИЕ | SKILL.md:217 | Формат `@` ставить только на ячейки текста — шапку, подписи, колонку формул карт | @ format only on text cells. |
U227 | ПРИЧИНА | SKILL.md:217 | что он делает с числом, записанным следом, не проверялось | Effect of @ on later numbers unverified. |
U228 | ПОРОГ | SKILL.md:220 | function asText_(s) { return (typeof s === 'string' && /^[=+\-@]/.test(s)) | asText_ prefixes strings starting with = + - @. |
U229 | ПОРОГ | SKILL.md:221 | rng.setNumberFormat('@').setValues(...) | Set @ format before setValues. |
U230 | ПРИЧИНА | SKILL.md:224 | Какого из двух средств — апострофа или формата `@` — хватает в одиночку | Unknown which of the two suffices alone... |
U231 | ПРАВИЛО | SKILL.md:224 | проверки записью не было, поэтому ставятся оба | ...so both are applied. |

### §2.6 1000 rows (226–228)
U232 | ПОРОГ | SKILL.md:226 | Новый лист по умолчанию 1000 строк | New sheet has 1000 rows by default. |
U233 | ПРИЧИНА | SKILL.md:228 | Выгрузка карты или бэкапа может не поместиться. | Map/backup export may not fit. |
U234 | ПРАВИЛО | SKILL.md:228 | Перед `setValues` проверять `getMaxRows()` и добавлять строки. | Check getMaxRows before setValues, add rows. |

### §2.7 Date and time zone (230–242)
U235 | ПРИЧИНА | SKILL.md:232 | Дата, собранная в скрипте как полночь UTC (`Date.UTC(...)`, арифметика суток в | UTC-midnight date written as is shifts by book time zone. | КОПИЯ(ОСТАВИТЬ — другой объект; дом таймзоны NEM §4.10)
U236 | ПРОВЕРКА | SKILL.md:232 | 46286,083 вместо 46286 | Symptom: fractional serial instead of integer. |
U237 | ПРИЧИНА | SKILL.md:232 | Но фильтр `SUMIFS(…,">="&начало,…,"<="&конец)` выбрасывает граничную неделю | SUMIFS date filter drops border week; period sum silently smaller. |
U238 | СЛУЧАЙ | SKILL.md:232 | книга «Деньги», лист «Деньги по неделям», неделя 21.09.2026, позиция AH-7 | Case: book «Деньги», week 21.09.2026, AH-7. | ИСТ ОСОБ
U239 | ПРАВИЛО | SKILL.md:234 | Внутри скрипта считать в UTC сколько угодно, а перед записью переводить в местну | Compute in UTC inside, convert to local date before write. |
U240 | ПОРОГ | SKILL.md:237 | function localDate_(d) { return new Date(d.getUTCFullYear(), d.getUTCMonth(), d | localDate_ code. |
U241 | ПРИЧИНА | SKILL.md:240 | `new Date(год, месяц, день)` строит полночь в часовом поясе ПРОЕКТА СКРИПТА | new Date(y,m,d) uses script project TZ; cell reads in book TZ. |
U242 | ПРОВЕРКА | SKILL.md:240 | сверить «Настройки проекта» скрипта с `ss.getSpreadsheetTimeZone()` | Check: script project TZ equals spreadsheet TZ. |
U243 | СЛУЧАЙ | SKILL.md:240 | У привязанного скрипта книг Андрея оба пояса одинаковые — проверено результатом | Claim: Andrei's bound scripts have equal TZ (checked by result). | ИСТ ОСОБ
U244 | СЛУЧАЙ | SKILL.md:240 | после `localDate_` даты недель в книге «Деньги» стали целыми | Case: after localDate_ week dates in «Деньги» became integers. | ИСТ ОСОБ
U245 | ПРОВЕРКА | SKILL.md:242 | чтение колонки дат через `gsheets-read` с `render:"UNFORMATTED_VALUE"` | Check: read date column UNFORMATTED_VALUE... |
U246 | ПРОВЕРКА | SKILL.md:242 | даты обязаны прийти целыми числами | ...dates must be integers. |

### Function names in code blocks (added after coverage check)
U247 | ПОРОГ | SKILL.md:101 | function loc_(f) { | Converter function name loc_ (US → book locale). |
U248 | ПОРОГ | SKILL.md:130 | function setF_(rng, formula) { | Single-formula writer setF_ (only allowed path besides setFormulas of loc_-ed array). |
U249 | ПОРОГ | SKILL.md:153 | function alert_(msg) { | Non-modal summary function alert_. |
U250 | ПОРОГ | SKILL.md:183 | function unfreeze_(sh) { | Unfreeze helper name. |
U251 | ПОРОГ | SKILL.md:190 | function freezeHead_(sh) { | Freeze helper name. |
U252 | ПОРОГ | SKILL.md:205 | function setName_(ss, name, rng) { | Named-range redirect helper name. |

## NEW

excluded: AJ-5 #1, #7, #10, #12 (edit-history header lines, not applied — В1), #13 (state of Telegram courier workflow, carrier registry/n8n-map.md — В0, not in Skill). Group A also does NOT own #4, #5 (B), #6, #8, #9, #11 (D), Х-8 (C).

Source prefixes: HE = CLONE/meta/HARVEST_2026-10-18_edits/apps-script-sheets.md; QR = ROOT/in/queue_rows.md; WB = ROOT/in/WRITER_BRIEF.md; GBP = CLONE/projects/gas-bridge/PLAN.md; GBL = CLONE/projects/gas-bridge/LOG.md; GBS = CLONE/projects/gas-bridge/STATE.md; SCP = CLONE/projects/sku-cost/PLAN.md; VS = ROOT/in/verdicts_section4.md.

### AJ-5 #2 — routing row (HE:70)
N1 | ПРАВИЛО | HE:70 | проверять свежесть книги, бэкапа или сводки, назначать порог возраста | Route: checking freshness of a book/backup/summary and setting an age threshold → signal.md. |
N2 | ПОРОГ | HE:70 | references/signal.md | 9.1–9.9 | signal.md row covers §9.1–9.9 (new §9.9 Свежесть). |

### AJ-5 #3 — locale per book, separator by probe (HE:87–88, WB:28)
N3 | ПРАВИЛО | HE:87 | Локаль у книг Андрея не одна: в одних книгах аргументы разделяет `;` (запись `ru | Locale is not one: some books use «;», others «,». Replaces U61. |
N4 | ПРАВИЛО | HE:87 | разделитель определяется зондом в каждой книге при каждом прогоне | Separator is probed in each book on each run... |
N5 | ПОРОГ | HE:87 | `detectSeparator_` (§2.1) | ...by detectSeparator_ (§2.1)... |
N6 | ПРАВИЛО | HE:87 | в тяжёлой книге чтением живой формулы `detectSeparatorByRead_` (§4.8) | ...in a heavy book by reading a live formula, detectSeparatorByRead_ (§4.8). |
N7 | ПРАВИЛО | HE:87 | никогда не переносится из другой книги или из прошлой сессии | Separator is never carried over from another book or a past session. |
N8 | СЛУЧАЙ | HE:88 | Опровергнуто чтением формул 2026-10-14: в книге WB_RAW_Аналитика разделитель `;` | Case: 2026-10-14 WB_RAW_Аналитика «;», Price Master «,» (wb-ue LOG Р-64). | ИСТ ОСОБ
N9 | СЛУЧАЙ | HE:88 | Про ту же книгу Price Master запись 2026-10-09 говорит обратное | Contradiction: meta/PRODUCT_DATA_HIERARCHY.md line 42 says Price Master «;». | ИСТ ОСОБ
N10 | ПРИЧИНА | HE:88 | два канона расходятся об одной книге, и это само показывает, что записанной лока | Recorded locale cannot be trusted — the canon itself disagrees. |
N11 | ПРИЧИНА | HE:88 | но строка подсказывала пропустить зонд | The old ru_RU line invited skipping the probe. |
N12 | ПРАВИЛО | WB:28 | in the Skill — «the separator of each book is determined by a probe» | Skill states only «separator determined by probe»; no per-book value. |
N13 | ПРАВИЛО | WB:28 | the value for a concrete book lives with that book's carrier | Per-book separator value lives with the book's own carrier. | ОСОБ
N14 | ПРАВИЛО | WB:28 | a contradiction in the canon goes as a capture to the book's project | Canon contradiction about a book → capture to that book's project (Price Master). | ОСОБ

### AJ-16 — live script via gas-bridge, clasp emergency path
N15 | ПРАВИЛО | QR:4 | живой текст скрипта книги из таблицы gas_allowlist сессия читает и правит сама ч | For a book in gas_allowlist the session reads and edits the script itself through the bridge. |
N16 | ПРАВИЛО | QR:4 | а не просит у Андрея и не выдаёт полный текст на вставку | ...does not ask Andrei for the text and does not hand out full paste text. |
N17 | ПРАВИЛО | QR:4 | для книг вне таблицы — прежний порядок | Books outside the table: old order (U69–U78, U115–U120). |
N18 | АДРЕС | QR:4 | контракт вызова — `projects/gas-bridge/PLAN.md`, раздел «Контракт вызова» | Call contract lives in gas-bridge PLAN «Контракт вызова». |
N19 | ПОРОГ | GBP:41 | execute_workflow workflowId=38BkuLXhxXLTPpqQ executionMode=manual | Bridge workflow ID — particular; must NOT be in Skill; resolved by name in registry/n8n-map.md (WB:27). | ОСОБ
N20 | ПРАВИЛО | WB:27 | ID taken from the row of CLONE/registry/n8n-map.md by workflow name | Workflow ID is taken from registry/n8n-map.md row by workflow name, never written into Skill. |
N21 | ПРАВИЛО | WB:27 | The sign «book is in gas_allowlist» must be something read in this session | Allowlist membership must be read in this session, not remembered. |
N22 | ПРАВИЛО | GBP:18 | Запись — только в скрипты, у которых в таблице данных n8n `gas_allowlist` стоит | Write only where gas_allowlist access = write; write row added only after Andrei's word. |
N23 | ПРАВИЛО | GBP:18 | Чтение — любой скрипт, доступный аккаунту Андрея. | Read: any script accessible to Andrei's account. |
N24 | ПРАВИЛО | GBP:55 | rules: always read -> write with that projectHash; truncated:true file is incomp | Always read first, write with that projectHash; never edit from a truncated file. |
N25 | ПРАВИЛО | GBP:56 | report versionBefore so the change can be undone | Report versionBefore so the change can be rolled back. |
N26 | ПОРОГ | GBP:43 | nodeNames=["90_Respond"] truncateData=1 | Read the response only from 90_Respond (otherwise script code floods context, GBL Р-2 допущение). |
N27 | ПРАВИЛО | GBP:17 | Функции запускает Андрей: запуск меняет данные книги необратимо | Running functions stays with Andrei (stage B not decided); Skill must not promise session runs functions. |
N28 | ПРАВИЛО | GBS:22 | Этап Б (запуск функций) — только отдельным решением Андрея. | Stage B only by separate Andrei decision. |
N29 | ИСКЛЮЧЕНИЕ | GBP:20 | Код книг в репозиторий не пишется: репозиторий публичный, запись в него необрати | Book code never into repo (И-7). | КОПИЯ(дом second-brain-git И-7)
N30 | ПРАВИЛО | GBL:29 | правку через clasp делает только Андрей, сессия её не планирует | Emergency path: when n8n/bridge unavailable, only Andrei edits via clasp; session doesn't plan it. |
N31 | ПРАВИЛО | GBL:29 | свежий `clasp clone` или `clasp pull` в чистую папку непосредственно перед правк | Emergency order 1: fresh clasp clone/pull into a clean folder right before edit... |
N32 | ПРАВИЛО | GBL:29 | затем первая же сессия читает проект через мост, чтобы получить новый отпечаток | ...then clasp push; then the first session reads via bridge to get the new hash. |
N33 | ПРИЧИНА | GBL:30 | `clasp push` заменяет весь проект содержимым локальной папки, не создаёт версию | clasp push replaces whole project, no version, no hash check — bypasses both bridge protections. |
N34 | ПРИЧИНА | GBL:30 | Устаревшая локальная копия, загруженная после правки моста, молча стирает эту пр | Stale local copy silently erases a bridge edit. |
N35 | АДРЕС | GBL:29 | его текст в зеркале `skills/clasp-apps-script/SKILL.md` остаётся справочником | clasp reference: mirror skills/clasp-apps-script/SKILL.md (not uploaded). |
N36 | ПРИЧИНА | GBL:7 | причина в привязке: узел ждёт ключ входа от имени человека, а стоит ключ сервисн | Correction of U70: gscript-read failed due to credential binding, not API denial. |
N37 | СЛУЧАЙ | GBL:14 | Р-2 | В СИЛЕ | 2026-10-18 | устройство инструмента после приёмки | Basis: bridge accepted 2026-10-18 (executions 82241–82284). | ИСТ
N38 | СЛУЧАЙ | GBL:28 | Р-4 | В СИЛЕ | 2026-10-18 | место clasp рядом с мостом | Basis: clasp = emergency manual path, Andrei «Я за вариант В». | ИСТ
N39 | СЛУЧАЙ | GBS:10 | Подключены на чтение и запись книги Ozon «Деньги» и «Товары» (Р-3) | State: «Деньги», «Товары» write; sku_cost_Шаблон read-only (composition = gas_allowlist). | ОСОБ

### AJ-14 Х-9 — one scope for all files of an Apps Script project (SCP:132–136)
N40 | ПРАВИЛО | SCP:132 | В Apps Script все файлы делят одну область видимости, побеждает определение | All files of a project share one scope; the last-loaded definition wins. |
N41 | ПРИЧИНА | SCP:132 | Порядок загрузки при пустом `filePushOrder` проверить нельзя. | Load order with empty filePushOrder cannot be verified. |
N42 | СЛУЧАЙ | SCP:133 | `setupAll` определена в `Код.js` и в `Исследование таблицы.js`; выполняется толь | Case: setupAll in two files; only one runs. | ИСТ ОСОБ
N43 | СЛУЧАЙ | SCP:134 | `onOpen` определён в `Код.js` и в `Фаза_5.js`; работать будет только одно меню. | Case: two onOpen → one menu. | ИСТ ОСОБ
N44 | СЛУЧАЙ | SCP:135 | `withRetry_` определена в `Код.js` (дважды) и в `Фаза_2.js` | Case: withRetry_ variants with different behaviour; which runs depends on file order. | ИСТ ОСОБ
N45 | СЛУЧАЙ | SCP:136 | Внутри `Код.js` повторно объявлены `SEP`, `withRetry_`, `asText_`, `loc_` и `ale | Case: redeclarations in one file; last wins. | ИСТ ОСОБ
N46 | АДРЕС | VS:32 | Х-9 — файлы проекта Apps Script делят одну область видимости | Verdict: synthesize into cluster 3 (locale/first function), basis sku-cost PLAN 132–136. |
