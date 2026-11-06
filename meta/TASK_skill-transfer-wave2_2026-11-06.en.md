# TASK skill-transfer wave2 (agent copy). Canon = RU file meta/TASK_skill-transfer-wave2_2026-11-06.md; on conflict RU wins.

GOAL: 8 skills -> short form per meta/CRITERIA_skill-transfer.md (read fully first). Each rule duplicated across skills gets exactly 1 home. No Stop/Trap rule lost between skills. Output: 8 zips + 1 LOG entry.

SCOPE:
- wave1 (Opus each): second-brain-engineer 277KB | second-brain-git 243KB | naryad 107KB
- wave2 (start only after wave1 LEDGER closed + headings frozen): avtopilot+denken | context-handoff | n8n-workflow-passport+n8n-workflow-registry
- OUT: apps-script-sheets, n8n-engineering-manual, google-drive-docs (done, frozen; do not edit); triz, triz-skill (3rd party); clasp-apps-script (not live; ask Andrei, do not transfer)

MODE: lead + <=3 agents at once. agent teams if available, else subagents. Decision exists ONLY when written in LEDGER; messages are not decisions.

LEDGER meta/TRANSFER_wave2/LEDGER.md, row: |archive addr (skill,file,heading)|CRITERIA type|short wording|home (skill,section)|proposed by|status|
status: proposed -> taken-by-home (only home agent sets, after rule is in its new text) | dispute -> lead decides or ask Andrei.
HOME RULE: home = skill loaded at the moment of the action the rule governs (repo file write -> second-brain-git; when/whose consent -> second-brain-engineer; naryad fields -> naryad). Others get 1 line "Skill X, раздел «Y»".
NEVER drop a rule from own skill "because other will take it" until LEDGER says taken-by-home.

PER SKILL:
1 lead: diff -rq skills/<n> /mnt/skills/plugins/<n>. Known: avtopilot mirror ahead of live (unuploaded edit Р-44) -> transfer mirror version, report it.
2 CRITERIA step1: archive skills/_v1/<n>/ + header line "Архив до переноса 2026-11-06…".
3 CRITERIA step2: markup + new skill + skills/_v1/<n>/TRANSFER.md + LEDGER rows for foreign-home rules.
4 description += exact RU phrase (Р-46): «Загружать сразу, до первого вызова инструмента, и тогда, когда задача — только план, разбор или вопрос без правки: пункт плана «загрузить Skill» загрузку не заменяет.» len<=1024 chars, yaml check per second-brain-git references/skill-edit.md step4.
5 CRITERIA step3: lead merges RED "?" items of whole wave -> Andrei, <=3 questions at a time, plain words, consequences of yes/no.
6 CRITERIA step4 EXTENDED: independent agent (not a transferer) scans ALL wave archives for Stop + F-trap phrases missing from ANY new skill; script: every "Skill X, раздел «Y»" in all new skills (incl. 3 done) resolves to heading Y in new X.
7 CRITERIA step5: SKIP (Р-47).
8 CRITERIA step6: 1 zip per skill per skill-edit.md step4; state avtopilot zip supersedes Р-44 zip.

GIT: agents write only own skills/<n>/, skills/_v1/<n>/, LEDGER rows. Only lead commits+pushes main; after each batch git ls-remote origin main + git status; agent commit/push -> stop+revert (avtopilot gate4).

DONE WHEN: 8 new skills + 8 TRANSFER.md; LEDGER no open proposed/dispute; step6 zero missing + zero broken links; 8 zips delivered with list of older zips not to upload; LOG entry projects/kontext-reduktion/LOG.md per second-brain-git references/log-form.md (per-skill numbers, tokens from agent reports).

STOP: upload only by Andrei; no zip before step6 passes; size unlimited, shrinking is not a goal; report token spend after wave1 before wave2 (pilot ~1.3M/skill; expect 8-15M total).
