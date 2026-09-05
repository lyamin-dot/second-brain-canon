<!-- T-109 | CORE байт 102168-102654 | Хвост файла: GDOCS_APPLY_FROM_FILE (fdiWemSCln1WA8gt) + TEST_GDOCS_APPLY -->
GDOCS_APPLY_FROM_FILE: fdiWemSCln1WA8gt, воркфлоу gdocs-apply-from-file, паспорт 1KBJep9gNjWTxtgtxStyIRiO4odgsJsQ_A9UfCeTwdFM, режимы append/overwrite/replace, потолок 1500000 символов одним batchUpdate, наряд Н-26.08-03
TEST_GDOCS_APPLY: 1bMsJ3eSG5K4i_2cogRiSvirnH73K8031uv8-fZ-df4A, регрессионная мишень воркфлоу gdocs-apply-from-file, состояние на 2026-08-26: byteLength 174326, checkSum cf15650f

## Инструменты n8n для git [источник: PLAN_git-migration §5; раздел 5 источника]

git-read: webhook POST `{path, ref?}` → GitHub Contents API GET → `{text, sha, byteLength, encoding}`; SHA блоба — родная контрольная сумма, FNV-протез не нужен.
git-write: webhook POST `{path, newText, expectedSha, message}` → сверка `expectedSha` с текущим SHA (несовпадение — отказ с явной причиной, класс Т-05 закрыт архитектурно) → PUT → `{newSha, commitSha}`. Верификация — независимый git-read по пути, сверка SHA.
канал на Git Data API есть, воркфлоу 7OQh206m8xrZAzPF (git-commit), покрывает мультифайловый коммит и delete через sha:null в blob-записи.  Непокрытая операция — повод остановиться и назвать её, а не обходить канал прямым git: push из облачной песочницы сессии закрыт прокси (чтение разрешено, запись нет), и это граница платформы, а не поломка. До появления канала на Git Data API (blobs → tree с `sha:null` на удаление → commit → обновление refs/heads/main, `force:false`) удаление выполняет владелец вручную через веб-интерфейс GitHub.
git-log: webhook POST `{path?, limit}` → список коммитов `{sha, date, message}`.
git-diff — вторая очередь, не пилот: сравнение двух ref по файлу, для приёмки правок по diff строк.
Git Append | M7u4VX4Y4KtYyoVV | дозапись в LOG.md, вход {path, text}, принят Н-05.09-03 exec 55695
Действующие ID (подтверждено этой сессией прямым вызовом 2026-09-03, get_workflow_details, оба `active:true`): git-read `72DWYjGbeAxEgYwj`, git-write `Omt9oDYf7NthOw5T`.
