projects/archive-recon/SERVER_TASKS.en.md

Task board for the Claude Code session on the owner's server (Hetzner; n8n and the OCR service run there). Written by the cloud session 2026-10-13, decision Р-32 of projects/archive-recon/LOG.md. Human-readable Russian plan: PLAN.md, section «Работа с книгами через сервер». On conflict PLAN.md wins.

Goal: full text of every page and PDF bookmarks (tables of contents) of the archive PDFs, searchable on the server, reachable from the cloud session through n8n. Test folder first: Google Drive folder "AA Beruf" (folder ID 100K6ANAOStQ19kQfT2RLt0Hw0wtn0o1r, 497 PDFs, about 5.6 GB, largest file about 790 MB). Main archive (about 70 GB) only after acceptance.

## Hard rules (all tasks)
- Google Drive access is READ-ONLY (rclone scope drive.readonly). Never write, move, rename or delete anything on Drive.
- Mirror, index and logs live OUTSIDE any git checkout: default /srv/archive/aa-beruf (mirror), /srv/archive/index (output). Repo is PUBLIC: never commit file paths of the archive, page texts, tables of contents, md5 lists with paths, keys, tokens, webhook URLs (rule И-7 of skills/second-brain-git/SKILL.md).
- Do not print key files or tokens into chat or logs.
- Do not disturb the running OCR service and n8n: run heavy jobs with `nice -n 10 ionice -c3`; one indexing process at a time.
- Before any change of n8n workflows read skills/n8n-engineering-manual/SKILL.md from this repo (mirror of the live Skill). New n8n workflows are permanent tools: never delete or archive them afterwards.
- Report numbers, not impressions. Each task ends with a filled "Report" block below (or, if you cannot push to the repo, the same text pasted to the owner, who brings it to the cloud session).

## S0 — environment check (read-only, no changes)
Report: OS; free disk on the partition for /srv (need about 7 GB now, about 80 GB for the main archive later); RAM; python3 version; whether PyMuPDF imports (`python3 -c "import pymupdf"`); SQLite FTS5 available (`python3 -c "import sqlite3;sqlite3.connect(':memory:').execute('create virtual table t using fts5(x)')"`); rclone installed and version; docker containers (names only); how the OCR service (container n8n-ocr) is built (Dockerfile/app path, framework, auth header name — not its value); whether a Google service-account JSON key file for n8n-liamin@decent-surf-488714-u4.iam.gserviceaccount.com already exists on disk (path only, never content). STOP after S0 if disk is insufficient.

## S1 — read-only mirror of "AA Beruf"
Preconditions done by the owner: (a) folder "AA Beruf" shared with n8n-liamin@decent-surf-488714-u4.iam.gserviceaccount.com as Viewer; (b) service-account JSON key placed on the server, chmod 600. If (b) is missing: tell the owner the exact steps (Google Cloud Console, project decent-surf-488714-u4, IAM, Service Accounts, n8n-liamin, Keys, Add key, JSON) and stop; fallback only if the owner says so: rclone OAuth with the owner's account, scope drive.readonly, via `rclone authorize "drive"` on the owner's PC.
Steps: rclone remote `aaberuf` (type drive, scope drive.readonly, service_account_file=<key>, root_folder_id=100K6ANAOStQ19kQfT2RLt0Hw0wtn0o1r). Dry run: `rclone lsf -R --files-only --include "*.{pdf,PDF}" aaberuf: | wc -l` — expect 497 (a few shortcuts may differ; report). Then `rclone sync aaberuf: /srv/archive/aa-beruf --include "*.{pdf,PDF}" --transfers 2 --checkers 4` and `rclone check aaberuf: /srv/archive/aa-beruf --include "*.{pdf,PDF}" --one-way` (md5 compared by Drive). Report: files and bytes copied, check differences, duration.

## S2 — build the index
Script: projects/archive-recon/tools/pdf_index.py of this repo (pull main first). `pip install pymupdf` if needed (venv preferred).
Run: `nice -n 10 ionice -c3 python3 tools/pdf_index.py build --root /srv/archive/aa-beruf --out /srv/archive/index`.
Smoke tests: `python3 tools/pdf_index.py search --out /srv/archive/index "tranexam*" --limit 5`, then "Hydrocortison", "Bauchlage", "Mitralklappe". Report: the content of index_report.json (counts only), runtime, peak memory if visible, the number of hits per smoke query (no texts), files with error (count and error class only).

## S3 — make the index reachable through n8n
Add read-only HTTP endpoints, preferably inside the existing OCR service (same auth as its other routes), reading /srv/archive/index:
- GET /archive/search?q=<FTS5 query>&limit=<1..100> -> [{md5, page, score, snippet}] (snippet ≤ 300 chars; no paths);
- GET /archive/page?md5=<md5>&page=<n> -> {md5, page, text} (one page);
- GET /archive/outlines -> outlines.json as stored (for the cloud session; contains paths — stays between server and n8n, never into the repo);
- GET /archive/status -> index_report.json.
Mount /srv/archive/index read-only into the container. Then three n8n workflows, webhook trigger "01_Webhook", POST body, respond with the endpoint JSON, credential = the one already used for the OCR service:
"ArchiveRecon Fulltext Search" {q, limit}; "ArchiveRecon Page Text" {md5, page}; "ArchiveRecon Outlines Read" {}. Test each once in manual mode. Report: workflow IDs, execution IDs of the tests, result sizes.

## S4 — later, not now
OCR of pages without text layer (list in outlines.json, notext_pages) through the existing OCR queue; nightly incremental `rclone sync` + `pdf_index.py build` (phase Ф6); main archive with its own remote and index folder (phase Ф5).

## Report
(Server session: append one block per task — date, task, status DONE/BLOCKED, numbers, open questions. Do not edit text above this heading.)
