projects/n8n/STATE.md

<!-- obzor-блок: форма — projects/obzor/PLAN.md, «Устройство», пункт 2; правится тем же шагом, что разделы ниже -->
> Состояние: работает
> Дата: 2026-11-10
> Что это: Инфраструктура n8n
> Следующий шаг: Ручные действия Андрея, пункты 2 и 3
> Ждёт Андрея: Перевыпустить ключ сервиса поиска; одна команда на сервере — найти ключи в узлах и истории версий

# STATE_n8n — текущее состояние работ

Здесь только то, что меняет действие следующей сессии. Решения — `LOG.md`; правила и устройство проекта — `PLAN.md`; невзятое при переносе из N8N_INDEX — `NOT_TAKEN.md`.

## Состояние инстанса

Сверено 2026-10-27 по снимку `registry/n8n-map.md` (instance_last_change 2026-10-26T19:28): активных 100, неактивных 88, архивных 97; без errorWorkflow из активных 4, после правки 2026-10-28 (запись Р-9 журнала) — 1, сам Error Notifier; без явной таймзоны 64 (32 на Europe/Moscow, 4 на Europe/Berlin явно); с неопубликованным черновиком 1 — N8N Registry Sync gFFiBPm1OomOzJOj (узлы-зонды, projects/n8n-map/STATE.md); висячих вызовов 0.

## СЛЕДУЮЩИЙ ШАГ

- Ручные действия Андрея — раздел ниже, остались пункты 2 и 3.

## Ручные действия Андрея

1. СДЕЛАНО 2026-10-18, проверено по объекту: list_credentials по имени ключа API n8n вернул 0 записей. Остаток: узлы 03_Ozon_Transaction_List (MPzPrtsnPtf0sVQo, get_workflow_details 2026-10-18: в credentials.httpHeaderAuth стоит удалённый ключ API n8n) и 03_Ozon_Analytics_Request (SElTcMg3BpY6pmdo, неактивен) ещё ссылаются на удалённый ключ — висячая ссылка; узел аутентифицируется по genericAuthType httpCustomAuth (Ozon Seller API). Убрать ссылку при ближайшей правке этих узлов. Было: удалить ключ доступа API n8n в n8n → Credentials. Он висит лишней привязкой на узлах 03_Ozon_Transaction_List (MPzPrtsnPtf0sVQo) и 03_Ozon_Analytics_Request (SElTcMg3BpY6pmdo, неактивен), оба узла ходят с ключом «Ozon Seller API». Если его значение — живой ключ n8n API или WB, отозвать и там, где он выдан. После удаления — проверить, что ночной прогон OzonRawАналитика (02:00 по серверу) не прислал алерт. Гипотеза (не проверена): лишняя привязка после удаления ключа узел не роняет.
2. Перевыпустить ключ Serper в кабинете Serper и вставить новое значение в ключ доступа Serper в n8n; старый отозвать. Правок в воркфлоу ноль. Проверка — ручной прогон GDI35U36bBRzKZp5, результат по объекту.
3. Одна команда на сервере — найти литералы ключей в узлах и истории версий (закрывает вопрос «Anthropic: 1 ключ, 2 воркфлоу, не перепроверено» из аудита 2026-07-23):
   docker exec -i n8n-postgres-1 psql -U n8n -d n8n -c "select id, name, active from workflow_entity where nodes::text like '%sk-ant-%' or nodes::text ilike '%Api-Key%'"
   Имя пользователя и базы сверить с docker-compose. Второе условие ловит и законные упоминания имени заголовка — смотреть только строки, где рядом стоит значение ключа. Найденное — ID воркфлоу прислать сессии N8N; ключ Anthropic в n8n есть готовый, перевод узла на него — точечная правка.

## ОТКРЫТЫЕ ЗАДАЧИ

[ ] [2026-10-28] Перевод часов (запись Р-9 журнала, пункт 4): суточное расписание дописывающего воркфлоу на 02:00–03:59 по Берлину в ночь возврата часов идёт дважды, в ночь перехода на летнее время в 02:00–02:59 не идёт вовсе. Сдвигать при касании по решению владельца воркфлоу. Строка соседу marketplace-rebuild записана 2026-10-28: Ozon RAW Accrual Sync aVpgEnYBAgIIss4k (02:00), OZON_UE Accrual → sales_raw_operations Adapter BPVFEmZF6QxXuTB6 (02:20), Получение SKU Ozon J0v5swjXLfiANJa2 (03:00). Ближайшая ночь, где 02:xx пропадёт, — 2027-03-28.

[ ] [2026-10-26] Стандарт интерфейсов (пункт 3 роли): у трёх посредников MKT2 API (95w8XpN3OHNl2NsE, JzoU49Wy2soTzZ44, ZhpjwjErqHEpoFCA) охрана методов — общий список, не привязанный к ключу (находка Прораба, по его чтению определений). Правило: воркфлоу, который только читает, ходит ключом только на чтение (n8n-engineering-manual §2.1.4); ⚡ Это затрагивает MARKETPLACE_REBUILD: ключ Ozon ИП — завести R-only, вопрос уже в его STATE.

