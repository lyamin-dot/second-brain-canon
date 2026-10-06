meta/PRODUCT_DATA_HIERARCHY.md

# Иерархия таблиц товарных данных (Liqui Moly, Ozon, Wildberries)

Читатель: любая сессия любого проекта, которой нужен список товаров, их ключи или номера деклараций. Мастер-промпт проекта для этого не нужен: файл самодостаточен. Решение Андрея от 2026-10-02, подтверждено 2026-10-06. Обоснование — Google Doc DESIGN_единая_модель_данных_товара (1hhO6Vd5WNNmxzPfIEvvcfWeaehf0ns0FdI6imSrpNVM, 2026-10-02). Состояние описано на 2026-10-06. Ведёт лаборатория ozon-ue, задача labs/ozon-ue/t-product-data-model.md. Если файл расходится с живой таблицей, прав таблица, а расхождение записывается в эту задачу.

## 1. Главное правило

Список товаров и связь «наш артикул → номера Liqui Moly → SKU Ozon → nmID Wildberries → номер декларации» читается из ОДНОЙ таблицы: Price Master (1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk), лист Artikel. Ключ товара — наш артикул (число из 4 и более цифр). Другие копии этой связи источником не являются.

## 2. Иерархия таблиц

1. Корень: «Справочник LM 2026.08.20» (1UBiXDZDHfMwxK3Q6mDRYaG65MjnIF2K7ygZhWhOPumY), лист «Артикулы». Единственное место, куда Андрей вручную вносит новый артикул и номера Liqui Moly. ID действующего справочника лежит в ячейке J3 листа Акт.цена книги «Актуальные цены Lique Moly» (17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU); при новом прайсе Андрей вписывает туда новый ID.
2. Промежуточные копии через IMPORTRANGE: Акт.цена, затем WB_RAW_Аналитика (14QMHYMM4mZRnnq1wHQA4_SA8ZnOeE1xcVJDL2h9h1Pk), лист sku_cost. Данные о товаре отсюда не читать и не править.
3. ГЛАВНАЯ ТАБЛИЦА: Price Master, лист Artikel. Читают все.
4. Накопители рядом с ней (пишут роботы n8n, Artikel подтягивает их формулами): Ozon_SKU_Staging (воркфлоу J0v5swjXLfiANJa2, ночью) и WB_Cards_Staging (воркфлоу fGHfVrI58Ws1wfTw, ежедневно в 04:10 по Москве; колонки nm_id, vendor_code, our_sku, brand, subject, decl_no). Остальные листы Price Master: CURRENT, HISTORY, SUPPLIER_RAW.
5. Декларации: LM_DECL_MASTER (1PO7vNyoY16tYqpU_KB5xuK4aSAbOU7YW_MM0scg5ksY), ведёт проект deklaration-ozon. Ключ там — номер Liqui Moly (article_1, article_2), не наш артикул. Номера Liqui Moly проект берёт из Artikel.
6. Выводится из эксплуатации: SKU_Artikel_Map (1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU), лист MASTER_MAP, снимок от 19.06.2026. Не источник, вручную не дописывать. Перевод читателей на Artikel не закончен: WB Sync (QCQI6utFFH3dvTJT) и Ozon Upload (BLNA8sbdnLtuz7Uj) читают его до сих пор, воркфлоу «Получение nmID WB» (gglEq5U90Gt3sI7h) пишет в него nmID, загрузчик WB (qrZw8bxIEpRAUwEe) читал его по документу DESIGN от 2026-10-02.

## 3. Колонки Artikel

A sku (наш артикул, ключ), B wb_nm_id, C wb_barcode, D ozon_product_id, E ozon_sku, F LM_ID_1, G LM_ID_2, H product_name, I wb_last_seen, J offer_id, K name, L wb_card (nmID из WB_Cards_Staging), M wb_decl_no (номер декларации в карточке WB), N status («продаётся», если есть SKU Ozon или карточка WB). Колонки A–N читают роботы: посреди них колонки не вставлять и не переставлять. O:S — ручная вставка старого снимка Ozon, не трогать. X lm_decl_no (декларация по номеру Liqui Moly из LM_DECL) и Y wb_decl_check (совпадает ли номер в карточке WB) добавил Андрей.
<<<ПРОДОЛЖЕНИЕ>>>
