meta/COST_skill-reading_2026-10-22.md

# Модель цены чтения сессии — по видам сессий (замер 2026-10-22)

Кто читает: проект `projects/kontext-reduktion/` (цель — уменьшить обязательное чтение) и любая сессия, которая решает, что переносить между слоями Skills. Что это: разовый расчёт скриптом `meta/scripts/reading_cost.py` по зеркалу `skills/` на коммите main, названном в записи журнала (`projects/kontext-reduktion/LOG.md`, запись о контракте 2026-10-22). Не монитор: пересчитывается по слову, когда нужно сравнить «до» и «после».

Что складывается: описания всех Skills (лежат в каждом чате каждого проекта) + `SKILL.md` сработавших Skills + файлы `references/` по строкам таблиц «Что читать дальше» + CORE по Манифесту + файл проекта + `meta/PENDING_RULES.md`. Мастер-промпт живёт в интерфейсе и скриптом не читается: у сессии SYS он около 12 000 Б (оценка по тексту промпта, не замер инструментом) — прибавлять к видам S1–S7.

Два числа описаний: зеркало `skills/` держит только собственные Skills Андрея — 13 819 Б; живой каталог сессии 2026-10-22 содержал 26 Skills, включая Skills Anthropic, — 22 142 Б. В каждом чате лежит второе число. Разница 8 323 Б платится всеми проектами и правится не в репозитории.

Проверка модели по живой сессии 2026-10-22 (SYS, задача проектирования): файлы, вошедшие в контекст до первого ответа, сложены вручную — 159 КБ база (с описаниями живого каталога и мастер-промптом) и около 250 КБ с файлами задачи; модель даёт S1 = 138 850 − 13 819 + 22 142 + 12 000 ≈ 159 200 Б. Сходится.

Коэффициент 0,37 токена на байт — оценка (замер цены русского текста на выходе модели, `second-brain-git` 8.2), не замер чтения; байты — факт.

## Таблица (зеркало skills/, 2026-10-22)

| Вид сессии | Байт | ≈ токенов (0,37/Б) | Файлы (байт) |
|---|---|---|---|
| S1 старт сессии SYS (до первого ответа) | 138 850 | 51 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563 |
| S2 SYS + первая запись в репозиторий (лаборатория) | 212 331 | 79 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-git/references/write.md 59739; second-brain-git/references/lab.md 13742 |
| S2б то же + отказ GitHub или параллельная сессия | 236 470 | 87 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-git/references/write.md 59739; second-brain-git/references/lab.md 13742; second-brain-git/references/delivery.md 24139 |
| S3 SYS + !save | 232 859 | 86 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/commands.md 5042; second-brain-engineer/references/save.md 15486; second-brain-git/references/write.md 59739; second-brain-git/references/lab.md 13742 |
| S4 SYS + правка воркфлоу n8n | 219 667 | 81 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/permissions.md 12793; n8n-engineering-manual/SKILL.md 36073; n8n-engineering-manual/references/write.md 31951 |
| S4б то же + диагностика «почему не работает» | 318 147 | 118 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/permissions.md 12793; n8n-engineering-manual/SKILL.md 36073; n8n-engineering-manual/references/write.md 31951; n8n-engineering-manual/references/roots.md 98480 |
| S5 SYS + выдача наряда | 217 388 | 80 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/permissions.md 12793; naryad/SKILL.md 34936; naryad/references/issuer.md 30809 |
| S6 SYS + проектирование (метод Р19) | 177 937 | 66 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/design.md 39087 |
| S7 SYS + харвест | 249 866 | 92 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; labs/sys/INDEX.md 13653; meta/PENDING_RULES.md 4563; second-brain-engineer/references/commands.md 5042; second-brain-engineer/references/harvest.md 3302; meta/PROTOCOL_harvest.md 36309; meta/PROTOCOL_lesson-triage.md 30891; meta/PROTOCOL_knowledge-synthesis.md 35472 |
| S8 старт repo-проекта (projects/kontext-reduktion: STATE + PLAN) | 151 946 | 56 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-git/SKILL.md 47555; second-brain-engineer/references/start.md 5795; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; meta/PENDING_RULES.md 4563; projects/kontext-reduktion/STATE.md 5997; projects/kontext-reduktion/PLAN.md 14957 |
| S9 старт Docs-проекта (INDEX в Google Docs не считается — живёт в Drive) | 126 548 | 47 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-engineer/references/start.md 5795; google-drive-docs/SKILL.md 36902; google-drive-docs/references/docs-read.md 10772; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726 |
| S10 работа с книгой Google Sheets через Apps Script | 268 190 | 99 тыс. | описания 13819; second-brain-engineer/SKILL.md 41320; second-brain-engineer/references/start.md 5795; core/MANIFEST.md 8459; core/R-04.md 1438; core/R-05.md 1260; core/R-06a.md 5057; core/R-07.md 1726; google-drive-docs/SKILL.md 36902; google-drive-docs/references/sheets.md 32123; apps-script-sheets/SKILL.md 80043; apps-script-sheets/references/book-traps.md 40248 |

## Что видно по таблице

1. База S1 — 139 КБ (152 КБ с описаниями живого каталога, около 164 КБ с мастер-промптом). Из неё 89 КБ — два `SKILL.md`, которые загружаются в каждой сессии SYS. Это главный объект работы над чтением.
2. Самые дорогие файлы по событию: `n8n-engineering-manual/references/roots.md` 98 КБ (диагностика), `apps-script-sheets/SKILL.md` 80 КБ (постоянный слой, не по событию), `second-brain-git/references/write.md` 60 КБ (любая запись), `design.md` 39 КБ (любое проектирование).
3. Файл по событию стоит столько же, сколько постоянный слой, когда его зерно — тема, а не момент действия: `design.md` для проектирования, `write.md` для записи. Поэтому следующий шаг — зерно `references/` по моменту действия (правило в `meta/PROTOCOL_knowledge-synthesis.md`, шаг С4а).

## Как пересчитать

`python3 meta/scripts/reading_cost.py --md` из корня клона; `--skills /mnt/skills/plugins` — по живому каталогу сессии; `--project projects/<имя>` — другой проект для вида S8.
