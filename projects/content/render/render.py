"""Рендер 32 слайдов эталона CONTENT (пакет С3): HTML/CSS → PNG 1200×1600 + проверки.

Вход: data/<арт>.json (build_data.py), архив фото CONTENT_PHOTOS_ZIP, распакованный в --photos,
npm-пакеты @fontsource/montserrat и lucide-static в --npm.
Выход: --out/<арт>_<N>.png, --out/<арт>_<N>.html, --out/checks.json.
Запуск: python3 render.py --photos DIR --npm DIR --out DIR [--only 1340]

Шаблон один, восемь типов слайдов; слайд 7 — четыре варианта (config.json, поле s7).
Фоны — только CSS/SVG (градиенты, геометрия, свет). Логотип не рисуется: заглушка «ЛОГО».
"""
import argparse
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cutout import cutout  # noqa: E402

W, H = 1200, 1600
M = 48            # поля
TOP, BOTTOM = 60, 80  # безопасные зоны площадок
PALETTE = {"#C8102E": "красный", "#1A1A1A": "тёмный", "#F8F8F8": "светлый", "#FFFFFF": "белый", "#003087": "синий"}
THEMES = {
    "dark": {"bg": "#1A1A1A", "fg": "#FFFFFF", "fgrgb": "255,255,255"},
    "light": {"bg": "#F8F8F8", "fg": "#1A1A1A", "fgrgb": "26,26,26"},
    "white": {"bg": "#FFFFFF", "fg": "#1A1A1A", "fgrgb": "26,26,26"},
}
# бейдж — без слова «гарантия», логотипа отдельной плашкой нет (FACTS.md, обновление Г1; запись Р-7 LOG.md)
BADGE_TEXT = "Официальный продавец"

ICON_CACHE = {}


def icon(npm, name, cls="ic"):
    if not name:
        return ""
    if name not in ICON_CACHE:
        p = os.path.join(npm, "node_modules", "lucide-static", "icons", f"{name}.svg")
        s = open(p, encoding="utf-8").read()
        s = re.sub(r"<!--.*?-->", "", s, flags=re.S).strip()
        s = re.sub(r'\s(width|height)="24"', "", s)
        s = re.sub(r'class="[^"]*"', "", s)
        ICON_CACHE[name] = s
    return ICON_CACHE[name].replace("<svg", f'<svg class="{cls}"', 1)


def esc(t):
    return html.escape(t, quote=False)


