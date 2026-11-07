"""Рендер v2 (2026-11-07): шаблон render.py без изменений файла, поверх — крупнее текст и пиктограммы
для телефона (слайд 1200 px показывается на ~390 px экрана, всё мельче втрое), новый тип «Кому и где»
(audspec) и макет «Честный знак» (--chz). Порог проверки «минимальный кегль» поднят с 28 до 36 px.
Запуск: python3 render_v2.py --photos DIR --npm DIR --out DIR [--chz]
"""
import argparse, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import render as R  # noqa: E402

MIN_FONT = 36
# старое правило → новое; каждая замена обязана сработать ровно один раз (иначе стоп)
SIZES = [
    (".badge{{position:absolute;right:{M}px;top:{TOP}px;height:88px", ".badge{{position:absolute;right:{M}px;top:{TOP}px;height:96px"),
    (".badge .bt{{font-size:32px", ".badge .bt{{font-size:36px"),
    (".h1{{font-weight:800;font-size:84px", ".h1{{font-weight:800;font-size:96px"),
    (".sub{{font-weight:600;font-size:48px", ".sub{{font-weight:600;font-size:52px"),
    (".ic{{stroke-width:2}}", ".ic{{stroke-width:1.8}}"),
    (".tile .ib{{width:96px;height:96px", ".tile .ib{{width:136px;height:136px"),
    (".tile .ib .ic{{width:54px;height:54px", ".tile .ib .ic{{width:80px;height:80px"),
    (".tile .t{{font-size:36px", ".tile .t{{font-size:48px"),
    (".tile.prow .t{{font-size:40px}}", ".tile.prow .t{{font-size:48px}}"),
    (".row .ib{{flex:none;width:100px;height:100px", ".row .ib{{flex:none;width:136px;height:136px"),
    (".row .ib .ic{{width:56px;height:56px", ".row .ib .ic{{width:80px;height:80px"),
    (".row .t{{font-size:40px", ".row .t{{font-size:48px"),
    (".card .ic{{flex:none;width:58px;height:58px", ".card .ic{{flex:none;width:80px;height:80px"),
    (".card .t{{font-size:38px", ".card .t{{font-size:48px"),
    (".spec .ic{{flex:none;width:56px;height:56px", ".spec .ic{{flex:none;width:72px;height:72px"),
    (".spec .k{{font-size:30px", ".spec .k{{font-size:36px"),
    (".spec .v{{font-size:40px", ".spec .v{{font-size:48px"),
    (".small{{font-size:30px", ".small{{font-size:36px"),
    (".small .ic{{flex:none;width:40px;height:40px", ".small .ic{{flex:none;width:52px;height:52px"),
    (".num{{flex:none;width:104px;height:104px;border-radius:50%;background:var(--acc);color:var(--bg);font-weight:800;font-size:56px",
     ".num{{flex:none;width:120px;height:120px;border-radius:50%;background:var(--acc);color:var(--bg);font-weight:800;font-size:64px"),
    (".step .t{{font-size:40px", ".step .t{{font-size:48px"),
    (".step .ic{{flex:none;width:60px;height:60px", ".step .ic{{flex:none;width:76px;height:76px"),
    (".warn .ic{{flex:none;width:56px;height:56px", ".warn .ic{{flex:none;width:72px;height:72px"),
    (".warn .t{{font-size:36px", ".warn .t{{font-size:44px"),
    (".stage .t{{font-size:34px", ".stage .t{{font-size:42px"),
    (".vstage .circ{{flex:none;width:136px;height:136px", ".vstage .circ{{flex:none;width:150px;height:150px"),
    (".vstage .circ .ic{{width:68px;height:68px", ".vstage .circ .ic{{width:80px;height:80px"),
    (".vstage .t{{font-size:40px", ".vstage .t{{font-size:48px"),
    (".grid2 .row .ib{{width:84px;height:84px", ".grid2 .row .ib{{width:112px;height:112px"),
    (".grid2 .row .ib .ic{{width:46px;height:46px", ".grid2 .row .ib .ic{{width:64px;height:64px"),
    (".grid2 .row .t{{font-size:36px}}", ".grid2 .row .t{{font-size:44px}}"),
    (".tl .dot .ic{{width:60px;height:60px", ".tl .dot .ic{{width:72px;height:72px"),
    (".tll .t{{font-size:38px", ".tll .t{{font-size:46px"),
    (".cap .ic{{flex:none;width:56px;height:56px", ".cap .ic{{flex:none;width:72px;height:72px"),
    (".cap .t{{font-size:36px", ".cap .t{{font-size:46px"),
]
EXTRA = """
/* v2: «Кому и где» */
.aud{display:grid;grid-template-columns:1fr 1fr;gap:26px 28px;margin-top:40px}
.aud .row{gap:22px}
.aud .row .t{font-size:44px}
.specs2{display:grid;grid-template-columns:1fr 1fr;gap:0 36px;margin-top:34px;padding-top:12px;border-top:3px solid var(--acc)}
.specs2 .spec{padding:20px 0}
/* v2: Честный знак */
.chz{flex:1;display:flex;gap:36px;margin-top:44px;min-height:0}
.chz .steps{gap:40px}
.phone{flex:none;width:330px;align-self:center;height:600px;border:6px solid var(--fg);border-radius:56px;position:relative;display:flex;align-items:center;justify-content:center}
.phone .scan{width:190px;height:190px;position:relative}
.phone .scan .ic{width:190px;height:190px;color:var(--acc);stroke-width:1.2}
.phone .ok{position:absolute;bottom:56px;left:50%;transform:translateX(-50%);width:92px;height:92px;border-radius:50%;background:var(--acc);display:flex;align-items:center;justify-content:center}
.phone .ok .ic{width:56px;height:56px;color:var(--bg)}
.phone .notch{position:absolute;top:22px;left:50%;transform:translateX(-50%);width:90px;height:14px;border-radius:7px;background:var(--fg)}
.note{margin-top:30px;border:3px solid var(--acc);border-radius:24px;padding:24px 28px;display:flex;gap:22px;align-items:center}
.note .ic{flex:none;width:68px;height:68px;color:var(--acc)}
.note .t{font-size:42px;font-weight:600}
"""

