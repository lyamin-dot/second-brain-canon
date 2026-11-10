projects/content/PLAN.en.md

Agent copy of the autopilot contract in `projects/content/PLAN.md` (pair file: edit both in one commit). Human version (Russian) is authoritative on conflict -> stop and ask Andrei. Always reply/write user-facing text in Russian.

# CONTENT autopilot — run brief

GOAL: approvable reference set: 4 SKUs x 8 slides PNG 1200x1600 + copy + bg prompts, no Andrei involvement.
SKUs: 1340 (cooling-system sealant), 1342 (Engine Flush), 1750 (windshield cleaner Cherry), 1709 (marten/rodent spray). Demand list of 23: see PLAN.md item 7.
Brand DNA, grid, slide structure: PLAN.md sections "Что сохранено" and "Структура 8 слайдов" — read them, do not restate from memory.

## Every package starts with
1. Load Skills (Skill tool) whose description fits: second-brain-git, second-brain-engineer, avtopilot; plus google-drive-docs if touching Drive/Docs/Sheets.
2. `git clone` lyamin-dot/second-brain-canon (public, anonymous); read `meta/PENDING_RULES.md`, `projects/content/STATE.md`, `projects/content/PLAN.md`, this file.
3. GATE: STATE.md must show `С<N-1>: ГОТОВО` (С1 has no gate). Missing -> write to STATE.md `С<N>: ЗАБЛОКИРОВАНО — <reason>` and stop.
4. Writing to repo: if `git push --dry-run` passes -> commit to main directly (fetch+rebase first); else Канал (n8n Git Write / Git Append File / Git Commit Files, IDs in registry/tools.md); else stop as blocked. Prove every write by re-read (blob sha).
5. Never: write to WB/Ozon cabinets, change any n8n workflow, delete anything, draw the Liqui Moly logo (use neutral "ЛОГО" box), spawn subagents, put PNGs or personal data into the repo. Any product claim needs a source address.

## С1 Facts (output `projects/content/FACTS.md`, then STATE `С1: ГОТОВО <date> <sha7 of FACTS.md>`)
- gsheets-read (workflow ID: registry/n8n-map.md, name "Claude → Google Sheets Read", trigger 01_Webhook) book 1sPD5SAFCTygzUaEPg8RKRPHQyc0HCMIK-aMpnXqYu3k, sheet `kb_auto_chemistry`: header row + rows for the 4 SKUs (full) and the 23 demand SKUs (article, name, type, volume, purpose, application_area). Record sheet+row address for every value.
- Verify hypotheses Г1–Г4 (PLAN.md) by PRIMARY sources only (WB seller help/rules on media & infographics; Ozon seller docs on images; Честный знак official site / government decree for automotive chemicals & cosmetics marking timeline; image size requirements). WebSearch "standard", escalate "extended" if thin. Each verdict: confirmed / refuted / unclear + URL + read date. Secondary articles = hypothesis only.
- FACTS.md sections: Data (per SKU), Platform rules (Г1–Г4 verdicts), Implications for slides (one line each).

## С2 Copy (output `projects/content/etalon/<art>.md` x4 + one Google Doc; STATE `С2: ГОТОВО`)
- Per SKU (format of the Project master prompt): Product Insight; 8 slides — goal, H1 (3–7 words), subline (<=2 lines), body blocks (1 idea = 1 block), icons, badge flags; every factual claim tagged `[src: kb_auto_chemistry!row N col X]` or `[src: URL, date]`; untraceable claim -> drop it. Designer brief; 3 background prompts (scene+product+angle+light+materials+style+palette+quality+limits; product packaging kept unchanged).
- Respect FACTS.md platform verdicts (no forbidden wording) — the section "Обновление вердиктов Г1 и Г3" at the end of FACTS.md overrides earlier ones: no separate Liqui Moly logo plaque, badge text "Официальный продавец" without the word "гарантия", cover slide = product large, minimal text. Brand spelling: Liqui Moly.
- Starting draft: `projects/content/etalon/_draft_2026-06-27_T2_chat.md` (June chat output, unverified). Reuse its structure/ideas; every claim must get a source or be dropped; its palette and the 01.07.2026 ЧЗ date are wrong — follow PLAN.md and FACTS.md.
- 1709 source (absent in kb_auto_chemistry): own WB card nmID 391706057 (cabinet kiparis_wb) in DB mkt2. Read via n8n workflow "MKT2 SQL Read" ID XP6mOTq6EJ3Mjxav, trigger 01_SQL_Text, inputs {chatInput: "<SQL>"}, result node 02_SQL_Read_As_Reader; table raw.wb_card, columns cabinet_code, payload (jsonb: description, characteristics, title, vendorCode, nmID), last_loaded_at (current version = max last_loaded_at). Tag such claims `[src: wb_card 391706057 <field>]`; seller text → only purpose, how to apply, volume; no effect promises. Same source may confirm/complete the other three (nmIDs 1340→257044108, 1342→258487785, 1750→563129033).
- Human Doc: create_file text/html into Drive folder "эталон-2026-11" (ID registry/documents.md, row CONTENT_ETALON_FOLDER); register in registry/documents.md; verify by gdocs-read (no raw tags).

