"""Таблица вердиктов по слайдам для REPORT.md из checks.json (render.py) и visual.json (глазной вердикт).
Запуск: python3 report.py OUT_DIR > table.md"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(open(os.path.join(sys.argv[1], "checks.json"), encoding="utf-8"))
v = json.load(open(os.path.join(HERE, "visual.json"), encoding="utf-8"))
print("| слайд | тип | тема | размер | мин. кегль | цвета палитры | поля 48 / зоны 60–80 | вылет / наложение / текст на фото | фото, px | скрипт | глазами |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for k in sorted(x for x in c if not x.startswith("_")):
    r = c[k]
    pal = f'{len(r["palette"])}: ' + " ".join(r["palette"]) + (" + вне палитры " + " ".join(r["offPalette"]) if r["offPalette"] else "")
    m = "чисто" if not r["outMargin"] and not r["outSafe"] else f'{len(r["outMargin"])} / {len(r["outSafe"])}'
    o = "нет" if not (r["overflow"] or r["textOverlap"] or r["textOnPhoto"]) else f'{len(r["overflow"])} / {len(r["textOverlap"])} / {len(r["textOnPhoto"])}'
    ph = ", ".join(f'{p["w"]}×{p["h"]}' for p in r["photos"])
    print(f'| {k} | {r["type"]} | {r["theme"]} | {r["size"][0]}×{r["size"][1]} | {r["minFont"]:.0f} | {pal} | {m} | {o} | {ph} | {"прошёл" if r["ok"] else "НЕ прошёл"} | {v.get(k, "не просмотрен")} |')
st = c.get("_selftest", {})
print()
print("Положительный контроль (заведомо плохой слайд, тот же код проверок): " + ", ".join(f"{a} — {'пойман' if b else 'НЕ пойман'}" for a, b in st.items()))
