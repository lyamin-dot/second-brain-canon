# PARTICULARS — группа B2, синтез 2026-10-20

Особенности конкретных объектов из старого текста R10–R19 и §7, снятые из Skill. Проверка носителя — поиском по клону `/home/claude/second-brain-canon` (что искал — в последней колонке).

| единица (цитата ≤80) | предлагаемый носитель | носитель уже держит факт? (что искал) |
|---|---|---|
| «исполнение 79110 воркфлоу `6wTXfH3rFRfo6Ra6`, узел `01_T_NoOption_Blackhole`» | REPORT (BASIS R11.1); `projects/archivarius/LOG.md` Р-35 | ДА: Р-35 называет 79108–79110 и `6wTXfH3rFRfo6Ra6`; имена узлов — `projects/archivarius/TRIAGE.md` (искал «79110», «Blackhole», «Drip15») |
| «(узел `03_T_5s_Drip15`, исполнение 79109); … (узел `02_T_5s_Delay15`, исполнение 79108)» | то же | ДА, то же |
| «Зависший запрос держит воркер — на CPX32 дорого» | `registry/projects.md` (тип сервера) | ДА: `registry/projects.md:77` «Hetzner CPX32» (искал «CPX32»); в Skill оставлено «держит воркер инстанса» |
| «(описания узлов Postgres 2.7 и Telegram 1.2, прочитаны 2026-10-12)» | дата — REPORT; версии узлов оставлены в Skill (свойство платформы) | ДА: `projects/archivarius/LOG.md` Р-35 (искал «connectionTimeout») |
| «Состояние периметра на 2026-09-26: <состояние аутентификации вебхуков на дату — не публикуется, И-7>» | `projects/n8n-map/STATE.md`; строки HOOK N8N_REGISTRY | ДА: `projects/n8n-map/STATE.md:43` (искал «27 вебхук») |
| «Канал закрыт ключом «ключ вебхуков Канала (имя не публикуется, И-7)» … токеном Wildberries» | `projects/git-migration/LOG_ARCHIVE.md` Р-104; `registry/tools.md` | ДА: LOG_ARCHIVE строки 1152–1153; `registry/tools.md:25` (перепроверено в круге 1: строка 25 «Аутентификация вебхуков: 2026-09-18 …»; замечание проверяющего о строке 38 не подтвердилось — там Git Read Lines) — Header Auth на всех восьми вебхуках Канала (искал «ключ вебхуков Канала (имя не публикуется, И-7)») |
| «(WB_REVIEWS_INDEX 2026-09-24)» | REPORT (BASIS R12.3); WB_REVIEWS_INDEX | НЕ ПРОВЕРЕНО: документ Google Docs, в клоне не читается; в `projects/wb-reviews/*.md` не найдено (искал «2026-09-24», «заголов») |
| «оба воркфлоу `LM_DECL — WB Sync` (основной кабинет и ИП) опубликованы с формами без аутентификации» (вход AJ-1 #8) | `projects/deklaration-v2/STATE.md`, LOG; снимок `registry/n8n-map.md` | ДА: `projects/deklaration-v2/STATE.md:54`, LOG строка 140; `registry/n8n-map.md` строки 49 и 118 — `active`, `formTrigger` (искал «formTrigger», «аутентиф») |
| «Счёт периметра выше (27 вебхуков) снят со строк HOOK снимка … форм в нём нет» (вход AJ-1 #8) | правило обобщено в Skill (формы ищутся по `formTrigger` в строках W) | число — `projects/n8n-map/STATE.md:43` |
| «Аудит 2026-07-23 нашёл один живой ключ Anthropic сразу в двух воркфлоу — `Ozon_Hashtag_Generator` и …» | `projects/n8n/STATE.md` (открытый вопрос); паспорта воркфлоу `KQqajdrYKxle9JRe`, `GVyBj6xEcFjnmQ09` | ДА частично: `projects/n8n/STATE.md:24` «Anthropic: 1 ключ, 2 воркфлоу, не перепроверено»; имена/ID — `registry/n8n-map.md` строки 70 и 91 (искал «Hashtag», «News Filter») |
| «На 2026-09-26 у обоих в снимке присутствует тип `<тип ключа — не публикуется, И-7>» | `projects/n8n/STATE.md`; до переноса — BASIS.md U43 | НЕТ дословно: строка 24 держит вопрос, но не факт снимка 2026-09-26 (искал «httpHeaderAuth» в `projects/n8n/STATE.md`). Сейчас адрес — BASIS.md «Случаи без адреса», U43 (полный текст). Предлагаемый окончательный носитель — `projects/n8n/STATE.md`; дописывает проект n8n, в клон не писалось |
| «в 2026-07 узел слал ключ на чужой домен (корпус N8N_JOURNAL_2026; аудит 2026-07-23)» | REPORT (BASIS R13.3) | ДА: уроки У-13а, У-13б `projects/archivarius/TRIAGE.md` строки 27–28 |
| Ключ Serper в истории версий (вход AJ-14 Х-24) | `projects/n8n/LOG.md` Р-6 | ДА: строка 46, пункт 8 (искал «Serper») |
| «`https://liamin-n8n.duckdns.org/...`» | SKILL.md §1 (группа A); `registry/projects.md` | ДА: `registry/projects.md:77`; в Skill R14 ссылается на §1 |
| «Запрос физически уходит на Caddy» | канон SERVER (SERVER_INDEX); до переноса — BASIS.md U60 | НЕТ: «Caddy» в `registry/` и `projects/n8n*` не найден (только `projects/archive-recon/`); в Skill заменено на «reverse-proxy». Сейчас адрес — BASIS.md «Случаи без адреса», U60 (полный текст). Предлагаемый окончательный носитель — канон SERVER (SERVER_INDEX); в клон не писалось |
| «Обнаружено 2026-09-14: из 26 HTTP-нод в 9 воркфлоу только 2 использовали internal-адрес» | `projects/n8n-map/PLAN.md` | ДА частично: строка 50, В12 «из 26 узлов 2 внутренних» (без «в 9 воркфлоу»); текущее состояние — `projects/n8n-map/STATE.md:44` (искал «из 26») |
| «Проверено 2026-09-16: вебхук закрыт Header Auth, вызов через MCP без заголовка прошёл» | `projects/git-migration/LOG_ARCHIVE.md` Р-88 | ДА: строки 1000–1006 (искал «2026-09-16» + «Header») |
| «RAW-sync вернул 245 строк за дату → … 245 чтений → 429 по квоте 60/мин» | REPORT (BASIS, «Случаи без адреса») | НЕТ (искал «245», «245 items», «по квоте 60») |
| «Три сцепленных эффекта, наблюдались 2026-09-19 на googleSheets typeVersion 4.7» | дата — REPORT; версия узла оставлена в Skill | НЕТ (искал «2026-09-19», «returnAllMatches», «Return only First» — найден только разбор опции в TRIAGE, не случай) |
| «(2026-10-07, WB `/content/v2/cards/update`): эндпоинт заменяет карточку целиком» | Skill `n8n-workflow-registry`, `references/cards-and-declarations.md` (специфика API); `meta/CASES_wb-api-card-write.md` | ДА: cards-and-declarations строки 11, 17; CASES строки 7, 12 (искал «cards/update») |
| «характеристику ОКПД 2 (15004292) API не показал ни у одной из 457 карточек» | то же; `projects/deklaration-wb/LOG.md` Р-3 | ДА: cards-and-declarations строка 38 (15004292); число 457 — в `projects/deklaration-wb/LOG.md` строка 25, Р-3 (искал «15004292», «457») |
| «у `kizMarked` значение по умолчанию false» | cards-and-declarations | ДА: строка 44 (искал «kizMarked») |
| «у 29 карточек основного кабинета флаги `needKiz` и `kizMarked` стали false (27 из них — …)» | `projects/deklaration-ozon/LOG.md` Р-46; INCIDENT_LOG | ДА: Р-46 строка 398 «у 29 карточек основ…» |
| «где КИЗ зависит от ОКПД 2 по постановлению № 1683» | cards-and-declarations | ДА: «1683» найден в cards-and-declarations и `projects/deklaration-wb/LOG.md` |
| «повторная запись `kizMarked=true` принята с кодом 200, но флаги остались false» | `meta/CASES_wb-api-card-write.md` кейс 3 | ДА: строки 50–62; общий вывод оставлен в Skill (запись правильного значения может быть принята с 200 и не примениться) |
| «снимок 02.10 — исполнение 73753 воркфлоу `LM_DECL — WB Sync`, узел `05_Fetch_Cards`» | `projects/deklaration-wb/LOG.md` Р-3 | ДА: строка 25 (искал «73753»; также Р-22, Р-44, Р-46 `projects/deklaration-ozon/LOG.md`) |
| «(здесь флаг `needKiz`)» как признак, который меняет запись | `projects/deklaration-ozon/LOG.md` Р-44, Р-46 | ДА (старый адрес) |
| Три одноразовых воркфлоу ARTIKEL_PROPS `xRAIcTOz8TdZAOYm`, `tVkcLMa6tN811CwZ`, `YozhFlVFZVKnj3U8` (вход Х-32) | `projects/deklaration-wb/STATE.md` | ДА: строка 123 |
| «все заказы WB с 18 июля записывались в первую зону, скидка не ставилась ни разу» | `projects/wb-logistics/LOG.md` Р-94 | ДА: строка 726 «с 18.07 все заказы … = zone1, скидка не ст…» |
| «новое имя операции WB попало в категорию «прочее»» | `projects/wb-ue/LOG.md` Р-12, Р-56 | ДА: Р-12 «переименование операций WB с 01.09.2026» |
| «отказ ключа Ozon записан служебной строкой «пустой день» (`EMPTY_`)» | OZON_UE_INDEX (Google Doc) | НЕ ПРОВЕРЕНО: документ Google Docs; в репозитории `EMPTY_` в этом смысле не найден (искал «EMPTY_») |
| «узел `01C_Set_Business_Date`» | `labs/ozon-ue/t-n8n-ozon-workflow-defects.md` | ДА: строка 37, дефект D2 |
| «(labs/ozon-ue `t-product-data-model.md`, артикул 1180): … все четыре кабинета» | `labs/ozon-ue/t-product-data-model.md` | ДА: строка 139; «четыре кабинета» — свойство бизнеса Андрея, в Skill обобщено до «все источники (все кабинеты)» |
| «при нуле заказов снимок не писал ничего (WB_LOGISTICS_INDEX)» | `projects/wb-logistics/LOG.md` | ДА: Р-14 строка 77, Р-58 строка 340 (`__empty__`) |
| «в Decision Engine `throw` при отсутствии порогов остановил бы и запись статусов отгрузки» | `projects/wb-logistics/LOG.md` Р-94 | ДА: строка 726 |
| «(`|| 1.95` для коэффициента логистики, `|| 46` для тарифа первого литра) … 1,7» (вход AJ-1 #9) | `projects/wb-logistics/STATE.md` | ДА: строка 16, «РУТИНА (2026-10-18)» |
| «узлы `07_Calculate_Decision` воркфлоу Decision Engine и `06_Calculate_Forecast` воркфлоу Morning Forecast» | `projects/wb-logistics/STATE.md` | ДА: строка 16 |
| §7: «(WB_REVIEWS_INDEX; не перепроверено)» в двух строках | REPORT (BASIS §7.1) | НЕ ПРОВЕРЕНО: документ Google Docs |
| §7 (вход AJ-1 #7): «случай 2026-10-15, `projects/deklaration-ozon/STATE.md`» | REPORT (BASIS §7.2) | ДА: `projects/deklaration-ozon/STATE.md:63` |
| «27 из них — предметы «Автохимия» и «Смазки автомобильные», где КИЗ зависит от ОКПД 2 по постановлению № 1683» (U-extra X1) | `projects/deklaration-ozon/LOG.md` Р-44; Skill n8n-workflow-registry `references/cards-and-declarations.md` | ДА: Р-44 строки 373–374; «1683» в cards-and-declarations (проверено проверяющим и синтезом) |
