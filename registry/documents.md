registry/documents.md

# Реестр идентификаторов документов и папок Google Drive

Что это: идентификаторы системных документов, INDEX-файлов, журналов и папок Google Drive. До 2026-09-10 — Раздел 2 CORE («ID системных файлов», файлы `core/R-02a.md` … `core/R-02d.md`); перенесён в `registry/` решением Р-66 журнала `projects/git-migration/LOG.md`, потому что это реестр, а не правило: из него берут одну строку в момент использования, а не читают целиком на каждой команде.

Кто читает и когда: сессия, которой нужен идентификатор конкретного документа — команда !save, онбординг проекта, обслуживание, поиск документа. На старте сессии и при чтении CORE по Манифесту этот файл не читается. Ссылка «CORE Р.2» в Skills и документах означает этот файл (разрешение — `meta/MAP_core-sections.md`).

Как перенесено: блоки T-NN взяты из четырёх файлов подряд, в прежнем порядке, вместе с провенанс-маркерами; текст строк не правился, серии пустых строк сокращены до одной. Файлы до переноса читаются из истории — адрес в `meta/MAP_core-sections.md`. Внутри блоков остались снимки чисел на даты записи (номера исполнений, контрольные суммы, размеры) и слова «этот раздел», «этот файл» — они говорят о прежнем месте и прежнем носителе. Разбор по §5.1 `second-brain-git` (удаление устаревших снимков, указатель вместо дубля) — отдельным действием, не этим переносом.

<!-- T-005 | CORE байт 5540-5838 | Р.2 заголовок раздела -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
РАЗДЕЛ 2 — ID СИСТЕМНЫХ ФАЙЛОВ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

<!-- T-006 | CORE байт 5839-6266 | Р.2 базовые системные ID (CORE, INBOX, USER_PROFILE, REFERENCE_DOC, ТЗ, ЧЕК-ЛИСТ) -->

CORE (этот файл):   1fnWdPUE695BYXhwkMe8Pkzncsi8jYBecH_66ELCcjo4
INBOX:              1iciFTKXYOrN-l7avFySJv2Q__mFEOffps_xsFQwtZDk
USER_PROFILE:       1Kssh75BZWhA9nbudW7A2nbGUQjUd2ZQFjIFOfuu5SBo
REFERENCE_DOC:      1wLXGvxc5HQ9KXgsZzqAGTN0-1nmhbf_L9fAjYVAJh_k
ТЗ:                 1cFBggiGQWtzt_cITae7RUCh8oPhI1aVsybSElDOhfGI
ЧЕК-ЛИСТ:          1LsKb5CNy-M5LhxlCRD6a7yi0kaye4ovFVLo_c9t2-WI

<!-- T-007 | CORE байт 6267-7545 | Р.2 ID проектных INDEX (N8N … WB_REVIEWS_INDEX, вкл. wb_fbs_orders_tracking) -->
N8N_INDEX:          1GktMsgl1UOIzuWj02gqDirMSYlSjiuLuDVDd9vevB5Q
SERVER_INDEX:       1n5WPjZ99H9cwVj3w7FwLsvLZLiabAFIcp8fF5hzq5rY
SERVER_SVC_ocr:     1ZBCgE6hOyz3q-0hkL6v5KzN_0qeTY66iuzySbhz98dQ
OZON_UE_INDEX:      13gg5K9lGx_ypJZdnt-Fe8xFtShWYYFI9uEtClPNsjhQ
OZON_CV_INDEX:      1t4DWGWB7z_4uAsGhbs8xHXvr6MI__i8A5Nc73puid3U
WB_UE_INDEX:        1qY2bB8VZtepPQCp0uZQ6hzO4a2SsE-_ooHnghYHjuZY
WB_CV_INDEX:        1qWAjqyjxb_M7S9XveSqt9L0c_AH1DyT1LAEsrf9Qkz0

WB_LOGISTICS_INDEX: 1mxYgiK9X4qOId2vNF7xnne-cQszTqPpJZHux_AuDZjQ
Claude Project WB_LOGISTICS: https://claude.ai/project/019ea86d-05da-7731-b99f-f0f163be8182
wb_fbs_orders_tracking (Sheets, includes performance_log + monitor_params, подтверждено кодом 7 воркфлоу SYSTEM-MAP 18.07): 1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ (исправлено 2026-10-09: прежняя ручная копия была без «uDB», 41 знак; верное значение — 19 вхождений в снимке `registry/n8n-map.md`, снятом с инстанса, зонд Z-10 `projects/n8n-map/PLAN.md`)
RENO_INDEX:         1r3hSt4pccSHbya31KLNYtyr5xJtbTl1VcX-OCprBjcM
TRADING_INDEX:      1GhOuwVL41hzyWYF4X8Su0bSuraVw6X4pGxc0G3hkT2Y
SYS_INDEX:          12k2l2oT92m33PFcnlYDr1MdtkGOj7Gy5Vf7ksSw4nm8 — ЗАМОРОЖЕН 2026-09-30 (решение 2026-09-23, Р-109 журнала projects/git-migration/LOG.md); рабочий носитель — labs/sys/INDEX.md; не читать и не писать

CONTENT_INDEX:      12YmBvtmAGImFm2fMPz2FglsrCibG3v7acj3NY5LG7m0

AUTOCHEM_BUNDLES_INDEX: 1Lnod5P2LTn5ECDHWEzfP34LCvXvgfBC6-gdZDq6ywDs

ANAST_QUICKREF_INDEX: 1MdqSVr0bHAJ5tbIgNJoHNuBjmqR2V8gLQf5RHco-430
WB_REVIEWS_INDEX:   1D-mwjyl_rJ0ekYBSwliIRBwfOSJdJBeDi1SQddaeODc

<!-- T-009 | CORE байт 8926-9256 | Р.2 OZON_REVIEWS_INDEX, CHANGELOG, SYS_ARCHIVE, SYS_ACTION_PLAN, JOURNAL_INCIDENTS -->
OZON_REVIEWS_INDEX: 1aVS_PLC-WR1HoSp24JwGvUS6S7D9wd7vQ-G8Lzyi3zQ
CHANGELOG:          1VsuHOWDTxnUkOZoQob1TPj2kNB4jUPtFchxgBMmgDWE
SYS_ARCHIVE:        1kZmn3VIKc1RZz2Kmyxqn8u802d1zBq4qiIT7yaWrX1s
SYS_ACTION_PLAN:    1BPMRo4WaDLZUSJ9axywem5LJmcwaBhAZ5KivhGNZJxc
JOURNAL_INCIDENTS:   1q9WiAbbkqazabOA9VMBMBS_pk-S-P20-qsjAfODqEjk — ЗАМОРОЖЕН 2026-10-13 (последнее изменение документа 2026-08-31; прочитан целиком — Архивариус, запись Р-14 журнала projects/archivarius/LOG.md; пишущих в него воркфлоу, промптов и Skills нет — проверка 2026-10-13, Р-41 того же журнала)

<!-- T-010 | CORE байт 9257-10140 | Р.2 журнальные корпуса SYS_JOURNAL_2026, READER_R2_passport, N8N_JOURNAL_2026 -->
SYS_JOURNAL_2026:   1gDi41gTkLp8b2Us6UN8h_Cpj5gcBxpsCE3UnVQ0NkVU — ЗАМОРОЖЕН 2026-10-13 (последнее изменение документа 2026-09-08; прочитан целиком — Архивариус, запись Р-12; запись 2026-09-08 — сессия SYS 2026-10-13 журнала projects/archivarius/LOG.md; пишущих в него воркфлоу, промптов и Skills нет — проверка 2026-10-13, Р-41 того же журнала). Прежнее описание: журнальный корпус SYS (вырезано из SYS_INDEX 31.07, дословно; читатель — читатель R2 по паспорту READER_R2_passport, гейт пройден 2026-08-13 (6/17), карантин снят 2026-08-15; прежняя запись читателя error-memory была фикцией, снята 2026-08-15)
READER_R2_passport: 1rBU7c-xSL8D4kd5bXiAhk5UbVPOvAAhEWjiQIt3NByI — паспорт читателя R2 (PUSH, анализ паттернов корпуса), поля по MISSION_knowledge-loop v0.4 р.3, папка _SYSTEM, наряд Н-15.08-01, создан 2026-08-15
N8N_JOURNAL_2026:   19U4cDQ-JnxhZStBUKyJARL6NQHpCVxZZsEereITJ1Wo — ЗАМОРОЖЕН 2026-10-13 (последнее изменение документа 2026-08-26; прочитан целиком — Архивариус, запись Р-8 журнала projects/archivarius/LOG.md; пишущих в него воркфлоу, промптов и Skills нет — проверка 2026-10-13, Р-41 того же журнала). Прежнее описание: журнальный корпус N8N (зарегистрирован наряд 14 Ф8, 2026-08-05)

