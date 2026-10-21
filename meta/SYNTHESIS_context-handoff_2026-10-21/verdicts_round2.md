# Verdicts round 2 (context-handoff new text vs old units)

## 1. H010, H012 (version 1.1, supersedes 1.0)
H010: BY_ADDRESS. REPORT.md section «Прежние значения шапки» names «version 1.1; created 2026-08-03; supersedes 1.0; owner Андрей», source line 3 of the old text, and says history is in the mirror commit history. Not in the Skill itself; class is CASE-like metadata, so address admission is acceptable.
H012: BY_ADDRESS, same section («supersedes 1.0»).
H011 (created 2026-08-03) and H013 (owner) stay IN_TEXT / also listed there.

## 2. diff new_SKILL_r1.md -> new_SKILL.md (three hunks)
- l118: «Это сжатая форма меток Р15» replaced by «Метки соответствуют меткам Р15, грубо: Ф — прочитано в этой сессии; Г — всё, что не прочитано (вспомнено, выведено, предположено)». Nothing lost: «Ф = проверено чтением, Г = гипотеза» (H114) intact. Mapping now honest.
- l191: «раздел 8» now «раздел 8 Skill second-brain-git» and «раздел 8 того Skill». Nothing lost, ambiguity removed.
- l197: transport clause rewritten (dry-run probe wording, 8.2 citation, Cyrillic warning). Nothing lost from r1 content: block-then-mark order, 8.10, 8.3, reason all kept.
Result: no WEAKENED, no LOST introduced by the diff.

## 3. Round-1 new-claim items
- l118 label mapping: RESOLVED. Wording «грубо», Г = everything not read; matches Р15 (three labels plus «Гипотеза (не проверена)» prefix). Listed in «Расширено» п.8.
- «раздел 8» ambiguity: RESOLVED in l191 (both occurrences name second-brain-git). Remaining unqualified «раздел 8» at l30, l31, l147 means this Skill's section 8 and sits in the same Skill context; acceptable.
- Cyrillic warning: RESOLVED in substance (l197 now states the \uXXXX weak spot). Pointer to 8.2 is partly right: write.md 8.2 says «Кириллица набирается как есть: последовательности \uXXXX модель в теле вызова не набирает», and the cost/weak-link discussion (table rows (в),(г) saying Git Replace has no Drive-file input yet) sits a few lines below 8.2 in the same part of write.md (lines 140-151), not in the 8.2 sentence itself. Minor: cite 8.2 «и следующий за ним разбор» or accept.
- l197 transport via clone: NOT RESOLVED, still wrong attribution. write.md 8.2 says only: text of a write must exist as a file before the call (on session disk or in Drive _git_staging); body typing from memory forbidden; Cyrillic as is. It does NOT say that clone writing of session-produced text is permitted, nor that it «снимает набор тела». The permission/route lives in delivery.md 9.4: (а) fragment edit or append of session-made text -> Channel, «маршрут по умолчанию в любой среде»; (б) clone script route is for files assembled from already existing text, after `git push --dry-run` passed (9.1). So «обе правки уходят одним коммитом клоном» for session-made block text contradicts 9.4(а) default and is not supported by 8.2. Fix: either drop the clone route (use Channel only, 8.3, 8.10) or cite 9.4 and say clone route is allowed only if the session chose it and push passed, and name that Channel is default. Cited 9.1 (dry-run predicate) is correct.

## 4. «Расширено» completeness
Round-1 writer elaborations: INDEX mark form (п.1), order block-then-mark (п.2), two-last-lines anchor (п.3), clone transport (п.4), closure with mark (п.5), one-line for repo files (п.6), stale = case of Р15 rule (п.7), Ф/Г mapping (п.8), «Как устроен текст» (п.9), INDEX -> канон in anti-pattern (п.10). All round-1 items are listed; the Cyrillic warning is included in п.4. Gaps (two minor, both low): (a) the reason for the INDEX mark («на старте читается только INDEX.md…», l195) is not named as elaboration; (b) the clause on the 4.5 exception (l196: overwrite whole file allowed only for atomic create/close) is a verified paraphrase, not new. Verdict: complete except gap (a). Item п.4 must change once l197 is fixed.

## Summary
H010, H012 -> BY_ADDRESS. Diff clean. Open: l197 clone-route attribution (8.2 does not hold it). Minor: Cyrillic detail lives just below 8.2; elaboration list lacks the INDEX-mark reason.