_css0 = R.css


def css(npm, th):
    s = _css0(npm, th)
    return s + EXTRA


def patch_source():
    import inspect
    src = inspect.getsource(R.css)
    for old, new in SIZES:
        n = src.count(old)
        if n != 1:
            raise SystemExit(f"замена размера сработала {n} раз: {old}")
        src = src.replace(old, new)
    ns = {}
    exec(src, R.__dict__, ns)
    global _css0
    _css0 = ns["css"]
    R.css = css


CHZ = {"H1": "Проверьте подлинность за 10 секунд", "sub": "Товар промаркирован в системе «Честный знак»",
       "steps": [("Установите приложение «Честный ЗНАК»", "smartphone"),
                 ("Наведите камеру на квадратный код на упаковке", "scan-line"),
                 ("Сверьте название и производителя с упаковкой", "list-checks")],
       "note": ("После покупки статус «продан» — это нормально", "info")}


def build_audspec(d, slide, npm, img):
    I = lambda n, c="ic": R.icon(npm, n, c)  # noqa: E731
    rows = "".join(f'<div class="row"><div class="ib">{I(e["icon"])}</div><div class="t">{R.esc(e["text"])}</div></div>'
                   for e in R.els(slide, "блок"))
    specs, smalls = "", ""
    for e in R.els(slide, "спец "):
        k = e["kind"][5:]
        if k.startswith("примечание"):
            smalls += f'<div class="small">{I(e["icon"])}<span>{R.esc(e["text"])}</span></div>'
        elif e["icon"]:
            sep = ": " if ": " in e["text"] else " — "
            kk, v = e["text"].split(sep, 1) if sep in e["text"] else ("", e["text"])
            specs += f'<div class="spec">{I(e["icon"])}<div><div class="k">{R.esc(kk)}</div><div class="v">{R.esc(v)}</div></div></div>'
        else:
            smalls += f'<div class="small">{R.esc(e["text"])}</div>'
    body = (f'<div class="frame">{R.h1sub(slide, bar=True)}<div class="aud">{rows}</div>'
            f'<div class="specs2">{specs}</div><div>{smalls}</div></div>')
    th = slide["theme"]
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{R.css(npm, th)}</style></head>'
            f'<body><div class="slide {th}">{R.decor(d["decor"], th, slide["n"])}{R.head(th, True, npm)}{body}</div></body></html>')


