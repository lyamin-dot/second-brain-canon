# Verdicts round 2 (n8n-workflow-passport)
| id | verdict | evidence |
|---|---|---|
| P331 | IN_TEXT-equivalent (accepted, BY_ADDRESS for the rename) | New heading «## Долг паспортов» carries no date; REPORT.md «Переименовано» states the reason (date was a snapshot date, snapshot removed) and that no links to the old name exist. The snapshot date is now only in REPORT.md and mirror history; the new section says «Числа в этот Skill не пишутся». Sufficient: the heading was a label of a removed snapshot, not a rule. |
| P338 | IN_TEXT | New «Долг паспортов»: «Долгом считается и паспорт, который есть, но недостижим: не назван ни в `description`, ни в `registry/tools.md`, — ни один путь стадии 1, кроме поиска по имени, его не найдёт.» The old «or no passport, or unreachable — both debt» is restored (the missing-passport half is already in the section's first sentence). |

## Diff new_SKILL_r1.md vs new_SKILL.md (3 changed lines)
1. credential paragraph: «объект не скажет никогда» -> «объект не скажет». Removes the strengthening I flagged as beyond-old (round-1 section 2, item 4); matches old P081 exactly. Nothing lost.
2. Stage 3 step 5 Основание: «4 плана проектов» -> «3 плана проектов». Consistent with the round-1 address finding (only three plans require «руками»). The sentence in the step «так требуют планы проектов» is unchanged; P162/P163 remain IN_TEXT/BY_ADDRESS (REPORT.md row NWP.строка-паспорта lists the three plans and the fourth separately). Nothing lost.
3. «Долг паспортов»: added the unreachable-passport sentence (fixes P338). Nothing else changed.
Result: no weakening or loss of anything IN_TEXT in round 1.

## Addresses
- Address 2 (deklaration-wb/PLAN.md): FIXED. REPORT.md row NWP.строка-паспорта now says three plans require manual entry; deklaration-wb/PLAN.md only requires the line's presence (verified before: PLAN.md l.45). The row cites `projects/n8n/STATE.md` section «Правила, вынесенные из закрытых задач»: that section exists (l.47) and l.49 holds the 255-char/manual rule.
- Address 4 (DOCS_FOLDER): FIXED. «Расширено» item 3 cites `projects/wb-ue/PLAN.md` l.36 (DOCS_FOLDER verified) and `labs/ozon-ue/INDEX.md` l.28 (`DOCS_FOLDER: 1yifa_sfm6l7b0l08dB8ghzadeEGbIcSQ` verified). Lab = INDEX.md and repo project = PLAN.md are now backed by a real lab example. Note: new text says «у лаборатории — её INDEX.md»; that is true for ozon-ue, not for labs/sys (no DOCS_FOLDER there) — fine as a general statement, listed in REPORT.md as writer's generalization awaiting Andrei's decision.

## Findings
No new defects. Skipped by instruction: address 1 (STATE.md line about four Git workflows) and 3 (report not yet in repo).