<!-- T-012 | CORE байт 10997-11361 | Р.2 SYS_PROTOCOL_REGISTRY -->
SYS_PROTOCOL_REGISTRY: 1ftGIevprVglEytkI_qTobmMyL8ufP5c5pY__b2pbqHE — реестр протоколов (Протокол | Дата рождения | Число применений | Дата последнего применения | Статус | ТРИГГЕР), вынесен из SYS_INDEX нарядом Н-14.08-01.8, 2026-08-13, папка _SYSTEM

<!-- T-016 | CORE байт 12429-13377 | Р.2 документы и папки (SECOND_BRAIN_TZ, SKILL_SBE, USER_MANUAL, TECH_INDEX, N8N_TEMPLATES, N8N_INCIDENT_LOG, _SYSTEM, INDEX_FOLDER) -->
SECOND_BRAIN_TZ:    1j9sqL43m3PvUjpqAvfj71gFDsWVjajz_sZKQCRxVdnc
SKILL_SBE:          1gybzP1Gre3aJCkjRcHFoSe1m6YpcYYEd9w8qGHTzPWI — ЗАМОРОЖЕН 2026-09-27 (текст на 2026-08-22; канон Skill — skills/second-brain-engineer/, Р-114 журнала projects/git-migration/LOG.md)
SKILL_GDD:          1CXJM_kBNtOVwF1Xs91Izxrd-kmPiLGyciGY3FH1CO6A — ЗАМОРОЖЕН 2026-09-27 (Google Doc skill_google-drive-docs, текст на 2026-08-30; канон Skill — живой Skill в Customize, копия — skills/google-drive-docs/; Р-114 журнала projects/git-migration/LOG.md)
USER_MANUAL:        1ZFUggkhZoip6ytesV0D-SlfIsCtpNZQ6TKQfYqnjiHo
TECH_INDEX:         10fAtNieWynJL3hUUVn8KsPWhv66RwkiAihLApJDhOMM
N8N_TEMPLATES:      1A5LrTDyThvox90jCHjM6UnVhQhfmPOv3K8gAylUnY4g — ЗАМОРОЖЕН 2026-10-14 (устаревшая копия TEMPLATES.md с шаблонами T1–T4, последнее изменение документа 2026-08-11; живой текст — файл references/templates.md внутри Skill n8n-engineering-manual, шаблоны T1–T5, обновлён 2026-10-13; задача labs/sys/t-harvest-frozen-journals.md, автопилот сессии SYS 2026-10-14 по поручению Андрея решать открытые задачи самостоятельно; образец — строка N8N_INCIDENT_LOG). Прежний текст строки: TEMPLATES.md (T1-T4), спутник SKILL n8n-engineering-manual. Существование подтверждено 2026-08-11 (был в Корзине, невидим владельцу; восстановлен Андреем). Корень Диска, не папка SKILLS.
N8N_INCIDENT_LOG:   1Ts6ycdKBH42uTtC6osi0FsqO8C2v8-ifTrKCaWQVB7Q — ЗАМОРОЖЕН 2026-10-11 (устаревшая копия INCIDENT_LOG.md версии v1.1 от 2026-08-04, последнее изменение документа 2026-08-13; живой текст — файл INCIDENT_LOG.md внутри Skill n8n-engineering-manual; Р-20 журнала projects/archivarius/LOG.md, решение Андрея в чате SYS 2026-10-11). Восстановлен 2026-08-11. Корень Диска, не папка SKILLS.
_SYSTEM папка:      1Y43bKpjWCkk3L0qi6dEfMfakF5jG_R2x
INDEX_FOLDER:       1UV-7hP0L2jiwPAtulPZ1gket-mdz0ktT

<!-- T-017 | CORE байт 13378-13561 | Р.2 N8N_REGISTRY (live snapshot, автообновление 05:30, воркфлоу gFFiBPm1OomOzJOj) -->
N8N_REGISTRY: 1zdz12-cwFZyHaHkKA8tJ1MvQKGCMN4xZdYztfYS3SOc (live snapshot, автообновление 05:30 ежедневно, воркфлоу N8N Registry Sync gFFiBPm1OomOzJOj)

<!-- 2026-10-05 | n8n-map Ф5, Р-8 журнала projects/n8n-map/LOG.md -->
N8N_CREDENTIALS: 1Ez-JSrgO6vO1oTSn11ry2mBb3vDrvNT5eM-8bTMcTvQ (закрытая таблица — реестр credentials инстанса n8n: лист «Авто» целиком пишет воркфлоу Credential Inventory qolCVtDpTo2YlnGb по ручному запуску, лист «Ключи» — Андрей и агент, лист «Правило имени»; читается gsheets-read; имён и прав credentials в repo нет)

<!-- T-024 | CORE байт 15080-15411 | Р.2 INFRA_CONTRACT (источник ID инструментов записи для изолированных контуров) -->
INFRA_CONTRACT: 1Jz0_xLGVRMOOFLQ55f5bUM93syreIZArAO6TlGis0J0 — единственный источник ID инструментов записи для всех изолированных контуров (SYS, DOSSIER, MED/Spiegel, Tutor) — статус ЭМБРИОН 2026-07-22 (канон: PROTOCOL_infra-contract, Р.14)

<!-- T-030 | CORE байт 18054-18281 | Р.2 MISSION_knowledge-loop (Главная Задача, цикл знания) -->

MISSION_knowledge-loop: 1FT4PsQLYY05ysR6FxiER7JIBBShlronAcOh6lpTM_oE (Главная Задача, цикл знания; зарегистрировано нарядом Н-13.08-01, 2026-08-13)

<!-- T-032 | CORE байт 19062-21840 | Р.2 контур обслуживания: AUDIT_CHECKLIST_maintenance, MAINT_HANDOFF, PROTOCOL_maintenance_v4, LOG_gap-monitor-findings, SYS_INDEX_SIZE_LOG -->

AUDIT_CHECKLIST_maintenance: 1K4ymRqgIKakpwtUMJFqlvr2t4Cr5jWEZHAAU5rvdoWY — чек-лист аудит-приёмки цикла обслуживания (см. Р.12), папка _SYSTEM, создан 2026-08-23, SA n8n — writer, read-back exec 47619 (checkSum b738f9c6). Статус КРАСНЫЙ до первого применения.
MAINT_HANDOFF: 1IP8CLSfWLE6CK-JqZmyj6F0t3HLiS7dmXjEH2FwGJO4 — журнал сводок обслуживания (append-only), шаг 1 маршрута по PROTOCOL_maintenance_v4. ПРИНИМАЕТ: сводки закрытых шагов цикла, доказательства exec-ID и checkSum, разбор дефектов цикла. НЕ ПРИНИМАЕТ: блок ЭСТАФЕТА, открытые наряды, записи ЗАХВАЧЕНО, задачи с критерием готовности; их адрес Зона А INDEX проекта. Основание: append-only файл не может нести объект, требующий перезаписи (context-handoff п.5), прецедент три активных блока ЭСТАФЕТА от 17.08, 19.08, 24.08, создан 2026-08-15, наряд Н-15.08-06.3, папка _SYSTEM. 
PROTOCOL_maintenance_v4: 1N0hs6BPbG1qP4C-9cSWFcFGPY_KhCip2t8Ych7B5Jqs — СНЯТ 2026-09-07, не читается (решение владельца, записи Р-89 и Р-93 журнала projects/git-migration/LOG.md; пометка внесена 2026-09-17). Документ не удалён и остаётся историческим следом; функцию харвеста ведёт meta/PROTOCOL_harvest.md репозитория second-brain-canon. Прежнее описание: процедура обслуживания одной сессией, действующие фазы в шапке документа, папка _SYSTEM, наряд Н-25.08-01, 2026-08-25
LOG_gap-monitor-findings: 1hg_hLpIWQbSVduS7e2a8K5rSzYBEJ1HtZYxvs6KNXNY — append-only журнал находок PROTOCOL_maintenance-gap-monitor, воркфлоу-производитель n8n 5Rs6pNDSm4weWDVj (cron пн 09:00 UTC, пишет только при anyFinding=true или parseBroken=true), читатель — шаг 0 Р.12 п.10 (хвост читается при каждом триггере "обслуживание", наряд Н-26.08-02). Создан нарядом Н-23.08-02, 2026-08-23.
SYS_INDEX_SIZE_LOG (таблица истории M1): 1Dm-mVKyXaFTEwFJRM_J16z8yQg4gu_axZTKy11e4w-4 — Google Sheets, append-снимок динамики размеров INDEX-файлов по проектам, воркфлоу-производитель n8n f7kdTpDADk7q0v2t "SYS Index Size + Zone Sync Monitor" (паспорт 1gyfjWMaTSdyx4QlHdfBVWpcKTHSsnvG0EM8IzVvkc8w, cron пн 09:00 UTC, с 2026-08-03), читатель — шаг 0 Р.12 п.10 (последние строки читаются при каждом триггере "обслуживание", наряд Н-26.08-02). ВНИМАНИЕ: не Google Doc, gdocs-read не читает — использовать read_file_content или Sheets-путь.

