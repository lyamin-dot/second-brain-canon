meta/EDITS_extinguished_2026-10-26.md

# Правки Skill и мастер-промпта после охоты на потухшие факты — «было → стало» (2026-10-26)

Источник: пакет `meta/AUDIT_extinguished-facts_2026-10-25.md` (раздел Д и закрытие задач лаборатории коммитом 6b5ba5f). Вносит Андрей. Каждый текст «было» сверен с живым Skill 2026-10-26; зеркало `skills/` совпадает с живыми Skills во всех затронутых файлах. Позиция очереди — AJ-53 `registry/maintenance-queue.md`. После внесения: сессия сверяет живые Skills и обновляет зеркало (`second-brain-git`, references/skill-edit.md, 2.6).

Зачем: в Skills стоят ссылки на файлы и решения, которые уже ушли или поменялись. Сессия, читающая Skill, идёт по ссылке в пустоту или считает решённое открытым.

---

## 1. Skill second-brain-git — SKILL.md, инвариант И-7, пункт 4

Почему: проект sku-cost закрыт 2026-10-18; решение о копии кода книг принял его преемник gas-bridge (копию делает мост), открытым остался только вопрос «куда класть».

Было:
4. Код книг Google Sheets (проекты Apps Script). Где хранить его копию — предложение проекта sku-cost (закрытый репозиторий), ждёт решения Андрея: projects/sku-cost/STATE.md, раздел «Ждёт Андрея», пункт 3; в этот репозиторий код не кладётся в любом случае.

Стало:
4. Код книг Google Sheets (проекты Apps Script). Копию кода вне Google делает мост gas-bridge по расписанию (запись Р-4 журнала projects/gas-bridge/LOG.md); куда её класть — закрытый репозиторий или папка Google Drive — решение Андрея: projects/gas-bridge/STATE.md, долг 3, связано с задачей labs/sys/t-private-repo.md. В этот репозиторий код не кладётся в любом случае.

## 2. Skill second-brain-git — references/basis.md, строка под GIT-08 «код книг»

Было:
  - код книг — предложение проекта sku-cost, projects/sku-cost/STATE.md (2026-10-18).

Стало:
  - код книг — предложение проекта sku-cost (2026-10-18; проект закрыт тем же днём); решение о копии — запись Р-4 журнала projects/gas-bridge/LOG.md.

## 3. Skill second-brain-git — references/basis.md, строка GIT-29

Почему: задача labs/sys/t-unmerged-claude-branches.md закрыта 2026-10-26 (условие снятия выполнено); её текст читается по родителю коммита закрытия.

