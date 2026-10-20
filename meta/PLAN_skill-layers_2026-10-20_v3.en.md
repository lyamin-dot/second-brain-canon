meta/PLAN_skill-layers_2026-10-20_v3.en.md

# Skill layers & harvest-edit valuation — plan v3 (agent digest, EN)

Human version with reasoning: meta/PLAN_skill-layers_2026-10-20_v3.md. This file is the compact copy for an executing session. Supersedes "plan after review" sections of meta/PLAN_skill-bytes_2026-10-20.md and meta/PLAN_skill-reading-cost_2026-10-20_v2.md; their measurements (D1–D9) stay valid.

## Decisions (Andrei, 2026-10-20)
- ACCEPTED: layer of a Skill section = its TRIGGER line (rule below); layout = pure script move, before synthesis; lever order: second-brain-engineer/SKILL.md → second-brain-git/references/write.md → Skill descriptions.
- REJECTED: any size ceiling with displacement (pair approval or zip gate). Reason: the writing model has no competence to displace; agents fear deletion. Growth control = periodic synthesis session (meta/PROTOCOL_knowledge-synthesis.md), removal only by Andrei via "propose to remove" list. Agent never displaces/deletes.

## Rule: layer by TRIGGER
- TRIGGER names a concrete event/action (session start, !save, n8n workflow change, work outside Claude Project, heavy-object answer, find document) → references/<action>.md + row in "What to read next".
- TRIGGER contains one of three exact phrases "любое действие" / "любое утверждение" / "любая запись" ("любое изменение воркфлоу" in Р10 is NOT one of them), or no TRIGGER line that cannot be given one → SKILL.md (constant layer). Script = check of the table below, not the source of layout.
- New rule must name its trigger; trigger decides file. Rule without trigger does not enter the Skill.
- Applies to TRIGGER–ACTION–CHECK skills. second-brain-git uses its header table as trigger and is already split; only И-7 case list (~1.5 KB) → one basis line at next edit. No separate step.

Layout of second-brain-engineer (live file 48 098 B): CONSTANT = header+table 5021, Р0 1831, Р6 5450, Р14 1860, Р15 10034 minus two write-moment items (3006 + 699; they get the narrower trigger "moment of writing an ID/number/date into canon and read-back of the written") ≈ 20.5 KB. BY-ACTION = Р1 4086 (start), Р8 3828 (commands), Р9 1830 (search), Р10 1372 + Р13 3981 + Р18 357 (permissions, one file), Р16 3185 (outside), Р21 5251 (intermediary), Р15 write-moment items. Sections without TRIGGER get one in the same commit, marked "assigned at layout 2026-10-20".

## Harvest-edit valuation (next session starts here)
Objects: open queue positions targeting Skills — read registry/maintenance-queue.md fresh (expected: AJ-1…AJ-10 packets in meta/HARVEST_2026-10-18_edits/; AJ-11…AJ-20, where AJ-14 = fifteen lessons in meta/HARVEST_2026-10-18_reports/LESSONS_WAITING_CANDIDATES.md; AI-5, AI-6, AI-23, AI-25…AI-28).
Per edit, questions Q0–Q5 in order; first "yes" gives verdict. DONE 2026-10-20: meta/HARVEST_2026-10-18_verdicts.md.
- Q0 (Andrei 2026-10-20, asked first) edit describes state or specifics of a concrete project, sheet/book, workflow, server or marketplace cabinet (can change or be cancelled any minute)? → NOT_IN_SKILL; name the carrier (project/lab canon, passport, registry/, meta/CASES_*.md), check the fact is there, else move it. Platform/tool property true for any instance (n8n engine, Sheets, Telegram, git) is not specifics → go on. Rule also in meta/PROTOCOL_knowledge-synthesis.md «Чего в Skill не бывает».
- Q1 edit only adds history (header history line, "entered on <date>", case story without new rule)? → NOT_ENTERED (history; address exists). Basis: Andrei decision 2 of 2026-10-18.
- Q2 fixes a fact that a session violated after reading the item (text does not hold; e.g. \uXXXX)? → TO_CODE (workflow/script task, needs Andrei "yes"); Skill gets one line "device: …", no paragraph.
- Q3 mechanism has a cluster in the Skill (meta/SKILLS_MAP.md or phrase grep over catalog)? → SYNTH_CLUSTER <name>; edit becomes a unit in step С3 table; new text's layer by trigger.
- Q4 no cluster, new mechanism, basis = 2 independent cases, or 1 with data loss, or Andrei's word? → ENTER_IN <file by trigger>, four-element rule form.
- Q5 none → ASK_ANDREI (both texts if contradiction; one text if basis is a single case and Andrei has not spoken).
Output: meta/HARVEST_2026-10-18_verdicts.md — table: position | edit | deciding question | verdict | file or cluster | basis. Queue statuses per second-brain-git 10.5: NOT_ENTERED → СНЯТА <date>, причина «история»; SYNTH_CLUSTER → ЖДЁТ синтеза <Skill>; others unchanged until entered. Only Q5 rows and "propose to remove" go to Andrei.
Heavy reading of *.json packets → one mid-class subagent per 2–3 skills, batched questions, evidence addresses required, NOT_FOUND allowed.

## Steps
0. DONE (this session): this plan (RU+EN); protocol gets new step С4а (trigger→file) after С4; "when synthesis is mandatory" links valuation procedure; task labs/sys/t-knowledge-synthesis.md updated; INDEX row reduced to one line.
1. Valuation (new SYS chat) → verdicts file + queue statuses; Andrei gets Q5 rows only; heavy *.json reading → mid-class subagent, batched questions with evidence addresses.
2. Layout of second-brain-engineer by script (session with open push): commit mirror skills/second-brain-engineer/ + zip. Acceptance by script: each non-empty source line exactly once in result files; section numbers unchanged; new table rows present.
3. Andrei uploads zip. Check: live snapshot == mirror both ways (second-brain-git 2.6).
4. Re-test: 5 tasks of test 1 + 4 tasks hitting moved sections (!save; n8n edit Р10/Р13; "where is document" Р9; intermediary Р21). Pass: 0 violations; SKILL.md load < 16 542 tokens. Fail → move violated section back to SKILL.md with trigger "any action"; rest stays.
5. Synthesis of second-brain-engineer on laid-out files with step-1 verdicts (avtopilot, protocol С1–С7); every rule carries trigger+file.
6. write.md: steps 2–4 by v1 split draft (general write mechanics; Skill edit+mirror; log form; !save with PLAN/STATE); delete table row "several writes in a row" (rule lives in 8.6).
7. Descriptions: only load reasons stay; rules/exceptions move to body; route check 5 should-trigger + 5 should-not per changed Skill, before==after.
8. Out of frame, one line: SYS master prompt duplicates Р1 and out-of-frame finding rule (~12 KB per SYS session); same mechanism later, on Andrei's word.

## Falsifiers
- Re-test violation of a moved rule → trigger was narrower than real scope; fix = return section, not drop rule.
- Constant layer larger after two synthesis passes than before layout → ceiling question returns to Andrei with that number.
- >50 % Q5 verdicts → questions badly posed; rewrite questions, do not reintroduce importance judgment.
