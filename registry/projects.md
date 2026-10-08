registry/projects.md

| проект | папка | носитель канона | статус | Claude Project |
|---|---|---|---|---|
| git-migration | projects/git-migration/ | repo | активен | |
| anis-evidence | projects/anis-evidence/ | repo | активен | https://claude.ai/project/01a09a12-fef3-737b-8f00-75badd522e12 |
| archive-recon | projects/archive-recon/ | repo | активен | |
| n8n-map | projects/n8n-map/ | repo | активен | |
| kontext-reduktion | projects/kontext-reduktion/ | repo | активен | |
| wb-ue | projects/wb-ue/ | repo | активен — перенос 2026-09-28, приёмка Контролёром закрыта (три круга, `projects/git-migration/LOG.md` Р-115…Р-118); источник заморожен | |
| deklaration-ozon | projects/deklaration-ozon/ | repo | активен — создан 2026-10-01 выделением из OZON_UE (лаборатория ozon-ue); Андрей, чат 2026-10-01; 2026-10-07 разделён по площадке: Wildberries ведёт deklaration-wb, общий слой — `meta/DECLARATION_COMMON.md` (Андрей, чат 2026-10-07; `projects/deklaration-ozon/LOG.md` Р-47) |
| deklaration-wb | projects/deklaration-wb/ | repo | активен — создан 2026-10-07 выделением из deklaration-ozon (Wildberries, кабинеты основной и ИП); Андрей, чат 2026-10-07; `projects/deklaration-wb/LOG.md` Р-1 | |
| wb-logistics | projects/wb-logistics/ | repo | активен — перенос 2026-10-04 из WB_LOGISTICS_INDEX (Google Doc `1mxYgiK9X4qOId2vNF7xnne-cQszTqPpJZHux_AuDZjQ`); приёмка Контролёром: перенос принят, замечания исправлены; источник заморожен 2026-10-04; мастер-промпт проекта переведён на repo (зеркало `meta/prompts/wb-logistics.md`) | https://claude.ai/project/019ea86d-05da-7731-b99f-f0f163be8182 |
| card-content-sync | projects/card-content-sync/ | repo | активен — создан 2026-10-04 из задачи лаборатории ozon-ue `t-card-content-sync.md` (наряд Н-04.10-01а); Ф0 остановлена: нет ключей API у Ozon ИП и второго магазина WB | |
| wb-reviews | projects/wb-reviews/ | repo | активен — перенос 2026-10-05 Зоны А WB_REVIEWS_INDEX (Google Doc `1D-mwjyl_rJ0ekYBSwliIRBwfOSJdJBeDi1SQddaeODc`); приёмка Контролёром: два круга, второй — принят (`projects/wb-reviews/LOG.md` Р-5); Зона Б осталась в замороженном Docs | https://claude.ai/project/019e8466-e4cb-7588-99c1-496ee2d759ed |
| n8n | projects/n8n/ | repo | активен — перенос 2026-10-06 Зоны А N8N_INDEX (Google Doc `1GktMsgl1UOIzuWj02gqDirMSYlSjiuLuDVDd9vevB5Q`); приёмка Контролёром: четыре круга, четвёртый — принят (`projects/n8n/LOG.md` Р-3); доставлено в main 1642f60; источник заморожен 2026-10-06, Зона Б осталась в Docs архивом | |

## Лаборатории

| лаборатория | папка | носитель | статус |
|---|---|---|---|
| sys | labs/sys/ | repo — Зона А SYS_INDEX (перенос 2026-09-14, ф4 git-migration); Зона Б осталась в Docs 12k2l2oT92m33PFcnlYDr1MdtkGOj7Gy5Vf7ksSw4nm8 | активна |
| ozon-ue | labs/ozon-ue/ | repo — Зона А OZON_UE_INDEX и незакрытые дефекты Зоны Б (перенос 2026-09-30, git-migration; Контролёр: 4 круга, круг 4 без дефектов; доставлено в main f8c580e, INDEX.md прочитан Каналом, blob ef1d5a33a6f09794ec8f876b5170650e609ac559, исполнение 72247); Зона Б осталась в Docs 13gg5K9lGx_ypJZdnt-Fe8xFtShWYYFI9uEtClPNsjhQ | активна — перенос принят Контролёром 2026-09-30; мастер-промпт проекта ещё читает Docs (AH-11), Зона А в Docs не заморожена |

