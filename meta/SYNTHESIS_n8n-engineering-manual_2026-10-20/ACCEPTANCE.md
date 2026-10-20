# ACCEPTANCE — synthesis of Skill n8n-engineering-manual, 2026-10-20

Acceptor: independent, judged by objects only (writer/checker reports not read). ROOT = scratchpad/nem. CLONE = /home/claude/second-brain-canon (read-only). Old = ROOT/old, New = ROOT/new.

## Verdicts

| Claim | Verdict |
|---|---|
| C1 no knowledge lost/weakened | CONFIRMED (85 statements sampled, 0 ПОТЕРЯНО; 0 substantive ОСЛАБЛЕНО; 1 deliberate reversal by owner decision; 1 minor softening covered by address) |
| C2 harvest items reflected / excluded | CONFIRMED (all 26 СИНТЕЗ/ВНОСИТСЯ items found; all 4 НЕ В SKILL + 1 НЕ ВНОСИТСЯ absent) |
| C3 no case stories / ИСТОРИЯ / one-line header | CONFIRMED (dated observations survive only inside short «не путать»/«пометка» lines) |
| C4 no particulars; sampled particulars addressed; SERVER_INDEX | PARTLY REFUTED — 3 particulars remain in text (below); 30 sampled removed particulars all have an address; SERVER_INDEX holds all three facts |
| C5 one full statement per mechanism | PARTLY REFUTED — 3 duplicate full statements (below) |
| C6 resolutions applied | CONFIRMED (one Гипотеза on carrier of item 5) |
| C7 numbering anchors | CONFIRMED — check_numbers.py: old 57 / new 57, MISSING [], MOVED FILE [], NEW ONLY [] |

## Refutations

### C4 — particulars still in Skill text
1. Server timezone stays as instance fact: `new/references/engine.md:123` «при таймзоне сервера Europe/Berlin (SKILL.md §1)». SKILL.md §1 no longer states the zone (it now points to n8n-map tz field) — the reference «SKILL.md §1» is dangling. Same in `roots.md:215` «время таймзоны сервера (SKILL.md §1)» (only reference, acceptable) — the engine line is the defect.
2. Concrete value of a concrete workflow: `new/references/templates.md:199` «запасной константой вида `|| 1.95`» (1.95 is the Decision Engine constant; R19 table row 310 already uses the neutral `|| <число>`).
3. Concrete database name: `new/SKILL.md:97` «embedding-модель для `liquimoly_kb` — `voyage-3`». Kept as a declared intentional duplicate (map, section 2) — Гипотеза that this conflicts with owner decision (a); old text had it too.

### C5 — duplicate full statements
1. Probe results of the point-operation form are stated in full twice: `write.md:78` «Проверено: замена кода узла Code сохранила настройки воркфлоу, аутентификацию вебхука…» and `roots.md:50` «Пробами установлено: замена кода узла Code сохранила настройки…»; «Не проверено: узлы Switch и правка узла-вебхука» likewise in both. §2.4 should refer to R1b.0.
2. Autopick mechanism stated in full in `write.md:68` (§2.3 п.4: «берёт самый недавно правленный, а имя… выбор не направляет») and `roots.md:26` (R1a.2). Has (R1a) refs but repeats the mechanism.
3. Berlin→Moscow offset numbers «+1 летом и +2 зимой» in three places: `engine.md:123` (home §4.10.1), `roots.md:216` (R7, with ref to §4.10), `templates.md:214` (T4 качество 8, with ref). Same for 429 Wait ≥60 s: `roots.md:163` (R6.3) and `templates.md:127` (T2.1.3). Minor — referring copies carry numbers.
(Checked and clean: R12/R13/R15 vs §2.1 — §2.1 holds the procedure, R12 points «порядок шагов в §2.1», R13 points secret rule to §2.1; T5 vs R18/R19 — T5.5 items point to R18; R4/A1 — A1 rows point to R4; R6 — T1-C bullets point to R6, except «matchingColumns заданы всегда + приведение типов» `templates.md:71` which restates R6.8 without ref.)

