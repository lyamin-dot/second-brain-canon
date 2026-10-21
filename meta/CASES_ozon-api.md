meta/CASES_ozon-api.md

# Ozon Seller API — факты, установленные исполнениями

Домен — поведение Ozon Seller API, верное для любого кабинета; читатель — сессия, которая строит или чинит воркфлоу, ходящий в Ozon. Правила записи и проверки — Skills `n8n-engineering-manual` (R4) и `second-brain-git`; здесь только факты API с адресами.

Перенесено 2026-10-21 из Skill `n8n-workflow-registry` при разборе его по носителям (задача `projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md`, отчёт `meta/SYNTHESIS_n8n-workflow-registry_2026-10-21.md`); текст строк не правился, прежнее место — зеркало `skills/n8n-workflow-registry/` на коммите b91fb1e, SKILL.md, строки 115, 116, 119–127, 130–134, 138, 139, и references/cards-and-declarations.md, строки 50, 52, 54, 55; остальные строки тех же разделов лежат у других носителей — перечень в отчёте. Пометка `[снимок ДД.ММ]` значит «сверено со строкой registry/n8n-map.md на эту дату», `[владелец ДД.ММ]` — «со слов Андрея»; строка без пометки набита руками и могла устареть.

Ссылки строк ниже на подраздел «Внешние источники» и на «SKILL.md, «Внешние источники»» ведут теперь в `meta/CASES_external-access.md`.

## Общее, отзывы и вопросы

- Ozon кладёт ошибку в тело ответа при коде HTTP 200. Примеры: `{"code":9,"message":"obsolete method cannot be used"}` у отключённого `/v3/finance/transaction/list` — исполнение при этом success с нулём строк (labs/ozon-ue/t-n8n-ozon-workflow-defects.md); `PermissionDenied` «not available with existing subscription» на публикации ответа на отзыв (projects/n8n/STATE.md). Поэтому тело ответа проверяется на поля `code` и `message`, а итог — по объекту. Общее правило «результат по объекту, не по статусу» — корень R4 (успех по статусу при отказе по существу) в n8n-engineering-manual.
- Лимит частоты Seller API считается на Client-Id, а не на воркфлоу: все воркфлоу, которые ходят в Ozon с одним Client-Id, делят один счётчик; у второго кабинета (другое юрлицо) свой Client-Id, значит и свой счётчик. Общий лимит — 50 запросов в секунду на все методы с одного Client-Id, с 22.05.2025 (прежде 10); превышение даёт 429 «You have reached request rate limit per second». Источник — официальный канал новостей Seller API в Telegram (t.me/s/OzonSellerAPI, сообщения 485 и 491); саму документацию Ozon из сессии не прочитать (подраздел «Внешние источники» ниже). Сверх общего у отдельных методов свой, более низкий потолок, и он назван в тексте ответа 429: `/v1/analytics/data` в августе 2026 отвечал «rate limit exceeded for `seller-api` client, current max rate per sec.: 2». С 24.02.2026 операции с товарами (`/v3/product/import`, `/v1/product/update/offer-id`, `/v1/product/pictures/import`, `/v1/product/import-by-sku`) ограничены 30 000 товаров в минуту на все четыре метода вместе; запрос, в котором товаров больше остатка, отклоняется целиком с текстом «You have reached operation items limits» (пересказ avoshop.ru от 18.02.2026, первоисточник Ozon не прочитан). Поэтому 429 при одном запросе за прогон — не дефект этого воркфлоу и паузой внутри него не лечится: диагностика начинается с текста ошибки (какой лимит назван) и с суммы запросов всех воркфлоу того же Client-Id в том же окне времени; пауза между пакетами внутри воркфлоу уменьшает только его собственный вклад. Основание: 1 случай, 2026-08-25 — шесть из шести плановых прогонов OZON RAW Konversion Sync (`SElTcMg3BpY6pmdo`) 20–25.08.2026 упали 429 при одном HTTP-запросе за прогон, на том же Client-Id было ещё 12 активных воркфлоу (отчёт REPORT_H-25.08-01, раздел 2, ID — registry/documents.md; урок У-77 журнала projects/archivarius/LOG.md, запись Р-13).

