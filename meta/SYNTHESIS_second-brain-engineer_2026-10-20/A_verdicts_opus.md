/home/claude/second-brain-canon/meta/SYNTHESIS_second-brain-engineer_2026-10-20/A_verdicts_opus.md

# Группа А — вердикты С5, второй независимый проверяющий (Opus)

Old text: `git show baa077c:…`. New text: working tree `skills/second-brain-engineer/SKILL.md`, `references/write-moment.md` (+ `references/permissions.md` where a unit moved). Units: `A_units_opus.md` (229). Every В ТЕКСТЕ quote was checked by script to occur verbatim in the named new file; every ПО АДРЕСУ address checked by `sed -n <line>p` + grep in the clone.

## Count

| verdict | count |
|---|---|
| В ТЕКСТЕ | 204 |
| ПО АДРЕСУ | 17 |
| СНЯТИЕ ПРЕДЛОЖЕНО | 6 |
| ОСЛАБЛЕНО | 2 |
| ПОТЕРЯНО | 0 |
| total | 229 |

Precondition for every ПО АДРЕСУ with «отчёт синтеза, правило X»: the file `meta/SYNTHESIS_second-brain-engineer_2026-10-20.md` DOES NOT EXIST yet; the table lives in `A_WRITER_REPORT.md`. Verdicts hold only after the dispatcher transfers that table with the same rule ids.

## 1. Per-unit verdicts

