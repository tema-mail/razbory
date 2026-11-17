#!/usr/bin/env python3
"""Контактные листы: kontakt-oblozhki.webp (все обложки статей) и kontakt-kartochki.webp (все карточки каруселей)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

K = Path(__file__).resolve().parent.parent
F = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 20)
STATI = ['xtrail-t32', 'note-e12', 'lc200', 'solaris-2', 'juke-f15', 'shuttle']
KARUSELI = ['karusel-kitay', 'karusel-sugrob', 'karusel-prisoska']


def list_(kadry, kol, w, h, out):
    rows = (len(kadry) + kol - 1) // kol
    c = Image.new('RGB', (kol * (w + 10) + 10, rows * (h + 40) + 10), 'white')
    d = ImageDraw.Draw(c)
    for i, (put, podpis) in enumerate(kadry):
        x, y = 10 + (i % kol) * (w + 10), 10 + (i // kol) * (h + 40)
        if put.exists():
            im = Image.open(put).convert('RGB')
            im.thumbnail((w, h))
            c.paste(im, (x, y))
        else:
            d.rectangle([x, y, x + w, y + h], outline='red', width=3)
        d.text((x, y + h + 8), podpis, font=F, fill='black')
    c.save(K / out, 'WEBP', quality=80)
    print('ok', out, len(kadry))


if __name__ == '__main__':
    ob = []
    for s in STATI:
        ob += [(K / s / 'oblozhka-1-vs.webp', f'{s} – основная'), (K / s / 'oblozhka-2-zapas.webp', f'{s} – запасная')]
    list_(ob, 2, 640, 360, 'kontakt-oblozhki.webp')
    ka = []
    for k in KARUSELI:
        for f in sorted((K / k).glob('[0-9][0-9]-*.webp')):
            ka.append((f, f'{k[8:]} {f.name[:2]}'))
    list_(ka, 7, 300, 375, 'kontakt-kartochki.webp')
