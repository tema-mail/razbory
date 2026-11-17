#!/usr/bin/env python3
"""Обложка Дзена 1280×720 в стиле принятой «2003 VS 2026» (Accord 7): картинка + надписи скриптом.

vs:    python3 oblozhka.py vs  <картинка> <выход.webp> <год слева> <год справа> "<нижняя строка>"
zapas: python3 oblozhka.py zag <картинка> <выход.webp> "<верх: строка1|строка2, *акцент*>" "<нижняя строка>"
Текст не влезает – уменьшается кегль; меньше 34 px – ошибка, а не обрезка. Длинное тире – ошибка.
"""
import re
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1280, 720
SHRIFT = '/System/Library/Fonts/Supplemental/Impact.ttf'
BELYY, ZHELTYY, KRASNYY = (255, 255, 255), (255, 214, 0), (230, 32, 32)
POLOSA = 120


def font(px):
    return ImageFont.truetype(SHRIFT, px)


def podognat(d, tekst, shir, start):
    px = start
    while px >= 34:
        if d.textlength(tekst, font=font(px)) <= shir:
            return font(px)
        px -= 2
    raise SystemExit(f'не влезает: {tekst}')


def osnova(put):
    im = Image.open(put).convert('RGB')
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.35))


def polosa(im, tekst):
    d = ImageDraw.Draw(im)
    d.rectangle([0, H - POLOSA, W, H], fill=(0, 0, 0))
    f = podognat(d, tekst, W - 100, 64)
    tw = d.textlength(tekst, font=f)
    bb = d.textbbox((0, 0), tekst, font=f)
    d.text(((W - tw) / 2, H - POLOSA / 2 - (bb[3] + bb[1]) / 2), tekst, font=f, fill=BELYY)


def nadpis(d, xy, tekst, f, cvet):
    d.text(xy, tekst, font=f, fill=cvet, stroke_width=6, stroke_fill=(0, 0, 0))


def vs(src, out, l, r, niz):
    im = osnova(src)
    d = ImageDraw.Draw(im)
    f = font(150)
    fv = font(120)
    y = 26
    for tekst, cx, cvet, ff in ((l, W * 0.25, BELYY, f), (r, W * 0.75, ZHELTYY, f)):
        tw = d.textlength(tekst, font=ff)
        nadpis(d, (cx - tw / 2, y), tekst, ff, cvet)
    tw = d.textlength('VS', font=fv)
    nadpis(d, (W / 2 - tw / 2, y + 22), 'VS', fv, KRASNYY)
    polosa(im, niz)
    return im


def zag(src, out, verh, niz):
    im = osnova(src)
    # затемнение сверху под заголовок
    ten = Image.new('L', (1, 300))
    for yy in range(300):
        ten.putpixel((0, yy), int(200 * (1 - yy / 300) ** 1.4))
    im.paste(Image.new('RGB', (W, 300), (0, 0, 0)), (0, 0), ten.resize((W, 300)))
    d = ImageDraw.Draw(im)
    y = 28
    for stroka in verh.split('|'):
        chist = stroka.replace('*', '')
        f = podognat(d, chist, W - 120, 104)
        x = (W - d.textlength(chist, font=f)) / 2
        ak = False
        for kus in re.split(r'(\*)', stroka):
            if kus == '*':
                ak = not ak
                continue
            if kus:
                nadpis(d, (x, y), kus, f, ZHELTYY if ak else BELYY)
                x += d.textlength(kus, font=f)
        y += int(f.size * 1.08)
    polosa(im, niz)
    return im


if __name__ == '__main__':
    a = sys.argv[1:]
    if any('—' in s for s in a):
        raise SystemExit('длинное тире: только «–»')
    im = vs(a[1], a[2], a[3], a[4], a[5]) if a[0] == 'vs' else zag(a[1], a[2], a[3], a[4])
    im.save(a[2], 'WEBP', quality=86, method=6)
    print('ok', a[2])