def css(npm, th):
    f = os.path.join(npm, "node_modules", "@fontsource", "montserrat", "files")
    faces = ""
    for wgt in (400, 600, 800):
        for sub, rng in (("cyrillic", "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116"),
                         ("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD")):
            faces += (f"@font-face{{font-family:'M';font-weight:{wgt};font-style:normal;"
                      f"src:url('file://{f}/montserrat-{sub}-{wgt}-normal.woff2') format('woff2');unicode-range:{rng};}}\n")
    t = THEMES[th]
    return faces + f"""
:root{{--bg:{t['bg']};--fg:{t['fg']};--fgr:{t['fgrgb']};--acc:#C8102E;--accr:200,16,46}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:var(--bg)}}
body{{font-family:'M';color:var(--fg);-webkit-font-smoothing:antialiased}}
.slide{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:var(--bg)}}
.bg{{position:absolute;inset:0;pointer-events:none}}
.bg svg{{position:absolute;inset:0;width:100%;height:100%}}
.badge{{position:absolute;right:{M}px;top:{TOP}px;height:88px;border:3px solid var(--acc);border-radius:46px;
  padding:0 30px 0 22px;display:flex;align-items:center;gap:14px}}
.badge .ic{{width:46px;height:46px;color:var(--acc);stroke-width:2.2;flex:none}}
.badge .bt{{font-size:32px;line-height:1.12;font-weight:600}}
.frame{{position:absolute;left:{M}px;right:{M}px;top:184px;bottom:{BOTTOM}px;display:flex;flex-direction:column}}
.h1{{font-weight:800;font-size:84px;line-height:1.06;letter-spacing:-.01em}}
.h1 .accent{{color:var(--acc)}}
.sub{{font-weight:600;font-size:48px;line-height:1.16;margin-top:22px;color:rgba(var(--fgr),.82)}}
.bar{{width:96px;height:10px;background:var(--acc);border-radius:5px;margin-bottom:28px}}
.ph{{position:relative;min-height:0;display:flex;align-items:center;justify-content:center}}
.ph img{{max-width:100%;max-height:100%;object-fit:contain;display:block;position:relative;z-index:1}}
.ph .halo{{position:absolute;inset:0;z-index:0;-webkit-mask-image:radial-gradient(ellipse 55% 50% at 50% 50%,#000 35%,transparent 72%)}}
.ph .shadow{{position:absolute;left:50%;bottom:-6px;width:70%;height:60px;transform:translateX(-50%);
  background:radial-gradient(ellipse at center,rgba(26,26,26,.22),rgba(26,26,26,0) 70%);z-index:0}}
.dark .ph .shadow{{background:radial-gradient(ellipse at center,rgba(var(--accr),.35),rgba(var(--accr),0) 70%)}}
.t{{font-size:38px;line-height:1.2}}
.ic{{stroke-width:2}}
/* tiles (promise) */
.tiles{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:28px}}
.tile{{border:2px solid rgba(var(--fgr),.22);border-radius:28px;padding:30px 24px 30px;display:flex;flex-direction:column;align-items:flex-start;gap:22px}}
.tile .ib{{width:96px;height:96px;border-radius:50%;background:var(--acc);display:flex;align-items:center;justify-content:center}}
.tile .ib .ic{{width:54px;height:54px;color:var(--bg)}}
.tile .t{{font-size:36px;font-weight:600;line-height:1.18}}
.tile.prow{{flex-direction:row;align-items:center;padding:26px 28px;gap:28px}}
.tile.prow .t{{font-size:40px}}
/* list rows (audience / benefits) */
.body{{flex:1;min-height:0;display:flex;gap:36px;margin-top:40px}}
.col{{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;gap:26px}}
.row{{display:flex;align-items:center;gap:26px}}
.row .ib{{flex:none;width:100px;height:100px;border-radius:24px;border:3px solid var(--acc);display:flex;align-items:center;justify-content:center}}
.row .ib .ic{{width:56px;height:56px;color:var(--acc)}}
.row .t{{font-size:40px;font-weight:600}}
.card{{border-left:10px solid var(--acc);background:rgba(var(--fgr),.06);border-radius:0 24px 24px 0;padding:26px 28px;display:flex;gap:22px;align-items:center}}
.card .ic{{flex:none;width:58px;height:58px;color:var(--acc)}}
.card .t{{font-size:38px;font-weight:600}}
.side{{flex:none;width:400px;display:flex}}
.side .ph{{flex:1}}
/* specs */
.spec{{display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:2px solid rgba(var(--fgr),.12)}}
.spec:last-child{{border-bottom:0}}
.spec .ic{{flex:none;width:56px;height:56px;color:var(--acc);margin-top:4px}}
.spec .k{{font-size:30px;font-weight:600;color:rgba(var(--fgr),.62);line-height:1.15}}
.spec .v{{font-size:40px;font-weight:800;line-height:1.15;margin-top:6px}}
.small{{font-size:30px;line-height:1.25;color:rgba(var(--fgr),.68);display:flex;gap:14px;align-items:center;margin-top:14px}}
.small .ic{{flex:none;width:40px;height:40px;color:var(--acc)}}
/* steps */
.steps{{display:flex;flex-direction:column;gap:34px;justify-content:center;flex:1}}
.step{{display:flex;align-items:center;gap:28px}}
.num{{flex:none;width:104px;height:104px;border-radius:50%;background:var(--acc);color:var(--bg);font-weight:800;font-size:56px;display:flex;align-items:center;justify-content:center}}
.step .t{{font-size:40px;font-weight:600;flex:1}}
.step .ic{{flex:none;width:60px;height:60px;color:var(--acc)}}
.warn{{margin-top:34px;background:var(--acc);color:var(--bg);border-radius:24px;padding:26px 30px;display:flex;gap:22px;align-items:center}}
.warn .ic{{flex:none;width:56px;height:56px;color:var(--bg)}}
.warn .t{{font-size:36px;font-weight:800}}
/* s7 mech_h */
.stages{{display:flex;align-items:flex-start;justify-content:space-between;margin-top:56px}}
.stage{{width:320px;display:flex;flex-direction:column;align-items:center;gap:26px;text-align:center}}
.stage .circ{{width:230px;height:230px;border-radius:50%;border:5px solid var(--acc);display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,rgba(var(--accr),.28),rgba(var(--accr),0) 70%)}}
.stage .circ .ic{{width:104px;height:104px;color:var(--fg);stroke-width:1.8}}
.stage .t{{font-size:34px;font-weight:600;line-height:1.2}}
.arrow{{flex:none;width:40px;margin-top:95px;color:var(--acc)}}
.arrow .ic{{width:40px;height:40px;stroke-width:3}}
/* s7 mech_v */
.vstages{{flex:1;position:relative;display:flex;flex-direction:column;justify-content:space-around;padding-left:0}}
.vline{{position:absolute;left:66px;top:12%;bottom:12%;width:0;border-left:4px dashed var(--acc)}}
.vstage{{position:relative;display:flex;align-items:center;gap:30px}}
.vstage .circ{{flex:none;width:136px;height:136px;border-radius:50%;background:var(--acc);display:flex;align-items:center;justify-content:center}}
.vstage .circ .ic{{width:68px;height:68px;color:var(--fg)}}
.vstage .t{{font-size:40px;font-weight:600}}
/* s7 glass */
.glass{{position:relative;flex:1;border:3px solid rgba(var(--fgr),.55);border-radius:36px;overflow:hidden}}
.glass .half{{position:absolute;top:0;bottom:0;width:50%}}
.glass .l{{left:0}} .glass .r{{right:0;background:linear-gradient(125deg,rgba(var(--fgr),0) 30%,rgba(var(--fgr),.16) 45%,rgba(var(--fgr),0) 60%)}}
.glass .div{{position:absolute;left:50%;top:0;bottom:0;border-left:3px solid var(--fg)}}
.spot{{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(var(--fgr),.42),rgba(var(--fgr),.10) 65%,rgba(var(--fgr),0) 72%)}}
.streak{{position:absolute;height:14px;border-radius:7px;background:linear-gradient(90deg,rgba(var(--fgr),0),rgba(var(--fgr),.28),rgba(var(--fgr),0))}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:22px 30px;margin-top:34px}}
.grid2 .row .ib{{width:84px;height:84px;border-radius:20px}}
.grid2 .row .ib .ic{{width:46px;height:46px}}
.grid2 .row .t{{font-size:36px}}
/* s7 timeline */
.tl{{position:relative;height:190px;margin-top:70px}}
.tl .line{{position:absolute;left:60px;right:60px;top:60px;border-top:4px solid rgba(var(--fgr),.5)}}
.tl .tick{{position:absolute;top:44px;width:4px;height:36px;background:rgba(var(--fgr),.5);border-radius:2px}}
.tl .dot{{position:absolute;top:0;width:120px;height:120px;border-radius:50%;background:var(--acc);display:flex;align-items:center;justify-content:center}}
.tl .dot .ic{{width:60px;height:60px;color:var(--fg)}}
.tll{{display:flex;justify-content:space-between;margin-top:-20px}}
.tll .t{{font-size:38px;font-weight:600;max-width:46%}}
.tll .t:last-child{{text-align:right}}
.cap{{display:flex;gap:22px;align-items:center;margin-top:40px;border:2px solid rgba(var(--fgr),.22);border-radius:24px;padding:24px 28px}}
.cap .ic{{flex:none;width:56px;height:56px;color:var(--acc)}}
.cap .t{{font-size:36px;font-weight:600}}
"""


