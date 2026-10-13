labs/sys/t-audit-0723-unverified.md

# Восемь дефектов аудита 2026-07-23 не перепроверялись с августа

Метка: РУТИНА. Заведена 2026-09-27 сессией обхода Skill при слиянии монолита TEMPLATES.md в `references/templates.md`.

## Суть

Аудит 82 воркфлоу от 2026-07-23 нашёл дефекты, часть которых перепроверена живым чтением 2026-08-04, а часть с тех пор не трогали. При слиянии они перенесены в `references/templates.md` Skill `n8n-engineering-manual` как примеры с датой наблюдения — то есть как история, а не как текущее состояние. Это честно, но вопрос «живы ли они сейчас» остался открытым.

Не перепроверены:
- `MPzPrtsnPtf0sVQo` узел `09_IF_RAW_Rows_Exist` — false-ветвь отсутствует, при этом её ждёт Merge; рецидив, чинили 2026-07-04, вернулось к 07-23, подтверждено 08-04;
- `IvgysDKrq3UISYEY` узел `08_IF_RAW_Rows_Exist` — тот же класс;
- `IvgysDKrq3UISYEY` узлы `07_Find_RAW_Rows_By_Date`, `09_Delete_RAW_Rows`, `11_Write_RAW_To_Sheets` — все три на `continueRegularOutput`, никто ниже не читает code и error, а `errorWorkflow` задан и потому не сработает никогда;
- `DWyvoJYkCodJxMg1` узел `06_Extract_Text_From_PDF` — ветвь ошибки не подключена;
- `VMPxWzXPefKT2R1B` узлы `05A` и `05C_Error_Handler_*` — ошибку получают, но их выход никуда не ведёт;
- `wWFfPIAfLd7yunU8` и `5Iyr82zmzCeievFv` узел `07_Extract_Result` — `throw` внутри цикла останавливает весь батч;
- `VWyXmCPJevCnbkZT` узлы `05_Write_Snapshots_History` и `07_Write_Detail_History` — append с пустым `matchingColumns`;
- `qZWrl0MkRnZBipXA` узел `06_Is_Snapshot_Duplicate` — собирает item заново вместо spread, счётчики категорий теряются каждую неделю.

## Следующий шаг

Отдельный проход с явным бюджетом: связи узлов в снимке не лежат, поэтому проверка возможна только чтением `get_workflow_details` по каждому воркфлоу — 25–45 КБ на воркфлоу, то есть попутной сверкой это не закрывается. Экономный маршрут — посредник по правилу Р21 Skill `second-brain-engineer`: ответ `get_workflow_details` сужению не поддаётся и отдаётся субагенту, который возвращает вердикт по одному вопросу «подключены ли оба выхода узла N», а не текст.

## Проверка 2026-10-13

Пилот Skill avtopilot (`t-avtopilot-skill.md`). Четыре субагента прочитали `get_workflow_details` всех девяти воркфлоу только на чтение; независимый приёмщик сильного класса перечитал их и подтвердил все восемь вердиктов. Опровергнуть ему не удалось ни один.

