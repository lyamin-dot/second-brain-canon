projects/deklaration-v2/PLAN.md

# Декларации и коды 2.0 — перестройка контроля карточек и кодов

Проект заведён 2026-10-10 по слову Андрея (текст задания — документ «ПРОЕКТ „Декларации и коды 2.0"», вставленный в чат 2026-10-10; запись Р-1 журнала этого проекта). Имя папки `deklaration-v2` назначил Андрей. Старая версия — проекты `projects/deklaration-ozon/` и `projects/deklaration-wb/` с общим слоем `meta/DECLARATION_COMMON.md` и `meta/DECLARATION_SCAN.md` — продолжает работать параллельно до переключения, которое утверждает Андрей.

## Назначение

Перестройка системы контроля карточек и кодов по четырём магазинам (Ozon основной, Ozon ИП, WB основной «Кипарис», WB ИП): появление новых карточек, декларации соответствия, ТН ВЭД, ОКПД 2, Честный знак (КИЗ), в будущем другие документы. Все алгоритмы и наработки сохраняются, мусор убирается, архитектура оптимизируется.

## Старт сессии

Прочитать Skill `second-brain-engineer` и выполнить его стартовый протокол (раздел Р1: `meta/PENDING_RULES.md` и `STATE.md` этого проекта). Перед работой с n8n — Skill `n8n-engineering-manual`. Перед работой с файлами repo `second-brain-canon` — Skill `second-brain-git`. Перед работой с Google Drive и Sheets — Skill `google-drive-docs`. Паспорта воркфлоу — Skill `n8n-workflow-passport`. Идентификаторы книг и специфика API — Skill `n8n-workflow-registry`.

## Фазы (порядок не переставлять)

1. Поиск существующей документации: паспорта воркфлоу, техническая документация, журналы решений, протоколы, иерархия данных, карта n8n. Сначала собрать то, что уже описано, и только потом исследовать живую систему.
2. Инвентаризация, только чтение. Итог — одна карта: каждый воркфлоу (что читает, что пишет, расписание, паспорт, статус: боевой / инструмент / дубль / сломан / неизвестно), каждый лист и колонка (кто пишет, кто читает), источник истины по каждому коду, действующие решения и решения, отменённые позже.
3. Андрей принимает решения по строкам со статусами дубль, сломан, неизвестно.
4. Целевая архитектура и полноценный мастер-промпт.
5. Перестройка по нарядам, блок за блоком.

## Определение мусора

Мусор — то, у чего есть лучшая версия себя. Данные, лежащие в нескольких местах, остаются источниками до тех пор, пока собранная версия не построена и не проверена; только после этого старые места становятся мусором. Пробные воркфлоу и зонды мусором не являются — это инструменты, их не удалять и не архивировать (строка 6 `meta/PENDING_RULES.md`, подтвердил Андрей 2026-10-08). Старые воркфлоу, связанные с декларациями (семейство «Deklaration *», снятые Seed, Worker, Watch, Seed РОСС, Worker РОСС, мониторинги V.2 и прочие, которые карта Ф2 отнесёт к старой версии), перемещаются в архив n8n в конце работы над этим проектом — решение Андрея 2026-10-10 (запись Р-3 журнала); до этого не трогаются.

## Жёсткие правила параллельной работы

- Проект 2.0 только читает всё, что принадлежит старой версии: воркфлоу, книгу Price Master, карточки на маркетплейсах. Никаких правок и записей туда до переключения, которое утверждает Андрей.
- Свои воркфлоу и таблицы проект 2.0 создаёт отдельно, с пометкой 2.0 в имени.
- Карта инвентаризации фиксирует дату снимка. Перед переключением перечитать журналы решений старой версии (`projects/deklaration-ozon/LOG.md`, `projects/deklaration-wb/LOG.md`) с этой даты и сверить карту.
- Ничего не удаляется до завершения перестройки.

## Рабочая гипотеза для проверки (не решение)

Декларация, ТН ВЭД, ОКПД 2 и «нужен КИЗ» — свойства артикула, а не маркетплейса; единый источник истины на уровне артикула, слои маркетплейсов — для фактического состояния карточки и требований конкретного маркетплейса. Проверяется фазами 1–2; решением станет только после фазы 3.

## Носитель карты Ф2

Карта инвентаризации — книга Google Sheets в папке DOCS `1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ`, ID — `registry/documents.md` (решение Андрея 2026-10-10, запись Р-3 журнала). Файлом в этой папке карта не ведётся.

## Связи

- `projects/deklaration-ozon/` и `projects/deklaration-wb/` — старая версия, только чтение; их журналы — источник действующих и отменённых решений для карты фазы 2.
- `meta/DECLARATION_COMMON.md`, `meta/DECLARATION_SCAN.md`, `meta/PRODUCT_DATA_HIERARCHY.md`, `meta/PROTOCOL_wb-card-write.md` — общий слой старой версии и модель данных товара; вход фазы 1.
- `registry/n8n-map.md` — снимок инстанса n8n, вход фазы 2.
- Лаборатория `labs/ozon-ue/` — единая модель данных товара; гипотеза этого проекта с ней пересекается.
- `projects/card-content-sync/` — описания карточек тех же четырёх магазинов; вне этого проекта.

## Ф1 — найденная документация (снимок 2026-10-10)

Что уже описано о старой версии, где лежит и чего стоит. Оценка: **актуален** — описывает живой объект на дату в документе; **устарел** — объекта в таком виде больше нет, читать как историю; **противоречит** — расходится с другим документом или с живым инстансом, расхождение названо. Всё ниже ПРОЧИТАНО В ЭТОЙ СЕССИИ (repo — клоном `origin/main` ed79be5 и раньше; Google Docs — gdocs-read, исполнения 78150–78154; состав папок Drive — search_files), кроме строк с пометкой «не читан».

### 1. Repo second-brain-canon — старая версия

| документ | что держит | оценка |
|---|---|---|
| `meta/DECLARATION_COMMON.md` (9 979 Б) | общий слой двух проектов: четыре кабинета и их права, единый источник данных (Price Master!Artikel, книга LM_DECL_MASTER, Scan), реестр типов документов по площадкам, журнал общего слоя | актуален на 2026-10-08; его строка от 2026-10-08 уже формулирует «ОКПД 2 и ТН ВЭД — свойство товара, а не площадки» — первое подтверждение рабочей гипотезы |
| `meta/DECLARATION_SCAN.md` (29 619 Б) | устройство Scan и книги LM_DECL_MASTER (листы «Декларации» 12 колонок, LM_DECL 18, Decl_History; скрытые листы), регламент разбора дайджеста, ловушки 1–9, адреса общего слоя, состояние (таблица товаров, читатели MASTER_MAP, «руками Андрею», открытые вопросы) | актуален, часть 2 (состояние) — на 2026-10-07; содержит перечень снятых воркфлоу и указание «Worker и Worker РОСС снять с публикации» — на снимке `registry/n8n-map.md` 2026-10-09 оба ещё `active` (строки 14 и 140) |
| `meta/PRODUCT_DATA_HIERARCHY.md` (28 616 Б) | иерархия товарных данных: Справочник LM → Акт.цена → sku_cost → Price Master!Artikel (главная таблица, колонки A:N, X lm_decl_no, Y wb_decl_check); накопители Ozon_SKU_Staging, WB_Cards_Staging, WB_Cards_Staging_IP (колонки A–R); лист ARTIKEL_PROPS (свойства артикула: okpd2, tnved_decl, wb_kiz_danger…); лист WB_Compare (эталон / основной / ИП по четырём критериям); источники истины; раздел 8 «Не решено» | актуален на 2026-10-09; это уже половина карты Ф2 по листам и колонкам Price Master |
| `meta/PROTOCOL_wb-card-write.md` + `.en.md` | порядок записи в карточку WB через API: источники истины по полю (декларация, даты, ТН ВЭД, ОКПД 2, kizMarked, needKiz), где смотреть текущее, инструменты записи, ловушки | актуален на 2026-10-10 |
| `projects/deklaration-ozon/PLAN.md` (16 774 Б) | цель и границы Ozon-части, Ozon Upload (режимы «проверка/боевой/статус», защита от повтора, факты API Ozon /v2/product/certificate/create, /v2/product/certification/list), ловушка 9, адреса | актуален на 2026-10-07; раздел «Как вести проект» — правила старого проекта, для 2.0 не действует |
| `projects/deklaration-ozon/STATE.md` (28 483 Б) | загрузки в Ozon (10 деклараций 2026-10-01, РОСС 01582/26, 20237/26, 15088/26), сверка покрытия 386 товаров по классам А–Ж, отклонённые товары, очередь действий, задачи DECL_SAAS | актуален на 2026-10-06; над бюджетом чтения, разбор не делался (позиция AH-18 очереди) |
| `projects/deklaration-ozon/LOG.md` (158 808 Б, записи Р-1…Р-47, Т-1…Т-10) | решения старой версии до разделения, в том числе Р-2 (один Scan вместо Seed/Worker/Watch), Р-23 (единая модель данных — в лаборатории ozon-ue), Р-26 (Scan дописывает новые артикулы из Artikel), Р-27 (карточки WB вне справочника: 30 LOPAL, AEG), Р-41 (лист категорий в Price Master), Р-44…Р-46 (потеря КИЗ при полной перезаписи карточки), Р-47 (разделение) | оглавление прочитано целиком; тела — Р-23, Р-25…Р-27, Р-41, Р-47; остальное читать по номеру при составлении карты Ф2 |
| `projects/deklaration-ozon/NOT_TAKEN.md` (10 988 Б) | что не взято из OZON_UE_INDEX: паспорта снятых воркфлоу (Watch, Worker, Seed, Seed РОСС, Worker РОСС, мониторинг `ukuFBDUD4mRYVGBu`) с ID, скрипт processDeclPdfInbox и Drive API v2, книги-источники MASTER_MAP | актуален как указатель на историю; ID паспортов снятых воркфлоу нужны для Ф2 (статус «инструмент») |
| `projects/deklaration-wb/PLAN.md` (21 102 Б) | цель и границы WB-части, факты зонда Ф0 (характеристики 15001135/15001137/15001138, 62945173), устройство WB Sync, факты записи (склейка imtID, error/list), адреса всех WB-инструментов и паспортов | актуален на 2026-10-09; **противоречит** Drive: четыре паспорта от 2026-10-09 (WB_WF_wb-cards-staging-ip, WB_WF_price-master-sheet-headers, WB_WF_wb-card-tool-ip-batch, WB_WF_wb-card-tool-ip-single) и WB_WF_price-master-update-by-key лежат не в папке DOCS `1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ`, а в папке `1OuVo5-ELBm7B8KWgJNh6mnwP6raz-Qdy` (папка задачи «2026.01 Обновить Декларацию соответствия WB»); проверено search_files по parentId 2026-10-10 |
| `projects/deklaration-wb/STATE.md` (42 147 Б) | вердикт WB по документам, КИЗ и ОКПД 2 (опасная зона 49 карточек, запрет в коде WB Sync), эстафеты 2026-10-04 и 2026-10-10 (этапы 1–3 по кабинету ИП), цели после 2026-10-09, очередь, «руками Андрею» | актуален на 2026-10-10; самый живой файл старой версии — его «следующий шаг» исполняется параллельно с 2.0 |
| `projects/deklaration-wb/LOG.md` (92 615 Б, Р-1…Р-16) | решения WB-части: Р-2 (источники ОКПД 2), Р-5 (паспорта; зонд WB KIZ Probe — «ядро нового проекта»), Р-6 (временные воркфлоу — инструменты), Р-8 (маркировка — по кабинету из листов карточек), Р-11 (лист WB_Compare), Р-12 (источники истины), Р-13 (эталон ТН ВЭД), Р-14 (формат дат ДД.ММ.ГГГГ), Р-15, Р-16 | оглавление целиком; тела Р-5, Р-6, Р-8, Р-11…Р-13 |
| `labs/ozon-ue/t-product-data-model.md` (52 346 Б) | наряд Н-02.10-01 и его исполнение: единая модель данных товара, точные правки узлов для перевода читателей с MASTER_MAP на Artikel | не читан целиком (первые 30 строк); для Ф2 — источник правок узлов Ozon Upload и WB Sync |
| `labs/ozon-ue/t-ozon-ip-cabinet.md` | кабинет Ozon ИП: воркфлоу PWFVE0UbM3ajvVFc ждёт credential ИП | актуален; блокер четвёртого кабинета |
| `labs/ozon-ue/t-lopal-brand.md` | карточки LOPAL видны сторожу карточек r35gXE6VxvuacEfW | не читан целиком |
| `registry/n8n-map.md` (снимок инстанса 2026-10-09 18:52 UTC) | строки W (воркфлоу, статус, расписание), D (документы по узлам), X/H (вызовы), C (типы credential) | актуален; по теме проекта — около 60 строк W, перечень — раздел 3 ниже |

### 2. Google Drive — паспорта, инструкции, техдоки

| документ | ID | что держит | оценка |
|---|---|---|---|
| OZON_WF_lm-decl-scan — паспорт Scan | `11nO1-pF22USWrJzeXkucUHoWQ86TCzhnJHUcOM-tDgY` | устройство Scan, ADR | не читан в этой сессии; по `meta/DECLARATION_SCAN.md` — ADR Р-13 внесён 2026-10-02, строка о смене номера в Зоне Б устарела |
| OZON_WF_lm-decl-ozon-upload — паспорт Ozon Upload; инструкции для человека и агента | `16r4swPyVr6gMZpcTPL-08waBrUKLt5YSqKRhaRuswr4`; `1WGkP1-RS-okY2lPjXG2ZDlH84lbGaXAFJyv5LNK9Z70` / `1yi16FSJKF6oRP1nLdNoSg70-A4kwFTngfbFkpT7qp1s` | порядок запуска, таблица ошибок, режим «статус» | не читаны; по STATE ozon сверены 2026-10-02 |
| WB_WF_lm-decl-wb-sync — паспорт WB Sync; инструкция | `1cXeMBem_qOazW7PwQPWwNMAnejKHHoDYoO7yaOsmXcM`; `1RqQkq0mEZwMydnGTci6XvGefegXYaVqEpSz7XpHE00w` | | не читаны; имя ключа «Контент» с правом записи в паспорт ещё не вписано (STATE wb, «Руками Андрею») |
| WB_WF_wb-cards-staging, WB_WF_tnved-restore (закрыт: воркфлоу переделан), WB_WF_kiz-probe | `1bm75deygPU93mNWQYnPvlpRX6t87WvgM7kG-y6U1qrA`, `1uy2CAE0ssoVjsIWFSnuyCi1D-Nr8XfmMyb0ghx-Vp38`, `1uRQy9gsxIVvLNZdR61yfwrbgqzB_4gI4Uh-KfqrHFyc` | папка DOCS; kiz-probe прочитан: зонд справочников WB (tnved с isKiz, okpd, charcs по предметам), только чтение, списки предметов зашиты в 03_Build, ключ с правом записи — лишний; «ядро будущего проекта по КИЗ и ОКПД 2» (Андрей 2026-10-08) | актуальны на 2026-10-08 |
| WB_WF_wb-cards-staging-ip, WB_WF_price-master-sheet-headers, WB_WF_wb-card-tool-ip-batch, WB_WF_wb-card-tool-ip-single, WB_WF_price-master-update-by-key | `1EUGi6ZU5f6DaZ3WSlRBkB1-YQ7OdODjFXspujDi3a7s`, `10XmcuORETkk2Rj6qlOzCjYk5O5Mm9TMNIaG_F202TqM`, `1H5p-hAyfQxqu36vlBM1T25HuKjd64qDDmdRY_lYUu30`, `1DWn2B3cPOVkmvE4drUrh_x4vJU7X36aXJ9thnJdsitw`, `1BibPMtcwrJERkyVxFhB3TQWVvaR2E22NQAMobnzaby8` | паспорта инструментов 2026-10-09 | не читаны; лежат в папке `1OuVo5-ELBm7B8KWgJNh6mnwP6raz-Qdy`, не в DOCS (см. раздел 1) |
| OZON_WF_cards-watch — паспорт «Cards Watch — незнакомые карточки (4 кабинета)» `r35gXE6VxvuacEfW` | `1aYQE8KtoNL0nAv37LUTkbCRUk1-oQ9qTXeOICcXW-2c` | сторож незнакомых карточек: раз в сутки (cron 50 6, не опубликован) читает карточки WB основной, WB ИП, Ozon основной (Ozon ИП выключен), сравнивает артикул с Price Master!Artikel, шлёт в Telegram незнакомые; seen в static data; ограничения 1–10 | актуален на 2026-10-08; **ни в одном проекте repo не описан** (только задача `labs/ozon-ue/t-lopal-brand.md`); закрывает пункт назначения 2.0 «появление новых карточек» |
| OZON_WF_lm-decl-intake — паспорт «LM_DECL Intake» `qKgc8hhOLwehejYp` | `1l54Dyh_5OGtaMYClrRCY6h0nKRsyzAAUSoK_3tEqlD4` | новые номера Liqui Moly из Artikel → LM_DECL, 05:30 по Москве | не читан; описан в `meta/PRODUCT_DATA_HIERARCHY.md` раздел 7 |
| LM_DECL_MASTER — техдокументация (RU) ред. 4.0; LM_DECL_MASTER_TECHDOC_EN (раздел «v2 ADDENDUM 2026-09-30» — текущее) | `1Z6wbrh_W0R0_mqDNujihr_dZqKNfYC3h7cTrciWMapM`; `1_tOucfOnJ_BFCWK3eEmP9w5qpuvHtRuHT3MYgWzTp8g` | канон устройства книги LM_DECL_MASTER | не читаны; по STATE ozon сверены 2026-10-02 (RU не поднят до 4.1); EN выше раздела ADDENDUM — устарел (книга до перестройки) |
| LM_DECL_TABLE_TECHDOC | `1AdYC4AimCWfC8V_UKnM44pPAMhiXRFdcP--JNugoXTE` | только указатель | устарел |
| DESIGN_единая_модель_данных_товара | `1hhO6Vd5WNNmxzPfIEvvcfWeaehf0ns0FdI6imSrpNVM` (39 КБ) | инвентаризация книг/листов/колонок с данными о товаре, дизайн модели (наряд Н-02.10-01) | не читан; кандидат на основу карты Ф2 по листам — проверить, что в нём уже сделана инвентаризация, которую Ф2 требует |
| PLAN_ACTIONS_deklaration-ozon; COVERAGE_deklaration-ozon_2026-10-02.csv | `1MTmatK-9oeK1sbJJr6BzP6rcAg3GRVYJ5mkIkLXGuQ8`; `13RLqXuMGp7vNbgV1R1GuMcZBkEp1W2T0` | план действий Ozon по этапам; таблица покрытия 386 товаров Ozon по классам | не читаны; снимок 2026-10-02 |
| DECL_SAAS — Стратегический план v1.0 | `1LCGNLoT8buXrEpARoHl1eT1ixk-tpwlQTyhC7DbTN1Y` | монетизация мониторинга | вне проекта 2.0 |
| OZON_DOC_sku-artikel-map, OZON_WF_sku-artikel-map, OZON_WF_SKUArtikelMap | `1Y-__wFnv_60-w3JWZ6aqlqKRtRZTo91AmbCNmFmjEmQ`, `1aKPiIDTTtIkxIJoARXWJzHfJLiwnwT70zAprs8PftN8`, `1dwXZABZZVR3WMA-OCC4y8dr7e6GGjA8wkavat0NGDmU` | книга SKU_Artikel_Map / MASTER_MAP | устарели: MASTER_MAP выводится из эксплуатации (решение 2026-10-02/06) |
| LM_DECL_WF_Watch | `1sn01YsLIhhYd-jWB44SaG6Y26VKbakcGSUJwhvGqF5o` | паспорт снятого Watch (2026-06-29) | устарел; воркфлоу снят с публикации 2026-10-02 |
| паспорта снятых Worker, Seed, Seed РОСС, Worker РОСС, мониторинга `ukuFBDUD4mRYVGBu` | ID — `projects/deklaration-ozon/NOT_TAKEN.md` | | устарели как описание дежурных; нужны для статуса «инструмент» в Ф2 |
| `_src_LM_DECL_TECHDOC_*` (три служебных файла) | `19TFJ0ngcXEV1ZYkrpkHOzx_JeZPTkNM99Dz6C6mp8JM`, `1005NnqIPDuzD6LTXrJ4mShAti-pLVVlh`, `1x4-lr9NvgK0D4PwEt3oVMeMtfB7TmbAp` | исходники техдоков | устарели; в очереди старой версии на удаление (STATE ozon, пункт 5) |

### 3. Google Drive — поколение до LM_DECL (февраль–июнь 2026, папка `1OuVo5-ELBm7B8KWgJNh6mnwP6raz-Qdy`)

| документ | ID | что держит | оценка |
|---|---|---|---|
| Projekt_Deklaration V.2 (Google Doc, 47 688 Б текста, 1 450 строк) | `1tab-m5Kj-nK22dqvWqCn-8LVB6ZseitrLCCUezgM1GQ` | техдокументация воркфлоу поколения V.2 (2026-02-21): чтение артикулов из Sheets → поиск страницы через Serper → загрузка страницы → извлечение ссылки на декларацию → обновление листа; замечания и рекомендации по узлам; дальше описаны версии с LM_DECL, POST-запросами и ответами | устарел: Serper заменён поиском сайта (`projects/deklaration-ozon/LOG.md` Р-29, Р-32), «первую ссылку выдачи без проверки» названо ошибкой (Skill n8n-workflow-registry, раздел «Liqui Moly — декларации»); прочитан по оглавлению, тело — в файле сессии, для Ф2 читать только если нужен алгоритм извлечения со страницы |
| Описание процесса Декларация соответствия (2026-02-19…03-13) | `153qXe_fC_clKjzBoyKqcIxTuEp1JGwM1jI5Wa1bjY24` | теория (декларация vs сертификат, ТР ТС 030/2012, СГР для аэрозолей), исходный промпт задачи, список воркфлоу «Workflow Automation — n8n Масло моторное/трансмиссионное/гидравлическое» и книг «Парсинг Деклараций *», «Совмещение Деклараций и Даты», «Работа с карточками» | история; теоретическая часть пригодна для мастер-промпта Ф4 |
| ТехДокументация Декларация соответствия | `1fj6QabO4rUjE-WAV0vdnYnyXSlqBWYgHya8vE_sEgGU` | две строки: «Projekt_Deklaration V.3 ссылка на техническую документацию» | пусто, устарел |
| книги «Парсинг Деклараций MotorOel» `1wRxajjT8EYjO39BkfYMSFCusVaNW3hE-aVqIckXpEHE` (лист LM_DECL — его читает и пишет Deklaration_MotorOel_V.5 `56cGbN0MRyggaGq8`, строки D 473–474 снимка), Autochemie `1rICK7-MBFqeR9FbCugganrTGU8kvPK4yuEyqNs8EnEo`, TransmissionOel `1hpp90KJAj2m2sYYk-excFouG8aNnCvv04hE7aG5j-hw`, HydraulischesOel `1Ymp5kpWf6mV00kIPWSFwG7xA_8PblQSwqpsZZC3R6ro`, Bremseflussigkeit `1jiFVxT3NtZWYARI_xxA-4MMKPridfWoHURoUmAu-yJg`; «Совмещение Деклараций и Даты» `1zirMaWew78hsl1GON0icsnJyhTs8Qc1ffvItzoFYunQ` | | книги старого поколения; не читаны; в Ф2 — кандидаты в «дубль» LM_DECL_MASTER после сверки |
| воркфлоу семейства «Deklaration *» на инстансе (снимок 2026-10-09): Deklaration_MotorOel_V.5 `56cGbN0MRyggaGq8` inactive; Deklaration_Hydraulisches_Oil_V.4 `EH2JaB8WGa0JsBqs` **active** (расписание раз в 1000 месяцев); Deklaration_TransmissionOil_V.4 `GDI35U36bBRzKZp5` inactive; Deklaration AutoChemieV.4 `GxV03QtlsRCInkMU` inactive; архивные: MotorOel, MotorOel_V.2…V.4, TransmissionOel ×2, HydraulischesOel | | паспортов нет; ни в одном проекте repo, кроме упоминания V.5 как «судьба неизвестна», не описаны; статус для Ф2 — «неизвестно» |

### 4. Воркфлоу по теме на снимке `registry/n8n-map.md` 2026-10-09 (строки W) — вход Ф2

Живые по расписанию: Scan `vKjqExap1mJjM6Ap` (пн 06:00 МСК), LM_DECL Intake `qKgc8hhOLwehejYp` (05:30 МСК), WB Cards → Price Master `fGHfVrI58Ws1wfTw` (04:10 МСК), WB Cards ИП → Price Master `vIteQxGrqI7kLkb0` (04:25 МСК), Получение SKU Ozon `J0v5swjXLfiANJa2` (03:00). Опубликованы, запуск формой: Ozon Upload `BLNA8sbdnLtuz7Uj`, WB Sync `QCQI6utFFH3dvTJT`, WB Sync ИП `9Qhnkz9E6mjidqs5`. Active без своего триггера (вызывались из снятых Seed): Worker `ZyaOSSDvGsf0eq7L`, Worker РОСС `2ZxUm8WNzccoVfuy`. Неактивные инструменты: Cards Watch `r35gXE6VxvuacEfW`, WB KIZ Probe `UOxe3lay5R7cFed7`, WB Probe `RJ9qlEVyBaaJkaGH`, WB Card Tool ИП одна карточка `4dWCd1l1QiUQBPQQ` и пакет `nIRKnhKyI5LibFW3`, Price Master — лист и заголовки `NaD5kdaD2tFOkkO7`, Price Master — запись колонок по ключу `AVoemWtBLO8L0Kdm`, ARTIKEL_PROPS — Build `jEYQtwSxCEF0Swiv`, ARTIKEL_PROPS — Blatt anlegen `zuhOhRc6PchTJERw`, GTIN Map `DCdm1xOojRKOpn4I`, CZ Proxy Test `GZhOSbxt2KeU4dMo`, Ozon IP SKU Staging `PWFVE0UbM3ajvVFc`, Watch `OnEludZYMusvFxTS`, Seed `IG49VPuULlv60IOz`, Seed РОСС `QmPIz9uhfU48FcWX`, мониторинг V.2 `VMPxWzXPefKT2R1B` и `ukuFBDUD4mRYVGBu`, Получение nmID WB `gglEq5U90Gt3sI7h` (active, раз в 100 месяцев). Архивные: Coverage Probe, Page Probe, FSA Probe, Cert Probe, Test Worker, TDS диагностика, очистка листа, CZ GTIN Probe, WB Content Charcs Probe, ARTIKEL_PROPS — OKPD2 ×2 и KIZ-Gefahrenzone, ONE-OFF ×2, семейство Deklaration (раздел 3). Полный перечень с узлами — грепом по снимку; статусы «боевой / инструмент / дубль / сломан / неизвестно» присваивает Ф2.

### 5. Что Ф1 показала помимо списка

1. Карта Ф2 по листам и колонкам Price Master уже наполовину написана в `meta/PRODUCT_DATA_HIERARCHY.md`; по книге LM_DECL_MASTER — в `meta/DECLARATION_SCAN.md`; инвентаризацию «каждая книга, лист, колонка» требовал наряд Н-02.10-01 — его документ DESIGN не читан, в Ф2 начать с него, а не с живых книг.
2. Три объекта по теме проекта не описаны ни в одном проекте repo: Cards Watch `r35gXE6VxvuacEfW` (есть паспорт), семейство «Deklaration *» (паспортов нет), книги «Парсинг Деклараций *».
3. Два расхождения документов с живым инстансом или Drive: Worker и Worker РОСС активны вопреки `meta/DECLARATION_SCAN.md`; пять паспортов 2026-10-09 лежат не в DOCS, а в папке `1OuVo5-ELBm7B8KWgJNh6mnwP6raz-Qdy` (адреса в `projects/deklaration-wb/PLAN.md` ведут на верные ID, неверна только фраза «в той же папке DOCS»).
4. Рабочая гипотеза: `meta/DECLARATION_COMMON.md` (журнал, 2026-10-08) и `meta/PROTOCOL_wb-card-write.md` уже закрепили декларацию, даты, ТН ВЭД и ОКПД 2 как свойства артикула с источниками истины вне кабинетов. Исключение, которое гипотеза должна учесть: маркировка КИЗ (needKiz, kizMarked) — свойство карточки и юрлица, в двух кабинетах WB она различается (`projects/deklaration-wb/LOG.md` Р-8); «нужен КИЗ» на уровне артикула выводится из ОКПД 2 и предмета, а подтверждение нанесения — только по кабинету.
