# ACCEPTANCE — apps-script-sheets, synthesis pass 2026-10-22

Acceptor: independent subagent; read-only. Objects read: OLD /mnt/skills/plugins/apps-script-sheets/ (diff -r against clone skills/apps-script-sheets/ is empty), NEW scratchpad/ass/new/, BASIS_TABLE.md, clone /tmp/second-brain-canon (HEAD d17836a), Google documentation pages listed under A6. Abbreviation: N = scratchpad/ass/new/.

## Summary

| Claim | Verdict |
|---|---|
| A1 13 findings present | NOT REFUTED |
| A2 addresses fixed | NOT REFUTED |
| A3 headings and verbatim old text | REFUTED (minor): two old sentences in lines the claim does not exempt lost their final period because text was added after them; their meaning is unchanged |
| A4 no object data or case stories in inserted text | NOT REFUTED (one borderline note) |
| A5 BASIS addresses exist and support | NOT REFUTED |
| A6 documentation claims | NOT REFUTED |
| A7 no contradictions | NOT REFUTED |
| A8 samples.md identical | NOT REFUTED |

## A1 — NOT REFUTED

Source of the findings: /tmp/second-brain-canon/meta/HARVEST_2026-10-22.md, lines 89–103.

- J1#13: N/references/design.md:51 is the example paragraph (columns for truth, first account and second account; the platform's value is never written into the truth column). It is narrowed to an example. Justification: Andrei's decision (3) in projects/knowledge-synthesis/PLAN.md:136 («входит примером, не общим правилом»), and the source projects/deklaration-v2/LOG.md Р-39 (12): «Идея Андрея на развитие, не задание сейчас».
- J3#1: N/references/book-traps.md:115–116 covers a service call on every row, the run time jumping by multiples, the 6-minute ceiling, the cure by caching or by date arithmetic, and the measured gain of hundreds of times. The table row is at N/references/book-traps.md:224.
- J3#7: N/SKILL.md:158 marks it as a hypothesis, untested. It says FORMULA reads may arrive in US notation, so the separator is taken from §0.2 or §4.8 instead.
- L2#14: N/references/book-traps.md §3.13 (lines 190–193) plus the table row at line 234. The finding's "334 rows #N/A" part is omitted. That is justified: labs/ozon-ue/t-cost-history-copy.md:46 records that defect as harmless and closed («Дефект снят как безвредный»). The key-in-one-place idea is kept as «ключ связки брать из его источника».
- L2#17б: N/SKILL.md:419 (trigger time is chosen by Google; a day is missed after the trigger is moved) plus the table row at line 452.
- L2#19: N/SKILL.md:421 (a backup second trigger does not cure the failure and masks it) plus the table row at line 452.
- S1#17: N/references/design.md:38 plus the table row at N/SKILL.md:456.
- S1#18: N/SKILL.md:350 plus the table row at line 454.
- S1#19: N/SKILL.md:352 covers row numbers shared by two layers, hard-coded addresses, and the number of periods in a code comment. The table row is at line 455.
- S2#14: N/SKILL.md:62, confirmed by documentation (see A6).
- S3#2: N/SKILL.md:337 (the execution log is kept about 7 days; read it immediately) plus the table row at line 453.
- M1c#8-5: N/references/signal.md §9.10 (lines 144–148) plus the table row at line 166.
- M1c#8-22: N/references/design.md:34 (an alert cell without a reader is a dead alert: the reader must exist, be published, and its message must be checked by actual arrival).

## A2 — NOT REFUTED

- AJ-32: N/SKILL.md:16 now points to projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md. The section «Решение Андрея 2026-10-20: Skill — инструкции для всех» exists at line 179 of that file. The old path labs/sys/t-knowledge-synthesis.md does not exist in the clone, and grep finds no occurrence of it in N.
- AJ-45: N/SKILL.md:80 now reads «в коммите 2f30998 … удалён коммитом 053bdce».
  - `git show 2f30998:labs/ozon-ue/t-goods-book-script.md` has ЭСТАФЕТА at line 21 and ЗАПРЕТЫ at line 26, containing «полный текст файла на вставку, не дифф».
  - Commit 053bdce removes 15 lines from that file. The current file has no ЭСТАФЕТА section.
- AJ-37: N/SKILL.md:341 and N/references/signal.md:138 now point to `references/design-acceptance.md`, point 14.
  - Point 14 is at skills/second-brain-engineer/references/design-acceptance.md:13.
  - Letter е (cited in signal.md) is at line 41 of the same file. It is the right letter: it is about proving "nothing found" with a positive control.
  - grep finds no remaining «references/design.md» link to point 14 of second-brain-engineer anywhere in N.
- Observation, not part of the claim: N/SKILL.md:18 names a new file, meta/SYNTHESIS_apps-script-sheets_2026-10-22.md. That file does not exist in the clone yet; only the 2026-10-20 report exists. All 15 new «Основание» lines point to it, so it must be written before the Skill is uploaded.

## A3 — REFUTED (minor, no loss of meaning)

