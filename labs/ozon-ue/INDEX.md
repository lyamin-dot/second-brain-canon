labs/ozon-ue/INDEX.md

# INDEX_ozon-ue — список живых задач лаборатории OZON_UE

Лаборатория, не летопись: у темы «юнит-экономика Ozon» финиша нет, задачи независимы (`second-brain-git` 4б.1). Тел задач здесь нет — только строка сути; тело каждой в своём `t-*.md`.

Заведена 2026-09-30 переносом Зоны А OZON_UE_INDEX (Google Doc 13gg5K9lGx_ypJZdnt-Fe8xFtShWYYFI9uEtClPNsjhQ) по решению Андрея 2026-09-28 (позиция AH-11 очереди); «Условие снятия» и «Следующий шаг» в задачах, где в источнике нет слов «Готово =», сформулированы переносом из текста источника; слова источника — только там, где они процитированы дословно. Зона Б документа (хроника решений и прогресса, накопленный опыт) в repo не переносилась и остаётся в Docs — как Зона Б SYS_INDEX; решение Андрея 2026-09-30 в чате переноса. Из неё взяты только незакрытые записи: дефекты (задачи `t-old-calc-sheets-fate`, `t-n8n-ozon-workflow-defects`, `t-raw-book-hygiene`, `t-master-map-ozon-sku`, `t-lm-decl-master-defects`, `t-books-followups`). Счёт переноса и адрес каждой невзятой записи — `projects/git-migration/NOT_TAKEN.md`, раздел «OZON_UE_INDEX». Число строк здесь не пишется: оно равно числу строк таблицы ниже (в ней 13 задач и два списка — идеи и вопросы).

Колонка «заведена» — дата появления задачи в источнике, провенанс; прочерк — даты не было. Возраст считается по дате последнего коммита файла (4б.8), лежалой помечается не тронутая более 30 суток.

## Постоянные адреса лаборатории (справка, не задача)

Взято из Зоны А источника без изменений; читатель — сессия лаборатории на старте. Отступление от 4б.3 (в INDEX только список): без этого блока сессия, читающая только INDEX, теряет ID книг и документов; решение владельцу — оставить или вынести.

ПРОЕКТ: Юнит-экономика Ozon — прибыль, издержки, аналитика SKU.
Client-Id: 559661 | Поставщик: Аллея Групп | SKU: ~300
АРХИТЕКТУРА: API → n8n → RAW Sheets → Unit Economics → DECISION_ENGINE
Точная юнит-экономика по Ozon — от данных до решений по ценам.

Связи:
[LM_DECL] → поиск и сопоставление деклараций соответствия выделены 2026-10-01 в проект-летопись `projects/deklaration-ozon/` (решение Андрея, чат 2026-10-01); задачи `t-lm-decl-scan-rollout` и `t-decl-pdf-inbox-cleanup` закрыты, в лаборатории по декларациям ничего не вести. Исключение — связь данных о товаре (артикул, ozon_sku, wb_nm_id, цена, номер декларации как ключ): она ведётся здесь, задача `t-product-data-model`, deklaration-ozon читает её по ключу (решение Андрея, чат 2026-10-02). Две задачи DECL_SAAS перенесены в deklaration-ozon 2026-10-06 (см. строку [DECL_SAAS]).
[DECL_SAAS] → монетизация мониторинга деклараций: задачи `t-decl-saas-phase0` и `t-decl-saas-starters` перенесены 2026-10-06 в проект `projects/deklaration-ozon/` (STATE.md, раздел «Перенесено из лаборатории ozon-ue») по решению Андрея; в лаборатории не ведётся.
[WB_UE] → общая задача: гибридная архитектура исторических констант (cost_price, params_history) проектируется сразу под Ozon и WB.
[Price Master 1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk] → предоставляет sku_cost_Шаблон!SKU_Artikel через Ozon_SKU_Staging (gid 1524622105) и воркфлоу J0v5swjXLfiANJa2.
[Главная таблица товаров] → Price Master, лист Artikel (решение Андрея 2026-10-02): наш артикул, номера Liqui Moly, SKU Ozon, карточка WB (L), номер декларации в карточке WB (M), статус «продаётся / не продаётся» (N). Корень списка — книга «Справочник LM …» (сейчас «Справочник LM 2026.08.20» 1UBiXDZDHfMwxK3Q6mDRYaG65MjnIF2K7ygZhWhOPumY), её ID Андрей вписывает в ячейку J3 листа Акт.цена книги «Актуальные цены Lique Moly» при каждом новом прайсе. Все карточки WB — лист WB_Cards_Staging (ключ nm_id), робот fGHfVrI58Ws1wfTw ежедневно 04:10 МСК. Задача `t-product-data-model`.