## Гипотезы (beyond claims)
- Carrier of resolution 5 still holds the refuted version: `new/references/roots.md:290` sends the WB case to `n8n-workflow-registry/references/cards-and-declarations.md`, whose CLONE line 38 still says «полная перезапись карточки… его стирает. …вместе с ним Wildberries снимает `needKiz` и `kizMarked`» (the text А that resolution 5 rejects). The NEM text itself is consistent with ВЕРЕН Б; the pointer is safe only after the registry synthesis lands.
- `roots.md:34` «Миграция ключа у многих узлов — запрет в §2.3» narrows wording of the absolute ban (`write.md:72` «не использовать для миграции credential»); the full statement is intact.
- Many BASIS/PARTICULARS addresses point to INCIDENT_LOG.md, which now sits at `skills/n8n-engineering-manual/INCIDENT_LOG.md` in CLONE and leaves the Skill; `{{INCIDENT_LOG_PATH}}` must be filled when the file moves, or these addresses break.
- Old rule «Лечится подавлением повторов одной и той же ошибки в самом алерте» (`old/templates.md:169`) is replaced by the opposite «Ограничитель частоты алертов не строится» (`new/templates.md:158`). Not a loss: it follows owner decision Р-6 п.4 (verified CLONE `projects/n8n/LOG.md:46`).

## C1 evidence — 85 sampled statements (old → new)
Legend: Т = В ТЕКСТЕ (new file:line), А = ПО АДРЕСУ (carrier).