# ---------- фоны (только CSS/SVG) ----------
def decor(kind, theme, n):
    """Фон слайда: мягкий свет на тёмных; у 1709 — луч сверху. Узор (каналы, поток, жгуты, капли)
    рисуется за товаром — класс .halo в photo(), чтобы не ложиться под текст."""
    if theme != "dark":
        return ""
    s = '<div class="bg" style="background:radial-gradient(ellipse 70% 45% at 62% 52%,rgba(255,255,255,.075),rgba(255,255,255,0) 70%)"></div>'
    if kind == "harness":
        s += '<div class="bg" style="background:linear-gradient(180deg,rgba(255,255,255,.08),rgba(255,255,255,0));clip-path:polygon(44% 0,64% 0,86% 100%,22% 100%)"></div>'
    return s


HALO = {
    ("channels", "dark"): "repeating-linear-gradient(180deg,rgba(200,16,46,0) 0 52px,rgba(200,16,46,.34) 52px 54px)",
    ("channels", "light"): "repeating-linear-gradient(180deg,rgba(26,26,26,0) 0 52px,rgba(26,26,26,.07) 52px 54px)",
    ("flow", "dark"): "repeating-linear-gradient(120deg,rgba(200,16,46,0) 0 70px,rgba(200,16,46,.36) 70px 73px)",
    ("flow", "light"): "repeating-linear-gradient(120deg,rgba(200,16,46,0) 0 70px,rgba(200,16,46,.13) 70px 73px)",
    ("harness", "dark"): "repeating-linear-gradient(100deg,rgba(200,16,46,0) 0 44px,rgba(200,16,46,.30) 44px 46px)",
    ("harness", "light"): "repeating-linear-gradient(100deg,rgba(26,26,26,0) 0 44px,rgba(26,26,26,.07) 44px 46px)",
}


