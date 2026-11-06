"""Вырезка товара из белого фона фото карточки WB (пакет С3).

Заливка от краёв по почти-белым пикселям (связная область, касающаяся рамки),
мягкий край — размытие маски. Выход: PNG с прозрачностью, обрезанный по товару.
Запуск: python3 cutout.py <вход.webp> <выход.png> [порог=252]
"""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage


def cutout(src, dst, thr=252, feather=1.4, pad=8):
    im = Image.open(src).convert("RGB")
    a = np.asarray(im).astype(np.int16)
    mn = a.min(axis=2)
    mx = a.max(axis=2)
    near_white = (mn >= thr) & ((mx - mn) <= 12)
    lab, _ = ndimage.label(near_white)
    border = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])))
    border.discard(0)
    bg = np.isin(lab, list(border))
    # закрыть мелкие дыры в товаре, не трогая фон
    fg = ~bg
    fg = ndimage.binary_fill_holes(fg)
    fg = ndimage.binary_opening(fg, iterations=1)
    # оставить только самую крупную связную область (товар), снять полосы рамки фото
    lab2, n2 = ndimage.label(fg)
    if n2 > 1:
        sizes = ndimage.sum(fg, lab2, range(1, n2 + 1))
        fg = lab2 == (int(np.argmax(sizes)) + 1)
    alpha = Image.fromarray((fg * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(feather))
    # уменьшить белый ореол: альфа сдвигается внутрь на полпикселя
    al = np.asarray(alpha).astype(np.float32) / 255.0
    al = np.clip((al - 0.25) / 0.75, 0, 1)
    rgba = np.dstack([np.asarray(im), (al * 255).astype(np.uint8)])
    out = Image.fromarray(rgba, "RGBA")
    ys, xs = np.where(al > 0.05)
    box = (max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + pad + 1, im.width), min(ys.max() + pad + 1, im.height))
    out = out.crop(box)
    out.save(dst)
    return box, out.size, float(fg.mean())


if __name__ == "__main__":
    thr = int(sys.argv[3]) if len(sys.argv) > 3 else 252
    print(cutout(sys.argv[1], sys.argv[2], thr))
