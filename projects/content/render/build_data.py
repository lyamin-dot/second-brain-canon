"""Сборка data/<арт>.json из projects/content/etalon/<арт>.md (пакет С3).

Тексты переносит скрипт: колонка «текст» таблиц слайдов — на слайд, колонка «иконка» —
имя lucide-static; колонка «источник» не печатается. Тема слайда (светлый/тёмный/белый) —
из строки «Слайды: 1 светлый, 2 тёмный…» раздела «Визуальная концепция».
Запуск: python3 build_data.py  (из папки render/)
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ETALON = os.path.join(HERE, "..", "etalon")
CFG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
THEME = {"светлый": "light", "тёмный": "dark", "белый": "white"}


def parse(art):
    md = open(os.path.join(ETALON, f"{art}.md"), encoding="utf-8").read()
    vis = md.split("## Визуальная концепция", 1)[1].split("## Текст на слайды", 1)[0]
    themes = {int(n): THEME[t] for n, t in re.findall(r"(\d) (светлый|тёмный|белый)", vis)}
    assert sorted(themes) == list(range(1, 9)), (art, themes)
    title = re.search(r"^# Эталон \d+ — (.+)$", md, re.M).group(1)
    body = md.split("## Текст на слайды", 1)[1].split("## Техническое ТЗ", 1)[0]
    parts = re.split(r"^### Слайд (\d) — (.+)$", body, flags=re.M)
    slides = []
    for i in range(1, len(parts), 3):
        n, name, chunk = int(parts[i]), parts[i + 1].strip(), parts[i + 2]
        els = []
        for line in chunk.splitlines():
            if not line.startswith("| ") or line.startswith("| элемент") or line.startswith("|---"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                continue
            kind, text, icon = cells[0], cells[1], cells[2]
            if text.startswith("нет"):
                continue
            m = re.search(r"`([a-z0-9-]+)`", icon)
            els.append({"kind": kind, "text": text, "icon": m.group(1) if m else None})
        slides.append({"n": n, "name": name, "theme": themes[n],
                       "type": CFG["slide_types"][n - 1], "elements": els})
    assert [s["n"] for s in slides] == list(range(1, 9)), art
    return {"art": art, "title": title, **CFG["skus"][art], "slides": slides}


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    for art in CFG["skus"]:
        d = parse(art)
        json.dump(d, open(os.path.join(HERE, "data", f"{art}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(art, [len(s["elements"]) for s in d["slides"]], "".join(s["theme"][0] for s in d["slides"]))
