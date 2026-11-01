"""Статусы очереди, карта каталога, список ожидающих — правки синтеза AJ-74.

Вызов из корня клона: python -I repo_updates.py
Каждое изменение проверяется: строка найдена ровно одна, иначе стоп без записи.
"""
import re
from pathlib import Path

D = "2026-11-01"
ZIP = "second-brain-git_AJ-74_2026-11-01.zip"
REP = "meta/SYNTHESIS_second-brain-git_2026-11-01.md"

QUEUE = {
    "AJ-74": f"ЖДЁТ {D} — заливки владельцем архива `{ZIP}` (набор 2026-11-01; синтез готов, отчёт `{REP}`); прежние архивы second-brain-git (наборы 2026-10-27 и 2026-10-28) не заливать; Х-69 удаляется после приёмки заливки",
    "AJ-60": f"ЖДЁТ {D} — заливки в составе архива `{ZIP}` позиции AJ-74 (текст А4 влит синтезом, строка (г) с прежним охватом — `{REP}`, раздел 3); прежние архивы second-brain-git наборов 2026-10-27 и 2026-10-28 не заливать: они стёрли бы синтез",
    "AJ-63": f"ЖДЁТ {D} — заливки в составе архива `{ZIP}` позиции AJ-74 (references/log-form.md, 11.1, основание GIT-72)",
    "AJ-45": f"ЖДЁТ {D} — часть L1#30 (строка «вторую и каждую следующую запись в той же сессии» таблицы «Что читать дальше» second-brain-git) — заливки в составе архива `{ZIP}` позиции AJ-74; остальные части — как прежде",
}


def one(lines, pred, what):
    idx = [i for i, l in enumerate(lines) if pred(l)]
    if len(idx) != 1:
        raise SystemExit(f"{what}: найдено {len(idx)}")
    return idx[0]


q = Path("registry/maintenance-queue.md")
lines = q.read_text(encoding="utf-8").split("\n")
for pid, new in QUEUE.items():
    i = one(lines, lambda l: l.startswith(f"| {pid} |"), pid)
    row = lines[i]
    assert row.endswith(" |"), pid
    head, old = row[:-2].rsplit(" | ", 1)
    lines[i] = f"{head} | {new}; прежний статус: {old} |"
    print(pid, "статус заменён")
q.write_text("\n".join(lines), encoding="utf-8")

m = Path("meta/SKILLS_MAP.md")
lines = m.read_text(encoding="utf-8").split("\n")
i = one(lines, lambda l: l.startswith("| second-brain-git | готов:"), "SKILLS_MAP")
lines[i] = lines[i].replace("| second-brain-git | ", f"| second-brain-git | ждёт заливки: синтез AJ-74 по харвесту 2026-10-31, архив `{ZIP}`, отчёт `{REP}` ({D}); прежнее: ", 1)
m.write_text("\n".join(lines), encoding="utf-8")
print("SKILLS_MAP: строка second-brain-git")

w = Path("meta/LESSONS_waiting.md")
lines = w.read_text(encoding="utf-8").split("\n")
for x in ("Х-48", "Х-50", "Х-91"):
    i = one(lines, lambda l: re.match(rf"^\| {x} \|", l), x)
    del lines[i]
    print(x, "удалена")
w.write_text("\n".join(lines), encoding="utf-8")
