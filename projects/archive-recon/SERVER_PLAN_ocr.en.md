projects/archive-recon/SERVER_PLAN_ocr.en.md

# ARCHIVE OCR PLAN ON THE SERVER (agent copy) — 2026-10-21
Status: ACCEPTED by Andrei 2026-10-21 12:09 (container instead of host — replaces his 2026-10-16 decision "run on host for this stage"; code changes only by Andrei's command; drive-reader stays Editor on `AA Beruf`). archive-recon session accepted the design with additions below. Author: server agent (Claude Project «01_Развитие сервера»; its canon is Google Doc SERVER_INDEX). Human copy: SERVER_PLAN_ocr.md; on conflict this English copy wins. No server paths, addresses or IDs here (public repo); they live in the server snapshot in the server Project files. Origin: denken level-3 revision 2026-10-21.
Scope: 40 files of Drive folder `Telegram` (~5.3 GB; scans without layer, scans with partial layer, PDFs with layer and figures).

## DESIGN
- New compose service `archive`: python, PyMuPDF (bookmarks/ToC, page labels; tools/pdf_index.py uses it), tesseract (eng, deu, rus, osd), poppler-utils, rclone, sqlite. Non-root, no docker socket, no host access. Mounts: archive folder rw; drive-reader key folder ro. Limits 1.5 CPU / 1.5G (host 8 GB, no swap). Own network shared only with n8n (no Postgres/Vaultwarden reach). No published port. n8n also listed in that network in compose.
- Long-running loop (restart unless-stopped), resumable: next queued file (priority order) -> rclone copyto + md5 vs Drive -> language: first 3 pages OCR'd eng+deu+rus, then the combination with best confidence -> OCR EVERY page at the book's dpi (default 200) -> layer text if present -> index -> delete download -> queue status.
- Per page THREE texts: layer as is; OCR as is; OCR search text with hyphen joins in place. Every search hit carries its source (layer, ocr, both). Search text rebuildable from raw without re-OCR. Book 1 rebuilt; old index kept as copy.
- Join rule parameters: keep hyphen if second part starts uppercase (default yes), min letters each side (default 2).
- dpi: 200 for mass run; archive-recon decides 300 for illustrated books after its measurement on book 1.
- Why OCR all pages: garbage layers (book 1: 1202 control chars, hidden Russian text) and missing figure labels (book 1 pp. 103-104). ~1.5 days machine time [U].
- Why own tesseract, not the shared OCR service: its queue/503/413 code untested live; per-page calls would re-upload the whole file per page.

## CHANNELS
- Internal addresses (archive network only): http://archive:8080/status, /search, /page, /control/... .
- n8n tool workflows "search", "status and page", "control". Control: per book requeue, skip, enqueue, priority, language, dpi; default dpi; rebuild search text for all books; join-rule parameters; pause/resume. Whitelist: language only eng/deu/rus joined by "+", dpi integer 150-400, else rejected (values reach the OCR command line). No code execution via control. Created by server agent after Andrei's yes.
- Code: only by Andrei's command (fetch by commit, sha256 check, restart `archive`). Frozen during mass run.
- Notification: Andrei's personal Telegram chat already used by active workflows. Proposed: n8n workflow polls /status hourly, messages only on stop or finish (no new inbound endpoint; n8n webhooks are internet-reachable via Caddy). If archive-recon insists on script-initiated call: webhook with header secret kept only on the server. Awaiting archive-recon.
- Acceptance launch: archive-recon's own delayed message at estimated run end.

## STEPS
1 DONE 2026-10-21 Andrei read-only survey (compose, networks, disk, uid, key files) matched snapshot. 2 Server agent: code in tools/; test in own workspace on a scan and a layered PDF with figures. 3 Andrei: compose backup, service+network, n8n listed, code by commit with sha check, build, up -d archive only, docker network connect n8n; check status from n8n container -> empty queue. 4 Server agent: tool workflows after yes. 5 Test phase: book 1 ("contralateral" -> p.251, snippets without glued tail) + one scan without layer. 6 Mass run 40 files. 7 Independent Opus acceptor: ToC questions from 3 random books, hit confirmed by chapter heading; page-number fallback: PDF page labels, else offset from one chapter (book 1 offset 19); pass 4/5 per book in top 5. 8 Server agent: report, snapshot edit, journals.

## STOPS
Free < 20 GiB pause; 3 books failed in a row; 5 code versions without success in test phase; acceptance below pass; any change to existing workflows, other compose services, or Drive writes.

## REJECTED
Auto-pull of code (Editor key could write to Drive; repo written by many sessions would become a code-execution channel; no saving: slower than Andrei's command in test phase, code frozen in mass run); separate host user + cron + venv; shared OCR service; page classifier.

## VERDICT
Solution exists, partly degenerate: run needs no Andrei, code changes need one command per version. Owner barrier "drive-reader stays Editor" not lifted — that is the price.