Инструменты:
DOCS_FOLDER: 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ
Паспорт SKU Artikel Map → 1aKPiIDTTtIkxIJoARXWJzHfJLiwnwT70zAprs8PftN8
Паспорт OZON RAW Konversion Sync (SElTcMg3BpY6pmdo) → 1qAScnksy_097CBM9C7j5MG_DkBWipcgdmgUyfqousKI (зарегистрирован 2026-09-13; с 25.08.2026 429, детали в паспорте ЗОНА В) [в n8n снят с публикации: снимок registry/n8n-map.md 2026-10-04 показывает inactive; записано 2026-10-05]
Паспорт Ozon RAW Accrual Sync (aVpgEnYBAgIIss4k) → 1hcAxLuj3YBSPUrOe8bYNbFD6ib8r7y56Pv1Ad8j1j8w (создан 2026-09-17; пометка «НЕ production-ready» в паспорте устарела: воркфлоу активен и с 08.09.2026 питает адаптер BPVFEmZF6QxXuTB6 в бою, данные в sales_raw_operations по 04.10.2026; паспорт не обновлялся — записано 2026-10-05)
Паспорта адаптера BPVFEmZF6QxXuTB6, «Получение SKU Ozon» J0v5swjXLfiANJa2 и Accrual Types Sync c7TIdv32dHV3MBRU здесь не записаны: есть ли они в DOCS — не проверялось (2026-10-05)
Техдок SKU_Artikel_Map + MASTER_MAP → 1Y-__wFnv_60-w3JWZ6aqlqKRtRZTo91AmbCNmFmjEmQ
SKU_ARTIKEL_MAP_SHEETS: 1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU
OZON_ANALYTICS_DASHBOARD_SHEETS: 1hyhR4cktHgdl2jwugf-h6M5JkJ4SxZfLdw8eBD9Vy9A — таблица Ozon_Analytics_Dashboard (папка 1fmQoSplX9Y-1FX2QRS0PD6nsJWGa-Qol; modifiedTime на момент регистрации 2026-03-17) [ВЫВЕДЕН ИЗ РАБОТЫ 2026-09-28 решением Андрея: его вопросы закрывают книги «Цена», «Деньги», «Товары»; не считает с 23.08.2026]
OZON_ANALYTICS_DASHBOARD_TECHDOC: 1YP6n558FedJMtJrYBrQNBx-S2lZvP9UYmTOrV0yM0Vs — «Тех.документация к файлу Ozon_Analytics_Dashboard» (та же папка; modifiedTime 2026-03-11). Зарегистрировано 2026-08-08 в CORE Р.2 и здесь. [документ выведенной из работы таблицы, 2026-09-28]
Техдок sku_cost_Шаблон → 1y1gp2txlOZh330cIr2DB8zi-8A1Zg2pyt7dCSd3vDzk
sku_cost_Шаблон SHEETS: 1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4 [РЕШЕНИЕ Андрея 2026-10-06: книга целиком — расчётные листы и монитор oz_* — заменяется книгами «Цена», «Деньги», «Товары» и не сопровождается; из неё ещё читаются cost_price_history (книги «Деньги»/«Товары», перенос в Price Master — t-cost-history-copy) и SKU_Artikel (адаптер BPVFEmZF6QxXuTB6, узел 01D); задачи t-old-calc-sheets-fate, t-weekly-commissions-deferred, t-oz-dashboard-reference-block, t-ozon-raw-mirror-grid закрыты 2026-10-06]
Книга «Цена» SHEETS: 1j_qIlvowDIWMJfxq8Ydag3WTLsstoyeA-eEFgGQoycg — калькулятор цены, листы «Калькулятор цены», «Сборы по товару», «Параметры»; скрипт oz_price_book.gs привязан к книге (меню «Ozon · Цена»); источники: sales_raw_operations (1P-Ggi…), «Актуальные цены Lique Moly» 17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU, Price Master!Artikel (зарегистрировано 2026-09-28)
Книга «Деньги» (Geld Ozon) SHEETS: 1lBySm-BuN9h3S6RGHBrrBkJJtQpgdNmBEKrnjjqbvWQ — листы «Куда ушли деньги», «Что-если», «Деньги по неделям», «Деньги по месяцам», «Параметры», «Поправки», «Деньги · лента», «Деньги · месяцы»; скрипты привязаны к книге: oz_money_book.gs (меню «Ozon · Деньги», недели и месяцы) и oz_money_tape.gs (ленты, buildMoneyTape и buildMoneyTapeMonths; добавлено 2026-09-29) (зарегистрировано 2026-09-28)
Техдок книг «Цена», «Деньги», «Товары» (агентская, англ.) OZON_UE_BOOKS_TECHDOC_EN → 1W2HvOYwAA79WAq_CzRaJEqWBw0NnPVvX-dNHuFUsGj4 (папка DOCS; создан 2026-09-28). Русская версия для человека — Claude Doc https://claude.ai/code/artifact/f9549fbd-4632-41e7-ad3d-e9a3d908e75f
Обзор системы юнит-экономики Ozon для читателя с нуля (данные, конвейер, книги, модель товара, смежные проекты, 16 слепых мест, порядок развития) OZON_UE_OVERVIEW_2026-10-05 → 1VWBJQW4EkcjPVHGY3sZ0Nqnsrs75RQ86vFsMg0Xt7L8 (папка DOCS; снимок на 2026-10-05, без схем). Живая версия с двумя схемами — Claude Doc https://claude.ai/code/artifact/a78ab852-2175-4d77-a7b0-be8bda3adee0
Книга «Товары» (WarenOz) SHEETS: 1KN62zamEcLYzm3OrYtoloCzHnhpLA7g2oWr-YRfiTSM — листы «Товары за период», «Что-если по товару», «Классы по месяцам», «Параметры», «Убытки», «Убытки · строки» (с 2026-10-06); скрипты oz_goods_book.gs ред. 3 и oz_goods_losses.gs (меню «Ozon · Товары») (зарегистрировано 2026-09-28)
Разбор убыточных товаров 06.10 (для человека, с разделом «Как пользоваться листом «Убытки»»): живая версия — Claude Doc https://claude.ai/artifact/B2ff3ZuLny6CzxBTqYoLb5; выгрузка в Google Doc 1upMJTjN7VaIy_6KjSIG-1L6F0-gv4mTb0xXOHxAZBf0 (снимок 2026-10-06, записано по просьбе Андрея); задача `t-loss-analysis`
Справочные копии кода книг (папка DOCS, простой текст, 2026-10-06; истина — скрипты, привязанные к книгам): oz_goods_book.gs ред. 3 → 1tCFyFFBqbO-YNX7nvxQX95p1L8XsZnK5; oz_goods_losses.gs → 11Me7GS1oQpvQkI9GW1lrcp2h8e9zSdaw; oz_price_book.gs ред. 5 → 1PxwH6KDs1JURgpTYa_bFs1VRiXkEp5vq. Список и правило замены — раздел CODE техдока OZON_UE_BOOKS_TECHDOC_EN; копий скриптов книги «Деньги» нет
LM_DECL_MASTER — техдокументация таблицы (агентская, англ.) LM_DECL_MASTER_TECHDOC_EN → 1_tOucfOnJ_BFCWK3eEmP9w5qpuvHtRuHT3MYgWzTp8g (папка DOCS; создан 2026-09-28). Русская версия для человека — LM_DECL_MASTER — техдокументация (RU) → 1Z6wbrh_W0R0_mqDNujihr_dZqKNfYC3h7cTrciWMapM (папка DOCS; создан 2026-09-28)

