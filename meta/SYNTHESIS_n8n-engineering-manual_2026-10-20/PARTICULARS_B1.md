# PARTICULARS — группа B1

Единицы старого текста, которые описывают конкретный объект (воркфлоу, исполнение, счёт, проект), а не правило. В новом тексте их нет — там общий образец. Поиск — `grep -rl` по `registry/ projects/ labs/ meta/` клона (HEAD 95c7bc6), исключая файлы харвеста, синтеза и `TRIAGE.md`.

| единица (цитата ≤80) | предлагаемый носитель | носитель уже держит? (что искал) |
|---|---|---|
| «вебхуку Канала автопривязка поставила токен Wildberries» | `projects/kontext-reduktion/LOG.md` Р-16 | ДА — Р-16 строка «блокер»: «01_Webhook — ключ вебхуков Канала (имя не публикуется, И-7) (автопривязка поставила ключ API маркетплейса (имя не публикуется, И-7))» |
| «ключей Google, Wildberries и Header Auth на инстансе несколько» | `registry/n8n-map.md` / книга N8N_CREDENTIALS | ДА по сути — N8N_CREDENTIALS в `registry/documents.md` строка 77 (реестр credentials); в Skill оставлено общее «если ключей этого типа несколько» |
| «git-migration Т-29, 2026-09-06: Канал записи перестал писать совсем» | `projects/git-migration/LOG_ARCHIVE.md` Т-29 | ДА — Т-29 «канал git-commit был нерабочим около двух часов» |
| «например `fGHfVrI58Ws1wfTw`, узел `02_Fetch_WB_Cards`: `WB-Content-API-Key`, id `g3bSSm…`» | `projects/deklaration-wb/LOG.md` Р-5 | ДА — grep g3bSSmWWg9XjTNOQ: deklaration-wb/LOG.md, deklaration-v2/LOG.md, maintenance-queue.md |
| «проверено на HTTP-узлах двух воркфлоу» | отчёт синтеза (BASIS R1a.5) | факт оставлен в тексте без ID — свойство инструмента, нужное для правила |
| «2026-10-12 на воркфлоу `6wTXfH3rFRfo6Ra6` `setWorkflowSettings` поставил `timezone`… (исполнения 79109–79111)» | `projects/archivarius/LOG.md` Р-35 | ДА — Р-35 «почему»: 6wTXfH3rFRfo6Ra6, исполнения 79108–79111, setWorkflowSettings, maxTries 4, waitBetweenTries 1000 |
| «Пробы: 2026-10-09 замена кода узла Code в Git Read Batch» | `registry/maintenance-queue-archive.md` AI-3 | ДА — позиция AI-3 строка 668 |
| «2026-10-08 через `setWorkflowSettings` уже массово назначали воркфлоу ошибок» | `projects/n8n/LOG.md` Р-4 | ДА — Р-4 |
| «Установлено на `WB FBS Decision Engine` (`S4rZMUkI21dVu3ML`) 2026-10-02» | `projects/wb-logistics/LOG.md` Р-94/Р-95; `registry/n8n-map.md` | ДА — grep S4rZMUkI21dVu3ML: n8n-map.md, wb-logistics/LOG.md |
| «то же — в решении OZON_UE_INDEX 2026-09-30 и наряде Н-05.09-01 (N8N_INDEX)» | Google Docs OZON_UE_INDEX, N8N_INDEX (заморожены, адреса в `registry/documents.md`) | ЧАСТИЧНО — документы есть в `registry/documents.md`; строка «Н-05.09-01» в репозитории не найдена (grep пуст) — факт живёт только в Doc N8N_INDEX |
| «(2026-09-18, повторено на Decision Engine 2026-10-02)» — retry | отчёт синтеза (BASIS, «Случаи без адреса» 1) | НЕТ для 2026-09-18 (grep maxTries + 09-18 пуст); 2026-10-02 — wb-logistics Р-94/95 |
| «эскалация отзывов в `WB Reviews Response` (`2KorY7GdncsIs5Ro`) не работала» | `projects/wb-reviews/LOG.md` Р-1, Р-6 | ДА — grep 2KorY7GdncsIs5Ro: wb-reviews/LOG.md, STATE.md, n8n-map.md |
| «Полная пересборка сменила его у нетронутого узла-вебхука (N8N_INDEX, 2026-09-05)» | Google Doc N8N_INDEX | ДА — адрес в `registry/documents.md` строка 26; в репозитории текста нет |
| «`projects/card-content-sync/LOG.md` запись Р-9 падение прогонов 75619 и 75620» | `projects/card-content-sync/LOG.md` Р-9, Т-3 | ДА — grep 75619: 2 совпадения в card-content-sync/LOG.md |
| «Та же устаревшая посылка … `meta/DECLARATION_SCAN.md` (ловушка 5), `projects/wb-logistics/STATE.md`…» | эти файлы | ИСПРАВЛЕНО в носителях (см. BASIS, «Опровергнутые диагнозы», R1b) |
| «Наблюдалось на ручной правке интервала Schedule Trigger через UI» (R2) | WB_REVIEWS_INDEX; строка §7 lookup (группа B2) | ЧАСТИЧНО — в §7 строка «WB_REVIEWS_INDEX; не перепроверено»; в репозитории не найдено |
| «корпус N8N_JOURNAL_2026» (workflow_statistics) | `projects/archivarius/LOG.md` Р-8 (урок У-12) | ДА — Р-8 строка 157 |
| «запрос готовит сессия, выполняет Андрей через `docker exec … psql`» | `projects/n8n/STATE.md` (строка 25 — готовая команда `docker exec -i n8n-postgres-1 psql …`) | ДА; в Skill оставлено «на сервере (`psql` в контейнере базы)» без имени контейнера |
| «`projects/n8n-map/PLAN.md` раздел 5, журнал n8n-map записи Р-2 и Р-5» | эти файлы | ДА |
| «OZON_REVIEWS_INDEX 2026-10-05; … Р-126: владелец сообщил «деактивировал»» | `projects/git-migration/LOG.md` Р-126 | ДА — Р-126 строка 159 |
| «(DCdm1xOojRKOpn4I, 2026-10-08: прогон 77020 ничего не записал, … 77039 записал)» | `projects/deklaration-wb/STATE.md` | ДА — grep 77020: deklaration-wb/STATE.md |
| «Ozon отвечает 200 с `{"code":9,…}` — `OzonRawАналитика` (`MPzPrtsnPtf0sVQo`) месяц…» | `labs/ozon-ue/t-n8n-ozon-workflow-defects.md`; n8n-workflow-registry SKILL.md строка 115 | ДА — grep «obsolete method»: t-n8n-ozon-workflow-defects.md, deklaration-ozon/LOG.md; Skill n8n-workflow-registry §3 держит форму тела |
| «Wildberries на запись карточки отвечает 200, меняет `updatedAt`…; одна ошибочная карточка… всю пачку» | n8n-workflow-registry `references/cards-and-declarations.md` строки 11, 15 | ДА — в Skill оставлена обобщённая форма («запись может ответить 200, сменить метку изменения») — как пример класса |
| «(WB_REVIEWS_INDEX, 2026-07-28)» — вебхук ответил рано | Google Doc WB_REVIEWS_INDEX | ДА — адрес в `registry/documents.md` строка 46 |
| «измерено: тело файла трижды — узел загрузки, узел сборки ответа, Respond» | отчёт синтеза (BASIS, «Случаи без адреса» 3) | НЕТ — адреса вне Skill нет |
| «`n8n-nodes-base.httpRequest` оставляет сырое тело…, `n8n-nodes-base.github` не оставляет» | — | НЕ особенность: свойство типов узлов n8n, оставлено в Skill |
| «исполнения 82240 и 82241» (AJ-15, подворкфлоу) | `projects/gas-bridge/LOG.md` Р-2 | ДА — grep 82240: gas-bridge/LOG.md, n8n/STATE.md, maintenance-queue.md |
| «(журнал `projects/wb-ue/LOG.md` записи Р-44 и Р-46; card-content-sync Р-9…)» | эти журналы | ДА |
| «следующая нода получает 7 ответов на 8 конфигов» (R5) | — | оставлено в Skill как иллюстрация механизма (не объект) |
| «наблюдался 429 при разрыве 5+ минут» | отчёт синтеза (BASIS, «Случаи без адреса» 5) | НЕТ — grep «5+ минут» пуст |
| «`executionTime` упавшего узла ≈ 59000 мс» | — | оставлено в Skill как признак (не объект); случай — BASIS «Случаи без адреса» 6 |
| «(`meta/DECLARATION_SCAN.md` ловушка 1; `projects/n8n/STATE.md`)» — шапка | эти файлы | ДА — DECLARATION_SCAN «Ловушки» пункт 1 |
| «(WB_LOGISTICS_INDEX, 2026-07: надбавка не считалась с начала эксплуатации)» | `projects/wb-logistics/LOG.md` Р-12 | ДА — grep «#ERROR», «надбавк»: wb-logistics/LOG.md Р-12 (2026-06-20) |
| «(исполнения 74384–74387 воркфлоу `LM_DECL Intake` `qKgc8hhOLwehejYp`, позиция очереди AH-20)» | `registry/maintenance-queue.md` AH-20 | ДА — grep 74384: maintenance-queue.md |
| «перед вводом 35 строк Lopal… проверены 11 воркфлоу-читателей — девять…, один…, один…» (AJ-1 #5) | `projects/wb-ue/LOG.md` Р-64, Р-62 | ДА — Р-64 «читатели Artikel проверены»; Р-62 |
| «Price Master!Artikel» | `registry/documents.md`, `registry/n8n-map.md` | ДА — grep «Price Master» |
| «(labs/ozon-ue `t-lopal-brand`; … deklaration-ozon/LOG.md записи Р-4 и Р-45)» | эти файлы | ДА — t-lopal-brand.md строка 9 (IMPORTRANGE в колонке A Artikel) |
| «(проба 2026-10-12, запись Р-31 журнала `projects/archivarius/LOG.md`, исполнение 79035…)» | `projects/archivarius/LOG.md` Р-31 | ДА |
| «(«1058.0» против «1058», `projects/card-content-sync/PLAN.md`)» | `projects/card-content-sync/PLAN.md` строка 133 | ДА; пример «1058.0» оставлен в Skill как иллюстрация вида расхождения |
| «(labs/ozon-ue `t-product-data-model.md`, артикулы 3326 и 1795)» | `labs/ozon-ue/t-product-data-model.md` | ДА — grep 3326, 1795: по 1 совпадению |
| «(WB_REVIEWS_INDEX, 2026-07-29 — ключ модели; коды ACEA)» | Google Doc WB_REVIEWS_INDEX | ДА по адресу документа |
| «(64 из 182 строк product_model, исполнение 31969)» | отчёт синтеза (BASIS, «Случаи без адреса» 7) | НЕТ — grep «31969», «product_model», «64 из 182» пуст |
| «(корпус N8N_JOURNAL_2026, две сессии)» — пустой ключ | Google Doc N8N_JOURNAL_2026 (заморожен; `registry/documents.md` строка 58) | ДА по адресу документа |
| «перезаписала соседний порог (3 вместо 42), и надбавки дошли до 12,5 млн ₽» | `projects/wb-logistics/LOG.md` Р-42 | ЧАСТИЧНО — «вместо 42» есть в Р-42; «12,5 млн» в репозитории не найдено (grep пуст) — сумма живёт только в Google Doc WB_LOGISTICS_INDEX; журнал задним числом не правится, поэтому адрес — этот документ и BASIS R6.9 |
| «(`projects/wb-logistics/STATE.md`, Order Intake)» | `projects/wb-logistics/STATE.md` | ДА — grep «Order Intake» |
| «(WB_LOGISTICS_INDEX, `sorted_detected_at`)» | `projects/wb-logistics/LOG.md` Р-28 | ДА — grep sorted_detected_at |
| «(OZON_REVIEWS_INDEX 2026-10-04/05…)» — append архива | Google Doc OZON_REVIEWS_INDEX | ДА по адресу документа |
| «(журнал `projects/wb-ue/LOG.md` запись Р-54; … узел `09_Delete_RAW_Rows`)» | `projects/wb-ue/LOG.md` Р-54, STATE.md | ДА |
| «(`OZON Reviews Archive` `HH7pDL2VZfU9C9Np`, `projects/n8n/STATE.md`…)» | `projects/n8n/STATE.md`, `registry/n8n-map.md` | ДА — grep HH7pDL2VZfU9C9Np |
| «по пакету харвеста 2026-10-08 — рецидив инцидента 2026-06-11» | файл пакета харвеста 2026-10-08 | НЕТ — в `meta/` файла харвеста 2026-10-08 нет (ls), grep «2026-06-11» находит только wb-logistics/LOG.md и LOG_ARCHIVE не по этому случаю; адрес остаётся BASIS R6.12 |
| «(`projects/card-content-sync/PLAN.md` узлы 10–11; `projects/n8n/STATE.md`; `projects/wb-ue/STATE.md` пункт (A))» | эти файлы | ДА |
| «Масштаб на 2026-09-26, по строкам W…: из 39 реально тикающих… нет у 32» | `labs/sys/t-failure-visibility.md` | ДА — строка 14 («без явной таймзоны — 32»), пересчёт строка 46 (32 → 16); снято по резолюции 3а-7, в Skill — указатель |
| «Без `settings.timezone` Schedule Trigger трактует cron как локальное время Europe/Berlin» | SKILL.md §1 (группа A; таймзона сервера); `registry/n8n-map.md` поле 8 строк W | ДА — n8n-map.md пишет «Europe/Berlin» в поле tz. В R7 правило стало «таймзона сервера (SKILL.md §1)»; Берлин и Москва оставлены как пример расчёта смещения |
