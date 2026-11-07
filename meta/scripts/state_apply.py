#!/usr/bin/env python3
"""meta/scripts/state_apply.py — применение решений разбора STATE.md: перенос строк без набора моделью.

Вход — JSON-файл решений:
{
  "state": "projects/<имя>/STATE.md",
  "expect_sha": "<blob sha или его начало>",
  "date": "2026-10-30",
  "decisions": [
    {"section": "<подстрока заголовка>", "to": "STATE|LOG|PLAN"},
    {"lines": [от, до], "to": "LOG|PLAN", "note": "<одна строка — почему уезжает>"}
  ],
  "plan_heading": "## Перенесено из STATE.md разбором 2026-10-30"
}
Разделы без решения остаются в STATE.md. Строки по номерам (включительно, с 1) переносятся
из любого раздела; остаток раздела остаётся. Сверх источника добавляются только две служебные строки: строка происхождения блока хроники
(форма second-brain-git 11.5) и заголовок блока в PLAN.md; «note» печатается в отчёт и в файлы не пишется.

Действие «заменить строку текстом из файла» (пилот 2026-11-07, только projects/deklaration-v2/):
    {"replace": [N, ...], "with_file": "<файл коротких строк>", "note": "<почему>"}
  Строка N источника (с 1) уезжает без изменений в блок хроники LOG, на её место в STATE встаёт строка из файла
  коротких строк с ключом [N] (формат строки файла: «[N] текст»; остальные строки файла игнорируются).
  Короткая строка: одна строка не длиннее 500 байт UTF-8. Если в решениях есть ключ "log" (путь к LOG.md),
  каждая вставленная строка обязана нести указатель «хроника ГГГГ-ММ-ДД, строка, начинающаяся словами «…»»:
  дата равна "date", слова начинают ровно одну строку журнала (старый LOG + новый блок), и это уехавшая строка N.
  Закрытие дела — без вставки: обычное действие "lines" (строка уезжает в LOG, на месте ничего).
  Путь with_file ищется как задан, затем рядом с файлом решений.
  Приёмка (ДО записи и по записанным файлам): мультимножество непустых строк источника ==
  (STATE.new минус вставленные строки) + LOG_append + PLAN_append минус служебные строки; иначе выход с ошибкой, ничего не записано.
  Решения без "replace" работают побайтово как до этого дополнения.

Выход в папке out/: STATE.new.md, LOG_append.md (блок хроники, дописывается в конец LOG.md),
PLAN_append.md (дописывается в конец PLAN.md). Приёмка: мультимножество непустых строк
источника == STATE.new + LOG_append + PLAN_append минус две служебные строки; приёмка идёт ДО записи файлов и повторяется по записанным файлам.
Запуск: python3 state_apply.py <решения.json> <папка out>
"""
import hashlib, json, os, re, sys

def blob_sha(b):
    # CRLF рабочей копии Windows (core.autocrlf=true) сводится к LF, как в git: sha совпадает с git rev-parse <ref>:<путь>
    b = b.replace(b"\r\n", b"\n")
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()

