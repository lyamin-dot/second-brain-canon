meta/OZON_UE_INPUTS_MAP.md

# Карта входов и выходов юнит-экономики Ozon (OZON_UE)

Читатель: любая сессия любого проекта, которой нужно знать, что OZON_UE получает с площадки Ozon, куда кладёт, каким ключом, что пишет в Ozon и в чужие книги, что вносится руками и каких данных нет. Мастер-промпт не нужен. Снята 2026-10-24 по живым объектам по запросу интегратора MARKETPLACE_REBUILD (`projects/marketplace-rebuild/`); владелец файла — лаборатория `labs/ozon-ue/` (адреса книг — блок «Постоянные адреса» её `INDEX.md`). Карта — снимок на дату: перед решением сверять с объектом.

Метки происхождения: П — сессия OZON_UE прочитала объект 2026-10-24 (get_workflow_details, search_workflow_executions, gsheets-read, мост gas-bridge); ПП — прочитал посредник (субагент) в той же сессии; Д — документ канона, с объектом не сверено. Имена и номера ключей доступа сюда не пишутся (И-7 Skill second-brain-git): они в закрытой книге N8N_CREDENTIALS, ID — `registry/documents.md`.

## 1. Входы с площадки (кабинет Кипарис; по ИП входов нет)

| Метод Ozon | Воркфлоу | Расписание | Куда пишет | Последний успех | Дубль |
|---|---|---|---|---|---|
| /v1/finance/accrual/by-day + /v3/posting/fbs/get | Ozon RAW Accrual Sync aVpgEnYBAgIIss4k | ежедневно 02:00 (00:00 UTC) | книга RAW 1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4, лист ozon_raw_accrual_TEST | исполнение 85021, 24.10 (П) | зонд H5XqX4xXyaFuRVHb, выключен (ПП) |
| — (читает ozon_raw_accrual_TEST, ozon_accrual_types, Price Master!Artikel A1:H1506) | адаптер BPVFEmZF6QxXuTB6 | ежедневно 02:20 | RAW, лист sales_raw_operations, ключ operation_id | 85026, 24.10 (П) | — |
| /v1/finance/accrual/types | OZON_UE Accrual Types Sync c7TIdv32dHV3MBRU | пн 01:00 | RAW, лист ozon_accrual_types | успешные прогоны не сохраняются, ошибок 0 (П) | зонд H5Xq |
| /v3/product/list + /v3/product/info/list | Получение SKU Ozon J0v5swjXLfiANJa2 | ежедневно 03:00 | Price Master 1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk, лист Ozon_SKU_Staging | 85032, 24.10 (П) | nNNJuafLqTX7g8TU |
| /v3/product/list + /v3/product/info/list | SKU Artikel Map nNNJuafLqTX7g8TU | активен, но «раз в 1000 месяцев» — фактически не запускается | SKU_Artikel_Map 1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU (выводится из эксплуатации, Д) | не сохраняются (П) | J0v5; снять — предложение, решения Андрея нет |
| /v1/analytics/data (выручка и заказанные штуки по SKU и дню) | OZON RAW Analytics History Load NTNN2Kvqg09yoRKi | ручной инструмент, одна дата в коде | ozon_raw_конверсия 1xxO6QpwyJ17tbpGjX9VJgtCt7y-Bfs0h0TCIuPUU5B4, лист ozon_raw_analytics | не сохраняются (П) | ежедневный SElTcMg3BpY6pmdo снят с публикации (П) |
| /v3/finance/transaction/list | OzonRawАналитика MPzPrtsnPtf0sVQo | СНЯТ С ПУБЛИКАЦИИ 2026-10-24 (П) | RAW, sales_raw_operations | метод отключён Ozon (исполнение 63904, Д) | FnB2Imp7thMKuwnD, выключен (ПП) |

Свежесть цепочки: книга «Деньги», лист «Параметры» — последняя дата в источнике 23.10.2026, снимок 24.10.2026 6:32 (П). Сверка 17–23.10: каждый raw_key листа ozon_raw_accrual_TEST есть в sales_raw_operations, строк не от адаптера с 07.10 — 0 (gsheets-read 85439, 85442, 85446; ПП, пересчитано сессией).

## 2. Ключи

| Кабинет | Права | Истекает | Кто пользуется |
|---|---|---|---|
| Кипарис (основной) | Admin и 30 частных ролей, чтение и запись (лист «Ключи», П) | 2 дек. 2026 (лист «Ключи», П) — перевыпуск: `labs/ozon-ue/t-n8n-ozon-workflow-defects.md`, раздел 2026-10-24 | все входы раздела 1; инструмент u06pa4u5sDYdQD3W (только чтение основного); вне OZON_UE: BLNA8sbdnLtuz7Uj, r35gXE6VxvuacEfW, 529VWvqSTg8l4fUU, 555GP7GWs1EL5FIO, IHn3Bmyh1VeHf4Ya, XG4gzxtqPJXafBXN, XFEhjlkrXXnl1bpU, oJrg4XY0HZwPCq59, tZ4NrzdAAurD4GQH, FnB2Imp7thMKuwnD, ft4D2JGquVUzhtO0 (ПП) |
| ИП | в списке разрешённых методов есть запись (/v3/product/import, /v1/product/import/prices, /v1/barcode/add); имя роли не прочитано | 2027-01-19 (ответ /v1/roles в книге «Описания карточек», лист «Перенос в Ozon ИП», B420; П) | u06pa4u5sDYdQD3W (П); eLBcH8MeE38NbMZq, m6svDS7yhrTjTCrt, GElwjPKkJQkCao3b — проект deklaration-ozon (ПП) |

Ключ ИП: есть, но частично настроен — в лист «Ключи» не внесён; выгрузка товаров ИП PWFVE0UbM3ajvVFc к ключу не привязана, листа Ozon_IP_SKU_Staging в Price Master нет (П). Задача — `labs/ozon-ue/t-ozon-ip-cabinet.md`.

## 3. Запись в площадку

| Воркфлоу | Проект | Что пишет | Включён | Сухой режим |
|---|---|---|---|---|
| Ozon Copy Осн → ИП u06pa4u5sDYdQD3W | OZON_UE | ИП: /v3/product/import, /v1/barcode/add, /v1/barcode/generate | нет, ручной; последний прогон 84874, 23.10 (П) | да, узел 02_Params, по умолчанию «проверка» (П) |
| LM_DECL — Ozon Upload BLNA8sbdnLtuz7Uj | deklaration-ozon | Кипарис: /v2/product/certificate/create | ДА, запуск формой | да, поле формы mode, по умолчанию «проверка» (ПП) |
| Ozon Card Fields Fix (ИП) eLBcH8MeE38NbMZq | deklaration-ozon | ИП: /v1/product/attributes/update | нет | да (ПП) |
| LM_DECL — Ozon Upload ИП GElwjPKkJQkCao3b | deklaration-ozon | ИП: /v2/product/certificate/create | нет | да (ПП) |
| OZON Publish Reviews XG4gzxtqPJXafBXN | в каноне OZON_UE не ведётся | Кипарис: /v1/review/comment/create, каждые 30 мин | нет | НЕТ (ПП) |