- Поля `pros`, `cons`, `text` раздельные; статус `rejected` возможен.
- Публикация отзыва: POST `/v1/review/comment/create`, задержка 4 секунды между запросами.
- Маппинг `operation_type` → узел `06C_Map_Operation_Category`, обычный объект JS. Новый тип добавляется в словарь; неизвестные дают `'Не классифицировано: ' + opType`.
- Эндпоинты вопросов идут БЕЗ `/product/`: POST `/v1/question/list`, `/v1/question/answer/create`, `/v1/question/answer/delete`.
- Публичный ответ на карточке закрыт без тарифа Premium Plus (порядка 25 тысяч рублей в месяц); ответ через чат `/v3/chat/` виден только самому покупателю.
- Вебхука `TYPE_NEW_QUESTION` не существует.
- Стоп пагинации `/v1/review/list` — любое из трёх: пустой массив, `last_id` не изменился, длина меньше `limit`.
- Встроенная пагинация HTTP-узла для транзакций: `paginationCompleteWhen: other`, `completeExpression: ={{ $response.body.result.operations.length < 1000 }}`.
- Ограничение частоты примерно один запрос в секунду: Items per Batch = 1, Batch Interval = 4000 мс.

## Начисления (accrual)

- POST `/v1/finance/accrual/by-day`, тело `{date, last_id}` → ответ `{accruals:[...], last_id}`. Пагинация останавливается, когда `last_id` пришёл пустой строкой, НЕ по длине массива.
- `accrued_category` принимает `POSTING`, `ITEM`, `NON_ITEM`; у каждой своя вложенная форма объекта.
- Наблюдаемая формула нэттинга: `sale_amount + sale_commission + delivery.total_accrued = total_amount`.
- `container_fees` ни разу не приходило непустым; статус поля неизвестен.
- Ловушка совместимости с `/v3/posting/fbs/get` (вход `{posting_number}`): валидный `posting_number` даёт только `unit_number` из записей с `accrued_category=POSTING`. Взятый из `ITEM` или `NON_ITEM` даёт 404 в 85–91 проценте случаев.

## Ключи строк RAW-слоя Ozon

- Ozon, транзакции — `business_date|operation_id`
- Ozon, начисления — `accrual_id`

## Декларации — дополнение к `projects/deklaration-ozon/PLAN.md`

- Для типа DECLARATION стандарт — только `NATIONAL` или `EAEU`. Что значение прошло проверку Ozon, не значит, что оно верное: `EAEU` для декларации РОСС Ozon принял (projects/deklaration-ozon/LOG.md, Т-5, Р-16) — стандарт выводится из номера документа.
- `page_size` у `/v1/product/certificate/list` — не больше 100. У `/v1/product/certificate/products/list` поле `limit` от 1 до 1000, `page_size` не годится; по товару он отдаёт только `product_id`, `sku`, `product_status_code`, причину отказа не отдаёт (projects/deklaration-ozon/LOG.md, Т-4).
- Статус документа `approved` не значит, что товары одобрены: Ozon проверяет каждый товар отдельно, порядка 10 дней; итог перечитывается отдельным режимом «статус» (projects/deklaration-ozon/LOG.md, Р-36). Вкладки кабинета «На проверке», «Отклонены», «Одобрены» фильтруют статус документа, а не товаров: документ с зависшими товарами стоит в «Одобрены», зависание видно только по колонке «Одобрено товаров» (projects/deklaration-ozon/PLAN.md).
- Факты этого раздела сняты с полного swagger.json, прочитанного в браузере 2026-10-01, и проверены вызовами; из сессии документацию Ozon прочитать нельзя (SKILL.md, «Внешние источники»).
