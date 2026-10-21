# PARTICULARS — группа D (references/mcp.md, references/failures.md)

Особенности конкретных объектов и привязки к конкретным документам, снятые из Skill (решение Андрея 2026-10-20, `projects/knowledge-synthesis/HISTORY_2026-10-18_to_2026-10-21.md`, раздел «Решение Андрея 2026-10-20: Skill — инструкции для всех»). Поиск — по клону на коммите c07975a, `grep -rn` без папки `skills/`.

В этих двух файлах особенностей объектов мало: почти всё — свойства коннектора Google Drive, Docs API и движка n8n, верные для любого экземпляра. ID воркфлоу в старых mcp.md и failures.md не было.

| unit (quote ≤80) | носитель | держит ли носитель (что искалось) |
|---|---|---|
| «узлы … `03_Get_Metadata` и `05A_Export_Doc` … `n8n-nodes-base.httpRequest`» (по смыслу строки §9 о contextData: «свойство принадлежит типу узла загрузки (`n8n-nodes-base.httpRequest`)» — факт о воркфлоу gdocs-read) | `registry/tools.md`, раздел «Свойства канала целиком», строка 22 | да — «воркфлоу чтения Google Docs `gdocs-read` … тоже ГРЯЗНЫЙ — узлы `03_Get_Metadata` и `05A_Export_Doc` имеют тип `n8n-nodes-base.httpRequest`» (искалось «ГРЯЗН», «05A_Export_Doc»). В новом тексте — указатель на этот раздел и на механизм R4.5 |
| «Карта узлов по воркфлоу — `registry/tools.md`» | `registry/tools.md` | да; указатель оставлен |
| «google_drive_fetch … на крупных и растущих файлах (INDEX, CORE, OPS)» | случай, не особенность; `projects/n8n/INCIDENT_LOG.md` строка 32 | да (искалось «google_drive_fetch»); имена документов — в BASIS D.2.2.1 |
| «2,81 на SYS_INDEX 2026-10-12 — 160 087 байт при fileSize 57 065» | `projects/archivarius/TRIAGE.md` строка 997 | да (искалось «57 065») |
| «одна статья среднего размера (Thieme CME, PDF 1,5 МБ)» | `projects/archive-recon/LOG.md`, Т-1 | да (искалось «Thieme»); в Skill оставлено «статья среднего размера (PDF около 1,5 МБ)» — порядок величины, не особенность |
| «опись папки «ANTIBIOTIKA» скриптом archive_scan.py версии 1.0 … «FOLDERS THAT COULD NOT BE READ»» | `projects/archive-recon/LOG.md`, Т-3; `projects/archive-recon/tools/` | да (искалось «ANTIBIOTIKA», «FOLDERS THAT») |
| «запросами `parentId = '<папка INDEX>'` … `fullText contains 'SENTINEL'`» | случай проверки синтаксиса | носителя вне Skill нет — текст целиком в BASIS, «Случаи без адреса», пункт 8 |
| «строки шапки LAST_UPDATED, N8N_JOURNAL_2026» (E20) | `projects/archivarius/LOG.md` Р-8 (У-21, корпус N8N_JOURNAL_2026); `projects/n8n/INCIDENT_LOG.md` строка 36 | да (искалось «У-21», «occurrencesChanged:0»); в Skill осталось обобщённое «строки шапки документов, в том числе строка поля LAST_UPDATED» — LAST_UPDATED это общее поле шаблона документов, не особенность одного документа |
| «выгрузка листа 182 строки около 2026-07-23, строки 114, 146, 176; WB_REVIEWS_INDEX» | `projects/archivarius/TRIAGE.md` строка 174 (У-153) | да (искалось «У-153») |
| «(SYS_JOURNAL_2026, одно наблюдение; не перепроверено)» (ineligible) | `projects/archivarius/LOG.md` Р-12, У-57 | да (искалось «ineligible») |
| «прогон 73643, `projects/deklaration-ozon/LOG.md`, запись о создании CSV» | `projects/deklaration-ozon/LOG.md` Р-17 | да (искалось «73643») |
| «проверено 2026-09-17 документом REPORT_git-migration_2026-09-17 (блок T-108 …)» | `registry/documents.md` блок T-108 | да (искалось «T-108») |
| «исполнение 51779, 2026-08-30» (E21) | `projects/archivarius/LOG.md` Р-22, У-99 | да (искалось «51779») |
| «exec 67942 … exec 68199 … 38 299 Б» | `registry/tools.md` строка 22 | да (искалось «67942») |
| «(позиция AH-27 очереди)» | `registry/maintenance-queue.md`, `projects/n8n/INCIDENT_LOG.md` | да (искалось «AH-27») |
| «(SYS_JOURNAL_2026, 2026-09-08; задача `labs/sys/t-get-execution-context.md`)» | история задачи (закрыта коммитом 0173c22), `registry/maintenance-queue.md` строка 170, `meta/HARVEST_INPUT_2026-10-16.md` строка 356 | да — по истории git (`git log` по пути: 0173c22, 118bf61); живого файла задачи нет, адрес в BASIS дан через `git show 0173c22^:…` |
| «(наряды Н-26.08-03…06, 2026-08-27, … SYS_INDEX)» | `projects/archivarius/LOG.md` Р-22, У-98 | да (искалось «Н-26.08-03») |
| «(JOURNAL_incidents, захват Ж)» | корпус JOURNAL_INCIDENTS (Google Doc, ЗАМОРОЖЕН, `registry/documents.md` строка 53) | частично: корпус есть, «захват Ж» в репозитории поиском не найден; дописывать нечего — корпус заморожен, адрес в BASIS D.10.4 |
| «в сессии SYS (облачная среда Claude Code) … second-brain-git и second-brain-engineer» | — | носителя вне Skill нет — текст целиком в BASIS, «Случаи без адреса», пункт 17. Носитель не нужен как особенность: это наблюдение о среде, а не об объекте |

Дописывать в носители нечего: все проверенные носители факт держат. Единица без носителя (запросы проверки синтаксиса search_files, наблюдения о снимке `/mnt/skills/`) — это случаи, а не особенности объекта; их адрес — отчёт синтеза.