def main():
    dec = json.load(open(sys.argv[1], encoding="utf-8")); out = sys.argv[2]
    raw = open(dec["state"], "rb").read(); sha = blob_sha(raw)
    if not sha.startswith(dec["expect_sha"]):
        sys.exit(f"СТОП: {dec['state']} изменился — {sha[:7]}, ожидался {dec['expect_sha'][:7]}")
    lines = raw.decode("utf-8").splitlines(keepends=True)
    dest = ["STATE"] * len(lines)
    # разделы
    heads = [(i, l.rstrip("\n")) for i, l in enumerate(lines) if re.match(r"^#{1,3} ", l)]
    for d in dec["decisions"]:
        if "section" in d:
            hits = [k for k, (i, h) in enumerate(heads) if d["section"] in h]
            if len(hits) != 1: sys.exit(f"СТОП: заголовок «{d['section']}» найден {len(hits)} раз")
            start = heads[hits[0]][0]
            end = heads[hits[0] + 1][0] if hits[0] + 1 < len(heads) else len(lines)
            for i in range(start, end): dest[i] = d["to"]
    for d in dec["decisions"]:
        if "lines" in d:
            a, b = d["lines"]
            for i in range(a - 1, b): dest[i] = d["to"]
    # действие «replace»: длинная строка → LOG, на её место — короткая строка из файла
    inserted = {}  # индекс строки → вставленный текст (с концом строки)
    for d in dec["decisions"]:
        if "replace" in d:
            path = d["with_file"]
            if not os.path.exists(path): path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), os.path.basename(path))
            short = {}
            for fl in open(path, encoding="utf-8").read().splitlines():
                m = re.match(r"^\[(\d+)\] (.+)$", fl)
                if m:
                    if m.group(1) in short: sys.exit(f"СТОП: в {path} два раза ключ [{m.group(1)}]")
                    short[m.group(1)] = m.group(2).strip()
            for n in d["replace"]:
                if not 1 <= n <= len(lines) or dest[n - 1] != "STATE" or not lines[n - 1].strip():
                    sys.exit(f"СТОП: строка {n} не годится для замены (нет, пустая или уже в другом решении)")
                if str(n) not in short: sys.exit(f"СТОП: в {path} нет короткой строки [{n}]")
                t = short[str(n)]
                if len(t.encode("utf-8")) > 500: sys.exit(f"СТОП: короткая строка [{n}] длиннее 500 байт")
                dest[n - 1] = "REPL"
                inserted[n - 1] = t + ("\n" if lines[n - 1].endswith("\n") else "")
    bucket = {"STATE": [], "LOG": [], "PLAN": []}
    for i, l in enumerate(lines):
        if dest[i] == "REPL": bucket["LOG"].append(l); bucket["STATE"].append(inserted[i])
        else: bucket[dest[i]].append(l)
    text = "".join(lines)
    log_head = f"\nХроника | {dec['date']} | перенесено из {dec['state']} разбором по 5.1 — не свидетельство этой сессии\n"
    plan_head = "\n" + dec.get("plan_heading", f"## Перенесено из STATE.md разбором {dec['date']}") + "\n\n"
    notes = [d["note"] for d in dec["decisions"] if "note" in d]
    # приёмка ДО записи на диск: собрать тексты выходных файлов в памяти, перечитать их как строки
    # и сравнить мультимножество непустых строк с источником (служебные строки — только две: шапка хроники и заголовок PLAN)
    out_texts = {"STATE.new.md": "".join(bucket["STATE"]),
                 "LOG_append.md": (log_head + "".join("  " + l if l.strip() else l for l in bucket["LOG"])) if bucket["LOG"] else "",
                 "PLAN_append.md": (plan_head + "".join(bucket["PLAN"])) if bucket["PLAN"] else ""}
    service = {log_head.strip(), plan_head.strip()}
    src = sorted(l.strip() for l in text.splitlines() if l.strip())
    got = sorted(l.strip() for t in out_texts.values() for l in t.splitlines() if l.strip() and l.strip() not in service)
    if inserted:
        # вставленные строки вычитаются из РЕЗУЛЬТАТА (а не из источника): потеря строки источника остаётся потерей
        rest = list(got)
        for t in inserted.values():
            if t.strip() not in rest: sys.exit("ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: вставленной строки нет в результате")
            rest.remove(t.strip())
        got = sorted(rest)
        if dec.get("log"):
            logp = dec["log"]
            if not os.path.exists(logp): logp = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), os.path.basename(logp))
            all_log = [x.strip() for x in open(logp, encoding="utf-8").read().splitlines()] + \
                      [x.strip() for x in out_texts["LOG_append.md"].splitlines()]
            for i, t in inserted.items():
                m = re.search(r"хроника (\d{4}-\d{2}-\d{2}), строка, начинающаяся словами «([^»]+)»", t)
                if not m: sys.exit(f"ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: у вставленной строки нет указателя: {t[:50]}")
                if m.group(1) != dec["date"]: sys.exit(f"ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: дата указателя {m.group(1)} != {dec['date']}")
                hits = [x for x in all_log if x.startswith(m.group(2))]
                if hits != [lines[i].strip()]:
                    sys.exit(f"ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: слова «{m.group(2)}» начинают {len(hits)} строк журнала или не ту строку")
    if src != got:
        missing = [l for l in src if l not in got]; extra = [l for l in got if l not in src]
        sys.exit(f"ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: потеряно {len(missing)}, лишних {len(extra)}; первые: {missing[:2]} {extra[:2]}")
    os.makedirs(out, exist_ok=True)
    for name, body in out_texts.items():
        with open(os.path.join(out, name), "w", encoding="utf-8") as f: f.write(body)
    # повторная приёмка по записанным файлам (перечитывание с диска)
    got2 = sorted(l.strip() for name in out_texts for l in open(os.path.join(out, name), encoding="utf-8").read().splitlines() if l.strip() and l.strip() not in service)
    if inserted:
        for t in inserted.values():
            if t.strip() not in got2: sys.exit("ПРИЁМКА НЕ ПРОЙДЕНА при перечитывании записанных файлов: вставленной строки нет")
            got2.remove(t.strip())
    if src != got2: sys.exit("ПРИЁМКА НЕ ПРОЙДЕНА при перечитывании записанных файлов")
    for n in notes: print("  причина:", n)

if __name__ == "__main__": main()