## С3 Template + render (code in `projects/content/render/`; STATE `С3: ГОТОВО`)
- npm: @fontsource/montserrat (cyrillic 400/600/800, also latin), lucide-static. Python playwright, executable_path /usr/bin/google-chrome, args --no-sandbox, viewport 1200x1600.
- One parametric template set (8 slide types) fed from a JSON per SKU built from etalon/<art>.md. Backgrounds in CSS only (gradients/geometry/light), palette per PLAN.md.
- Photos: download the ZIP (registry/documents.md row CONTENT_PHOTOS_ZIP) with download_file_content — output > limit lands in a file under /tmp/claude-tool-results/; decode the longest base64 run with python, unzip, check each member size and 900x1200. NEVER download single small images (they arrive inline as base64 and get corrupted). Use: 1340 -> 1340_1_wb257044108-2.webp (Russian label; the _alt_ file has a foreign label, do not use), 1342_1_…, 1709_1_…, 1750_1_…. White background: cut out (flood-fill near-white from the borders, soft edge) for dark slides; check the cutout by looking at it. If a newer ZIP or extra files appear, prefer files starting with the article. Missing -> grey silhouette "фото товара".
- Render 32 PNG. Check script per slide: exact size; min computed font-size of visible text >= 28px; nothing inside 48px margins except backgrounds; palette colors used <= 3 (ignore photo). Then LOOK at every PNG (Read tool) and fix overflow/clipping/contrast; record a per-slide verdict table in `render/REPORT.md`.
- Publish gallery: Artifact publish_files (index.html + PNGs from disk), private. No artifact tool -> SendUserFile the PNGs and note it in STATE.
- STATE: gallery URL/slug, report sha7.

## Close each package
STATE.md: only next step / blockers / open questions (contract meta/CONTRACT_state-content.md). LOG.md: one Р-entry per real decision (form: second-brain-git "Форма записи в журнал"). Run `python3 meta/scripts/state_split.py check projects/content/STATE.md`.

## Н-10.11-04 Ozon main-photo audit (READ-ONLY; Russian section «Контракт автопилота Н-10.11-04» in PLAN.md is authoritative)
- Run in Claude Code on Andrei's computer (Ozon CDN is blocked from cloud sessions).
- К1: MKT2 SQL Read (same call as С2 above). raw.ozon_product, cabinet_code in (ip_ozon, kiparis_ozon), current version per product_id (max last_loaded_at). Extract offer_id, sku, product_id, payload primary_image, images, first-version date, archived/visible flags. Join first WB photo of the same article: raw.wb_card current version, payload photos[0] (big size URL), via ref.v_article_item. Check: row count == SQL count(distinct product_id) per cabinet; sku 5895406668 present. One cabinet missing -> STOP, report, no Ozon API workaround.
- К2: Python + Pillow, download each image into memory only (never save images to repo), record width, height, ratio w/h, white-border flag (10 px strip, all channels >= 235). Positive control: sku 5895406668 main photo == 535x1600. measured + failed == К1 rows; failed > 10% -> STOP. Output projects/content/photo-audit/photo_audit.csv (one row per Ozon card).
- К3: classes: norm = 0.70 <= w/h <= 0.80 and min side >= 900; off_with_wb = off-norm and WB photo in norm; off_human = otherwise. Harm: if mkt2 has Ozon search funnel per card (impressions -> card visits) for 2026-10-01..2026-11-09, compare median visit share off vs norm within each cabinet; else "не измерено" + where searched. Origin: off-norm grouped by cabinet and first-version date (hypothesis, unverified: came with the 2026-11-05 card copy into Ozon ИП). Output projects/content/photo-audit/REPORT.md in Russian, incl. section «Находки вне рамки». Independent acceptor refutes the report against CSV and DB.
- К4: one Р-entry in projects/content/LOG.md. К5: one line in projects/content/STATE.md + state_split.py check.
- Forbidden: writes to Ozon/WB cabinets, any n8n workflow edit/publish, paths outside projects/content/.
