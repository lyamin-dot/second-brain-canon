meta/ANSWERS_synthesis-questions_2026-10-21/review_SBE.md

# Review SBE (second-brain-engineer synthesis 2026-10-20): L1, L2, Q2, Q3, Q9

Paths. Repo = /root/second-brain-canon (the path /home/claude/second-brain-canon does not exist). Reports = meta/SYNTHESIS_second-brain-engineer_2026-10-20/{A,B,C}_WRITER_REPORT.md. Live = /mnt/skills/plugins/second-brain-engineer/ (SKILL.md = S, references/ = r/). Old text = git commit baa077c.
Method: every "live" claim checked by grep -n / Read on the live files. Observation: the live Skill is already AFTER round 2 AND already contains the Р21 node-count threshold (S:136,141) - report "Ждёт Андрея" item 1 is already decided (Andrei 2026-10-20).

## L1 - "Предлагаю снять" (17 items)

| id | item | verdict | evidence | note |
|---|---|---|---|---|
| A-S1 | rule of the `[НОВОЕ 2026-09-07]` marker (+ marker in Р4 step 0) | KEEP | live S:16; r/onboarding.md:69 | Both still live. Marker means "awaiting Andrei's yes": removing it without his yes silently settles the rule. Remove both on his one-line yes (report item 7). |
| A-S2 | "Назначен при раскладке 2026-10-20", "Файл выделен…", cut references | REMOVE_OK | grep "Назначен при раскладке\|Файл выделен\|нарезк" in live = 0 hits; baa077c; projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md:198 | History only; mechanism is in the rules themselves. |
| A-S3 | header line "Редакция 2026-09-07 … с правками …" | REMOVE_OK | live S:8 has only "Редакция 2026-10-20."; projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md:40 (Andrei 2026-10-18 pt 2: history in headers not entered) | Owner decision exists. |
| B-S1 | history paragraphs in headers of save/harvest/start/commands/search/permissions/outside | REMOVE_OK | grep "Правка 20" in r/ = 0; baa077c | Active parts moved into body (r/save.md:11,28,29; r/outside.md:11). |
| B-S2 | "Назначен при раскладке" at Р13 and Р18 triggers | REMOVE_OK | r/permissions.md:25,40 (no mark); t-knowledge-synthesis.md:198 | History. |
| B-S3 | Р16 "однобуквенные префиксы A–Z исчерпаны 2026-09-24" | REMOVE_OK | still live r/outside.md:14; queue rows are visibly two-letter (registry/maintenance-queue.md:206 AJ-17); numbering rule: second-brain-git references/write.md:179 | Particular of one file (R-a), observable in the object. Still live: needs a removal edit. Optional: one line into queue header first. |
| B-S4 | Р5 precedent TRADING_INDEX with SENTINEL line text | REMOVE_OK | grep TRADING_INDEX live = 0; rule kept r/onboarding.md:105,122; case in SYNTHESIS report line 135 (Р5-1); registry/documents.md:38 | Case moved to address. |
| B-S5 | Р2 list of diverged copies | REMOVE_OK | r/onboarding.md:9 keeps "Признак расхождения…"; report line 134 (Р2-1) | Mechanism survives in Признак. |
| B-S6 | save.md 8a retelling of Р15 | REMOVE_OK | r/save.md:26 (short, points to Р15); S:104,109 hold the rule | Content lives in Р15. |
| C-S1 | T-1 queue-position sentence (PROTOCOL_project-development note) | REMOVE_OK | grep in live = 0; registry/maintenance-queue-archive.md:395 | Executed history. |
| C-S2 | separate PROJECT_LOG_SYS journal proposal | REMOVE_OK | grep = 0; registry/documents.md:102 (ЗАМОРОЖЕН 2026-09-26) | State of one object (R-a). |
| C-S3 | G-1 queue-position sentence in item 6 | REMOVE_OK | grep = 0; registry/maintenance-queue.md:41 | State of a queue position. |
| C-S4 | METHOD_project-design source line (byteLength, checkSum) | REMOVE_OK | grep byteLength = 0; reason kept r/design.md:18 | Origin history; reason survives. |
| C-S5 | C-4 "closes this position" | REMOVE_OK | grep = 0; registry/maintenance-queue-archive.md:379 (СНЯТО) | Executed. |
| C-S6 | lessons journal in prompt-craft.md (5 entries) | REMOVE_OK | each lesson is now a rule: r/prompt-craft.md:62-64 (09-28), :36-38,:91 (09-30), :21,:30 (10-04), :30-34 (10-05), :23 + S:50 (10-06); replaced by :104-106 | Mechanisms preserved; cases at SYNTHESIS report (prompt-* rows). |
| C-S7 | examples WB_LOGISTICS B24→B11, "08:00", T1–T5, Telegram cost format, old Ozon prompt | REMOVE_OK | grep B24\|B11\|08:00\|T1–T5 live = 0; generic rule r/prompt-craft.md:21; old text baa077c:skills/second-brain-engineer/references/prompt-craft.md:16 | Object particulars (R-a). Only address is baa077c (stated by writer C); acceptable. |
| C-S8 | properties of deleted history.md ("no rules here", "numbers shared") | REMOVE_OK | `ls` live r/ has no history.md; C_WRITER_REPORT.md:65-85 maps each record to an address | Property of a deleted file. |