- Headings: comparing the numbered headings of OLD and NEW per file, the only additions are book-traps §3.13 and signal §9.10. No number moved files or was renumbered. The bold numbered paragraphs 0.1 and 0.2 are unchanged.
- Verbatim text, checked by `diff` of the four files: every changed line falls into an exempt category, with two exceptions:
  - N/SKILL.md:18 (paragraph «Строка «Основание»»). The old sentence ended «…где лежат адреса самих случаев.»; the period is now a semicolon followed by a new clause about the 2026-10-22 report.
  - N/references/signal.md:142 (§9.9 «Основание» line). The old line ended «…правило ASS.9.9.свежесть.»; the period is now a semicolon followed by a new case.
  - Neither line is in the claim's exemption list. In both, the old words are intact and only the final punctuation changed to make room for an extension.
- Lines extended without breaking any old sentence (the old text survives verbatim, so not a refutation):
  - N/SKILL.md:62: S2#14 sentences inserted between two old sentences.
  - N/references/signal.md:128: sentences appended after the old paragraph.
  - N/references/signal.md:138: besides the address change, «, буква е» was added.
  - The claim's exemption list does not mention these extensions.
- Remedy: update the claim's exemption list to include SKILL.md:18 and signal.md:142, or keep the old sentence and put the new clause in a separate sentence.

## A4 — NOT REFUTED (one borderline note)

- The inserted text, the «>» lines of all four diffs, contains no:
  - Google file IDs, workflow IDs, webhook paths, e-mail addresses or credential names;
  - book code;
  - book, sheet or shop names. Checked by grep for long identifiers, @, Деньги, Товары, Price Master, sku_cost, wb_/oz_, WB, Ozon, ИП, Lopal, Liqui. The only hits were old unchanged lines that sit on the same changed lines.
- Accounts are generalized to «первый кабинет» and «второй кабинет» (design.md:51).
- Some in-body references to Andrei's decisions remain: signal.md:128 and design.md:51. This matches the existing practice in OLD (for example §9.9 «решение Андрея 2026-10-18 …») and the protocol rule «Правило, основанное на решении Андрея, называет дату и место решения».
- Borderline:
  - N/SKILL.md:421 says in the body «дважды отклонялось сессиями (решения Андрея о запрете нет)», which is who-decided status outside the «Основание» line. It works as a status qualifier, like «гипотеза, не проверена», not as a story.
  - N/references/book-traps.md:115 states «Измерено на `Utilities.formatDate` … в сотни раз», a measurement fact without who or when.

## A5 — NOT REFUTED

Every BASIS address exists and supports its row. Lines read:

- ASS.1.запуск: projects/gas-bridge/PLAN.md:17 says running through Google's interface requires moving each book into a Google Cloud project; no source is named.
- ASS.2.1.чтение-api:
  - projects/wb-ue/LOG.md, Р-70 (8) (line 420) states the hypothesis verbatim.
  - projects/wb-ue/STATE.md:83 is the separator disagreement that proposes checking by a FORMULA read.
- ASS.4.4.журнал:
  - labs/ozon-ue/t-money-telegram.md:107 «хранит 7 дней (надпись страницы)».
  - Р-70 (2) «журнал хранится 7 дней».
  - STATE.md:86 «окно до 23.10».
- ASS.4.5.число: projects/sku-cost/PLAN.md:151.
- ASS.4.5.договорённость: projects/sku-cost/PLAN.md:124 (rows 5–17 on two layers), :145 (98 periods versus 54 columns), :170.
- ASS.4.9.час: labs/ozon-ue/t-money-telegram.md:82 (trigger times 06:32 and 04:17) and :106 (the trigger was moved and on 15.10 there was no trigger run).
- ASS.4.9.повтор:
  - t-money-telegram.md:102 is proposal (3), a second trigger.
  - t-money-telegram.md:112 is its rejection.
  - projects/wb-ue/LOG.md:423 has «отвергнуто: второй триггер…».
- ASS.3.7.вызовы:
  - Р-70 (2): about 98 thousand formatDate calls, 70–300 s, failures on 16, 20 and 21.10.
  - Р-71 (2): 0.2 s after the fix, «в сотни раз».
  - Р-71 (4): the Ozon books convert dates by arithmetic and do not fail this way.
  - sku-cost/PLAN.md:153–163, including line 161 (about 46 thousand formatDate calls) and lines 154–159 (single-cell writes).
