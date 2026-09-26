# google-drive-docs — rclone и credentials

Часть Skill google-drive-docs. Читать: перед работой с бэкапом и при отказе записи, похожем на проблему прав. Номера разделов — прежние, общие с SKILL.md.

## 5. RCLONE — бэкапы
PostgreSQL → Google Drive ежедневно, remote gdrive.
- apt-пакет rclone может быть собран без backend Mega — ставить официальным install-скриптом, зафиксировать версию.
- Shared client_id rclone планово выводится Google из обращения — использовать собственный client_id для gdrive-remote, иначе бэкапы молча остановятся. Проверка: `rclone config show <remote>:` — пустые client_id/client_secret означают использование общего client_id (под угрозой); заполненные значения или service account — не касается.

## 6. CREDENTIALS И ПУТИ ЗАПИСИ

### 6.1 Два независимых пути
- MCP-коннектор Google Drive (claude.ai): чтение метаданных / create_file / get_file_metadata. Авторизация — OAuth на стороне claude.ai, может протухать (см. E14 в §8) — лечится переподключением коннектора и новым чатом.
- n8n-вебхуки (append/replace/overwrite/gdocs-read): авторизация — Service Account (тип credential googleApi), не OAuth. SA-ключи не протухают по времени.
Это разные, независимые токены: один путь может лежать при полностью рабочем втором — при проблемах сначала определить, какой именно путь отказал.

### 6.2 Правила Service Account
Файл, не расшаренный на SA, даёт тихие отказы: 404 (overwrite) / 403 (replace) — не похожи на auth error, легко спутать с опечаткой fileId.
(а) При тихом неприменении записи — первым делом проверить get_file_permissions (SA должен быть в writers), не переавторизацию.
(б) Верификация — только read-back; `executionId: 'started'` не гарантия успеха.
(в) Новые файлы вне уже расшаренных папок — проверять доступ SA ДО первой записи.
(г) При нескольких write-узлах в одном воркфлоу мигрировать credential на ВСЕХ узлах одним update_workflow — частичная миграция даёт частичный молчаливый отказ.
(д) trash/delete через Drive API под SA возвращает HTTP 200 без реального эффекта (нужна роль owner) — только под credential владельца, с проверкой чтением после.
Credential в кэше «does not exist» → переключить на другой и вернуть обратно → Save → Publish.