Добавлено переносом (в источнике нет): книга RAW с листами `sales_raw_operations`, `ozon_raw_accrual_TEST`, `ozon_accrual_types` — 1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4. В строке «Книга «Цена»» источника этот ID обрезан («1P-Ggi…»); полный взят из `skills/n8n-workflow-registry/SKILL.md`, строка 75.

## Задачи

| файл | суть | метка | заведена |
|---|---|---|---|
| `t-dup-2006.md` | дубль 20.06.2026 в `sales_raw_operations`: 233 строки, неделя 15.06 книги «Деньги» завышена на 53 705,01 ₽ | РЫЧАГ | 2026-09-30 |
| `t-adjustments-rows.md` | лист «Поправки штук» книги RAW: перезаписать строку 539 и добавить строку 1131 | РУТИНА | 2026-09-30 |
| `t-goods-book-script.md` | `oz_goods_book.gs`: поправки штук, раскладка «Денег»; активная эстафета «месяцы-Деньги-29.09» | РУТИНА | 2026-09-30 |
| `t-cost-history-copy.md` | «Деньги» и «Товары» читают `cost_price_history` из тяжёлой книги — перенести на копию в лёгкой | РЫЧАГ | 2026-09-30 |
| `t-returns-dynamics.md` | динамика возвратов по SKU по неделям в книге «Товары» | РЫЧАГ | 2026-09-28 |
| `t-price-ozon-vs-wb.md` | правило: цена Ozon не выше цены WB, формула в калькуляторе цен | РЫЧАГ | 2026-09-28 |
| `t-ozon-ip-cabinet.md` | подключить кабинет Ozon ИП: ждёт credential ИП и сервисный аккаунт Google в PWFVE0UbM3ajvVFc | РЫЧАГ | 2026-09-28 |
| `t-history-constants-design.md` | гибридная архитектура исторических констант Ozon + WB — дизайн книги «Деньги» | РУТИНА | — |
| `t-n8n-ozon-workflow-defects.md` | открытые дефекты воркфлоу n8n цепочки Ozon (скан 2026-09-28) | РЫЧАГ (метки в источнике нет) | 2026-07-24 (сводная; самая ранняя запись) |
| `t-raw-book-hygiene.md` | книга RAW: шапка AB/AC, лист «Лист3», провал строк в июле | РУТИНА (метки в источнике нет) | 2026-09-28 |
| `t-product-data-model.md` | единая модель данных товара: главная таблица Price Master!Artikel, карточки WB в WB_Cards_Staging, статус «продаётся»; шаги 0–3 сделаны (новые номера Liqui Moly дописывает в LM_DECL робот LM_DECL Intake qKgc8hhOLwehejYp, 05:30 МСК); колонки X/Y в Artikel работают (Y учитывает ЕАЭС и РОСС), исправление номеров в карточках WB ведёт deklaration-ozon; дальше — приёмка по Artikel!Y и накопитель документов карточек Ozon | РЫЧАГ | 2026-10-02 |
| `t-master-map-ozon-sku.md` | MASTER_MAP: `ozon_sku` = 0 у артикулов 1908 и 2203 | РУТИНА (метки в источнике нет) | 2026-09-28 |
| `t-books-followups.md` | хвосты книг «Деньги» и «Товары»: ABC-переход, падение прибыли 31.08–27.09, перенос «Поправок» | РУТИНА (метки в источнике нет) | 2026-09-28 |
| `t-loss-analysis.md` | убыточные товары: разбор 06.10 — за 30 дней в минусе 20 товаров на −16 808 ₽ (цена ниже безубыточной на 0–16%), лист «Убытки» в книге «Товары»; возвраты решены (товар годен, закупка возвращается); открыты решения по Ventil Sauber и «Сбору первых отзывов» и правка диагноза «возвраты» книги «Товары» | РЫЧАГ | 2026-10-06 |
| `t-ideas-backlog.md` | семь живых идей (SKU Stock Forecast, Price API, Postgres и др.) | — | 2026-09-28 |
| `t-open-questions.md` | шесть вопросов без ответа (аллокация склада, other_cost и др.) | — | 2026-08-22 |
