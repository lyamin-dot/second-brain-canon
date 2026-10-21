# Acceptance round 2 — n8n-workflow-passport synthesis

Compared new_SKILL_acc1.md with new_SKILL.md. The diff touches only lines 34, 89, 93, 99, 152 and 263. Also re-checked the updated REPORT.md and /tmp/sbc (HEAD 3a553aa).

## A1.1 / A3.1 — ИНСТРУМЕНТЫ scope — REFUTED (residual, minor)
- Stage 3, last paragraph (line 99) is now fixed. It restores the old wording: «У проектов, чей INDEX перенесён в репозиторий, — например лаборатория `labs/sys/` — секции ИНСТРУМЕНТЫ нет вовсе (у лаборатории две роли файлов — second-brain-git, 4б.3)». The pointer is now applied to the laboratory, which `lab.md` 4б.3 covers. Checked: `labs/sys/INDEX.md` and `labs/ozon-ue/INDEX.md` have no ИНСТРУМЕНТЫ section; no `projects/*/INDEX.md` exists. The scope and strength match old line 91.
- Line 263 is still not true against /tmp/sbc. It says «у проекта в репозитории — его `PLAN.md` (обычно раздел ИНСТРУМЕНТЫ)». Only 2 of the 17 `projects/*/PLAN.md` files have a `## ИНСТРУМЕНТЫ` section (wb-ue, wb-logistics). Only one PLAN holds `DOCS_FOLDER` at all (`projects/wb-ue/PLAN.md:36`). So «обычно» is an overstatement. The word also sits uneasily next to line 99, which says repository projects have no ИНСТРУМЕНТЫ section. Fix: drop «(обычно раздел ИНСТРУМЕНТЫ)», or write «(у wb-ue — раздел ИНСТРУМЕНТЫ)». REPORT «Расширено» item 3 carries the same «обычно».

## A1.2 — record "снят и почему" — HOLDS
- Line 152: «Что воркфлоу снят и почему, записывается туда, где проект хранит невзятое и снятое (обычно `NOT_TAKEN.md` или журнал проекта), — причина обязательна и тогда, когда паспорта у воркфлоу нет.» This has the same strength as old line 149 step 3. The added clause makes the passport-less case explicit.

## A1.3 / A3.2 — superseded-version contradiction — HOLDS
- The new text no longer says «Само правило … — раздел 2.5». It delegates only «Как снимать и как проверять снятие чтением» to 2.5, and 2.5 does contain both (lines 84 and 90).
- The passport's own no-archive rule for «вытесненный новым» stays in the passport as in the old line 144. The contradiction with 2.5 line 86 is listed in REPORT «Противоречия», item 0, quoting both texts.

## A2.2 — addresses for "Андрей руками" — HOLDS
Checked in the repo:
- `projects/card-content-sync/PLAN.md:42` says «(вписывает Андрей руками)».
- `meta/DECLARATION_SCAN.md:96` says «вписывать руками в настройках воркфлоу, не через MCP».
- `projects/n8n/STATE.md` section «Паспорта воркфлоу (2026-10-21, автопилот)», line 65, says «Строку вписывает Андрей руками».
- The REPORT row now separates out the «Правила, вынесенные…» section correctly and names deklaration-wb PLAN as presence-only.
- New line 93 says «2 плана проектов и состояние проекта n8n», which is consistent; the unsupported date 2026-10-09 is gone.

## A4 — instance count — HOLDS
- Line 34 now reads «при проверке воркфлоу в августе–сентябре 2026». The count «девяти» is kept in REPORT row NWP.что-вносится, line 14.

## Hypothesis H1 (empty description wording) — HOLDS (resolved)
- Line 89 now reads: «Без риска потери обходится только пустой `description`, но и это правило «вписывает Андрей» не меняет.» This is unambiguous.
- Minor leftover: REPORT «Расширено» item 1 (line 48) still uses the old wording «безопасен для записи сессией только пустой `description`». Align it with the Skill.

## Did any fix lose or weaken something else? — No loss found
- The diff has only the six changed lines. Each new line keeps everything the round-1 line held, apart from the intentionally removed «девяти», «2026-10-09» and «Само правило».
- The check by reading (`active: false`) is still delegated to 2.5, which holds it, so it is not weakened.
- The passport status-line form and the owner-only archiving rule are unchanged.