[ ] [2026-10-17] Таймзона: 68 активных без явной таймзоны работают по серверной Europe/Berlin. Массово не ставить (Р-6, отвергнуто). Правило при касании воркфлоу: если расписание или текст рассчитаны на московское время (пример — Order Intake kNg2uEoYlaGOLC82, описание «Telegram только в 06:00 и 16:00 МСК»), ставить Europe/Moscow и пересчитать часы расписания; иначе ставить Europe/Berlin явно.

[ ] [2026-10-17] Перевод Google-узлов с OAuth2 на сервисный аккаунт — по одному воркфлоу при касании, руками в редакторе (Р-6, пункт 8). Первыми — потребители «Google Drive account» XagmJHhXQU748dYW (протухал в сентябре): GDrive Trash Sweeper LFDK2oAFdGWQ3Nxd, create_folder uapccJY1O4ykyDi7, Claude → Obsidian kJTXJuHQAv1go52t, DOSSIER W3KjaXVqWD2c02IK, bFJsM3aFlIHIFeAd, KEucSnA2duWI3eRA. Перед переводом — файлам и папкам дать доступ сервисному аккаунту (n8n-engineering-manual §8).

[ ] ЗАМОРОЖЕНО — проект OZON_REVIEWS (решение Андрея 2026-10-06): все четыре воркфлоу OZON_REVIEWS неактивны. При разморозке, по порядку: (1) вернуть строку заголовков листа ozon_reviews_queue книги OZON Reviews System (1mgtcD2wSm_-8hqfpv3v883KE34-Smy-kFxHvt6zMXj4) — эталон: первые 28 колонок строки 1 листа ozon_reviews_archive, имя 29-й колонки не установлено; (2) в OZON Reviews Archive HH7pDL2VZfU9C9Np, узел 10_Delete_From_Queue, startIndex = row_number вместо row_number − 1 (сейчас удаляет строку над архивированной); (3) только потом включать. Публикация в Ozon отвечает PermissionDenied «not available with existing subscription». Подробности — прежний текст файла, blob ff350070.

## От соседнего проекта

- Строки marketplace-rebuild Р-32 (ключи Google), Р-58 и Р-96 (Telegram в Error Notifier и мониторе) разобраны 2026-11-10 — LOG.md Р-10, ответ в STATE.md marketplace-rebuild.

## Паспорта воркфлоу (2026-10-21, автопилот)

- 2026-10-28 (запись Р-9 журнала; пересчёт по выдаче search_workflows без учёта регистра): из 99 активных строки паспорта нет у 11 (2026-11-04: у трёх инструментов архива — Archive Read Status Page, Archive Control, Archive Search — вписана строка общего паспорта SERVER_WF_archive-tools, он существовал с 21.10, но из описаний не был виден) — OZON RAW Analytics History Load NTNN2Kvqg09yoRKi, Ozon RAW Accrual Sync aVpgEnYBAgIIss4k, WB FBS Supply Accepted 7x9wPrugdbseaEp2, WB FBS Order Intake kNg2uEoYlaGOLC82, WB FBS Order Close v2 DM26WhTJyCV0DhkP, OZON Money Telegram YkUb5SnLtEaTctoH, Получение nmID WB gglEq5U90Gt3sI7h, WB_WF_sku-mapping-loader qrZw8bxIEpRAUwEe, KB TO — Annotation Preprocessor wWFfPIAfLd7yunU8, KB Loader — Transmission Oil jb9L7xLCYyiJ95aa, Ozon_Hashtag_Generator KQqajdrYKxle9JRe; строка словом «Passport:» в другом регистре — у WB Monitor Telegram Reader DcIqwTVqBqMQyigs, WB Reports Official Sync P7CZYJZWIqC5Me4c, LM_DECL — Scan vKjqExap1mJjM6Ap. Строки паспорта шести общих компонентов (Git Read, Git Log, Git Append, Git Replace, Git Read Batch, gsheets-read) вписаны сессией 2026-10-28. Паспорт чужого воркфлоу заводит его владелец при касании. Пересчёты ниже — история.
- 2026-10-27 ⚡ от marketplace-rebuild (Р-27 его журнала): паспорта MKT2 исполнены — строки PASSPORT видны в выдаче поиска у всех 21 активных воркфлоу MKT2 (16 сборщиков вписала сессия через update_workflow, setWorkflowMetadata, версия не менялась; пять остальных — Андрей руками); сервисный аккаунт — редактор папки DOCS, gdocs-read читает паспорт. Осталось по этому наряду только «да» Андрея на корзину шести первых черновиков паспортов. Охрана посредников, не привязанная к ключу, вынесена Андреем в отдельное обсуждение — решения нет.

- NTNN2Kvqg09yoRKi починен и опубликован 2026-10-21 по решению Андрея (подробности — `meta/CASES_ozon-ue-lab-closed-2026-10-28.md` (раздел «labs/ozon-ue/t-n8n-ozon-workflow-defects.md»), раздел «Решение 2026-10-21 по NTNN»). Паспорта у него нет — завести.
