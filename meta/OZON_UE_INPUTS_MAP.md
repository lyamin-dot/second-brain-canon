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
| OZON Publish Manual XFEhjlkrXXnl1bpU | то же | Кипарис: /v1/review/comment/create, вебхук | нет | НЕТ (ПП) |
| скрипты книг «Цена», «Деньги», «Товары» | OZON_UE | ничего: обращений к Ozon в коде 0 | — | — |

Код книг прочитан мостом gas-bridge целиком (исполнения 85428–85450, ПП; три больших файла перепроверены сессией): наружу книги ходят только SpreadsheetApp.openById. Цены, остатки и ответы на отзывы сейчас не пишет ни один включённый воркфлоу (П, ПП). Ключ Кипарис с ролью Admin технически позволяет запись любому воркфлоу, к которому привязан.

## 4. Чужие объекты

| Книга / лист | Читает OZON_UE | Пишет OZON_UE | Владелец |
|---|---|---|---|
| Price Master, Ozon_SKU_Staging | — | J0v5swjXLfiANJa2 (П) | в `registry/documents.md` не указан; главная таблица товаров (`meta/PRODUCT_DATA_HIERARCHY.md`) |
| Price Master, Artikel | адаптер BPVFEmZF6QxXuTB6, узел 01D (П); книги «Цена», «Деньги», «Товары» (код, ПП) | — | то же; колонка A — IMPORTRANGE из книги WB_RAW_Аналитика 14QMHYMM4mZRnnq1wHQA4_SA8ZnOeE1xcVJDL2h9h1Pk (WB_UE, Д) |
| Price Master, ARTIKEL_PROPS | u06pa4u5sDYdQD3W (П) | — | то же |
| «Описания карточек» 1IE0B89Pd1jVdDpgkjqb3pgJow3cFtimYY07RSEAnO6Y | — | u06pa4u5sDYdQD3W: листы «Перенос в Ozon ИП», «Снимок ИП 2026-10-23» (П) | card-content-sync (ПП) |
| «Актуальные цены Lique Moly» 17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU, Акт.цена | Cost Price Snapshot 2UsyP3q5Jd9OafJD (снимок registry/n8n-map.md), книги (код, ПП) | — | не указан |
| «Справочник LM» 1UBiXDZDHfMwxK3Q6mDRYaG65MjnIF2K7ygZhWhOPumY | через IMPORTRANGE в Акт.цена, адрес в J3 (П) | — | Андрей (Д) |

## 5. Ручные входы

| Где | Что | Когда | Если забыть |
|---|---|---|---|
| Акт.цена!J3:L3 | ID нового справочника LM; K3 — дата прайса (сейчас 20.08.2026), L3 «внесено» (П) | новый прайс (Д) | закупка по старому прайсу |
| Cost Price Snapshot 2UsyP3q5Jd9OafJD | ручной запуск | после смены прайса (Д) | нет новых цен в cost_price_history; сейчас 38 проданных штук без закупки, прибыль по ним завышена («Деньги»!Параметры, П) |
| «Деньги», «Параметры» B4:B8 | начало истории, упаковка FBS (50 ₽), период анализа, расходы вне Ozon (0 ₽; реклама — сюда же) (П) | по изменению | прибыль без постоянных расходов и рекламы |
| «Деньги», «Поправки» | начисления из отчёта Ozon, которых нет в RAW: 15 строк, 90 168,70 ₽ (П) | после сверки с отчётом Ozon | недоучёт «Получили» недели |
| RAW, «Поправки штук» | 1129 строк, 1707 штук, недосчитанных до 07.09.2026 (П) | разово, история | штуки и себестоимость до 07.09 занижены |
| «Справочник LM», лист «Артикулы» | новый артикул и номера Liqui Moly (Д) | новый товар | товара нет в Artikel |
| OZON_UE Adapter Catch-up xijbGRJS2apq61ls | даты в узле 01_Dates, ручной запуск (ПП) | после упавшей ночи | дыра в sales_raw_operations; пропуск 01.10 не закрыт (Д) |

## 6. Чего нет

| Данные | Нужны для | Почему нет |
|---|---|---|
| остатки FBS и FBO | оборачиваемость, прогноз | не делали; метод есть только в выключенном «Контроль FBS Ozon» oJrg4XY0HZwPCq59 (ПП) |
| реклама по SKU | полная прибыль | ни одного воркфлоу; «Параметры»: реклама пока не в данных (П). Гипотеза (не проверена): нужен отдельный ключ Performance API |
| текущие цены, скидки, тарифы комиссий | калькулятор цены, правило «Ozon не выше WB» | /v5/product/info/prices читает только ручной инструмент u06p (П); ежедневно не делали |
| заказы до доставки, отмены | ранний сигнал | не делали; начисления приходят по факту |
| причины и статусы возвратов | `labs/ozon-ue/t-returns-dynamics.md` | не делали; деньги возвратов в начислениях есть (П) |
| конверсия | — | ежедневный SElT снят, NTNN ручной (П) |
| всё по кабинету ИП | учёт ИП | ключ есть, не привязан (раздел 2) |

Логистика, комиссия, эквайринг, хранение, штрафы по отправлению — есть, в начислениях (поля delivery_total, type_ids; П).

## 7. Документация

Строка PASSPORT в описании воркфлоу (П): есть у J0v5swjXLfiANJa2, c7TIdv32dHV3MBRU, BPVFEmZF6QxXuTB6, u06pa4u5sDYdQD3W, SElTcMg3BpY6pmdo, 5MDOGVCTxwDjHqy3. Нет у aVpgEnYBAgIIss4k (паспорт есть, устарел — Д), nNNJuafLqTX7g8TU и YkUb5SnLtEaTctoH (паспорта в каноне — Д), у MPzPrtsnPtf0sVQo, NTNN2Kvqg09yoRKi, xijbGRJS2apq61ls, PWFVE0UbM3ajvVFc, 2UsyP3q5Jd9OafJD и выключенных инструментов. Документы паспортов не открывались.

Не описано в каноне или описано неверно (на 2026-10-24):
1. DECISION_ENGINE из строки архитектуры мастер-промпта и INDEX — объекта для Ozon нет; в снимке n8n Decision Engine только у WB FBS (П).
2. Ozon_Hashtag_Generator KQqajdrYKxle9JRe — активен, пишет книгу 1MfVmwlF2ar99Zo6k28VqNoI_CfE55sHbaoKEUKW3Yic, ни в одном проекте канона не ведётся (ПП).
3. NsOOnadQGNlbxf6g (Fix Category in OzonRawАналитика) — закрыт для MCP, не прочитан.
Исправлено тем же днём в `labs/ozon-ue/INDEX.md`: строка об источнике адаптера, книга ozon_raw_конверсия, лист «Поправки штук», скрипт книги «Цена» 1ozb26DZb9VspKXoKt50bdfBrhAVkBtZFKdZVf83VTuMDvOYtGGReELEr.