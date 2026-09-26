n8n Incident Log — провенанс
Версия: v1.1 (слияние 2026-08-04, наряд Аргус/Прораб) · Дата первой версии: 2026-07-24
Спутник SKILL.md (n8n-engineering-manual). Читать только на харвесте / обслуживании. В рабочей сессии не нужен.
ИНВАРИАНТ ЭТОГО ФАЙЛА. Здесь нет и не должно быть НИ ОДНОГО правила — только даты, ID и ссылки. Любое правило обязано иметь адрес в SKILL.md (§5) или в TEMPLATES.md (T1–T4). Если при харвесте появляется соблазн записать сюда правило — значит, ему не хватило места в тех двух файлах, и вписывать надо туда. Иначе знание становится невидимым: оседает в логе и не доезжает до read-path.

1. Хронология инцидентов

2026-06-30 — OzonRawАналитика пишет в _OLD лист (53 дня) — R6
2026-06-30 — KB TO Preprocessor — сброс matchingColumns — R1b / R6
2026-07-03 — Health Monitor .to([a,b]); Registry Sync 114 вместо 76 — R1b
2026-07-04 — OZON_REVIEWS — порча jsonBody, neverError — R1b / R4
2026-07-05 — SYS Index Size Monitor — HTTP перезаписал json — R5
2026-07-05 — Получение nmID WB — регрессия связей при вложенных .to(merge.input(N)) — R1b
2026-07-07 — Получение nmID WB — composite matchingColumns — R6
2026-07-10 — Харвест 07-04 → 07-10 (5.13–5.22, 4.22–4.26) — R1b / R3 / R5 / R6
2026-07-15 — OZON_REVIEWS (5.23 neverError, 5.24, 5.25) — R4
2026-07-18 — ZIvTVFHNw9m2gns3 — Schedule Trigger не тикает, 24ч+ простоя — R2
2026-07-19 — WB_REVIEWS — кросс-аудит Fable (credential-type change) — R1a / R1b
2026-07-21 — DOSSIER INBOX Accept To Archive (alwaysOutputData, pairedItem) — R3
2026-07-22 — P3 SYS Canary — HTTP onError, race condition вкладки редактора — R5 / R1b
2026-07-22 — gdocs-replace-v2 — неуникальный якорь «ОТКРЫТЫЕ ЗАДАЧИ», правка размножилась в 3 места — —
2026-07-23 — Аудит 82 воркфлоу: 67 MUST FIX, 92 SHOULD FIX, 24 NICE TO HAVE, 36 открытых вопросов — все
2026-07-23 — OzonRawАналитика — рецидив мёртвой false-ветки IF (чинили 07-04, вернулась) — R1b
2026-07-23 — WB RAW Finance Sync V.3 — тот же класс впервые (08_IF_RAW_Rows_Exist) — R1b / R3
2026-07-23 — DOSSIER Build CORPUS+REGISTRY — Save без Publish, активная версия с калибровочным лимитом — R2
2026-07-23 — Anthropic-ключ: один и тот же в Ozon_Hashtag_Generator и WB+Ozon News Filter — R13
2026-07-23 — Аномалия «0 executions при живом расписании» — объяснена: SAVE_ON_SUCCESS=none + PRUNE, не баг — R4
2026-07-23 — google_drive_fetch вернул пусто на двух рабочих доках → конфабуляция поверх пустого чтения — —
2026-07-24 — Drive MCP create_file падает на любом содержимом (47 КБ и одна строка), чтение работает — протух write-scope — —
2026-07-24 — gdocs-overwrite-v2 → success:false, bytesRead:0, «not shared to SA»: новый Doc не расшарен сервис-аккаунту — —
2026-07-24 — Подтверждено: execute_workflow в production не создаёт видимого execution; наблюдаемость только в manual — R4
2026-07-24 — gdocs-replace-v2 не находит строки метаданных в шапке INDEX (2 попытки, occurrencesChanged:0) при рабочем replace по телу того же файла — —, уже внесено в 1Ts6ycdKBH42uTtC6osi0FsqO8C2v8-ifTrKCaWQVB7Q (перенесено без изменений формулировок)

