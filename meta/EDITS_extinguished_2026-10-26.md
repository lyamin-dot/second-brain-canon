meta/EDITS_extinguished_2026-10-26.md

# Правки Skill и мастер-промпта после охоты на потухшие факты — «было → стало» (2026-10-26)

ПРИМЕНЕНО 2026-10-27 — правки 1–21: все шесть Skills равны зеркалу (позиция AJ-53, сверка 2026-10-27); открыта только правка 22 (мастер-промпт deklaration-v2) (сверка харвеста 2026-10-31).

Источник: пакет `meta/AUDIT_extinguished-facts_2026-10-25.md`; решения Андрея 2026-10-26 («да» на пакет; задачу об источниках Ozon перенести и закрыть; битые ссылки позиции AJ-37 исправить самой сессии; запрет на работу со Skill для этих правок снят — они отменяют испорченные факты). Позиция очереди — AJ-53.

Правки 1–21 ВНЕСЕНЫ В ЗЕРКАЛО `skills/` 2026-10-26 скриптом: каждый текст «было» найден в файле ровно один раз, до правки зеркало совпадало с живыми Skills побайтно (`diff -rq` пуст для всех шести). Живой Skill меняется только заливкой zip владельцем: архивы шести Skills собраны из зеркала и отданы Андрею в чате. После заливки сессия сверяет живые Skills с зеркалом (`second-brain-git`, references/skill-edit.md, 2.6, шаг 1 и шаг 2). Правку 22 (мастер-промпт) вставляет владелец.

Ссылки на задачи лаборатории, закрытые 2026-10-26, ведут в файлы кейсов `meta/CASES_*.md`: текст каждой задачи перенесён туда скриптом без изменений, кроме строки пути, поэтому номера строк в старых ссылках верны (`second-brain-git`, пункт 4б.6).

---

## 1. Skill second-brain-git — SKILL.md

Было:
4. Код книг Google Sheets (проекты Apps Script). Где хранить его копию — предложение проекта sku-cost (закрытый репозиторий), ждёт решения Андрея: projects/sku-cost/STATE.md, раздел «Ждёт Андрея», пункт 3; в этот репозиторий код не кладётся в любом случае.

Стало:
4. Код книг Google Sheets (проекты Apps Script). Копию кода вне Google делает мост gas-bridge по расписанию (запись Р-4 журнала projects/gas-bridge/LOG.md); куда её класть — закрытый репозиторий или папка Google Drive — решение Андрея: projects/gas-bridge/STATE.md, долг 3, связано с задачей labs/sys/t-private-repo.md. В этот репозиторий код не кладётся в любом случае.

## 2. Skill second-brain-git — references/basis.md

Было:
  - код книг — предложение проекта sku-cost, projects/sku-cost/STATE.md (2026-10-18).

Стало:
  - код книг — предложение проекта sku-cost (2026-10-18; проект закрыт тем же днём); решение о копии — запись Р-4 журнала projects/gas-bridge/LOG.md.

## 3. Skill second-brain-git — references/basis.md