| # | Old (file:line, quote ≤80) | Verdict |
|---|---|---|
| 1 | SKILL:13 «Нумерация R и T — append-only» | Т SKILL:10 |
| 2 | SKILL:15 «Один факт живёт в одном месте» | Т SKILL:12 |
| 3 | SKILL:17 «Фиксированная фраза подтверждением не считается» | Т SKILL:16 |
| 4 | SKILL:23 файл не в таблице не читается | Т SKILL:24 |
| 5 | SKILL:41 два вида доказательства | Т SKILL:42 |
| 6 | SKILL:47 «credentials must be configured manually» — шаблон | Т SKILL:50 |
| 7 | SKILL:48 отсутствие поля credentials не доказывает | Т SKILL:51 |
| 8 | SKILL:49 настройки в коде не применяются | Т SKILL:52 (уточнено «целиком») |
| 9 | SKILL:51 triggerInfo противоречив; проверять active/activeVersionId | Т SKILL:54; Z-8 → A/BASIS A1.2 |
| 10 | SKILL:56 у узла нет параметра — умолчание интерфейса | Т SKILL:59 |
| 11 | SKILL:60 диагностика по факту исполнения приоритетнее | Т SKILL:65 |
| 12 | SKILL:62 тест: обязан пройти + обязан отказать | Т SKILL:67 |
| 13 | SKILL:70–83 таблица A2, 14 строк | Т SKILL:75–88 (все 14 + 1 новая) |
| 14 | SKILL:91 URL duckdns | А registry/projects.md:77 (проверено) |
| 15 | SKILL:92 self-hosted, Docker Compose | А SERVER_INDEX стр.17 (проверено Drive) |
| 16 | SKILL:93 Timezone сервера Europe/Berlin | А n8n-map/PLAN.md:70 (проверено) |
| 17 | SKILL:95 версию снимать с инстанса; правило пишется с версией | Т SKILL:95 |
| 18 | SKILL:97 voyage-3 1024d, не voyage-3-lite | Т SKILL:97 |
| 19 | SKILL:101 egress proxy блокирует; только execute_workflow | Т SKILL:101 |
| 20 | SKILL:103 triggerNodeName + inputs без type; два текста ошибок | Т SKILL:103 |
| 21 | SKILL:104 старая форма inputs.type; payload → status:error | Т SKILL:103 («Не путать») |
| 22 | SKILL:106 executionMode только manual | Т SKILL:105 |
| 23 | SKILL:108 get_execution требует оба параметра | Т SKILL:107 |
| 24 | SKILL:114–117 соглашения именования, raw_key | Т SKILL:115–120 (примеры обезличены; A/PARTICULARS:24) |
| 25 | SKILL:125 PRUNE обязателен «~93MB/день» | Т SKILL:128 без числа; число А A/BASIS:63 |
| 26 | SKILL:126 второго канала верификации нет | Т SKILL:129 |
| 27 | SKILL:127 покрытие errorWorkflow «из 39 … у 26 … у 32» | снято по 3а-7; указатель Т SKILL:130 |
| 28 | SKILL:129 воркфлоу ошибок не ограничивает частоту | Т SKILL:131 |
| 29 | SKILL:130 Drive create_file write-scope | Т SKILL:132 |
| 30 | SKILL:131 расшарить SA, bytesRead:0 | Т SKILL:133 |
| 31 | SKILL:133 $vars не перечисляются | Т SKILL:135 |
| 32 | SKILL:141–151 одиннадцать принципов §9 | Т SKILL:144–154 (все 11) |
| 33 | write:11–15 пять шагов порядка | Т write:14–18 |
| 34 | write:17 вебхук без headerAuth не создаётся | Т write:23 |
| 35 | write:20 HTTP к вебхуку — docker-сервис + httpHeaderAuth | Т write:26 |
| 36 | write:22 открытый только по решению Андрея; граница R15 | Т write:28 |
| 37 | write:24 секрет не через чат/узел/репо | Т write:31 |
| 38 | write:25 минимальное право; 403 «read-only token» | Т write:33 |
| 39 | write:25 второй кабинет — отдельный воркфлоу | Т write:35 |
| 40 | write:27 availableInMCP только на опубликованном | Т write:37 |
| 41 | write:29 обрыв ответа — найти, потом создавать | Т write:39 |
| 42 | write:31 update не публикует; полный тумблер | Т write:21 |
| 43 | write:37–47 пред-полётные пункты 1–7 (с 4а, 4б, 6а, 6б) | Т write:45–55 (все) |
| 44 | write:45 Registry Sync 16 суток бил 404 | А A/BASIS (§2.2.6а) |
| 45 | write:47 «ЗАПРЕТ 2» | исправлено: Т write:55 «Р13 … и Р14, запрет 1» (проверено в CLONE) |
| 46 | write:51–62 пост-полётные 1–6 (3а, 3б, 3в) | Т write:61–70 |
| 47 | write:60 autoAssignedCredentials непустое/пустое | Т write:68 |
| 48 | write:64 запрет миграции credential, cachedResultName | Т write:72 + пометка (решение c) |
| 49 | write:68 цена записи целиком не зависит от размера | Т write:76 |
| 50 | write:70 построчное сравнение при замене кода | Т write:79 |
| 51 | write:72 неизменяемые узлы — скриптом, сверка байт в байт | Т write:81 |
| 52 | write:73 пробный прогон черновиком; оговорка триггера расписания | Т write:82 |
| 53 | write:77 снимать с публикации, не архивировать; NOT_TAKEN | Т write:86–88 |
| 54 | write:78 «деактивировал» проверкой не является | Т write:90 |
| 55 | write:83 копия — реконструкция; Duplicate; сразу активна | Т write:96–98 |
| 56 | engine:21 режим Code-узла; $json берёт первый; .all() падает | Т engine:23–25 |
| 57 | engine:22 ВСЕГДА spread | Т engine:28 |
| 58 | engine:24 regex anyChar | Т engine:32 |
| 59 | engine:25 throw в SplitInBatches | Т engine:34 |
| 60 | engine:26–28 axios, NODE_FUNCTION_ALLOW_BUILTIN, $env | Т engine:36–40 |
| 61 | engine:29 httpRequestWithAuthentication не поддерживается | Т engine:42–43 |
| 62 | engine:31 executeOnce: первый элемент, 5→1, 3→1, не перепроверено на HTTP/Sheets | Т engine:52 |
| 63 | engine:39–44 pairedItem, Multiple matches, pairedItemNoInfo, .first() | Т engine:62–67 |
| 64 | engine:46–48 fan-out последовательно; .to(a).add(source).to(b) | Т engine:71–73 |
| 65 | engine:50 Merge numberOfInputs; off-by-one 1 vs 0; Switch fallback | Т engine:77 |
| 66 | engine:56 двойная сериализация с 2.20.9 | Т engine:83 |
| 67 | engine:57–60 три вида выражения, три отказа | Т engine:84–88 |
| 68 | engine:62–64 токен fx; Autodetect; rate limit на узле | Т engine:90–92 |
| 69 | engine:66 позиция только 1:1; после Merge — по ключу | Т engine:94 |
| 70 | engine:68–70 fullResponse; пустое тело {}; двойная вложенность | Т engine:96–98 |
| 71 | engine:71–74 GitHub sha; поле идентичности; parse_mode; зонд 403 | Т engine:99–106 |
| 72 | engine:76–80 курсор персистентно; полнота; body-курсор | Т engine:112–114 |
| 73 | engine:82 WB rrdid Wait 70с; Ozon paginationCompleteWhen | Т engine:115 общо; А registry SKILL.md:126,152 (проверено) |
| 74 | engine:86 Берлин→МСК +1/+2 | Т engine:123 |
| 75 | engine:88 «Дедлайн WB FBS — 16:00 МСК всегда» | А wb-logistics/LOG.md Р-5/Р-14 (проверено) |
| 76 | engine:92 WB даты ММ-ДД-ГГ | А cards-and-declarations.md:33 (проверено) |
| 77 | engine:95 гонка расписаний | Т engine:127 |
| 78 | engine:101–103 OOM средства; Data Table get | Т engine:129–131 |
| 79 | roots:11 поиск по смыслу сравнения | Т roots:13 |
| 80 | roots:15–17 три формы R1a (переименование рвёт) | Т roots:26–31 (+setNodeCredential по AJ-15) |
| 81 | roots:26–34 потери R1b: settings, retry 3/1s, IF литерал, matchingColumns, связи, auth, webhookId | Т roots:55–68 |
| 82 | roots:37 credentials не теряются | Т roots:70–71 |
| 83 | roots:45–47 R2 тумблер, versionId/activeVersionId, workflow_statistics, черновик/опубликованная | Т roots:84–91 |
| 84 | roots:51 R3 пять причин, Sheets create → 0 items | Т roots:101–106 |
| 85 | roots:55–61 R4: SAVE≠PUBLISH, 200 с ошибкой, ответ вебхука раньше цепочки, neverError/таймаут, два слагаемых цены, файл+скрипт | Т roots:117–137 |
| 86 | roots:65 R5 7 из 8, сверка длины с throw | Т roots:144 |
| 87 | roots:69–98 R6: симптомы, null, квота 60/мин на потребителя, consumer, 59000 мс, шапка, gid, формула, autoMap, тип ключа (5 видов), горизонтальная таблица, жизненный цикл, append, delete «first row is 2», барьер <2, повторное чтение, batchGet | Т roots:154–208 (все) |
| 88 | roots:86 «64 из 182 строк product_model, исполнение 31969» | А B1/BASIS:66 |
| 89 | roots:88 «3 вместо 42 … 12,5 млн ₽» | А B1/BASIS:86 |
| 90 | roots:117 R11: 135 с, 10000 мс умолчание, только заголовки, 5006 мс | Т roots:231–232; числа А B2/BASIS R11.1 |
| 91 | roots:118 Postgres connectionTimeout 30 с; Telegram нет | Т roots:233 |
| 92 | roots:124 «<состояние аутентификации вебхуков на дату — не публикуется, И-7>» | А n8n-map/STATE.md:43 (проверено) |
| 93 | roots:125 отдельный ключ; включать после вызывающего; два смысла Header Auth | Т roots:243–245 |
| 94 | roots:131,134 R13 формы; ключ и домен; Allowed Domains; перебор базы; удаление не отзывает | Т roots:251–256 |
| 95 | roots:138 R14 «уходит на Caddy» | Т «reverse-proxy» roots:261; Caddy А SERVER_INDEX стр.17 (проверено) |
| 96 | roots:143 R15 | Т roots:267 |
| 97 | roots:147–149 R16, 245 items | Т roots:272–274; 245 А B2/BASIS |
| 98 | roots:154–156 R17 (а)(б)(в) | Т roots:280–282 |
| 99 | roots:160–162 R18 механизм, правило, снимок до записи | Т roots:289–292; 457/15004292/№1683 А B2/PARTICULARS:27 |
| 100 | roots:167–174 R19 шесть видов + paramsOk | Т roots:300–310 |
| 101 | roots:181–256 таблица §7 (75 строк) | Т roots:320–402 — все строки; 2 обобщены формулировкой (R18, R19), смысл тот же |
| 102 | templates:22–26 шаг 0, принцип состояния | Т templates:23–28 |
| 103 | templates:31–51 T1-A JSON, T1-B 1–6 | Т templates:30–49 |
| 104 | templates:54–57 T1-E четыре пункта | Т templates:52–55 |
| 105 | templates:61–81 T1-C JSON и 12 обязательных пунктов, 272 строки | Т templates:58–81 |
| 106 | templates:84–87 накопитель — 4 правила | Т templates:84–87 |
| 107 | templates:95–113 T1-D граф, false-ветка, дискриминатор, Filter, детерминированный писатель | Т templates:91–109 |
| 108 | templates:113 открытый вопрос 11_Wait_For_Delete | А C/PARTICULARS:43 → INCIDENT_LOG раздел 4 |
| 109 | templates:123–134 T2 слой 1 JSON, retry по типу, 5 попыток/5000 мс, флаг | Т templates:114–129 |
| 110 | templates:140–143 слой 2 — 4 правила | Т templates:132–135 |
| 111 | templates:150–157 слой 3 | Т templates:140–145 |
| 112 | templates:161–167 слой 4 — 7 пунктов | Т templates:148–157 |
| 113 | templates:169 «Лечится подавлением повторов… в самом алерте» | заменено решением Р-6 п.4 (Т templates:158) — не потеря |
| 114 | templates:175–186 T3 тело, модель, credential | Т templates:165–178 |
| 115 | templates:196–216 гейты 1–6 | Т templates:185–205 |
| 116 | templates:218–223 качество 7, четыре условия | Т templates:207–212 |
| 117 | templates:225–240 качество 8–12 | Т templates:214–229 |
| 118 | templates:246–267 T5: два режима, ворота в коде, не «ручной запуск», не публикуется, 6 пунктов, хэш, итог | Т templates:235–259 |
| 119 | templates:262 «EAEU … нужен NATIONAL» | А deklaration-ozon/LOG.md Т-5/Р-16 (проверено: EAEU ×6) |

