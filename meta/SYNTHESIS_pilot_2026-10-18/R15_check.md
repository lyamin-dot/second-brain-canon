meta/SYNTHESIS_pilot_2026-10-18/R15_check.md

# Р15 — check of the rewrite against the unit table

Sources: R15_old.md, R15_new.md, R15_units.md (same folder). Addresses checked in /home/claude/second-brain-canon (read-only).

| id | class | verdict | evidence |
|---|---|---|---|
| U-01 | RULE | IN_TEXT | «Р15. Провенанс и верификация — единый стандарт» (line 1) |
| U-02 | RULE | WEAKENED | Trigger widened: old «утверждение о состоянии системы» → new «Любое утверждение о системе или о внешнем мире» (scope widened beyond state, beyond the system) |
| U-03 | RULE | IN_TEXT | «любая запись» (line 3) |
| U-04 | RULE | IN_TEXT | «Каждое утверждение несёт метку происхождения» (line 8) |
| U-05 | THRESHOLD | IN_TEXT | «ПРОЧИТАНО В ЭТОЙ СЕССИИ (объект), ПРОЧИТАНО ПОСРЕДНИКОМ (…) или ВСПОМНЕНО» (line 8) |
| U-06 | RULE | WEAKENED | Label annotation changed: old «ПРОЧИТАНО В ЭТОЙ СЕССИИ (файл)» → new «(объект)»; the requirement to name the file is widened/blurred to any object |
| U-07 | RULE | IN_TEXT | «ПРОЧИТАНО ПОСРЕДНИКОМ (кто и какой объект — Р21)» (line 8) |
| U-08 | ADDRESS | IN_TEXT | «(кто и какой объект — Р21)» (line 8) |
| U-09 | RULE | IN_TEXT | «Четвёртой метки нет» (line 8) |
| U-10 | RULE | IN_TEXT | «уверенность происхождением не является» (line 8) |
| U-11 | RULE | IN_TEXT | «Решение цитируется вместе со статусом» (line 8) |
| U-12 | REASON | IN_TEXT | «отметка об отмене часто стоит в хвосте записи» (line 8) |
| U-13 | RULE | WEAKENED | Old is general: anyone takes ID/thresholds/versions from the registry at time of use, not from task text. New (item 4) binds only «исполнитель»: «исполнитель берёт её из реестра в момент использования» — scope narrowed to the executor role |
| U-14 | THRESHOLD | IN_TEXT | «конкретика (ID, пороги, версии) не пишется» (line 26) |
| U-15 | RULE | IN_TEXT | «в задание пишутся правила поведения при неизвестном» (line 26) |
| U-16 | RULE | IN_TEXT | «Перед пакетной операцией — манифест реальных объектов, полученных чтением» (line 26) |
| U-17 | RULE | IN_TEXT | «Кто читал источник, тот и прав — независимо от роли в наряде и класса модели» (line 8) |
| U-18 | RULE | IN_TEXT | «Расхождение факта с ожиданием — стоп и вопрос, не тихая правка» (line 28) |
| U-19 | RULE | IN_TEXT | «способ проверки пишется рядом с утверждением» (table row «Состояние», line 13) |
| U-20 | THRESHOLD | IN_TEXT | «Состояние: «работает», «выключен», «опубликован», «внесено», «удалено»» (line 13) |
| U-21 | THRESHOLD | IN_TEXT | «в `STATE.md`, INDEX, задачу, журнал» (line 13) |
| U-22 | THRESHOLD | IN_TEXT | «номер исполнения, поле ответа инструмента или строку объекта» (line 13) |
| U-23 | EXCEPTION | IN_TEXT | «либо утверждение пишется словами «Гипотеза (не проверена):»» (line 5) |
| U-24 | THRESHOLD | IN_TEXT | ««Гипотеза (не проверена):»» (line 5) |
| U-25 | CASE | AT_ADDRESS | projects/wb-ue/LOG.md:274 (Р-53 «почему»: «запись не пережила сверки с живым воркфлоу дважды за неделю (Monitor Reader «работает по расписанию» — Р-39 …)») |
| U-26 | CASE | IN_TEXT | «состояние — 2 за неделю (записи Р-39 и Р-53 журнала `projects/wb-ue/LOG.md`)» (line 30) |
| U-27 | RULE | IN_TEXT | Row «Причина … — в канон и в текст правила \| пробу на объекте» (line 14) + law «либо … «Гипотеза (не проверена):»» (line 5) |
| U-28 | THRESHOLD | WEAKENED | Third form «откатилось, потому что» dropped; new lists only «X случилось потому, что Y», «не работает из-за Y» (line 14) |
| U-29 | THRESHOLD | IN_TEXT | «где меняется только предполагаемая причина и результат меняется вместе с ней» (line 14) |
| U-30 | RULE | IN_TEXT | «совпадение по времени, правдоподобный механизм» in column «не считается» (line 14) |
| U-31 | REASON | IN_TEXT | «закрывает поиск и молча стареет — следующая сессия не ищет того, что «уже известно»» (line 5, generalized, same mechanism) |
| U-32 | RULE | WEAKENED | Only the prohibition kept: «Опровергнутая причина не стирается — core/R-06a.md, пункт 0.4.1» (line 28). The positive duty «сохраняется рядом с исправлением блоком ИСТОРИЯ ДИАГНОЗА» is gone from the text (exists only at core/R-06a.md:60); a RULE must be IN_TEXT |
| U-33 | ADDRESS | IN_TEXT | «`core/R-06a.md`, пункт 0.4.1» (line 28); confirmed core/R-06a.md:60 |
| U-34 | CASE | IN_TEXT | «причина — 4, последний 2026-10-17» (line 30) |
| U-35 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 (finding A1: «Wildberries применяет правки … с задержкой в часы» … «с 9 по 17 октября, на деле запись одними характеристиками не применяется вовсе»). Note: «documents.items» not named there |
| U-36 | CASE | LOST | Proof «пункт 5 записи Р-11 отменён записью Р-20 журнала projects/deklaration-wb/LOG.md» absent from new text; finding A1 (HARVEST:69) gives no record ids |
| U-37 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 («перезапись стёрла ОКПД 2, и поэтому слетела отметка КИЗ» … «не передавалось поле needKiz») |
| U-38 | CASE | LOST | Proof «Р-46 журнала projects/deklaration-ozon/LOG.md, Р-21 журнала projects/deklaration-wb/LOG.md» absent; A1 names only project names |
| U-39 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 («язык распознавания зашит в код» (SERVER — на деле поле lang работало)). Partial: A1 attributes it to SERVER, not archive-recon; Р-15 / 2026-09-27 / Р-22 ids absent |
| U-40 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 («немецкий язык не работает» (archive-recon — на деле мешала параллельная нагрузка)). Partial: «пойман до записи» and Т-4 absent |
| U-41 | RULE | IN_TEXT | «Слово Андрея «сделал», «удалил», «внёс» — ВСПОМНЕНО» (line 8) |
| U-42 | REASON | IN_TEXT | «Андрей помнит действие, а объект сессия не видела» (line 8) |
| U-43 | RULE | IN_TEXT | «задача по такому слову закрывается только после чтения объекта» (line 8) |
| U-44 | THRESHOLD | IN_TEXT | ««по словам Андрея, объект не прочитан»» (line 8) |
| U-45 | CASE | AT_ADDRESS | projects/git-migration/LOG.md:160 (Р-126: «Андрей сообщил в чате, что деактивировал его; чтение search_workflows … показало active:true») |
| U-46 | RULE | IN_TEXT | «— перед исполнением и перед вопросом Андрею \| объект и оглавление журнала проекта» (line 16) |
| U-47 | THRESHOLD | IN_TEXT | «задание, старая запись, память чата или Андрея («тот же ключ, что у git-write», …)» (line 16) |
| U-48 | REASON | IN_TEXT | «условие могло устареть, вопрос — быть уже решённым» (line 16) |
| U-49 | CASE | IN_TEXT | «условие из прошлого — 2 (Р-104 и Р-107 того же журнала)» (line 30). Note: Р-104 is actually in projects/git-migration/LOG_ARCHIVE.md:1152, not LOG.md (defect inherited from old text) |
| U-50 | RULE | IN_TEXT | «обещание в шапке документа … \| … перед ссылкой на объект его ищут \| само условие» (line 16) |
| U-51 | RULE | IN_TEXT | Separate row «Описание объекта» (line 15) |
| U-52 | RULE | IN_TEXT | «Описание объекта: описание воркфлоу в n8n, паспорт, строка реестра, пометка в карте, строка Skill … \| само описание» (line 15) |
| U-53 | RULE | IN_TEXT | «перед решением выключить, считать тестовым, считать подключённым, считать, что у листа нет читателя» (line 15) |
| U-54 | THRESHOLD | IN_TEXT | «определение воркфлоу, сам лист, исполнение» (line 15) |
| U-55 | CASE | IN_TEXT | «описание объекта — 5, последний 2026-10-16» (line 30). Note: the cited finding A5 says «Шесть объектов» |
| U-56 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:77 (A5: «описание воркфлоу утверждает подключённую ветку, которой нет»). Workflow id MPzPrtsnPtf0sVQo and labs/sys/t-draft-trigger-divergence.md not named there |
| U-57 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:77 («паспорт Health Monitor — «10 воркфлоу» при шести») |
| U-58 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:77 («Skill называет Ozon RAW Accrual Sync тестовым, а он кормит боевой лист; … вывод … оказался ложным») |
| U-59 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:77 («описание канарейки — «битый идентификатор» при рабочем») |
| U-60 | RULE | WEAKENED | Old: absence claim «пишется и произносится» only after search. New row sits under column «Что прочитать до решения или до записи в канон» (line 11/17): saying it in a reply is no longer explicitly covered; only «в ответе перечислено, где искали» hints at replies |
| U-61 | THRESHOLD | IN_TEXT | ««файла нет», «воркфлоу не существует», «журнала нет», «решения нет», «в Skill этого нет»» (line 17) |
| U-62 | RULE | IN_TEXT | «в ответе перечислено, где искали» (line 17) |
| U-63 | THRESHOLD | IN_TEXT | «воркфлоу — search_workflows или get_workflow_details на инстансе» (line 20) |
| U-64 | THRESHOLD | IN_TEXT | «файл — названный слой: живой Skill в `/mnt/skills/`» (line 20) |
| U-65 | THRESHOLD | IN_TEXT | «в среде с клоном `git ls-files` и `grep`, без клона — Git Read Lines с pattern» (line 20) |
| U-66 | THRESHOLD | IN_TEXT | «документ Google Drive (поиск Drive)» (line 20) |
| U-67 | THRESHOLD | IN_TEXT | «оглавление журнала своего и соседнего проекта по словам темы, `STATE.md` и `PLAN.md`» (line 20) |
| U-68 | ADDRESS | IN_TEXT | «(`second-brain-git` 7.6)» (line 20) |
| U-69 | RULE | IN_TEXT | «отсутствие в реестре, в CORE или в памяти сессии — это дефект регистрации» (line 17) |
| U-70 | ADDRESS | IN_TEXT | «Поиск документа по просьбе Андрея — Р9» (line 20) |
| U-71 | CASE | IN_TEXT | «отсутствие — 4, последний 2026-07-30» (line 30) |
| U-72 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 (У-78: «журнал объявлен несуществующим при ID в мастер-промпте») |
| U-73 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 («воркфлоу M5dqSv2yiklnDXoP объявлен «выдуманным», и на этом ложном опровержении отменена верная правка CORE») |
| U-74 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 («INCIDENT_LOG.md не существует» — существовал в смонтированном Skill) |
| U-75 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 («У-78 (113–117, 120–124, 211–215)») within record Р-14 (JOURNAL_INCIDENTS corpus, line 293) |
| U-76 | CASE | LOST | New text points to «урок У-144 журнала projects/archivarius/LOG.md», but LOG.md holds no body of У-144 (only mentions at 541/544, no «решения нет»/WB_REVIEWS_INDEX 1722). The case lives in projects/archivarius/TRIAGE.md:165, which the new text does not name |
| U-77 | CASE | IN_TEXT | «(уроки У-78 и У-144 журнала `projects/archivarius/LOG.md`)» (line 30) |
| U-78 | RULE | IN_TEXT | «выдача объекта или поиска этой сессии — копированием \| память, перепечатка из другого текста» (line 18) |
| U-79 | THRESHOLD | IN_TEXT | «ID, sha, номер исполнения, порог, счёт, дата» (line 18) |
| U-80 | CASE | AT_ADDRESS | projects/n8n-map/PLAN.md:28 and :234 (Z-10: registry/documents.md ID 41 chars vs 44 in the workflow) |
| U-81 | RULE | IN_TEXT | «Число в критерии приёмки, в контракте работы и в ожидаемом результате проверки — тоже число в канон» (line 23) |
| U-82 | RULE | IN_TEXT | «его выводят чтением объекта до того, как критерий записан» (line 23) + «счёт в уме» not reading (line 18) |
| U-83 | RULE | IN_TEXT | «рядом называют чтение, из которого оно взято» (line 23) |
| U-84 | CASE | IN_TEXT | «число в критерии — 2, последний 2026-10-15» (line 30) |
| U-85 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:115 (Б11: «wb-ue: «536 строк» при 496»); original PLAN.md:67 also contains «536 строк» |
| U-86 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:115 («41 неделя» при 40). «по нумерации ISO» and Р-66 pointer absent |
| U-87 | RULE | IN_TEXT | «а не из памяти модели» (line 25) |
| U-88 | THRESHOLD | IN_TEXT | «Дата записи — в журнале, в имени файла, в поле «создан»» (line 25) |
| U-89 | THRESHOLD | IN_TEXT | «из инструмента текущего времени, из даты, которую харнесс сообщил …» (line 25) |
| U-90 | CASE | AT_ADDRESS | Count «дата — 2, последний 2026-07-30 (урок У-45)» in text (line 30); details at projects/archivarius/LOG.md:233 («ошибки на 3 дня (2026-07-15) и на 1 день с исправлением имени файла (2026-07-30)») Caveat: new text names «урок У-45»/«уроки У-75 и У-80» without a file path (path only implied by the preceding «журнала projects/archivarius/LOG.md»). |
| U-91 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:233 («У-45 (2611, 5781–5782)») inside record Р-12 on SYS_JOURNAL_2026 (line 220) Caveat: new text names «урок У-45»/«уроки У-75 и У-80» without a file path (path only implied by the preceding «журнала projects/archivarius/LOG.md»). |
| U-92 | REASON | IN_TEXT | «Утверждение верно только для того чтения объекта, из которого оно взято» (line 5, generalized) |
| U-93 | RULE | IN_TEXT | «пишется вместе с отметкой версии чтения» (line 24) |
| U-94 | THRESHOLD | IN_TEXT | «blob sha для файла репозитория, checkSum ответа gdocs-read для документа Google» (line 24) |
| U-95 | RULE | IN_TEXT | «соотношение, проверяемое на свежем чтении в момент приёмки» (line 24) |
| U-96 | THRESHOLD | IN_TEXT | «(«зона не выросла», «добавилась ровно одна запись»)» (line 24) |
| U-97 | RULE | IN_TEXT | «абсолютное число — только база для сравнения» (line 24) |
| U-98 | CASE | IN_TEXT | «число живого файла — 5, последний 2026-08-30» (line 30) |
| U-99 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:279 (У-75: «замер Зоны А протух за одну сессию, +2288 Б от другого контура», 2026-08-26) Caveat: new text names «урок У-45»/«уроки У-75 и У-80» without a file path (path only implied by the preceding «журнала projects/archivarius/LOG.md»). |
| U-100 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:303 (У-80: «критерий «21956 байт ± 2» остановил бы исправную правку … зона ужалась на 141 байт») Caveat: new text names «урок У-45»/«уроки У-75 и У-80» without a file path (path only implied by the preceding «журнала projects/archivarius/LOG.md»). |
| U-101 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:419 (Р-22: «У-75 — 594–595 (2026-08-10), 808 (2026-08-25), 870 пункт 6в (2026-08-30)») Caveat: new text names «урок У-45»/«уроки У-75 и У-80» without a file path (path only implied by the preceding «журнала projects/archivarius/LOG.md»). |
| U-102 | CASE | WEAKENED | Pointer «порция Р-22 файла projects/archivarius/TRIAGE.md» dropped; new keeps only «(уроки У-75 и У-80)» without repeating the journal path |
| U-103 | RULE | IN_TEXT | «Запись верифицируется только независимым перечитыванием» (line 27) |
| U-104 | THRESHOLD | IN_TEXT | «Docs — gdocs-read, счёт вхождений якоря или совпадение текста» (line 27) |
| U-105 | ADDRESS | IN_TEXT | «repo — `second-brain-git` 8.1» (line 27) |
| U-106 | THRESHOLD | IN_TEXT | «в среде с клоном `git fetch` и `git hash-object`» (line 27) |
| U-107 | THRESHOLD | IN_TEXT | «без клона — один вызов Git Read Lines с pattern по первой строке записанного» (line 27) |
| U-108 | CHECK | IN_TEXT | «blob sha записанного равен sha намеренного» (line 27) |
| U-109 | RULE | IN_TEXT | «`success: true`, `occurrencesChanged`, номер исполнения, ответ инструмента — сигналы» (line 27) |
| U-110 | RULE | IN_TEXT | «один стандарт для обоих носителей» (line 27) |
| U-111 | CHECK | IN_TEXT | «В отчёте о записи названы файл, способ обратного чтения и совпавшая величина» (line 32) |
| U-112 | CHECK | IN_TEXT | «каждое причинное объяснение в записанном тексте несут способ проверки или слово «Гипотеза»» (line 32) |