- ASS.3.13.копия: labs/ozon-ue/t-cost-history-copy.md:42 («Копировать в»), :43 (VLOOKUP gives #REF!), :46, :50 («Листа SKU_Artikel не существует»; columns cleared).
- ASS.9.9.метка:
  - Р-70 (1): a false "data did not arrive" alert while the book had not recalculated.
  - Р-70 (6): the session's rejection.
  - STATE.md:17 and :85.
  - Decision: projects/knowledge-synthesis/PLAN.md:134–136, answer (1).
- ASS.9.10.неполный:
  - t-money-telegram.md:44 (6 of 7 days, the gap was silent), :61 and :72.
  - meta/HARVEST_2026-10-18_reports/G8.md:46.
- ASS.5.читатель:
  - t-money-telegram.md:10–11 (Ozon alert texts that no workflow read).
  - projects/wb-ue/LOG.md:202, Р-39 (WB reader never published; status «ОТМЕНЕНО Р-59», republished at line 310, as the BASIS row says).
  - G8.md:80.
- ASS.5.ширина: sku-cost/PLAN.md:168 (`autoResizeColumn(1)` widened the column to 1560 px).
- ASS.5.сверка-колонки:
  - projects/deklaration-wb/LOG.md:104, Р-13 (a separate reference column; «смешение … в одной колонке вернуло бы путаницу»).
  - projects/deklaration-v2/LOG.md, Р-39 (12).
- Check of the JavaScript claim: `node -e` gives Number("1 234,56") = NaN, and NaN||0 = 0.

## A6 — NOT REFUTED

- Sheets API ValueRenderOption (https://developers.google.com/workspace/sheets/api/reference/rest/v4/ValueRenderOption): FORMULA reads «Values will not be calculated. The reply will include the formulas.» Locale is mentioned only under FORMATTED_VALUE. Matches N/SKILL.md:158 «о локали молчит».
- scripts.run (https://developers.google.com/apps-script/api/reference/rest/v1/scripts/run):
  - «the calling application must share the same Cloud Platform project».
  - «403, PERMISSION_DENIED … the Cloud Platform project used to authorize the request is not the same as the one used by the script».
  - The script must be deployed for the Apps Script API.
- Cloud Platform projects (https://developers.google.com/apps-script/guides/cloud-platform-projects): a standard project is needed for an application that executes functions with scripts.run; «the script project and the calling application must share the same standard project».
- Logging (https://developers.google.com/apps-script/guides/logging): the execution log «persists only for a short time»; no number is given.
- ClockTriggerBuilder (https://developers.google.com/apps-script/reference/script/clock-trigger-builder):
  - nearMinute: «Specifies the minute at which the trigger runs (plus or minus 15 minutes)».
  - atHour example: «Runs between 5am-6am».
  - The installable-triggers guide (https://developers.google.com/apps-script/guides/triggers/installable) adds «Apps Script chooses a time between 9 AM and 10 AM».
- One inference in N/SKILL.md:419, «пересоздание ставит время заново», is not stated in the documentation. It is consistent with it (the time is chosen once, then fixed) and with labs/ozon-ue/t-money-telegram.md:106.

## A7 — NOT REFUTED

- §4.9 (N/SKILL.md:419, 421) against signal §9.9: both rely on the external label-age check, and §4.9 adds no new monitor, so the rule «новый воркфлоу не заводится» holds. The §9.9 addition at line 128 is consistent with the existing text «читает метку последнего прогона книги … и последнюю дату данных».
- §9.10 against §9.5: §9.5 step 2 drops periods without a full norm window from the threshold backtest. §9.10 keeps dropping them from the norm («исключение из нормы правильно для расчёта») and only adds a message. No conflict.
- book-traps §3.7 new paragraph:
  - against SKILL §2.1: block writes with `setFormulas`, explicitly cross-referenced at N/SKILL.md:156.
  - against §2.7: date arithmetic «учитывая сдвиг часового пояса», with a reference.
  - against §4.8: it says nothing about read or write order, and it points the "heavy book read" hang back to the «Практический вывод» paragraph.
- design.md new paragraphs:
  - «Ширина» (setColumnWidth, or setColumnWidths on a block) agrees with book-traps:115 (no loops of single setColumnWidth calls).
  - «Без читателя» demands an existing published reader, not a new workflow, so it agrees with §9.9 «Новый воркфлоу ради этого не заводится».
  - The «сверка-колонки» example applies the §5 law (the eye must not read one value for another).

## A8 — NOT REFUTED

`cmp` of OLD and NEW references/samples.md shows the files are byte-identical (7239 bytes each).

## A3 — повторная проверка (после правки координатора)

Verdict: NOT REFUTED.

Method: `diff` of OLD against the current N, then a Python check. The script split each OLD paragraph into sentences and tested that each sentence occurs verbatim in the matching N line.

- N/SKILL.md:18, paragraph «Строка «Основание»»: both OLD sentences are verbatim, including the original period after «…адреса самих случаев.». The new sentence «Строка «— отчёт синтеза 2026-10-22, правило …» ведёт в отчёт `meta/SYNTHESIS_apps-script-sheets_2026-10-22.md`.» is separate.
- N/references/signal.md:142, §9.9 «Основание»: the OLD line is verbatim, ending «…правило ASS.9.9.свежесть.». The new case is a separate following sentence, «Ложная тревога …».
- N/SKILL.md:62, «Мост пишет код…»: every OLD sentence is verbatim, 0 missing.
- N/references/signal.md:128, «Кто проверяет возраст»: every OLD sentence is verbatim, 0 missing.
- N/references/signal.md:138, «Ветка «старое»…»: the first sentence is verbatim. The second differs only by the exempt AJ-37 address change, `references/design.md` → `references/design-acceptance.md`, plus the appended «, буква е». It is otherwise verbatim.
