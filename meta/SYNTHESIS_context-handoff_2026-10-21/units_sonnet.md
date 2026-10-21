# context-handoff old text decomposition
| id | lines | class | quote | paraphrase |
|---|---|---|---|---|
| H001 | 2 | THRESHOLD | name: context-handoff | Skill name is context-handoff |
| H002 | 3 | THRESHOLD | name: context-handoff description: \" | Description field contains a nested duplicate "name: context-handoff description:" prefix (malformed nesting) |
| H003 | 3 | RULE | Читай этот Skill ТОЛЬКО по явной команде пользователя | Read the Skill only on an explicit user command |
| H004 | 3 | THRESHOLD | эстафета, эстафета?, перенеси в новый чат, передай контекст, пора в новый чат | Trigger command words: эстафета, эстафета?, перенеси в новый чат, передай контекст, пора в новый чат |
| H005 | 3 | RULE | Не применяй по собственной инициативе | Do not apply on own initiative |
| H006 | 3 | EXCEPTION | не при общих разговорах о контексте, лимитах или токенах | Do not trigger on general talk about context, limits, tokens |
| H007 | 3 | THRESHOLD | протокол переноса работы над проектом в новую сессию через Зону А INDEX | Content: protocol of moving project work to new session via Zone A of INDEX |
| H008 | 3 | THRESHOLD | две независимые шкалы оценки сессии, стоп-линию | Content: two independent session-assessment scales, stop-line |
| H009 | 3 | THRESHOLD | правила разрешения конфликта записи и протухания | Content: rules for write-conflict resolution and staleness |
| H010 | 3 | THRESHOLD | version: \"1.1\" | Version 1.1 |
| H011 | 3 | CASE | created: 2026-08-03 | Created 2026-08-03 |
| H012 | 3 | THRESHOLD | supersedes: \"1.0\" | Supersedes version 1.0 |
| H013 | 3 | THRESHOLD | owner: Андрей | Owner Andrei |
| H014 | 6 | THRESHOLD | CONTEXT-HANDOFF — протокол эстафеты между сессиями | Title: CONTEXT-HANDOFF, relay protocol between sessions |
| H015 | 7 | THRESHOLD | 0. ЗАЧЕМ И ЧЕГО ЭТОТ SKILL НЕ ДЕЛАЕТ | Heading section 0: why and what Skill does not do |
| H016 | 8 | REASON | каждое сообщение оплачивает весь накопленный контекст заново | Each message re-pays the entire accumulated context |
| H017 | 8 | REASON | Расход растёт квадратично к длине сессии | Cost grows quadratically with session length |
| H018 | 8 | REASON | Перенос работы в новый чат — прежде всего экономия лимитов, и только во вторую очередь гигиена качества | Handoff is primarily limit savings, secondarily quality hygiene |
| H019 | 9 | REASON | Перенос НЕ бесплатен: новая сессия заново платит преамбулу | Handoff is not free: new session pays the preamble again |
| H020 | 9 | THRESHOLD | мастер-промпт + Skills + стартовые чтения ≈ 15 КБ | Preamble = master prompt + Skills + start reads ≈ 15 KB |
| H021 | 9 | RULE | Эстафета применяется не «когда устали», а когда накопленный контекст стал заметно дороже новой преамбулы | Apply handoff when accumulated context is noticeably costlier than new preamble, not when "tired" |
| H022 | 10 | RULE | ГРАНИЦА ПРИМЕНИМОСТИ — читать первым | Applicability boundary: read first |
| H023 | 10 | REASON | Skill загружается только по явной команде. До первой команды в сессии его в контексте нет, и Claude ничего не отслеживает | Skill loads only on explicit command; before the first command it is not in context and Claude tracks nothing |
| H024 | 11 | RULE | Skill не даёт проактивных предупреждений «пора переносить» | No proactive "time to hand off" warnings |
| H025 | 11 | REASON | Это осознанная цена невидимости | That is a deliberate price of invisibility |
| H026 | 12 | RULE | Все оценки ниже выполняются в момент команды, ретроспективно | All assessments performed at command time, retrospectively |
| H027 | 13 | RULE | Если после команды эстафета? пользователь решил продолжить в этом же чате, ... Claude может добавлять одну строку статуса | If user continues after "эстафета?", Claude may add one status line at end of replies |
| H028 | 13 | EXCEPTION | До первой команды — нет | Before first command no status line |
| H029 | 14 | THRESHOLD | СРЕДА. В claude.ai и Cowork нет /compact и /clear | Environment: claude.ai and Cowork have no /compact and /clear |
| H030 | 14 | THRESHOLD | ПРОДОЛЖАТЬ / ЭСТАФЕТА+новый чат / ВЫНЕСТИ в файл | Exactly three outcomes: CONTINUE / HANDOFF+new chat / MOVE OUT to file |
| H031 | 14 | RULE | Не предлагать компактизацию и очистку | Do not suggest compaction or clearing |
| H032 | 14 | REASON | этих механизмов здесь не существует | Those mechanisms do not exist here |
| H033 | 15 | RULE | Канал переноса — Зона А INDEX проекта, не буфер обмена. Пользователь ничего не копирует | Transfer channel is Zone A of project INDEX, not clipboard; user copies nothing |
| H034 | 15 | RULE | В новой сессии Зона А читается на старте по мастер-промпту | In new session Zone A is read at start per master prompt |
| H035 | 17 | THRESHOLD | 1. КОМАНДЫ | Heading section 1: commands |
| H036 | 18-19 | THRESHOLD | Команда / Действие | Table 1 columns: Command, Action |
| H037 | 20-21 | THRESHOLD | эстафета? / Только оценка по разделу 2. Вердикт по форме из 2.4 | Command "эстафета?" = assessment only per section 2, verdict in form 2.4 |
| H038 | 21 | RULE | НЕ писать в INDEX | "эстафета?" must not write to INDEX |
| H039 | 22-23 | THRESHOLD | эстафета / Стоп-линия → запись → верификация → «открывай новый чат» | Command "эстафета" = stop-line check, write, verify, say "open new chat" |
| H040 | 24-25 | THRESHOLD | эстафета в [ПРОЕКТ] / То же, в INDEX указанного проекта | Command "эстафета в [ПРОЕКТ]" = same, into INDEX of named project |
| H041 | 27 | RULE | Право решения — за пользователем. Claude оценивает и рекомендует; действует только по команде эстафета | Decision belongs to user; Claude assesses/recommends, acts only on command "эстафета" |
| H042 | 27 | EXCEPTION | Единственное исключение — стоп-линия (раздел 4): она блокирует запись даже по прямой команде, до устранения блокера | Sole exception: stop-line blocks writing even on direct command until blocker removed |
| H043 | 29 | THRESHOLD | 2. ОЦЕНКА: ДВЕ НЕЗАВИСИМЫЕ ШКАЛЫ | Heading section 2: assessment, two independent scales |
| H044 | 30 | RULE | Шкалы измеряют разное и дают разные рекомендации. Считать обе, не смешивать | Scales measure different things; compute both, do not mix |
| H045 | 31 | THRESHOLD | 2.1 Шкала СТОИМОСТЬ — сколько весит сессия | Heading 2.1: COST scale, how heavy session is |
| H046 | 32-36 | RULE | Оценивается всё, что вошло в контекст с начала сессии, а не только прочитанные файлы | Assess everything in context since session start, not only read files |
| H047 | 33 | THRESHOLD | документы, вставленные пользователем | Included: documents pasted by user |
| H048 | 34 | THRESHOLD | прочитанные файлы и выхлопы инструментов | Included: files read and tool outputs |
| H049 | 35 | THRESHOLD | собственные развёрнутые ответы Claude | Included: Claude's own long replies |
| H050 | 36 | THRESHOLD | созданные в сессии артефакты | Included: artifacts created in session |
| H051 | 37 | RULE | Оценка грубая, в КБ, по порядку величины | Estimate is rough, in KB, order of magnitude |
| H052 | 37 | THRESHOLD | экран плотного текста ≈ 3 КБ | Reference: screen of dense text ≈ 3 KB |
| H053 | 37 | THRESHOLD | крупная статья или выхлоп исследования ≈ 8–10 КБ | Reference: large article / research output ≈ 8-10 KB |
| H054 | 37 | THRESHOLD | INDEX-файл — десятки КБ | Reference: INDEX file tens of KB |
| H055 | 38-40 | THRESHOLD | Уровень / Объём сессии / Смысл | Cost table columns: Level, Session volume, Meaning |
| H056 | 41-43 | THRESHOLD | 🟢 / до ~30 КБ | COST green: up to ~30 KB |
| H057 | 43 | RULE | Перенос убыточен: преамбула дороже накопленного | Green meaning: handoff is unprofitable, preamble costs more than accumulated |
| H058 | 44-46 | THRESHOLD | 🟡 / ~30–60 КБ | COST yellow: ~30-60 KB |
| H059 | 46 | RULE | Перенос окупается, если фаза закрыта | Yellow meaning: handoff pays off if phase closed |
| H060 | 47-49 | THRESHOLD | 🔴 / свыше ~60 КБ | COST red: over ~60 KB |
| H061 | 49 | RULE | Перенос окупается заметно | Red meaning: handoff clearly pays off |
| H062 | 51 | RULE | Пороги — эвристика, не закон | Thresholds are heuristics not law |
| H063 | 51 | REASON | Погрешность оценки в разы допустима: решение меняется только на порядках | Multiple-fold error acceptable; decision changes only by orders of magnitude |
| H064 | 52 | THRESHOLD | 2.2 Шкала НАДЁЖНОСТЬ — можно ли доверять этой сессии | Heading 2.2: RELIABILITY scale, can this session be trusted |
| H065 | 53 | RULE | Считать только внешне наблюдаемые события | Count only externally observable events |
| H066 | 53 | RULE | Собственное ощущение («кажется, я путаюсь») признаком НЕ является | Own feeling ("I seem confused") is not a sign |
| H067 | 53 | REASON | сломанный прибор не измеряет свою поломку | A broken instrument does not measure its own breakage |
| H068 | 55 | THRESHOLD | перечитан файл, уже прочитанный в этой сессии | Sign 1: re-read file already read in session |
| H069 | 56 | THRESHOLD | Claude противоречит решению, принятому ранее в этой же сессии | Sign 2: Claude contradicts earlier decision of same session |
| H070 | 57 | THRESHOLD | Claude спросил факт, который пользователь уже давал | Sign 3: Claude asked a fact user already gave |
| H071 | 58 | THRESHOLD | пользователь сказал «мы это уже обсуждали» / «я тебе говорил» | Sign 4: user said "we already discussed" / "I told you" |
| H072 | 59 | THRESHOLD | две итерации без нового проверяемого результата | Sign 5: two iterations without new verifiable result |
| H073 | 60-62 | THRESHOLD | Уровень / Условие / 🟢 / признаков нет | RELIABILITY green: no signs |
| H074 | 64-65 | THRESHOLD | 🟡 / один признак | RELIABILITY yellow: one sign |
| H075 | 66-67 | THRESHOLD | 🔴 / два и более признака | RELIABILITY red: two or more signs |
| H076 | 69 | RULE | При 🟡 и выше по НАДЁЖНОСТИ — сначала re-anchor, до любой рекомендации | At yellow+ reliability, do re-anchor first, before any recommendation |
| H077 | 69 | RULE | Re-anchor: вслух повторить ЦЕЛЬ, действующие ЗАПРЕТЫ и СЛЕДУЮЩИЙ ШАГ | Re-anchor = say aloud GOAL, active PROHIBITIONS, NEXT STEP |
| H078 | 69 | CHECK | Если воспроизвести не удалось или пользователь поправил — деградация подтверждена внешне | If can't reproduce or user corrects -> degradation confirmed |
| H079 | 69 | CHECK | Если воспроизвелось точно — признак был ложным, уровень снижается | If reproduced exactly -> sign was false, level lowered |
| H080 | 70 | THRESHOLD | 2.3 Совмещение шкал | Heading 2.3: combining scales |
| H081 | 71-73 | THRESHOLD | СТОИМОСТЬ / НАДЁЖНОСТЬ / Рекомендация | Table 2.3 columns |
| H082 | 74-76 | RULE | 🟢 / 🟢 / ПРОДОЛЖАТЬ | Cost green + reliability green -> CONTINUE |
| H083 | 77-79 | RULE | 🟢 / 🔴 / ЭСТАФЕТА — контекст мешает, хотя и дёшев | Cost green + reliability red -> HANDOFF (context hinders though cheap) |
| H084 | 80-82 | RULE | 🟡 / 🟢/🟡 / ЭСТАФЕТА, если фаза закрыта; иначе — закрыть фазу | Cost yellow + reliability green/yellow -> HANDOFF if phase closed, else close phase |
| H085 | 83-85 | RULE | 🔴 / любая / ЭСТАФЕТА, если фаза закрыта; иначе — закрыть фазу | Cost red + any reliability -> HANDOFF if phase closed, else close phase |
| H086 | 80-82 | CASE | (gap) 🟡 cost + 🔴 reliability row not in table | Table has no explicit row for yellow cost + red reliability (implicit gap) |
| H087 | 87 | RULE | «Фаза закрыта» = завершён шаг обслуживания, закрыта задача либо готов артефакт, и нет незавершённой записи | Phase closed = service step done, task closed or artifact ready, and no unfinished write |
| H088 | 88 | RULE | Правило незакрытой фазы (перевешивает уровни шкал): посреди операции эстафета не рекомендуется | Unclosed-phase rule overrides scale levels: no handoff recommended mid-operation |
| H089 | 88 | RULE | Рекомендуется завершить текущую фазу и после этого перенести. Формулировать именно так, не как «продолжаем» | Recommend finishing the phase then handoff; phrase it that way, not as "continue" |
| H090 | 89 | RULE | Приоритет при конфликте: сохранность данных > точность работы > экономия контекста | Conflict priority: data safety > work accuracy > context savings |
| H091 | 89 | RULE | Экономия никогда не оправдывает разрыв незавершённой операции | Savings never justify breaking an unfinished operation |
| H092 | 90 | THRESHOLD | 2.4 Форма вердикта по команде эстафета? | Heading 2.4: verdict form on "эстафета?" |
| H093 | 91 | THRESHOLD | Ровно четыре строки, без развёрнутых рассуждений | Exactly four lines, no extended reasoning |
| H094 | 92 | THRESHOLD | СТОИМОСТЬ: 🟡 ~45 КБ | Line 1: COST: emoji + ~KB |
| H095 | 93 | THRESHOLD | НАДЁЖНОСТЬ: 🟢 признаков нет | Line 2: RELIABILITY: emoji + signs note |
| H096 | 94 | THRESHOLD | ФАЗА: закрыта / не закрыта — [что именно висит] | Line 3: PHASE: closed / not closed - what hangs |
| H097 | 95 | THRESHOLD | ВЕРДИКТ: ПРОДОЛЖАТЬ / ЭСТАФЕТА / ЗАКРЫТЬ ФАЗУ, ЗАТЕМ ЭСТАФЕТА | Line 4: VERDICT: CONTINUE / HANDOFF / CLOSE PHASE THEN HANDOFF |
| H098 | 98 | THRESHOLD | 3. ФОРМАТ БЛОКА | Heading section 3: block format |
| H099 | 99 | RULE | Пишется в Зону А INDEX проекта ОДНОЙ строкой | Written into Zone A of project INDEX as ONE line |
| H100 | 99 | THRESHOLD | поля разделены « | », перевода строки внутри нет | Fields separated by " | ", no newline inside |
| H101 | 99 | THRESHOLD | Лимит 1 КБ | Limit 1 KB |
| H102 | 100 | THRESHOLD | ## ЭСТАФЕТА | Block heading token "## ЭСТАФЕТА" |
| H103 | 100 | THRESHOLD | СТАТУС: active | Field СТАТУС: active |
| H104 | 100 | THRESHOLD | ОБНОВЛЕНО: YYYY-MM-DD HH:MM | Field ОБНОВЛЕНО: YYYY-MM-DD HH:MM |
| H105 | 100 | THRESHOLD | ЧАТ: [короткая метка сессии] | Field ЧАТ: short session label |
| H106 | 100 | THRESHOLD | ЦЕЛЬ: одна фраза — что должно быть достигнуто | Field ЦЕЛЬ: one phrase, what to achieve |
| H107 | 100 | THRESHOLD | СОСТОЯНИЕ: где остановились | Field СОСТОЯНИЕ: where stopped |
| H108 | 100 | THRESHOLD | ЗАПРЕТЫ: что нельзя делать в этой задаче (must-not, контракты, форматы) | Field ЗАПРЕТЫ: must-not, contracts, formats |
| H109 | 100 | THRESHOLD | ДОБЫТО [Ф/Г]: факты из дорогих чтений — ID, значения, результаты проверок | Field ДОБЫТО [Ф/Г]: facts from expensive reads: IDs, values, check results |
| H110 | 100 | THRESHOLD | РЕШЕНО: решения сессии, ещё не попавшие в CORE/CHANGELOG | Field РЕШЕНО: session decisions not yet in CORE/CHANGELOG |
| H111 | 100 | THRESHOLD | ТУПИКИ: что проверено и НЕ сработало — с причиной | Field ТУПИКИ: checked and failed, with reason |
| H112 | 100 | THRESHOLD | СЛЕДУЮЩИЙ ШАГ: один исполнимый шаг, без «продолжить работу» | Field СЛЕДУЮЩИЙ ШАГ: one executable step, not "continue work" |
| H113 | 100 | THRESHOLD | ЯКОРЯ: ID файлов, воркфлоу, номера строк | Field ЯКОРЯ: IDs of files, workflows, line numbers |
| H114 | 101 | RULE | В ДОБЫТО каждый пункт несёт метку: Ф = проверено чтением, Г = гипотеза | Each ДОБЫТО item carries label: Ф = verified by reading, Г = hypothesis |
| H115 | 102 | REASON | Почему одна строка: инструменты записи в Google Docs заменяют только однострочный якорь | Why one line: Google Docs write tools replace only a single-line anchor |
| H116 | 102 | ADDRESS | Skill `google-drive-docs`, `references/docs-write.md`, §3.2 и §3.6 | Pointer: google-drive-docs, references/docs-write.md, §3.2 and §3.6 |
| H117 | 102 | REASON | многострочный блок заменой по заголовку не перезаписать — заменится строка заголовка, тело старого блока останется | Multi-line block can't be replaced by heading: only heading line replaced, old body remains |
| H118 | 102 | REASON | Почему 1 КБ: строка блока целиком служит якорем следующей замены и идёт телом вызова | Why 1 KB: whole block line is anchor of next replace and goes in call body |
| H119 | 102 | THRESHOLD | граница текста телом вызова — 1–2 КБ | Call-body text limit is 1-2 KB |
| H120 | 102 | ADDRESS | (там же, §3.0) | Pointer: same file, §3.0 |
| H121 | 102 | CASE | решение Андрея 2026-10-21 | Basis: Andrei's decision 2026-10-21 |
| H122 | 102 | ADDRESS | `meta/ANSWERS_synthesis-questions_2026-10-21.md`, вопрос 3 раздела google-drive-docs | Pointer: meta/ANSWERS_synthesis-questions_2026-10-21.md, question 3 of google-drive-docs section |
| H123 | 104 | RULE | Все поля обязательны. Пустое пишется как нет, не удаляется | All fields mandatory; empty field written as "нет", not deleted |
| H124 | 104 | REASON | отсутствие поля неотличимо от забытого поля | Absent field is indistinguishable from forgotten field |
| H125 | 105 | RULE | Порядок при превышении 1 КБ — резать снизу вверх в этом порядке | Over 1 KB: cut bottom-up in this order |
| H126 | 106 | RULE | ЯКОРЯ (сокращать до тех, что нужны для СЛЕДУЮЩЕГО ШАГА) | Cut 1st: ЯКОРЯ down to those needed for NEXT STEP |
| H127 | 107 | RULE | ТУПИКИ (оставить только последний) | Cut 2nd: ТУПИКИ keep only the last |
| H128 | 108 | RULE | ДОБЫТО (оставить только пункты, нужные для СЛЕДУЮЩЕГО ШАГА) | Cut 3rd: ДОБЫТО keep only items needed for NEXT STEP |
| H129 | 109 | RULE | Не режутся никогда: ЦЕЛЬ, ЗАПРЕТЫ, РЕШЕНО, СЛЕДУЮЩИЙ ШАГ | Never cut: ЦЕЛЬ, ЗАПРЕТЫ, РЕШЕНО, СЛЕДУЮЩИЙ ШАГ |
| H130 | 109 | REASON | По данным о деградации multi-turn диалогов первыми теряются именно инварианты — обязательства, запреты и прошлые решения | Per multi-turn degradation data, invariants (commitments, prohibitions, past decisions) are lost first |
| H131 | 110 | RULE | Если после реза не влезает — содержимое переросло эстафету и должно жить в INDEX как задача | If still not fitting, content outgrew handoff, must live in INDEX as task |
| H132 | 110 | RULE | Сказать об этом пользователю | Tell the user about that |
| H133 | 112 | THRESHOLD | 4. СТОП-ЛИНИЯ | Heading section 4: stop-line |
| H134 | 113 | RULE | Запись эстафеты ЗАПРЕЩЕНА, пока верно любое | Handoff write forbidden while any condition holds |
| H135 | 114 | THRESHOLD | выполнена деструктивная запись (replace, overwrite) без обратного чтения | Stop condition 1: destructive write (replace, overwrite) without read-back |
| H136 | 115 | THRESHOLD | ожидается результат воркфлоу | Stop condition 2: workflow result pending |
| H137 | 116 | THRESHOLD | есть незаписанные [ЗАХВАЧЕНО] | Stop condition 3: unrecorded [ЗАХВАЧЕНО] items |
| H138 | 117 | THRESHOLD | открыта операция, разрыв которой оставит систему в промежуточном состоянии | Stop condition 4: open operation whose interruption leaves system in intermediate state |
| H139 | 118 | RULE | Порядок жёсткий: сначала закрыть стоп-линию, потом эстафета | Strict order: close stop-line first, then handoff |
| H140 | 118 | REASON | Разорванная сессия посреди записи — тот класс потери данных, против которого построена вся система | Session torn mid-write is the data-loss class the whole system is built against |
| H141 | 119 | RULE | Стоп-линия ≠ незакрытая фаза. Стоп-линия запрещает запись | Stop-line is not an unclosed phase; stop-line forbids writing |
| H142 | 119 | EXCEPTION | Незакрытая фаза меняет рекомендацию, но по прямой команде запись выполняется | Unclosed phase only changes recommendation; on direct command write proceeds |
| H143 | 121 | THRESHOLD | 5. ПРОТОКОЛ ЗАПИСИ | Heading section 5: write protocol |
| H144 | 122 | RULE | Шаг 1: Проверить стоп-линию. Не прошла — назвать блокер и остановиться | Step 1: check stop-line; if failed name blocker and stop |
| H145 | 123 | RULE | Шаг 2: Прочитать текущую Зону А INDEX проекта | Step 2: read current Zone A of project INDEX |
| H146 | 124 | RULE | Шаг 3: Если блок ## ЭСТАФЕТА уже есть и поле ЧАТ не совпадает с текущей сессией — НЕ перезаписывать | Step 3: if block exists and ЧАТ differs from current session, do NOT overwrite |
| H147 | 124 | RULE | Показать пользователю существующий блок и спросить | Show the existing block to user and ask |
| H148 | 124 | RULE | Независимо от давности | Regardless of age of block |
| H149 | 124 | REASON | одновременная работа в нескольких проектах — норма, и цена лишнего вопроса ничтожна против цены затёртой чужой эстафеты | Parallel work in many projects is normal; extra question is cheap vs. overwriting another's handoff |
| H150 | 125 | RULE | Шаг 4: Собрать блок по разделу 3. Проверить объём, при необходимости резать по заданному порядку | Step 4: build block per section 3, check size, cut per given order |
| H151 | 126 | RULE | Шаг 5: Записать заменой, не append: эстафета всегда одна, последняя | Step 5: write by replace, not append; handoff is always single, latest |
| H152 | 126 | RULE | Якорь замены — ВСЯ текущая строка блока, начинающаяся с «## ЭСТАФЕТА», в точности как она прочитана на шаге 2, а не одни слова «## ЭСТАФЕТА» | Replace anchor = the whole current block line as read at step 2, not just "## ЭСТАФЕТА" words |
| H153 | 126 | REASON | замена меняет только совпавший текст | Replacement changes only the matched text |
| H154 | 126 | CHECK | Перед заменой проверить уникальность якоря (text.count) | Before replace verify anchor uniqueness (text.count) |
| H155 | 126 | THRESHOLD | Инструмент — gdocs-apply-from-file в режиме replace | Tool: gdocs-apply-from-file in replace mode |
| H156 | 126 | RULE | новая строка блока — файлом-источником, лежащим в папке, доступной сервисному аккаунту; старая — полем search | New block line goes as source file in a folder reachable by service account; old line in search field |
| H157 | 126 | ADDRESS | (там же, §3.6) ... Skill `google-drive-docs`, `references/docs-write.md`, §3.6 | Pointers: same file §3.6; google-drive-docs references/docs-write.md §3.6 |
| H158 | 126 | RULE | Если блока нет — тем же инструментом по якорю строки SENTINEL | If block absent: same tool, anchored on SENTINEL line |
| H159 | 126 | RULE | якорь заменяется на «строка эстафеты + перевод строки + та же строка SENTINEL», строка SENTINEL остаётся последней строкой Зоны А | SENTINEL anchor replaced with "handoff line + newline + same SENTINEL line"; SENTINEL stays last line of Zone A |
| H160 | 126 | RULE | Блок старой многострочной формы, найденный в документе, — вопрос Андрею | Old multi-line-form block found in document: ask Andrei |
| H161 | 126 | REASON | его тело одной заменой не убрать | Its body cannot be removed by one replace |
| H162 | 126 | RULE | gdocs-append пишет только в конец документа, то есть в Зону Б | gdocs-append writes only at document end, i.e. Zone B (not usable for block) |
| H163 | 126 | ADDRESS | Skill `google-drive-docs`, `references/docs-write.md`, раздел 3.1 | Pointer: google-drive-docs references/docs-write.md section 3.1 |
| H164 | 127 | RULE | Шаг 6: Верифицировать обратным чтением | Step 6: verify by read-back |
| H165 | 127 | CHECK | success: true подтверждением не является | success: true is not confirmation |
| H166 | 128 | RULE | Шаг 7: Сказать: «Эстафета записана в [ПРОЕКТ]. Открывай новый чат.» | Step 7: say "Handoff written in [PROJECT]. Open new chat." |
| H167 | 130 | THRESHOLD | 6. ПОДХВАТ В НОВОЙ СЕССИИ | Heading section 6: pickup in new session |
| H168 | 131 | RULE | Отдельной команды не требуется: Зона А читается на старте по мастер-промпту | No separate command needed; Zone A read at start per master prompt |
| H169 | 132 | RULE | Проверка свежести. ОБНОВЛЕНО старше 7 дней либо СТАТУС: stale → объявить вслух: «Эстафета протухла, работаю с нуля» | Freshness check: ОБНОВЛЕНО older than 7 days or СТАТУС stale -> announce "Handoff expired, working from scratch" |
| H170 | 132 | THRESHOLD | старше 7 дней | Staleness threshold 7 days |
| H171 | 132 | RULE | Данные из неё не использовать как факты | Do not use its data as facts |
| H172 | 132 | REASON | Устаревшая эстафета опаснее отсутствующей — она выглядит как знание | Stale handoff is more dangerous than none: looks like knowledge |
| H173 | 133 | RULE | Проверка расшифровки. Первым сообщением назвать вслух ЦЕЛЬ, ЗАПРЕТЫ и СЛЕДУЮЩИЙ ШАГ — тремя строками | Decode check: first message states GOAL, PROHIBITIONS, NEXT STEP in three lines |
| H174 | 133 | REASON | Это внешняя валидация: пользователь сразу видит, если эстафета расшифрована неверно | External validation: user sees if decoded wrongly |
| H175 | 133 | RULE | Не пересказывать блок целиком | Do not retell the whole block |
| H176 | 134 | RULE | Пункты с меткой [Г] — гипотезы. Не строить на них выводы без перепроверки | [Г] items are hypotheses; no conclusions on them without re-check |
| H177 | 135 | RULE | Отработать СЛЕДУЮЩИЙ ШАГ, не переизобретать план | Execute NEXT STEP, don't reinvent plan |
| H178 | 136 | RULE | Кто ставит stale: новая сессия — сразу после первого содержательного шага, если она отклонилась от СЛЕДУЮЩЕГО ШАГА или обнаружила, что состояние изменилось | New session sets stale right after first substantive step if deviated from NEXT STEP or found state changed |
| H179 | 136 | RULE | Пользователь — командой эстафета устарела | User sets stale via command "эстафета устарела" |
| H180 | 136 | THRESHOLD | эстафета устарела | Command word "эстафета устарела" |
| H181 | 136 | RULE | Автоматически по 7 дням статус не меняется: срок проверяется при чтении | Status not auto-changed at 7 days; age checked at read time |
| H182 | 138 | THRESHOLD | 7. АНТИ-ПАТТЕРНЫ | Heading section 7: anti-patterns |
| H183 | 139 | RULE | Раздувание. Эстафета > 1 КБ = второй INDEX. Резать по разделу 3 | Bloat: handoff over 1 KB = second INDEX; cut per section 3 |
| H184 | 140 | RULE | Протухание. Блок не обновлён после новых решений, но используется как живой | Staleness: block not updated after new decisions yet used as live |
| H185 | 141 | RULE | Ложная уверенность. Пункт без метки Ф/Г | False confidence: item without Ф/Г label |
| H186 | 142 | RULE | Ссылки вместо фактов. «См. CORE §12» ... Нести добытое значение, а не адрес | Links instead of facts: carry the obtained value, not the address |
| H187 | 142 | REASON | заставляет новую сессию перечитывать дорогой источник — экономии нет | Forces new session to re-read expensive source - no saving |
| H188 | 143 | RULE | Свалка. Всё в одном уровне важности, инварианты не видны | Dump: everything at one importance level, invariants invisible |
| H189 | 144 | RULE | Эстафета вместо INDEX. Задачи живут в Зоне А как задачи; эстафета несёт только то, что нужно для продолжения этой работы | Handoff instead of INDEX: tasks live in Zone A as tasks; handoff carries only what is needed to continue this work |
| H190 | 145 | RULE | Экономия против сохранности. Перенос ради лимитов посреди незавершённой операции. Приоритет обратный | Savings vs safety: handoff for limits mid-operation; priority is the opposite |
| H191 | 147 | THRESHOLD | 8. ГРАНИЦЫ | Heading section 8: boundaries |
| H192 | 148 | RULE | Skill не срабатывает сам и не читается по собственной инициативе | Skill doesn't trigger itself or get read on own initiative |
| H193 | 149 | RULE | Skill не пишет в CORE и CHANGELOG | Skill doesn't write to CORE or CHANGELOG |
| H194 | 149 | REASON | Эстафета — оперативный чекпоинт, не летопись | Handoff is an operational checkpoint, not a chronicle |
| H195 | 150 | RULE | Эстафета живёт в INDEX проекта, где идёт работа. В SYS эстафеты не пишутся | Handoff lives in INDEX of the project where work runs; none written in SYS |
| H196 | 150 | REASON | SYS принимает записи от всех проектов, это общий канал | SYS accepts writes from all projects, it is a shared channel |
| H197 | 151 | RULE | Skill не отменяет !save. Захваты записываются до эстафеты, не вместо неё | Skill does not replace !save; captures written before handoff, not instead |
| H198 | 152 | RULE | Skill не предлагает /compact и /clear | Skill doesn't suggest /compact or /clear |
| H199 | 152 | REASON | в claude.ai и Cowork их нет | They don't exist in claude.ai and Cowork |
| H200 | 153 | EXCEPTION | Проект в repo без Зоны А INDEX: эстафета не пишется отдельным блоком по разделу 3 | Repo project without Zone A INDEX: no separate block per section 3 |
| H201 | 153 | ADDRESS | see second-brain-git §10, «своего INDEX в Docs у repo-проекта нет» | Pointer: second-brain-git §10 (repo project has no own INDEX in Docs) |
| H202 | 153 | RULE | Роль СОСТОЯНИЯ и СЛЕДУЮЩЕГО ШАГА несёт первая строка раздела «Следующий шаг» в STATE.md проекта | Role of СОСТОЯНИЕ and СЛЕДУЮЩИЙ ШАГ carried by first line of "Следующий шаг" section in project STATE.md |
| H203 | 153 | RULE | команда эстафета для такого проекта означает обновить STATE.md по контракту second-brain-git §10.3, а не писать блок ## ЭСТАФЕТА | Command "эстафета" there = update STATE.md per second-brain-git §10.3, not write block |
| H204 | 153 | ADDRESS | second-brain-git §10.3 | Pointer: second-brain-git §10.3 |
| H205 | 153 | RULE | Стоп-линия (раздел 4) и протокол записи (раздел 5, шаги 1–2, 6–7) действуют без изменений | Stop-line and write protocol steps 1-2, 6-7 apply unchanged for repo projects |
| H206 | 153 | EXCEPTION | меняется только пункт 5 («записать заменой») на «записать по контракту second-brain-git §10, п. 8» | Only step 5 changes: write per second-brain-git §10 item 8 |
| H207 | 153 | ADDRESS | second-brain-git §10, п. 8 | Pointer: second-brain-git §10 item 8 |
| H208 | 6 | THRESHOLD | протокол эстафеты между сессиями | (covered by H014) — Skill concept: relay protocol between sessions |

## Coverage
Total units: 208
Per class: ADDRESS=8, CASE=3, CHECK=4, EXCEPTION=6, REASON=24, RULE=85, THRESHOLD=78
Uncovered old-file lines: none (blank lines 1,4,5,16,26,28,97,101-blank,103,111,120,129,137,146 contain no text; line 1 and 4 are frontmatter delimiters)
