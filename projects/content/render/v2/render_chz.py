"""Значок «Честный знак» на слайдах одного товара (2026-11-08, просьба Андрея: «используй этот значок у товаров,
маркированных Честный знак … предложи различные размеры … оформи только картинки для одного товара»).

Значок нарисован вектором (зелёный щит с белой галочкой, цвет снят с образца Андрея: #43995C), не скачан:
сеть песочницы закрыта для картинок, а официальный логотип «Честного ЗНАКа» — товарный знак оператора.
Галочка — цветом фона светлого слайда #F8F8F8 (правило «текст на плашке — цветом фона», запись Р-8 журнала). Зелёный — четвёртый цвет на слайде: проверка палитры пропускает только его и только как знак системы.

Выход: обложка в трёх размерах значка (S — как пиктограммы, M, L), слайд «Как проверить» со значком,
лист «как это видно в ленте каталога» (обложки, уменьшенные до ширины карточки в выдаче телефона).
Запуск: python3 render_chz.py --art 1340 --photos DIR --npm DIR --out DIR
"""
import argparse, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, ".."))
import render as R  # noqa: E402
import render_v2 as V  # noqa: E402

GREEN = "#43995C"


def shield(px):
    return (f'<svg width="{px}" height="{px}" viewBox="0 0 100 100" style="flex:none;display:block">'
            f'<path d="M50 4 L90 17 V47 C90 71 73 88 50 96 C27 88 10 71 10 47 V17 Z" fill="{GREEN}"/>'
            f'<polyline points="30,51 44,65 71,37" fill="none" stroke="#F8F8F8" stroke-width="10" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


# значок ниже верхней безопасной зоны площадок (60 px); размер значка на обложке: S — как пиктограммы слайдов (80 px), M — с подписью, L — крупный, подпись под щитом (сбоку налезала на фото товара)
VARIANTS = {
    "S": f'<div style="position:absolute;left:48px;top:72px">{shield(80)}</div>',
    "M": (f'<div data-box style="position:absolute;left:48px;top:72px;display:flex;align-items:center;gap:18px">{shield(120)}'
          f'<div style="font-weight:600;font-size:40px;line-height:1.1;color:#1A1A1A">Честный<br>знак</div></div>'),
    "L": (f'<div data-box style="position:absolute;left:48px;top:72px;display:flex;flex-direction:column;align-items:center;gap:14px">{shield(170)}'
          f'<div style="font-weight:800;font-size:44px;line-height:1.08;color:#1A1A1A;text-align:center">Честный<br>знак</div></div>'),
}


def check(pg, hp, png):
    c = V.check(pg, hp, png)
    c["palette"] = [h for h in c["palette"] if h != GREEN]
    if isinstance(c["offPalette"], dict):
        c["offPalette"] = {k: v for k, v in c["offPalette"].items() if k != GREEN}
    c["ok"] = (c["size"] == [R.W, R.H] and c["minFont"] >= V.MIN_FONT and not c["outMargin"] and not c["outSafe"]
               and len(c["palette"]) <= 3 and not c["offPalette"] and not c["overflow"]
               and not c["textOnPhoto"] and not c["textOverlap"] and all(p["loaded"] for p in c["photos"]))
    return c


def chz_slide(npm, img):
    h = V.build_chz(npm, img)
    ok_old = '<div class="ok">' + R.icon(npm, "check", "ic") + '</div>'
    if h.count(ok_old) != 1:
        raise SystemExit("в макете не найдена галочка телефона")
    h = h.replace(ok_old, f'<div style="position:absolute;bottom:40px;left:50%;transform:translateX(-50%)">{shield(130)}</div>')
    # значок рядом с подзаголовком: «Товар промаркирован в системе «Честный знак»»
    sub_old = '<div class="sub" data-fit="2" data-min="40">'
    if h.count(sub_old) != 1:
        raise SystemExit("в макете не найден подзаголовок")
    h = h.replace(sub_old, f'<div style="display:flex;align-items:center;gap:24px;margin-top:22px">{shield(96)}'
                  f'<div class="sub" data-fit="2" data-min="40" style="margin-top:0">', 1)
    h = h.replace('«Честный знак»</div>', '«Честный знак»</div></div>', 1)
    return h


def main():
    ap = argparse.ArgumentParser()
    for k in ("art", "photos", "npm", "out"):
        ap.add_argument("--" + k, required=True)
    a = ap.parse_args()
    V.patch_source()
    os.makedirs(a.out, exist_ok=True)
    d = json.load(open(os.path.join(HERE, "data_v2", a.art + ".json"), encoding="utf-8"))
    cut = os.path.join(a.out, f"{a.art}_cut.png")
    R.cutout(os.path.join(a.photos, d["photo"]), cut, d["cut_thr"])
    img = "file://" + cut
    from playwright.sync_api import sync_playwright
    res = {}
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = br.new_page(viewport={"width": R.W, "height": R.H}, device_scale_factor=1)
        cover = V.build(d, d["slides"][0], a.npm, img)
        anchor = '<div class="frame"'
        if cover.count(anchor) != 1:
            raise SystemExit("в обложке не найден блок текста")
        jobs = {f"{a.art}_cover_{k}": cover.replace(anchor, v + anchor, 1) for k, v in VARIANTS.items()}
        jobs[f"{a.art}_chz"] = chz_slide(a.npm, img)
        for name, h in jobs.items():
            hp = os.path.join(a.out, name + ".html")
            open(hp, "w", encoding="utf-8").write(h)
            c = check(pg, hp, os.path.join(a.out, name + ".png"))
            res[name] = c
            print(name, "OK" if c["ok"] else "FAIL", round(c["minFont"]), c["palette"], c["offPalette"] or "",
                  c["outMargin"] or "", c["outSafe"] or "", c["overflow"] or "", c["textOverlap"] or "")
        br.close()
    json.dump(res, open(os.path.join(a.out, "checks_chz.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # лента каталога: карточка в выдаче на телефоне ~180 px шириной (две колонки); обложки в этом масштабе
    from PIL import Image, ImageDraw
    tw, th = 180, 240
    sheet = Image.new("RGB", (3 * tw + 4 * 20, th + 40), "#E9E7E5")
    for i, k in enumerate("SML"):
        im = Image.open(os.path.join(a.out, f"{a.art}_cover_{k}.png")).convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, (20 + i * (tw + 20), 20))
    sheet.save(os.path.join(a.out, f"{a.art}_feed.png"))


if __name__ == "__main__":
    main()
