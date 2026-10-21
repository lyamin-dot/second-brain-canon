# Verdicts round 1 (avtopilot new text vs old units)

| id | line(s) old | class | verdict | evidence |
|---|---|---|---|---|
| U01 | 2 | THRESHOLD | IN_TEXT | "name: avtopilot" |
| U02 | 3 | RULE | IN_TEXT | "Автопилот — Андрей один раз согласует контракт" |
| U03 | 3 | RULE | IN_TEXT | "дальше сессия ведёт работу до итогового отчёта без него" |
| U04 | 3 | RULE | IN_TEXT | "раздаёт тяжёлое чтение субагентам" |
| U05 | 3 | RULE | IN_TEXT | "пишет в канон сама" |
| U06 | 3 | RULE | IN_TEXT | "сдаёт результат независимой приёмке" |
| U07 | 3 | THRESHOLD | IN_TEXT | "автопилот, делай сам до конца, автономно, без меня" |
| U08 | 3 | THRESHOLD | IN_TEXT | "«Действуй!» в ответ на контракт запуска" |
| U09 | 3 | EXCEPTION | IN_TEXT | "Не читать для быстрой итерации, где Андрей и так отвечает на каждом ша" |
| U10 | 3 | EXCEPTION | IN_TEXT | "и для одиночной операции" |
| U11 | 6 | ADDRESS | IN_TEXT | "# АВТОПИЛОТ" |
| U12 | 8 | THRESHOLD | LOST | New line 8 has only "Редакция 2026-10-21"; version number 1.0 is gone (SKILLS_MAP.md:535 still cites "Версия 1.0") |
| U13 | 8 | CASE | BY_ADDRESS | labs/sys/t-avtopilot-skill.md line 3 "Заведена 2026-10-13 сессией SYS (Аргус)" (checked); new line 12 names the file |
| U14 | 8 | CASE | BY_ADDRESS | pilot task via row AVT.цена -> t-audit-0723-unverified.md at b379506^ (exists, line 27 "Пилот Skill avtopilot") |
| U15 | 8 | ADDRESS | IN_TEXT | "Решение скилла и отвергнутые варианты — `labs/sys/t-avtopilot-skill.md`" (new line 12; file exists) |
| U16 | 8 | THRESHOLD | IN_TEXT | "Владелец — Андрей." |
| U17 | 10 | RULE | IN_TEXT | "Этот Skill не повторяет чужую механику." |
| U18 | 10 | ADDRESS | IN_TEXT | "Ревизия — `denken`." |
| U19 | 10 | ADDRESS | IN_TEXT | "Чтение и запись репозитория — `second-brain-git`." |
| U20 | 10 | ADDRESS | IN_TEXT | "Форма вопроса посреднику — `second-brain-engineer`, правило «Чтение че" |
| U21 | 10 | RULE | IN_TEXT | "Здесь только то, чего нет нигде" |
| U22 | 10 | RULE | IN_TEXT | "кто держит работу, когда Андрея нет рядом, и где она обязана остановит" |
| U23 | 12 | ADDRESS | IN_TEXT | "## Зачем" |
| U24 | 14 | REASON | IN_TEXT | "Каждое короткое «да» Андрея заставляет модель заново обработать весь р" |
| U25 | 14 | REASON | IN_TEXT | "Когда Андрей только соглашается, его реплики ничего не добавляют" |
| U26 | 14 | REASON | IN_TEXT | "а стоят каждый раз дороже предыдущего" |
| U27 | 14 | REASON | IN_TEXT | "Автопилот переносит согласование в одну точку — контракт запуска" |
| U28 | 14 | REASON | IN_TEXT | "и убирает Андрея из роли курьера между исполнителями" |
| U29 | 16 | ADDRESS | IN_TEXT | "## Пять ворот" |
| U30 | 18 | RULE | IN_TEXT | "Работа проходит ворота по порядку." |
| U31 | 18 | RULE | IN_TEXT | "Ворота не пройдены — дальше не идти." |
| U32 | 20 | ADDRESS | IN_TEXT | "### Ворота 1. Разговор — Андрей здесь" |
| U33 | 22 | THRESHOLD | IN_TEXT | "Сессия добивается четырёх вещей, коротко и без лишнего контекста:" |
| U34 | 24 | THRESHOLD | IN_TEXT | "**Квитанция рамки.**" |
| U35 | 24 | RULE | IN_TEXT | "Цели Андрея отдельно, его предположения о способе отдельно" |
| U36 | 24 | THRESHOLD | IN_TEXT | "по каждому предположению — «оставляю» или «предлагаю снять, потому что" |
| U37 | 24 | ADDRESS | IN_TEXT | "метод проектирования, пункт 1, `second-brain-engineer` references/desi" |
| U38 | 25 | RULE | IN_TEXT | "**Критерий приёмки — наблюдаемый объект.**" |
| U39 | 25 | CHECK | IN_TEXT | "Не «проверено», а, например, «по каждому из восьми пунктов вердикт с адресом |
| U40 | 25 | RULE | IN_TEXT | "Критерий без объекта — ворота не пройдены." |
| U41 | 26 | RULE | IN_TEXT | "**Все ручные действия Андрея — одним списком сразу.**" |
| U42 | 26 | THRESHOLD | IN_TEXT | "Это действия, которые сессия сделать не может" |
| U43 | 26 | THRESHOLD | IN_TEXT | "создать Claude Project, привязать ключ доступа в n8n, перезалить Skill" |
| U44 | 26 | THRESHOLD | IN_TEXT | "вставить мастер-промпт, открыть папку сервисному аккаунту" |
| U45 | 26 | RULE | IN_TEXT | "Список собирается в начале, а не всплывает по ходу" (line 30, plus added reason) |
| U46 | 27 | RULE | IN_TEXT | "**Стоп-список** (раздел ниже) дополняется особыми стопами этой работы." |
| U47 | 29 | ADDRESS | IN_TEXT | "### Ворота 2. Ревизия" |
| U48 | 31 | THRESHOLD | IN_TEXT | "Skill `denken`, уровень 2, при необратимой или разрушительной операции" |
| U49 | 31 | RULE | IN_TEXT | "Ревизия идёт по написанному плану." |
| U50 | 31 | RULE | IN_TEXT | "Отдельный пункт ревизии для автопилота: какие шаги действительно незав" |
| U51 | 31 | REASON | IN_TEXT | "Если все шаги строго последовательны, параллельности не будет" |
| U52 | 31 | RULE | IN_TEXT | "это говорится вслух до запуска, а не обнаруживается после" |
| U53 | 33 | ADDRESS | IN_TEXT | "### Ворота 3. Контракт запуска — одно «да»" |
| U54 | 35 | RULE | IN_TEXT | "Контракт — один текст, записанный в канон до исполнения:" |
| U55 | 36 | THRESHOLD | IN_TEXT | "repo-проект — раздел «Контракт автопилота» в `PLAN.md` проекта" |
| U56 | 37 | THRESHOLD | IN_TEXT | "лаборатория — сам файл задачи `t-<имя>.md`" |
| U57 | 38 | EXCEPTION | IN_TEXT | "если записать нельзя — блоком в чате" |
| U58 | 38 | RULE | IN_TEXT | "запись контракта становится первым шагом исполнения" |
| U59 | 40 | THRESHOLD | IN_TEXT | "Поля контракта: цель; критерий приёмки; пакеты работы" |
| U60 | 40 | THRESHOLD | IN_TEXT | "(у каждого — объекты, вопрос, ожидаемый результат-объект, класс модели" |
| U61 | 40 | THRESHOLD | IN_TEXT | "разрешённые правки списком; особые стопы." |
| U62 | 42 | RULE | IN_TEXT | "Список разрешённых правок и есть пакет разрешения" |
| U63 | 42 | ADDRESS | IN_TEXT | "раздел Р10 «Воркфлоу n8n — полномочия», references/permissions.md" (line 46; Р10 exists in permissions.md:7) |
| U64 | 42 | RULE | IN_TEXT | "правка из списка исполняется без повторного «да»" |
| U65 | 42 | EXCEPTION | IN_TEXT | "правка вне списка — снова по общему правилу." |
| U66 | 44 | THRESHOLD | IN_TEXT | "Согласием считается ответ Андрея на контракт: «да», «действуй», «запус" |
| U67 | 44 | RULE | IN_TEXT | "Молчание согласием не считается." |
| U68 | 46 | ADDRESS | IN_TEXT | "### Ворота 4. Исполнение — Андрея нет" |
| U69 | 48 | RULE | IN_TEXT | "**Шина — сессия-диспетчер, а не Андрей.**" |
| U70 | 48 | EXCEPTION | IN_TEXT | "правило Skill `naryad` «Андрей — шина, роли между собой не общаются» н" |
| U71 | 48 | RULE | IN_TEXT | "диспетчер сам раздаёт работу субагентам и сам принимает их ответы" |
| U72 | 48 | RULE | IN_TEXT | "Вне автономного режима `naryad` не меняется" (line 52) |
| U73 | 48 | RULE | IN_TEXT | "Наряды в формате `naryad` внутри автопилота не печатаются" |
| U74 | 48 | REASON | IN_TEXT | "пакет контракта — не наряд" |
| U75 | 50 | ADDRESS | IN_TEXT | "**Когда раздавать субагенту.**" |
| U76 | 50 | CASE | IN_TEXT | Старт одного субагента стоит около 80–110 тысяч токенов; date in "Основание числа: 1 замер, 2026-10-13" |
| U77 | 50 | REASON | IN_TEXT | "почти всё — его собственный стартовый контекст" |
| U78 | 51 | RULE | IN_TEXT | "субагенту отдаётся только тяжёлое чтение, которое нельзя сузить до поп" |
| U79 | 51 | THRESHOLD | IN_TEXT | "полный граф воркфлоу, длинная выдача внешнего API, большая пачка файло" |
| U80 | 52 | RULE | IN_TEXT | "лёгкий шаг (одно чтение файла, одно число, одна запись) диспетчер дела" |
| U81 | 53 | RULE | IN_TEXT | "объекты группируются так, чтобы один старт обслуживал два-три объекта" (line 57; "по субагентам" dropped, meaning same) |
| U82 | 53 | CASE | IN_TEXT | "девять объектов на четыре субагента" |
| U83 | 54 | RULE | IN_TEXT | "независимые пакеты запускаются одним сообщением" |
| U84 | 54 | REASON | IN_TEXT | "тогда они идут параллельно" |
| U85 | 56 | THRESHOLD | IN_TEXT | "**Что умеет субагент**" |
| U86 | 56 | CASE | BY_ADDRESS | row AVT.зонд-субагента -> t-avtopilot-skill.md "Замеры 2026-10-13" line 36 contains "исполнение n8n 79581" (checked) |
| U87 | 56 | THRESHOLD | IN_TEXT | "Есть: инструменты n8n, Канал чтения репозитория, память, Google Drive" |
| U88 | 56 | THRESHOLD | IN_TEXT | "Нет: запуска своих субагентов — глубина одна, как в `naryad`." |
| U89 | 58 | RULE | IN_TEXT | "**Задание субагенту** — вопрос, а не файл" |
| U90 | 58 | ADDRESS | IN_TEXT | "по форме посредника (`second-brain-engineer`, Р21 «Чтение через посред" |
| U91 | 58 | THRESHOLD | IN_TEXT | "вопрос без ожидаемого ответа, адрес доказательства при каждом факте," |
| U92 | 58 | THRESHOLD | IN_TEXT | "NOT_FOUND со списком мест, вопросы пакетом" |
| U93 | 59 | RULE | IN_TEXT | "по умолчанию только чтение, и это написано в задании словами" |
| U94 | 59 | THRESHOLD | IN_TEXT | "«READ-ONLY, ничего не менять»" |
| U95 | 60 | RULE | IN_TEXT | "у вопроса закрытый набор вердиктов" |
| U96 | 60 | THRESHOLD | IN_TEXT | "(например, ЖИВ / ИСПРАВЛЕН / ИЗМЕНЁН)" |
| U97 | 61 | RULE | IN_TEXT | "задание пишется на английском и компактно" |
| U98 | 61 | REASON | IN_TEXT | "субагент его читает, Андрей нет" |
| U99 | 63 | RULE | IN_TEXT | "**Пишет в канон только диспетчер.**" |
| U100 | 63 | REASON | IN_TEXT | "Так нет гонки записи внутри прогона" |
| U101 | 63 | REASON | IN_TEXT | "и правила записи `second-brain-git` читает одна сессия, а не каждая" |
| U102 | 63 | RULE | IN_TEXT | "Правила, которые диспетчер исполняет сам, он читает сам, а не через по" |
| U103 | 65 | RULE | IN_TEXT | "**Перед правкой воркфлоу n8n** диспетчер перечитывает время последнего" |
| U104 | 65 | THRESHOLD | IN_TEXT | "(updatedAt)" |
| U105 | 65 | CHECK | IN_TEXT | "сверяет его с прочитанным в начале" |
| U106 | 65 | RULE | IN_TEXT | "Расхождение — стоп" |
| U107 | 65 | REASON | IN_TEXT | "воркфлоу правит параллельная сессия" |
| U108 | 65 | REASON | IN_TEXT | "а правка в n8n перезаписывает граф без проверки версии" |
| U109 | 65 | ADDRESS | IN_TEXT | "(`labs/sys/t-n8n-workflow-race.md`)" |
| U110 | 67 | THRESHOLD | IN_TEXT | "Долгое ожидание** (прогон воркфлоу на десятки минут" (scope widened, see EXTENDED) |
| U111 | 67 | RULE | WEAKENED | Return-to-same-session was THE carrier; new line 73 makes it one of two carriers, used only "когда продолжать должна та же сессия" (deliberate, per probe 2026-10-18) |
| U112 | 67 | CASE | IN_TEXT | "Основание: 5 срабатываний, последнее до 2026-10-13" (line 73) |
| U113 | 67 | CASE | IN_TEXT | new line 75 keeps it as superseded history: "ни разу не создавалась ... так было до 2026-10-18" |
| U114 | 67 | REASON | IN_TEXT | "Режим одобрения задачи называет ответ на её создание" (line 74; reason "unknown until creation" restated) |
| U115 | 67 | RULE | WEAKENED | Old: scheduled task only after a separate probe. New line 74: probe done, usable as carrier if approval mode is auto (condition replaced; deliberate, supported by t-avtopilot-skill.md probe section) |
| U116 | 67 | ADDRESS | IN_TEXT | "`labs/sys/t-avtopilot-skill.md`" (line 12) and probe section "Зонд запланированной задачи" exists there |
| U117 | 69 | RULE | IN_TEXT | "**Массовая механическая работа** — скриптом, а не моделью" |
| U118 | 69 | ADDRESS | IN_TEXT | "`second-brain-engineer`, references/design.md, пункт 17" |
| U119 | 69 | ADDRESS | IN_TEXT | "для файлов репозитория — `second-brain-git` 9.4(б)" |
| U120 | 71 | ADDRESS | IN_TEXT | "### Ворота 5. Приёмка и отчёт" |
| U121 | 73 | RULE | IN_TEXT | "**Приёмку делает отдельный субагент сильного класса, который работу не" |
| U122 | 73 | RULE | IN_TEXT | "Он получает утверждения в виде списка проверяемых фраз и задачу их опр" |
| U123 | 73 | RULE | IN_TEXT | "Отчёты исполнителей и рассуждения диспетчера ему не передаются" (line 81) |
| U124 | 73 | CASE | BY_ADDRESS | row AVT.приёмщик -> projects/archive-recon/STATE.md (commit 2375562, 2026-10-13) (checked) |
| U125 | 73 | ADDRESS | BY_ADDRESS | same row; STATE.md exists (checked) |
| U126 | 73 | CASE | BY_ADDRESS | STATE.md line 53 contains "независимую проверку делает агент с моделью opus, запускаемый из сессии" (checked) |
| U127 | 74 | RULE | IN_TEXT | "Вопросы приёмки составляет не исполнитель" |
| U128 | 74 | RULE | IN_TEXT | "исправления по находке приёмщика проверяет повторно приёмщик" |
| U129 | 74 | ADDRESS | IN_TEXT | "(`second-brain-engineer`, references/design.md, пункт 14, г и д)" |
| U130 | 76 | RULE | IN_TEXT | "**Находки приёмщика сверх вопроса — гипотезы.**" |
| U131 | 76 | THRESHOLD | IN_TEXT | "Они идут в канон словом «Гипотеза (не проверена):»" |
| U132 | 76 | RULE | IN_TEXT | "пока диспетчер не проверил их по объекту" |
| U133 | 76 | CASE | BY_ADDRESS | generalized in new line 84 ("Признак"); specifics in row AVT.гипотеза; t-audit-0723-unverified.md at b379506^ line 41 has the "/**" unclosed comment hypothesis (checked) |
| U134 | 76 | CASE | BY_ADDRESS | same line 41: run 72481 failed on first node 01_Sheets_Read_URL_List, Google credential (checked) |
| U135 | 76 | CASE | IN_TEXT | "значит, по прогону причина не проверена" |
| U136 | 78 | RULE | IN_TEXT | "**Критерий приёмки не смягчается**" |
| U137 | 78 | ADDRESS | IN_TEXT | "(метод проектирования, пункт 15)" |
| U138 | 78 | THRESHOLD | IN_TEXT | "Не выполнен — итог «не выполнено, вот почему»." |
| U139 | 80 | RULE | IN_TEXT | "Затем диспетчер пишет результат в канон" |
| U140 | 80 | CHECK | IN_TEXT | "проверяет запись обратным чтением" |
| U141 | 80 | THRESHOLD | IN_TEXT | "выдаёт Андрею один отчёт: проблема, причина, что сделано, что сделать " |
| U142 | 80 | RULE | IN_TEXT | "Без пересказа шагов." |
| U143 | 82 | ADDRESS | IN_TEXT | "## Стоп-список — где работа останавливается сама" |
| U144 | 84 | RULE | IN_TEXT | "Остановка — сообщение Андрею с тем, на чём встало, и с подготовленным " |
| U145 | 84 | RULE | IN_TEXT | "Не тихое ожидание." |
| U146 | 86 | RULE | IN_TEXT | "Нужно действие из списка ручных действий Андрея, а он его не сделал." |
| U147 | 87 | RULE | IN_TEXT | "Нужно необратимое решение, которое разумно принять в обе стороны." |
| U148 | 88 | RULE | IN_TEXT | "Меняется цель или предмет работы." |
| U149 | 88 | CASE | BY_ADDRESS | new line 96 generalizes; row AVT.цель -> projects/archive-recon/LOG.md Р-14 "цель проекта archive-recon переопределена" (checked) |
| U150 | 88 | CASE | BY_ADDRESS | new line 96 "цель приходится переопределять задним числом"; row AVT.цель |
| U151 | 88 | ADDRESS | BY_ADDRESS | row AVT.цель lists Р-13 (2026-09-27) and Р-14; both exist in LOG.md (checked) |
| U152 | 89 | RULE | IN_TEXT | "Правка нужна вне списка разрешённых." |
| U153 | 90 | RULE | IN_TEXT | "Два круга правок без сходимости — стоп-линия `denken`." |
| U154 | 90 | ADDRESS | IN_TEXT | "стоп-линия `denken`" |
| U155 | 91 | RULE | IN_TEXT | "Жёсткий барьер: политика, закон, ограничение платформы." |
| U156 | 91 | THRESHOLD | IN_TEXT | "политика, закон, ограничение платформы" |
| U157 | 92 | RULE | IN_TEXT | "Время последнего изменения воркфлоу разошлось с прочитанным в начале." |
| U158 | 93 | RULE | IN_TEXT | "Критерий приёмки не выполнен." |
| U159 | 95 | RULE | IN_TEXT | "Находка вне рамки контракта работу не прерывает." |
| U160 | 95 | ADDRESS | IN_TEXT | "Она идёт захватом по правилу мастер-промпта проекта" |
| U161 | 95 | RULE | IN_TEXT | "объектный блокер — сразу, кандидат и мелочь — на !save" |
| U162 | 97 | ADDRESS | IN_TEXT | "## Чего этот Skill не делает" |
| U163 | 99 | RULE | IN_TEXT | "Не заводит мониторов, сигналов живости и журналов наблюдения за автопи" |
| U164 | 100 | RULE | IN_TEXT | "Не меняет `naryad` вне автономного режима." |
| U165 | 101 | RULE | IN_TEXT | "Не разрешает правку Skill, мастер-промпта, удаление данных или правку " |
| U166 | 101 | EXCEPTION | IN_TEXT | "без контракта, где они названы" |
| U167 | 102 | RULE | IN_TEXT | "Не считает ответ субагента записью в канон" |
| U168 | 102 | RULE | IN_TEXT | "в канон идёт то, что диспетчер прочитал сам" |
| U169 | 102 | RULE | IN_TEXT | "вердикт приёмщика входит в канон, когда диспетчер сам прочитал адрес" |
| U170 | 102 | THRESHOLD | IN_TEXT | "(одна строка файла, одно поле ответа инструмента)" |
| U171 | 102 | RULE | IN_TEXT | "без этого он гипотеза" |
| U172 | 102 | ADDRESS | IN_TEXT | "(`second-brain-engineer`, Р21, ПРОВЕРКА)" |
| U173 | 104 | ADDRESS | BY_ADDRESS | heading removed; row AVT.цена cites "прежний раздел Skill «Цена пилота 2026-10-13»" at commit f4f4a49 (exists, section present). SKILLS_MAP.md:130 still names the heading |
| U174 | 106 | CASE | BY_ADDRESS | row AVT.цена -> t-audit-0723-unverified.md at b379506^ line 3 "Восемь дефектов аудита 2026-07-23" (checked) |
| U175 | 107 | CASE | BY_ADDRESS | row AVT.цена: 433 329 (in text of report row); t-avtopilot-skill.md line 38 (checked) |
| U176 | 108 | CASE | BY_ADDRESS | row AVT.цена: 185 402; t-avtopilot-skill.md line 38 (checked) |
| U177 | 109 | CASE | IN_TEXT | "между согласием и итоговым отчётом от Андрея не требуется ни одного сообщения" |
| U178 | 111 | CASE | IN_TEXT | "сколько стоила бы та же работа без автопилота — сравнения нет" |