<!-- T-034 | CORE байт 22110-22627 | Р.2 PROTOCOL_index-surgery v2.2 (действующая версия) -->
PROTOCOL_index-surgery v2.2: 1i-OzunXciekeU6kUkmvPK9nDBGMNLiFuQIiGzwcHO-Y — пересобранный протокол хирургии INDEX-файлов (v2.0 утрачен до регистрации), папка _SYSTEM, назначение: канон Ф0-Ф8 + записьевой разрез с ID-манифестом для файлов с ID-плотностью + открытые уроки гейта Н-08.08-03 (FD, [ВОПРОС] провенанс D6-D28), наряд Н-14.08-06, 2026-08-14.

<!-- T-036 | CORE байт 23656-25143 | Р.2 SYS_JOURNAL_2026_02 (живой корпус-приёмник + доказательство инварианта реконструкции ПОТЕРЯНО=0) -->
SYS_JOURNAL_2026_02: 1m6_0LQUBTzDTQ1B2hbQg9wrEh3kmtAifa0mdQfQM9bc — ЗАМОРОЖЕН 2026-10-13 (последнее изменение документа 2026-08-30; прочитан целиком — Архивариус, запись Р-13 журнала projects/archivarius/LOG.md; пишущих в него воркфлоу, промптов и Skills нет — проверка 2026-10-13, Р-41 того же журнала); слова «тип ЖИВОЙ» ниже устарели. Прежнее описание: корпус-приёмник хирургии Н-15.08-05 (PROTOCOL_index-surgery v2.2, Раздел II, Ф2'/Ф3'), папка _SYSTEM, тип ЖИВОЙ, читатель 1rBU7c-xSL8D4kd5bXiAhk5UbVPOvAAhEWjiQIt3NByI, последний прогон 2026-08-13. Содержит 40 юнитов КОРПУС из SYS_INDEX (стамп-строка + юниты, разделители \n). Read-back (exec 43247): byteLength 17377, checkSum 787f9a03, 0 расхождений по 44 параграфам против эталона /tmp/corpus_full.txt (16326 байт, 75b3945a) — разница в байтах объяснена удвоением пустых абзацев при ручной вставке. SYS_INDEX после Ф3' (вставка Андреем, наряд Н-15.08-05): byteLength 174025, checkSum fc0cd0f1 (exec 43251, состояние С МОРАТОРИЕМ, флаг снимается следующим действием), 0 расхождений по 201 параграфу против эталона, инвариант реконструкции подтверждён: снимок Ф0 (117680 симв. без \r) = живое-после-Ф3' (107668 симв.) + корпус-юниты-исходные (10126 симв.) + 114 симв. намеренных указателей «см. корпус» (2×57) — ПОТЕРЯНО=0.

<!-- T-037 | CORE байт 25144-25497 | Р.2 PROJECT_LOG_SYS (журнал решений проекта SYS, пилот до 2026-09-20) -->
PROJECT_LOG_SYS (журнал решений проекта SYS; ЗАМОРОЖЕН 2026-09-26 — пилот закрыт по его собственному условию, Skill project-log-description отозван, Р-112 журнала projects/git-migration/LOG.md; читается только как история, не пишется): 1KT4ssADqRUny6rExLNdVxtPw4sNS-WBnY1f8-KfbiYo, папка _SYSTEM, расшарен на сервисный аккаунт, byteLength 5110, checkSum 66895212 на 2026-08-30. Контракт чтения и записи внутри самого файла.

<!-- T-039 | CORE байт 26161-26517 | Р.2 ПРАВИЛО: ID файла в Drive не меняется при перемещении или переименовании -->
ПРАВИЛО: ID файла в Drive НЕ меняется при перемещении или переименовании.
ID меняется только при удалении файла и создании нового.
После удалении и пересоздания — обновить ID в этом разделе.

<!-- T-107 | CORE Р.2 REPORT_H-25.08-01 (регистрация задним числом, сессия Аргус 2026-09-07) -->
REPORT_H-25.08-01: 1LRmdYNxKELAcM3iBJeAcyycI94iiBcb5cKxHAT_n9VY — отчёт по наряду Н-25.08-01, папка _SYSTEM. Не был зарегистрирован в Р.2 при создании (находка SYS Зона А, 2026-08-26); зарегистрирован сессией Аргус 2026-09-07.


<!-- T-108 | CORE Р.2 отчёт архитектора о миграции в Git (регистрация при создании, сессия Cowork 2026-09-17) -->
REPORT_git-migration_2026-09-17: 1LhAtFDlfmeQ8CYCM7P3QOpAlZPHPmFAcVnP-clFGcJA — «Миграция Second Brain в Git — отчёт архитектора, 2026-09-17», папка _SYSTEM. Человеко-читаемый отчёт для владельца, не канон и не источник правил: что пройдено по фазам ф0–ф4, сравнение Docs и git, оценка системы по четырём шкалам. Создан через create_file с contentMimeType text/html — форматирование сохранено, конвертация в родной Doc подтверждена чтением gdocs-read (сырой разметки в тексте нет). Наблюдение для будущих сессий: text/html через create_file работает и даёт заголовки, таблицы и списки — Skill `google-drive-docs` §2.1 называет обязательным text/plain, что верно для плоского текста, но не единственный рабочий тип. Числа-снимки (byteLength, checkSum) здесь намеренно не записаны: по открытому пункту О-8 такие снимки в реестре устаревают и числятся дефектом.


ARCHIVE_RECON_CATALOG: 1aRqQr6wRY3_p4_FFd4TJfyQXHZtGuLixj8UimZd0znU — Google Sheets «Каталог архива статей — archive-recon», лист «catalog» (17 колонок: path, source, top_folder, topic, topic_origin, doc_type, pages, size_bytes, year, year_source, doi, awmf_reg_nr, mm_status, duplicate_of, excluded, excluded_reason, processed_date), 495 строк данных на 2026-09-27. Не был зарегистрирован здесь при создании — ID отсутствовал в repo, следующая сессия не нашла бы таблицу; зарегистрирован задним числом сессией 2026-09-27 по решению Р-13 журнала projects/archive-recon/LOG.md. Лист «Sheet2» той же таблицы — не канон, содержит незавершённую, оборванную на полуслове заметку, статус и происхождение не выяснены (см. STATE.md проекта archive-recon).

ARCHIVE_RECON_EXPORTS: 1Hq1nxFaKM7knfZyY3nhy4SqYW5jZQWvt — папка Google Диска «Projekt archive-recon»: выгрузки скрипта archive_scan.py по тестовой папке «AA Beruf» (files.csv 1VXq7zJJOnktxmRK1HvnwqBVPaPDlUDV0, folders.csv, guidelines.csv, summary.txt, папка texts и её архив texts.zip 1oiyO8P_ZgQFJPOp3AD-aDdg9h2mCxDW-, кэш скрипта). Создана сессией Claude Code 2026-10-10 (Р-19 журнала projects/archive-recon/LOG.md). В repo из неё ничего не переносится: пути личных папок владельца и чужие тексты статей.

HARVEST_2026-10-08: 1AYwP1WPKpZtCSs2TcgYUBN4OpX_7_8QiOcgxFFR3EbE — «harvest-2026-10-08.md», полный пакет находок харвеста 2026-10-08 (редакция 2). Разобран сессией SYS 2026-10-09: правки внесены в девять Skills (зеркало `skills/`), решения по противоречиям — в позициях очереди и в `meta/PROTOCOL_harvest.md`. Читается только по вопросу «откуда взялась правка Skill от 2026-10-09».

