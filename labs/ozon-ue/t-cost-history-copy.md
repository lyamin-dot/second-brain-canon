labs/ozon-ue/t-cost-history-copy.md

# Книги «Деньги» и «Товары»: читать cost_price_history из лёгкой копии

Суть: обе книги читают `cost_price_history` из тяжёлой `sku_cost_Шаблон` ради одного листа (3 701 строка). Прогон книги «Деньги» 30.09 12:38 упал на шаге «чтение истории закупки»: `sku_cost_Шаблон` не отвечала 349 с, ответ Google «Document … is missing (perhaps it was deleted…)», хотя файл на месте (Drive metadata, gsheets-read exec 72163 за 11 с); повторный прогон прошёл (заведено 2026-09-30). Связанный дефект (Зона Б, 2026-09-30): в `cost_price_history` в колонке B есть ячейки «#N/A (Did not find value '1037' in VLOOKUP evaluation.)» вместо SKU (gsheets-read exec 72170); такие строки скрипты книг пропускают; сколько строк и каких артикулов — не считалось.

Следующий шаг: перенести чтение на копию листа в лёгкой книге (например RAW); пересчитать строки с #N/A в колонке B.

Условие снятия: скрипты читают копию, прогон не открывает `sku_cost_Шаблон`.

Ссылки: `sku_cost_Шаблон` 1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4; книги «Деньги» 1lBySm-BuN9h3S6RGHBrrBkJJtQpgdNmBEKrnjjqbvWQ и «Товары» 1KN62zamEcLYzm3OrYtoloCzHnhpLA7g2oWr-YRfiTSM; источник — Зона А OZON_UE_INDEX, строка 178; Зона Б, записи 2026-09-30 (строки 1063, 1064).
