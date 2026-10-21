# ACCEPTANCE — synthesis of Skill `naryad`, 2026-10-21

Independent acceptor. Read fully: OLD (old_raw/, 6 files), NEW (new/, 6 files), BASIS_A/B/C, PARTICULARS_A/B/C, protocol `meta/PROTOCOL_knowledge-synthesis.md` (Закон, Что такое правило, Чего в Skill не бывает, С5), contract in `projects/knowledge-synthesis/PLAN.md`. Did not read WRITER_REPORT_*, units_*, verdicts_*. Clone c0b3ce3. Live Skills at /mnt/skills/plugins/.

| Claim | Verdict |
|---|---|
| К1 rules/thresholds preserved | ПОДТВЕРЖДЕНО (no loss or weakening found; 4 minor extensions listed as «расширено») |
| К2 no case stories / history | ЧАСТИЧНО (no stories, no execution numbers, header is one line; three edit-history fragments survive inside basis lines) |
| К3 numbering and incoming references | ПОДТВЕРЖДЕНО for § references; one line-number reference from a live lab task breaks (see Находки) |
| К4 pointers to other Skills | ПОДТВЕРЖДЕНО (every pointer checked, all found and say what is claimed) |
| К5 AI-16 narrow; ГДЕ tree unchanged | ПОДТВЕРЖДЕНО |
| К6 no particulars / secrets | ПОДТВЕРЖДЕНО |
| К7 ≥15 basis addresses hold | ПОДТВЕРЖДЕНО (42 addresses checked across BASIS_A/B/C, all hold) |

## К1 — details

Method: sentence-by-sentence comparison OLD→NEW for every file, plus a token script (every number, § address, Latin identifier and «quoted phrase» of OLD searched in NEW; output reviewed — all misses are version numbers, case IDs/line numbers of journals, journal names, «Supersedes/Version/Owner», the English 403 text, and «§5.3»/«§8.9» which in NEW are written «5.3»/«8.9» without §). Modal words compared: «запрещ» 5→7, «никогда» 5→6, «ВСЕГДА» 1→1; «обязан» 12→8 — each of the 4 missing occurrences checked: old issuer «РЕЗУЛЬТАТ В обязано указывать файл» → new issuer.md:25 «поле РЕЗУЛЬТАТ В называет файл, а не «в ответ»» (same force, imperative); old destructive «обязана называть механизм/объект» → new destructive-orders.md:111-114 table column «Обязана»; old «Не обязан знать оснастку» → issuer.md:103 «Оснастку сред знать не обязан». No «желательно/рекомендуется/по возможности» introduced.

Checked present with unchanged force (selection of thresholds): template fields and order (SKILL.md:56-70); голое «git» refused by §6(а) (SKILL.md:76, executor.md:13); «интерфейс n8n»/«браузер Андрея» only on explicit «да», silence ≠ permission (SKILL.md:78); 3.1 four questions, first «да» stops, no default, «ГДЕ: не определено» (SKILL.md:84-98); push dry-run + add repo + НЕ ПРИНЯТ §6(б) (SKILL.md:85); push+Канал split in two orders (SKILL.md:86); 3.1а three questions высший/высокий/средний, none → order rewritten (SKILL.md:104-108); ID Н-ДД.ММ-NN, one dot max, letter on collision, ID first word of every message (SKILL.md:112-133); 3.4 five values, audit = «процедура, посылка, цифры, вход», size refusal = violation (SKILL.md:141-157); Глубина 1, Потолок 5 root orders, children excluded (SKILL.md:161-163); Контролёр rule «даже маршрутом Б» (SKILL.md:171); diff-of-lines acceptance (SKILL.md:181); 3.9 formula «B = N×3 + R … O = S + 3» (issuer.md:79); refusal not executable via route Б (issuer.md:86); passport formula «B = N×3 + R, прогноз T = B × 20 с × 2» (destructive-orders.md:15); ceiling «N ≤ 5 и правимых путей ≤ 1» (destructive-orders.md:46); atomic exception three conditions (destructive-orders.md:60-62); «запись результата: <путь>, N=1» (destructive-orders.md:75); journal line format and STOP-LOSS «m ≥ B/2 при k < N/2» (executor.md:89, 99); refusal (а)–(е) and six response lines (executor.md:13-31); Пересмотр 1–7 verbatim in meaning (revision.md:19-40).