ПОТЕРЯНО: none. ОСЛАБЛЕНО: none substantive. Minor softening: `old/roots.md:57` «одна ошибочная карточка в пачке отклоняет всю пачку» → `new/roots.md:121` «может отклонить всю пачку»; definite WB fact is at the address `n8n-workflow-registry/SKILL.md:146` and `cards-and-declarations.md:15` («отклоняет всю склейку») — covered.

## C2 evidence
A: #15 → write:50; #18 → SKILL:130; #20 → write:49; #21 → write:64; #22 → write:80; #25 → SKILL:44; Х-34 → write:92. #1 НЕ ВНОСИТСЯ — no v4.6 line (grep «v4.» none). #23 — overridden by owner decision (b): platform line SKILL:136; server part absent (grep encryptionKey / n8n_n8n_data / home/node — none).
B1: #3 → roots:93; #5 → roots:168; #14 → roots:31; #16 → roots:55; #17 → roots:215; AJ-15 → roots:24–28 and roots:133.
B2: #4 → roots:340; #7 → roots:351; #8 → roots:246; #9 → roots:310; Х-24 → roots:254; Х-32 → roots:293.
C: #2 → engine:46–50; #6 → templates:221; #10 → templates:199; #19 → templates:148; AJ-11 → templates:237; AJ-13 → templates:239; Х-13 → engine:102; Х-42 → templates:255. НЕ В SKILL #11 (Finance Sync), #12 (Canary), #13 (Error Notifier format), #24 (ДД.ММ.ГГГГ) — grep: none in new text.

