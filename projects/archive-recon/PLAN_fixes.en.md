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

## Book assembly algorithm (split books; PLAN.md section "Метод: как книга…", code tools/build_data.py)

Never use file names (they lie: "5.1" = chapter 7). Use printed book page numbers.
1 Book: running footer "Surname, Title (ISBN …)" in first-pages text; same ISBN = same book (Thieme prints it on every page; other publishers: re-verify).
2 TOC: read front-matter file fully (Drive read_file_content on PDF, or local script) -> chapters [num, title, first page]; last text page = Sachverzeichnis/Literatur.
3 File span: collect printed page numbers next to footer (regex PAGE): start = min, end = start + pdf_pages - 1.
4 Chapter = last chapter with first_page <= start; if end >= next chapter start -> spans "Kap. a–b".
5 No page numbers or start < chapter 1 -> front matter. Same span -> likely copy. Span inside longer file -> "contained in".
6 Coverage per chapter: covered pages / (next chapter start - this start); chapter without own files but covered by previous file -> "start of chapter in file X".
7 Verify on first use per book/publisher: first TOC heading found in file text must be in the same chapter (Notfallsonografie: 73/73 match).
Fallback without page numbers: TOC section headings in first-pages text (Р-28), weaker.
Out of scope: no PDF merge/rename; TOC text not in public repo; whole-file books -> PDF bookmarks (deferred).
