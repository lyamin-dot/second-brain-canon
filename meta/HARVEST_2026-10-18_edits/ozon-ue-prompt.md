# Мастер-промпт OZON_UE — позиции AH-17 и AI-18 (зеркало meta/prompts/ozon-ue.md)

Источник текстов: `meta/HARVEST_INPUT_2026-10-16.md`, часть 3, позиции AH-17 (строки 429–466) и AI-18 (строки 468–495); позиции очереди `registry/maintenance-queue.md`, строки 149 (AH-17, срок был 2026-10-16 — просрочена) и 181 (AI-18). Решение: `meta/HARVEST_2026-10-18_answers.md`, Г1 и условие на строке 147.

УСЛОВИЕ ИЗ ФАЙЛА ОТВЕТОВ (строка 147): до вставки Андрей сохраняет старый текст промпта файлом — промпт живёт только в интерфейсе Claude Project и не откатывается (Skill second-brain-engineer, раздел Р13, строка «Андрей обязан»: «сохранить старый текст мастер-промпта файлом до вставки нового»).

Это не Skill. Цель — поле Project instructions проекта «02_Unit_Econ._Ozon»; поле `file` в json — путь зеркала в репозитории (`meta/prompts/ozon-ue.md`), и якоря проверены по зеркалу. Зеркало снято с живого текста 2026-10-09 и после этого с живым текстом не сверялось: перед вставкой Андрей видит живой текст сам. После вставки зеркало обновляется тем же текстом (шапка зеркала, строка 5), и тогда же нужно поправить саму строку 5 — она говорит «строки позиции AH-17 … в живом тексте на 2026-10-09 нет».

Проверка якорей по зеркалу: AH-17 — строка 16 «Architecture: …» найдена ровно один раз; AI-18 — предложение строки 70, кончающееся «(Manifest «По событию» row «запись в INDEX-документ проекта»).», найдено ровно один раз. Факты AI-18 сверены: `core/MANIFEST.md`, строки 46 и 47 (две строки «По событию»), `core/R-06-marshrut.md`, строка 13 (абзац «ОБЛАСТЬ ДЕЙСТВИЯ»). Промпт ведётся по-английски — тексты вставки английские, как в позициях.

## 1. Правки «было → стало»

### Основные правки (файл ozon-ue-prompt.json)

#### AH-17

- Файл: `meta/prompts/ozon-ue.md`, строка 16 живого файла.

ЯКОРЬ (скопирован из живого файла программно):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
````

БЫЛО (точный фрагмент, заменяется целиком):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
````

СТАЛО (полный текст на замену):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
Declaration search and matching (conformity declarations: LM_DECL, workflows Scan and Ozon Upload, book LM_DECL_MASTER) has been a separate chronicle project, projects/deklaration-ozon/, since 2026-10-01 (Andrei's decision). Do not work on declarations here and do not write to Zone B for them; read projects/deklaration-ozon/STATE.md and PLAN.md. Exception: the product-data link model (article, Ozon SKU, WB card, price, declaration number as key) is kept here — task labs/ozon-ue/t-product-data-model.md (Andrei's decision 2026-10-02, projects/deklaration-ozon/LOG.md Р-23).
````

#### AI-18

- Файл: `meta/prompts/ozon-ue.md`, строка 70 живого файла.

ЯКОРЬ (скопирован из живого файла программно):
````text
Before the first such write in a session read core/R-06-marshrut.md, core/R-06b.md, core/R-06d.md, core/R-08.md, core/R-11.md (Manifest «По событию» row «запись в INDEX-документ проекта»).
````

БЫЛО (точный фрагмент, заменяется целиком):
````text
Before the first such write in a session read core/R-06-marshrut.md, core/R-06b.md, core/R-06d.md, core/R-08.md, core/R-11.md (Manifest «По событию» row «запись в INDEX-документ проекта»).
````

