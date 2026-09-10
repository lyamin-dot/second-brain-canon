<!-- T-109 | CORE байт 102168-102654 | Хвост файла: GDOCS_APPLY_FROM_FILE (fdiWemSCln1WA8gt) + TEST_GDOCS_APPLY -->
GDOCS_APPLY_FROM_FILE: fdiWemSCln1WA8gt, воркфлоу gdocs-apply-from-file, паспорт 1KBJep9gNjWTxtgtxStyIRiO4odgsJsQ_A9UfCeTwdFM, режимы append/overwrite/replace, потолок 1500000 символов одним batchUpdate, наряд Н-26.08-03
TEST_GDOCS_APPLY: 1bMsJ3eSG5K4i_2cogRiSvirnH73K8031uv8-fZ-df4A, регрессионная мишень воркфлоу gdocs-apply-from-file, состояние на 2026-08-26: byteLength 174326, checkSum cf15650f

## Инструменты n8n для git [источник: PLAN_git-migration §5; раздел 5 источника]

git-read: webhook POST `{path, ref?}` → GitHub Contents API GET → `{text, sha, byteLength, encoding}`; SHA блоба — родная контрольная сумма, FNV-протез не нужен.
git-write: webhook POST `{path, newText, expectedSha, message}` → сверка `expectedSha` с текущим SHA (несовпадение — отказ с явной причиной, класс Т-05 закрыт архитектурно) → PUT → `{newSha, commitSha}`. Верификация — независимый git-read по пути, сверка SHA.
git-commit: воркфлоу 7OQh206m8xrZAzPF, webhook `{branch, message, expectedSha, files[], deletes[]}` -> Git Data API (blobs -> tree -> commit -> обновление refs/heads/main, force:false). Покрывает мультифайловый коммит и удаление путей через `deletes[]` (Р-43 журнала git-migration, 2026-09-06). Паспорт 1cw8g7TS84v6qggNU-Su_zIhvoKwJywG-Z1PJ-eGT_Jk.
ДВА РАЗНЫХ КАНАЛА, НЕ ПУТАТЬ (правка 2026-09-07, разбор протокола «обслуживание»):
— прямой `git push` из облачной песочницы сессии закрыт прокси: чтение репозитория открыто, запись нет. Это граница платформы, чинить нечего, обход искать не нужно;
— канал записи — перечисленные здесь воркфлоу. Они вызываются по HTTP, PUT выполняет сервер n8n, а не песочница, поэтому канал работает из любой среды: Claude Project, Cowork, Claude Code. Формулировка «писать из этой среды нельзя» относится только к прямому push и никогда — к каналу.
Непокрытая каналом операция — повод остановиться и назвать её, а не обходить прямым git (`second-brain-git` §6a).
git-log: воркфлоу `ZXTQwjUkd81wyRoI`, webhook POST `{path?, limit}` → `{success, count, commits:[{sha, message, author, date, url}]}`; узел результата `04_Build_Response`. Проверено прямым вызовом 2026-09-09 по пути `core/MANIFEST.md`.
git-diff — вторая очередь, не пилот: сравнение двух ref по файлу, для приёмки правок по diff строк.
Git Append | M7u4VX4Y4KtYyoVV | дозапись в LOG.md, вход {path, text}, принят Н-05.09-03 exec 55695
Действующие ID (подтверждено этой сессией прямым вызовом 2026-09-03, get_workflow_details, оба `active:true`): git-read `72DWYjGbeAxEgYwj`, git-write `Omt9oDYf7NthOw5T`.

git-read-batch: workflow uUwqH9RPjMfoax9M, паспорт 1BkFlDbTv4CwhTkm4Y_HJRraMLtcuzRhLx4TxSNXXH34; вход POST {paths:[...]} (плоский список путей репозитория lyamin-dot/second-brain-canon, без разбора манифеста, без ref) -> {requested, returned, files:[{path,text,sha,byteLength}], missing:[{path,reason}]}, requested и returned считаются независимо друг от друга; 2026-09-08, наряд Н-08.09-01.
Правило выбора: git-read — для одиночного чтения одного пути; git-read-batch — для набора путей за одно исполнение.

Git Grep | 4RsgY1vhL3C72vp8 | вход POST {path, pattern, limit?}, выход {path, sha, pattern, count, matches:[{line,text}]}; один файл за вызов; pattern — регулярное выражение JS (`new RegExp(pattern)` рантайм-строкой, литералов regex в коде нода нет — исключён баг SDK на \s\S\d\w из n8n-engineering-manual §4.7); count — общее число совпавших строк, matches — не более limit (default 20), text каждой строки обрезан до 200 символов; ошибка транспорта (в т.ч. «Credentials not found») отделена от GitHub-404 полем reason. GitHub Contents API GET, credential githubApi (та же, что у git-read/git-write/Git Append). Опубликован (active). Зонд наряда Н-09.09-10: exec 58953 — path=projects/git-migration/LOG_ARCHIVE.md, pattern="Р-33 \|" → count=1, matches[0]={line:170, text начинается с "Р-33 | "}, тело ответа 715 Б (< 2048 Б); exec 58958 — заведомо отсутствующий паттерн → count=0, success=true, reason=null, без ошибки.
