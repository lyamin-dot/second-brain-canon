# Checker brief — TASK 2: verify preservation (step С5)

READ-ONLY. Write only your verdict file. ROOT, CLONE, OLD as in CHECKER_BRIEF.md (ROOT/in/).
Read CLONE/meta/PROTOCOL_knowledge-synthesis.md step С5 and section «Чего в Skill не бывает».
Inputs for group G: your table ROOT/work/units_G_<model>.md; the OLD text of your group; the NEW text of your group (A: ROOT/new/SKILL.md; B: ROOT/new/references/issuer.md, foreman.md; C: ROOT/new/references/destructive-orders.md, executor.md, revision.md); the writer's ROOT/work/BASIS_G.md (address of every case — the synthesis report will contain it) and ROOT/work/PARTICULARS_G.md (particulars moved to carriers). Do NOT read WRITER_REPORT_G.md (it is the writer's self-assessment).
Pointers to other groups are legitimate: if the new text points to a section owned by another group (e.g. §3.7, §6, §3.1), check the unit is in that group's new file.

For EVERY unit (OLD and NEW) one verdict:
- В ТЕКСТЕ — quote from the new text (≤80);
- ПО АДРЕСУ — the address is named in the new text or in BASIS_G/PARTICULARS_G and you verified it exists in CLONE (grep) and holds the fact; for a particular (flag ОСОБ) the carrier must hold the fact or PARTICULARS must say «перенести: <text>» with the text;
- ОСЛАБЛЕНО — meaning changed (condition narrowed/widened, «запрещено» → «желательно», number changed, a reason lost its mechanism);
- ПОТЕРЯНО.
Admission: ПРАВИЛО, ИСКЛЮЧЕНИЕ, ПОРОГ, ПРОВЕРКА only В ТЕКСТЕ (exception: ОСОБ units → ПО АДРЕСУ allowed); ПРИЧИНА in text, generalised form allowed; СЛУЧАЙ, АДРЕС — in text or ПО АДРЕСУ. A unit that is intentionally superseded by a NEW unit (e.g. the issuer.md counter «из 10 шагов» replaced by the pointer to revision questions — contradiction 8; the description line on Claude-Projects replaced by AI-5) — verdict «ЗАМЕНЕНО» with the new quote and the superseding unit id; that is acceptable only if the supersession comes from a NEW unit backed by Andrei's decision/journal.

Then three more sections:
1. «Знание вне таблицы» — re-read the OLD text and list knowledge absent from your table, with its verdict in the new text.
2. «Расширено» — what the new text claims beyond old+new units (generalisations widening a rule's scope; new facts).
3. «Дефекты формы» — case stories, edit-history lines, ИСТОРИЯ ДИАГНОЗА blocks, particulars of concrete objects, missing «почему», basis lines not in the form «Основание: N случаев, последний <дата> — отчёт синтеза, правило <id>» (or Andrei's decision with date), section/point numbers or names lost or renumbered vs OLD (3.1–3.9, 3.1а, 4–8, Ограничители, Приёмка, Пересмотр, numbered questions), И-7 classes (IDs of documents/workflows, webhook paths, credential names, emails).

Output: ROOT/work/verdicts_G_<model>.md: header with counts per verdict; table «id | class | verdict | quote or address | note»; then the three sections. Report back counts + every ПОТЕРЯНО/ОСЛАБЛЕНО id in ≤15 lines.