| id | verdict | new location | quote from new text (≤80) | note |
|---|---|---|---|---|
| A-O001 | В ТЕКСТЕ | SKILL.md:2 | name: second-brain-engineer |  |
| A-O002 | В ТЕКСТЕ | SKILL.md:3 | ОБЯЗАТЕЛЬНО читай в каждом Claude Project |  |
| A-O003 | В ТЕКСТЕ | SKILL.md:3 | старт сессии до ответа на первое сообщение, команды !save |  |
| A-O004 | В ТЕКСТЕ | SKILL.md:3 | Полевой регламент поведения — триггер |  |
| A-O005 | В ТЕКСТЕ | SKILL.md:3 | Эталонный блок мастер-промпта и онбординг |  |
| A-O006 | В ТЕКСТЕ | SKILL.md:3 | Механика чтения и записи файлов репозитория |  |
| A-O007 | В ТЕКСТЕ | SKILL.md:6 | # SECOND BRAIN — ПОЛЕВОЙ РЕГЛАМЕНТ |  |
| A-O008 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History; Andrei decision 2026-10-18 п.2. Address: commit baa077c. |
| A-O009 | ПО АДРЕСУ | SKILL.md:14 | история коммитов зеркала | history.md deleted; new address = commit history of mirror; baa077c holds history.md (verified `git show`). |
| A-O010 | В ТЕКСТЕ | SKILL.md:12 | единственное место регламента Второго мозга для всех Claude Project |  |
| A-O011 | В ТЕКСТЕ | SKILL.md:12 | несёт только адрес проекта, триггер старта, слова-команды |  |
| A-O012 | В ТЕКСТЕ | SKILL.md:12 | а старт, захват, !save и команды исполняются отсюда |  |
| A-O013 | В ТЕКСТЕ | permissions.md:30 | Правка Skill действует только после перезаливки | Moved to Р13 (permissions.md line 30); SKILL.md line 12 points «Когда правка этого Skill начинает действовать — Р13». |
| A-O014 | В ТЕКСТЕ | SKILL.md:16 | правило ждёт подтверждения Андрея |  |
| A-O015 | В ТЕКСТЕ | SKILL.md:16 | при возражении — спросить, не откатывать молча |  |
| A-O016 | В ТЕКСТЕ | SKILL.md:10 | Формат каждого блока: **ТРИГГЕР** — когда применять |  |
| A-O017 | В ТЕКСТЕ | SKILL.md:10 | Нет проверки — блок не закрыт. |  |
| A-O018 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History of the split; address baa077c + t-knowledge-synthesis.md. |
| A-O019 | В ТЕКСТЕ | SKILL.md:20 | Этот файл читается всегда. |  |
| A-O020 | В ТЕКСТЕ | SKILL.md:20 | читается перед своим действием, целиком, по таблице ниже |  |
| A-O021 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History; address baa077c. |
| A-O022 | ОСЛАБЛЕНО | SKILL.md:20 | Номера пунктов общие для всех файлов Skill | Old: numbers «сохранены прежними» (no renumbering). New: numbers are a shared namespace across files. The no-renumber statement is gone from text (it is only contract Э-3). Low impact. |
| A-O023 | В ТЕКСТЕ | SKILL.md:22 | Раздел, чья строка ТРИГГЕР называет конкретное событие |  |
| A-O024 | В ТЕКСТЕ | SKILL.md:22 | «любое действие», «любое утверждение» или «любая запись», и два исключения |  |
| A-O025 | В ТЕКСТЕ | SKILL.md:22 | захват (Р6) — он срабатывает почти в каждом ответе |  |
| A-O026 | В ТЕКСТЕ | SKILL.md:22 | решение о нём принимается до вызова инструмента |  |
| A-O027 | В ТЕКСТЕ | SKILL.md:22 | исключение Р21 — 1 случай, последний 2026-10-20 — отчёт синтеза | Generalised to «из references/ его не открыли» + basis line; report table address labs/sys/t-knowledge-synthesis.md line 219 verified. |
| A-O028 | В ТЕКСТЕ | SKILL.md:22 | Новое правило обязано назвать триггер, и триггер определяет файл |  |
| A-O029 | В ТЕКСТЕ | SKILL.md:22 | правило без триггера в Skill не входит |  |
| A-O030 | В ТЕКСТЕ | SKILL.md:22 | Основание: решение Андрея 2026-10-20 (`meta/PLAN_skill-layers_2026-10-20_v3.md` |  |
| A-O031 | В ТЕКСТЕ | SKILL.md:26 | \| Что собираешься сделать \| Что прочитать до этого \| Пункты \| |  |
| A-O032 | В ТЕКСТЕ | SKILL.md:28 | \| references/onboarding.md \| Р2, Р3, Р4, Р5 \| |  |
| A-O033 | В ТЕКСТЕ | SKILL.md:29 | записать урок после выдачи промпта (раздел «Урок после выдачи») |  |
| A-O034 | В ТЕКСТЕ | SKILL.md:30 | \| запустить харвест \| references/harvest.md \| Р11 \| |  |
| A-O035 | В ТЕКСТЕ | SKILL.md:31 | спроектировать новый Skill / протокол / архитектурное решение |  |
| A-O036 | В ТЕКСТЕ | SKILL.md:31 | снять или заменить действующую процедуру, монитор или журнал |  |
| A-O037 | В ТЕКСТЕ | SKILL.md:31 | построить проверку, приёмку, аудит или замер |  |
| A-O038 | В ТЕКСТЕ | SKILL.md:32 | выполнить !save (repo-проект, лаборатория или Docs) |  |
| A-O039 | В ТЕКСТЕ | SKILL.md:33 | начать сессию: первое сообщение в Claude Project |  |
| A-O040 | В ТЕКСТЕ | SKILL.md:34 | ответить на команду: сообщение Андрея начинается с !save |  |
| A-O041 | В ТЕКСТЕ | SKILL.md:34 | для !save затем references/save.md, для харвеста |  |
| A-O042 | В ТЕКСТЕ | SKILL.md:35 | действие затрагивает другой проект; Андрей просит найти документ |  |
| A-O043 | В ТЕКСТЕ | SKILL.md:36 | изменить воркфлоу n8n; действие, требующее «да» Андрея |  |
| A-O044 | В ТЕКСТЕ | SKILL.md:36 | выдать наряд или задание исполнителю |  |
| A-O045 | В ТЕКСТЕ | SKILL.md:37 | записать в канон идентификатор, число или дату |  |
| A-O046 | В ТЕКСТЕ | SKILL.md:38 | работать над проектом вне Claude Project (Cowork |  |
| A-O047 | В ТЕКСТЕ | SKILL.md:38 | вскрылся факт, требующий правки CORE, задачи лаборатории |  |
| A-O048 | В ТЕКСТЕ | SKILL.md:40 | выяснить, почему правило этого Skill изменилось |  |
| A-O049 | В ТЕКСТЕ | SKILL.md:44 | ## Р0. Два носителя — один разделитель |  |
| A-O050 | В ТЕКСТЕ | SKILL.md:46 | **ТРИГГЕР.** Любое действие с документом системы. |  |
| A-O051 | В ТЕКСТЕ | SKILL.md:49 | Определить носитель документа. |  |
| A-O052 | В ТЕКСТЕ | SKILL.md:49 | Docs → этот Skill целиком. |  |
| A-O053 | В ТЕКСТЕ | SKILL.md:49 | чтение и запись по `second-brain-git` |  |
| A-O054 | В ТЕКСТЕ | SKILL.md:49 | поведение (когда, зачем, с чьего согласия) — по этому Skill |  |
| A-O055 | В ТЕКСТЕ | SKILL.md:50 | этот Skill отвечает «что делать, когда и с чьего согласия» |  |
| A-O056 | В ТЕКСТЕ | SKILL.md:50 | «как физически прочитать и записать файл репозитория» |  |
| A-O057 | В ТЕКСТЕ | SKILL.md:50 | `google-drive-docs` — то же для Google Docs и Sheets |  |
| A-O058 | В ТЕКСТЕ | SKILL.md:50 | Механика из них сюда не переписывается — только ссылка на пункт |  |
| A-O059 | В ТЕКСТЕ | SKILL.md:50 | копия механики расходится с источником | Reason generalised. Case address in report table: prompt-craft.md line 98 NO LONGER resolves in working tree (writer В rewrote prompt-craft; lesson line gone); resolves only at baa077c (prompt-craft:98, history.md:19). |
| A-O060 | В ТЕКСТЕ | SKILL.md:51 | колонка «носитель канона» в `registry/projects.md` |  |
| A-O061 | В ТЕКСТЕ | SKILL.md:51 | проекта не существует, не угадывать |  |
| A-O062 | В ТЕКСТЕ | SKILL.md:52 | CORE живёт в repo (`core/`, состав — `core/MANIFEST.md`) |  |
| A-O063 | ПО АДРЕСУ | SKILL.md:52 | ID — `registry/documents.md`, строка CORE | ПОРОГ moved out of text to registry/documents.md line 18 (ID verified). Strict admission says ПОРОГ only В ТЕКСТЕ — but old Р14 п.6 itself forbids registry IDs in Skill; treat as carrier transfer, dispatcher to confirm. |
| A-O064 | В ТЕКСТЕ | SKILL.md:52 | исторический источник, для принятия решений не читается |  |
| A-O065 | В ТЕКСТЕ | SKILL.md:54 | В ответе назван носитель и файл, из которого он прочитан |  |
| A-O066 | В ТЕКСТЕ | SKILL.md:54 | для Docs-проекта ID его INDEX — `registry/documents.md` |  |
| A-O067 | В ТЕКСТЕ | SKILL.md:58 | ## Р6. Захват |  |
| A-O068 | В ТЕКСТЕ | SKILL.md:60 | появилось то, чего ещё нет в каноне проекта |  |
| A-O069 | В ТЕКСТЕ | SKILL.md:62 | В конце того же ответа, не прерывая работу, одним блоком |  |
| A-O070 | В ТЕКСТЕ | SKILL.md:65 | → [<ТЕГ>] <Тип>: <текст> |  |
| A-O071 | В ТЕКСТЕ | SKILL.md:67 | Типы: Задача, Идея, Вопрос, Решение (с датой) |  |
| A-O072 | В ТЕКСТЕ | SKILL.md:67 | Результат (что исправлено → что получилось), Событие |  |
| A-O073 | В ТЕКСТЕ | SKILL.md:68 | Тег — проект, которому факт принадлежит |  |
| A-O074 | В ТЕКСТЕ | SKILL.md:68 | тег [N8N], адрес `projects/n8n/STATE.md` |  |
| A-O075 | В ТЕКСТЕ | SKILL.md:68 | Баг бизнес-воркфлоу другого проекта — тег того проекта |  |
| A-O076 | В ТЕКСТЕ | SKILL.md:68 | `[?] Не классифицировано: <текст>`, не угадывать |  |
| A-O077 | В ТЕКСТЕ | SKILL.md:69 | Баг — сразу предложить записать, не ждать конца сессии. |  |
| A-O078 | В ТЕКСТЕ | SKILL.md:69 | После трёх и более захватов подряд |  |
| A-O079 | В ТЕКСТЕ | SKILL.md:69 | в конце сессии с захватами — предложить !save |  |
| A-O080 | В ТЕКСТЕ | SKILL.md:69 | Пересказ уже записанного захватом не является. |  |
| A-O081 | В ТЕКСТЕ | SKILL.md:70 | мешают результату работы, сессия вправе |  |
| A-O082 | В ТЕКСТЕ | SKILL.md:70 | «Трение: <что мешает> → <чему мешает>» |  |
| A-O083 | В ТЕКСТЕ | SKILL.md:70 | без разбора, без вопроса и без отдельного захвата |  |
| A-O084 | В ТЕКСТЕ | SKILL.md:70 | Это снятый запрет, а не обязанность и не ритуал |  |
| A-O085 | В ТЕКСТЕ | SKILL.md:70 | захватом типа Идея с тегом [SYS] только тогда |  |
| A-O086 | В ТЕКСТЕ | SKILL.md:70 | договорённость Андрея 2026-07-20, подтверждена им 2026-10-11 | Date + record kept in text; У-53 in report table (TRIAGE line 69 verified). |
| A-O087 | В ТЕКСТЕ | SKILL.md:72 | Три случая, которые не ждут !save |  |
| A-O088 | ПО АДРЕСУ | SKILL.md:75 | решение харвеста 2026-10-08 | report table (A_WRITER_REPORT.md) → Edit date 2026-10-09 dropped (history); harvest 2026-10-08 named; history.md:21 at baa077c verified (А44). |
| A-O089 | В ТЕКСТЕ | SKILL.md:73 | — отдельное решение, а не продолжение прежнего |  |
| A-O090 | В ТЕКСТЕ | SKILL.md:73 | Захват типа Решение, вопрос Андрею и запись в журнал решений |  |
| A-O091 | В ТЕКСТЕ | SKILL.md:73 | (`second-brain-git` 11) |  |
| A-O092 | В ТЕКСТЕ | SKILL.md:73 | «по аналогии, владельцу не задано» |  |
| A-O093 | ПО АДРЕСУ | SKILL.md:73 | 1 случай, последний 2026-09-27 — отчёт синтеза, правило Р6.цель | report table (A_WRITER_REPORT.md) → archive-recon LOG Р-13 line 73, Р-14 line 84 verified. Narrative dropped. |
| A-O094 | В ТЕКСТЕ | SKILL.md:74 | регистрируется в `registry/documents.md` тем же шагом, которым создан |  |
| A-O095 | В ТЕКСТЕ | SKILL.md:74 | Без строки в реестре следующая сессия объект не найдёт. |  |
| A-O096 | ПО АДРЕСУ | SKILL.md:74 | 1 случай, последний 2026-09-27 — отчёт синтеза, правило Р6.документ | report table (A_WRITER_REPORT.md) → archive-recon LOG Р-13 line 73 verified. |
| A-O097 | В ТЕКСТЕ | SKILL.md:74 | Право на эту запись — Р13. |  |
| A-O098 | В ТЕКСТЕ | SKILL.md:75 | — захват с тегом соседа |  |
| A-O099 | ОСЛАБЛЕНО | SKILL.md:75 | тем же шагом, на котором узнан, он ложится одной строкой в `STATE.md` | Moment changed «на !save» → «тем же шагом»; «если сосед ведёт раздел — туда» moved to second-brain-git 10.6 (which now says always the section). Declared in writer «Расширено» 3; matches 10.6 but not confirmed by Andrei. Meaning changed → ОСЛАБЛЕНО until Andrei confirms. |
| A-O100 | В ТЕКСТЕ | SKILL.md:75 | Сказанное в чате записью не считается |  |
| A-O101 | В ТЕКСТЕ | SKILL.md:75 | соседняя сессия чат не читает |  |
| A-O102 | В ТЕКСТЕ | SKILL.md:75 | Образец — `meta/DECLARATION_COMMON.md`, раздел 4. |  |
| A-O103 | В ТЕКСТЕ | SKILL.md:77 | Захват виден в том же ответе, где возник |  |
| A-O104 | В ТЕКСТЕ | SKILL.md:77 | Смена цели — запись в журнале названа номером |  |
| A-O105 | В ТЕКСТЕ | SKILL.md:77 | созданный документ — строка в `registry/documents.md` видна обратным |  |
| A-O106 | В ТЕКСТЕ | SKILL.md:81 | ## Р14. Запреты |  |
| A-O107 | В ТЕКСТЕ | SKILL.md:83 | **ТРИГГЕР.** Любое действие. |  |
| A-O108 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History. |
| A-O109 | В ТЕКСТЕ | SKILL.md:85 | 1. Деструктив без подтверждения. |  |
| A-O110 | В ТЕКСТЕ | SKILL.md:85 | «Собираюсь [действие] на [объект]. Это изменит [что]. Подтверждаешь?» |  |
| A-O111 | В ТЕКСТЕ | SKILL.md:85 | Любой объект: воркфлоу, строки Sheets, Drive, repo, >3 нод. |  |
| A-O112 | В ТЕКСТЕ | SKILL.md:86 | 2. Структурные изменения INDEX и мастер-промпта попутно |  |
| A-O113 | В ТЕКСТЕ | SKILL.md:86 | Исключение — критический баг, ломающий систему прямо сейчас. |  |
| A-O114 | В ТЕКСТЕ | SKILL.md:87 | 3. Второй носитель одного документа. Docs или repo — одно. |  |
| A-O115 | В ТЕКСТЕ | SKILL.md:88 | без позиции в `registry/maintenance-queue.md` с датой смерти |  |
| A-O116 | В ТЕКСТЕ | SKILL.md:88 | (очередь читает харвест, Р11) |  |
| A-O117 | В ТЕКСТЕ | SKILL.md:88 | прочую находку — без задачи в `labs/sys/` (Р16) |  |
| A-O118 | В ТЕКСТЕ | SKILL.md:89 | 5. Считать запись выполненной по ответу инструмента (Р15). |  |
| A-O119 | В ТЕКСТЕ | SKILL.md:90 | 6. Хранить в Skill ID и адреса, у которых есть реестр |  |
| A-O120 | В ТЕКСТЕ | SKILL.md:90 | документы Docs — `registry/documents.md` |  |
| A-O121 | В ТЕКСТЕ | SKILL.md:90 | git-канал и repo — `registry/` |  |
| A-O122 | В ТЕКСТЕ | SKILL.md:90 | таблицы Sheets и доменные детали — `n8n-workflow-registry` |  |
| A-O123 | В ТЕКСТЕ | SKILL.md:90 | Три реестра, три класса объектов, пересечений нет. |  |
| A-O124 | В ТЕКСТЕ | SKILL.md:90 | Таблица или документ, созданные сессией, регистрируются |  |
| A-O125 | В ТЕКСТЕ | SKILL.md:90 | Skill `n8n-workflow-registry` сессия не правит |  |
| A-O126 | В ТЕКСТЕ | SKILL.md:94 | ## Р15. Провенанс и верификация — единый стандарт |  |
| A-O127 | В ТЕКСТЕ | SKILL.md:96 | **ТРИГГЕР.** Любое утверждение о состоянии системы; любая запись. |  |
| A-O128 | В ТЕКСТЕ | SKILL.md:101 | ПРОЧИТАНО В ЭТОЙ СЕССИИ (файл), ПРОЧИТАНО ПОСРЕДНИКОМ |  |
| A-O129 | В ТЕКСТЕ | SKILL.md:101 | Четвёртой метки нет; уверенность происхождением не является. |  |
| A-O130 | В ТЕКСТЕ | SKILL.md:101 | Решение цитируется вместе со статусом |  |
| A-O131 | В ТЕКСТЕ | SKILL.md:101 | отметка об отмене часто стоит в хвосте записи |  |
| A-O132 | В ТЕКСТЕ | SKILL.md:118 | берётся из реестра в момент использования, а не из текста задания |  |
| A-O133 | В ТЕКСТЕ | SKILL.md:118 | в задания пишутся правила поведения при неизвестном, а не факты |  |
| A-O134 | В ТЕКСТЕ | SKILL.md:118 | Перед пакетной операцией — манифест реальных объектов |  |
| A-O135 | В ТЕКСТЕ | SKILL.md:101 | Кто читал источник, тот и прав — независимо от роли в наряде |  |
| A-O136 | В ТЕКСТЕ | SKILL.md:101 | Расхождение факта с ожиданием — стоп и вопрос, не тихая правка. |  |
| A-O137 | В ТЕКСТЕ | SKILL.md:107 | **Утверждение о состоянии**: «работает», «выключен», «опубликован» |  |
| A-O138 | В ТЕКСТЕ | SKILL.md:107 | номер исполнения, поле ответа инструмента или строку объекта |  |
| A-O139 | В ТЕКСТЕ | SKILL.md:107 | без него — «Гипотеза (не проверена):» |  |
| A-O140 | ПО АДРЕСУ | SKILL.md:122 | утверждение о состоянии — 2 случая, последний 2026-09-28 | report table (A_WRITER_REPORT.md) → wb-ue LOG Р-39 line 202 (status ОТМЕНЕНО Р-59), Р-53 line 272 verified. |
| A-O141 | В ТЕКСТЕ | SKILL.md:102 | «сделал», «удалил», «внёс» — для сессии ВСПОМНЕНО |  |
| A-O142 | В ТЕКСТЕ | SKILL.md:102 | закрывается только после чтения объекта |  |
| A-O143 | В ТЕКСТЕ | SKILL.md:102 | «по словам Андрея, объект не прочитан» |  |
| A-O144 | ПО АДРЕСУ | SKILL.md:102 | 1 случай, последний 2026-10-01 — отчёт синтеза, правило Р15.слово | report table (A_WRITER_REPORT.md) → git-migration LOG Р-126 line 159 verified; workflow name dropped. |
| A-O145 | В ТЕКСТЕ | SKILL.md:110 | **Условие, записанное раньше**: в задании, в старой записи |  |
| A-O146 | В ТЕКСТЕ | SKILL.md:110 | условие могло устареть, вопрос — быть уже решённым |  |
| A-O147 | В ТЕКСТЕ | SKILL.md:110 | обещание в шапке документа («старые записи уезжают в такой-то архив») |  |
| A-O148 | В ТЕКСТЕ | SKILL.md:110 | перед ссылкой на объект его ищут |  |
| A-O149 | В ТЕКСТЕ | SKILL.md:111 | **Утверждение об отсутствии**: «файла нет», «воркфлоу не существует» |  |
| A-O150 | В ТЕКСТЕ | SKILL.md:111 | в ответе перечислено, где искали |  |
| A-O151 | В ТЕКСТЕ | SKILL.md:114 | воркфлоу — search_workflows или get_workflow_details на инстансе |  |
| A-O152 | В ТЕКСТЕ | SKILL.md:114 | живой Skill в `/mnt/skills/`, файл репозитория |  |
| A-O153 | В ТЕКСТЕ | SKILL.md:114 | решение — оглавление журнала своего и соседнего проекта по словам темы |  |
| A-O154 | В ТЕКСТЕ | SKILL.md:111 | отсутствие в реестре, в CORE или в памяти сессии — это дефект регистрации |  |
| A-O155 | В ТЕКСТЕ | SKILL.md:114 | Поиск документа по просьбе Андрея — Р9. |  |
| A-O156 | ПО АДРЕСУ | SKILL.md:126 | утверждение об отсутствии — 4 случая, последний датированный 2026-07-30 | report table (A_WRITER_REPORT.md) → TRIAGE lines 94 (У-78), 165 (У-144) verified; corpus lines are Docs, не проверяемо в клоне. Detail (M5dqSv2yiklnDXoP, cancelled CORE edit) only at addresses. |
| A-O157 | В ТЕКСТЕ | SKILL.md:112 | правило — references/write-moment.md, читается перед такой записью |  |
| A-O158 | В ТЕКСТЕ | SKILL.md:119 | Запись верифицируется ТОЛЬКО независимым перечитыванием |  |
| A-O159 | В ТЕКСТЕ | SKILL.md:119 | Docs — gdocs-read, счёт вхождений якоря или совпадение текста |  |
| A-O160 | В ТЕКСТЕ | SKILL.md:119 | в среде с клоном `git fetch` и `git hash-object` |  |
| A-O161 | В ТЕКСТЕ | SKILL.md:119 | blob sha записанного равен sha намеренного |  |
| A-O162 | В ТЕКСТЕ | SKILL.md:119 | `success: true`, `occurrencesChanged`, номер исполнения |  |
| A-O163 | В ТЕКСТЕ | SKILL.md:119 | один стандарт для обоих носителей |  |
| A-O164 | В ТЕКСТЕ | SKILL.md:128 | В отчёте о записи названы файл, способ обратного чтения |  |
| A-O165 | В ТЕКСТЕ | SKILL.md:128 | несут способ проверки или слово «Гипотеза» |  |
| A-O166 | В ТЕКСТЕ | SKILL.md:132 | ## Р21. Чтение через посредника |  |
| A-O167 | В ТЕКСТЕ | SKILL.md:134 | нужен ответ на вопрос, а не текст, от справки Skill, архива |  |
| A-O168 | В ТЕКСТЕ | SKILL.md:136 | можно ли сузить объект ДО попадания в контекст |  |
| A-O169 | В ТЕКСТЕ | SKILL.md:137 | Файл, любой — сужает сама сессия по правилу «чем читать» |  |
| A-O170 | В ТЕКСТЕ | SKILL.md:137 | (`second-brain-git` 7.6; в среде с клоном grep и sed) |  |
| A-O171 | В ТЕКСТЕ | SKILL.md:137 | Посредник на файле почти ничего не добавляет |  |
| A-O172 | ПО АДРЕСУ | SKILL.md:137 | Основание: 1 замер, 2026-09-24 — отчёт синтеза, правило Р21.файл | report table (A_WRITER_REPORT.md) → kontext-reduktion LOG Р-25 line 201 verified; 2%/24% numbers only at address. |
| A-O173 | В ТЕКСТЕ | SKILL.md:137 | выигрыш поверх среза съедается проверкой его ответа |  |
| A-O174 | В ТЕКСТЕ | SKILL.md:138 | Ответ инструмента, который приходит целиком и сужению не поддаётся |  |
| A-O175 | В ТЕКСТЕ | SKILL.md:134 | `get_workflow_details` воркфлоу целиком, выдача исполнения грязного |  |
| A-O176 | В ТЕКСТЕ | SKILL.md:138 | Это его единственная ниша |  |
| A-O177 | В ТЕКСТЕ | SKILL.md:138 | выигрыш на таком ответе измерен около 5,7 раза |  |
| A-O178 | В ТЕКСТЕ | SKILL.md:139 | посредником не читаются НИКОГДА |  |
| A-O179 | В ТЕКСТЕ | SKILL.md:139 | Исполнять можно только прочитанное; пересказ правила исполнением |  |
| A-O180 | В ТЕКСТЕ | SKILL.md:141 | Заданием посреднику назначается вопрос, а не файл |  |
| A-O181 | ПО АДРЕСУ | SKILL.md:143 | Основание: 1 замер, 2026-09-25 — отчёт синтеза, правило Р21.адрес | report table (A_WRITER_REPORT.md) → Р-29 line 235 verified; «правка 2026-10-09» dropped (history). |
| A-O182 | В ТЕКСТЕ | SKILL.md:142 | Вопрос не несёт ожидаемого ответа и ожидаемой роли объекта. |  |
| A-O183 | В ТЕКСТЕ | SKILL.md:142 | посредник, которому назвали ответ, ищет доводы за него |  |
| A-O184 | ПО АДРЕСУ | SKILL.md:142 | Основание: 1 случай — отчёт синтеза, правило Р21.подсказка | report table (A_WRITER_REPORT.md) → TRIAGE line 40 (У-22), archivarius LOG lines 40/139 verified; corpus N8N_JOURNAL_2026 line 2896 — Docs, не проверяемо в клоне. Basis line lacks «последний <дата>» (form deviation). |
| A-O185 | В ТЕКСТЕ | SKILL.md:142 | решение Андрея 2026-10-13 — запись Р-39 журнала |  |
| A-O186 | В ТЕКСТЕ | SKILL.md:143 | При каждом факте ответа стоит адрес доказательства |  |
| A-O187 | В ТЕКСТЕ | SKILL.md:143 | имя узла и путь в JSON или цитата до 80 знаков |  |
| A-O188 | В ТЕКСТЕ | SKILL.md:143 | Ничего не нашёл — пишет NOT_FOUND и перечисляет, где искал. |  |
| A-O189 | ПО АДРЕСУ | SKILL.md:143 | Основание: 1 замер, 2026-09-25 — отчёт синтеза, правило Р21.адрес | report table (A_WRITER_REPORT.md) → 7/8 vs 8/8 numbers only at address (Р-29 line 235 verified); generalised reason in text. |
| A-O190 | В ТЕКСТЕ | SKILL.md:144 | Вопросы одному посреднику задаются пакетом. |  |
| A-O191 | В ТЕКСТЕ | SKILL.md:144 | второй вопрос в том же задании стоит примерно десятую часть первого |  |
| A-O192 | В ТЕКСТЕ | SKILL.md:145 | Модель посредника по умолчанию — среднего класса. |  |
| A-O193 | В ТЕКСТЕ | SKILL.md:145 | Самая лёгкая — только для буквального извлечения |  |
| A-O194 | В ТЕКСТЕ | SKILL.md:145 | Имена моделей здесь не пишутся |  |
| A-O195 | В ТЕКСТЕ | SKILL.md:145 | они меняются чаще Skill |  |
| A-O196 | В ТЕКСТЕ | SKILL.md:147 | Расход посредника замеру не подлежит |  |
| A-O197 | В ТЕКСТЕ | SKILL.md:147 | харнесс сообщает его не всегда, а приборы наблюдения |  |
| A-O198 | В ТЕКСТЕ | SKILL.md:150 | Ответ посредника помечается ПРОЧИТАНО ПОСРЕДНИКОМ с именем объекта |  |
| A-O199 | В ТЕКСТЕ | SKILL.md:150 | факт без адреса доказательства и без NOT_FOUND считается не полученным |  |
| A-O200 | В ТЕКСТЕ | SKILL.md:150 | В таком виде он годится, чтобы направить следующий шаг сессии. |  |
| A-O201 | В ТЕКСТЕ | SKILL.md:150 | он не пишется, пока сессия не прочитала источник сама |  |
| A-O202 | В ТЕКСТЕ | SKILL.md:150 | тогда пометка становится ПРОЧИТАНО В ЭТОЙ СЕССИИ |  |
| A-O203 | В ТЕКСТЕ | SKILL.md:150 | Правило «кто читал источник, тот и прав» посредник не отменяет |  |
| A-O204 | В ТЕКСТЕ | write-moment.md:1 | # second-brain-engineer — идентификатор, число или дата в канон |  |
| A-O205 | В ТЕКСТЕ | write-moment.md:3 | Часть Skill second-brain-engineer. |  |
| A-O206 | В ТЕКСТЕ | write-moment.md:3 | Читать: перед записью в канон идентификатора, числа или даты |  |
| A-O207 | В ТЕКСТЕ | write-moment.md:3 | Номера пунктов общие со SKILL.md |  |
| A-O208 | В ТЕКСТЕ | write-moment.md:3 | ссылки на пункты других частей разрешаются по таблице |  |
| A-O209 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History. |
| A-O210 | В ТЕКСТЕ | write-moment.md:5 | ## Р15 (пункт). Идентификатор, число или дата в канон |  |
| A-O211 | В ТЕКСТЕ | write-moment.md:7 | Запись в канон (файл repo, INDEX, реестр, позиция Очереди, журнал) |  |
| A-O212 | В ТЕКСТЕ | write-moment.md:7 | ID, sha, номера исполнения, порога, счёта, размера, даты записи |  |
| A-O213 | СНЯТИЕ ПРЕДЛОЖЕНО | — |  | History. |
| A-O214 | В ТЕКСТЕ | write-moment.md:3 | Закон этого пункта — закон раздела Р15 в SKILL.md | Old «остальной Р15 действует оттуда» now: heading «Р15 (пункт)» + «Закон этого пункта — закон раздела Р15 в SKILL.md» + shared numbering line 3. |
| A-O215 | В ТЕКСТЕ | write-moment.md:13 | выдача объекта или поиска этой сессии — копированием |  |
| A-O216 | В ТЕКСТЕ | write-moment.md:13 | память, перепечатка из другого текста, счёт в уме |  |
| A-O217 | ПО АДРЕСУ | write-moment.md:23 | идентификатор — 1 случай, последний 2026-09-23 | report table (A_WRITER_REPORT.md) → Z-10 projects/n8n-map/PLAN.md lines 28, 234 verified. Old present-tense claim «в registry лежит копия 41 знак» dropped — registry now 44 chars (correct removal). |
| A-O218 | В ТЕКСТЕ | write-moment.md:15 | Дата записи — в журнале, в имени файла, в поле «создан» |  |
| A-O219 | В ТЕКСТЕ | write-moment.md:15 | (время старта исполнения n8n, createdTime ответа Drive) |  |
| A-O220 | В ТЕКСТЕ | write-moment.md:15 | \| память модели \| |  |
| A-O221 | ПО АДРЕСУ | write-moment.md:25 | дата — 2 случая, последний 2026-07-30 | report table (A_WRITER_REPORT.md) → TRIAGE line 61 (У-45) verified; corpus lines Docs. |
| A-O222 | В ТЕКСТЕ | write-moment.md:16 | Число о живом файле или документе, в который пишут и другие |  |
| A-O223 | В ТЕКСТЕ | write-moment.md:16 | и вместе с числом отметка версии этого чтения |  |
| A-O224 | В ТЕКСТЕ | write-moment.md:16 | blob sha для файла репозитория, checkSum ответа gdocs-read |  |
| A-O225 | В ТЕКСТЕ | write-moment.md:20 | задаётся соотношением, которое проверяется на свежем чтении |  |
| A-O226 | В ТЕКСТЕ | write-moment.md:20 | абсолютное число — только база для сравнения |  |
| A-O227 | ПО АДРЕСУ | write-moment.md:26 | число о живом файле — 5 случаев, последний 2026-08-30 | report table (A_WRITER_REPORT.md) → TRIAGE line 91 (У-75) verified. |
| A-O228 | ПО АДРЕСУ | write-moment.md:26 | число о живом файле — 5 случаев, последний 2026-08-30 | report table (A_WRITER_REPORT.md) → TRIAGE line 96 (У-80) verified. |
| A-O229 | ПО АДРЕСУ | write-moment.md:26 | число о живом файле — 5 случаев, последний 2026-08-30 | report table (A_WRITER_REPORT.md) → TRIAGE line 241 (порция Р-22) verified. |

ОСЛАБЛЕНО: A-O022, A-O099. ПОТЕРЯНО: none. Admission question for dispatcher: A-O063 is a ПОРОГ (old Docs CORE ID) that left the text for `registry/documents.md` line 18 — strict admission requires В ТЕКСТЕ, but old Р14 point 6 itself forbids registry IDs in a Skill; accepted as ПО АДРЕСУ pending confirmation.

## 2. Knowledge in the old text missing from my unit table

Re-read both old files sentence by sentence against the table: no uncovered sentence found. Sub-details that exist only inside units and are now only at addresses (correct per new basis form, listed so nothing is silent): workflow name «SYS INDEX Restore from Revision» (Р-126); workflow ID `M5dqSv2yiklnDXoP` and «на ложном опровержении отменена верная правка CORE» (У-78); corpus line numbers JOURNAL_INCIDENTS 113–124, 211–215, WB_REVIEWS_INDEX 1722, SYS_JOURNAL_2026 2611/5781, N8N_JOURNAL_2026 2896 (Google Docs corpora, не проверяемо в клоне; the TRIAGE rows that cite them are verified); measurements 2 % / 24 %, 7 of 8 vs 8 of 8; 2 288 bytes, «21 956 байт ± 2», 141 bytes, приёмка K3.

## 3. Claims beyond the old text NOT declared in the writer's «Расширено»

1. write-moment ПРОВЕРКА: «Рядом с записанным идентификатором, числом или датой назван источник — выдача, чтение или инструмент времени этой сессии». This is a new duty on EVERY ID/number/date written to canon (old text required copying from output, not naming the source beside it). «Расширено» 10 says only «раздел получил ПРОВЕРКУ» — the content of the new duty is not declared. Highest-impact undeclared expansion.
2. write-moment table, column «Что источником не считается»: «счёт в уме» added for IDs/numbers — new, undeclared (minor).
3. SKILL.md line 107, Р15 table, column «Что чтением не считается» for state claims: «прежняя запись о состоянии» — new explicit exclusion; came with the pilot table («Вошло из пакетов»), not in «Расширено».
4. SKILL.md line 98, Р15 ЗАКОН: «Всё, чего сессия не прочитала в самом объекте, — память, пересказ или старая запись, и решение на этом не принимается» — broadens from «claims are tagged» to «no decision without reading the object». Listed under «Вошло из пакетов» (pilot accepted 2026-10-18), not «Расширено» — acceptable if dispatcher confirms the pilot acceptance covers it.
5. SKILL.md line 22: reason «так постоянный слой … не растёт от правил одного вида действия» — new reason, undeclared (minor).
6. SKILL.md line 72: «каждый записывается тем шагом, на котором возник» — the timing generalisation for all three cases; «Расширено» 2 and 3 cover the reason and the neighbour case, but not that the document-registration and goal-change cases now share an explicitly unified moment (substantively already so in old text; minor).
7. SKILL.md line 14: «Skill читается целиком при каждом срабатывании, и каждая строка истории оплачивается в каждой сессии» — new reason; and «кластер переписывается правилом, урок не дописывается» — new rule (from AJ-17 / Andrei decision 2026-10-18; listed in «Вошло», not «Расширено»).

## 4. Leftover narratives, execution numbers, edit history, ИСТОРИЯ ДИАГНОЗА

- No execution numbers, no ИСТОРИЯ ДИАГНОЗА blocks, no case narratives found in either new file.
- `[НОВОЕ 2026-09-07]` paragraph (SKILL.md line 16) — edit-history-flavoured; writer proposes removal («Предлагаю снять» 1). Agree.
- SKILL.md line 148 «Не путать: … отклонили 2026-10-09 …» — dated decision inside a «не путать» line; allowed by `core/R-06a.md` 0.4.1 form, but the date is history; could drop the date.
- Basis-line form deviations: Р21.подсказка (SKILL.md line 142) has no «последний <дата>»; Р6.трение (line 70) and Р21 подсказка name journal record numbers in-Skill (allowed: Andrei's word/decision with place).
- Rule-id naming mismatch: Skill basis lists use descriptive names («правила Р15.<вид>»: «утверждение о состоянии», «причинное объяснение», «число в критерии», «число о живом файле», …) while the report table uses ids Р15.состояние, Р15.причина, Р15.число-критерий, Р15.число-живого-файла. Resolvable by a human, but the contract wants literal lookup — align ids.

## 5. Structure, routing, cross-references

- ТРИГГЕР and ПРОВЕРКА: Р0, Р6, Р15, Р21 (SKILL.md) and the write-moment point — both present. **Р14 has ТРИГГЕР but no ПРОВЕРКА** (same in old text) — contradicts the file's own rule «Нет проверки — блок не закрыт» (line 10).
- Routing table «Что читать дальше»: all 11 files in references/ are named (commands, design, harvest, onboarding, outside, permissions, prompt-craft, save, search, start, write-moment); every named file exists; `meta/PROTOCOL_knowledge-synthesis.md` exists; history.md is no longer named. Section numbers Р0–Р22 each found exactly once as headings (Р15 twice: SKILL.md + write-moment point; Р17 absent in old and new) — preserved.
- Outbound addresses verified existing: `second-brain-git` 7.6 (live SKILL.md:169), 8.1 (references/write.md:122), 10.6 (write.md:235 — says section «От соседнего проекта» always, consistent with new Р6), 11 (write.md:242); `core/R-06a.md` 0.4.1 (line 60, contains the Skill exception «не путать»); prompt-craft «Урок после выдачи» (line 102); `meta/DECLARATION_COMMON.md` раздел 4 (line 34); `meta/PLAN_skill-layers_2026-10-20_v3.md` раздел 2 (line 18); `labs/sys/t-knowledge-synthesis.md` «Решения Андрея 2026-10-18» (37), абзац 2026-10-20 пункт 5 (105); maintenance-queue AH-13 (142), AH-23 (153); `meta/SKILLS_MAP_resolution_2026-10-19.md` разбор 6 (54), разбор 9 (69); permissions.md Р13 paragraph «Правка Skill действует только после перезаливки» (30).
- **Missing target:** `meta/SYNTHESIS_second-brain-engineer_2026-10-20.md` (named in every basis line) does not exist yet.
- **Broken case address in the report table:** Р0.граница → `skills/second-brain-engineer/references/prompt-craft.md` line 98 — in the working tree line 98 is now «1. Два файла: …», the 2026-10-06 lesson line is gone (writer В rewrote prompt-craft). Resolves only at baa077c. Same «only in git history» status for Р6.сосед and Р21.непутать (history.md deleted; baa077c:history.md line 21 verified). The table should cite `baa077c:<path>` explicitly.
- Р15.состояние address wb-ue LOG Р-39 (line 202) has status «ОТМЕНЕНО Р-59» — address exists, but the cited record is cancelled; worth a note in the table.
- Inbound references from other Skills (grep /mnt/skills/plugins): `second-brain-git` write.md:50,84 and delivery.md:95 → design.md пункты 11, 17 (exist, design.md lines 73, 116); migration.md:17 → onboarding Р4 (exists); `second-brain-git` write.md:260 → «Р15 (условие, записанное раньше)» (row exists); «Чтение через посредника» name (kept); «кто читал источник, тот и прав» (kept); naryad «Р14 пункт 4» (kept); `n8n-engineering-manual/references/write.md:47` «ЗАПРЕТ 2» — already stale in old text; writer supplied «было → стало» (correct: запрет 1 of Р14 + Р13). No inbound reference to history.md remains in /mnt/skills/plugins outside this Skill.

## 6. Р21 trigger

- Yes: new ТРИГГЕР (SKILL.md line 134) names the moment «Перед вызовом инструмента, чей ответ нельзя сузить …» with concrete tool kinds and states «Решение принимается до вызова, а не по пришедшему ответу». It fires before the call.
- What can still make a session miss it:
  1. SKILL.md line 114 (Р15, search for absence) prescribes «воркфлоу — search_workflows или get_workflow_details на инстансе» with no pointer to Р21 — a session doing an absence check will call get_workflow_details itself. Suggest «(целиком — через посредника, Р21)».
  2. `n8n-engineering-manual` (live) mentions get_workflow_details 23 times (with second-brain-git) and has no pointer to Р21; a session in n8n work follows the manual, not this Skill's last section. The test failure (Health Monitor task) was exactly this path. Suggest a «было → стало» pointer in the manual (outside group A).
  3. Over-breadth risk: the first sentence makes the trigger unconditional on tool kind; when the session needs the workflow text itself to edit it (Р10 / n8n manual), Р21 now says hand it to a mediator, while the third bullet says rules the session executes are never read via mediator. The edit case (need text, not answer) is not carved out — expect either a conflict or the session ignoring Р21 as inapplicable. Suggest: «… когда нужен ответ на вопрос о воркфлоу, а не его текст для правки».
  4. Placement: Р21 is the last section of a 150-line file, after the long Р15 table; nothing in the description frontmatter or the header mentions it. Minor.