def halo(kind, theme):
    if theme == "white":
        return ""
    if kind == "drops":
        fg = "255,255,255" if theme == "dark" else "26,26,26"
        g = []
        for x, y, r in ((18, 22, 110), (82, 34, 80), (24, 70, 70), (80, 78, 120), (55, 12, 40), (12, 48, 36)):
            g.append(f"radial-gradient(circle at {x}% {y}%,rgba({fg},.05) 0 {r - 3}px,rgba({fg},.13) {r - 3}px {r}px,rgba({fg},0) {r + 1}px)")
        g.append("radial-gradient(circle at 80% 78%,rgba(200,16,46,.5) 0 10px,rgba(200,16,46,0) 11px)")
        bg = ",".join(g)
    else:
        bg = HALO.get((kind, theme), "")
    return f'<div class="halo bgx" style="background:{bg}"></div>' if bg else ""


def head(theme, badge=True, npm=None):
    if not badge:
        return ""
    return f'<div class="badge">{icon(npm, "badge-check")}<div class="bt">{esc(BADGE_TEXT)}</div></div>'


def photo_base(src, shadow=True, style="", hl=""):
    sh = '<div class="shadow bgx"></div>' if shadow else ""
    return f'<div class="ph" style="{style}">{hl}{sh}<img class="photo" src="{src}"></div>'


def els(slide, prefix):
    return [e for e in slide["elements"] if e["kind"].startswith(prefix)]


def one(slide, kind):
    for e in slide["elements"]:
        if e["kind"] == kind:
            return e["text"]
    return None


def h1sub(slide, bar=False, fit="3", h1min=64):
    s = '<div class="bar"></div>' if bar else ""
    s += f'<div class="h1" data-fit="{fit}" data-min="{h1min}">{esc(one(slide, "H1"))}</div>'
    sub = one(slide, "подзаголовок")
    if sub:
        s += f'<div class="sub" data-fit="2" data-min="40">{esc(sub)}</div>'
    return s


