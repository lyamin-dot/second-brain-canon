projects/wb-ue/PLAN.md

# PLAN_wb-ue — цель, архитектура, инструменты (правила проекта)

Перенесено из WB_UE_INDEX (Google Doc `1qY2bB8VZtepPQCp0uZQ6hzO4a2SsE-_ooHnghYHjuZY`, снимок на дату переноса 2026-09-28: driveSize 18617 Б) по протоколу `meta/PROTOCOL_file-migration.md`, этап 0в. Что не взято и почему — `projects/wb-ue/NOT_TAKEN.md`.

## ЦЕЛЬ

Юнит-экономика по Wildberries — отдельный трек от Ozon. WB — основной источник прибыли, менее оцифрован.

Архитектура: WB API → n8n → RAW Sheets → Unit Economics (WB_Аналитика).

## СВЯЗИ

- [N8N] → WB RAW Finance Sync V.3 (`IvgysDKrq3UISYEY`, еженедельный, среда 10:00 МСК), WB RAW History Load V.3 CLEAN (`Iis5dlRS1GWZqQXD`, backfill истории), WB Reports Official Sync (`P7CZYJZWIqC5Me4c`, эталон официальных отчётов WB), WB Monitor Telegram Reader — бывший WB Reconciliation Reader (`DcIqwTVqBqMQyigs`, читатель сверки → Telegram).
- [OZON_UE] → Price Master (`1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk`) — общий источник цен с проектом OZON_UE.

## ИНСТРУМЕНТЫ (архитектурные факты; текущее состояние и находки — `STATE.md`/`LOG.md`)

**WB RAW Finance Sync V.3** — `IvgysDKrq3UISYEY`. Расписание: среда 10:00, еженедельно, окно — прошлая неделя понедельник–воскресенье (узел `01_Set_WOCHE_Range`). Error Workflow: `M5BLqclKBjGTpz33` (🚨 Error Notifier), задан.

**WB RAW History Load V.3 CLEAN** — `Iis5dlRS1GWZqQXD`. Псевдо-ручной запуск (расписание раз в 100 месяцев), API v1, история залита полностью. Диапазон задаётся жёстко в узле `01_Set_History_Range` (на 28.09: `2026-09-07…2026-09-07`). Пауза между неделями — Code-узел `03_Wait_API_Limit`, 75 секунд внутри цикла. Пагинации нет. Узел `11_Write_RAW_To_Sheets` выключен — пишет только слой транзакций (`15_Write_Transactions`, appendOrUpdate по `tx_key`). Error Workflow не задан.

**WB Reports Official Sync** — `P7CZYJZWIqC5Me4c`. Среда 12:00 МСК, timezone задан, Error Workflow задан, активен. Тянет `sales-reports/list` за окно `WINDOW_DAYS = 400` в лист `wb_reports_official` (17 колонок, appendOrUpdate по `report_id`). Живость подтверждена: `synced_at` в `wb_reports_official` — `2026-09-16 12:00:13` и `2026-09-23 12:00:13`. Примечание: в комментарии кода и описании воркфлоу ещё указано окно «120 дней» — устарело, актуально `WINDOW_DAYS=400`. Шапка листа — контракт: переименование колонок молча ломает autoMapInputData.

**WB Monitor Telegram Reader** (бывший WB Reconciliation Reader) — `DcIqwTVqBqMQyigs`. Два триггера — ежедневно 10:00 и понедельник 09:00, timezone не задан. Читает лист `dashboard` (C79 — текст тревоги, C80 — недельная сводка, A84:C137 — строки графика), а не `weekly_history!B33:C34`. Шлёт в Telegram `6054723832`. Error Workflow не задан.

**🚨 Error Notifier** — `M5BLqclKBjGTpz33`. Подключён у `IvgysDKrq3UISYEY` и `P7CZYJZWIqC5Me4c`. Не подключён у `Iis5dlRS1GWZqQXD` и `DcIqwTVqBqMQyigs`. Сохранённых исполнений ноль (SAVE_ON_SUCCESS=none на инстансе) — пустая история ≠ «не запускался»; живость проверять по данным (synced_at, новая неделя в weekly_history), не по списку исполнений.

**WB_Аналитика** (Google Sheets). 14 листов: `dashboard`, `как_читать`, `cost_monitor`, `weekly_history`, `sales_unit_economics`, `sales_sku_profit_ranking`, `sales_abc_profit_analysis`, `sales_sku_efficiency_matrix`, `sales_growth_opportunities`, `_data`, `wb_reports_official`, `_map`, `_refs`, `_dashboard_backup` (сверено 28.09, листа `_dashboard_backup_conflict1561150441` больше нет). Период расчёта: `dashboard!K3 = DATE(2026;1;1)`, `dashboard!K4 = TODAY()`. Формулы и оформление правит только скрипт `WB_Monitor.gs` (Расширения → Apps Script книги, исходник живёт в книге, в Drive отдельно не хранится). Ручная правка ячейки стирается следующим прогоном `setupAll`.

**Price Master**: `1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk` | Документация: `13qo8xl-Hg0Xpvq02QmlWbe2raogsMrl3Q8CXuZkibVg`. `sku_price_calculator` создан 2026-06-09, документирован (docx). `sku_fees_map` — вспомогательный для калькулятора, создан 2026-06-09.

**DOCS_FOLDER**: `1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn` — папка паспортов и ранбуков проекта.

Паспорта воркфлоу: WB RAW Finance Sync V.3 → `1GWR2SwPYlyl6T_frXYRDi_kVpyx7wBgIimEGZGOiacI`; WB RAW History Load V.3 CLEAN → `12oBjTa2nSWjX1UBf1L07IM3mNcdGPplvlx89r3R2uR8`; WB Reports Official Sync → `1prHzpt-wWl-SVFwnR8N0CG7VgVue4ZGLvEPBgVBhtN8`; WB Monitor Telegram Reader → `1LOGZGKFHV6CoDYcUEvi9unGYM9vzWy-A7YNg24YqfmU` (имя файла паспорта ещё «reconciliation-reader» — долг на переименование, см. `STATE.md`).

РАНБУК «Расхождение витрины с отчётами WB» — читать первым при любом расхождении: RU `1dcneWnN81XlMGygkpZk2KPJy1e6daQJBQWFUhjp1Omo`, EN `1Qo70VGg8FxeJeDDvbC0VIhPGi5o2Vj167YRozdiO_zE`. Правило поддержания: новое название операции WB или новый тип строки — дописывать в обе версии.

ДОКУМЕНТАЦИЯ КНИГИ WB_Аналитика — читать первым при любой работе с книгой: RU `1E-RlQjYjTVpCgHWRVAjwJl8ZkTxi01tYRnNnsndDq04`, EN `170lL6pdsROdkxa5Cjb8ad02powoywufg4f7HXSoplBw`. Парный Skill: `apps-script-sheets`.

КОНСТРУКТОР ВИТРИНЫ (норма → отклонение → светофор, для переноса в другую книгу): RU `10f6nbTUWMZQJm2dApneCuZEiLPCRE-CoukI3ihRCpoI`, EN `13uULDvR5l5aBUsEM7vR93_GXk_OvU7HZkBEyDQozvsw`. Правило поддержания то же — обе версии.