Было (фрагмент):
(labs/sys/t-unmerged-claude-branches.md; урок Х-22

Стало:
(labs/sys/t-unmerged-claude-branches.md — задача снята коммитом 6b5ba5f, текст по его родителю; урок Х-22

## 4. Skill second-brain-git — references/basis.md, строка GIT-49

Почему: задача labs/sys/t-skills-mirror-drift.md закрыта 2026-10-26 (оба условия снятия выполнены).

Было (фрагмент):
2026-10-09 и 2026-10-13 — labs/sys/t-skills-mirror-drift.md.

Стало:
2026-10-09 и 2026-10-13 — labs/sys/t-skills-mirror-drift.md (задача снята коммитом 6b5ba5f, текст по его родителю).

## 5. Skill second-brain-git — references/skill-edit.md, абзац «Не путать: зеркало не канон…»

Было (фрагмент):
(labs/sys/t-skills-mirror-drift.md; решение В12 файла meta/HARVEST_2026-10-18_answers.md).

Стало:
(labs/sys/t-skills-mirror-drift.md, снята коммитом 6b5ba5f — текст по его родителю; решение В12 файла meta/HARVEST_2026-10-18_answers.md).

## 6. Skill second-brain-git — SKILL.md, раздел 3 «Карта репозитория», абзац «Не путать: зеркало skills/ — не канон…»

Было (фрагмент):
а зеркало их догоняло (labs/sys/t-skills-mirror-drift.md). Канон — живой Skill

Стало:
а зеркало их догоняло (labs/sys/t-skills-mirror-drift.md, снята коммитом 6b5ba5f — текст по его родителю). Канон — живой Skill

## 7. Skill second-brain-git — references/migration.md, абзац «Здесь — то, что обязан знать выдающий задание на перенос…»

Почему: шаблон meta/NARYAD_file-migration.md удалён 2026-10-26 (был помечен «УСТАРЕЛ, ПО НЕМУ НЕ ПЕРЕНОСИТЬ»).

Было (фрагмент):
а также шаблон meta/NARYAD_file-migration.md целиком написаны

Стало:
а также шаблон meta/NARYAD_file-migration.md (удалён 2026-10-26 коммитом 6b5ba5f) целиком написаны

## 8. Skill second-brain-git — references/write.md, пункт 2.4

Почему: пример ведёт в журнал PROJECT_LOG_SYS, замороженный 2026-09-26. Пример лучше брать из живого журнала.

Было:
2.4. Ссылка на запись чужого файла пишется с именем файла: «Т-05 журнала PROJECT_LOG_SYS», не «класс Т-05». Номера уникальны внутри файла.

Стало:
2.4. Ссылка на запись чужого файла пишется с именем файла: «Р-109 журнала projects/git-migration/LOG.md», не «решение Р-109». Номера уникальны внутри файла.

## 9. Skill second-brain-engineer — references/basis.md, строка «файл только в рабочей папке сессии и в чате…»

Почему: задача labs/sys/t-unsaved-session-files.md закрыта 2026-10-26 — правило внесено в Р6, процедура харвеста пишет пакет в репозиторий.

Было (фрагмент):
`labs/sys/t-unsaved-session-files.md`, раздел «Суть» (кандидат в БЛОКЕРы);

Стало:
`labs/sys/t-unsaved-session-files.md`, раздел «Суть» (задача снята коммитом 6b5ba5f — правило внесено; текст по родителю коммита);

## 10. Skill n8n-workflow-registry — SKILL.md, абзац «Этот Skill — указатель, а не справочник…»

Почему: файла labs/sys/t-knowledge-synthesis.md нет с коммита a36cf1c; раздел с решением живёт в файле истории проекта.

Было (фрагмент):
(`labs/sys/t-knowledge-synthesis.md`, раздел «Решение Андрея 2026-10-20: Skill — инструкции для всех»)

Стало:
(`projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md`, раздел «Решение Андрея 2026-10-20: Skill — инструкции для всех»; задача labs/sys/t-knowledge-synthesis.md снята коммитом a36cf1c)

## 11. Skill avtopilot — SKILL.md, пункт 3 «Все ручные действия Андрея — одним списком сразу»

Почему: с 2026-10-20 ключ к узлам привязывает сама сессия операцией `setNodeCredential` (second-brain-engineer, references/permissions.md; google-drive-docs, references/infra.md). Создать ключ сессия по-прежнему не может: секрет через неё не проходит.

Было (фрагмент):
создать Claude Project, привязать ключ доступа в n8n, перезалить Skill

Стало:
создать Claude Project, создать ключ доступа (credential) в редакторе n8n — привязывает его к узлам сама сессия, перезалить Skill

## 12. Skill naryad — SKILL.md, абзац «Действие в интерфейсе n8n или в браузере Андрея…»

Почему: то же, что в правке 11 — привязка ключа больше не ручное действие по умолчанию.

Было (фрагмент):
— клик в редакторе, привязка ключа, вставка текста —

Стало:
— клик в редакторе, вставка текста; привязка ключа — только когда сессия не может сделать её сама операцией `setNodeCredential` —

## 13. Skill n8n-engineering-manual — три места с одним и тем же фрагментом

Места: SKILL.md, абзац «Воркфлоу ошибок и явная таймзона — не по умолчанию»; references/roots-net-time.md, абзац «Отсутствие явной таймзоны — не исключение…»; references/templates.md, пункт T2.4.9.

Почему: «текст — в истории коммитов» не называет коммит, а без номера коммита снятую задачу из истории не найти.

Было (фрагмент, во всех трёх местах одинаковый):
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 (текст — в истории коммитов)

Стало:
задача `labs/sys/t-failure-visibility.md`, снята 2026-10-21 коммитом b91fb1e (текст — по его родителю)

## 14. Мастер-промпт Claude Project проекта deklaration-v2 — строка «Marketplace API facts…»

Почему: файла Skill `references/cards-and-declarations.md` нет с 2026-10-21, а разделов «Права ключей маркетплейсов», «Внешние источники», «Liqui Moly — декларации» в SKILL.md Skill `n8n-workflow-registry` тоже больше нет — их содержимое разнесено по файлам канона, адреса — в таблице Skill. После правки сессия проекта обновляет зеркало `meta/prompts/deklaration-v2.md` и вычёркивает строку «⚡ 2026-10-21, от SYS» в `projects/deklaration-v2/STATE.md`.

Было:
Marketplace API facts (WB card write, documents, marking, Ozon declarations), each with its source: Skill n8n-workflow-registry, references/cards-and-declarations.md and SKILL.md sections «Права ключей маркетплейсов», «Внешние источники», «Liqui Moly — декларации»; facts the Skill lacks — PLAN.md, section «Справочник фактов API». Read before any card or declaration work.

Стало:
Marketplace API facts (WB card write, documents, marking, Ozon declarations), each with its source: meta/CASES_wb-api.md (section «Карточки и маркировка»), meta/CASES_ozon-api.md (section «Декларации»), meta/CASES_wb-api-card-write.md; other addresses (key rights, unreachable external sources, Liqui Moly declarations) — table of Skill n8n-workflow-registry; facts not there — PLAN.md, section «Справочник фактов API». Read before any card or declaration work.

---

## Противоречия и устаревшие места, найденные попутно (решение по каждому — Андрея)

- Skill n8n-workflow-registry, SKILL.md, строка таблицы «Два источника OZON_UE RAW в одной книге»: ведёт в задачу `labs/sys/t-ozon-ue-parked-active.md`. Задача оставлена открытой именно потому, что она — адрес ответа для этой строки; её остаток (паспорт Accrual Sync) ведётся в `labs/ozon-ue/INDEX.md`. Если перенести ответ («живой — Accrual Sync, OzonRawАналитика снят 2026-10-24») в `meta/CASES_ozon-api.md`, задачу можно будет закрыть, а строку Skill переадресовать туда.
- Остатки уже открытых позиций очереди (новых позиций не завожу): AJ-37 — avtopilot SKILL.md и n8n-engineering-manual SKILL.md ещё ссылаются на пункты 14, 15, 17 файла references/design.md, которые переехали в design-acceptance.md и mass-transfer.md; AJ-45 — n8n-engineering-manual references/roots-silent.md и engine-time.md ссылаются на снятый `references/cards-and-declarations.md`; AJ-33 — второй факт (правка только описания черновика не создаёт) в n8n-engineering-manual не внесён, статус позиции исправлен на ОТКРЫТА 2026-10-26.