def build(d, slide, npm, img):
    t = slide["type"]
    th = slide["theme"]
    n = slide["n"]
    I = lambda name, cls="ic": icon(npm, name, cls)  # noqa: E731
    hl = halo(d["decor"], th)
    photo = lambda src, shadow=True, style="": photo_base(src, shadow, style, hl)  # noqa: E731
    side = d.get("photo_side", False)
    body = ""
    if t == "cover":
        body = (f'<div class="frame" style="align-items:center;text-align:center;top:{TOP}px">'
                f'{photo(img, style="flex:1;width:100%")}'
                f'<div style="margin-top:40px;display:flex;flex-direction:column;align-items:center">'
                f'<div class="bar" style="margin-bottom:24px"></div>'
                f'<div class="h1" data-fit="2" style="font-size:86px">{esc(one(slide, "H1"))}</div>'
                f'<div class="sub" data-fit="1" data-min="40" style="margin-top:20px">{esc(one(slide, "подзаголовок"))}</div></div></div>')
    elif t == "promise":
        if side:
            cards = "".join(f'<div class="tile prow" data-box><div class="ib">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "блок"))
            body = (f'<div class="frame">{h1sub(slide, fit="2", h1min=68)}'
                    f'<div class="body"><div class="col" style="gap:24px">{cards}</div><div class="side" style="width:380px">{photo(img)}</div></div></div>')
        else:
            tiles = "".join(f'<div class="tile" data-box><div class="ib">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "блок"))
            body = (f'<div class="frame">{h1sub(slide, fit="2", h1min=68)}'
                    f'{photo(img, style="flex:1;margin-top:36px")}'
                    f'<div class="tiles">{tiles}</div></div>')
    elif t == "audience":
        rows = "".join(f'<div class="row"><div class="ib">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "блок"))
        body = (f'<div class="frame">{h1sub(slide, bar=True)}'
                f'<div class="body"><div class="col">{rows}</div><div class="side">{photo(img)}</div></div></div>')
    elif t == "benefits":
        cards = "".join(f'<div class="card" data-box>{I(e["icon"])}<div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "блок"))
        body = (f'<div class="frame">{h1sub(slide, bar=True)}'
                f'<div class="body"><div class="side" style="width:360px">{photo(img)}</div><div class="col" style="gap:22px">{cards}</div></div></div>')
    elif t == "specs":
        specs, smalls = "", ""
        for e in els(slide, "блок"):
            if e["icon"]:
                sep = ": " if ": " in e["text"] else " — "
                k, v = e["text"].split(sep, 1) if sep in e["text"] else ("", e["text"])
                specs += f'<div class="spec">{I(e["icon"])}<div><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div></div>'
            else:
                smalls += f'<div class="small">{esc(e["text"])}</div>'
        for e in els(slide, "примечание"):
            smalls += f'<div class="small">{I(e["icon"])}<span>{esc(e["text"])}</span></div>'
        body = (f'<div class="frame">{h1sub(slide, bar=True)}'
                f'<div class="body"><div class="col" style="gap:0;justify-content:center">{specs}<div style="margin-top:10px">{smalls}</div></div>'
                f'<div class="side" style="width:380px">{photo(img)}</div></div></div>')
    elif t == "steps":
        steps = "".join(f'<div class="step"><div class="num">{i + 1}</div><div class="t">{esc(e["text"])}</div>{I(e["icon"])}</div>' for i, e in enumerate(els(slide, "шаг")))
        warn = "".join(f'<div class="warn" data-box>{I(e["icon"])}<div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "предупреждение"))
        body = (f'<div class="frame">{h1sub(slide, bar=True)}'
                f'<div class="body" style="margin-top:30px"><div class="steps">{steps}</div><div class="side" style="width:330px">{photo(img)}</div></div>'
                f'{warn}</div>')
    elif t == "s7":
        v = d["s7"]
        if v == "mech_h":
            st = els(slide, "этап")
            parts = []
            for i, e in enumerate(st):
                parts.append(f'<div class="stage"><div class="circ">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>')
                if i < len(st) - 1:
                    parts.append(f'<div class="arrow">{I("chevron-right")}</div>')
            body = (f'<div class="frame">{h1sub(slide)}<div class="stages">{"".join(parts)}</div>'
                    f'{photo(img, style="flex:1;margin-top:40px")}</div>')
        elif v == "mech_v":
            st = "".join(f'<div class="vstage"><div class="circ">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "этап"))
            body = (f'<div class="frame">{h1sub(slide, bar=True)}<div class="body"><div class="vstages"><div class="vline bgx"></div>{st}</div>'
                    f'<div class="side" style="width:380px">{photo(img)}</div></div></div>')
        elif v == "glass":
            spots = "".join(f'<div class="spot bgx" style="left:{x}%;top:{y}%;width:{s}px;height:{s}px"></div>'
                            for x, y, s in ((8, 6, 110), (52, 18, 60), (14, 34, 46), (60, 40, 84), (6, 56, 70), (44, 62, 40), (18, 76, 96), (64, 82, 52), (36, 90, 34), (70, 4, 30), (30, 48, 26), (74, 60, 22)))
            spots += "".join(f'<div class="streak bgx" style="left:{x}%;top:{y}%;width:{w}px;transform:rotate({r}deg)"></div>'
                             for x, y, w, r in ((10, 26, 160, -18), (30, 54, 120, 12), (6, 88, 140, -8)))
            glass = f'<div class="glass bgx"><div class="half l">{spots}</div><div class="half r"></div><div class="div"></div></div>'
            rows = "".join(f'<div class="row"><div class="ib">{I(e["icon"])}</div><div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "блок"))
            body = (f'<div class="frame">{h1sub(slide, bar=True)}<div class="body" style="margin-top:34px">'
                    f'<div style="flex:1;display:flex">{glass}</div><div class="side" style="width:300px">{photo(img)}</div></div>'
                    f'<div class="grid2">{rows}</div></div>')
        elif v == "timeline":
            st = els(slide, "этап")
            ticks = "".join(f'<div class="tick" style="left:calc(60px + (100% - 120px) * {i / 13:.4f} - 2px)"></div>' for i in range(14))
            dots = (f'<div class="dot" style="left:0">{I(st[0]["icon"])}</div>'
                    f'<div class="dot" style="right:0">{I(st[1]["icon"])}</div>')
            cap = "".join(f'<div class="cap" data-box>{I(e["icon"])}<div class="t">{esc(e["text"])}</div></div>' for e in els(slide, "подпись"))
            body = (f'<div class="frame">{h1sub(slide, bar=True)}'
                    f'<div class="tl"><div class="line"></div>{ticks}{dots}</div>'
                    f'<div class="tll"><div class="t">{esc(st[0]["text"])}</div><div class="t">{esc(st[1]["text"])}</div></div>'
                    + (f'<div class="body" style="margin-top:40px"><div class="col">{cap}</div><div class="side" style="width:380px">{photo(img)}</div></div></div>'
                       if side else f'{cap}{photo(img, style="flex:1;margin-top:40px")}</div>'))
    elif t == "white":
        body = f'<div class="frame">{photo(img, style="flex:1")}</div>'
    badge = n >= 2
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{css(npm, th)}</style></head>'
            f'<body><div class="slide {th}">{decor(d["decor"], th, n)}{head(th, badge, npm)}{body}</div></body></html>')


FIT_AND_CHECK_JS = r"""
async () => {
  await document.fonts.ready;
  // подгонка заголовков: уменьшать кегль, пока текст не уложится в data-fit строк
  for (const el of document.querySelectorAll('[data-fit]')) {
    const lines = +el.dataset.fit, min = +(el.dataset.min || 64);
    let fs = parseFloat(getComputedStyle(el).fontSize);
    const lh = parseFloat(getComputedStyle(el).lineHeight) / fs;
    while (el.getBoundingClientRect().height > fs * lh * lines + 2 && fs > min) { fs -= 2; el.style.fontSize = fs + 'px'; }
  }
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const W = 1200, H = 1600, M = 48, TOP = 60, BOT = 80;
  const PAL = {'#C8102E':1,'#1A1A1A':1,'#F8F8F8':1,'#FFFFFF':1,'#003087':1};
  const hex = (r,g,b) => '#' + [r,g,b].map(x => (+x).toString(16).padStart(2,'0')).join('').toUpperCase();
  const used = {}, off = {};
  const add = (s, where) => {
    if (!s) return;
    for (const m of s.matchAll(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/g)) {
      if (m[4] !== undefined && +m[4] === 0) continue;
      const h = hex(Math.round(m[1]), Math.round(m[2]), Math.round(m[3]));
      if (PAL[h]) used[h] = 1; else off[h] = where;
    }
  };
  const isBg = el => !!el.closest('.bg') || el.classList.contains('bgx') || !!el.closest('.bgx');
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0; };
  let minFont = 999, minFontText = '';
  const outM = [], outSafe = [], overflow = [], textRects = [];
  const all = document.querySelectorAll('.slide, .slide *');
  for (const el of all) {
    if (!vis(el)) continue;
    if (el.tagName === 'IMG') continue;  // фото товара — без учёта палитры
    const cs = getComputedStyle(el);
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (hasText) { add(cs.color, 'color'); const f = parseFloat(cs.fontSize); if (f < minFont) { minFont = f; minFontText = el.textContent.trim().slice(0, 40); } }
    add(cs.backgroundColor, 'bg'); add(cs.backgroundImage, 'bgimg'); add(cs.boxShadow, 'shadow'); add(cs.textShadow, 'tshadow');
    for (const side of ['Top','Right','Bottom','Left']) if (parseFloat(cs['border' + side + 'Width']) > 0 && cs['border' + side + 'Style'] !== 'none') add(cs['border' + side + 'Color'], 'border');
    if (el instanceof SVGElement && el.tagName !== 'svg') { if (cs.fill && cs.fill !== 'none') add(cs.fill, 'fill'); if (cs.stroke && cs.stroke !== 'none') add(cs.stroke, 'stroke'); }
    if (el.classList.contains('slide') || isBg(el)) continue;
    const r = el.getBoundingClientRect();
    const drawn = hasText || el.tagName === 'svg' || (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') || parseFloat(cs.borderTopWidth) > 0 || parseFloat(cs.borderLeftWidth) > 0;
    if (!drawn) continue;
    if (r.left < M - 0.5 || r.top < M - 0.5 || r.right > W - M + 0.5 || r.bottom > H - M + 0.5) outM.push((el.getAttribute('class') || el.tagName) + ':' + el.textContent.trim().slice(0,30));
    if (r.top < TOP - 0.5 || r.bottom > H - BOT + 0.5) outSafe.push((el.getAttribute('class') || el.tagName) + ':' + Math.round(r.top) + '-' + Math.round(r.bottom));
    if (hasText) {
      if (el.scrollWidth > el.clientWidth + 1) overflow.push('scroll:' + el.textContent.trim().slice(0,30));
      const box = el.closest('[data-box]');
      if (box) { const b = box.getBoundingClientRect(); if (r.right > b.right + 1 || r.bottom > b.bottom + 1) overflow.push('box:' + el.textContent.trim().slice(0,30)); }
      textRects.push({t: el.textContent.trim().slice(0,30), r: [r.left, r.top, r.right, r.bottom]});
    }
  }
  // фото: реально отрисованная область (object-fit: contain)
  const photos = [];
  for (const img of document.querySelectorAll('img.photo')) {
    const r = img.getBoundingClientRect();
    photos.push({w: Math.round(r.width), h: Math.round(r.height), box: [r.left, r.top, r.right, r.bottom], loaded: img.complete && img.naturalWidth > 0});
    if (r.left < M - .5 || r.top < M - .5 || r.right > W - M + .5 || r.bottom > H - M + .5) outM.push('photo');
    if (r.top < TOP - .5 || r.bottom > H - BOT + .5) outSafe.push('photo:' + Math.round(r.top) + '-' + Math.round(r.bottom));
  }
  const inter = (a, b) => Math.max(0, Math.min(a[2], b[2]) - Math.max(a[0], b[0])) * Math.max(0, Math.min(a[3], b[3]) - Math.max(a[1], b[1]));
  const textOnPhoto = [];
  for (const p of photos) for (const t of textRects) if (inter(p.box, t.r) > 4) textOnPhoto.push(t.t);
  // наложение текстов друг на друга
  const textOverlap = [];
  for (let i = 0; i < textRects.length; i++) for (let j = i + 1; j < textRects.length; j++) {
    const a = textRects[i].r, b = textRects[j].r;
    const inside = (a[0] >= b[0] && a[1] >= b[1] && a[2] <= b[2] && a[3] <= b[3]) || (b[0] >= a[0] && b[1] >= a[1] && b[2] <= a[2] && b[3] <= a[3]);
    if (!inside && inter(a, b) > 4) textOverlap.push(textRects[i].t + ' / ' + textRects[j].t);
  }
  const fits = [...document.querySelectorAll('[data-fit]')].map(e => parseFloat(e.style.fontSize || getComputedStyle(e).fontSize));
  return {minFont, minFontText, palette: Object.keys(used).sort(), offPalette: off, outMargin: outM, outSafe, overflow, textOnPhoto, textOverlap, photos, fitSizes: fits};
}
"""


def selftest(pg):
    """Положительный контроль проверок: заведомо плохой слайд обязан провалить каждую из них."""
    bad = ('<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0}body{width:1200px;height:1600px;background:#F8F8F8}'
           '.a{position:absolute;left:10px;top:10px;font-size:20px;color:#1A1A1A}'
           '.b{position:absolute;left:300px;top:1550px;font-size:40px;color:#00' + 'AA00}'
           '.c{position:absolute;left:300px;top:300px;width:100px;white-space:nowrap;overflow:hidden;font-size:40px;color:#C8102E}'
           '.d{position:absolute;left:300px;top:700px;font-size:40px;color:#FFFFFF;background:#003087}'
           '.e{position:absolute;left:300px;top:705px;font-size:40px}</style></head>'
           '<body><div class="slide"><div class="a">мелко</div><div class="b">в поле</div>'
           '<div class="c">длинная-строка-без-переноса</div><div class="d">наложение</div><div class="e">наложение 2</div></div></body></html>')
    pg.set_content(bad)
    r = pg.evaluate(FIT_AND_CHECK_JS)
    got = {"minFont<28": r["minFont"] < 28, "outMargin": bool(r["outMargin"]), "outSafe": bool(r["outSafe"]),
           "offPalette": bool(r["offPalette"]), "palette>3": len(r["palette"]) > 3, "overflow": bool(r["overflow"]),
           "textOverlap": bool(r["textOverlap"])}
    return got


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--photos", required=True)
    ap.add_argument("--npm", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    from playwright.sync_api import sync_playwright
    from PIL import Image
    results = {}
    cpath = os.path.join(a.out, "checks.json")
    if a.only and os.path.exists(cpath):
        results = json.load(open(cpath, encoding="utf-8"))
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        pg = br.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        st = selftest(pg)
        print("selftest", st)
        if not all(st.values()):
            raise SystemExit("проверки не ловят заведомо плохой слайд — рендер остановлен")
        results["_selftest"] = st
        for fn in sorted(os.listdir(os.path.join(HERE, "data"))):
            d = json.load(open(os.path.join(HERE, "data", fn), encoding="utf-8"))
            art = d["art"]
            if a.only and art not in a.only.split(","):
                continue
            src = os.path.join(a.photos, d["photo"])
            cut = os.path.join(a.out, f"{art}_cut.png")
            if os.path.exists(src):
                cutout(src, cut, d["cut_thr"])
                img = "file://" + cut
            else:  # фото нет — серый силуэт «фото товара»
                img = "data:image/svg+xml;utf8," + "<svg xmlns='http://www.w3.org/2000/svg' width='300' height='900'><rect x='60' y='0' width='180' height='900' rx='30' fill='%231A1A1A' fill-opacity='.25'/><text x='150' y='460' font-size='30' text-anchor='middle' fill='%231A1A1A'>фото товара</text></svg>"
            for s in d["slides"]:
                name = f"{art}_{s['n']}"
                hp = os.path.join(a.out, name + ".html")
                open(hp, "w", encoding="utf-8").write(build(d, s, a.npm, img))
                pg.goto("file://" + hp)
                chk = pg.evaluate(FIT_AND_CHECK_JS)
                png = os.path.join(a.out, name + ".png")
                pg.screenshot(path=png, full_page=False)
                chk["size"] = list(Image.open(png).size)
                chk["type"] = s["type"] + (f":{d['s7']}" if s["type"] == "s7" else "")
                chk["theme"] = s["theme"]
                chk["ok"] = (chk["size"] == [W, H] and chk["minFont"] >= 28 and not chk["outMargin"] and not chk["outSafe"]
                             and len(chk["palette"]) <= 3 and not chk["offPalette"] and not chk["overflow"]
                             and not chk["textOnPhoto"] and not chk["textOverlap"] and all(ph["loaded"] for ph in chk["photos"]))
                results[name] = chk
                print(name, "OK" if chk["ok"] else "FAIL", chk["minFont"], chk["palette"], chk["offPalette"] or "",
                      chk["outMargin"] or "", chk["outSafe"] or "", chk["overflow"] or "", chk["textOnPhoto"] or "",
                      chk["textOverlap"] or "", [(ph["w"], ph["h"]) for ph in chk["photos"]], chk["fitSizes"])
        br.close()
    json.dump(results, open(cpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
