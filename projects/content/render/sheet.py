"""Листы просмотра 2×2 (по 600×800) для глазной проверки PNG. Запуск: python3 sheet.py OUT_DIR"""
import os, sys
from PIL import Image
out = sys.argv[1]
names = sorted(f[:-4] for f in os.listdir(out) if f.endswith(".png") and "_cut" not in f and not f.startswith("sheet"))
for i in range(0, len(names), 4):
    sh = Image.new("RGB", (1210, 1610), (128, 128, 128))
    for j, n in enumerate(names[i:i + 4]):
        im = Image.open(os.path.join(out, n + ".png")).convert("RGB").resize((600, 800))
        sh.paste(im, ((j % 2) * 610, (j // 2) * 810))
    sh.save(os.path.join(out, f"sheet_{i // 4:02d}.png"))
    print(f"sheet_{i // 4:02d}", names[i:i + 4])
