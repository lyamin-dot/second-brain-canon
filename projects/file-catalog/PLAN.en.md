projects/file-catalog/PLAN.en.md

# file-catalog — agent plan (compact). Human RU versions (PLAN.md, STAGES.md) = canon; this = execution copy, regenerate on change. 2026-10-21

GOAL priority: 1 doc content (articles, work orders, instructions vs junk) > 2 where-is-what > 3 safety (>=2 copies on distinct physical disks) + delete surplus dupes > 4 media identity > 5 collecting tools. Claude queries DB on owner's NL questions.
NON-GOALS: folder restructuring/renaming; media player; backup service.

INVARIANTS
I1 disks read-only unless owner confirms specific write/delete.
I2 NO deletion until all reachable media are scanned (R-5: a broken and an inaccessible medium cannot be scanned; reports say 'single copy among scanned media'). Delete only copies beyond 2 on distinct live physical disks; via _quarantine on same disk; only owner-confirmed list (logged).
I3 catalog data (names, paths, content, exports) NEVER to public repo second-brain-canon. Repo = plans/decisions/code w/o personal data.
I4 no dashboards/schedules/detectors before first disk scanned. Controller = gate role only.
I5 every stage ends with usable result.

ENV: Windows PC, 6 external disks (<=16 TB, mostly video, much audio, many docs, some old). Server Hetzner (Tesseract in n8n-ocr container) - cannot see disks. Cloud sandbox: no git push.
ARCH: Python scanner/hasher/text-extractor/classifier on Windows -> SQLite master DB (FTS5) in local project dir on internal drive. Claude Code on PC reads DB. Server replica = Stage 4 only on need.
TABLES v1: disks, files, scans, read_errors; later: hashes, doc_text, doc_labels, comments.

STAGES
S0 setup: 0.1 verify exec path (Claude Code on Windows OR remote-devices bridge) -> list mounted drives. 0.2 python+libs. 0.3 project dir internal drive. 0.4 schema from scratch 1 cmd. 0.5 owner: code location (private GH repo vs local). 0.6 test scan 1-2k files.
 ACCEPT: rowcount==Windows count; rerun idempotent; test dir mtime unchanged; answers "where is file named X".
 RETHINK P0.1 no exec path -> WSL or owner runs scripts. P0.2 AV blocks reads.
S1 inventory: 1.1 disk passport (volume serial, label, size, free, fs, approx year from owner). 1.2 oldest first. 1.3 read-only scan: path,name,ext,size,ctime,mtime; skip system dirs. 1.4 read errors logged, non-fatal, reported. 1.5 category by ext (doc,pdf,image,video,audio,ebook,archive,program,other). 1.6 summary per disk x category. 1.7 DB backup to an external disk.
 ACCEPT: 6 passports; counts match Windows (minus skipped); controller 20 random files located & confirmed; 5 real owner where-is questions answered.
 RETHINK P1.1 after disk1: >2h/disk or >5M files/disk -> change traversal. P1.2 old disk many read errors -> rescue copy before cataloging. P1.3 after all 6: doc count <~50k -> local full; >>100k -> filter + re-cost LLM. P1.4 many docs inside archives -> decide unpacking.
S2 dupes+safety: 2.1 funnel size->head+tail fingerprint->full hash (candidates). 2.2 docs/pdf: full hash all. 2.3 copies + distinct physical disks per content. 2.4 twin folders. 2.5 safety report: valuable single-copy by disk/age. 2.6 dupes report + reclaimable space. 2.7 deletion list (only >2 copies distinct disks) owner-confirmed. 2.8 move to _quarantine; delete after owner-set delay; DB updated.
 ACCEPT: 20 same-hash pairs byte-equal; every to-delete file has >=2 other copies on distinct disks (checked by query); zero deletes w/o logged confirmation.
 RETHINK P2.1 twin folders >50% dupe volume -> folder-level confirm. P2.2 much valuable single-copy on old disk -> copy first, delete waits. P2.3 full hash >1 day/disk -> video: size+head/tail, full hash only pre-delete. P2.4 owner won't confirm lists -> defer deletion.
S3 doc content (MAIN): 3.1 decide merge w/ archive-recon (P3.1). 3.2 unique docs, drop obvious junk (0 bytes, ~$*, system). 3.3 extract text by format (txt,rtf,doc,docx,odt,xls,xlsx,pdf text layer); encoding detect cp1251/cp866. 3.4 no-text PDF/images -> Tesseract rus+deu+eng; two texts per page (raw OCR + search text w/ hyphenation joined) as archive-recon. 3.5 PILOT 500 docs mixed years/formats: LLM labels type{article,order,instruction,letter,form,personal,draft,junk}, topic (archive-recon list, extensible), doc date, org, lang, 1-2 line summary, value{important,reference,junk}; measure cost+time. 3.6 controller checks 50 random. 3.7 full run only after pilot accepted. 3.8 FTS5 over text+summaries. 3.9 comments table via chat. 3.10 20 real owner questions run by controller (Opus).
 ACCEPT: type correct >=85% of 50; <=1 valuable labeled junk; >=17/20 questions found; every no-text doc has reason.
 RETHINK P3.1 merge if majority valuable docs = medical articles. P3.2 pilot below threshold -> change prompts/model/types; 2 rounds no convergence -> owner drops a label. P3.3 projected cost > owner budget -> stricter filter or cheap first pass. P3.4 scans >1/3 -> OCR on server. P3.5 <17/20 due to wording mismatch -> add vector search.
S4 remote access: START ONLY after owner >=3 times wanted search while PC off. 4.1 DB copy to server after each update. 4.2 read-only query tool (n8n workflow or MCP). 4.3 10 questions PC off >=9.
 RETHINK P4.1 replica lags -> move master to server.
S5 media: 5.1 video ffprobe+guessit+TMDB. 5.2 audio mutagen; untagged AcoustID/MusicBrainz. 5.3 photo EXIF. 5.4 ebook metadata. Order = owner. ACCEPT per type 30 sample >=90%.
 RETHINK P5.1 low film match -> Jellyfin as recognizer, read its DB. P5.2 >50% untagged audio -> worth it?
S6 collecting: plan after S5 (near-dupes, collection gaps, curated lists).

CONTROLLER: separate Opus session, not executor, no contact w/ executor. Input: project state file, own stage section, DB read access. Triggers ONLY: gate ("stage N ready") or owner command "контроль". Does: run acceptance via own queries/samples; check rethink points missed; check I1-I3; on "контроль" also: current stage, done since last log entry, stalled step + why. Verdict: принято | не принято (criterion + query) | переосмыслить (point + fact; owner decides). Writes ONE log entry. Nothing between calls.

KEY RETHINK MOMENTS: after all 6 disks; after 500-doc pilot.
