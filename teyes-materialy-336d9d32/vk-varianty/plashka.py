#!/usr/bin/env python3
"""Картинка 2 поста ВК: реальный кадр BMW X5 E70, экран мультимедиа закрыт плашкой с вопросом.

Запуск: python3 vk-varianty/plashka.py  (из папки teyes-materialy-336d9d32)
Плашку и текст рисует этот скрипт, не нейросеть. Шрифт и цвета – как в карусели TEYES
(~/Sites/redakciya/scripts/karusel.py): Inter Tight ExtraBold/SemiBold, голубой акцент (90,190,255).
Стили: temnaya – матовое стекло (экран размыт и затемнён); yarkaya – сплошная голубая плашка TEYES.
Проверка: длинное тире или текст, который не влез, роняют сборку.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

KORNI = Path(__file__).resolve().parent.parent
KEYS = KORNI / 'keys'
OUT = KORNI / 'vk-varianty'
F_ZAG = Path.home() / 'Library/Fonts/InterTight-ExtraBold.ttf'
F_MEL = Path.home() / 'Library/Fonts/InterTight-SemiBold.ttf'
GOLUBOY = (90, 190, 255)
BELYY = (255, 255, 255)
CHERNYY = (14, 16, 20)
RAZMER = (1600, 1200)

# Кадры: исходник, рамка корпуса экрана Teyes (x1, y1, x2, y2) в пикселях исходника, кроп 4:3.
KADRY = {
    'salon': ('bmw-x5-e70-teyes-cc3-salon.webp', (838, 274, 1472, 592), (300, 60, 1600, 1035)),
    'navi': ('bmw-x5-e70-teyes-cc3-navigaciya.webp', (734, 312, 1358, 618), (130, 0, 1600, 1102)),
}

VARIANTY = [
    ('a', 'salon', 'temnaya', 'Что станет со штатным *меню BMW?*'),
    ('b', 'salon', 'yarkaya', 'Что станет со штатным меню BMW?'),
    ('c', 'salon', 'temnaya', 'Камера, климат, меню BMW – *что останется?*'),
    ('d', 'salon', 'yarkaya', 'Штатная система BMW – что с ней после Teyes?'),
    ('e', 'navi', 'temnaya', 'Поменяли экран. *А iDrive?*'),
    ('f', 'navi', 'yarkaya', 'Поменяли экран. А iDrive?'),
]
PODPIS = 'BMW X5 E70 · Teyes 12″'


def slova(tekst):
    res, ak = [], False
    for kus in tekst.split('*'):
        res += [(s, ak) for s in kus.split()]
        ak = not ak
    return res


def perenos(d, tekst, f, shir):
    stroki, tek = [], []
    for s, a in slova(tekst):
        proba = tek + [(s, a)]
        if tek and d.textlength(' '.join(x for x, _ in proba), font=f) > shir:
            stroki.append(tek)
            tek = [(s, a)]
        else:
            tek = proba
    stroki.append(tek)
    # висячее тире в начале строки – вернуть на прошлую строку
    for i in range(1, len(stroki)):
        if stroki[i] and stroki[i][0][0] == '–':
            stroki[i - 1].append(stroki[i].pop(0))
    return [s for s in stroki if s]


def podobrat(d, tekst, shir, vys, maks=112, mini=56):
    for r in range(maks, mini - 1, -2):
        f = ImageFont.truetype(str(F_ZAG), r)
        st = perenos(d, tekst, f, shir)
        if len(st) <= 3 and all(d.textlength(' '.join(x for x, _ in s), font=f) <= shir for s in st) \
                and len(st) * r * 1.08 <= vys:
            # выровнять строки: сужать ширину, пока число строк то же (без одинокого слова внизу)
            sh = shir
            while sh > shir * 0.55 and len(perenos(d, tekst, f, sh - 10)) == len(st):
                sh -= 10
            return f, r, perenos(d, tekst, f, sh)
    raise SystemExit(f'текст не влезает: {tekst}')


def sobrat(bukva, kadr, stil, tekst):
    if '—' in tekst:
        raise SystemExit('длинное тире: только «–»')
    fajl, (x1, y1, x2, y2), krop = KADRY[kadr]
    src = Image.open(KEYS / fajl).convert('RGB')
    m = 16  # плашка чуть больше корпуса экрана
    box = (x1 - m, y1 - m, x2 + m, y2 + m)
    w, h = box[2] - box[0], box[3] - box[1]
    rad = 34
    maska = Image.new('L', (w, h), 0)
    ImageDraw.Draw(maska).rounded_rectangle((0, 0, w - 1, h - 1), rad, fill=255)

    if stil == 'temnaya':
        pod = src.crop(box).filter(ImageFilter.GaussianBlur(28))
        pod = Image.blend(pod, Image.new('RGB', (w, h), (10, 12, 16)), 0.64)
        tsvet, akcent, tsvet_pod = BELYY, GOLUBOY, (170, 180, 190)
    else:
        pod = Image.new('RGB', (w, h), GOLUBOY)
        tsvet, akcent, tsvet_pod = CHERNYY, CHERNYY, (20, 40, 60)

    # тень под плашкой
    ten = Image.new('L', src.size, 0)
    ImageDraw.Draw(ten).rounded_rectangle((box[0] + 6, box[1] + 12, box[2] + 6, box[3] + 12), rad, fill=150)
    ten = ten.filter(ImageFilter.GaussianBlur(18))
    src.paste(Image.new('RGB', src.size, (0, 0, 0)), (0, 0), ten)
    src.paste(pod, box[:2], maska)
    d = ImageDraw.Draw(src)
    if stil == 'temnaya':
        d.rounded_rectangle(box, rad, outline=(120, 132, 145), width=2)
        d.rounded_rectangle((box[0] + 2, box[1] + 2, box[2] - 2, box[3] - 2), rad - 2, outline=(70, 80, 90), width=1)

    pole_x, pole_y = 46, 34
    f_mel = ImageFont.truetype(str(F_MEL), 30)
    vys_pod = 30 + 22
    f, r, stroki = podobrat(d, tekst, w - 2 * pole_x, h - 2 * pole_y - vys_pod)
    lh = int(r * 1.08)
    blok = len(stroki) * lh + vys_pod
    y = box[1] + (h - blok) // 2 - 4
    for st in stroki:
        x = box[0] + pole_x
        for i, (s, a) in enumerate(st):
            d.text((x, y), s, font=f, fill=akcent if a else tsvet)
            x += d.textlength(s + ' ', font=f)
        y += lh
    y += 22
    d.text((box[0] + pole_x, y), PODPIS, font=f_mel, fill=tsvet_pod)

    im = src.crop(krop).resize(RAZMER, Image.LANCZOS)
    put = OUT / f'2-plashka-{bukva}.webp'
    im.save(put, 'WEBP', quality=88, method=6)
    return put, r, len(stroki)


if __name__ == '__main__':
    for v in VARIANTY:
        put, r, n = sobrat(*v)
        print(f'{put.name}: кегль {r} px в исходнике, строк {n}')
