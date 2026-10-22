# V3 — проверка вердиктов «уже есть» (харвест 2026-10-22)

Проверяющий: независимый субагент, вердиктов не выносил. Метод: протокол `meta/PROTOCOL_lesson-triage.md`, пункт А2; раздел 4 `meta/PLAN_skill-layers_2026-10-20_v3.md`. Поиск по смыслу (несколько формулировок) в живых Skills `/mnt/skills/plugins/<имя>/`, в `meta/`, `core/`, `registry/` клона; найденный абзац прочитан целиком. Код воркфлоу не читался. Адреса: путь от `/mnt/skills/plugins/` для Skills, от корня клона для `meta/`, `core/`, `registry/`. Номера строк — по живым файлам на 2026-10-22.

Как читать вердикты: ПОДТВЕРЖДЁН — найденный абзац описывает тот же механизм. ЧАСТИЧНО — механизм описан не весь, разница названа. ОПРОВЕРГНУТ — механизма нет, урок нужно выносить. СПОРНО — урок расходится с действующим правилом.

| id | вердикт | адрес / довод |
|---|---|---|
| M1a#1 | ПОДТВЕРЖДЁН | second-brain-engineer/SKILL.md:106 — причинное объяснение = гипотеза до пробы, в которой меняется только предполагаемая причина |
| M1a#5 | ПОДТВЕРЖДЁН | second-brain-git/SKILL.md:60 (И-7) — запрет по классам данных; история коммитов не очищается |
| M1a#7 | ПОДТВЕРЖДЁН | second-brain-engineer/references/permissions.md:15, :18 — «реши сам» в пределах задачи, только обратимое |
| M1a#11 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/templates.md:220 (T4.10.2); references/roots.md:93 (R2.5) |
| M1a#14 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/templates.md:221 (T4.10.3); references/write.md:21 |
| M1a#17 | ЧАСТИЧНО | Есть: second-brain-git/references/write.md:15–19 (пункт 2.5 «Перенумерация»: ссылка, ведущая не туда) и :30 (приёмка правки Skill по якорям); roots.md:404 записывает сам исправленный случай R2→R4 как основание. Нет: общего правила «перекрёстные ссылки на корни и пункты проверяются по смыслу при приёмке правки» — 2.5 срабатывает только при сдвиге номера, а случай R2/R4 — неверная ссылка без перенумерации |
| M1a#18 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:246 «Форма — вход того же класса»; references/write.md:28 |
| M1a#22 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:299–300 (R19: ноль и запасная константа — не «неизвестно») |
| M1a#56 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:106 (R3: «create» на существующем листе — 0 items) |
| M1a#59 | ЧАСТИЧНО | Есть: n8n-workflow-passport/SKILL.md:84–85 (паспорт создаётся с parentId папки DOCS); google-drive-docs/references/mcp.md:35–40 (проверка после create_file в три шага). Нет: шага «после create_file проверить родителя через get_file_metadata (parentId)» — проверка после вызова сверяет id и содержимое, но не папку, а пять паспортов легли не в ту папку именно так |
| M1a#60 | ПОДТВЕРЖДЁН | second-brain-git/references/write.md:111–115 (5.5: превышение бюджета — не проблема, критерий — содержание; закрытое уходит в журнал разбором 5.1) |
| M1a#63 | ПОДТВЕРЖДЁН | meta/prompts/sys.md:5 и шапки других зеркал «Резерв, не канон: живой экземпляр — в интерфейсе»; second-brain-git/SKILL.md:86 |
| M1a#64 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:243 (отдельный ключ вебхука, не общий ключ другого назначения); references/templates.md:179 (T3.6: общий ключ — ротация бьёт по всем) |
| M1a#66 | ПОДТВЕРЖДЁН | n8n-engineering-manual/SKILL.md:14 (состояние в Skill не пишется); references/templates.md:159 (T2.4.9: покрытие считать заново по снимку) |
| M1a#80 | ПОДТВЕРЖДЁН | second-brain-engineer/references/save.md:51 — адрес класса ошибки по носителю: Docs → Зона Б, репозиторий → PLAN.md, лаборатория → файл задачи |
| M1a#81 | ПОДТВЕРЖДЁН | naryad/references/issuer.md:50 «CORE Р.5 — не реестр блокеров, строк-задач в нём нет» |
| M1a#82 | ЧАСТИЧНО | Есть: second-brain-git/references/delivery.md:84 (коммит в ветке claude/* не доставка), :106 (ветка, не переведённая в main, — незакрытая доставка). Нет: «отсутствие патча в main не доказывает ни потерю, ни доставку — сверять каждую строку» и «перед удалением ветки, на которую ссылается журнал, ставить тег» |
| M1a#84 | ПОДТВЕРЖДЁН | avtopilot/SKILL.md:61 (глубина одна), :54 (старт 80–110 тыс.), :35 (строго последовательные шаги — параллельности нет) |
| M1b#12 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/write.md:86; SKILL.md:149; n8n-workflow-passport/SKILL.md:152 — снять с публикации, не архивировать |
| M1b#13 | ПОДТВЕРЖДЁН | naryad/references/issuer.md:75 (поле наряда, заполняемое по памяти, а не по прочитанному, → маршрут А, первое действие — чтение); second-brain-engineer/references/write-moment.md:13 |
| M1b#19 | ПОДТВЕРЖДЁН | second-brain-engineer/references/write-moment.md:14, :20 — число критерия только из чтения объекта до записи критерия |
| M1b#20 | ПОДТВЕРЖДЁН | second-brain-engineer/references/design.md:54 (каждая запись — независимым обратным чтением); core/R-06a.md:59 (0.4) |
| M1b#22 | ПОДТВЕРЖДЁН | apps-script-sheets/references/book-traps.md:59 — диапазон до фиксированной строки недосчитывает молча |
| M1b#23 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/templates.md:237 — повтор фразы с названием объекта после показа проверки = «да» (решение Андрея внесено) |
| M1b#36 | ПОДТВЕРЖДЁН | second-brain-git/references/write.md:58–75 (4.5 и исключение: создание и закрытие задачи); context-handoff/SKILL.md:196–198 (пометка «активная эстафета», правка фрагментом) |
| M1b#38 | ПОДТВЕРЖДЁН | core/MANIFEST.md:47 (строка «запись в файлы репозитория» → абзац «ОБЛАСТЬ ДЕЙСТВИЯ»); core/R-06-marshrut.md:13 |
| M1b#51 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/templates.md:158 (T2.4.8) |
| M1b#54 | ЧАСТИЧНО | Есть: n8n-engineering-manual/SKILL.md:136 — бэкап без N8N_ENCRYPTION_KEY не восстанавливает ключи доступа. Нет: правила «полноту бэкапа проверять вопросом «чего не хватит для восстановления»» (общий метод для любого бэкапа). Где лежит ключ на нашем сервере — особенность объекта (В0), в Skill не нужна |
| M1b#57 | ПОДТВЕРЖДЁН | google-drive-docs/references/infra.md:24; references/failures.md:30 (E22) |
| M1b#65 | ПОДТВЕРЖДЁН | google-drive-docs/SKILL.md:83, :95; registry/tools.md:49 — имя скрыто «***», ID брать из registry/tools.md |
| M1b#66 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/engine.md:102 (4.8.15) |
| M1b#74 | ПОДТВЕРЖДЁН | docx/SKILL.md:47; pptx/SKILL.md:264 (живые Skills; в Skills второго мозга нет, но правило живёт там, где pdftoppm применяется) |
| M1b#75 | ЧАСТИЧНО | Есть: (а) R5 неподключённый выход ошибки — roots.md (R5); общий ретрай — templates.md:112–129 (T2.1). Нет: (б) «три повтора с паузой около секунды не переживают занятость сервиса — ждать освобождения на стороне сервиса, а не отвечать 503 сразу» — T2.1.3 говорит о транзиентных сбоях и квоте 429, не о длине паузы против занятого сервиса; (в) ошибка наряда «узел 08 недостижим» — исходный отчёт сам пометил «НОВЫЙ» (meta/HARVEST_2026-10-18_reports/G10.md:30) |
| M1b#77 | ЧАСТИЧНО | Есть: приёмка по объекту — naryad/SKILL.md:182; second-brain-engineer/references/design.md:54. Нет в Skills: «файл данных JSON перед слиянием проверять разбором (типографские кавычки ломают формат)» — найдено только строкой Х-43 в meta/LESSONS_waiting.md:77. По А2 совпадение со списком ожидающих — не «уже есть», а новый случай: встречаемость Х-43 +1, урок возвращается в отбор |
| M1b#82 | ПОДТВЕРЖДЁН | meta/CASES_wb-api-card-write.md:11, :88; meta/PROTOCOL_wb-card-write.md (раздел о приёмке) |
| M1b#93 | ПОДТВЕРЖДЁН | second-brain-engineer/references/design-acceptance.md:14 (п.14а «Эталон приходит путём, независимым от проверяемого») |
| M1b#102 | ПОДТВЕРЖДЁН | (а) design-acceptance.md:22 (п.14г); (б) naryad/references/executor.md:78; (в) second-brain-engineer/SKILL.md:109, google-drive-docs/references/mcp.md:50 |
| M1b#102в | ПОДТВЕРЖДЁН | дубль строки M1b#102 — те же адреса |
| M1b#111 | ПОДТВЕРЖДЁН | meta/PROTOCOL_lesson-triage.md:31–59 (А1–А5); meta/PROTOCOL_harvest.md:39 (граница окна), :44 (полное чтение без отсечки) |
| M1c#E1 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/engine.md:46 (4.2.10) |
| M1c#E5 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:168 |
| M1c#E9 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:24 (addNode с credentials), :31 (renameNode сохраняет привязку) |
| M1c#E10 | ПОДТВЕРЖДЁН | n8n-engineering-manual/SKILL.md:130; references/templates.md:148 |
| M1c#E13 | ПОДТВЕРЖДЁН | n8n-engineering-manual/SKILL.md:44 (A1 — закрытая константа; слов «десятки раз» в тексте нет) |
| M1c#E16 | ПОДТВЕРЖДЁН | second-brain-engineer/SKILL.md:107 (строка «Описание объекта») |
| M1c#E19 | ПОДТВЕРЖДЁН | second-brain-engineer/references/design-acceptance.md:22–23 (п.14г); avtopilot/SKILL.md:81–82 |
| M1c#E20 | ПОДТВЕРЖДЁН | second-brain-engineer/references/design-acceptance.md:25–26 (п.14д) |
| M1c#E21 | ПОДТВЕРЖДЁН | second-brain-engineer/references/save.md:51 — адрес по носителю и перенос превентива до удаления файла задачи (открытый вопрос урока закрыт) |
| M1c#E24 | ПОДТВЕРЖДЁН | second-brain-git/references/write.md:221 и таблица под ним |
| M1c#E25 | ПОДТВЕРЖДЁН | context-handoff/SKILL.md:196 |
| M1c#E26 | ПОДТВЕРЖДЁН | second-brain-git/SKILL.md:194, :203 (contextData — свойство типа узла, параметрами вызова не режется) |
| M1c#E27 | ПОДТВЕРЖДЁН | naryad/SKILL.md:16, :18 (Летописи), :36 (автономный режим — шина-диспетчер, контракт один раз) |
| M1c#E30 | ПОДТВЕРЖДЁН | meta/PROTOCOL_knowledge-synthesis.md:78 (С4а: правило живёт в файле по своему триггеру, читаемом перед действием) |
| M1c#C1 | ПОДТВЕРЖДЁН | second-brain-engineer/references/save.md:28 (8в — поиск по оглавлению журнала перед записью решения) |
| M1c#C3 | ПОДТВЕРЖДЁН | second-brain-git/references/migration.md:72 (13.4 (в) контрольный набор вопросов) |
| M1c#C23 | ЧАСТИЧНО | Есть: naryad/SKILL.md:52 «Наряд печатается ВСЕГДА целиком» — про поля при печати. Нет: «уже выданный наряд не поправляется частями (дополнением, сообщением "исправь поле X"), только перевыпуском целиком». Поиск «перевыпуск», «частями», «выданный» по naryad пуст |
| M1c#C26 | ПОДТВЕРЖДЁН | (а) meta/PROTOCOL_harvest.md:46 (А5: стадию А — отдельная сессия); (б) n8n-engineering-manual/references/roots.md:87 (R2.2) |
| M1c#C45 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/templates.md:239 (T5.1) |
| M1c#C66 | ЧАСТИЧНО | Есть: две версии (русская и английская для агента) — только для мастер-промптов (second-brain-engineer/references/prompt-craft.md:72, :98) и для задания субагенту (avtopilot/SKILL.md:66); файлы meta/CASES_wb-api-card-write.md:5 и meta/PROTOCOL_wb-card-write.md:5 так устроены по факту. Нет: правила «находки для использования вне проекта — отдельным файлом в meta/ с английской копией для агента» (в предпочтениях Андрея есть, в Skills — нет) |
| M1c#C69 | ЧАСТИЧНО | Есть: meta/PROTOCOL_harvest.md:17 (харвест читает meta/HARVEST_INPUT_<дата>.md целиком); avtopilot/SKILL.md:109 (без контракта Skill не правится). Нет: правила для пишущей стороны — «во время автопилота тексты правок Skills копятся в meta/HARVEST_INPUT_*.md» |
| M1c#C72 | ПОДТВЕРЖДЁН | apps-script-sheets/references/signal.md:132–134 (порог возраста от ритма прихода данных и нормального возраста метки) |
| M1c#C74 | ПОДТВЕРЖДЁН | apps-script-sheets/SKILL.md:96 (разделитель — опытом в самой книге, §0.2); :16 (разделитель книги — особенность, в Skill не пишется) |
| M1c#3-12 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:254 |
| M1c#3-32 | ПОДТВЕРЖДЁН | apps-script-sheets/references/book-traps.md:111–113 (3.7 п.4) |
| M1c#3-39 | СПОРНО | Половина урока («clasp push заменяет проект целиком») есть — apps-script-sheets/SKILL.md:64. Первая половина («код доставлять через clasp на компьютере Андрея, API закрыт сервисным аккаунтам») расходится с действующим правилом: основной путь — мост gas-bridge ключом Андрея, clasp — аварийный путь только руками Андрея, сессия через clasp не пишет (SKILL.md:64, :66 «Не путать»). Выносить урок в таком виде нельзя — он устарел; вносить нечего |
| M1c#3-40 | ПОДТВЕРЖДЁН | apps-script-sheets/SKILL.md:272–274 (2.8) |
| M1c#3-41 | ЧАСТИЧНО | Есть: формулы «;» и локаль — SKILL.md:33, :89–96; пояс Date — SKILL.md:256–266 (2.7); жёсткие границы — book-traps.md:59; setConditionalFormatRules заменяет все правила — SKILL.md:290. Нет (урок сам это называет, поиск подтвердил): autoResizeColumn(1) и Number(x) — в apps-script-sheets совпадений нет |
| M1c#4-7 | ПОДТВЕРЖДЁН | google-drive-docs/references/sheets.md:11; apps-script-sheets/SKILL.md:300–302 |
| M1c#4-8 | ПОДТВЕРЖДЁН | apps-script-sheets/references/book-traps.md:152; n8n-engineering-manual/references/roots.md:166 (R6.4), :208 |
| M1c#4-11 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/write.md:33 (читающему — ключ только на чтение) |
| M1c#6-2 | ПОДТВЕРЖДЁН | google-drive-docs/references/mcp.md:63; references/failures.md:50 |
| M1c#6-10 | ЧАСТИЧНО | Есть: avtopilot/SKILL.md:28 (критерий приёмки — наблюдаемый объект); design-acceptance.md:22 упоминает «вопросы приёмочного теста». Нет: правила «результат готов, когда им можно пользоваться по назначению (приёмочный тест на назначение), собранные данные — ещё не результат» (так же оценил исходный отчёт G6.md:43) |
| M1c#6-13 | ОПРОВЕРГНУТ | Правила «в облачной сессии путь клона проверять, а не предполагать» нет: поиск «путь клона», «клон лежит», «облачн», «/home/claude» в second-brain-git, second-brain-engineer, avtopilot, context-handoff даёт только delivery.md:54, :59 (push в облачной сессии) — другой механизм. Общее Р15 о идентификаторах (write-moment.md:13) касается записи в канон, не рабочих путей среды |
| M1c#6-16 | ПОДТВЕРЖДЁН | second-brain-engineer/references/intermediary.md:25; avtopilot/SKILL.md:84; meta/PROTOCOL_harvest.md:44 («каждый вердикт "новый урок" основная сессия перепроверяет сама») |
| M1c#6-17 | ПОДТВЕРЖДЁН | second-brain-engineer/references/design.md:42 (п.4 обязательный поиск прецедента и существующего инструмента); second-brain-engineer/SKILL.md:109 (утверждение об отсутствии, в том числе «читателя нет», — только после поиска в носителе) |
| M1c#6-21 | ПОДТВЕРЖДЁН | meta/PROTOCOL_lesson-triage.md:31 (А1, разделение склеенного урока); meta/PROTOCOL_knowledge-synthesis.md:50; n8n-engineering-manual/SKILL.md:14 (строка «Основание» у каждого правила) |
| M1c#8-1 | ПОДТВЕРЖДЁН | apps-script-sheets/SKILL.md:400–405 (4.9); n8n-engineering-manual/references/templates.md:225 (T4.10.4) |
| M1c#8-2 | ЧАСТИЧНО | Механизм «срыв через раз, метка одного дня ничего не доказывает» есть: apps-script-sheets/SKILL.md:405–411 (основание «перемежающийся срыв»). Средство в Skill другое, по решению Андрея 2026-10-21: вместо «серии дней» — встроенная внешняя проверка возраста метки, «сначала встраивается проверка, а не считаются дни». Вносить «нужна серия дней» нельзя — противоречит действующему правилу |
| M1c#8-3 | ПОДТВЕРЖДЁН | apps-script-sheets/references/signal.md:128 «Кто проверяет возраст — внешний исполнитель, не сама книга» |
| M1c#8-8 | ЧАСТИЧНО | Есть: доля выручки в п.п. — signal.md:48–50 (9.3); прогон по истории — signal.md:83–85 (9.6). Нет: «норма — медиана нескольких недель, а не среднее» (слова «медиан» в apps-script-sheets нет) и «жёлтое — только в недельную сводку, не в тревогу» |
| M1c#8-15 | ПОДТВЕРЖДЁН | denken/SKILL.md:64 «Показание к операции» — наблюдаемый факт об объекте, до первого наряда |
| M1c#8-19 | ПОДТВЕРЖДЁН | n8n-workflow-passport/SKILL.md:90, :93 |
| M1c#9-2 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:289 (R18) |
| M1c#9-16 | ПОДТВЕРЖДЁН | meta/CASES_wb-api-card-write.md:125–131 «Как проверять запись»; meta/PROTOCOL_wb-card-write.md |
| M1c#9-20 | ЧАСТИЧНО | Есть: «прав живой объект, расхождение — в отчёт» только для мастер-промпта (second-brain-engineer/references/prompt-craft.md:35, :50); для решений по описанию объекта — second-brain-engineer/SKILL.md:107. Нет общего правила для любого файла канона: «файл расходится с живой таблицей или воркфлоу → прав объект, расхождение записывается в файл» |
| M1c#9-23 | ПОДТВЕРЖДЁН | n8n-engineering-manual/references/roots.md:282 (побочная активация при Save) |