СТАЛО (полный текст на замену):
````text
Before the first such write in a session read core/R-06-marshrut.md, core/R-06b.md, core/R-06d.md, core/R-08.md, core/R-11.md (Manifest «По событию» row «запись в INDEX-документ проекта»). Before the first write to repository files in a session (a task file, labs/ozon-ue/INDEX.md) read core/R-06-marshrut.md, paragraph «ОБЛАСТЬ ДЕЙСТВИЯ» (Manifest «По событию» row «запись в файлы репозитория»).
````

### Варианты и дополнения на решение Андрея (файл ozon-ue-prompt.optional.json)

#### AH-17, вариант с учётом разделения 2026-10-07 и проекта deklaration-v2 (на решение Андрея)

- Файл: `meta/prompts/ozon-ue.md`, строка 16 живого файла. Применяется ВМЕСТО позиции «AH-17» основного файла.

ЯКОРЬ (скопирован из живого файла программно):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
````

БЫЛО (точный фрагмент, заменяется целиком):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
````

СТАЛО (полный текст на замену):
````text
Architecture: Ozon API → n8n → RAW Google Sheets book → Unit Economics book → DECISION_ENGINE.
Conformity declarations (LM_DECL: search and matching, workflows Scan and Ozon Upload, book LM_DECL_MASTER) are not worked on here since 2026-10-01 (Andrei's decision): they belong to separate chronicle projects. Which projects and where — registry/projects.md (rows deklaration-*) and the [LM_DECL] line of «Постоянные адреса» in labs/ozon-ue/INDEX.md; this prompt deliberately holds no project paths (paragraph below). A declaration finding made here goes neither into this lab nor into Zone B: it goes as one line into the «От соседнего проекта» section of the STATE.md of the project it concerns — the same way Skill second-brain-git 10.6 prescribes for projects in the repository. Exception: the product-data link model (article, Ozon SKU, WB card, price, declaration number as key) is kept here — task t-product-data-model (Andrei's decision 2026-10-02, projects/deklaration-ozon/LOG.md Р-23).
````


## 2. Бюджет правки

Зеркало `meta/prompts/ozon-ue.md`: 12 318 → 13 160 байт (AH-17 и AI-18 по тексту очереди); с вариантом AH-17 — 13 536 байт.
Что те же правки снимают или сжимают: AH-17 добавляет строку; в промпте о декларациях больше ничего нет, снимать нечего. AI-18 добавляет предложение; соседнее предложение о записи в Google Doc остаётся, потому что лаборатория по-прежнему пишет в Зону Б документа OZON_UE_INDEX.

## 3. Найдено при сверке

1. Строка 39 (source_order): «Google Drive MCP read_file_content silently cuts the tail above ~130 KB» — опровергнуто: Skill google-drive-docs, SKILL.md, строки 34–35, блок ИСТОРИЯ ДИАГНОЗА от 2026-10-12 («число 130 КБ не было замером»; обрыв наблюдался около 64 тысяч символов, а 160 КБ однажды пришли целиком).
2. Строка 40: «an empty google_drive_search proves nothing» — инструмента google_drive_search в нынешнем коннекторе нет, его место занял search_files (google-drive-docs, references/mcp.md, раздел 2.3).
3. Строка 72: «Size: ≤ ~1–2 KB per n8n write call (transit corrupts bytes); split larger with re-read after each part» — google-drive-docs (§3, §3.6) с 2026-09-24 называет штатным путём для большого текста gdocs-apply-from-file, а дробление — запасным путём.
4. Строка 75: «Only after explicit «да»: any n8n workflow change» — к этому относится решение А4 харвеста 2026-10-18 (исключение для поручения «реши сам» в пределах задачи), если оно будет внесено в Skill; промпт тогда разойдётся со Skill.
5. Строка 76: «single-letter prefixes A–Z are exhausted, new items use two-letter prefixes» — верно (позиции AH-, AI- в очереди).
6. Строка 17: «The Git-channel and gdocs-* IDs below are the exception» — в промпте стоят ID Git Read Lines, Git Commit Files, gsheets-read, gdocs-read, gdocs-append, gdocs-replace (строки 25, 34, 39, 65, 70); все шесть активны по `registry/n8n-map.md` (снимок 2026-10-18). Не ошибка.

