#!/usr/bin/env python3
"""Сцены (обложки 2 и 3 из картинок Codex), фото работы в webp и контактные листы.
Запуск: python3 sobrat.py  →  <папка>/oblozhka-2.webp, oblozhka-3.webp, foto-N.webp; list-sceny.webp, list-bannery.webp"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from posty import POSTY, GEN, put

TUT = Path(__file__).resolve().parent
W, H = 1086, 1448
# таблички номеров, которые нарисовала модель, – размыть по рамке (координаты в кадре 1086×1448)
RAZMYT = {'246-sit': [[(528, 1210), (602, 1210), (602, 1242), (528, 1242)]]}


def webp(src, dst, maks=None, q=86):
    im = Image.open(src).convert('RGB')
    if maks:
        im.thumbnail((maks, maks), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=q, method=6)


def scena(src, dst, ramki=()):
    im = Image.open(src).convert('RGB')
    k = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    x, y = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((x, y, x + W, y + H))
    for q in ramki:
        m = Image.new('L', im.size, 0)
        ImageDraw.Draw(m).polygon(q, fill=255)
        vys = max(p[1] for p in q) - min(p[1] for p in q)
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(max(5, vys / 5))), im, m.filter(ImageFilter.GaussianBlur(1)))
    im.save(dst, 'WEBP', quality=88, method=6)


def shrift(r):
    for f in ('/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/Library/Fonts/Arial Bold.ttf'):
        if Path(f).exists():
            return ImageFont.truetype(f, r)
    return ImageFont.load_default()


def list_(fajly, podpisi, dst, kol, t=360):
    h = int(t * 4 / 3)
    ryadov = (len(fajly) + kol - 1) // kol
    S = Image.new('RGB', (kol * (t + 8) + 8, ryadov * (h + 40) + 8), (24, 26, 30))
    d = ImageDraw.Draw(S)
    f = shrift(18)
    for i, (src, pod) in enumerate(zip(fajly, podpisi)):
        x, y = 8 + (i % kol) * (t + 8), 8 + (i // kol) * (h + 40)
        if src.exists():
            S.paste(Image.open(src).convert('RGB').resize((t, h)), (x, y + 32))
        d.text((x, y + 6), pod, fill=(235, 235, 235), font=f)
    S.save(dst, 'WEBP', quality=82, method=6)


def main():
    sc, scp, bn, bnp = [], [], [], []
    for p in POSTY:
        papka = TUT / p['papka']
        papka.mkdir(exist_ok=True)
        for i, zad in ((2, 'sit'), (3, 'srv')):
            src = GEN / f'{p["nomer"]}-{zad}' / 'out.png'
            if src.exists():
                scena(src, papka / f'oblozhka-{i}.webp', RAZMYT.get(f'{p["nomer"]}-{zad}', ()))
            sc.append(papka / f'oblozhka-{i}.webp')
            scp.append(f'№{p["nomer"]} {p["model"].title()} – {"ситуация" if i == 2 else "сервис"}')
        for st in papka.glob('foto-*.webp'):
            st.unlink()
        for i, f in enumerate(p['foto'], 1):
            webp(put(f), papka / f'foto-{i}.webp', maks=1600, q=84)
        for v in range(1, 5):
            bn.append(papka / f'banner-v{v}.webp')
            bnp.append(f'№{p["nomer"]} {" ".join(p["model"].split()[1:])} В{v}')
    list_(sc, scp, TUT / 'list-sceny.webp', 4)
    list_(bn, bnp, TUT / 'list-bannery.webp', 8, t=240)
    print('сцен', sum(x.exists() for x in sc), 'из', len(sc), '; баннеров', sum(x.exists() for x in bn), 'из', len(bn))


if __name__ == '__main__':
    main()
