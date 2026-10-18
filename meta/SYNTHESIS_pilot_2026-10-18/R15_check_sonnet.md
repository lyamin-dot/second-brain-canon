meta/SYNTHESIS_pilot_2026-10-18/R15_check_sonnet.md

# R15 loss check (Sonnet)

| id | class | verdict | evidence |
|---|---|---|---|
| U-01 | RULE | IN_TEXT | «Р15. Провенанс и верификация — единый стандарт» |
| U-02 | RULE | WEAKENED | Trigger widened from «утверждение о состоянии системы» to «о системе или о внешнем мире» (scope widened, not in old) |
| U-03 | RULE | IN_TEXT | «любая запись» |
| U-04 | RULE | IN_TEXT | «Каждое утверждение несёт метку происхождения» |
| U-05 | THRESHOLD | IN_TEXT | «ПРОЧИТАНО В ЭТОЙ СЕССИИ (объект), ПРОЧИТАНО ПОСРЕДНИКОМ … или ВСПОМНЕНО» |
| U-06 | RULE | IN_TEXT | «ПРОЧИТАНО В ЭТОЙ СЕССИИ (объект)» (file generalised to object) |
| U-07 | RULE | IN_TEXT | «ПРОЧИТАНО ПОСРЕДНИКОМ (кто и какой объект — Р21)» |
| U-08 | ADDRESS | IN_TEXT | «— Р21)» |
| U-09 | RULE | IN_TEXT | «Четвёртой метки нет» |
| U-10 | RULE | IN_TEXT | «уверенность происхождением не является» |
| U-11 | RULE | IN_TEXT | «Решение цитируется вместе со статусом» |
| U-12 | REASON | IN_TEXT | «отметка об отмене часто стоит в хвосте записи» |
| U-13 | RULE | WEAKENED | Old: concrete values come from the registry at moment of use as a general rule. New item 4 limits it to «В задание исполнителю … исполнитель берёт её из реестра»; general scope narrowed to task texts |
| U-14 | THRESHOLD | IN_TEXT | «конкретика (ID, пороги, версии)» |
| U-15 | RULE | IN_TEXT | «в задание пишутся правила поведения при неизвестном» |
| U-16 | RULE | IN_TEXT | «Перед пакетной операцией — манифест реальных объектов, полученных чтением в этой сессии» |
| U-17 | RULE | IN_TEXT | «Кто читал источник, тот и прав — независимо от роли в наряде и класса модели» |
| U-18 | RULE | IN_TEXT | «Расхождение факта с ожиданием — стоп и вопрос, не тихая правка» |
| U-19 | RULE | IN_TEXT | table row «Состояние…»: «способ проверки пишется рядом с утверждением»; ЗАКОН: «либо утверждение пишется словами Гипотеза» (word «только» gone, equivalent via ЗАКОН) |
| U-20 | THRESHOLD | IN_TEXT | «Состояние: «работает», «выключен», «опубликован», «внесено», «удалено»» |
| U-21 | THRESHOLD | IN_TEXT | «в `STATE.md`, INDEX, задачу, журнал» |
| U-22 | THRESHOLD | IN_TEXT | «номер исполнения, поле ответа инструмента или строку объекта» |
| U-23 | EXCEPTION | IN_TEXT | «либо утверждение пишется словами «Гипотеза (не проверена):»» (general, in ЗАКОН) |
| U-24 | THRESHOLD | IN_TEXT | «Гипотеза (не проверена):» |
| U-25 | CASE | IN_TEXT | «состояние — 2 за неделю (записи Р-39 и Р-53 …)»; wording about «работает по расписанию» itself dropped but count+address kept |
| U-26 | CASE | AT_ADDRESS | quoted «Р-39 и Р-53 журнала `projects/wb-ue/LOG.md`»; verified projects/wb-ue/LOG.md:202,272,274 |
| U-27 | RULE | IN_TEXT | row «Причина … в канон и в текст правила» + ПРОВЕРКА «каждое причинное объяснение … несут способ проверки или слово «Гипотеза»» |
| U-28 | THRESHOLD | WEAKENED | Forms list lost «откатилось, потому что»; only «X случилось потому, что Y», «не работает из-за Y» remain |
| U-29 | THRESHOLD | IN_TEXT | «пробу на объекте: запись, запрос или прогон, где меняется только предполагаемая причина и результат меняется вместе с ней» |
| U-30 | RULE | IN_TEXT | «совпадение по времени, правдоподобный механизм» (in column «Что чтением не считается») |
| U-31 | REASON | IN_TEXT | «записанное когда-то выглядит как факт, закрывает поиск и молча стареет — следующая сессия не ищет» |
| U-32 | RULE | WEAKENED | Only «Опровергнутая причина не стирается — core/R-06a.md, пункт 0.4.1». Lost: kept NEXT TO the correction, block name ИСТОРИЯ ДИАГНОЗА. Mechanism exists at core/R-06a.md:60 but rule text is thinned to a bare pointer |
| U-33 | ADDRESS | IN_TEXT | «`core/R-06a.md`, пункт 0.4.1»; verified core/R-06a.md:60 |
| U-34 | CASE | IN_TEXT | «причина — 4, последний 2026-10-17 (находка А1 …)» |
| U-35 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 (А1) names the case and 9–17 Oct; NOTE the documents.items mechanism is worded differently there («запись одними характеристиками не применяется вовсе») |
| U-36 | CASE | LOST | Evidence Р-11 / Р-20 of projects/deklaration-wb/LOG.md (LOG:87,161) not named in new text nor in А1 |
| U-37 | CASE | AT_ADDRESS | meta/HARVEST_2026-10-18.md:69 (А1): «перезапись стёрла ОКПД 2 … на деле не передавалось поле needKiz» |
| U-38 | CASE | LOST | Evidence Р-46 deklaration-ozon/LOG.md and Р-21 deklaration-wb/LOG.md not named anywhere in new text or А1 |
| U-39 | CASE | AT_ADDRESS | HARVEST А1 (:69): «язык распознавания зашит в код … на деле поле lang работало»; record ids Р-15/Р-22 and date 2026-09-27 dropped |
| U-40 | CASE | AT_ADDRESS | HARVEST А1 (:69): «немецкий язык не работает … мешала параллельная нагрузка»; Т-4 id and «caught before write» dropped |
| U-41 | RULE | IN_TEXT | «Слово Андрея «сделал», «удалил», «внёс» — ВСПОМНЕНО» |
| U-42 | REASON | IN_TEXT | «Андрей помнит действие, а объект сессия не видела» |
| U-43 | RULE | IN_TEXT | «задача по такому слову закрывается только после чтения объекта»; «до того в ответе стоит…» (the explicit «до чтения она открыта» is dropped, implied) |
| U-44 | THRESHOLD | IN_TEXT | «по словам Андрея, объект не прочитан» |
| U-45 | CASE | AT_ADDRESS | new text: «слово Андрея — 1 (Р-126 журнала `projects/git-migration/LOG.md`)»; verified projects/git-migration/LOG.md:159 (деактивировал / active:true) |
| U-46 | RULE | IN_TEXT | row «Условие из прошлого … перед исполнением и перед вопросом Андрею / объект и оглавление журнала проекта» |
| U-47 | THRESHOLD | IN_TEXT | «задание, старая запись, память чата или Андрея («тот же ключ, что у git-write», «ждёт решения владельца»)» |
| U-48 | REASON | IN_TEXT | «условие могло устареть, вопрос — быть уже решённым» |
| U-49 | CASE | IN_TEXT | «условие из прошлого — 2 (Р-104 и Р-107 того же журнала)» |
| U-50 | RULE | IN_TEXT | «обещание в шапке документа … перед ссылкой на объект его ищут» |
| U-51 | RULE | IN_TEXT | row «Описание объекта …» exists as a sibling row |
| U-52 | RULE | IN_TEXT | row «Описание объекта: описание воркфлоу в n8n, паспорт, строка реестра, пометка в карте, строка Skill»; «Что чтением не считается: само описание» |
| U-53 | RULE | IN_TEXT | «перед решением выключить, считать тестовым, считать подключённым, считать, что у листа нет читателя / определение воркфлоу, сам лист, исполнение» |
| U-54 | THRESHOLD | IN_TEXT | «определение воркфлоу, сам лист, исполнение» |
| U-55 | CASE | IN_TEXT | «описание объекта — 5, последний 2026-10-16» |
| U-56 | CASE | AT_ADDRESS | HARVEST А5 (:77): «описание воркфлоу утверждает подключённую ветку, которой нет»; labs/sys/t-draft-trigger-divergence.md exists but is not named in new text; workflow ID MPzPrtsnPtf0sVQo dropped |
| U-57 | CASE | AT_ADDRESS | HARVEST А5 (:77): «паспорт Health Monitor — «10 воркфлоу» при шести»; file t-monitoring-minor.md not named |
| U-58 | CASE | AT_ADDRESS | HARVEST А5 (:77): «Skill называет Ozon RAW Accrual Sync тестовым, а он кормит боевой лист»; ложный вывод про выключение там тоже есть; file path not named |
| U-59 | CASE | AT_ADDRESS | HARVEST А5 (:77): «описание канарейки — «битый идентификатор» при рабочем»; t-failure-visibility.md not named |
| U-60 | RULE | IN_TEXT | row «Отсутствие … / поиск в собственном носителе объекта (ниже)»; word «произносится» not explicit |
| U-61 | THRESHOLD | IN_TEXT | ««файла нет», «воркфлоу не существует», «журнала нет», «решения нет», «в Skill этого нет»» |
| U-62 | RULE | IN_TEXT | «в ответе перечислено, где искали» |
| U-63 | THRESHOLD | IN_TEXT | «воркфлоу — search_workflows или get_workflow_details на инстансе» |
| U-64 | THRESHOLD | IN_TEXT | «живой Skill в `/mnt/skills/`» |
| U-65 | THRESHOLD | IN_TEXT | «в среде с клоном `git ls-files` и `grep`, без клона — Git Read Lines с pattern» |
| U-66 | THRESHOLD | IN_TEXT | «документ Google Drive (поиск Drive)» |
| U-67 | THRESHOLD | IN_TEXT | «оглавление журнала своего и соседнего проекта по словам темы, `STATE.md` и `PLAN.md`» |
| U-68 | ADDRESS | IN_TEXT | «(`second-brain-git` 7.6)»; 7.6 exists in skills/second-brain-git/SKILL.md |
| U-69 | RULE | IN_TEXT | «отсутствие в реестре, в CORE или в памяти сессии — это дефект регистрации» |
| U-70 | ADDRESS | IN_TEXT | «Поиск документа по просьбе Андрея — Р9» |
| U-71 | CASE | IN_TEXT | «отсутствие — 4, последний 2026-07-30 (уроки У-78 и У-144 …)» |
| U-72 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 (У-78): «журнал объявлен несуществующим при ID в мастер-промпте» |
| U-73 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301: «воркфлоу M5dqSv2yiklnDXoP объявлен «выдуманным», и … отменена верная правка CORE» |
| U-74 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301: «INCIDENT_LOG.md не существует — существовал в смонтированном Skill» |
| U-75 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:301 «У-78 (113–117, 120–124, 211–215)» (JOURNAL_INCIDENTS line ranges; new text names У-78 only) |
| U-76 | CASE | LOST | Case (WB_REVIEWS_INDEX 1722, «решения нет» при решении в индексе) is in projects/archivarius/TRIAGE.md:165, not in LOG.md which new text names; LOG.md:541-544 mention У-144 only as a map row. Case absent at named address |
| U-77 | CASE | IN_TEXT | «уроки У-78 и У-144 журнала `projects/archivarius/LOG.md`» |
| U-78 | RULE | IN_TEXT | row «Идентификатор, число или дата…/ выдача объекта или поиска этой сессии — копированием / память, перепечатка из другого текста, счёт в уме» |
| U-79 | THRESHOLD | IN_TEXT | «ID, sha, номер исполнения, порог, счёт, дата» |
| U-80 | CASE | AT_ADDRESS | new: «идентификатор — 1 (зонд Z-10 файла `projects/n8n-map/PLAN.md`)»; verified PLAN.md:234 (44 chars) and :28 (41 chars in registry/documents.md) |
| U-81 | RULE | IN_TEXT | «Число в критерии приёмки, в контракте работы и в ожидаемом результате проверки — тоже число в канон» |
| U-82 | RULE | IN_TEXT | «его выводят чтением объекта до того, как критерий записан» |
| U-83 | RULE | IN_TEXT | «рядом называют чтение, из которого оно взято» |
| U-84 | CASE | IN_TEXT | «число в критерии — 2, последний 2026-10-15» |
| U-85 | CASE | AT_ADDRESS | HARVEST Б11 (:115): «536 строк» при 496; PLAN.md line 67 / STATE.md line 159 addresses dropped |
| U-86 | CASE | AT_ADDRESS | HARVEST Б11 (:115): «41 неделя» при 40; ISO wording and Р-66 point 2 dropped |
| U-87 | RULE | IN_TEXT | «а не из памяти модели» |
| U-88 | THRESHOLD | IN_TEXT | «в журнале, в имени файла, в поле «создан»» |
| U-89 | THRESHOLD | IN_TEXT | «из инструмента текущего времени, из даты, которую харнесс сообщил в контексте сессии, или из ответа инструмента (время старта исполнения n8n, createdTime ответа Drive)» |
| U-90 | CASE | AT_ADDRESS | new: «дата — 2, последний 2026-07-30 (урок У-45)»; projects/archivarius/LOG.md:233 holds 3 days / 1 day / file rename |
| U-91 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:233 «У-45 (2611, 5781–5782)»; SYS_JOURNAL_2026 line numbers not in new text |
| U-92 | REASON | IN_TEXT | «Утверждение верно только для того чтения объекта, из которого оно взято»; «верно только для того чтения…» in item 3 |
| U-93 | RULE | IN_TEXT | «пишется вместе с отметкой версии чтения» |
| U-94 | THRESHOLD | IN_TEXT | «blob sha для файла репозитория, checkSum ответа gdocs-read для документа Google» |
| U-95 | RULE | IN_TEXT | «Критерий приёмки по такой величине — соотношение, проверяемое на свежем чтении в момент приёмки» |
| U-96 | THRESHOLD | IN_TEXT | «(«зона не выросла», «добавилась ровно одна запись»)» (wording slightly changed) |
| U-97 | RULE | IN_TEXT | «абсолютное число — только база для сравнения» |
| U-98 | CASE | IN_TEXT | «число живого файла — 5, последний 2026-08-30» |
| U-99 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:279 (У-75): «+2288 Б от другого контура», 2026-08-26; named via «уроки У-75 и У-80» |
| U-100 | CASE | AT_ADDRESS | projects/archivarius/LOG.md:303 (У-80): «21956 байт ± 2 … зона ужалась на 141 байт» |
| U-101 | CASE | LOST | Repeat dates 2026-08-10/08-25/08-30 live only in projects/archivarius/TRIAGE.md:264, which new text no longer names; not in LOG У-75/У-80 lines |
| U-102 | CASE | WEAKENED | Lessons У-75 и У-80 kept, but the TRIAGE.md порция Р-22 address is dropped (and the repeat-count evidence with it) |
| U-103 | RULE | IN_TEXT | «Запись верифицируется только независимым перечитыванием» |
| U-104 | THRESHOLD | IN_TEXT | «Docs — gdocs-read, счёт вхождений якоря или совпадение текста» |
| U-105 | ADDRESS | IN_TEXT | «`second-brain-git` 8.1»; exists skills/second-brain-git/references/write.md:58 |
| U-106 | THRESHOLD | IN_TEXT | «в среде с клоном `git fetch` и `git hash-object`» |
| U-107 | THRESHOLD | IN_TEXT | «без клона — один вызов Git Read Lines с pattern по первой строке записанного» |
| U-108 | CHECK | IN_TEXT | «blob sha записанного равен sha намеренного» |
| U-109 | RULE | IN_TEXT | «`success: true`, `occurrencesChanged`, номер исполнения, ответ инструмента — сигналы, не доказательства» |
| U-110 | RULE | IN_TEXT | «один стандарт для обоих носителей» |
| U-111 | CHECK | IN_TEXT | «В отчёте о записи названы файл, способ обратного чтения и совпавшая величина» |
| U-112 | CHECK | IN_TEXT | «несут способ проверки или слово «Гипотеза»» |

