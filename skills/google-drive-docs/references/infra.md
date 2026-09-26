# google-drive-docs — rclone и credentials

Часть Skill google-drive-docs. Читать: перед работой с бэкапом и при отказе записи, похожем на проблему прав. Номера разделов — прежние, общие с SKILL.md.

## 5. RCLONE — бэкапы
PostgreSQL → Google Drive ежедневно, remote gdrive.
- apt-пакет rclone может быть собран без backend Mega — ставить официальным install-скриптом, зафиксировать версию.
- Shared client_id rclone планово выводится Google из обращения — использовать собственный client_id для gdrive-remote, иначе бэкапы молча остановятся. Проверка: `rclone config show <remote>:` — пустые client_id/client_secret означают использование общего client_id (под угрозой); заполненные значения или service account — не касается.

## 6. CREDENTIALS И ПУТИ ЗАПИСИ

### 6.1 Два независимых пути
- MCP-коннектор Google Drive (claude.ai), от имени владельца: search_files, get_file_metadata, create_file, update_file, copy_file, trash_file, get_file_permissions, share_file, download_file_content, read_file_content (последний — только по §0 п.2). Авторизация — OAuth на стороне claude.ai, может протухать (см. E14 в §8) — лечится переподключением коннектора и новым чатом.
- n8n-вебхуки (append/replace/overwrite/gdocs-read/gdocs-apply-from-file/gsheets-read): авторизация — Service Account (тип credential googleApi), не OAuth. SA-ключи не протухают по времени. Исключение — create_folder (`uapccJY1O4ykyDi7`): по снимку registry/n8n-map.md 2026-09-26 его узел Drive работает на credential googleDriveOAuth2Api, то есть от имени владельца через OAuth, и при отказе искать надо протухший OAuth, а не доступ SA.
Это разные, независимые токены: один путь может лежать при полностью рабочем втором — при проблемах сначала определить, какой именно путь отказал.

### 6.2 Правила Service Account
Файл, не расшаренный на SA, даёт тихие отказы: 404 (overwrite) / 403 (replace) — не похожи на auth error, легко спутать с опечаткой fileId.
(а) При тихом неприменении записи — первым делом проверить get_file_permissions (SA должен быть в writers), не переавторизацию.
(б) Верификация — только read-back; `executionId: 'started'` не гарантия успеха.
(в) Новые файлы вне уже расшаренных папок — проверять доступ SA ДО первой записи.
(г) При нескольких write-узлах в одном воркфлоу мигрировать credential на ВСЕХ узлах одним update_workflow — частичная миграция даёт частичный молчаливый отказ.
(д) trash/delete через Drive API под SA возвращает HTTP 200 без реального эффекта (нужна роль owner) — только под credential владельца, с проверкой чтением после. Инструмент коннектора trash_file работает от имени владельца и под это ограничение не попадает; им же `second-brain-git` 8.3 убирает файл-источник Git Append File из папки _git_staging.
Credential в кэше «does not exist» → переключить на другой и вернуть обратно → Save → Publish.
