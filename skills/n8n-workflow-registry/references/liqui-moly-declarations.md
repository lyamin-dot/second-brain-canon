# Декларации Liqui Moly

Часть Skill `n8n-workflow-registry`. Читать: работа с декларациями Liqui Moly — конвейер, выписки, страница товара.

- Скрипт `processDeclPdfInbox` снят — не запускать.
- Действующий конвейер — `meta/DECLARATION_SCAN.md`; снятое и невзятое — `projects/deklaration-ozon/NOT_TAKEN.md`.
- Проверка страницы товара по полю `sku` — Skill `n8n-engineering-manual`, «Стоп-правила», подраздел «HTTP, пагинация, время», и мастер-промпт deklaration-v2 (`meta/prompts/deklaration-v2.md`, пункт 9a).