## 4. Противоречия и вопросы Андрею

1. AH-17 устарел по существу (исполнитель 2026-10-16 это отметил, подтверждаю): 2026-10-07 проект deklaration-ozon разделён — Wildberries ушёл в `projects/deklaration-wb/`, общий слой — `meta/DECLARATION_COMMON.md` (`registry/projects.md`, строка 11; `projects/deklaration-ozon/LOG.md`, Р-47), а с 2026-10-10 есть `projects/deklaration-v2/`. Текст очереди направляет сессию OZON_UE только в deklaration-ozon. Кроме того, он вписывает в промпт адреса проектов, а абзац строки 17 того же промпта прямо запрещает адреса в промпте («A prompt address goes stale silently») — ровно это и случилось. Подготовлен вариант (`ozon-ue-prompt.optional.json`, применяется вместо AH-17): без путей проектов, со ссылкой на `registry/projects.md` и на строку [LM_DECL] блока «Постоянные адреса» `labs/ozon-ue/INDEX.md`, где адрес уже держится; находка о декларациях идёт строкой в «От соседнего проекта» STATE.md нужного проекта. Какой текст вставлять — решение Андрея. Сама строка [LM_DECL] в INDEX.md (строка 21) тоже знает только deklaration-ozon — её правит сессия лаборатории, это не промпт.
2. «В Зону Б не писать» (текст очереди) против блока <writing>, строка 68: «Finding … with no task of its own → append to Zone B». Без оговорки сессия получает два правила; в варианте оговорка есть («goes neither into this lab nor into Zone B»).
3. AI-18 — место вставки (исполнитель 2026-10-16, пункт 1, подтверждаю): новое предложение о файлах репозитория оказывается внутри абзаца о Google Doc OZON_UE_INDEX, хотя относится к блоку «Tasks — in labs/ozon-ue/» (строки 64–69). Текст очереди требует именно «после этого предложения»; перенести в начало блока Tasks — решение Андрея (якорь тогда другой, текст не готовил).
Напоминание: до вставки любой из этих правок Андрей сохраняет старый текст промпта файлом.

## 5. Проверка скриптом

Порядок: живой файл скопирован во временную папку, правки основного файла применены по порядку, перед каждой заменой проверено, что фрагмент «было» встречается ровно один раз. Каждый вариант на решение Андрея проверен отдельно: вариант «вместо» — заменой своей основной позиции и прогоном всего набора заново на свежей копии, дополнение — поверх основного набора. Скрипты: `/tmp/claude-0/-home-claude/e8ea0284-4279-59d6-9131-3ccb358b5137/scratchpad/gen/verify.py` (сборка — `build.py` рядом).

- основной | AH-17 | meta/prompts/ozon-ue.md | найдено 1 раз, применено
- основной | AI-18 | meta/prompts/ozon-ue.md | найдено 1 раз, применено
- ozon-ue-prompt | РАЗМЕР | meta/prompts/ozon-ue.md | 12318 -> 13160 байт (основной набор)
- вариант вместо «AH-17», весь набор заново | AH-17, вариант с учётом разделения 2026-10-07 и проекта deklaration-v2 (на решение Андрея) | meta/prompts/ozon-ue.md | найдено 1 раз, применено
- вариант вместо «AH-17», весь набор заново | AI-18 | meta/prompts/ozon-ue.md | найдено 1 раз, применено
- ozon-ue-prompt | РАЗМЕР | meta/prompts/ozon-ue.md | 12318 -> 13524 байт (основной набор с этой позицией)

