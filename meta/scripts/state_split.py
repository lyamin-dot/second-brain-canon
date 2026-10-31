#!/usr/bin/env python3
"""meta/scripts/state_split.py — Разбор STATE.md по ролям — скриптом, без набора текста моделью.

Два режима:
  check  — только отчёт: размер, превышение бюджета чтения (8 192 Б), какие разделы
           остаются, какие уедут и куда. Ничего не пишет. Для вызова на !save,
           из контракта автопилота и из скриптов переноса.
  split  — раскладывает файл в папку вывода: STATE.new.md (остаётся),
           to_LOG.md (история — блок хроники для LOG.md), to_PLAN.md (правила),
           UNDECIDED.md (разделы, которые скрипт отнести не смог — решает модель
           или Андрей). Приёмка по строкам: каждая непустая строка источника
           встречается ровно в одном из четырёх файлов; иначе — ошибка и ничего
           не считается сделанным.

Запуск: python3 state_split.py check <STATE.md>
        python3 state_split.py split <STATE.md> <папка вывода> [--expect-sha <blob sha>]

Правило, которое исполняет скрипт, — meta/CONTRACT_state-content.md (что остаётся в STATE.md).
Раздел определяется заголовком (строки # / ## / ###). Текст до первого заголовка
(шапка файла) остаётся. Заголовок сравнивается без учёта регистра.
"""
import hashlib, os, re, sys

BUDGET = 8192

# Заголовки, разделы которых остаются в STATE.md: то, что меняет действие следующей сессии.
KEEP = ["следующий шаг", "где стоим", "статус", "фазы", "открыт", "ждёт андрея", "ждёт владельца",
        "ждет андрея", "руками андрею", "ручные действия", "блокер", "от соседнего проекта",
        "очередь действий", "на обсуждение", "ждёт отправки", "долги", "этапы"]
# Признаки истории в самом заголовке: раздел перекрыт, прежний, снят, выполнен — уезжает в LOG.md блоком хроники.
HISTORY = ["перекрыт", "прежний", "снято", "снят ", "выполнен", "состояние на 20", "сделано в", "проверено в этой сессии",
           "проверено 20", "сверка «", "приёмка переноса", "статус переноса", "перенесено из", "ретроспектива", "повтор теста"]
# Признаки правила: уезжает в PLAN.md.
RULE = ["правил", "как ответить", "как устроено", "источники истины", "маршрут доставки"]

def classify(heading):
    h = heading.lower()
    if h.startswith("# "): return "STATE"   # заголовок файла первого уровня — шапка, остаётся
    if any(k in h for k in HISTORY): return "LOG"
    if any(k in h for k in KEEP): return "STATE"
    if any(k in h for k in RULE): return "PLAN"
    return "UNDECIDED"

def sections(text):
    """[(heading или None для шапки, [строки])]"""
    out, cur_h, cur = [], None, []
    for line in text.splitlines(keepends=True):
        if re.match(r"^#{1,3} ", line):
            out.append((cur_h, cur)); cur_h, cur = line.rstrip("\n"), [line]
        else:
            cur.append(line)
    out.append((cur_h, cur))
    return out

def blob_sha(data: bytes):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()

def main():
    mode, path = sys.argv[1], sys.argv[2]
    raw = open(path, "rb").read(); text = raw.decode("utf-8")
    sha = blob_sha(raw)
    if "--expect-sha" in sys.argv:
        exp = sys.argv[sys.argv.index("--expect-sha") + 1]
        if not sha.startswith(exp):
            sys.exit(f"СТОП: файл изменился — blob sha {sha[:7]}, ожидался {exp[:7]}. Разбор по старому снимку запрещён.")
    secs = sections(text)
    plan = []
    for h, lines in secs:
        dest = "STATE" if h is None else classify(h)
        plan.append((dest, h, lines))
    size = len(raw)
    keep_bytes = sum(len("".join(l).encode()) for d, _, l in plan if d == "STATE")
    print(f"файл: {path}  blob sha: {sha[:7]}  размер: {size} Б  бюджет: {BUDGET} Б  {'ПРЕВЫШЕН' if size > BUDGET else 'в норме'}")
    print(f"остаётся в STATE.md: {keep_bytes} Б  {'— и после разбора больше бюджета' if keep_bytes > BUDGET else ''}")
    for d, h, l in plan:
        print(f"  [{d:9}] {len(''.join(l).encode()):6} Б  {h or '(шапка файла)'}")
    if mode == "check":
        return
    out = sys.argv[3]; os.makedirs(out, exist_ok=True)
    buckets = {"STATE": [], "LOG": [], "PLAN": [], "UNDECIDED": []}
    for d, h, l in plan: buckets[d].extend(l)
    names = {"STATE": "STATE.new.md", "LOG": "to_LOG.md", "PLAN": "to_PLAN.md", "UNDECIDED": "UNDECIDED.md"}
    # приёмка до записи: мультимножество непустых строк источника == объединение четырёх будущих файлов
    src = sorted(l.strip() for l in text.splitlines() if l.strip())
    dst = sorted(l.strip() for b in buckets.values() for l in "".join(b).splitlines() if l.strip())
    if src != dst: sys.exit(f"ПРИЁМКА НЕ ПРОЙДЕНА, ничего не записано: строк в источнике {len(src)}, в выводе {len(dst)}")
    os.makedirs(out, exist_ok=True)
    for d, lines in buckets.items():
        with open(os.path.join(out, names[d]), "w", encoding="utf-8") as f: f.write("".join(lines))
    # повторная приёмка по записанным файлам
    dst2 = sorted(l.strip() for d in buckets for l in open(os.path.join(out, names[d]), encoding="utf-8").read().splitlines() if l.strip())
    if src != dst2: sys.exit("ПРИЁМКА НЕ ПРОЙДЕНА при перечитывании записанных файлов")
    print(f"приёмка: {len(src)} непустых строк источника — все найдены, потерь 0. Вывод: {out}")

if __name__ == "__main__":
    main()
