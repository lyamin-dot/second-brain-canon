# avtopilot old text decomposition

| id | lines | class | quote | paraphrase |
|---|---|---|---|---|
| U01 | 2 | THRESHOLD | name: avtopilot | Skill name field is avtopilot |
| U02 | 3 | RULE | Автопилот — Андрей один раз согласует контракт | Andrei approves the contract once |
| U03 | 3 | RULE | дальше сессия ведёт работу до итогового отчёта без него | after that the session runs the work to the final report without him |
| U04 | 3 | RULE | раздаёт тяжёлое чтение субагентам | hands heavy reading to subagents |
| U05 | 3 | RULE | пишет в канон сама | session writes to canon itself |
| U06 | 3 | RULE | сдаёт результат независимой приёмке | result goes to independent acceptance |
| U07 | 3 | THRESHOLD | автопилот, делай сам до конца, автономно, без меня | trigger words list |
| U08 | 3 | THRESHOLD | «Действуй!» в ответ на контракт запуска | trigger: "Действуй!" in reply to launch contract |
| U09 | 3 | EXCEPTION | Не читать для быстрой итерации, где Андрей и так отвечает на каждом шаге | do not read for quick iteration where Andrei answers every step |
| U10 | 3 | EXCEPTION | и для одиночной операции | do not read for a single operation |
| U11 | 6 | ADDRESS | # АВТОПИЛОТ | title heading |
| U12 | 8 | THRESHOLD | Версия 1.0. | version 1.0 |
| U13 | 8 | CASE | Создан 2026-10-13 сессией SYS (Аргус) по просьбе Андрея | created 2026-10-13 by SYS session at Andrei request |
| U14 | 8 | CASE | пилот того же дня — задача `labs/sys/t-audit-0723-unverified.md` | pilot same day: task t-audit-0723-unverified |
| U15 | 8 | ADDRESS | Решение и отвергнутые варианты — `labs/sys/t-avtopilot-skill.md` | decision and rejected options live in t-avtopilot-skill.md |
| U16 | 8 | THRESHOLD | Владелец — Андрей. | owner is Andrei |
| U17 | 10 | RULE | Этот Skill не повторяет чужую механику. | Skill does not duplicate others' mechanics |
| U18 | 10 | ADDRESS | Ревизия — `denken`. | revision lives in denken |
| U19 | 10 | ADDRESS | Чтение и запись репозитория — `second-brain-git`. | repo read/write lives in second-brain-git |
| U20 | 10 | ADDRESS | Форма вопроса посреднику — `second-brain-engineer`, правило «Чтение через | intermediary question form in second-brain-engineer, rule Reading via intermediary |
| U21 | 10 | RULE | Здесь только то, чего нет нигде | only what exists nowhere else is here |
| U22 | 10 | RULE | кто держит работу, когда Андрея нет рядом, и где она обязана остановиться | scope: who holds the work when Andrei is absent and where it must stop |
| U23 | 12 | ADDRESS | ## Зачем | heading: Why |
| U24 | 14 | REASON | Каждое короткое «да» Андрея заставляет модель заново обработать весь разросшийся | every short "yes" makes the model reprocess the whole grown conversation |
| U25 | 14 | REASON | Когда Андрей только соглашается, его реплики ничего не добавляют | when he only agrees his replies add nothing |
| U26 | 14 | REASON | а стоят каждый раз дороже предыдущего | but each costs more than the previous |
| U27 | 14 | REASON | Автопилот переносит согласование в одну точку — контракт запуска | autopilot moves agreement into one point, the launch contract |
| U28 | 14 | REASON | и убирает Андрея из роли курьера между исполнителями | and removes Andrei as courier between executors |
| U29 | 16 | ADDRESS | ## Пять ворот | heading: Five gates |
| U30 | 18 | RULE | Работа проходит ворота по порядку. | gates are passed in order |
| U31 | 18 | RULE | Ворота не пройдены — дальше не идти. | gate not passed: do not go on |
| U32 | 20 | ADDRESS | ### Ворота 1. Разговор — Андрей здесь | heading Gate 1 |
| U33 | 22 | THRESHOLD | Сессия добивается четырёх вещей, коротко и без лишнего контекста: | session obtains four things, briefly |
| U34 | 24 | THRESHOLD | **Квитанция рамки.** | item 1 name: frame receipt |
| U35 | 24 | RULE | Цели Андрея отдельно, его предположения о способе отдельно | goals separate from assumptions about method |
| U36 | 24 | THRESHOLD | по каждому предположению — «оставляю» или «предлагаю снять, потому что» | per assumption one of: keep / propose to drop because |
| U37 | 24 | ADDRESS | метод проектирования, пункт 1, `second-brain-engineer` references/design.md | design method point 1 in design.md |
| U38 | 25 | RULE | **Критерий приёмки — наблюдаемый объект.** | acceptance criterion must be an observable object |
| U39 | 25 | CHECK | «по каждому из восьми пунктов вердикт с адресом доказательства» | not "verified" but verdict per each of eight items with evidence address |
| U40 | 25 | RULE | Критерий без объекта — ворота не пройдены. | criterion without object: gate not passed |
| U41 | 26 | RULE | **Все ручные действия Андрея — одним списком сразу.** | all manual actions of Andrei in one list at once |
| U42 | 26 | THRESHOLD | Это действия, которые сессия сделать не может | definition: actions the session cannot do |
| U43 | 26 | THRESHOLD | создать Claude Project, привязать ключ доступа в n8n, перезалить Skill, | examples: create Claude Project, bind n8n credential, re-upload Skill |
| U44 | 26 | THRESHOLD | вставить мастер-промпт, открыть папку сервисному аккаунту | examples: paste master prompt, open folder to service account |
| U45 | 26 | RULE | Список собирается в начале, а не всплывает по ходу. | list is collected at start, not surfacing along the way |
| U46 | 27 | RULE | **Стоп-список** (раздел ниже) дополняется особыми стопами этой работы. | stop list is supplemented with special stops of this work |
| U47 | 29 | ADDRESS | ### Ворота 2. Ревизия | heading Gate 2 |
| U48 | 31 | THRESHOLD | Skill `denken`, уровень 2, при необратимой или разрушительной операции — | denken level 2; level 3 for irreversible/destructive |
| U49 | 31 | RULE | Ревизия идёт по написанному плану. | revision runs on the written plan |
| U50 | 31 | RULE | Отдельный пункт ревизии для автопилота: какие шаги действительно независимы. | extra revision item: which steps are really independent |
| U51 | 31 | REASON | Если все шаги строго последовательны, параллельности не будет | if all steps are sequential there is no parallelism |
| U52 | 31 | RULE | это говорится вслух до запуска, а не обнаруживается после | say it aloud before launch, not discover after |
| U53 | 33 | ADDRESS | ### Ворота 3. Контракт запуска — одно «да» | heading Gate 3 |
| U54 | 35 | RULE | Контракт — один текст, записанный в канон до исполнения: | contract is one text written into canon before execution |
| U55 | 36 | THRESHOLD | repo-проект — раздел «Контракт автопилота» в `PLAN.md` проекта | repo project: section Autopilot contract in PLAN.md |
| U56 | 37 | THRESHOLD | лаборатория — сам файл задачи `t-<имя>.md` | lab: the task file itself |
| U57 | 38 | EXCEPTION | если записать нельзя — блоком в чате | if cannot write: block in chat |
| U58 | 38 | RULE | запись контракта становится первым шагом исполнения | then writing the contract is the first execution step |
| U59 | 40 | THRESHOLD | Поля контракта: цель; критерий приёмки; пакеты работы | contract fields: goal; criterion; work packages |
| U60 | 40 | THRESHOLD | (у каждого — объекты, вопрос, ожидаемый результат-объект, класс модели) | package fields: objects, question, expected result object, model class |
| U61 | 40 | THRESHOLD | разрешённые правки списком; особые стопы. | fields: allowed edits list; special stops |
| U62 | 42 | RULE | Список разрешённых правок и есть пакет разрешения | allowed-edits list is the permission package |
| U63 | 42 | ADDRESS | (`second-brain-engineer`, «Воркфлоу n8n — полномочия») | rule on n8n workflow authority in second-brain-engineer |
| U64 | 42 | RULE | правка из списка исполняется без повторного «да» | listed edit executes without repeat yes |
| U65 | 42 | EXCEPTION | правка вне списка — снова по общему правилу. | edit outside the list follows the general rule again |
| U66 | 44 | THRESHOLD | Согласием считается ответ Андрея на контракт: «да», «действуй», «запускай». | consent words: yes / act / launch |
| U67 | 44 | RULE | Молчание согласием не считается. | silence is not consent |
| U68 | 46 | ADDRESS | ### Ворота 4. Исполнение — Андрея нет | heading Gate 4 |
| U69 | 48 | RULE | **Шина — сессия-диспетчер, а не Андрей.** | bus is the dispatcher session, not Andrei |
| U70 | 48 | EXCEPTION | правило Skill `naryad` «Андрей — шина, роли между собой не общаются» не | in autonomous mode naryad rule "Andrei is the bus" does not apply |
| U71 | 48 | RULE | диспетчер сам раздаёт работу субагентам и сам принимает их ответы | dispatcher hands out work and accepts answers itself |
| U72 | 48 | RULE | Вне автономного режима `naryad` не меняется. | outside autonomous mode naryad unchanged |
| U73 | 48 | RULE | Наряды в формате `naryad` внутри автопилота не печатаются | naryad-format orders are not printed inside autopilot |
| U74 | 48 | REASON | пакет контракта — не наряд | a contract package is not an order |
| U75 | 50 | ADDRESS | **Когда раздавать субагенту.** | heading: when to hand to a subagent |
| U76 | 50 | CASE | Замер 2026-10-13: старт одного субагента — около 80–110 тысяч токенов | 2026-10-13 measurement: one subagent start ~80-110k tokens |
| U77 | 50 | REASON | почти всё — его собственный стартовый контекст | almost all is its own startup context |
| U78 | 51 | RULE | субагенту отдаётся только тяжёлое чтение, которое нельзя сузить до попадания в | only heavy reading that cannot be narrowed goes to a subagent |
| U79 | 51 | THRESHOLD | полный граф воркфлоу, длинная выдача внешнего API, большая пачка файлов | examples: full workflow graph, long external API output, big file batch |
| U80 | 52 | RULE | лёгкий шаг (одно чтение файла, одно число, одна запись) диспетчер делает сам | light step is done by the dispatcher |
| U81 | 53 | RULE | объекты группируются по субагентам так, чтобы один старт обслуживал два-три | group objects so one start serves two-three objects |
| U82 | 53 | CASE | пилот проверил девять воркфлоу четырьмя субагентами | pilot checked nine workflows with four subagents |
| U83 | 54 | RULE | независимые пакеты запускаются одним сообщением | independent packages launched in one message |
| U84 | 54 | REASON | тогда они идут параллельно | then they run in parallel |
| U85 | 56 | THRESHOLD | **Что умеет субагент** | heading: what a subagent can do |
| U86 | 56 | CASE | зонд 2026-10-13, исполнение n8n 79581 | probe 2026-10-13, n8n execution 79581 |
| U87 | 56 | THRESHOLD | Есть: инструменты n8n, Канал чтения репозитория, память, Google Drive | has: n8n tools, repo read channel, memory, Google Drive, shell |
| U88 | 56 | THRESHOLD | Нет: запуска своих субагентов — глубина одна, как в `naryad`. | has not: spawning subagents; depth one |
| U89 | 58 | RULE | **Задание субагенту** — вопрос, а не файл | task to subagent is a question, not a file |
| U90 | 58 | ADDRESS | по форме посредника (`second-brain-engineer`, Р21 «Чтение через посредника»: | follows intermediary form, section Р21 |
| U91 | 58 | THRESHOLD | вопрос без ожидаемого ответа, адрес доказательства при каждом факте, | question without expected answer; evidence address per fact |
| U92 | 58 | THRESHOLD | NOT_FOUND со списком мест, вопросы пакетом | NOT_FOUND with list of places; questions batched |
| U93 | 59 | RULE | по умолчанию только чтение, и это написано в задании словами | read-only by default, stated in the task in words |
| U94 | 59 | THRESHOLD | «READ-ONLY, ничего не менять» | exact phrase READ-ONLY, change nothing |
| U95 | 60 | RULE | у вопроса закрытый набор вердиктов | question has closed verdict set |
| U96 | 60 | THRESHOLD | (например, ЖИВ / ИСПРАВЛЕН / ИЗМЕНЁН) | verdict example: ALIVE / FIXED / CHANGED |
| U97 | 61 | RULE | задание пишется на английском и компактно | task written in English, compact |
| U98 | 61 | REASON | субагент его читает, Андрей нет | subagent reads it, Andrei does not |
| U99 | 63 | RULE | **Пишет в канон только диспетчер.** | only dispatcher writes to canon |
| U100 | 63 | REASON | Так нет гонки записи внутри прогона | no write race within a run |
| U101 | 63 | REASON | и правила записи `second-brain-git` читает одна сессия, а не каждая | one session reads write rules, not each |
| U102 | 63 | RULE | Правила, которые диспетчер исполняет сам, он читает сам, а не через посредника. | rules dispatcher executes it reads itself, not via intermediary |
| U103 | 65 | RULE | **Перед правкой воркфлоу n8n** диспетчер перечитывает время последнего изменения | before editing an n8n workflow re-read last-modified time |
| U104 | 65 | THRESHOLD | (updatedAt) | field name updatedAt |
| U105 | 65 | CHECK | сверяет его с прочитанным в начале | compare with the value read at start |
| U106 | 65 | RULE | Расхождение — стоп | mismatch: stop |
| U107 | 65 | REASON | воркфлоу правит параллельная сессия | a parallel session is editing the workflow |
| U108 | 65 | REASON | а правка в n8n перезаписывает граф без проверки версии | n8n edit overwrites the graph without version check |
| U109 | 65 | ADDRESS | (`labs/sys/t-n8n-workflow-race.md`) | evidence in t-n8n-workflow-race.md |
| U110 | 67 | THRESHOLD | **Долгое ожидание** (прогон воркфлоу на десятки минут) | long wait definition: workflow run of tens of minutes |
| U111 | 67 | RULE | возврат в ту же сессию через отложенное сообщение самому себе | return to same session via deferred message to itself |
| U112 | 67 | CASE | Это проверено пятью срабатываниями до 2026-10-13. | verified by five firings before 2026-10-13 |
| U113 | 67 | CASE | Запланированная задача со свежей сессией на этом аккаунте не создавалась ни разу | scheduled task with fresh session never created on this account |
| U114 | 67 | REASON | режим одобрения у неё неизвестен до создания | its approval mode unknown until creation |
| U115 | 67 | RULE | как носитель автопилота она используется только после отдельного зонда | scheduled task as autopilot carrier only after separate probe |
| U116 | 67 | ADDRESS | записанного в `t-avtopilot-skill.md` | probe recorded in t-avtopilot-skill.md |
| U117 | 69 | RULE | **Массовая механическая работа** — скриптом, а не моделью | mass mechanical work by script, not by model |
| U118 | 69 | ADDRESS | `second-brain-engineer`, references/design.md, пункт 17 | design.md point 17 |
| U119 | 69 | ADDRESS | для файлов репозитория — `second-brain-git` 9.4(б) | for repo files second-brain-git 9.4(b) |
| U120 | 71 | ADDRESS | ### Ворота 5. Приёмка и отчёт | heading Gate 5 |
| U121 | 73 | RULE | **Приёмку делает отдельный субагент сильного класса, который работу не делал.** | acceptance by separate strong-class subagent who did not do the work |
| U122 | 73 | RULE | Он получает утверждения в виде списка проверяемых фраз и задачу их опровергнуть | receives claims as checkable phrases and task to refute by object |
| U123 | 73 | RULE | Отчёты исполнителей и рассуждения диспетчера ему не передаются. | executor reports and dispatcher reasoning not passed |
| U124 | 73 | CASE | Прецедент: так принимался поиск archive-recon | precedent: archive-recon search accepted this way |
| U125 | 73 | ADDRESS | `projects/archive-recon/STATE.md` | address of the precedent |
| U126 | 73 | CASE | «независимую проверку делает агент с моделью opus, запускаемый из сессии» | quote: independent check by opus agent launched from session |
| U127 | 74 | RULE | Вопросы приёмки составляет не исполнитель | acceptance questions not written by the executor |
| U128 | 74 | RULE | исправления по находке приёмщика проверяет повторно приёмщик | fixes after acceptor finding re-checked by acceptor |
| U129 | 74 | ADDRESS | (`second-brain-engineer`, references/design.md, пункт 14, г и д) | design.md point 14 g and d |
| U130 | 76 | RULE | **Находки приёмщика сверх вопроса — гипотезы.** | acceptor findings beyond the question are hypotheses |
| U131 | 76 | THRESHOLD | Они идут в канон словом «Гипотеза (не проверена):» | recorded with label "Гипотеза (не проверена):" |
| U132 | 76 | RULE | пока диспетчер не проверил их по объекту | until dispatcher checks them by object |
| U133 | 76 | CASE | Пилот: приёмщик объявил, что незакрытый комментарий в коде узла роняет каждый | pilot: acceptor claimed unclosed comment crashes every run |
| U134 | 76 | CASE | единственный сохранённый прогон упал раньше — на ключе доступа Google в первом | only saved run failed earlier on Google credential in first node |
| U135 | 76 | CASE | Значит, по прогону гипотеза не проверена. | so hypothesis not verified by the run |
| U136 | 78 | RULE | **Критерий приёмки не смягчается** | acceptance criterion is not softened |
| U137 | 78 | ADDRESS | (метод проектирования, пункт 15) | design method point 15 |
| U138 | 78 | THRESHOLD | Не выполнен — итог «не выполнено, вот почему». | if unmet, outcome "not fulfilled, here is why" |
| U139 | 80 | RULE | Затем диспетчер пишет результат в канон | dispatcher then writes result to canon |
| U140 | 80 | CHECK | проверяет запись обратным чтением | verifies write by read-back |
| U141 | 80 | THRESHOLD | выдаёт Андрею один отчёт: проблема, причина, что сделано, что сделать ему. | one report: problem, cause, done, what he must do |
| U142 | 80 | RULE | Без пересказа шагов. | no retelling of steps |
| U143 | 82 | ADDRESS | ## Стоп-список — где работа останавливается сама | heading: stop list |
| U144 | 84 | RULE | Остановка — сообщение Андрею с тем, на чём встало, и с подготовленным решением. | stop = message to Andrei with blocker and prepared decision |
| U145 | 84 | RULE | Не тихое ожидание. | not silent waiting |
| U146 | 86 | RULE | Нужно действие из списка ручных действий Андрея, а он его не сделал. | stop 1: manual action not done |
| U147 | 87 | RULE | Нужно необратимое решение, которое разумно принять в обе стороны. | stop 2: irreversible decision reasonable both ways |
| U148 | 88 | RULE | Меняется цель или предмет работы. | stop 3: goal or subject changes |
| U149 | 88 | CASE | Прецедент — archive-recon начинался как разведка, а превратился в каталогизацию | precedent: archive-recon recon turned into cataloging |
| U150 | 88 | CASE | цель переопределяли задним числом | goal redefined retroactively |
| U151 | 88 | ADDRESS | (записи Р-13 и Р-14 журнала `projects/archive-recon/LOG.md`) | log entries Р-13 and Р-14 |
| U152 | 89 | RULE | Правка нужна вне списка разрешённых. | stop 4: edit needed outside allowed list |
| U153 | 90 | RULE | Два круга правок без сходимости — стоп-линия `denken`. | stop 5: two edit rounds without convergence |
| U154 | 90 | ADDRESS | стоп-линия `denken` | stop-line lives in denken |
| U155 | 91 | RULE | Жёсткий барьер: политика, закон, ограничение платформы. | stop 6: hard barrier |
| U156 | 91 | THRESHOLD | политика, закон, ограничение платформы | barrier types: policy, law, platform limit |
| U157 | 92 | RULE | Время последнего изменения воркфлоу разошлось с прочитанным в начале. | stop 7: workflow modified time diverged |
| U158 | 93 | RULE | Критерий приёмки не выполнен. | stop 8: acceptance criterion unmet |
| U159 | 95 | RULE | Находка вне рамки контракта работу не прерывает. | out-of-contract finding does not interrupt work |
| U160 | 95 | ADDRESS | Она идёт захватом по правилу мастер-промпта проекта | captured per project master prompt rule |
| U161 | 95 | RULE | объектный блокер — сразу, кандидат и мелочь — на !save | object blocker immediately; candidate and trivia on !save |
| U162 | 97 | ADDRESS | ## Чего этот Skill не делает | heading: what this Skill does not do |
| U163 | 99 | RULE | Не заводит мониторов, сигналов живости и журналов наблюдения за автопилотом. | no monitors, liveness signals, observation logs |
| U164 | 100 | RULE | Не меняет `naryad` вне автономного режима. | does not change naryad outside autonomous mode |
| U165 | 101 | RULE | Не разрешает правку Skill, мастер-промпта, удаление данных или правку воркфлоу | does not allow editing Skill, master prompt, data deletion, workflow edit |
| U166 | 101 | EXCEPTION | без контракта, где они названы | unless named in a contract |
| U167 | 102 | RULE | Не считает ответ субагента записью в канон | subagent answer is not a canon record |
| U168 | 102 | RULE | в канон идёт то, что диспетчер прочитал сам | canon gets what dispatcher read itself |
| U169 | 102 | RULE | вердикт приёмщика входит в канон, когда диспетчер сам прочитал адрес | acceptor verdict enters canon when dispatcher read the evidence address |
| U170 | 102 | THRESHOLD | (одна строка файла, одно поле ответа инструмента) | evidence address forms: one file line, one tool-response field |
| U171 | 102 | RULE | без этого он гипотеза | otherwise it is a hypothesis |
| U172 | 102 | ADDRESS | (`second-brain-engineer`, Р21, ПРОВЕРКА) | Р21 CHECK section |
| U173 | 104 | ADDRESS | ## Цена пилота 2026-10-13 | heading: pilot cost |
| U174 | 106 | CASE | Задача — восемь дефектов аудита 2026-07-23 в девяти воркфлоу. | task: eight defects of 2026-07-23 audit in nine workflows |
| U175 | 107 | CASE | Четыре проверяющих субагента среднего класса — 433 329 токенов. | four mid-class checkers: 433,329 tokens |
| U176 | 108 | CASE | Приёмщик сильного класса — 185 402 токена. | strong-class acceptor: 185,402 tokens |
| U177 | 109 | CASE | Сообщений Андрея между «Действуй!» и итоговым отчётом — ноль. | zero Andrei messages between Go and final report |
| U178 | 111 | CASE | Сравнения с той же работой без автопилота нет — не измерено. | no comparison without autopilot, not measured |