## Missed by the table

1. Old line 13: the fourth absence case is undated («последний датированный 2026-07-30»); new line 30 says «последний 2026-07-30», dropping «датированный» — implies all four cases are dated. Minor distortion of the basis.
2. Old line 10: the precise WB API mechanism «запись без блока documents.items созданный документ не меняет» (operational knowledge, not just a case label). New text has no address with this wording; finding A1 (meta/HARVEST_2026-10-18.md:69) states a different mechanism («запись одними характеристиками не применяется вовсе»). Knowledge about documents.items lost from this section.
3. Old line 10: the archive-recon case «язык распознавания зашит в вызов» is attributed to archive-recon (Р-15, 2026-09-27, refuted by Р-22). The new address A1 attributes it to SERVER — the rewrite points to a source that contradicts the old attribution.
4. Old line 10: «вывод пойман до записи» (the German-language case was caught before being written) — the nuance that this case was a near-miss, not a written false cause, is absent from new text and from A1.
5. Old line 14: «41 неделя» was wrong «по нумерации ISO» — the ISO week-numbering mechanism of the error is absent from new text and from Б11 (meta/HARVEST_2026-10-18.md:115).
6. Old line 9/12/13/14/16: per-rule «Основание» sat next to each rule; the new text collapses them into one line at the end (line 30). Each rule lost its adjacent justification sentence (e.g. «записи «работает по расписанию» дважды за неделю не пережили сверки с живым воркфлоу»); only counts and pointers remain.
7. Address defect inherited, not fixed: Р-104 lives in projects/git-migration/LOG_ARCHIVE.md:1152, not in projects/git-migration/LOG.md as both texts say. Similarly урок У-144 has no body in projects/archivarius/LOG.md; it lives in projects/archivarius/TRIAGE.md:165.