## Missed by the table

- M1. Old: the three-in-a-day precedent is the reason of the absence rule; new text keeps only a count («4, последний 2026-07-30») and lesson ids. The concrete failure modes (log declared nonexistent despite its ID in the master prompt; a correct CORE edit reverted on a false refutation; INCIDENT_LOG.md declared absent while mounted in a Skill) exist only in projects/archivarius/LOG.md:301, not in R15 (AT_ADDRESS for units, but the rule loses its illustrations of «ID в мастер-промпте» and «смонтированный Skill» as search layers).
- M2. Old: the «Основание» sentences state the mechanism of each failure (e.g. WB write without documents.items does not change a document; needKiz omission resets the КИЗ mark; lang field accepted). New text removes all mechanisms from R15; А1 in the HARVEST file keeps them only in shortened form (documents.items detail is replaced by «запись одними характеристиками»).
- M3. Old: «пишется и произносится» for absence claims (applies to spoken answers too). New: absence row does not say spoken; only the generic trigger «утверждение» covers it.
- M4. Old: «Опровергнутая причина … сохраняется рядом с исправлением блоком ИСТОРИЯ ДИАГНОЗА» — new gives only a pointer to R-06a 0.4.1 (see U-32).
- M5. Old: the hypothesis-label rule for causes says the label is used «до тех пор, пока причину не подтвердила проба»; new has no explicit sentence that the label is removed only after a probe (implied by row «Причина»).
- M6. Old: «Задача … до чтения она открыта» — explicit status «открыта» dropped (U-43 note).
- M7. Old: evidence for the numeric cases pinned to exact lines (PLAN.md line 67 vs STATE.md line 159; Р-66 point 2). New cites only HARVEST Б11, which has the numbers but not these lines.
- M8. New item numbering/«ДЕЙСТВИЕ» ordering: old said the registry-at-use rule right after provenance labels; new moved it into the executor-task paragraph (U-13).