| № | воркфлоу, узел | вердикт 2026-10-13 | доказательство |
|---|---|---|---|
| 1 | `MPzPrtsnPtf0sVQo` (OzonRawАналитика, активен, updatedAt 2026-10-06T05:57:33Z) `09_IF_RAW_Rows_Exist` | ЖИВ | `connections["09_IF_RAW_Rows_Exist"].main` — только выход 0; вход 1 Merge `11_Wait_For_Delete` приходит лишь через `10_Delete_RAW_Rows_By_Date`. Описание воркфлоу утверждает, что ветка «снова подключена к merge input1», — в объекте этого нет |
| 2 | `IvgysDKrq3UISYEY` (WB RAW Finance Sync V.3, активен, updatedAt 2026-09-28T15:57:16Z) `08_IF_RAW_Rows_Exist` | ЖИВ | `connections["08_IF_RAW_Rows_Exist"].main` — только выход 0; вход 1 Merge `10B_Merge_Before_Write` — лишь через `09_Delete_RAW_Rows` → `10_Wait_For_Delete`. Узел `09_Delete_RAW_Rows` выключен (`disabled: true`) |
| 3 | `IvgysDKrq3UISYEY` `07_Find_RAW_Rows_By_Date`, `09_Delete_RAW_Rows`, `11_Write_RAW_To_Sheets` | ЖИВ | у всех трёх `onError: continueRegularOutput`; поля ошибки не читает ни один узел ниже; `settings.errorWorkflow` = `M5BLqclKBjGTpz33` сработать от них не может. Той же настройкой обладает и запрос к API WB `03_WB_Report_Request` — в аудите его не было |
| 4 | `DWyvoJYkCodJxMg1` (Projekt_OCR OEM_V.5, активен, updatedAt 2026-10-08T12:11:11Z) `06_Extract_Text_From_PDF` | ЖИВ | `onError: continueErrorOutput`, а `connections["06_Extract_Text_From_PDF"].main` — только выход 0: выход ошибки не подключён |
| 5 | `VMPxWzXPefKT2R1B` (LM_DECL_MASTER V.2, выключен) `05A_Error_Handler_New`, `05C_Error_Handler_Expiring` | ЖИВ | ключей этих узлов в `connections` нет: статус PAGE_LOAD_ERROR дальше не идёт. Воркфлоу выключен |
| 6 | `wWFfPIAfLd7yunU8` и `5Iyr82zmzCeievFv` (KB TO и KB AC — Annotation Preprocessor, активны) `07_Extract_Result` | ИСПРАВЛЕН | `parameters.mode` = `runOnceForEachItem`, цикла по элементам нет, единственный `throw` не в цикле. Остаток другого рода: ни у `07_Extract_Result`, ни у `06_Call_Claude` нет `onError`, и одна ошибка останавливает весь прогон |
| 7 | `VWyXmCPJevCnbkZT` (SKU Category Historical Backfill, выключен) `05_Write_Snapshots_History`, `07_Write_Detail_History` | ЛОЖНАЯ НАХОДКА | `operation` = `append`; поле `matchingColumns` у append не используется, пустое значение дефектом не является. Настоящий риск другой: защиты от дублей нет, повторный ручной запуск задвоит все недели |
| 8 | `qZWrl0MkRnZBipXA` (SKU Category Weekly Snapshot, активен, еженедельно) `06_Is_Snapshot_Duplicate` | ЖИВ | код возвращает `[{ json: { snapshot_date: snapshotDate, is_duplicate: isDuplicate } }]` без входных полей; у `08_Write_Category_Snapshot` единственный вход идёт из этой цепочки, режим `autoMapInputData` — счётчики категорий (CORE_SKU и другие) в лист не попадают |

Попутные наблюдения проверяющих. Это гипотезы: по объекту диспетчер их не проверял.
- Гипотеза (не проверена): у `DWyvoJYkCodJxMg1` код узла `05B_Restore_Context_After_Download` начинается с `/**` без закрывающего `*/` — это синтаксическая ошибка на пути через PDF. Единственный сохранённый прогон этого воркфлоу (исполнение 72481, 2026-09-30) упал раньше: на первом узле `01_Sheets_Read_URL_List`, ключ доступа «Google Sheets account» (`lXyVaJbpEY7AJvHC`) отвергнут Google как недействительный или отозванный.
- Гипотеза (не проверена): `10_Delete_RAW_Rows_By_Date` в `MPzPrtsnPtf0sVQo` удаляет непрерывный диапазон от первой найденной строки; если строки даты лежат не подряд, удалятся чужие строки.
- Наблюдение по объекту: у `MPzPrtsnPtf0sVQo` и `qZWrl0MkRnZBipXA` черновик расходится с опубликованной версией (`activeVersion.sameAsDraft: false`). В черновике триггер расписания выключен, в опубликованной версии включён. Публикация черновика остановит оба расписания.

Следующий шаг — решение Андрея по каждому живому пункту: чинить с его «да» или принять. Пункты 5 и 7 — в выключенных воркфлоу.

## Условие снятия

По каждому из восьми пунктов вынесен вердикт «жив» или «исправлен», с датой проверки; живые заведены отдельными задачами или исправлены.

## Ссылки

`n8n-engineering-manual` — `references/templates.md` шаблоны T1-D, T2 слои 2 и 3, T3; `INCIDENT_LOG.md` того же Skill, хронология 2026-07-23 и 2026-08-04; правило посредника — `second-brain-engineer` Р21.