2026-07-19 — verified: исключение credentials-сброса при update_workflow (→ R1b). 2026-07-23 — AUDIT_FULL_OZON_WB_2026-07-23 (102uYVoW0HhH7qxNHRyUTrOQCowL7ZN1PaLHleA9MWnI) — полный аудит 82 воркфлоу, источник для R12 (webhook без аутентификации) и R13 (секреты в открытом виде). 2026-07-24 — verified: «второго канала верификации записи не существует» (MCP-запуски не трейсятся) (→ §8). 2026-07-24 — R12 и R13 утверждены Андреем как полноценные корни §5 (не только гейты T4). 2026-07-24 — v2.0: §5 переведён из развёрнутых разборов в индекс-роутер; §7 — табличный вид с адресами T1–T4. ADR-2026-07-24. 2026-07-25 — v2.1, обслуживание: добавлен §2.1 (микро-чеклист регрессов перед update_workflow). 2026-08-04 — коррекция ложной записи о завершении сплита (наряд Аргус/Прораб 03.08.2026): источник переключён на 1UWIsOxFYvXIREs7QPw5fvwEzGU5CCWjkgfvUG_CfweI (R1–R13), статусы T1–T4/TEMPLATES.md/INCIDENT_LOG.md исправлены на честные. CORE Р.14 зарегистрирован верно.

Новые записи по итогам наряда на проверку фактов (2026-08-04, Аргус/Прораб)
2026-07-22 — W3KjaXVqWD2c02IK (DOSSIER Build CORPUS+REGISTRY): лимит 1 файла снят, activeVersion синхронизирована с draft (подтверждено живым чтением 2026-08-04; на момент аудита 07-23 расхождение ещё было). 2026-07-26 — KQqajdrYKxle9JRe (Ozon_Hashtag_Generator) 04_SkipIfEmpty: false-ветка подключена обратно в цикл 03_LoopOverItems (подтверждено живым чтением 2026-08-04; на момент аудита 07-23 была не подключена). 2026-08-04 — MPzPrtsnPtf0sVQo (OzonRawАналитика) 09_IF_RAW_Rows_Exist: активный рецидив — false-ветка по-прежнему отсутствует в connections, description воркфлоу («снова подключена, как в оригинале») не соответствует действительности. 2026-08-04 — верификация T1–T4/INCIDENT_LOG.md (наряд Аргус/Прораб): 29 из 30 проверенных утверждений подтверждены (1 недоступно — ZIvTVFHNw9m2gns3 архивирован); из раздела «Источники» 2 ID не подтвердились (entity not found), 1 переименован по факту содержимого — см. правку раздела 3.

2. Провенанс корневых причин
Откуда пришёл каждый корень — номера старых харвест-блоков и записи плоской таблицы ошибок, свёрнутые рефактором 2026-07-22 и сплитом 2026-07-24.

R1a — credential-type-change (2026-07-19); error-table «credential does not exist»; выделен из R1 при сплите 2026-07-24
R1b — 5.8, 5.12, 5.13, 5.20, 5.29, 5.31, 5.33; error-table «IF теряет expressions»; рецидив false-ветки 2026-07-23; выделен из R1 при сплите 2026-07-24
R2 — 5.23 (ZIvTVFHNw9m2gns3, OZON_REVIEWS, 2026-07-18, 24ч+ простоя)
R3 — 4.2, 4.16, 4.21, 5.11; alwaysOutputData-top-level (2026-07-21); pairedItem/splitInBatches (2026-07-21); error-table «молча стоп после Find»
R4 — 4.20, 5.23 neverError, 5.24, 5.25, 5.30, 5.32 includeData, 1.x PRUNE; подтверждение production-режима 2026-07-24
R5 — 4.26, 5.32 onError-парадокс; переписан по данным аудита 2026-07-23
R6 — 4.15, 4.17, 4.22, 4.24, 4.25, 5.6, 5.15, 5.16, 5.18, 5.19, 5.20, 5.26, 5.27
R7 — 4.7-old, 5.17 (минимум 4 воркфлоу WB_LOGISTICS: Decision Engine, Morning/Evening Forecast)
R8–R11 — Черновик ревизии T1–T4 (2026-07-23), подтверждены аудитом 82 воркфлоу
R12 — Аудит 2026-07-23, батч 12/14: 12 воркфлоу с публичным webhook без аутентификации. Статус: утверждён 2026-07-24
R13 — Аудит 2026-07-23: Ozon (12 воркфлоу / 17 нод), Serper.dev (9 воркфлоу / 10 нод), Anthropic (1 ключ / 2 воркфлоу). Статус: утверждён 2026-07-24