## Added by the rewrite

1. Trigger widened: «Любое утверждение о системе или о внешнем мире» (old: «о состоянии системы»).
2. New «ЗАКОН»: «Утверждение верно только для того чтения объекта, из которого оно взято» — in the old text this held only for numbers about live files written by others (old line 16); now generalized to every claim.
3. «решение на этом не принимается: объект читается до решения» — a general read-before-decision duty for all claim kinds; old had it only for object descriptions and earlier-written conditions.
4. «Всё, чего сессия не прочитала в самом объекте, — память, пересказ или старая запись» — new classification; and reason «молча стареет».
5. Column «Что чтением не считается»: «прежняя запись о состоянии» (state row), «само условие», «само описание» — explicit negatives not stated in old text (derivable, but new wording).
6. Item 4 reframes specifics-from-registry as a duty of «исполнитель» (role framing absent in old).
7. New addresses: findings А1, А5, Б11 of meta/HARVEST_2026-10-18.md. A5 says «Шесть объектов», contradicting the new text's own count «описание объекта — 5».
8. New counts not stated in old: «слово Андрея — 1», «условие из прошлого — 2», «идентификатор — 1» (old said «Прецедент» / cited two records without a count).
9. Heading «Три уточнения закона для чисел» — new structuring claim that these are refinements of the general law.

## Counts per verdict (computed by script from the table rows)

- IN_TEXT: 80
- AT_ADDRESS: 22
- WEAKENED: 7
- LOST: 3
- Total: 112
