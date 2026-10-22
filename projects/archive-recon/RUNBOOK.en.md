projects/archive-recon/RUNBOOK.en.md

# ARCHIVE OCR + SEARCH — AGENT RUNBOOK (wins over RUNBOOK.md on conflict)
Decision: LOG.md Р-39 (2026-10-21). Design: SERVER_PLAN_ocr.en.md. Interface: tools/archive-worker/README.md. Public repo: never write server paths, n8n webhook paths, Telegram chat id, page texts, ToC texts (rule И-7 second-brain-git).

## SYSTEM
- Container `archive` (server), long-running, own network with n8n only, no published port. Reads Drive folder `Telegram` (rclone drive.readonly); key has Editor role on `AA Beruf` -> NEVER add code paths that write Drive.
- Per page 3 texts: `layer` (as is), `ocr` (as is), `ocr_search` (hyphen joins in place). FTS over layer + ocr_search; each hit has source layer|ocr|both.
- Book status: queued -> working -> done | error | skipped. Pause: free < 20 GiB, or 3 consecutive book errors.
- Endpoints (inside network only): GET /health, /status, /search?q&limit&book, /page?book&page, /toc?book; POST /control/{pause|resume|rescan|rebuild_search|settings|book}. Whitelist: lang in {eng,deu,rus} joined by "+", or null=auto; dpi int 150..400 or null; settings {default_dpi 150..400, keep_upper_hyphen bool, min_letters 1..5}; book op in {requeue,enqueue,skip,priority 0..1000,lang,dpi}. Else 400.
- Cloud sessions reach endpoints ONLY via n8n tool workflows (built by server agent; passport SERVER_WF_archive-tools; do not edit them — server agent's zone):
  - "Archive Search" 3ARodiEgXWs4DGmx: body {q, limit 1..50, book?}.
  - "Archive Read Status Page" Ta4fU7QI1QRb32tB: body {action: status|page|toc, book?, page?}.
  - "Archive Control" Hp0LJ5u37A0UgB41: body {action: pause|resume|rescan|rebuild_search|settings|book, payload}; whitelist checked in n8n before the container.
  Call: execute_workflow, executionMode manual, triggerNodeName "01_Webhook", inputs {webhookData: {method: "POST", body: {...}}} (manual mode needs no auth header). Result: get_execution includeData:true, nodeNames [the second node: 02_Archive_Search / 02_Archive_Read]. Last node is httpRequest -> raw response also sits in contextData, nodeNames does not cut it: status costs about twice its size (~25 KB at 39 books).
  - Status field `error` of a DONE book holds language-detection notes, not an error (fixed in code 1.1). Error = book status `error` only.
  Verified 2026-10-21: executions 83853 (status), 83854 (search) — LOG Р-40.

## WHO
- Container: all mechanical work. No LLM.
- n8n notify workflow: polls /status hourly, Telegram to Andrei only on pause or queue finished.
- archive-recon session (you): search answers, error triage, parameter changes via control, acceptance, canon writes (LOG/STATE/PLAN/RUNBOOK of this project).
- Server agent (Claude Project «01_Развитие сервера»): container, compose, n8n tool workflows, code deploy commands. Its canon: Google Doc SERVER_INDEX.
- Andrei: runs code-update command; answers stops.

## PROCEDURES
P1 search: call "search" {q, limit<=20}. Query = plain words, implicit AND; no OR/NOT/NEAR (stripped). Code 1.0 (deployed until Andrei installs 1.1): `*` and quotes are IGNORED -> exact word forms only; Russian inflection misses (эластография vs эластографии): try several word forms. Code 1.1: `word*` prefix (stem >=3 letters) and "a b" phrase work. Version: status field `version`. Report book, pdf page, printed label, source, snippet. Full page -> "status and page". Do not paste long page texts into the repo.
P2 error triage (book status error or pause by 3 errors): read /status error text. Wrong language -> control book lang; garbage OCR on small print -> dpi 300; corrupt file -> skip + note in LOG.md. Then control resume. Max 2 retries per book, then skip and record.
P3 rejoin rule change: control settings, then rebuild_search (no re-OCR). Record in LOG.md.
P4 code change: write code in tools/archive-worker/, commit, give Andrei commit + sha256 via server agent. Never during mass run unless a stop requires it. Code must keep: no Drive writes, whitelist, no new inbound endpoints.
P5 acceptance (after queue finished; triggered by own delayed message): spawn independent Opus subagent (did not do the work), READ-ONLY. Input: 3 books = 1 eng, 1 rus, 1 scan with partial layer (layer_pages < pages); + 1 deu if any deu book exists (LOG Р-40 p.4), via /toc pick 5 chapter/section titles per book, convert to questions NOT copying exact title wording where avoidable; expected page = chapter start; hit = expected page in top 5 AND chapter heading present on found page (/page); fallback page mapping: printed label, else offset from one chapter. Pass: >=4/5 per book. Acceptor gets claims to refute, not workers' reports. Below pass -> stop, report to Andrei with cause. Only then: 200 vs 300 dpi measurement if misses are figure captions.
P6 report to Andrei: problem, cause, what was done, what he must do. No step retelling.

## STOPS (message Andrei with prepared decision, do not wait silently)
Manual step of Andrei missing; irreversible choice that could go both ways; goal or subject change; edit outside allowed list (existing n8n workflows, other compose services, Drive writes, Skills, master prompts); 2 edit rounds without convergence; acceptance below pass; container paused for disk.

## ALLOWED WITHOUT NEW "YES"
Control calls within whitelist; canon writes in projects/archive-recon/ (LOG append, STATE, PLAN, RUNBOOK); code commits in tools/archive-worker/ (deploy still needs Andrei).