3. Источники

AUDIT_FULL_OZON_WB_2026-07-23 — 102uYVoW0HhH7qxNHRyUTrOQCowL7ZN1PaLHleA9MWnI — Полный несжатый текст всех 14 батчей аудита: по каждому воркфлоу имя, ID, статус, каждая находка с именем ноды и цитатой кода, плюс 8 пунктов «Ограничения аудита»
Ozon n8n Workflow Audit — Батчи 1-3 (2026-07-23) — 13YNL6yY2Y7Uj6xGoPXk8IXNA9ROD_RFQGGdLr4ODsMU — Выжимка; детальные батчи 1–13 существуют только в history версий и через API не читаются
N8N_INDEX — 1GktMsgl1UOIzuWj02gqDirMSYlSjiuLuDVDd9vevB5Q — Проектный лог: решения, баги, техдолг по датам
N8N_REGISTRY — 1zdz12-cwFZyHaHkKA8tJ1MvQKGCMN4xZdYztfYS3SOc — Живой снимок всех воркфлоу, автообновление 05:30 (N8N Registry Sync gFFiBPm1OomOzJOj)

Правка 2026-08-04 (наряд Аргус/Прораб): удалены N8N_GOLDEN_TEMPLATES_v1 (10NN3xp2...) и «Черновик ревизии T1–T4 + R1/R5» (1aQWMC5wD...) — оба ID проверены дважды, entity not found. Строка 13YNL6yY2Y7Uj6xGoPXk8IXNA9ROD_RFQGGdLr4ODsMU переименована с «Сжатая сводка аудита» на факт содержимого: «Ozon n8n Workflow Audit — Батчи 1-3 (2026-07-23)» — ID существует, но под другим содержимым, не «сжатая сводка».

4. Открытые вопросы, перенесённые из аудита
Не правила — незакрытые факты, ждущие решения Андрея. Каждый должен либо закрыться, либо превратиться в правило в SKILL.md / TEMPLATES.md.
1. list_credentials / setNodeCredential отсутствуют в наборе MCP-инструментов. Поддерживает ли сам SDK двухпараметрическую newCredential('Label','credId') — не проверялось (нужен get_sdk_reference).
2. Режим Merge в 11_Wait_For_Delete (OzonRawАналитика) и 10B_Merge_Before_Write (WB RAW Finance Sync V.3): parameters пусты, через API режим не виден. Нужен скриншот поля Mode.
3. Error Notifier (M5BLqclKBjGTpz33): добавляем ли error.message в текст алерта. Частично прояснено 04.08 — Прорабом подтверждено, что error.message сейчас отсутствует в шаблоне; решение «добавлять ли» — не принято.
4. Mass-assign errorWorkflow: аргумент за апгрейд до 2.29.0+ либо ручная работа по числу воркфлоу.
5. SYS Canary (B5jkqW0bUScxmTi7) с намеренно битым fileId: приходят ли ежедневные Telegram-алерты CANARY FAIL. Если нет — сломана сама система алертов, и T2 слой 4 надо проверять заново.