Было:
(labs/sys/t-unmerged-claude-branches.md; урок Х-22

Стало:
(meta/CASES_claude-branches.md — текст закрытой задачи labs/sys/t-unmerged-claude-branches.md; урок Х-22

## 4. Skill second-brain-git — references/basis.md

Было:
2026-10-09 и 2026-10-13 — labs/sys/t-skills-mirror-drift.md.

Стало:
2026-10-09 и 2026-10-13 — meta/CASES_skills-mirror-drift.md (текст закрытой задачи labs/sys/t-skills-mirror-drift.md).

## 5. Skill second-brain-git — references/skill-edit.md

Было:
(labs/sys/t-skills-mirror-drift.md; решение В12 файла meta/HARVEST_2026-10-18_answers.md).

Стало:
(meta/CASES_skills-mirror-drift.md — текст закрытой задачи labs/sys/t-skills-mirror-drift.md; решение В12 файла meta/HARVEST_2026-10-18_answers.md).

## 6. Skill second-brain-git — SKILL.md

Было:
а зеркало их догоняло (labs/sys/t-skills-mirror-drift.md). Канон — живой Skill

Стало:
а зеркало их догоняло (meta/CASES_skills-mirror-drift.md — текст закрытой задачи labs/sys/t-skills-mirror-drift.md). Канон — живой Skill

## 7. Skill second-brain-git — references/write.md

Было:
2.4. Ссылка на запись чужого файла пишется с именем файла: «Т-05 журнала PROJECT_LOG_SYS», не «класс Т-05». Номера уникальны внутри файла.

Стало:
2.4. Ссылка на запись чужого файла пишется с именем файла: «Р-109 журнала projects/git-migration/LOG.md», не «решение Р-109». Номера уникальны внутри файла.

## 8. Skill second-brain-engineer — references/basis.md

Было:
`labs/sys/t-unsaved-session-files.md`, раздел «Суть» (кандидат в БЛОКЕРы);

Стало:
`meta/CASES_unsaved-session-files.md` (текст закрытой задачи `labs/sys/t-unsaved-session-files.md`), раздел «Суть»;

## 9. Skill n8n-workflow-registry — SKILL.md

Было:
(`labs/sys/t-knowledge-synthesis.md`, раздел «Решение Андрея 2026-10-20: Skill — инструкции для всех»)

Стало:
(`projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md`, раздел «Решение Андрея 2026-10-20: Skill — инструкции для всех»; задача labs/sys/t-knowledge-synthesis.md снята коммитом a36cf1c)

## 10. Skill n8n-workflow-registry — SKILL.md

Было:
| `labs/sys/t-ozon-ue-parked-active.md`, `labs/ozon-ue/INDEX.md`;

Стало:
| `meta/CASES_ozon-raw-sources.md`, раздел «Итог 2026-10-26» в конце файла, `labs/ozon-ue/INDEX.md`;

## 11. Skill avtopilot — SKILL.md

Было:
создать Claude Project, привязать ключ доступа в n8n, перезалить Skill

Стало:
создать Claude Project, создать ключ доступа (credential) в редакторе n8n — привязывает его к узлам сама сессия, перезалить Skill

## 12. Skill avtopilot — SKILL.md

Было:
(`second-brain-engineer`, references/design.md, пункт 17;

Стало:
(`second-brain-engineer`, references/mass-transfer.md, пункт 17;

## 13. Skill avtopilot — SKILL.md

Было:
(`second-brain-engineer`, references/design.md, пункт 14, г и д)

Стало:
(`second-brain-engineer`, references/design-acceptance.md, пункт 14, г и д)

## 14. Skill naryad — SKILL.md

Было:
— клик в редакторе, привязка ключа, вставка текста —

Стало:
— клик в редакторе, вставка текста; привязка ключа — только когда сессия не может сделать её сама операцией `setNodeCredential` —

## 15. Skill n8n-engineering-manual — SKILL.md

Было:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 (текст — в истории коммитов)

Стало:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 коммитом b91fb1e (текст — по его родителю)

## 16. Skill n8n-engineering-manual — references/roots-net-time.md

Было:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 (текст — в истории коммитов)

Стало:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 коммитом b91fb1e (текст — по его родителю)

## 17. Skill n8n-engineering-manual — references/templates.md

Было:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 (текст — в истории коммитов)

Стало:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 коммитом b91fb1e (текст — по его родителю)

## 18. Skill n8n-engineering-manual — SKILL.md

Было:
(second-brain-engineer, references/design.md, пункт 15)

Стало:
(second-brain-engineer, references/design-acceptance.md, пункт 15)

## 19. Skill n8n-engineering-manual — references/roots-silent.md

Было:
— n8n-workflow-registry, `references/cards-and-declarations.md`, и файл кейсов `meta/CASES_wb-api-card-write.md

Стало:
— `meta/CASES_wb-api.md`, раздел «Карточки и маркировка» (бывший файл n8n-workflow-registry `references/cards-and-declarations.md`), и файл кейсов `meta/CASES_wb-api-card-write.md

## 20. Skill n8n-engineering-manual — references/engine-time.md

Было:
— n8n-workflow-registry (§3 и `references/cards-and-declarations.md`)

Стало:
— `meta/CASES_wb-api.md`, абзац «Форматы дат в карточках» (бывший файл n8n-workflow-registry `references/cards-and-declarations.md`)

## 21. Skill second-brain-git — references/migration.md, абзац «Здесь — то, что обязан знать выдающий задание на перенос…», конец абзаца

Было (абзац целиком):
Здесь — то, что обязан знать выдающий задание на перенос, и правила приёмки целиком. Подробные правила разбора задач и записей — этапы 0а, 0б, 0в и 5 файла meta/PROTOCOL_file-migration.md (редакция 5 от 2026-10-05). Раздел «Контракт записи» и пункт 10.5 «потолок размера» того же файла, а также шаблон meta/NARYAD_file-migration.md целиком написаны до правила происхождения текста и до правила «перенос закончен только в main»: они велят писать каждый файл через Git Write, запрещают push, требуют схождения суммы байт и называют потолок записи, которого нет. При расхождении с ними действует этот файл и references/write.md; по ним самим переноса не вести (противоречие В20 харвеста 2026-10-08 — пометки в первых строках обоих файлов; решение о переписывании этих файлов — за владельцем).

Стало (абзац целиком):
Здесь — то, что обязан знать выдающий задание на перенос, и правила приёмки целиком. Подробные правила разбора задач и записей — этапы 0а, 0б, 0в и 5 файла meta/PROTOCOL_file-migration.md (редакция 5 от 2026-10-05). Раздел «Контракт записи» и пункт 10.5 «потолок размера» того же файла и шаблон meta/NARYAD_file-migration.md были написаны до правила происхождения текста и до правила «перенос закончен только в main» (противоречие В20 харвеста 2026-10-08); 2026-10-26 по решению владельца раздел и пункт вырезаны, шаблон удалён — прежний текст читается по родителю коммита снятия. По оставшемуся тексту протокола при расхождении действует этот файл и references/write.md.

## 22. Мастер-промпт Claude Project проекта deklaration-v2 — строка «Marketplace API facts…»

Почему: файла Skill `references/cards-and-declarations.md` нет с 2026-10-21, а разделов «Права ключей маркетплейсов», «Внешние источники», «Liqui Moly — декларации» в SKILL.md Skill `n8n-workflow-registry` тоже больше нет — их содержимое разнесено по файлам канона, адреса — в таблице Skill. После правки сессия проекта обновляет зеркало `meta/prompts/deklaration-v2.md` и вычёркивает строку «⚡ 2026-10-21, от SYS» в `projects/deklaration-v2/STATE.md`.

Было:
Marketplace API facts (WB card write, documents, marking, Ozon declarations), each with its source: Skill n8n-workflow-registry, references/cards-and-declarations.md and SKILL.md sections «Права ключей маркетплейсов», «Внешние источники», «Liqui Moly — декларации»; facts the Skill lacks — PLAN.md, section «Справочник фактов API». Read before any card or declaration work.

Стало:
Marketplace API facts (WB card write, documents, marking, Ozon declarations), each with its source: meta/CASES_wb-api.md (section «Карточки и маркировка»), meta/CASES_ozon-api.md (section «Декларации»), meta/CASES_wb-api-card-write.md; other addresses (key rights, unreachable external sources, Liqui Moly declarations) — table of Skill n8n-workflow-registry; facts not there — PLAN.md, section «Справочник фактов API». Read before any card or declaration work.