## Added by the rewrite

- N1. Trigger widened to «утверждение о системе или о внешнем мире» (old: only о состоянии системы).
- N2. New ЗАКОН paragraph: «Всё, чего сессия не прочитала в самом объекте, — память, пересказ или старая запись, и решение на этом не принимается: объект читается до решения». This is a universal prohibition not in the old text (old applied reading-before-decision to specific cases). It also conflicts internally with the label ПРОЧИТАНО ПОСРЕДНИКОМ, which the same section allows as a valid provenance.
- N3. «Утверждение верно только для того чтения объекта, из которого оно взято» is generalised from the old rule that was stated only for numbers about live files.
- N4. «молча стареет» as a stated reason for all recorded claims (old said only «закрывает поиск» for causal claims).
- N5. Column «Что чтением не считается» entries «прежняя запись о состоянии» and «само условие» are new formulations (derived, not in old).
- N6. Counts in the closing «Основание» for «слово Андрея — 1», «условие из прошлого — 2», «идентификатор — 1» are the number of precedents in old, rendered as case counts; old stated no counts for these.
- N7. «описание объекта — 5 … (находка А5)»: the cited HARVEST А5 itself says «Шесть объектов за окно» (meta/HARVEST_2026-10-18.md:77), so the pointer does not match the count 5.
- N8. Item 6 now sits as a separate numbered step «Расхождение … — стоп и вопрос» together with the refuted-cause rule; grouping is new but content is old.
- N9. Item 1 generalises «(файл)» to «(объект)» for the label ПРОЧИТАНО В ЭТОЙ СЕССИИ.

## Counts per verdict (script, from table rows)

- IN_TEXT: 82
- AT_ADDRESS: 21
- WEAKENED: 5
- LOST: 4
- total: 112
- AT_ADDRESS used on non-CASE/ADDRESS class (inadmissible): []