## (c) Headings
All present verbatim: "Пять ворот" (l.20), "Ворота 1. Разговор — Андрей здесь" (24), "Ворота 2. Ревизия" (33), "Ворота 3. Контракт запуска — одно «да»" (37), "Ворота 4. Исполнение — Андрея нет" (50), "Ворота 5. Приёмка и отчёт" (79), "Стоп-список — где работа останавливается сама" (90), "Чего этот Skill не делает" (105), bold "Когда раздавать субагенту." (54). Not present: "Цена пилота 2026-10-13" (U173, removed by design; content moved to row AVT.цена).

## (a) Knowledge in OLD missing from the table
None found on full re-read.

## (b) EXTENDED (new text asserts beyond old)
- l.12 whole paragraph "Как устроен этот текст" (four-part rule structure, Основание format, report pointer, commit-history pointer, PROTOCOL_knowledge-synthesis rule "урок не дописывается, кластер переписывается правилом").
- l.8 "Редакция 2026-10-21".
- l.18 "Что измерено: ... Чего не измерено: ..." (restates old pilot facts as a rule-block).
- l.30 "действие, о котором Андрей узнал посреди прогона, останавливает работу, которая шла без него" (new reason).
- l.35 "тогда экономия автопилота сводится к отсутствию промежуточных «да» Андрея" (new reason; from task file).
- l.46 "раздел Р10 ... references/permissions.md" (more precise address).
- l.52 "обратная оговорка стоит в самом `naryad`, раздел «2. Роли»" (exists: naryad line 36); "Почему исключение, а не новый маршрут внутри `naryad`..."; "Цена исключения — пропадает взгляд Андрея между шагами; её компенсирует независимая приёмка" (from t-avtopilot-skill.md Решение).
- l.61 "Поэтому работа, которой нужен второй уровень раздачи, раздаётся диспетчером, а не субагентом" (new rule).
- l.72 "или работа, которую нужно продолжить на следующий день" (widened scope of Долгое ожидание).
- l.73 "Берётся, когда продолжать должна та же сессия, с её контекстом" (new condition).
- l.74 whole second carrier: "Свежая сессия не помнит разговора диспетчера, поэтому её задание пишется самостоятельным текстом..."; "если там не auto, такую задачу носителем автопилота не делать" (new RULE; basis "по описанию инструмента ... одобрить некому (зондом не проверялось)"); "Зонд не проверял правку воркфлоу n8n и запуск субагентов из такой сессии — для этих двух действий она гипотеза" (matches probe section).
- l.75 "Не путать: ..." paragraph (history of refuted claim).
- l.81 "приёмщик, прочитавший чужой вывод, ищет доводы за него" (new reason).
- l.84 "Признак: приёмщик называет причину отказа воркфлоу..." (generalized case as criterion).
- l.96 "Признак: делается уже не то, что записано целью в контракте" (new criterion).
- Основание lines l.18, 35, 52, 59, 61, 73, 74, 81, 84, 96.

