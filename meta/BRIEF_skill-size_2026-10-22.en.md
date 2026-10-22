meta/BRIEF_skill-size_2026-10-22.en.md

# Skill size after synthesis — agent copy (source: meta/BRIEF_skill-size_2026-10-22.md, RU, authoritative)

Input for a new session on Skill size (home: projects/kontext-reduktion/). Opinion of SYS session 2026-10-22 unless marked MEASURED. Challenge it.

## MEASURED (clone 2026-10-22; mirrors skills/ == live Skills)
- 11 own Skills, all files: ~1028 KB before synthesis (last mirror commit < 2026-10-18) → ~1187 KB now (+15%).
- SKILL.md layer (read on every trigger): ~394 KB → ~401 KB. Shifted: n8n-workflow-registry 60→11 KB; apps-script-sheets 57→80; context-handoff 18→32; second-brain-git 40→48.
- Composition now (script estimate): "Основание" paragraphs ~10% (~120 KB); "Почему" sentences ~9%; inline addresses ~2%; rules proper ~80%.
- Descriptions of all installed Skills ~22 KB — the only layer in EVERY chat of EVERY project.
- SYS session (sum of files, not a live trace): before first reply ≈143 KB (descriptions 22 + SKILL.md of second-brain-engineer 41 + second-brain-git 48 + CORE ~18 + labs/sys/INDEX.md 14); with first repo write ≈240 KB (+write.md 60, lab.md 14, often delivery.md 24). At ~0.37 token/byte (second-brain-git 8.2, measured on output, not input): ~53k / ~90k tokens. Estimate.

## Thesis
Catalog size is the wrong metric; unread references/ cost nothing. Metric = bytes a session reads by session type: always (descriptions), on trigger (SKILL.md), on event (references/). Step 0: build that cost model once by script from the "Что читать дальше" tables and master prompts. No monitors.

## Form work is exhausted
Stories, version history, ИСТОРИЯ ДИАГНОЗА blocks (33→1) already gone; ~80% is rules. Further reduction = structure, not rewording.

## Levers (ranked)
1. Rule → tool code, Skill keeps one line ("tool error text is the instruction"). Candidates: Channel call form, record-number check, append arithmetic, nodeNames narrowing, includeData ban on dirty workflows. Double win: bytes leave the Skill AND rule holds (second-brain-git 8.2: text bans fail against imitation, 4 repeats). Principle exists (second-brain-engineer references/design.md p.16) but applied per lesson, not as a program. Targets: second-brain-git write.md 60 KB + SKILL.md 48 KB; n8n-engineering-manual roots.md 98 KB. Needs n8n edits with Andrei's "yes".
2. Split executor vs editor reader: move all "Основание" lines to references/basis.md (read by synthesis/harvest only); rule keeps a short tag. ~10%, lossless. Requires change of meta/PROTOCOL_knowledge-synthesis.md ("Что такое правило": basis inside rule) — Andrei decides. Pilot on second-brain-git.
3. Constant layer of the two always-loaded Skills (~89 KB SKILL.md per SYS session): test each paragraph "would a session that never opened references/ err without it?" No → move to event file. Example: clean/dirty workflow table of 7.6 matters only for Channel reads.
4. Descriptions: trigger words + one zone sentence; move content lists to body. Small bytes, but paid always (e.g. medical project anis-evidence carries n8n/Apps Script descriptions). Risk: trigger misses → test on query set (skill-creator).
Keep: "Почему" (generalization, prompt-craft.md), "Не путать" lines.

## Reject
Size ceiling with eviction (Andrei rejected 2026-10-20; writer can't judge importance). Retrieval instead of reading (model doesn't know which rule it lacks). More, smaller Skills (more descriptions, more trigger confusion). Shortening wording (second-brain-git 5.1; Andrei: knowledge over compactness).

## Counter-argument
Maybe size isn't the problem: ~90k tokens of rules fits the window. Real costs: money/time and attention dilution. Dilution is unmeasured. Before big rework: run a few typical SYS tasks on current vs trimmed Skill (only event rules), compare errors. No difference → size is only about money → do lever 1 where reliability needs it anyway.

## Start tasks
1. Read-cost model per session type (script, once) → table in kontext-reduktion canon.
2. List rules of second-brain-git and n8n-engineering-manual enforceable by Channel/workflow code: check, error text, bytes saved.
3. Pilot lever 2 on one Skill; measure; preservation check per synthesis protocol step С5.
4. Lever-3 pass over SKILL.md of second-brain-engineer and second-brain-git.
5. Ask Andrei: dilution test before or after rework.

Related: meta/PLAN_skill-layers_2026-10-20_v3.md; meta/PROTOCOL_knowledge-synthesis.md; meta/SKILLS_MAP.md; projects/kontext-reduktion/LOG.md; projects/knowledge-synthesis/STATE.md.