Allowed replacements verified: (a) history/case lines → BASIS addresses (see К7); (b) old issuer.md:49 «Пересмотр: если из 10 шагов…» → new issuer.md:91 + revision.md:42 question 8, condition «m > 2·O» and consequence «на байты по бюджетам second-brain-git 4.5» unchanged; decision `meta/SKILLS_MAP_resolution_2026-10-19.md:64` «### 8. Счётчик «из 10 шагов» … ВЕРЕН Б»; (c) description diff = exactly the AI-5 sentence (`registry/maintenance-queue.md:162`); body brought in tone (SKILL.md:16,18) — per contract.

«Расширено» (new text claims slightly more than OLD; none weakens; for Andrei's list):
1. SKILL.md:169 «Для файлов репозитория непересечение путей гонки не снимает … second-brain-git 8.9» — new sentence (pointer to existing rule of another Skill).
2. destructive-orders.md:60 adds example «4б.5 (задача лаборатории вместе со строкой INDEX.md, references/lab.md)» to the atomic-exception examples (OLD named only 5.3 and 8.9). Example list, condition unchanged.
3. revision.md:12 «Не путать: условие пересмотра в любой части этого Skill, записанное счётчиком … его место — вопрос» — new general rule derived from decision Р-113.
4. issuer.md:82 lists «ограничители (§7)» explicitly among what route Б does not lift (OLD: «не §6–§8» — §7 already inside the range; harmonisation).
Harmonisations, not changes: executor.md:13 голое «git» moved into (а) (OLD stated it in SKILL.md:42); foreman.md:29 and issuer.md:129 «путей > 1, кроме исключения об атомарной записи» (OLD «файлов > 1»; exception already existed in OLD 3.7).

## К2 — details

grep for Н-ДД.ММ-NN in NEW: only format examples Н-08.08-02 (SKILL.md:120-131). No execution numbers, no byte counts of cases, no «ИСТОРИЯ ДИАГНОЗА», no «Введён/Введена». Header SKILL.md:6 «Редакция 2026-10-21.» Edit-history fragments that remain inside basis lines (minor):
- SKILL.md:104 «в живом Skill с 2026-10-20» (date of insertion into the Skill = edit history).
- SKILL.md:36 «внесено решением Г1 харвеста 2026-10-18».
- revision.md:44 «(прежний счётчик «из 10 шагов» в references/issuer.md заменён этим вопросом)».
Suggest dropping these three parentheticals; the addresses alone suffice.

## К3 — details

NEW has 2, 3, 3.1, 3.1а, 3.3, 3.4, 7 «Ограничители», 8 «Приёмка» in SKILL.md; 3.2, 3.5, 3.6, 3.9, 4 «Контракт Руководителя» in issuer.md; 3.7, 3.8 in destructive-orders.md; 5 in foreman.md; 6 with (а)–(е) in executor.md:13-18 (new subsections 6.1–6.6 added, letters kept); «Пересмотр» 1–8 in revision.md. Incoming § references grepped in clone (§3.1, §3.1 вопрос 3 [meta/NARYAD_file-migration.md:19], §3.4, §3.7, §3.9, §6, пункт 6(г), §7, §8) — all resolve to the same meaning. Live Skills: avtopilot/SKILL.md:48 quotes «Андрей — шина, роли между собой не общаются» — exists (SKILL.md:34); second-brain-engineer/references/permissions.md:50 «порядок вывода поля МОДЕЛЬ — naryad» — exists (3.1а); n8n-workflow-passport/SKILL.md:50 «references/issuer.md» — посылка rule exists (issuer.md:162-171); `meta/PROTOCOL_harvest.md:21` reads `skills/naryad/references/revision.md` — exists.

## К4 — details (pointer → live object)

- second-brain-git 9.4(б) → delivery.md:84-90 «(б) Файл собирается из уже существующего текста → скрипт …» ✓
- 9.1 → delivery.md:50-56 dry-run, «not in this session's authorized repository set», add repo ✓
- 7.6 → SKILL.md:169 «ЧЕМ ЧИТАТЬ» (clone, cat) ✓
- 5.5 → write.md:111 «переливной клапан» ✓; пункт 14 → write.md:305 «Отказывать в записи или откладывать запись по причине бюджета чтения или размера файла» ✓
- 4.5 «Правило происхождения текста» → write.md:60 «ПОТОЛКА ЗАПИСИ В БАЙТАХ НЕ СУЩЕСТВУЕТ» ✓; SKILL.md 4.5 + costs.md (budgets) ✓
- 8.9 → delivery.md:30-34 «Гонка за голову ветки»; pair «файл и список» ✓
- 5.3 → rotation.md:21 ✓; 4б.5 → lab.md:49 «одним вызовом Git Commit Files» ✓
- second-brain-engineer Р18 → permissions.md:38 «Калибровка исполнителя» table with высший/высокий/средний ✓
- Р15 пункт 1 → SKILL.md:101 «Кто читал источник, тот и прав — независимо от роли в наряде и класса модели» ✓; Р15 as verification standard → item 5 ✓
- Р14 запрет 4 → SKILL.md:86 «прочую находку — без задачи в labs/sys/ (Р16)» ✓; Р16 → outside.md:5 ✓
- Р21 → SKILL.md:132-, line «Вопрос не несёт ожидаемого ответа и ожидаемой роли объекта» ✓
- avtopilot «Ворота 4. Исполнение — Андрея нет» → avtopilot/SKILL.md:46-48 ✓
- denken раздел 2 «Причина существования» → denken/SKILL.md:22 «Генерация и оценка — разные режимы» ✓
- google-drive-docs references/mcp.md 2.2 правило 3 → mcp.md:58 «ПУСТОЙ РЕЗУЛЬТАТ ЧТЕНИЯ = СТОП» ✓
- n8n-engineering-manual references/roots.md R1a.5 → roots.md:36-41 credentials field «когда поведение сменилось, неизвестно» ✓
- n8n-workflow-passport стадия 1 → SKILL.md:34-50 «Паспорт здесь — заявление, а не доказательство» ✓
- context-handoff — Skill exists ✓

## К5 — details

AI-16: SKILL.md:36 — one rule, pointer «Как работает диспетчер — только в Skill avtopilot, здесь не повторяется»; no subagent/dispatcher mechanics restated. Matches queue text `registry/maintenance-queue.md:164` in meaning. ГДЕ tree SKILL.md:84-98: same four questions, same order, same answers, same caveats, same ОСНОВАНИЕ ГДЕ sample. Only change of a factual sentence: Q2 reason «в Claude Code, где нет Канала» → «где Канала может не быть» (SKILL.md:87) — consistent with Q1 caveat 2 of OLD itself; not a rule change.

## К6 — details

grep NEW for document/workflow IDs (16+ alnum), commit hashes, webhook, e-mail, journal names (PROJECT_LOG_SYS, SYS_JOURNAL, WB_REVIEWS_INDEX, SYS_INDEX…), «Share File», «182», «DO UPDATE» — none. Remaining concrete names are canon addresses (core/R-05.md, labs/sys/t-maintenance-audit.md, meta/prompts/sys.md, registry/maintenance-queue.md) and the repo name lyamin-dot/second-brain-canon (SKILL.md:12, as report location; was in OLD too) — addresses, not object state.

## К7 — details (address → what the line says; all hold)

BASIS_A: t-avtopilot-skill.md:13 «ревизия denken уровня 2 … «Действуй!»»; deklaration-v2/LOG.md:114 Р-21 and :133 Р-24 автопилот 2026-10-17; HARVEST_2026-10-18_answers.md:146 «Г1. Решение»; maintenance-queue.md:32 E-2, :33 E-3, :34 E-4; LOG_ARCHIVE.md:707 Т-67 (Н-10.09-05, Канал unreachable from Claude Code/Cowork, 403); maintenance-queue-archive.md:198 P-4; kontext-reduktion/LOG.md:134 Р-18 and :139 «облачная сессия Claude Code 2026-09-24 весь день вызывала Кан…»; LOG_ARCHIVE.md:632 Т-38; :495 Р-48 2026-09-06; :802 Р-74; :810 Р-75 «голова ушла на ccdf3af»; :489 «прецедент Н-20.08-04»; :1073 «§3.7 введён 2026-08-20»; :1053 Р-94; maintenance-queue-archive.md:450 «Н-24.09-02 … разорвана на 11 физических строк», :456 U-1; delivery.md:60 «проба 2026-09-26 … 9de27d6 … 6fe4c47»; SKILLS_MAP_resolution:85 «### 13. Проба 2026-09-26»; t-git-replace-escape.md:17; maintenance-queue-archive.md:479 AG-10; registry/documents.md:102 PROJECT_LOG_SYS frozen.
BASIS_B: archivarius/LOG.md:76 (2893 РЕЗУЛЬТАТ В); meta/prompts/sys.md:111 «внесено 2026-08-13, по результатам TRIZ-проверки»; maintenance-queue-archive.md:569 «Маршрут шага — добавлено 2026-09-10 (Н-10.09-10)», :630 P-6 ВНЕСЕНО, :29 E-1; archivarius/LOG.md:278 У-74, :167 У-22, :87 (5891), :548 Р-38; TRIAGE.md:90 У-74, :40 У-22, :147 У-126 (182 записи, DO NOTHING/DO UPDATE), :113 Ф2-4; resolution:64 пункт 8; git-migration/LOG.md:70 Р-113; LOG_ARCHIVE.md:340 Т-14 (Н-05.09-01, Н-05.09-04), :511 Т-30 «четыре раза», :206 Т-17, :1009 Т-71.
BASIS_C: maintenance-queue-archive.md:30 E-6, :294 W-1; LOG_ARCHIVE.md:487 Р-47, :1071 Р-96 «Н-17.09-01 отбит верно», :1098 Р-99 Н-17.09-02, :216 Т-19 (один отказ приёма, ЗАМЫСЕЛ); maintenance-queue.md:35 E-5; archivarius/LOG.md:406 У-100, :313 У-90; TRIAGE.md:121 У-100 (2026-08-18), :106 У-90 (2026-07-31); CONTRACT_file-limits.md:8 Н-17.09-02.
All 28 rule ids used in NEW basis lines exist as rows in BASIS_A/B/C (script comparison; reverse direction: 7 BASIS rows are decision-type and are addressed directly in NEW).

## Находки сверх вопроса

1. VERIFIED. Live lab task `labs/sys/t-prompt-blocker-registry.md:9` cites «Skill naryad (`references/issuer.md`, строка 23) уже называет такую ссылку ошибкой». In NEW that text is at issuer.md:50 («Не путать: CORE Р.5 …»); line 23 is now «## 3.5 …». The reference should be changed to «issuer.md, пункт 3.6, строка «Не путать»». (SKILLS_MAP line references will also all go stale — expected, map section 6 is in the contract.)
2. VERIFIED. `meta/SYNTHESIS_naryad_2026-10-21.md` does not exist in clone c0b3ce3; every «отчёт синтеза, правило NAR.…» line in NEW dangles until it is committed (contract Н-5). Must land in main before or with the mirror/zip.
3. VERIFIED. Rule «Каждый шаг — с веткой «если не выполнено»» (issuer.md:147-149) has no «Почему» element (protocol «Что такое правило» requires four). OLD's only reason was the case (six defects, recalled). Hypothesis for a generalized reason: «без ветки шаг, который не выполнился, молча переходит в следующий». Same for «Перегрузка классификации» (issuer.md:57-58) and parts of 3.8.3 — OLD had no reason either, so not a loss.
4. VERIFIED. SKILL.md:18 repeats the description sentence verbatim right after SKILL.md:16 says the same in other words — redundancy, not an error.
5. HYPOTHESIS. destructive-orders.md:6 and :119 cite NAR.3.7.формула as the basis of the part's law and of the ЗАМЫСЕЛ field; OLD's 3.8 field was introduced 2026-09-03 citing the same Н-20.08-04 precedent, so the attribution is correct, but the count «1 случай» for 3.8.2 may under-state (Т-19 2026-09-03 is a refusal by empty ЗАМЫСЕЛ — it is attributed to NAR.6.отказ instead). Not a loss.
6. HYPOTHESIS. «20 с» latency in the passport formula has no measurement in the repo (PARTICULARS_C last row) — kept as threshold, correctly; worth a lab task if Andrei wants the number grounded.

## Re-check К2 (after dispatcher edit)

Verdict: К2 ПОДТВЕРЖДЕНО (was ЧАСТИЧНО).
1. All three pieces are gone. A grep of NEW for «Г1 харвеста», «в живом Skill с» and «заменён этим вопросом» finds nothing.
2. Nothing else changed in those lines; I compared them against my first reading. SKILL.md:36 keeps the rule, the pointer to avtopilot, «решение Андрея 2026-10-13, чат SYS, после ревизии denken уровня 2; 3 случая … NAR.роли.автопилот». SKILL.md:104 keeps «ДА → высший. Основание: решение Андрея 2026-10-18 …, позиция AJ-18». revision.md:42-44 keeps the question, «m > 2·O», the consequence and the address `meta/SKILLS_MAP_resolution_2026-10-19.md`, пункт 8. Line counts did not change (SKILL.md 203, revision.md 44).
3. The moved facts are in BASIS_A, section «Round 3», and their addresses exist in the clone: `meta/HARVEST_2026-10-18_answers.md:146` «Г1. Решение: все, кроме AI-6»; `registry/maintenance-queue.md:207` AJ-18 «ВНЕСЕНО 2026-10-20 — zip naryad залит Андреем»; AJ-7 at line 198; commit f4f4a49 exists and its `skills/naryad/references/issuer.md` contains «из 10 шагов».