## Счёт

- Всего строк: 86 (строка M1b#102в — дубль M1b#102, проверена отдельно).
- ПОДТВЕРЖДЁН: 70.
- ОПРОВЕРГНУТ: 1 — M1c#6-13.
- ЧАСТИЧНО: 14 — M1a#17, M1a#59, M1a#82, M1b#54, M1b#75, M1b#77, M1c#C23, M1c#C66, M1c#C69, M1c#3-41, M1c#6-10, M1c#8-2, M1c#8-8, M1c#9-20.
- СПОРНО: 1 — M1c#3-39.

Замечания для сессии стадии Б:
1. M1b#77: часть про JSON совпадает со строкой Х-43 в meta/LESSONS_waiting.md — по А2 это новый независимый случай (встречаемость +1), а не «уже есть».
2. M1c#3-39 и M1c#8-2: в уроке есть утверждение, которое противоречит действующему правилу Skill (мост вместо clasp; встроенная проверка вместо серии дней). Вносить эти половины нельзя.
3. Исходные отчёты харвеста сами помечали часть этих строк «ЕСТЬ ЧАСТИЧНО» или «НОВЫЙ»: G10.md:30 (S8), CONTROL.md:23 (C23), :66 (C66), :69 (C69), G6.md:43 (У-10), G8.md:40, :52. Вердикт «уже есть» для них поставлен без учёта этих пометок.