DEKL_V2_MAP_workflows: 1crHd9h8lO8uAWIRazqINwltYlXh_D3ZJok5KzvVknvg — Google Sheets «DEKL_V2_MAP — воркфлоу», карта инвентаризации проекта deklaration-v2, блок 1: 58 воркфлоу по теме деклараций и кодов (ID, состояние, расписание, что читает и пишет по снимку n8n-map 2026-10-09, описание, паспорт, статус — предложение сессии, колонка решений Андрея для Ф3); папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ, расшарена на сервисный аккаунт n8n (writer); снимок 2026-10-10; создана сессией deklaration-v2 2026-10-10 (запись Р-4 журнала `projects/deklaration-v2/LOG.md`).

DEKL_V2_MAP_sheets: 1rpiFIB25IfuY78a6L0jJTvVoYxauPPtZCWmNzAFuM1o — Google Sheets «DEKL_V2_MAP — листы, источники, решения», карта инвентаризации проекта deklaration-v2, блоки 2–4: листы и колонки книг Справочник LM, Акт.цена, WB_RAW, Price Master, SKU_Artikel_Map, LM_DECL_MASTER и книг «Парсинг Деклараций *» (кто пишет, кто читает; строки DESIGN 02.10 с легендой кодов), источники истины по каждому коду, заголовки записей журналов старой версии со статусами; та же папка DOCS, расшарена на сервисный аккаунт (writer); снимок 2026-10-10; создана сессией deklaration-v2 2026-10-10 (Р-4).


<!-- 2026-10-11 | проект SERVER, доступ Claude Code к серверу; зарегистрировано при создании (Р6) -->
SERVER_claude-code-access_agent-en: 1_pl1PAViF5zNzYlovDawLqqTNI_7JDNOq6XbbkWzqGM — Google Doc (обычный, text/plain), папка INDEX_FOLDER, проект SERVER. Агентская копия на английском: как устроен разовый доступ Claude Code к боевому серверу (учётная запись claude-ops, четыре скрипта ops-*, правила и настройки на ноутбуке), решения Андрея 2026-10-11, состояние наряда по сервису распознавания. Секретов нет. Правится первой; русская копия ниже следует за ней. read-back 2026-10-11 (gdocs-read exec 78567): checkSum 022591bb, 40 строк. Документ временный: снять вместе с доступом claude-ops (решение Андрея).
SERVER_claude-code-access_ru: 1LKlWt_mML6beUbqz-bJ4JAe0fDk7daKZjV9CcG-Xfyw — Google Doc (обычный, text/plain), папка INDEX_FOLDER, проект SERVER. Русская копия того же для человека. read-back 2026-10-11 (gdocs-read exec 78568): checkSum 94da0344, 40 строк. При расхождении верна английская.

<!-- 2026-10-11 | проект deklaration-v2, фаза 5, блок «Эталон артикула»; зарегистрировано при создании (Р6) -->
DEKL_V2_BOOK: 1ASJ6sApvhWE2-o7bVCqKRaZaIcB6MxXN3FYWAOEpjQI — Google Sheets «DEKL 2.0 — эталон и сверка», книга 2.0 проекта deklaration-v2 (эталон свойств артикула, требования площадок, сверка «артикул × кабинет», очередь правок), папка DOCS проекта (1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ). Создана 2026-10-11 пустой, владелец — Андрей; расшарена на сервисный аккаунт n8n-liamin с правом редактора (get_file_permissions 2026-10-11). Листы и что они хранят — раздел 9 `meta/PRODUCT_DATA_HIERARCHY.md`; с 2026-10-13 в книге листы «Что где лежит», «Ввод», «Снимок КИЗ», «Эталон» (запись Р-11 журнала `projects/deklaration-v2/LOG.md`); листы создаёт и наполняет воркфлоу «DEKL 2.0 — Листы» `I3rU3hWHAHzUTWnv`, «Эталон» и новые строки «Снимка КИЗ» — «DEKL 2.0 — Эталон» `0jJSryMqJJqodL4K` (оба — инструменты, не опубликованы, запуск вручную). С 2026-10-17 в книге лист «Готовность WB» — готовность каждой карточки двух кабинетов WB к записи документа; строит воркфлоу «DEKL 2.0 — Готовность WB» `Z2mVOq6AQDwXyTo7` (инструмент, не опубликован, запуск вручную; запись Р-25 журнала `projects/deklaration-v2/LOG.md`).

DEKL_V2_WF_readiness: 1Md_v1O_DHgsXapX5UmCIW0cdSd9xwBRRkqQSmfcaV5E — Google Doc, паспорт воркфлоу «DEKL 2.0 — Готовность WB» Z2mVOq6AQDwXyTo7 (проект deklaration-v2), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ; создан 2026-10-17 create_file, перечитан gdocs-read (исполнение 81643); строку PASSPORT в описание воркфлоу вписывает Андрей (запись Р-27 журнала `projects/deklaration-v2/LOG.md`).

ARCHIVE_RECON_OCR_TEXTS: 1EscsvItOOyO1wDaHpyjtAOgR8KzglCVW — папка Google Диска «ocr_texts» внутри «Projekt archive-recon» (ARCHIVE_RECON_EXPORTS): 32 текста первых трёх страниц распознанных сканов, имена «<имя>.pdf.ocr.txt», первые четыре строки — SOURCE, LANG, PAGES и пустая. Создана воркфлоу n8n «ArchiveRecon OCR Scans Run» (ID 8ImKyDrw1Q2JIfHw) 2026-10-11 (Р-24 журнала projects/archive-recon/LOG.md). Рядом файл ocr_all.txt 1XV30i5EIdi4Y-o3GapxLjCNAyFSSCDOQ — все 32 текста одним файлом с разделителями «=====FILE: <имя> BYTES: <число>=====», собран воркфлоу n8n «ArchiveRecon OCR Texts Join» (ID NDY1YGwLIt4w3HQB, постоянный инструмент) для переноса в рабочую среду. В repo ничего не переносится.
ARCHIVE_RECON_SEARCH: https://claude.ai/artifact/GPeefjpcstBE4hzpxeaFZr — приватный артефакт «Поиск по архиву»: страница поиска по описи (497 PDF) и темам topics.py. Данные описи вшиты в страницу, версия 1 опубликована 2026-10-11 (Р-25 журнала projects/archive-recon/LOG.md). Исходные данные и topics.csv лежат только в рабочей среде сессии и в самой странице; на Диск не выгружены. С версии 6 (2026-10-13, Р-29 журнала projects/archive-recon/LOG.md) страница держит отметки и комментарии владельца в своей базе (коллекция notes, ключ — md5 содержимого файла) и кладёт их копию кнопкой на Google Диск в папку ARCHIVE_RECON_EXPORTS файлами archive-recon-notes-<дата-время>.json. Версия 10 (2026-10-13, Р-30 того же журнала): данные пересчитаны скриптом projects/archive-recon/tools/refine.py, страница принята тестом модели Opus; исходник страницы — сам артефакт (читать Artifact, action read). В той же папке ARCHIVE_RECON_EXPORTS лежит пробный файл archive-recon-notes-PROBE-2026-10-13.json (ID 1FAhnrXpulhsnL0LE5EzkPOx2yqA0QC3Y) — проверка формы вызова create_file, содержимого не несёт, удалять может владелец. Версии 11–12 (2026-10-13, Р-31 того же журнала): данные вынесены в файл data.json, опубликованный рядом со страницей (читать Artifact, action read, path data.json); шаблон страницы — projects/archive-recon/tools/search_page.html, сборка данных — projects/archive-recon/tools/build_data.py; у каждой записи ссылка на файл Google Диска; вкладка «Книги» — три книги по главам.
ARCHIVE_RECON_GUIDE: 1Vi0TPehMXYjLb-ZWyYJA_4L_M60vO99u0igBrnLXqY0 — Google Doc «Поиск по архиву — инструкция» (с оформлением) в папке ARCHIVE_RECON_EXPORTS: как пользоваться страницей поиска, книги, отметки, руководства, типы документов. Создан 2026-10-13 (Р-32 журнала projects/archive-recon/LOG.md); правится пересозданием или руками владельца — gdocs-overwrite снимает оформление.
ARCHIVE_RECON_DUP_REPORT: 1dfLABlJsD1R_gyDa3tHL-GOO7E1xrlMX — dup_report.txt в папке ARCHIVE_RECON_EXPORTS: разовый отчёт о повторах файлов «AA Beruf» (47 групп, ссылки на файлы), заменил вкладку «Дубли» страницы поиска (Р-31, Р-32 журнала projects/archive-recon/LOG.md).