## C3 evidence
Headers: `Редакция 2026-10-20` one line in SKILL:8, write:3, engine:3, roots:3, templates:3. grep «ИСТОРИЯ» — none. grep 5-digit execution numbers — only 59000/10000/30000 (thresholds). Remaining dated items are «Основание» lines or one-line «Не путать»/«Пометка» (roots:31, 38, 40; write:98) — allowed by protocol «Чего в Skill не бывает».

## C4 evidence
Sampled removed particulars with address present (grep in out/*/BASIS|PARTICULARS; * = also verified in CLONE/Drive): duckdns URL*, Docker Compose*, Caddy*, Europe/Berlin*, CPX32*, 27 webhooks*, deadline 16:00*, rrdid/Wait 70*, ММ-ДД-ГГ*, EAEU*, Р-4 counts 39/52, gFFiBPm1OomOzJOj*, S4rZMUkI21dVu3ML*, DCdm1xOojRKOpn4I, 77211, 21757, 34959, 79035, 74384, qZWrl0MkRnZBipXA, VWyXmCPJevCnbkZT, 7x9wPrugdbseaEp2, IHn3Bmyh1VeHf4Ya, OnEludZYMusvFxTS, EH2JaB8WGa0JsBqs, wWFfPIAfLd7yunU8, 6M9nS9iKQzMdztUs, GDI35U36bBRzKZp5, HH7pDL2VZfU9C9Np, 2KorY7GdncsIs5Ro, Htrj0Kyj7eT5SEhR, Iis5dlRS1GWZqQXD, dEMUvxBGI6JIp4vQ, 93MB, 245, 12,5 млн, 64 из 182, РА05, 457/15004292, артикул 1180, ACEA, Р-126 — all found.
New text grep for 16-char IDs, execution numbers, duckdns, Caddy, CPX32, LM_DECL, Decision Engine, Registry Sync, Error Notifier, Canary — none. Remaining: see Refutations C4.
SERVER_INDEX (Google Doc 1n5WPjZ99H9cwVj3w7FwLsvLZLiabAFIcp8fF5hzq5rY, saved acceptance/SERVER_INDEX.txt):
- encryption key not in backup — line 57 «ключ шифрования n8n лежит только на сервере … и не входит ни в одну копию»; line 864 same — YES.
- Caddy — line 17 «Стек: Docker Compose — n8n, PostgreSQL 16, Caddy, OCR» — YES.
- Docker Compose — lines 17, 370 — YES.

## C6 evidence
1 → write:86 «снимается с публикации … не архивируется»; «Устаревший инструмент снимается с публикации тем же действием». 4 → write:72 «Пометка: не проверено пробой … До пробы … запрет в силе». 5 → roots:289–290 mechanism general, needKiz via CASES кейс 3; «ОКПД не установлено» at B2/BASIS:58 (see Гипотеза on carrier). 3а-5 → roots:163 «Wait не меньше 60 секунд, затем повтор … Пауза 1–2 секунды … остаётся»; templates:127. 3а-6 → write:55 (CLONE: second-brain-engineer SKILL.md:85 Р14 п.1 «>3 нод», permissions.md:28 Р13 «>3 нод»). 3а-7 → no counts in SKILL:130, templates:159, roots:217; pointer to n8n-map field 10 and labs/sys/t-failure-visibility.md. T2.4.8 → templates:158 matches CLONE projects/n8n/LOG.md:46 Р-6 (4) «Ограничение частоты алертов не строим … чинится или выключается в тот же день».
