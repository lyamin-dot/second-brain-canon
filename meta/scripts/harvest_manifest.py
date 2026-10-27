#!/usr/bin/env python3
"""Harvest input manifest: what a harvest MUST read, derived from registries and
git history, not from the session's memory (meta/PROTOCOL_harvest.md, steps 1 and 1b).

Usage: python3 harvest_manifest.py <clone path> <last harvest date YYYY-MM-DD>
Output: JSON on stdout. Google Docs modification dates are not known to the script:
the session takes them (get_file_metadata) for the docs_candidates list.
Note: the first commit tried to keep the file ASCII-only (Cyrillic as backslash-u escapes);
the Git channel decoded the escapes into real Cyrillic letters. Behaviour is identical.
History: 2026-10-18 first run; fix same day - journal records "T-N | date |" without status field.
"""
import json, re, subprocess, sys, os

repo, since = sys.argv[1], sys.argv[2]

def git(*a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, check=True).stdout

def read(p):
    with open(os.path.join(repo, p), encoding="utf-8") as f:
        return f.read()

proto = read("meta/PROTOCOL_harvest.md")
m = re.search(r"^последний харвест:\s*(\S+)", proto, re.M)
proto_last = m.group(1) if m else None
m = re.search(r"^прочитаны после заморозки[^\n]*", proto, re.M)
frozen_read_line = m.group(0) if m else ""

# --- step 1: experience documents in Google Docs ---
docs = []
for ln in read("registry/documents.md").splitlines():
    # The parenthesis before the colon may itself contain parentheses (PROJECT_LOG_SYS),
    # so it is matched greedily up to the last ")" that is followed by ": <id>".
    mm = re.match(r"^([A-Za-z0-9_]+)(\s*\(.*\))?\s*:\s*(\S+)(.*)$", ln)
    if not mm:
        continue
    name, did, rest = mm.group(1), mm.group(3).rstrip(",;."), (mm.group(2) or "") + mm.group(4)
    if not re.search(r"INDEX|JOURNAL|LOG", name):
        continue
    low = (rest or "").lower()
    excluded = None
    if "FOLDER" in name or low.lstrip(" —-").startswith("папк"):
        excluded = "папка"
    elif "sheets" in low[:80] or "таблиц" in low[:40]:
        excluded = "таблица"
    elif name in ("LOG_gap-monitor-findings",) or name.startswith("LOG_"):
        excluded = "машинный журнал"
    frozen = "ЗАМОРОЖЕН" in rest or "СНЯТ" in rest
    already = name in frozen_read_line
    docs.append({"name": name, "id": did, "frozen_mark_in_registry": frozen,
                 "in_frozen_read_line": already, "excluded": excluded})

# --- step 1b: projects and labs in the repository ---
projects, labs = [], []
for ln in read("registry/projects.md").splitlines():
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) >= 3 and cells[1].startswith("projects/") and cells[2].startswith("repo"):
        projects.append(cells[1].rstrip("/"))
    if len(cells) >= 3 and cells[1].startswith("labs/") and cells[2].startswith("repo"):
        labs.append(cells[1].rstrip("/"))

# git log --since uses committer date; window starts at 00:00 of the last harvest day
since_arg = since + "T00:00:00"
rec_re = re.compile(r"^((?:Р|Т)-\d+) \| (?:[^|]*\| )?(\d{4}-\d{2}-\d{2})")
journal = {}
for p in projects:
    for fn in ("LOG.md", "LOG_ARCHIVE.md"):
        path = f"{p}/{fn}"
        if not os.path.exists(os.path.join(repo, path)):
            continue
        recs = []
        for i, ln in enumerate(read(path).splitlines(), 1):
            mm = rec_re.match(ln)
            if mm and mm.group(2) >= since:
                recs.append({"id": mm.group(1), "date": mm.group(2), "line": i})
        if fn == "LOG_ARCHIVE.md":
            rotated = git("log", f"--since={since_arg}", "--format=%h", "--", path).strip()
            if not rotated and not recs:
                continue
        if recs:
            journal[path] = recs

def changed(pathspec, status=False):
    fmt = ["--name-status"] if status else ["--name-only"]
    out = git("log", f"--since={since_arg}", "--format=", *fmt, "--", pathspec)
    res = {}
    for ln in out.splitlines():
        if not ln.strip():
            continue
        if status:
            parts = ln.split("\t")
            res.setdefault(parts[-1], set()).add(parts[0][0])
        else:
            res.setdefault(ln.strip(), set())
    return res

state_plan = []
for p in projects:
    for fn in ("STATE.md", "PLAN.md"):
        path = f"{p}/{fn}"
        if git("log", f"--since={since_arg}", "--format=%h", "-1", "--", path).strip():
            state_plan.append({"path": path, "exists": os.path.exists(os.path.join(repo, path))})

lab_tasks = []
for l in labs:
    for path, st in sorted(changed(l + "/", status=True).items()):
        if re.search(r"/t-[^/]+\.md$", path):
            lab_tasks.append({"path": path, "status": "".join(sorted(st)),
                              "exists": os.path.exists(os.path.join(repo, path))})

meta = []
for path in sorted(changed("meta/").keys()):
    if path.startswith("meta/prompts/") or path in ("meta/PENDING_RULES.md", "meta/PROTOCOL_harvest.md"):
        continue
    meta.append({"path": path, "exists": os.path.exists(os.path.join(repo, path))})

out = {
    "repo_head": git("rev-parse", "HEAD").strip(),
    "since": since,
    "protocol_last_harvest": proto_last,
    "docs_candidates": docs,
    "repo_projects": projects,
    "repo_labs": labs,
    "journal_records": journal,
    "journal_records_total": sum(len(v) for v in journal.values()),
    "state_plan_changed": state_plan,
    "lab_tasks_changed": lab_tasks,
    "meta_changed": meta,
}
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