## Проекты с INDEX в Google Docs

Проекты ниже ведут канон в Google Docs (INDEX); строка в таблице выше заводится для проекта при его переносе в репозиторий. Здесь же веса проектов для команды !priority; формула итогового приоритета — CORE Раздел 5 (`core/R-05.md`).

До 2026-09-10 — Раздел 1 CORE (`core/R-01.md`); перенесён сюда решением Р-66 журнала `projects/git-migration/LOG.md`, потому что это реестр, а не правило. Ссылка «CORE Р.1» означает эту секцию. Блоки T-002 и T-004 взяты целиком, с провенанс-маркерами; текст строк не правился, серии пустых строк сокращены до одной. Внутри блоков строка «используются при !priority для сравнения между проектами» и слово «Раздел 1» говорят о прежнем месте.

<!-- T-002 | CORE байт 136-2109 | Р.1 заголовок + ВЕСА ПРОЕКТОВ (формула, метки, 16 весов) -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
РАЗДЕЛ 1 — АКТИВНЫЕ ПРОЕКТЫ

ВЕСА ПРОЕКТОВ (используются при !priority для сравнения между проектами)
Итоговый приоритет задачи = метка x вес проекта
Метки: БЛОКЕР=4, РЫЧАГ=3, РУТИНА=2, ЗОМБИ=1

OZON_UE  вес 10  — прямое влияние на прибыль каждый день (~150к/день)
WB_UE    вес 9   — основной источник прибыли, менее оцифрован
N8N      вес 7   — инфраструктура автоматизации, влияет на всё
SERVER   вес 7   — инфраструктура сервера, влияет на всё
WB_LOGISTICS вес 7   — логистические издержки WB, активен
WB_REVIEWS вес 6   — AI-отзывы и Q&A WB, активен прямо сейчас
OZON_REVIEWS вес 6   — AI-отзывы и Q&A Ozon, активен прямо сейчас
CONTENT  вес 5   — контент для карточек товаров (инфографика, видео) WB+Ozon
WB_CV    вес 4   — не начат, ждёт WB_UE
OZON_CV  вес 4   — заморожен, ждёт Premium Plus
TRADE    вес 3   — личный проект, не бизнес
RENO     вес 3   — личный проект, не бизнес
SYS      вес 2   — мета-задача, инфраструктура системы

AUTOCHEM_BUNDLES вес 5   — комбинации товаров Автохимия для маркетплейсов (WB+Ozon)

ANAST_QUICKREF вес 3   — quick-reference по стандарту анестезиологии (личный инструмент)

ANIS_EVIDENCE вес 3   — доказательная справка по анестезиологии и интенсивной медицине (личный инструмент)

CARD_CONTENT_SYNC вес 6   — одна книга описаний карточек для четырёх магазинов Ozon и WB (папка projects/card-content-sync/; вес подтвердил Андрей 2026-10-05)

DEKLARATION_OZON вес 8   — декларации соответствия Liqui Moly в карточках Ozon (Wildberries — DEKLARATION_WB); товар без декларации не продаётся (папка projects/deklaration-ozon/; вес назначил Андрей 2026-10-06)

DEKLARATION_WB вес 8   — декларации и другие документы в карточках Wildberries, кабинеты основной и ИП; карточку без подтверждённого документа WB может скрыть (папка projects/deklaration-wb/; вес назначил Андрей 2026-10-08)

<!-- T-004 | CORE байт 2461-5539 | Р.1 карточки 14 проектов (описание, статус, реквизиты, файл индекса, Claude Project) -->

[N8N]     n8n автоматизации
          Файл индекса: 1GktMsgl1UOIzuWj02gqDirMSYlSjiuLuDVDd9vevB5Q

