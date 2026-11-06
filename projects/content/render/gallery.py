"""Страница-галерея 32 слайдов для Artifact (пакет С3). Запуск: python3 gallery.py OUT_DIR GALLERY_DIR
Пишет GALLERY_DIR/index.html; PNG ожидаются в GALLERY_DIR/png/<арт>_<N>.png."""
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
out, gdir = sys.argv[1], sys.argv[2]
checks = json.load(open(os.path.join(out, "checks.json"), encoding="utf-8"))
ORDER = ["1340", "1342", "1750", "1709"]
TYPE_RU = {"cover": "Обложка", "promise": "Главное обещание", "audience": "Для кого и для чего", "benefits": "Преимущества",
           "specs": "Назначение и применение", "steps": "Как применять", "white": "Белый фон"}
sections = []
for art in ORDER:
    d = json.load(open(os.path.join(HERE, "data", f"{art}.json"), encoding="utf-8"))
    cards = []
    for s in d["slides"]:
        k = f"{art}_{s['n']}"
        c = checks[k]
        name = html.escape(s["name"])
        state = "прошёл" if c["ok"] else "не прошёл"
        cards.append(
            f'<figure class="slide"><button class="zoom" type="button" data-src="png/{k}.png" aria-label="Открыть слайд {s["n"]} крупно">'
            f'<img src="png/{k}.png" alt="{art}, слайд {s["n"]}: {name}" loading="lazy" width="1200" height="1600"></button>'
            f'<figcaption><span class="n">{s["n"]}</span><span class="nm">{name}</span>'
            f'<span class="chk {"ok" if c["ok"] else "bad"}" title="мин. кегль {c["minFont"]:.0f} px · цветов палитры {len(c["palette"])}">{state}</span></figcaption></figure>')
    sections.append(f'<section class="sku" id="a{art}"><header><span class="art">{art}</span><h2>{html.escape(d["title"])}</h2></header>'
                    f'<div class="grid">{"".join(cards)}</div></section>')
nav = "".join(f'<a href="#a{a}">{a}</a>' for a in ORDER)
total_ok = sum(1 for k, v in checks.items() if not k.startswith("_") and v["ok"])
page = f"""<title>Эталон слайдов Liqui Moly</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap">
<style>
/* Layout: рабочая витрина — четыре полосы товаров, в каждой сетка из восьми слайдов 3:4 */
:root{{--bg:#F3F2F1;--surface:#FFFFFF;--fg:#1A1A1A;--muted:#5E5A57;--line:#DEDAD6;--accent:#C8102E;--ok:#1F7A4D;
  --display:'Montserrat',system-ui,sans-serif;--body:'Montserrat',system-ui,sans-serif}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--bg:#151414;--surface:#1F1E1D;--fg:#F4F2F0;--muted:#A9A29C;--line:#34312F;--accent:#E0384F;--ok:#4FBF86;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#151414;--surface:#1F1E1D;--fg:#F4F2F0;--muted:#A9A29C;--line:#34312F;--accent:#E0384F;--ok:#4FBF86;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 56px}}
.wrap{{max-width:1240px;margin:0 auto;display:flex;flex-direction:column;gap:40px}}
.top{{display:flex;flex-direction:column;gap:10px}}
.top h1{{font-family:var(--display);font-weight:800;font-size:clamp(26px,4vw,40px);line-height:1.1;text-wrap:balance}}
.top h1 b{{color:var(--accent)}}
.top p{{color:var(--muted);max-width:70ch}}
.meta{{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}}
.meta strong{{color:var(--fg);font-weight:600}}
nav{{display:flex;gap:8px;flex-wrap:wrap}}
nav a{{font-weight:600;font-size:14px;color:var(--fg);text-decoration:none;border:1.5px solid var(--line);border-radius:999px;padding:6px 14px}}
nav a:hover,nav a:focus-visible{{border-color:var(--accent);outline:none}}
.sku header{{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:16px;border-bottom:2px solid var(--line);padding-bottom:10px}}
.art{{font-weight:800;font-size:28px;color:var(--accent);font-variant-numeric:tabular-nums}}
.sku h2{{font-weight:600;font-size:18px;min-width:0;text-wrap:balance}}
.grid{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}}
@media (max-width:900px){{.grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
.slide{{margin:0;display:flex;flex-direction:column;gap:8px;min-width:0}}
.zoom{{all:unset;cursor:zoom-in;display:block;border-radius:10px;overflow:hidden;border:1px solid var(--line);background:var(--surface)}}
.zoom:focus-visible{{outline:3px solid var(--accent);outline-offset:2px}}
.zoom img{{display:block;width:100%;height:auto;aspect-ratio:3/4;max-width:100%}}
figcaption{{display:flex;align-items:center;gap:8px;font-size:13px;min-width:0}}
.n{{flex:none;width:22px;height:22px;border-radius:50%;background:var(--fg);color:var(--bg);font-weight:800;font-size:12px;display:flex;align-items:center;justify-content:center}}
.nm{{flex:1;min-width:0;color:var(--muted)}}
.chk{{flex:none;font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase}}
.chk.ok{{color:var(--ok)}} .chk.bad{{color:var(--accent)}}
.lb{{position:fixed;inset:0;background:rgba(10,10,10,.88);display:flex;align-items:center;justify-content:center;
  padding:max(16px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(16px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));z-index:20;cursor:zoom-out}}
.lb img{{max-height:100%;max-width:100%;width:auto;height:auto;border-radius:8px}}
.note{{font-size:13px;color:var(--muted);max-width:80ch}}
</style>
<div class="wrap">
<div class="top">
<h1>Эталон слайдов <b>Liqui Moly</b> · 4 товара × 8</h1>
<p>Слайды 1200×1600 для карточек WB и Ozon, собранные шаблоном из текстов эталона. Отдельной плашки логотипа нет, бейдж — «Официальный продавец» без слова «гарантия» (правила WB, запись Р-7); фоны нарисованы кодом, фото — первое фото карточки WB, вырезанное из белого фона.</p>
<div class="meta"><span>Пакет <strong>С3</strong></span><span>Собрано <strong>2026-11-06</strong></span><span>Проверки скрипта: <strong>{total_ok} из 32</strong> прошли</span><span>Нажмите на слайд, чтобы открыть крупно</span></div>
<nav aria-label="Товары">{nav}</nav>
</div>
{''.join(sections)}
<p class="note">Проверка скрипта на каждом слайде: размер ровно 1200×1600; видимый текст не мельче 28 px; ничего, кроме фона, в полях 48 px и в безопасных зонах 60 px сверху и 80 px снизу; не больше трёх цветов палитры (без учёта фото); нет вылезающего и наложенного текста. Тексты и источники — projects/content/etalon/, отчёт — projects/content/render/REPORT.md.</p>
</div>
<div class="lb" id="lb" hidden><img id="lbimg" alt=""></div>
<script>
const lb=document.getElementById('lb'),li=document.getElementById('lbimg');
document.querySelectorAll('.zoom').forEach(b=>b.addEventListener('click',()=>{{li.src=b.dataset.src;li.alt=b.querySelector('img').alt;lb.hidden=false;}}));
lb.addEventListener('click',()=>{{lb.hidden=true;li.removeAttribute('src');}});
document.addEventListener('keydown',e=>{{if(e.key==='Escape')lb.hidden=true;}});
</script>
"""
open(os.path.join(gdir, "index.html"), "w", encoding="utf-8").write(page)
print("ok", total_ok)