<!-- 2026-10-14 | лаборатория OZON_UE, задача t-money-telegram; зарегистрировано при !save (Р6) -->
OZON_WF_money-telegram: 1QeXJwWfy-yusxe29JTiqj7FutVhEp9PJZSFiVOTztGk — Google Doc (обычный, text/plain), паспорт воркфлоу «OZON Money Telegram» YkUb5SnLtEaTctoH, папка DOCS лаборатории (1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ). Создан 2026-10-14 create_file; read-back gdocs-read exec 79888: byteLength 12483 равен длине исходника после преобразования Docs (переводы строк CRLF, пустые строки удвоены), checkSum 29b89c7a.


<!-- 2026-10-14 | проект WB_UE, ввод бренда Lopal; зарегистрировано при создании (Р6) -->
WB_MAP_product-price-chain_en: 1P8jHudxxfyp8PNqlwsagiK0H26RI4vnLLlavB4Nmwa8 — Google Doc (обычный, text/plain), папка DOCS проекта WB_UE (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Агентская копия на английском: карта цепочки «товар → цена → себестоимость» для Liqui Moly и Lopal — книги и ID, формулы Справочников, Акт.цена, sku_cost, Artikel, cost_price_history, витрины WB_Аналитика, 18 воркфлоу Price Master по узлам. Создан 2026-10-14 create_file; read-back gdocs-read exec 80139: byteLength 11293, checkSum 03b6df09. При расхождении верна английская.
WB_MAP_product-price-chain_ru: 1JBzHYrYAWXDNM4SY7aRcM3-YJ1pYh2QDtnzMcOz3NpE — Google Doc (обычный, text/plain), та же папка. Русская копия той же карты для человека. read-back gdocs-read exec 80141: byteLength 16483, checkSum 4243e4b2, 104 строки.

<!-- 2026-10-15 | проект WB_UE, Фаза 3 (разделение книги WB_Аналитика); зарегистрировано при создании (Р6) -->
WB_DESIGN_two-books_en: 1cbpowPVeRiyKnX9QQXx70lrFZ4hAF8cF1ERRwl8dLTE — Google Doc (обычный, text/plain), папка DOCS проекта WB_UE (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Агентская копия на английском: проект устройства двух новых книг «WB · Деньги» и «WB · Товары» — источники, лист «Параметры», правила счёта, себестоимость по дате, что не переносится, критерий приёмки. Создан 2026-10-15 create_file; read-back gdocs-read exec 80348: byteLength 14498, checkSum 8fc7a0fb. При расхождении верна английская.
WB_DESIGN_two-books_ru: 1pUTrATImP9sFoJJmjVGsnATbhDyb_staJqJxKvPtjRY — Google Doc (обычный, text/plain), та же папка. Русская копия того же проекта для человека. read-back gdocs-read exec 80349: byteLength 31693, checkSum 8f2faab6.

<!-- 2026-10-15 | проект WB_UE, Фаза 3, пакет А2; зарегистрировано при создании (Р6) -->
WB_MONEY_book: 1lapptqj5vHZzuvo1360-V6f07KKrwjNzJilGR1CxDT8 — Google Sheets «WB · Деньги», папка старой книги WB_Аналитика (1RrkB1rsVIQbJ4xMKTxQrjR7Gx1AVU7Ps). Новая книга денег WB по проекту WB_DESIGN_two-books: недели, месяцы, монитор, дашборд, текст Telegram; структуру строит скрипт wb_money_book.gs (вставляет и запускает Андрей). Создана 2026-10-15 create_file пустой, сервисному аккаунту n8n выдан доступ на чтение; проверка gsheets-read 80434 (один лист «Лист1»).

<!-- 2026-10-17 | проект WB_UE, запись Р-69; зарегистрировано при создании (Р6) -->
WB_RAW_ARCHIVE_2026-10-17: 1ke5wsN6NQm9z7mtU-FN0yLy5-HVhFbIAJ_Lue_H6YIs — Google Sheets «WB_RAW_Аналитика_АРХИВ_2026-10-17 (копия до удаления листов V1)», та же папка, что WB_RAW_Аналитика (1X4Qn8GW4YHM1eiKE_w5m1GGAj5koZ-7a). Полная копия книги WB_RAW_Аналитика на 2026-10-17, сделана copy_file Drive перед удалением старых листов wb_raw_report и wb_transactions из живой книги (предел 10 млн ячеек, Р-69 журнала projects/wb-ue/LOG.md). Только хранение, никто не пишет. Проверка gsheets-read 81720: 8 листов, размеры равны живой книге.

<!-- 2026-10-18 | проект gas-bridge, запись Р-1 его журнала; зарегистрировано при создании (Р6) -->
GAS_SANDBOX: 1Dm1luJ3YkSE2Tv8BV0DsMfgK1-E2Jc0_b51PYXUZeI0 — Google Sheets «gas-sandbox», корень Диска Андрея, создана подключённым Google Drive. Тестовая книга инструмента gas-bridge: к ней привязывается пробный скрипт и разрешена запись кода (строка access=write таблицы данных n8n gas_allowlist). Данные книги никто не читает; это мишень для проверок инструмента, не удалять.
PURCHASE_HISTORY_book: 1GZSACQW1ApG3YnpszjC0e5snjSqv2a0NeOzm4OkBbXA — Google Sheets «Закупка — история закупочных цен», папка книг «Деньги»/«Товары» Ozon (17xJlTNw48RmIB25UbFsOKpiseRGyAE7G). Лёгкая статичная копия листа cost_price_history книги sku_cost_Шаблон (колонки A Artikul, B sku, C effective_from, D effective_to, E cost_price, F brand) — будущая единая история закупки Ozon + WB; источник закупки для скриптов книг «Деньги» и «Товары» Ozon после переноса (задача labs/ozon-ue/t-cost-history-copy.md). Создана 2026-10-18 create_file Google Drive пустой (createdTime 2026-10-18T16:08:59Z); наполнение и доступ сервисного аккаунта — в той же задаче.


<!-- 2026-10-18 | проект card-content-sync, запись Р-12 его журнала; зарегистрировано при создании (Р6) -->
WB_WF_wb-copy-main-to-ip: 1bK_FYscfzIyUANdr_8VWhgXvjIj9d22gPmjlAfAPAhY — Google Doc, паспорт воркфлоу-инструмента «WB Copy Кипарис → ИП (инструмент)» dD7Y3XMZ0R1Uvsys (перенос карточек основного кабинета WB в кабинет ИП); папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан create_file 2026-10-18, текст прочитан gdocs-read (исполнение 82361).

<!-- 2026-10-20 | синтез Skill apps-script-sheets: ID снят из references/samples.md Skill, в реестре его не было -->
WB_ANALITIKA_book: 1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI — Google Sheets «WB_Аналитика», старая книга юнит-экономики Wildberries (витрина «норма → отклонение → светофор», скрипт WB_Monitor.gs). Заморожена окончательно 2026-10-17 (запись Р-69 журнала projects/wb-ue/LOG.md, пункт 8); её заменила «WB · Деньги» (WB_MONEY_book). Не удалять, пока «WB · Деньги» читает из неё wb_reports_official.


<!-- 2026-10-21 | разбор Skill n8n-workflow-registry по носителям: книги Google Sheets и правило проверки ID перенесены сюда -->
## Книги Google Sheets — имена, листы, кто работает; проверка ID по длине

Перенесено 2026-10-21 из Skill `n8n-workflow-registry` при разборе его по носителям (задача `projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md`, отчёт `meta/SYNTHESIS_n8n-workflow-registry_2026-10-21.md`); текст строк не правился, прежнее место — зеркало `skills/n8n-workflow-registry/` на коммите b91fb1e, SKILL.md, строки 18, 30, 64, 69–71, 75, 79, 81–96, 98, 104–106, 108; остальные строки тех же разделов — в маршрутизаторе Skill, в `projects/n8n/PLAN.md` или вынесены Андрею списком «предлагаю снять», перечень в отчёте. Утверждение «не названы нигде» ниже — снимок 26.09: с тех пор книга `1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI` названа в этом файле (WB_ANALITIKA_book), книга `1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4` — в `labs/ozon-ue/INDEX.md` (sku_cost_Шаблон). Пометка `[снимок ДД.ММ]` значит «сверено со строкой registry/n8n-map.md на эту дату», `[владелец ДД.ММ]` — «со слов Андрея»; строка без пометки набита руками и могла устареть. Слова «строка 35 выше» в абзаце о проверке ID по длине ведут к строке `wb_fbs_orders_tracking` этого файла; повреждённый ID в ней исправлен 2026-10-09, что там и записано.

Строки помечены источником. `[снимок ДД.ММ]` — сверено со строкой файла registry/n8n-map.md, то есть выведено из JSON инстанса. `[владелец ДД.ММ]` — со слов Андрея. Строка БЕЗ пометки набита руками, датой не подтверждена и может быть устаревшей. Это и есть причина не заводить здесь ничего, что выводится из объекта: непомеченная строка живёт ровно до того дня, когда объект изменится, и никто об этом не узнает.

Строка таблицы «Чего здесь нет» прежнего Skill о книге ключей N8N_CREDENTIALS (ID книги — строка N8N_CREDENTIALS этого файла):

| Что нужно | Где |
|---|---|
| Какой credential привязан к какому узлу, активен ли он в узле, на какой хост узел его отправляет; права, сроки, магазин и юрлицо ключей | закрытая книга N8N_CREDENTIALS, ID — в registry/documents.md. Лист «Авто» перезаписывает воркфлоу Credential Inventory qolCVtDpTo2YlnGb по ручному запуску; лист «Ключи» — ручное знание по ID credential; лист «Правило имени» — правило имени нового ключа «<Сервис> · <Юрлицо> · <R или RW>» (R — только чтение, RW — чтение и запись). Исключение владельца от 2026-10-06: ключи Wildberries называются с русским словом и признаком права, например `WB_Контент_ИП_R`, — токенов Wildberries много, и по общему правилу их не различить (projects/deklaration-wb/STATE.md). Лист «Правило имени» этого исключения пока не содержит — правит владелец. Читать через gsheets-read, диапазон с номером строки (A1:Z1100) |

Снимок отвечает строками D на вопрос «какие воркфлоу и какими узлами трогают документ с этим ID». На обратный вопрос — «какой ID у книги, которую человек зовёт Price Master» или «в какой книге лежит лист seen_posts» — он не отвечает: человеческих имён в нём нет, а имя листа узел раскрывает не всегда. Этот раздел и есть ответ на обратный вопрос, поэтому ID отсюда не убираются.

- **Reviews Queue** — `1mgtcD2wSm_-8hqfpv3v883KE34-Smy-kFxHvt6zMXj4`, листы `ozon_reviews_queue` и `ozon_qa_queue`; 20 узлов [снимок 26.09].
- **Price Master** — `1mntwAaplJSn3bHczqGDrzmBjotrsHe3MZ78ChViCDVk`, листы `Artikel` и `CURRENT`; 8 узлов [снимок 26.09].
- **SKU_Artikel_Map** — `1dJN-wWrzr4LKi9FPTkbOpAu6N-LMymxiF-WJEFJPlCU`, листы `SKU_Artikel_Map` и `MASTER_MAP`. MASTER_MAP — таблица соответствия `sku + lm_id + ozon_sku + wb_nm_id`; это ЛИСТ внутри этой же книги, а не отдельный файл: узел `16_Write_WB_nmID` пишет в этот лист по тому же ID книги [снимок 26.09]. Источником истины MASTER_MAP НЕ является: это снимок, собранный скриптом 19.06.2026, и он отстаёт от живых данных — например, у нашего артикула 1908 в MASTER_MAP стоит `ozon_sku` = 0, а в Price Master, лист `Artikel`, настоящий SKU Ozon. Живой источник соответствия артикулов — **Price Master, лист `Artikel`**. По решению владельца 2026-10-02 MASTER_MAP выводится из употребления после того, как его читатели переключатся на Price Master (задача labs/ozon-ue/t-master-map-ozon-sku.md, запись 2026-10-03 — задача закрыта коммитом 69fe7bd, текст читается по его родителю; шаг 5 задачи labs/ozon-ue/t-product-data-model.md).

- **LM_DECL_MASTER** — `1PO7vNyoY16tYqpU_KB5xuK4aSAbOU7YW_MM0scg5ksY`; 13 узлов; там, где узел раскрывает имя листа, это `LM_DECL` [снимок 26.09]. Лист `Decl_Monitor` — дашборд со светофором; ни одним узлом не трогается, поэтому в снимке его нет [снимок 26.09]. Прежняя редакция этого файла называла рабочим листом именно `Decl_Monitor` — это описывало дашборд для человека, а не то, куда пишут воркфлоу.

Двадцать девять книг из сорока одной, которые трогают воркфлоу, не названы нигде: ни здесь, ни в `registry/documents.md`. Ниже те, что используются тремя и более узлами, опознанные по именам листов и воркфлоу. Человеческого имени у них нет — это долг, а не факт; кто знает имя, дописывает его сюда.

| ID книги | Листы | Кто работает | Узлов |
|---|---|---|---|
| `1P-GgiFm3067U_sgC2Dojos3BbT_-au6v-mT52vVT3y4` | `sales_raw_operations`, `ozon_raw_accrual_TEST`, `ozon_accrual_types` | конвейер OZON_UE RAW целиком | 19 |
| `1qdefReY1qHfWdwroorbxz2Bi20_3dsGHuDBiYy2W_XQ` | `wb_fbs_orders_tracking`, `wb_fbs_monitor_params`, `wb_fbs_performance_log` | WB FBS Decision Engine, Evening Report, Morning Forecast, Order Close v2 | 19 |
| `1JwV7bbfLLxztE7gRrUEOUIvUk-xCOcwDkT88RA5bHPg` | `wb_reviews_archive` | WB Reviews Intake, Publication, History Load, Full History Load | 17 |
| `1XMy8XsF4tIyiPIhiW2dAt8Sihbsy4xQOXWQhjCJEHyE` | `kb_motor_oil`, `Шаблон` | KB Loader Motor Oil, KB MO Annotation Preprocessor, KB Sync Motor Oil Specs | 15 |
| `1eQPV1KQ2FE4kV935KV3_05c6VgbRZkU0y4DwFgTIEL4` | `SKU_Artikel`, `cost_price_history` | OZON_UE Cost Price Snapshot и Backfill, Accrual-адаптер, SKU Category Backfill | 14 |
| `1AhgaspMQl3wLsVT7Iub0d195r8DwwUarhQAWwjBO8xE` | `wb_fbs_params`, `wb_fbs_supplies`, `wb_fbs_decision_log`, `wb_fbs_forecast_snapshot` | тот же конвейер WB FBS | 12 |
| `14QMHYMM4mZRnnq1wHQA4_SA8ZnOeE1xcVJDL2h9h1Pk` | имя листа узлы не раскрывают | WB RAW Finance Sync V.3, WB RAW History Load V.3 CLEAN | 6 |
| `17j3EOOGPFwnjF9RQbZzll-4Cm6JD8Cd5mNqm_p9AOBU` | `Акт.цена`, `Акт.цена_backfill` | OZON_UE Cost Price Snapshot и Backfill | 4 |
| `1sBYaluh1NDkb0zVmbV-NX4jsNbawEpXlae8fRg2AiuI` | `dashboard`, `wb_reports_official` | WB Reports Official Sync, WB Monitor Telegram Reader | 4 |
| `1eujHu87IO0IlngLX164_O81LxPI5NNpq9S47E8anVSo` | имя листа узлы не раскрывают; здесь лежит `seen_posts` | WB+Ozon News Filter | 3 |
| `1gPjWlhld9LAzGScEU9l63OGfcXK48dujYX1A9Uh6gBk` | имя листа узлы не раскрывают | KB Loader Transmission Oil, KB TO Annotation Preprocessor | 3 |
| `1sPD5SAFCTygzUaEPg8RKRPHQyc0HCMIK-aMpnXqYu3k` | имя листа узлы не раскрывают | KB Loader Auto Chemistry, KB AC Annotation Preprocessor | 3 |
| `11j0yKZ0FvE9EbZiTzCStEACsgecliaElVccpUixmQcQ` | имя листа узлы не раскрывают | Контроль Price WB | 3 |
| `1cK5dues1ffnUdy6UGCDHiMzxp1ZucdyvawS5Dvx-o3M` | имя листа узлы не раскрывают | SYS Lint | 3 |

Все строки таблицы — [снимок 26.09]. Полный список из сорока одного документа с их узлами достаётся из снимка одной командой: `grep '^D|' registry/n8n-map.md`.

ID попадает в канон только из объекта или из поиска этой же сессии — не по памяти и не перепечаткой из другого текста: перепечатанная руками копия уже повредилась (строка 35 выше). Дешёвая проверка перед записью любого ID Google — длина:
- документ Google Docs и книга Google Sheets — 44 знака;
- папка Google Drive — 33 знака.

Другая длина — ID повреждён или это не ID Google (например, ID Claude Project длиной 36 знаков с дефисами). Длина ловит пропуск и лишний знак, но не замену одного знака другим; сверка по объекту остаётся единственным доказательством. Происхождение: projects/n8n-map/PLAN.md, зонд Z-10; projects/deklaration-ozon/LOG.md, Т-3.

Паспорт воркфлоу `OzonRawАналитика` (`MPzPrtsnPtf0sVQo`): `1_E2KCZOVYaf68xVECwv9ZaGGn4bdz3jsh5D3lhsqdyM`; паспорт воркфлоу `Ozon RAW Accrual Sync` (`aVpgEnYBAgIIss4k`): `1hcAxLuj3YBSPUrOe8bYNbFD6ib8r7y56Pv1Ad8j1j8w` (строки 217–218 прежнего Skill; ID паспортов там шли без пометки источника).


<!-- 2026-10-21 | проект N8N, автопилот «паспорта воркфлоу без паспорта»; зарегистрировано при создании (Р6) -->
N8N_WF_error-notifier: 1QwibBtjfU-RsoK68lhDmALwEqo0zJ8qHJSltbEUtcaE — Google Doc (обычный, text/plain), паспорт воркфлоу «Error Notifier» M5BLqclKBjGTpz33, папка DOCS проекта N8N (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Создан 2026-10-21 create_file; независимая приёмка и чтение через gdocs-read пройдены.
N8N_WF_git-append-file: 1JKu_9yOFEwv-tkcIFeIYfPKA1AMGkEC0riKD1TuRX7g — Google Doc (обычный, text/plain), паспорт воркфлоу «Git Append File» Nzgy6Q1XwXQVxt1F, папка DOCS проекта N8N (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Создан 2026-10-21; приёмка пройдена.
N8N_WF_gsheets-append: 1TUS-1LNcrxw7E7pnp7bRCUGYQbJnvwiHCYH0c24DTWw — Google Doc (обычный, text/plain), паспорт воркфлоу «Claude → Google Sheets Append» LNlWIEdH0tkzmqPB, папка DOCS проекта N8N (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Создан 2026-10-21; приёмка пройдена.
N8N_WF_wb-finance-call: 1p4Kf_lmyhcHjw91ds_yFZSjD3j1-JCr773Ek57REafE — Google Doc (обычный, text/plain), паспорт воркфлоу «Claude → WB Finance API Call» H84pqpqX1qf85Pj6, папка DOCS проекта N8N (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Создан 2026-10-21; приёмка пройдена.
N8N_WF_gscript-bridge-call: 1VEQ6gfhDCzE_scNysE5X-objae_FTOKqgi4uFnY1bP0 — Google Doc (обычный, text/plain), паспорт воркфлоу «Claude → Google Apps Script Bridge · Call» j0DU23IXnp7xggX9 (подворкфлоу моста gscript-bridge 38BkuLXhxXLTPpqQ), папка DOCS проекта N8N (1nOwTGH6AR9vKfM1VM-mThfnRmDAaeOZn). Создан 2026-10-21; приёмка пройдена.
OZON_UE_WF_accrual-types-sync: 1Iieo4QAc9vccCWwwP7m6Nw8VWKMVxBzerh_2fgb3YiE — Google Doc (обычный, text/plain), паспорт воркфлоу «OZON_UE Accrual Types Sync» c7TIdv32dHV3MBRU, папка DOCS лаборатории OZON_UE (1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ). Создан 2026-10-21; приёмка пройдена без замечаний.
OZON_WF_sku-staging: 13Q-CrUX4ig1JLo2fwXeH0vEfyEJahG0zh54OJJsTj4E — Google Doc (обычный, text/plain), паспорт воркфлоу «Получение SKU Ozon» J0v5swjXLfiANJa2, папка DOCS лаборатории OZON_UE (1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ). Создан 2026-10-21; приёмка пройдена без замечаний; старые «TECH»-документы воркфлоу остаются справкой.
LM_WF_deklaration-hydraulisches-oil: 1Tnsin1yqxgrGVwYRQJpRjGRq_FW3_CJGX1mX6GzvBW0 — Google Doc (обычный, text/plain), паспорт воркфлоу «Deklaration_Hydraulisches_Oil_V.4» EH2JaB8WGa0JsBqs (старое поколение до LM_DECL), папка DOCS проекта deklaration (1XiC_aP_vYnMv5oByZ_JNpONxF8Etb05q). Создан 2026-10-21; приёмка пройдена.
OZON_WF_fields-probe-ip: 1xSjFFUBysmVmYsMYxbPd9Xkxkyiqgl5V58uwsQ9bSKg — Google Doc (обычный, text/plain), паспорт воркфлоу-инструмента «Ozon Fields Probe (ИП)» m6svDS7yhrTjTCrt (проект deklaration-ozon), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан 2026-10-22 create_file, перечитан gdocs-read (исполнение 84159, byteLength 9662).
OZON_WF_upload-ip: 1HHHdpSxaiXV2DZwTXUigJkDnr_FscisEPDhrS2m4aqw — Google Doc (обычный, text/plain), паспорт воркфлоу «LM_DECL — Ozon Upload ИП» GElwjPKkJQkCao3b (проект deklaration-ozon), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан 2026-10-22 create_file, перечитан gdocs-read (исполнение 84160, byteLength 10175).
OZON_WF_copy-main-to-ip: 18Fhj9MvYa7a0ypRmF92PhrNHiNN1u2g7Cmm3GIP9ge0 — Google Doc (обычный, text/plain), паспорт воркфлоу-инструмента «Ozon Copy Осн → ИП (инструмент)» u06pa4u5sDYdQD3W (лаборатория OZON_UE, задача labs/ozon-ue/t-ozon-ip-card-copy.md), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан 2026-10-22 create_file, текст перечитан gdocs-read (исполнение 84210, маркер конца зоны В на месте). Отчёт инструмента — лист «Перенос в Ozon ИП» книги «Описания карточек» 1IE0B89Pd1jVdDpgkjqb3pgJow3cFtimYY07RSEAnO6Y (лист создан инструментом 2026-10-22, перезаписывается каждым прогоном).
OZON_WF_card-fields-fix-ip: 1gtMouRk57m288qAxe0-82xDpfn4svGgDN5FAIq9c1D0 — Google Doc (обычный, text/plain), паспорт воркфлоу «Ozon Card Fields Fix (ИП)» eLBcH8MeE38NbMZq (проект deklaration-ozon), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан 2026-10-22 create_file, перечитан gdocs-read (исполнение 84161).
OZON_IP_FIELDS_2026-10-22: 1pL7J19M_CAZLkGhQqORU_f0lkXfaIjJhgu64gpUwk64 — Google Sheets «ozon_ip_after_2026-10-22», снимок кабинета Ozon ИП после записи 2026-10-22: по каждому из 169 товаров ТН ВЭД, «Нужен код маркировки», эталоны и привязанная декларация (проект deklaration-ozon, `projects/deklaration-ozon/LOG.md` Р-49, Р-50). Сделана Андреем из CSV сессии; ID — слово Андрея в чате 2026-10-22, объект сессией не открывался.

SYS_PROMPT_BACKUP_2026-10-23: 11zdW334LJEz-7rbP2mJtRQvPqUk0_qR4mIn6CCbOVK0 — Google Doc «MASTER PROMPT — SECOND BRAIN SYSTEM ENGINEER 23-10-2026», сохранён Андреем 2026-10-23 перед вставкой нового мастер-промпта SYS. По тексту, прочитанному 2026-10-23 (экспорт text/plain), это прежняя редакция: старт двумя пакетами без meta/PENDING_RULES.md, блок «Особенности проекта» со ссылкой на раздел «СТАРТ КАЖДОЙ СЕССИИ». Назначение — откат промпта; действующий текст — Project instructions проекта SYS, его ожидаемый blob sha — дополнение 2026-10-23 в meta/DRAFT_master-prompt-sys_2026-10-22.md.

<!-- 2026-10-23 | проект FINANZEN, онбординг (Р4) в чате SYS; зарегистрировано при создании (Р6) -->
FINANZEN_INDEX: 1cdygEpOvnuf0wMuZK-TuQHVhff_yRNVGZXSW5kwSU0s — Google Doc (обычный, text/plain), INDEX проекта FINANZEN (налоговый и финансовый аналитик), папка INDEX_FOLDER. Изолированный контур: канон проекта — этот документ и папка FINANZEN_FOLDER, в репозиторий содержание не переносится (личные финансовые данные, И-7 second-brain-git; решение Андрея 2026-10-23). Создан 2026-10-23 create_file, перечитан gdocs-read (исполнение 84883, byteLength 6961, checkSum f9e1c6a6, строка SENTINEL и разделитель ЗОНА Б на месте).
FINANZEN_FOLDER: 1U-OiXIX3F661sOs0Lst-Ps1WMOQh6kGG — папка Google Диска «FINANZEN» внутри папки «AA Haushalt» (рядом папки по годам «20xx Steuer» — исходные документы Андрея); место реестров и зеркала мастер-промпта проекта FINANZEN. Создана 2026-10-23 create_file Google Drive.
FINANZEN_PROMPT_EN_red2: 1p_EeD_tUmLrYhLTx5MYw4nPIWNF6S1Ka — файл «FINANZEN_masterprompt_EN_red2_2026-10-23.md» (text/markdown, не Google Doc) в папке FINANZEN_FOLDER: английская копия мастер-промпта проекта FINANZEN, редакция 2 от 2026-10-23, — текст, выданный Андрею для вставки в Project instructions проекта «Finanz» (адрес — registry/projects.md, карточка FINANZEN). Андрей вставил его 2026-10-24 (по словам Андрея; поле инструкций сессией не читается). Зеркало лежит на Drive, а не в meta/prompts/: промпт описывает структуру доходов Андрея (особенность 4 блока Второго мозга). Создан 2026-10-24 create_file; размер 10 415 байт равен файлу сессии, содержимое скачано download_file_content, побайтовой сверки не было.
FINANZEN_PROMPT_RU_red2: 13oBa1F6kvn27Z-APbueEuXdgO_fq1X0XNsWhOLmaKdY — Google Doc (красивый, text/html) в папке FINANZEN_FOLDER: русская копия того же промпта для чтения Андреем, редакция 2. Правится пересозданием или руками владельца — gdocs-overwrite снимает оформление. Создан 2026-10-24 create_file, перечитан gdocs-read (исполнение 85186, byteLength 19206, checkSum 4e5fb7f8, сырой разметки нет, последний раздел на месте). При правке промпта менять обе копии; при расхождении права английская — её исполняет агент.
<!-- 2026-10-24 | проект marketplace-rebuild, запись Р-10 его журнала; зарегистрировано при создании (Р6) -->
MKT2_PROBE_SCRIPT: 13ZH74ISt-bO67BzGfo7h1HcUOuKE-R2RZTLDlnc6KcY — Google Sheets «MKT2 Probe Script», корень Диска Андрея, копия книги GAS_SANDBOX через copy_file Drive 2026-10-24. Связанный скрипт 1_tbz5VAOf8vTjbsMgxRu63VVPEWzuCrfgSVxy3tnZrnWQq6dp38mGrwW, строка 5 таблицы n8n gas_allowlist (access=write). Мишень пробы 3 этапа 0 перестройки маркетплейсов (объект MKT2); данные книги никто не читает; инструмент, не удалять и не архивировать (инвариант 4 PLAN.md проекта).
OZON_WF_cost-price-snapshot: 1WlgpetxvpFXDtR1dmNZmdepvdXQ7xUb0qA3TIi4qENY — Google Doc (обычный, text/plain), паспорт воркфлоу «OZON_UE Cost Price Snapshot» 2UsyP3q5Jd9OafJD (лаборатория OZON_UE), папка DOCS 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ. Создан 2026-10-24 create_file, перечитан gdocs-read (исполнение 85744, byteLength 8888, последняя строка — маркер конца зоны В). Строку PASSPORT в описание воркфлоу вписывает Андрей.


WB_GOODS_book: 1LprTMVMDB5dG36s1gE5MzpUHYegLdvvGyfMcqTfz9Nc — Google Sheets «WB · Товары», папка «WB · Деньги» (1RrkB1rsVIQbJ4xMKTxQrjR7Gx1AVU7Ps). Книга товаров WB (пакет 6 контракта Н-24.10-01): вклад по артикулам и брендам, ABC, матрица, флаги, классы по месяцам; структуру строит скрипт wb_goods_book.gs. Создана 2026-10-25 create_file пустой, сервисному аккаунту n8n выдан доступ на чтение; проверка gsheets-read 86288 (один лист «Лист1»).

WB_PRICE_book: 1yd7gM3eOkPsf3V0CPI_VNwjaT7cqlvMRhqiUGX1EFGo — Google Sheets «WB · Цена», та же папка. Калькулятор цены продажи WB по артикулу по образцу книги Ozon «Цена» (расширение контракта Н-24.10-01 в projects/wb-ue/PLAN.md); структуру строит скрипт wb_price_book.gs. Создана 2026-10-25 create_file пустой, сервисному аккаунту n8n выдан доступ на чтение; проверка gsheets-read 86289 (один лист «Лист1»).

<!-- 2026-10-26 | проект marketplace-rebuild, наряд Андрея на паспорта воркфлоу MKT2; зарегистрировано при создании (Р6) -->
MKT2_DOCS_FOLDER: 1vECymYl2-U_NgUlO43dp47X0x2sk-Mot — папка Google Диска «MARKETPLACE_REBUILD DOCS» (корень Диска Андрея), место паспортов воркфлоу MKT2; строка DOCS_FOLDER — в PLAN.md проекта. Сервисному аккаунту n8n доступ НЕ выдан (gdocs-read отказал 2026-10-26), чтение паспортов — запасным путём коннектора Drive.
MKT2_WF_collect-family: 1RYrxAU5A8h-SC6mSqMsC7B9Ca7V0r0oVPvTcHXUYSQo — Google Doc (text/plain), семейный паспорт 16 сборщиков «MKT2 Collect /<путь API>», таблица «воркфлоу → путь API → кабинет → ключ». Создан 2026-10-26 create_file, перечитан read_file_content (полный, маркеры зон на месте).
MKT2_WF_collect-engine: 10bnY5rOUeUuiKWFmXCnDpRP9UdYTOdAyBN9KsVpWHCk — Google Doc (text/plain), паспорт «MKT2 Collect Engine» pd2K2KtImWlFfueW с реестром сборщиков. Создан 2026-10-26 create_file, перечитан read_file_content (полный).
MKT2_WF_mirror-ref-article: 1DojlhAB0cBmz_ETp60X5u3FODB65y9TZy-sbDMBvSgw — Google Doc (text/plain), паспорт «MKT2 Mirror ref.article» R5a2wT4emV9sUBT4. Создан 2026-10-26 create_file.
MKT2_WF_api-ip-ozon-ozon-seller: 1oREuMbrBS3L1qcdNYHEbGojq8v3d-yP10a4uG0aHIGs — Google Doc (text/plain), паспорт посредника «MKT2 API ip_ozon ozon_seller» 95w8XpN3OHNl2NsE. Создан 2026-10-26 create_file.
MKT2_WF_api-ip-wb-wb-content: 1Y1GezDbdoOSB4JJaEISYm7HF43aM31rJ3qx8LqBBH7w — Google Doc (text/plain), паспорт посредника «MKT2 API ip_wb wb_content» JzoU49Wy2soTzZ44. Создан 2026-10-26 create_file.
MKT2_WF_api-ip-wb-stat-fin-an-price: 1AeZ9xe645pky9jlHDPL43E1VFcfXyB3dFRWXKRLHyxw — Google Doc (text/plain), паспорт посредника «MKT2 API ip_wb wb_statistics+finance+analytics+prices» ZhpjwjErqHEpoFCA. Создан 2026-10-26 create_file.