[SERVER]  Сервер / инфраструктура
          Hetzner CPX32 | liamin-n8n.duckdns.org
          Файл индекса: 1n5WPjZ99H9cwVj3w7FwLsvLZLiabAFIcp8fF5hzq5rY

[OZON_UE] Ozon юнит-экономика
          Client-Id: 559661 | SKU ~300 | Поставщик: Аллея Групп
          Файл индекса: 13gg5K9lGx_ypJZdnt-Fe8xFtShWYYFI9uEtClPNsjhQ

[OZON_CV] Ozon конверсия и трафик
          СТАТУС: ЗАМОРОЖЕН (ждёт Premium Plus)
          Файл индекса: 1t4DWGWB7z_4uAsGhbs8xHXvr6MI__i8A5Nc73puid3U

[WB_UE]   WB юнит-экономика
          Основной источник прибыли, менее оцифрован
          Файл индекса: 1qY2bB8VZtepPQCp0uZQ6hzO4a2SsE-_ooHnghYHjuZY

ПЕРЕНЕСЕНО 2026-09-28: канон проекта WB_UE — `projects/wb-ue/` (repo), строка в таблице выше. Карточка [WB_UE] и вес в блоке T-002 выше — провенанс-маркер, текст не правится (second-brain-git 2.3); источник (Файл индекса выше) заморожен 2026-09-28 (маркер в шапке документа) — см. `projects/wb-ue/STATE.md`.

[WB_CV]   WB конверсия и трафик
          СТАТУС: НЕ НАЧАТ (ждёт WB_UE)
          Файл индекса: 1qWAjqyjxb_M7S9XveSqt9L0c_AH1DyT1LAEsrf9Qkz0

[WB_LOGISTICS] WB FBS логистика — везти сегодня или нет | вес 7 | АКТИВЕН
          Файл индекса: 1mxYgiK9X4qOId2vNF7xnne-cQszTqPpJZHux_AuDZjQ
          Claude Project: https://claude.ai/project/019ea86d-05da-7731-b99f-f0f163be8182

[WB_REVIEWS]  WB AI-отзывы и Q&A | вес 6 | АКТИВЕН
          Файл индекса: 1D-mwjyl_rJ0ekYBSwliIRBwfOSJdJBeDi1SQddaeODc
          Claude Project: https://claude.ai/project/019e8466-e4cb-7588-99c1-496ee2d759ed

[OZON_REVIEWS]  Ozon AI-отзывы и Q&A | вес 6 | АКТИВЕН
          Файл индекса: 1aVS_PLC-WR1HoSp24JwGvUS6S7D9wd7vQ-G8Lzyi3zQ
          Claude Project: https://claude.ai/project/019eb22c-236a-75b6-a786-2dd0e941297d

[CONTENT] Контент для карточек товаров (инфографика, видео) | вес 5 | АКТИВЕН
          Файл индекса: 12YmBvtmAGImFm2fMPz2FglsrCibG3v7acj3NY5LG7m0

[RENO]    Ремонт квартиры
          Арендная квартира, северная Германия, дом 1960-х
          Файл индекса: 1r3hSt4pccSHbya31KLNYtyr5xJtbTl1VcX-OCprBjcM

[TRADE]   Инвестиции и трейдинг
          Методология, мультиактивный подход
          Файл индекса: 1GhOuwVL41hzyWYF4X8Su0bSuraVw6X4pGxc0G3hkT2Y

[SYS]     Система «Второй мозг»
          Файл индекса: labs/sys/INDEX.md (репозиторий); документ Docs 12k2l2oT92m33PFcnlYDr1MdtkGOj7Gy5Vf7ksSw4nm8 заморожен 2026-09-30 (Р-123 журнала projects/git-migration/LOG.md)

[ANAST_QUICKREF] Quick-reference анестезиология (PWA) | вес 3 | АКТИВЕН
          Файл индекса: 1MdqSVr0bHAJ5tbIgNJoHNuBjmqR2V8gLQf5RHco-430