## Address check
Repository clone is /root/sbc (not /home/claude/sbc, which holds only meta/ with the report). All report-table addresses exist and contain the claimed facts: t-avtopilot-skill.md sections (Решение, Замеры, Зонд), STATE.md line 53 (opus quote), LOG.md Р-13/Р-14, deklaration-v2 LOG Р-27/Р-28, HARVEST В11, maintenance-queue AJ-6, edits/avtopilot.md+json, commits b379506^, f4f4a49 (blob 6576d1d), 2375562, t-audit-0723-unverified.md at b379506^ (lines 3, 27, 41). Minor: row AVT.цель says Р-13 as case of goal redefinition; Р-13 is the document/work mismatch, the redefinition itself is Р-14 (Andrei chose explicitly). Outside scope: meta/SKILLS_MAP.md lines 130, 535 still cite the removed heading "Цена пилота" and "Версия 1.0".

## Round 2
- U12 ("Версия 1.0."): BY_ADDRESS. Report paragraph "Шапка." quotes the old header line and names commit f4f4a49 and first mirror commit ae310c9; both exist and line 8 of SKILL.md in each begins "Версия 1.0. Создан 2026-10-13 сессией SYS (Аргус)". The version number is a CASE-like fact, so BY_ADDRESS is admissible. (Out of scope: meta/SKILLS_MAP.md:535 still cites it.)
- U111 and U115: CHANGED_BY_LESSON. I agree. The old claims (scheduled task with fresh session never created, carrier only after a probe) were refuted by the 2026-10-18 probe, which is documented in labs/sys/t-avtopilot-skill.md ("Зонд запланированной задачи 2026-10-17…18"), DEKL LOG Р-27/Р-28 and HARVEST В11/AJ-6. New-text quotes: U111 "отложенное сообщение самому себе — возврат в ту же сессию. Берётся, когда продолжать должна та же сессия" (l.73); U115 "Режим одобрения задачи называет ответ на её создание; если там не auto, такую задачу носителем автопилота не делать" (l.74). The refuted claim is kept in "Не путать" (l.75) and in full at f4f4a49. Caveat: the stated "если не auto -> не делать" rule is itself new, based on a tool description and marked "зондом не проверялось"; it is listed under EXTENDED, not hidden.
- AVT.цель row: OK. Row now says Р-14 is the redefinition (ЧАСТИЧНО ОТМЕНЕНО Р-17 in the goal part) and Р-13 is context (2026-09-27); matches LOG.md (Р-13 line 73, Р-14 line 84). U149, U150, U151 stay BY_ADDRESS.
- Other BY_ADDRESS units: no breakage. Rows AVT.цена, решение, замер-старта, зонд-субагента, ожидание, задача, приёмщик, гипотеза all still present; figures 433 329, 185 402 and execution 79581 still in the report.