L1 counts: REMOVE_OK 16, KEEP 1.

## L2 - "Расширено" + "Круг 2" additions (49 items)

Ids: A-n = A report "Расширено" item n (11 listed last); A2-n = A "Расширено круга 2"; B-dN = B dash items (круг 2 decisions), B-nN = B numbered 2..8; C-n = C "Расширено".

| id | item | verdict | evidence | note |
|---|---|---|---|---|
| A-1 | Р6 trigger "Любой ответ, в разговоре которого появилось" | ACCEPT | live S:60; basis projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md:209 (retest finding), S:22 | Matches real firing area; scope by letter wider, by intent same. |
| A-2 | Р6 common reason "next session reads canon, not chat" + sign for goal change | ACCEPT | S:72-73; r/outside.md:7 (same mechanism); case Р6.цель archive-recon LOG Р-13/Р-14 | True by construction. |
| A-3 | neighbour fact written "тем же шагом", not at !save | ACCEPT | S:75; second-brain-git references/write.md:235 (10.6 already says it); meta/SKILLS_MAP_resolution_2026-10-19.md:54-57 | Removes a conflict between two Skills. Not Andrei's own word, but not a new duty. |
| A-4 | Р0 reason for 3-Skill border | ACCEPT | S:50; baa077c prompt-craft.md journal entry 2026-10-06 | Reason, case-based. |
| A-5 | Р14 reasons for bans 1,3,4 | NARROW | S:85,87,88 | Ban 1 reason "удалённое… сессия сама не вернёт" is false for git (second-brain-git references/lab.md:54, 4б.6: restore from history). Narrow: «в Docs, Sheets, воркфлоу и Drive сессия удалённое сама не вернёт». |
| A-6 | Р15 ИСТОРИЯ ДИАГНОЗА: in Skill one line "не путать" | ACCEPT | S:118; core/R-06a.md:60 (0.4.1); t-knowledge-synthesis.md:39 (Andrei 2026-10-18 pt 1) | Owner decision. |
| A-7 | Р21 trigger = moment before the call | ACCEPT | S:136; RETEST.md result (report line 42); threshold decided S:141 | Contract of the pass; now also fixed by Andrei's threshold. |
| A-8 | Р21 ПРОВЕРКА: reading the cited evidence address is enough | ACCEPT | S:154; meta/SKILLS_MAP_resolution_2026-10-19.md:69 (разбор 9) | Reading the address = reading the source of that fact. |
| A-9 | Р21 reason for evidence address | ACCEPT | S:147; case Р21.адрес (measure 2026-09-25, report row) | Measured. |
| A-10 | write-moment: ПРОВЕРКА + "Почему" + numbers in criteria | ACCEPT | r/write-moment.md:60,71,81; t-knowledge-synthesis.md:39 (pilot accepted by Andrei); cases wb-ue PLAN.md:67 | Cases and owner acceptance. |
| A-12 | Р21 line "не путать: two-model check not required" | ACCEPT | S:152; Andrei preference 2026-09-03 (memory, R-d) | Negative rule, protects R-d. Could drop "отклонили 2026-10-09" (history) - cosmetic. |
| A-13 | table rows: design.md trigger "подготовить правку Skill", synthesis row | ACCEPT | S:31,39; registry/maintenance-queue.md:206 (AJ-17), :213 (AJ-21) | Queue positions entered 2026-10-20 by owner flow. |
| A-11 | header "Один регламент" reason | ACCEPT | S:12; baa077c history 2026-10-06 | Case-based reason. |
| A2-1 | Р14 ПРОВЕРКА added | ACCEPT | S:92, S:10 (format law) | Shows proof of an existing duty; not a new monitor. Last clause duplicates Р15. |
| A2-2 | old CORE ID replaced by pointer | ACCEPT | S:52; registry/documents.md:18 | R-a / Р14.6 compliant. |
| A2-3 | proposal "name source next to each recorded number" (declared NOT entered) | NARROW | r/write-moment.md:67 - it IS partly entered: "рядом называется чтение, из которого число взято" | Report and text disagree (R-d). Narrow row to: «чтение объекта до того, как критерий записан». |
| A2-4 | "счёт в уме" not a source | ACCEPT | r/write-moment.md:66-67 | From pilot accepted by Andrei (t-knowledge-synthesis.md:39). |
| A2-5 | write-moment "Почему" paragraph | ACCEPT | r/write-moment.md:71 with cases :76-79 | Each clause tied to a case row. |
| A2-6 | reason for ratio criteria | ACCEPT | r/write-moment.md:73; old text baa077c write-moment.md (K3 case) | Was in old text as example. |
| A2-7 | Р15 "прежняя запись о состоянии" + ЗАКОН | ACCEPT | S:100,109; t-knowledge-synthesis.md:39 | Pilot accepted "включая пять пунктов расширено". |
| A2-8 | header reasons ("history paid every session", "rewrite, don't append") | ACCEPT | S:14,22; t-knowledge-synthesis.md:37-46; PROTOCOL_knowledge-synthesis.md:34 | Andrei decisions 2026-10-18/20. |
| A2-9 | Р6 "each recorded at the step it arose" for all three | ACCEPT | S:72 | Depends on A-3 (accepted). |
| A2-10 | Р21 exception: workflow to be changed is read by session itself; Р15 pointer | ACCEPT | S:116,142,143; r/permissions.md:10 | Follows from S:142 "rules the session executes are never read via intermediary"; live wording is narrower than report. |
| A2-11 | save.md route row "повтор бага (Р12)" | ACCEPT | S:32; r/save.md:46 | Routing only; rule existed (AI-17). |
| B-d1 | Р16: handoff WRITES block in INDEX/STATE | ACCEPT | r/outside.md:11, :70; skill context-handoff description (transfer via Зона А INDEX); SKILLS_MAP_resolution:разбор 3 | Meaning reversed vs old, but true of the tool. |
| B-d2 | Р16: queue number from fresh read, pointer to 8.3 | ACCEPT | r/outside.md:14; second-brain-git references/write.md:179 | Pointer, no mechanics copied (Р0). |
| B-d3 | Р4 step 3 ID replaced by registry pointer | ACCEPT | r/onboarding.md:72; registry/documents.md:72 | R-a / Р14.6. |
| B-d4 | permissions "ЗАКОН ФАЙЛА" | NARROW | r/permissions.md:5 | First sentence reads as a licence ("acts alone where rollback is possible") that contradicts Р10 (revertible edits still need "да", :10-11) and 4б.6. Narrow to: «"Да" стоит там, где откат невозможен, дорог или задевает чужую работу. Закон объясняет Р10 и Р13, не отменяет их строк.» |
| B-d5 | Р18: first-match, "проверка чужого суждения" = high, Почему, no model names | ACCEPT | r/permissions.md:41-52; naryad SKILL.md:55 (same classification); :51 Andrei 2026-10-18 | Echoes naryad; note two homes (naryad SKILL.md:104 points here). |
| B-n2 | Р18 row "самый лёгкий — only literal extraction" | ACCEPT | r/permissions.md:48; S:149 | Copy of Р21 rule; duplicate home, harmless. |
| B-n3 | Р18 ПРОВЕРКА: class named in the order | ACCEPT | r/permissions.md:52; naryad references/executor.md:7 | Naryad already checks MODEL answer. |
| B-n4 | Р12 trigger "повтор бага" + ПРОВЕРКА with four fields | NARROW | r/save.md:46,51,53 vs r/onboarding.md:118 (3 fields) | Trigger ok. ПРОВЕРКА collides with Docs template - see Q9; narrow ПРОВЕРКА until template fixed. |
| B-n5 | Р9 ПРОВЕРКА: list where searched | ACCEPT | r/search.md:17; S:113 | Mirror of Р15 absence row. |
| B-n6 | new ПРОВЕРКА in Р5 and Р2 | ACCEPT | r/onboarding.md:47,123; S:10 | Proof of existing steps; Р1 depends on SENTINEL. |
| B-n7 | save.md step 0 (read MANIFEST event-row) | ACCEPT | r/save.md:11; meta/SKILLS_MAP_resolution_2026-10-19.md:111 (разбор 3а-4) | Gap fix. |
| B-n8 | Р4 step 0 "Почему repo по умолчанию", Ф6 pointer | ACCEPT | r/onboarding.md:69; second-brain-git SKILL.md:48 (И-1); projects/git-migration/PLAN.md:34 | Pointer + reason. |
| C-1 | 14д applies to any acceptance with a separate acceptor | ACCEPT | r/design.md:104; meta/HARVEST_2026-10-18_answers.md:196 (Ж2, Andrei's own answer); HARVEST_2026-10-18_edits/second-brain-engineer.md:176 | Owner word. |
| C-2 | lessons journal replaced by "case to project log, rule by synthesis" | ACCEPT | r/prompt-craft.md:104-106; meta/PROTOCOL_knowledge-synthesis.md:34; t-knowledge-synthesis.md:37-40 | Andrei law "rule instead of story". |
| C-3 | Р22 gets ТРИГГЕР/ПРОВЕРКА | ACCEPT | r/prompt-craft.md:13,108; S:29 | Format law. |
| C-4 | Р20 ПРОВЕРКА: no object particulars in Skill edits | ACCEPT | r/design.md:143; t-knowledge-synthesis.md:179 | Andrei 2026-10-20. Note live Skill still has some (r/permissions.md:31 wb_inbox / oz_inbox). |
| C-5 | "each Skill in its own style" | ACCEPT | r/design.md:135; Andrei preference 2026-09-17 (memory preferences) | Owner preference. |
| C-6 | prompt-craft 1.4: read carrier rule before advice | ACCEPT | r/prompt-craft.md:36-38; baa077c lesson 2026-09-30 | Case-based. |
| C-7 | Р20 ПРОВЕРКА names SKILLS_MAP, not harvest | ACCEPT | r/design.md:143; registry/maintenance-queue.md:206 (AJ-17 pt 2, "решение Андрея 2026-10-18") | Old check was never run. |
| C-8 | Р20 trigger includes "готовится правка Skill" | ACCEPT | r/design.md:128; registry/maintenance-queue.md:213 (AJ-21) | Queue/owner flow. |
| C-9 | Р20 new item "Skill holds instructions for all" | ACCEPT | r/design.md:136-141; t-knowledge-synthesis.md:179 | Andrei 2026-10-20 = R-a itself. |
| C-10 | design 14г full (acceptance questions not by executor; separate acceptor for phase/project) | ACCEPT | r/design.md:99-101; 4 projects (report row design-14г); meta/HARVEST_2026-10-18_answers.md:46 | Cases exist; boundary was set by the session, cheaper than "any". |
| C-11 | writer-added "Почему"/"Признак" lines in design (pts 4,7,8,9,11,12,15) | ACCEPT | r/design.md:43,55,59,64,75,83,108; S:121 (tool fields are signals) | Mechanisms true by construction. |
| C-12 | prompt-craft 1.1: get all parts of instructions first | ACCEPT | r/prompt-craft.md:30; baa077c lesson 2026-10-04 | Case-based. |
| C-13 | fallback "or session report if no project log" | NARROW | r/prompt-craft.md:104; r/outside.md:7 (chat/report is not canon) | A report is not canon. Narrow: «если журнала проекта нет — задача в labs/sys/ (Р16)». |

L2 counts: ACCEPT 44, NARROW 5 (A-5, A2-3, B-d4, B-n4, C-13), RETURN 0, OWNER 0. Total 49.

## Q2 - "Реши сам" (A4(a)): one task or standing?

Facts.
- What live Skill says (form б): r/permissions.md:15 - "в этой задаче поручил… в пределах этой задачи… обратимые правки… необратимые оставляет Андрею и перечисляет в отчёте; поручение не переносится на другие задачи и сессии. Почему так узко: постоянное снятие «да» убрало бы защиту…". Basis :17. Р13 line :28 mentions the exception. ПРОВЕРКА :18 has only two branches (chat "да" or recorded package) - no branch for "реши сам".
- B writer proposed (B_WRITER_REPORT.md:83-84, items 1 and 1a): ask whether standing; and RETURN of three things removed in round 2: (i) examples reversible (unpublish, edit with saved copy) vs irreversible (delete workflow/data); (ii) third phrase "если сомневаешься - прими решение сам"; (iii) third ПРОВЕРКА branch (words of the mandate + log address named, irreversible listed).
- Recorded owner statements (all inside a task): projects/n8n-map/LOG.md:8-36 (2026-09-24 «реши сам /denken», plan R-1..R-4); projects/archivarius/LOG.md:431 (2026-10-11 «Реши сам»); projects/n8n/LOG.md:48 (2026-10-17 «Реши самостоятельно все открытые вопросы /avtopilot. Если нужно согласование, то все равно прими решение сам. А потом уведоми меня и объясни почему так сделал»); projects/deklaration-v2/LOG.md:136-137 (Р-24, «Действуй максимально автономно. Если сомневаешься, прими решение сам, но уведоми меня»; границы 2026-10-13 «на WB ничего без отдельного подтверждения» не сдвигаются); 10 files labs/ozon-ue/t-*.md "Решения 2026-10-17 (… «реши сам все открытые вопросы, потом объясни»)"; projects/wb-ue/LOG.md:384 (Р-69). meta/HARVEST_2026-10-18.md:75 calls the 10-17 phrase "решение Андрея" and asks the (a) question.
- Nobody answered (a): meta/HARVEST_2026-10-18_answers.md:35-36 is the SESSION's reading ("(а) — за Андреем, моё прочтение… на задачу, а не постоянное"); part Ж (Andrei's own answers, :190+) has nothing on А4. Report item 2 still lists it open.
Recommendation: answer "one task (b)". No recorded statement supports "standing"; every grant was tied to a named task (the broadest, 2026-10-17, "все открытые вопросы" across projects in one chat, still bounded by the chat/task), and standing consent would remove the workflow-overwrite guard (r/permissions.md:11, labs/sys/t-n8n-workflow-race.md). Take the returned items (i) and (iii) as ACCEPT (examples come from HARVEST_2026-10-18.md:75 and G3.md:51; without the branch the ПРОВЕРКА cannot be satisfied under a "реши сам" task), and (ii) as trigger words only (Andrei's quote n8n/LOG.md:48). Ask Andrei one line: "«Реши сам» действует только в той задаче, где ты его сказал - верно?"

## Q3 - closing a lab task without Andrei's "yes" when the removal condition is verified (AJ-19 proposal)

Facts.
- Live now: closure = delete task file + INDEX row in one call, after "да" (r/permissions.md:28; r/save.md:16; second-brain-git lab.md 4б.5/4б.6:49,54).
- AJ-19 proposal text: registry/maintenance-queue.md:211; B_WRITER_REPORT.md:85 (item 2). Not entered.
- Cases where waiting for "yes" left a verified-closed task open: 1 clear - labs/sys/INDEX.md:20 `t-failure-visibility`: "открытых пунктов нет, снять по слову Андрея"; condition verified by object 2026-10-17 (execution 81691; labs/sys/t-failure-visibility.md:65), row still open 2026-10-21 (INDEX last commit 2026-10-21). Cost: a stale row for 4+ days, no lost work.
- Not cases: INDEX.md:31 `t-gsheets-credential-rejected` "ждёт решения Андрея и переподключения ключа" (needs Andrei's hands, and it is a label, not closure); INDEX.md:32 (publish by "да" - not a closure); labs/sys/t-unmerged-claude-branches.md:43 (grep hit on a different phrase).
- Cases where waiting cost work: 0 recorded (grep of labs/ for "снять по слову Андрея|ждёт решения Андрея" gives only the above).
- Context: 27 lab task files have been deleted in git history (git log --diff-filter=D on labs/sys/t-*.md), e.g. 0173c22 (five tasks closed 2026-10-16 "по проверке объекта"), b5acb3a, a5b496d - closure already happens routinely under Andrei's presence/mandates; whether each had an explicit "да" is not recorded.
- Side finding: Р14.1 reason (S:85) "сессия сама не вернёт" conflicts with 4б.6 (restore from history) - see A-5.
Recommendation: NO for now (threshold in the report: second case; count = 1 with zero lost work). Re-open at the second case or if Andrei says he does not want to confirm routine closures; if reopened, use the narrow AJ-19 form (condition written in the task file AND verified in this session by object AND delete is one git commit). Meanwhile fix A-5 wording so the two rules do not contradict each other.

## Q9 - second-time rule (Р12): four fields vs three; where the class goes at lab-task closure

Contradiction, precisely.
1. Rule: r/save.md:51 requires a class record of FOUR fields (symptom, class cause, preventive, moment); ПРОВЕРКА r/save.md:53 checks "все четыре поля". For a Docs project the carrier is "НАКОПЛЕННЫЙ ОПЫТ → Ошибки и решения", whose template line is `[YYYY-MM-DD] [симптом] → [решение]` (r/onboarding.md:118) = date, symptom, solution: no class cause, no preventive, no moment. Following the template cannot pass the ПРОВЕРКА.
2. Lab carrier: r/save.md:51 says "файл задачи, в которой ошибка повторилась" (or new lab task if class is wider). But the lab task file is deleted on closure (second-brain-git lab.md 4б.6:54; r/save.md:16) and the file has only roles "суть, следующий шаг, условие снятия, ссылки" (lab.md:24-25, no third role). So a preventive recorded there disappears with the closure and survives only in git history; and the "moment when the preventive must fire" has no home after closure.
3. Heading: "Р12. Гигиена Зоны А" (r/save.md:44) names Docs, while the second-time rule covers three carriers.
Minimal resolution (2 edits, no new mechanism):
(a) r/onboarding.md:118 template becomes `[YYYY-MM-DD] [симптом] → [решение]; класс: [причина класса]; превентив: [что]; срабатывает: [момент]` - four fields live in the one existing line, ПРОВЕРКА stays.
(b) r/save.md:51 lab clause: «лаборатория — файл задачи, в которой ошибка повторилась; при закрытии этой задачи превентив переносится до удаления файла: в правило (PLAN.md проекта-летописи, Skill через позицию очереди по Р16) или в новую задачу лаборатории, если класс остаётся открытым». Closure then cannot lose the class. Heading left unchanged (number and name are referenced).

Findings for the owner outside the lists: r/outside.md:14 still carries B-S3 text; r/permissions.md:31 (wb_inbox / oz_inbox), r/commands.md N8N lines and S:90 (Р14.6 "доменные детали - n8n-workflow-registry") are particulars against R-a (report items 8, B-5) - not decided here.