def build_chz(npm, img, th="light"):
    I = lambda n, c="ic": R.icon(npm, n, c)  # noqa: E731
    steps = "".join(f'<div class="step"><div class="num">{i + 1}</div><div class="t">{R.esc(t)}</div></div>'
                    for i, (t, ic) in enumerate(CHZ["steps"]))
    phone = f'<div class="phone bgx"><div class="notch"></div><div class="scan">{I("scan-qr-code")}</div><div class="ok">{I("check")}</div></div>'
    body = (f'<div class="frame"><div class="bar"></div><div class="h1" data-fit="2" data-min="72">{R.esc(CHZ["H1"])}</div>'
            f'<div class="sub" data-fit="2" data-min="40">{R.esc(CHZ["sub"])}</div>'
            f'<div class="chz"><div class="steps">{steps}</div>{phone}</div>'
            f'<div class="note" data-box>{I(CHZ["note"][1])}<div class="t">{R.esc(CHZ["note"][0])}</div></div></div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{R.css(npm, th)}</style></head>'
            f'<body><div class="slide {th}">{R.head(th, True, npm)}{body}</div></body></html>')


def build(d, slide, npm, img):
    if slide["type"] == "audspec":
        return build_audspec(d, slide, npm, img)
    if slide["type"] == "cover":
        return R.build(d, slide, npm, img).replace('style="font-size:86px"', 'style="font-size:100px"')
    h = R.build(d, slide, npm, img)
    if slide["type"] == "s7" and d["s7"] == "mech_h":  # заголовок в три строки съедал фото — держать в две
        h = h.replace('data-fit="3" data-min="64"', 'data-fit="2" data-min="72"', 1)
    if slide["type"] == "steps":  # шаги крупным шрифтом — шире колонка текста, уже фото
        h = h.replace('<div class="side" style="width:330px">', '<div class="side" style="width:270px">', 1)
    return h


def check(pg, html_path, png):
    from PIL import Image
    pg.goto("file://" + html_path)
    c = pg.evaluate(R.FIT_AND_CHECK_JS)
    pg.screenshot(path=png, full_page=False)
    c["size"] = list(Image.open(png).size)
    c["ok"] = (c["size"] == [R.W, R.H] and c["minFont"] >= MIN_FONT and not c["outMargin"] and not c["outSafe"]
               and len(c["palette"]) <= 3 and not c["offPalette"] and not c["overflow"]
               and not c["textOnPhoto"] and not c["textOverlap"] and all(p["loaded"] for p in c["photos"]))
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--photos", required=True); ap.add_argument("--npm", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    patch_source()
    os.makedirs(a.out, exist_ok=True)
    from playwright.sync_api import sync_playwright
    res = {}
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = br.new_page(viewport={"width": R.W, "height": R.H}, device_scale_factor=1)
        st = R.selftest(pg)
        if not all(st.values()):
            raise SystemExit("проверки не ловят заведомо плохой слайд — рендер остановлен")
        res["_selftest"] = st
        for fn in sorted(os.listdir(os.path.join(HERE, "data_v2"))):
            d = json.load(open(os.path.join(HERE, "data_v2", fn), encoding="utf-8"))
            art = d["art"]
            cut = os.path.join(a.out, f"{art}_cut.png")
            R.cutout(os.path.join(a.photos, d["photo"]), cut, d["cut_thr"])
            img = "file://" + cut
            for s in d["slides"]:
                name = f"{art}_{s['n']}"
                hp = os.path.join(a.out, name + ".html")
                open(hp, "w", encoding="utf-8").write(build(d, s, a.npm, img))
                c = check(pg, hp, os.path.join(a.out, name + ".png"))
                c["name"], c["type"] = s["name"], s["type"]
                res[name] = c
                print(name, "OK" if c["ok"] else "FAIL", round(c["minFont"]), c["palette"], c["outMargin"] or "", c["outSafe"] or "",
                      c["overflow"] or "", c["textOnPhoto"] or "", c["textOverlap"] or "", c["fitSizes"])
        hp = os.path.join(a.out, "chz.html")
        open(hp, "w", encoding="utf-8").write(build_chz(a.npm, None))
        c = check(pg, hp, os.path.join(a.out, "chz.png")); c["name"] = "Макет: Честный знак"; res["chz"] = c
        print("chz", "OK" if c["ok"] else "FAIL", round(c["minFont"]), c["palette"], c["outMargin"] or "", c["outSafe"] or "", c["overflow"] or "", c["textOverlap"] or "")
        br.close()
    json.dump(res, open(os.path.join(a.out, "checks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
