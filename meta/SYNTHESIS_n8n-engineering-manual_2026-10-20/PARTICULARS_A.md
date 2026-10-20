# PARTICULARS — группа A (SKILL.md, references/write.md)

Особенности конкретных объектов, снятые из Skill (решение Андрея 2026-10-20). Поиск — в клоне `/home/claude/second-brain-canon` (коммит 95c7bc6, 2026-10-20), `grep -rl`.

| unit (quote ≤80) | proposed carrier | does the carrier already hold the fact? (what was searched) |
|---|---|---|
| «URL \| https://liamin-n8n.duckdns.org» (§1) | `registry/projects.md`, строка SERVER | да — «Hetzner CPX32 \| liamin-n8n.duckdns.org» (поиск `liamin-n8n.duckdns.org`; также в `projects/n8n-map/PLAN.md`) |
| «Версия n8n … self-hosted, Docker Compose» (§1) | окончательный носитель — канон SERVER (SERVER_INDEX, `registry/documents.md` строка 27); до переноса адрес — BASIS.md «Случаи без адреса», пункт «§1, способ развёртывания» | нет — в репозитории «Docker Compose» как способ развёртывания не найден (поиск `Docker`, `self-hosted`); «docker-compose» упомянут только в `projects/n8n/STATE.md` пункт 3 ручных действий; SERVER_INDEX (Google Doc) не читался. Содержание целиком записано в BASIS |
| «Timezone сервера \| Europe/Berlin» (§1); «при таймзоне сервера Europe/Berlin» | `projects/n8n-map/PLAN.md` раздел 4, поле tz | да — «нет поля → «инстанс (Europe/Berlin)»» (поиск `Europe/Berlin`); также `projects/n8n/STATE.md` строка 32 |
| «здесь стояло 2.20.9 … доступно только с 2.29.0» (§1) | история — BASIS «Опровергнутые диагнозы» | факт истории; `2.29` есть в `labs/sys/t-failure-visibility.md`, `2.20.9` — в `projects/n8n-map/LOG.md` и др. |
| «назначен через `setWorkflowSettings` 39 воркфлоу (… Р-4)» (§1, §8) | `projects/n8n/LOG.md` Р-4 | да (поиск `Р-4 ` в журнале; «52 активных без него», «10 пропущены сознательно») |
| «embedding-модель для `liquimoly_kb` — `voyage-3`» (§1) | `n8n-workflow-registry/SKILL.md:193` | да — оставлено и в Skill как объявленный намеренный дубль (карта, раздел 2 строка 125: ОСТАВИТЬ). Если Андрей сочтёт имя базы особенностью — в «Предлагаю снять» записан вариант |
| «Egress proxy блокирует домен `liamin-n8n.duckdns.org`» (§1.1) | в Skill — общий паттерн «домен инстанса»; имя домена — `registry/projects.md` | да (см. первую строку) |
| «например `01_Webhook` у Git Read Batch» (§1.1) | `registry/tools.md` (сигнатура git-read-batch) | да — строка 31 `registry/tools.md`, вход и триггер; в Skill пример имени `01_Webhook` оставлен без привязки к воркфлоу |
| «исполнения gdocs-replace v2 77211 и 77212» (§1.1) | BASIS §1.1.1 | в `projects/deklaration-wb/LOG.md` поиском «77211» не найдено; адрес прежнего текста сохранён в BASIS |
| «`EXECUTIONS_DATA_PRUNE` обязателен (иначе ~93MB/день)» (§8) | `projects/n8n/STATE.md`; до переноса адрес — BASIS.md «Случаи без адреса», пункт «§8, объём данных исполнений» | частично — STATE несёт `SAVE_ON_SUCCESS=none`, «данные прогонов 342 МБ, хранение 14 дней» (замер 2026-10-09); число «~93MB/день» не найдено (поиск `93`, `PRUNE`). В Skill — общее «растёт без предела» |
| «`SAVE_ON_SUCCESS=none` — следствие для отладки» как факт инстанса (§8) | `projects/n8n/STATE.md` строка 51 | да (поиск `SAVE_ON_SUCCESS`) |
| «Измерено 2026-09-26 … из 39 реально тикающих расписаний `errorWorkflow` не было у 26, явной таймзоны — у 32» (§8) | `labs/sys/t-failure-visibility.md` строки 43–46 | да — «тикающих без errorWorkflow: 26 → 1», «без явной таймзоны: 32 → 16» (разрешение 3а-7) |
| «3 отклонены правами сессии, 10 пропущены сознательно» (§8) | `projects/n8n/LOG.md` Р-4 | да |
| «падающий каждые 15–30 минут воркфлоу засыпает Telegram» как случай OZON Publish Reviews | `projects/n8n/LOG.md` | да — поиск `OZON Publish Reviews` находит `projects/n8n/LOG.md`; в Skill осталось общее свойство платформы |
| «Квота Sheets — на потребителя credential» | — | свойство Google, остаётся в Skill |
| «ключ шифрования n8n … на нашем сервере не в бэкапе» и метод «чего не хватит для восстановления» (правка #23 AJ-1) | канон SERVER — SERVER_INDEX строки 57 и 864 (вердикт AJ-1 #23); пока документ не прочитан — BASIS.md «Случаи без адреса», два пункта «§8 … правки #23» | по вердикту — да; SERVER_INDEX — Google Doc, в синтезе не читался, поэтому содержание целиком скопировано в BASIS |
| «wb_raw_report_V2, sku_category_history» (§3, примеры) | `n8n-workflow-registry/SKILL.md` | да — `sku_category_history` в n8n-workflow-registry; `wb_raw_report_V2` в `projects/wb-ue/STATE.md`, `projects/n8n/NOT_TAKEN.md`. В Skill заменены шаблонами |
| «WB RAW Finance Sync, Ozon Reviews Response» (§3, примеры имён) | `registry/n8n-map.md` | да — оба имени в снимке (поиск: 2 и 3 совпадения). В Skill заменены шаблонами |
| «(sku_cost, а не общий CONTROL_PANEL)» (§9) | `projects/sku-cost/PLAN.md`; пример целиком — BASIS.md «Случаи без адреса», пункт «§9, пример» | частично — книга `sku_cost_Шаблон` есть в PLAN; «CONTROL_PANEL» в репозитории не найдено (поиск). В Skill — общее правило |
| «Google Doc N8N_REGISTRY, строки HOOK и HOOKCALL» (§10) | указатель, не особенность | остаётся в §10 как адрес носителя |
| «Git Write, созданный 01.09, … на 16.09 всё ещё был открыт» (write §2.1) | `projects/git-migration/LOG_ARCHIVE.md` Р-88 | да — «до этого решения вебхук принимал запись без учётных данных» (поиск `Р-88`); дата создания 01.09 не проверена |
| «литералы ключей Ozon и Anthropic в узлах, ключ до сих пор не ротирован» (write §2.1) | `projects/n8n/STATE.md`, «Ручные действия Андрея» п.3 | да — команда поиска литералов и вопрос «Anthropic: 1 ключ, 2 воркфлоу» (поиск `литерал`) |
| «договорённость 2026-10-07 о ключе «Честного знака»» (write §2.1) | `projects/deklaration-wb/STATE.md` строка 40 | да |
| «N8N Registry Sync 16 суток бил 404 в старый путь gdocs-overwrite» (write §2.2 6а) | урок У-34 `projects/archivarius/TRIAGE.md`; паспорт/`projects/n8n-map/` | да — TRIAGE строка 50 (поиск `16 суток`) |
| «2026-07-22 промпт звал архивный replace» (write §2.2 6а) | урок У-58 TRIAGE | да |
| «(наряд Н-07.08-04, gdocs-read)» (write §2.2 6а) | урок У-102 TRIAGE | да |
| «Проверено 2026-09-26 на воркфлоу `gFFiBPm1OomOzJOj`: поле пришло пустым …» (write §2.3 п.4) | INCIDENT_LOG (файл репозитория) запись 2026-09-26; `projects/n8n-map/LOG.md` Р-7 | INCIDENT_LOG — да; в n8n-map/LOG поиск `autoAssigned` пуст — факт держит только INCIDENT_LOG |
| «воркфлоу Ozon, скопированные с WB, наследуют дефекты оригинала» (write §2.3 3б) | `projects/wb-reviews/LOG.md` Р-1, Р-6 | да; в Skill — общее правило о копиях |
| «Git Read Batch, позиция AI-3 … воркфлоу `6wTXfH3rFRfo6Ra6`, исполнение 79111» (write §2.4) | `registry/maintenance-queue-archive.md` AI-3; `projects/archivarius/LOG.md` Р-31; снимок `registry/n8n-map.md` (6wTXfH3rFRfo6Ra6 — «TOOL — пробы стадии Б n8n-engineering-manual») | да (поиск `79111`, `6wTXfH3rFRfo6Ra6`, `AI-3`) |
| «`update_workflow` на 2026-10-12 кодом не пишет» / «Инструмента копирования … нет (на 2026-10-12)» | свойство инструмента MCP, дата проверки — BASIS | в Skill заменено на «проверять по схеме/составу инструментов в момент работы» |
| «2026-10-01 владелец сообщил, что деактивировал воркфлоу» (write §2.5) | `projects/git-migration/LOG.md` Р-126 | да |
| «Прежняя практика архивации зондов (git-migration Р-101, Р-114; …)» | журналы проектов; BASIS «Опровергнутые диагнозы» | да (поиск номеров записей) |
| «38BkuLXhxXLTPpqQ и j0DU23IXnp7xggX9» (AJ-15, setNodeCredential) | `registry/tools.md` строка 45, `projects/gas-bridge/LOG.md` Р-2 | да |
| «(корпус N8N_INDEX, 2026-08; не перепроверено)» (A1, узел без параметра) и «(N8N_INDEX, Зона Б, 2026-08)» (write §2.2 6б) | Google Doc N8N_INDEX (`registry/documents.md` строка 26); пока не прочитан — BASIS.md «Случаи без адреса», пункты A1.4 и §2.2.6б | N8N_INDEX — Google Doc, в синтезе не читался; содержание прежнего текста и смежные уроки TRIAGE (Ф2-2, Ф2-3, проверено) скопированы в BASIS |
