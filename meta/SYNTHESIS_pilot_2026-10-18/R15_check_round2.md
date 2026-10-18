meta/SYNTHESIS_pilot_2026-10-18/R15_check_round2.md

# Р15 — round 2 check

Inputs: R15_new.md (revised), R15_new_round1.md, R15_old.md, R15_units.md. Addresses checked read-only in /home/claude/second-brain-canon.

## 1. Re-verified units

| id | class | round 1 | round 2 | evidence |
|---|---|---|---|---|
| U-02 | RULE | WEAKENED | IN_TEXT | «**ТРИГГЕР.** Любое утверждение о состоянии системы; любая запись.» (line 3). Widening reverted |
| U-06 | RULE | WEAKENED | IN_TEXT | «ПРОЧИТАНО В ЭТОЙ СЕССИИ (файл)» (line 8) |
| U-13 | RULE | WEAKENED | IN_TEXT | «Конкретика (ID, пороги, версии) берётся из реестра в момент использования, а не из текста задания» (line 26). Executor-only framing removed |
| U-28 | THRESHOLD | WEAKENED | IN_TEXT | «…«не работает из-за Y», «откатилось, потому что»» (line 14) |
| U-32 | RULE | WEAKENED | IN_TEXT | «сохраняется рядом с исправлением блоком ИСТОРИЯ ДИАГНОЗА (`core/R-06a.md`, пункт 0.4.1)» (line 28); core/R-06a.md:60 |
| U-35 | CASE | AT_ADDRESS | AT_ADDRESS | Pointer «запись Р-11 (пункт 5, отменён записью Р-20) … projects/deklaration-wb/LOG.md» (line 32). projects/deklaration-wb/LOG.md:87 (Р-11, 2026-10-09, «ЧАСТИЧНО ОТМЕНЕНО Р-20 (пункт 5: причина не задержка в часы)»), :124 («запись применяется с задержкой в часы»), :163 (Р-20, 2026-10-17: «причина в том, что API не меняет созданный документ без блока documents.items»). A1 pointer replaced by primary source |
| U-36 | CASE | LOST | IN_TEXT | «запись Р-11 (пункт 5, отменён записью Р-20) … журнала `projects/deklaration-wb/LOG.md`» (line 32); confirmed deklaration-wb/LOG.md:87, :161 |
| U-37 | CASE | AT_ADDRESS | AT_ADDRESS | projects/deklaration-ozon/LOG.md:397–399 (Р-46: «механизм «стёрли ОКПД 2» был выводом и записан как факт»); projects/deklaration-wb/LOG.md:169 (Р-21: «запись … без поля needKiz сбрасывает «Нужна маркировка КИЗ»») |
| U-38 | CASE | LOST | IN_TEXT | «запись Р-21 журнала `projects/deklaration-wb/LOG.md`, запись Р-46 журнала `projects/deklaration-ozon/LOG.md`» (line 32); confirmed deklaration-wb/LOG.md:168, deklaration-ozon/LOG.md:397 |
| U-39 | CASE | AT_ADDRESS | AT_ADDRESS | Pointer «записи Р-15, Р-22 … `projects/archive-recon/LOG.md`» (line 32). projects/archive-recon/LOG.md:93 (Р-15, 2026-09-27) with :101 («язык зашит в вызов, потребовались бы правка app.py»); :175–176 (Р-22: «Маршрут /ocr/pdf требует поле lang»). Fully confirmed now, attribution to archive-recon correct |
| U-40 | CASE | AT_ADDRESS | AT_ADDRESS | «записи … Т-4 … (последний случай пойман до записи)» (line 32); projects/archive-recon/LOG.md:162–163 (Т-4: «едва не было записано как «немецкий язык не работает». Причина отказов — параллельная нагрузка»). Fully confirmed |
| U-56 | CASE | AT_ADDRESS | AT_ADDRESS | labs/sys/t-draft-trigger-divergence.md:19 («описание воркфлоу `MPzPrtsnPtf0sVQo` утверждает, что ложная ветка `09_IF_RAW_Rows_Exist` подключена …; в объекте её нет»). Fully confirmed |
| U-57 | CASE | AT_ADDRESS | AT_ADDRESS | labs/sys/t-monitoring-minor.md:10 (паспорт: «по всем 10 воркфлоу» … «в конфиге 6 воркфлоу») |
| U-58 | CASE | AT_ADDRESS | AT_ADDRESS | labs/sys/t-ozon-ue-parked-active.md:12, :14 («документирован как тестовый»; «внесены в Skill `n8n-workflow-registry`»), :52–53 («Прежняя запись «читатель неизвестен» неверна … пишет в боевой лист»; паспорт устарел) |
| U-59 | CASE | AT_ADDRESS | AT_ADDRESS | labs/sys/t-failure-visibility.md:62 («В коде воркфлоу сейчас рабочий fileId; формулировка в описании … «fileId сохранён битым» устарела») |
| U-60 | RULE | WEAKENED | IN_TEXT | «Отсутствие: … — пишется и произносится в ответе \| поиск в собственном носителе объекта» (line 17); canon writes covered by column header «до записи в канон» (line 11) |
| U-72 | CASE | AT_ADDRESS | AT_ADDRESS | projects/archivarius/TRIAGE.md:1556 (stage-B text: «журнал объявлен несуществующим при его ID в мастер-промпте»); TRIAGE.md:94 (У-78 row: «три случая за сутки 2026-07-30») |
| U-73 | CASE | AT_ADDRESS | AT_ADDRESS | projects/archivarius/TRIAGE.md:94 («на ложном опровержении отменена верная правка CORE»); :1556 names `M5dqSv2yiklnDXoP` |
| U-74 | CASE | AT_ADDRESS | AT_ADDRESS | projects/archivarius/TRIAGE.md:94 («есть ли INCIDENT_LOG.md? в реестре нет», файл лежит в папке Skills) |
| U-75 | CASE | AT_ADDRESS | AT_ADDRESS | projects/archivarius/TRIAGE.md:1556 («JOURNAL_INCIDENTS, строки 113–124 и 211–215; урок У-78»); :94 («JOURNAL_INCIDENTS 120–124») |
| U-76 | CASE | LOST | AT_ADDRESS | Pointer «уроки У-78 и У-144 карты `projects/archivarius/TRIAGE.md`» (line 36); TRIAGE.md:165 («ложный отчёт «решения нет» (WB_REVIEWS_INDEX 1722)») |
| U-77 | CASE | IN_TEXT | IN_TEXT | «уроки У-78 и У-144 карты `projects/archivarius/TRIAGE.md`» (line 36). Address corrected from LOG.md to TRIAGE.md, which holds both lessons (:94, :165) |
| U-85 | CASE | AT_ADDRESS | AT_ADDRESS | Pointer «`projects/wb-ue/PLAN.md` строка 67 против `projects/wb-ue/STATE.md` строка 159» (line 38). PLAN.md:67 contains «536 строк»; the 496 is at STATE.md:162 («sku_cost 496 строк, а не 536»), NOT line 159 (line 159 is about nmID sales). Path is right, line number stale (inherited from old text) |
| U-86 | CASE | AT_ADDRESS | AT_ADDRESS | «запись Р-66 … пункт 2 (неделя по нумерации ISO)» (line 38); projects/wb-ue/LOG.md:361 («недель 40, а не 41, как было записано в критерии (нумерация ISO»). Fully confirmed |
| U-90 | CASE | AT_ADDRESS | AT_ADDRESS | «дата — 2, последний 2026-07-30: урок У-45 карты `projects/archivarius/TRIAGE.md`» (line 40); TRIAGE.md:61 («ошибка на 3 дня 2026-07-15 и на 1 день 2026-07-30»), :1543 («пришлось переименовывать файл»). Path now explicit |
| U-91 | CASE | AT_ADDRESS | AT_ADDRESS | TRIAGE.md:61 («(2611, 5781)»); TRIAGE.md:1543 («SYS_JOURNAL_2026, строки 2611 и 5781; урок У-45») |
| U-99 | CASE | AT_ADDRESS | AT_ADDRESS | «уроки У-75 и У-80 карты `projects/archivarius/TRIAGE.md`» (line 39); TRIAGE.md:91 («+2288 Б от другого контура» (2026-08-26)). Path now explicit |
| U-100 | CASE | AT_ADDRESS | AT_ADDRESS | TRIAGE.md:1544 («критерий «21 956 байт ± 2» остановил бы исправную правку при приёмке K3 … зона уменьшилась на 141 байт (2026-07-30)»); TRIAGE.md:96 (У-80 merged into У-75) |
| U-101 | CASE | AT_ADDRESS | AT_ADDRESS | «порция Р-22 той же карты» (line 39); TRIAGE.md:264 inside section «Порция Р-22» (:241): «У-75 (с У-80) \| 594–595 (2026-08-10), 808 (2026-08-25), 870 пункт 6в (2026-08-30)» |
| U-102 | CASE | WEAKENED | IN_TEXT | «уроки У-75 и У-80 карты `projects/archivarius/TRIAGE.md`, порция Р-22 той же карты» (line 39); section exists at TRIAGE.md:241 |
| U-49 | CASE | IN_TEXT | IN_TEXT | «запись Р-104 файла `projects/git-migration/LOG_ARCHIVE.md` и запись Р-107 журнала `projects/git-migration/LOG.md`» (line 34); address defect fixed (LOG_ARCHIVE.md:1152, LOG.md:15) |
| U-55 | CASE | IN_TEXT | IN_TEXT | «описание объекта — 5, последний 2026-10-16» (line 35); contradicting A5 pointer («Шесть объектов») removed |
| U-71 | CASE | IN_TEXT | IN_TEXT | «отсутствие — 4, последний датированный 2026-07-30» (line 36) |

### Missed-by-the-table items (round 1 list)

1. «датированный» — RESOLVED, IN_TEXT: «отсутствие — 4, последний датированный 2026-07-30» (line 36).
2. documents.items mechanism — RESOLVED, AT_ADDRESS: pointer «механизм записи карточки — кейс 1 файла `meta/CASES_wb-api-card-write.md`» (line 32); meta/CASES_wb-api-card-write.md:37 («Документ меняется только блоком documents.items»); also projects/deklaration-wb/LOG.md:163.
3. archive-recon attribution — RESOLVED: text now points to archive-recon Р-15 and Р-22 (line 32); confirmed projects/archive-recon/LOG.md:93/:101 and :175–176. The SERVER-attributing A1 pointer is gone.
4. «пойман до записи» — RESOLVED, IN_TEXT: «(последний случай пойман до записи)» (line 32); projects/archive-recon/LOG.md:163.
5. ISO numbering — RESOLVED, IN_TEXT: «(неделя по нумерации ISO)» (line 38); projects/wb-ue/LOG.md:361.
6. Per-rule reason sentences collapsed into one basis list — UNCHANGED by design: line 30 states «рассказы здесь не повторяются». All REASON units are IN_TEXT; every case narrative is now confirmed at its address. No knowledge lost, only moved.
7. Address defects — Р-104 FIXED (LOG_ARCHIVE.md, line 34); У-144 FIXED (TRIAGE.md, line 36). ONE REMAINING defect: «`projects/wb-ue/STATE.md` строка 159» (line 38) — the 496 figure is at STATE.md:162; line 159 is about 5 nmID sales. Inherited from the old text; fix the line number.

## 2. Diff R15_new_round1.md → R15_new.md

Changed lines: 3 (trigger), 8 («(файл)»), 14 («откатилось, потому что»), 17 («пишется и произносится в ответе»), 26 (specifics rule restored to general form), 28 (ИСТОРИЯ ДИАГНОЗА duty), 30→30–40 (basis list rewritten as bullets with primary addresses).
Removed by the revision: pointers to findings А1, А5, Б11 of meta/HARVEST_2026-10-18.md; pointer «уроки У-78 и У-144 журнала projects/archivarius/LOG.md»; «уроки У-75 и У-80» / «урок У-45» without path; «В задание исполнителю … исполнитель берёт».
Check: every unit that round 1 had AT_ADDRESS via А1/А5/Б11 or archivarius/LOG.md (U-35, U-37, U-39, U-40, U-56–U-59, U-72–U-75, U-85, U-86, U-90, U-91, U-99–U-101) is confirmed at the new primary address (table above). Every IN_TEXT unit of round 1 is still present verbatim or strengthened. Nothing that round 1 had IN_TEXT or AT_ADDRESS was lost or weakened by the revision. Only blemish: the U-85 line number (see item 7).

## 3. Added by the rewrite (status after revision)

1. Trigger widened to «о внешнем мире» — REVERTED, no longer an addition.
2. General LAW «Утверждение верно только для того чтения объекта, из которого оно взято» — unchanged (design choice).
3. General read-before-decision duty for all claim kinds — unchanged.
4. «память, пересказ или старая запись» classification; «молча стареет» — unchanged.
5. Column «Что чтением не считается» with explicit negatives — unchanged.
6. Executor-role framing of specifics — REVERTED.
7. New addresses — the А1/А5/Б11 pointers (and the «Шесть объектов» vs 5 contradiction) are gone. New addition instead: «механизм записи карточки — кейс 1 файла meta/CASES_wb-api-card-write.md» (address not in the old text; content verified at :35–40).
8. New case counts «слово Андрея — 1», «условие из прошлого — 2», «идентификатор — 1» — unchanged.
9. «Три уточнения закона для чисел» framing — unchanged.
10. New: «(рассказы здесь не повторяются)» — editorial statement that narratives live only at the addresses.

## Counts per verdict over all 112 units after round 2 (computed by script)

- IN_TEXT: 89
- AT_ADDRESS: 23
- WEAKENED: 0
- LOST: 0
- Total: 112
