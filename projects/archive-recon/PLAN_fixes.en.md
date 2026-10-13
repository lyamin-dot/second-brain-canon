projects/archive-recon/PLAN_fixes.en.md

Agent copy of PLAN.md section "План исправлений по критике 2026-10-13" (decision Р-31 LOG.md). On conflict PLAN.md wins. State 2026-10-13, search page v12 (artifact ARCHIVE_RECON_SEARCH, registry/documents.md).

Build: data.json = tools/build_data.py over inputs NOT in repo (data.json cut from page v10, book_old.json, books.json with TOCs, links.json Drive IDs, meta/out*.json model extraction, syn.json). Page = tools/search_page.html, publishes with data.json beside it. Recover inputs: Artifact read path data.json (current data incl. books, syn).

| # | defect | status |
|---|---|---|
| 1 | no file link | DONE: Drive ID for 497/497, title links to drive.google.com/file/d/ID/view |
| 2 | book content not searchable | PARTIAL: split books done (#3); TOC of 39 whole books DEFERRED by owner; needs PDFs (owner computer link or server); use PDF bookmarks, no OCR |
| 3 | 1 of 3 split books assembled | DONE by rule: ISBN running footer -> book; printed book page numbers in file text -> chapter (start=min page, end=start+pdf_pages-1). Books: Notfallsonografie 73 files, Echokardiografie 27, POCUS 14. "Checkliste Sonographie" (4 excerpts) not assembled: no TOC |
| 4 | no authors, 57% title=filename | DONE: model extraction; title=filename left 39, authors 331 |
| 5 | data inside HTML | DONE: data.json beside page |
| 6 | wrong types | DONE: chapter 118, other 26; guidelines untouched |
| 7 | personal papers in search | DONE: 45 hidden, text stripped from data |
| 8 | notes orphaned after PDF resave | DONE: reattach button by path/title |
| 9 | comment per book page | PARTIAL: per chapter file; whole books after #2 |
| 10 | subtitle vs data | DONE: computed, shows scan and build dates |
| 11 | dup tab, folder-status block | DONE: removed; dup report given to owner as file |
| 12 | synonyms in code | DONE: in data.json |

Open after test of v11: first-pages-only text (main defect, needs PDFs); PDF-metadata years flagged not fixed; "newer edition outside archive" notes from model knowledge, not checked on ERC/AHA/AWMF sites.

Next: (1) PDF access; (2) full text + bookmarks into search, whole-book TOCs; (3) Opus re-test; (4) main archive (phase Ф5).
