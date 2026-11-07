"""Сборка v2 (2026-11-07): восемь слайдов эталона → шесть по просьбе Андрея «слить блоки по парам».
Новый текст скрипт не пишет — только отбирает элементы из data/<арт>.json (выход build_data.py):
  2 «Что делает и как» = заголовок и подзаголовок «Главного обещания» + схема «Механизма» (слайд 7);
    у 1709 = заголовок «Главного назначения» + пункты «Что обрабатывать» (подзаголовок снят: повторял начало заголовка);
  3 «Кому и где» = «Для кого и для чего» + «Назначение и применение»;
  4 «Преимущества» (у 1709 — «Ритм обработки», т.к. его пункты ушли в слайд 2);
  5 «Как применять»; 6 «Белый фон».
Слайд «Честный знак» — отдельный макет (render_v2.py --chz), к товарам не привязан, пока не решено, какие маркированы.
Запуск: python3 build_v2.py  (из папки render/v2/) → data_v2/<арт>.json
"""
import copy, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "data")


def S(d, n):
    return copy.deepcopy(next(s for s in d["slides"] if s["n"] == n))


def head_of(slide, drop_sub=False):
    return [e for e in slide["elements"] if e["kind"] == "H1" or (e["kind"] == "подзаголовок" and not drop_sub)]


def body_of(slide):
    return [e for e in slide["elements"] if e["kind"] not in ("H1", "подзаголовок", "бейдж")]


def v2(d):
    art = d["art"]
    cover, white = S(d, 1), S(d, 8)
    if art == "1709":
        s2 = S(d, 4); s2["elements"] = head_of(S(d, 2), drop_sub=True) + body_of(s2); s2["type"] = "benefits"
        s4 = S(d, 7)
    else:
        s2 = S(d, 7); s2["elements"] = head_of(S(d, 2)) + body_of(s2)
        s4 = S(d, 4)
    s2["name"] = "Что делает и как"; s2["theme"] = "dark"
    a, sp = S(d, 3), S(d, 5)
    s3 = {"n": 3, "name": "Кому и где", "theme": "light", "type": "audspec",
          "elements": head_of(a) + body_of(a) + [dict(e, kind="спец " + e["kind"]) for e in body_of(sp)]}
    s4["theme"] = "dark"
    s5 = S(d, 6)
    slides = [cover, s2, s3, s4, s5, white]
    for i, s in enumerate(slides, 1):
        s["n"] = i
    return dict(d, slides=slides)


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "data_v2"), exist_ok=True)
    for fn in sorted(os.listdir(SRC)):
        d = v2(json.load(open(os.path.join(SRC, fn), encoding="utf-8")))
        json.dump(d, open(os.path.join(HERE, "data_v2", fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(d["art"], [(s["n"], s["type"], s["theme"][0], len(s["elements"])) for s in d["slides"]])
