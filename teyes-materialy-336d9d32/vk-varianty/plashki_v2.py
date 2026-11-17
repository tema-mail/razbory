#!/usr/bin/env python3
"""Картинка 2 поста ВК, вторая итерация: 8 разных по дизайну вариантов «экран закрыт, вопрос».

Запуск: python3 vk-varianty/plashki_v2.py [буквы]   (например: python3 vk-varianty/plashki_v2.py a c)
Кадры – реальные фото работы №360 (оригиналы 2560 px: ~/.cache/teyes-keys/src/0360), картинка «было»
для варианта h – vk-varianty/1-shtatnaya-nsk-a.webp. Весь текст и плашки рисует этот скрипт
(HTML → PNG через Playwright, браузер закрывается в finally), нейросеть текст не рисует.
Шрифты: Inter Tight (как в карусели TEYES) и Druk Cyr Heavy для ленты.
Руль, который на двух кадрах перекрывает угол экрана, возвращается поверх плашки отдельным слоем.
Проверки, которые роняют сборку: длинное тире, незагруженный шрифт, текст шире своего поля.
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter
from playwright.sync_api import sync_playwright

KORNI = Path(__file__).resolve().parent.parent
OUT = KORNI / 'vk-varianty'
SRC = Path.home() / '.cache/teyes-keys/src/0360'
RAB = Path.home() / '.cache/teyes-keys/v2'
FONTS = Path.home() / 'Library/Fonts'
W, H = 1600, 1200
GOLUBOY, SINIY, FIOLET, TEMNYY = '#5ABEFF', '#009AE7', '#9A00E7', '#0E1014'
GRAD = 'linear-gradient(100deg,#00A6F7 0%,#1F7BFF 42%,#7A2BF0 78%,#9A00E7 100%)'

# Геометрия в пикселях оригинала: quad – корпус экрана Teyes (ЛВ, ПВ, ПН, ЛН), rul – внешний край обода руля
# сверху вниз (всё, что левее, – руль), nomer – рамки чужих госномеров, которые размываем.
KADRY = {
    'salon': dict(f='telegram_3132_AQADECJrG-ikWUt8.jpg',
                  quad=[(1343, 512), (2350, 443), (2345, 888), (1350, 978)],
                  rul=[(1160, 500), (1220, 550), (1275, 600), (1320, 650), (1360, 700), (1400, 750), (1435, 800),
                       (1465, 850), (1495, 900), (1520, 950), (1537, 1000), (1552, 1050), (1562, 1100)]),
    'kam': dict(f='telegram_3133_AQADESJrG-ikWUt8.jpg',
                quad=[(180, 504), (1587, 465), (1562, 1097), (212, 1093)], rul=None,
                nomer=[(552, 626, 622, 664)]),
    'menu': dict(f='telegram_3134_AQADEiJrG-ikWUt8.jpg',
                 quad=[(425, 700), (1350, 812), (1330, 1478), (428, 1172)], rul=None),
    'navi': dict(f='telegram_3135_AQADEyJrG-ikWUt8.jpg',
                 quad=[(1180, 566), (2163, 503), (2150, 920), (1188, 1028)],
                 rul=[(1050, 500), (1105, 550), (1150, 600), (1190, 650), (1225, 700), (1260, 750), (1295, 800),
                      (1332, 850), (1362, 900), (1390, 950), (1420, 1000), (1440, 1050), (1458, 1100)]),
}


class Kadr:
    """Кроп оригинала, приведённый к размеру mesto[2:] и поставленный на холст в точку mesto[:2]."""

    def __init__(self, imya, crop, mesto=(0, 0, W, H)):
        g = KADRY[imya]
        self.x0, self.y0, x1, y1 = crop
        self.dx, self.dy, w, h = mesto
        self.s = w / (x1 - self.x0)
        if abs((y1 - self.y0) * self.s - h) > 1.5:
            raise SystemExit(f'{imya}: кроп {crop} не той пропорции, что место {mesto}')
        im = Image.open(SRC / g['f']).convert('RGB')
        for b in g.get('nomer', []):
            im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(9)), b[:2])
        self.foto = im.crop(crop).resize((w, h), Image.LANCZOS)
        self.mesto = mesto
        self.quad = [self.pt(p) for p in g['quad']]
        self.rul = [self.pt(p) for p in g['rul']] if g['rul'] else None

    def pt(self, p):
        return ((p[0] - self.x0) * self.s + self.dx, (p[1] - self.y0) * self.s + self.dy)

    def holst(self):
        im = Image.new('RGB', (W, H), TEMNYY)
        im.paste(self.foto, (self.dx, self.dy))
        return im


def gomografiya(w, h, quad):
    """Матрица 3×3: прямоугольник w×h → четырёхугольник quad."""
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    a, b = [], []
    for (x, y), (u, v) in zip(src, quad):
        a += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        b += [u, v]
    k = np.linalg.solve(np.array(a, float), np.array(b, float))
    return np.append(k, 1).reshape(3, 3)


def matrix3d(m):
    v = [m[0, 0], m[1, 0], 0, m[2, 0], m[0, 1], m[1, 1], 0, m[2, 1], 0, 0, 1, 0, m[0, 2], m[1, 2], 0, m[2, 2]]
    return 'matrix3d(' + ','.join(f'{x:.8f}' for x in v) + ')'


def kontur(w, h, quad, r=40, zapas=0, n=8):
    """Точки скруглённого прямоугольника (с запасом наружу), перенесённые на кадр."""
    m = gomografiya(w, h, quad)
    x0, y0, x1, y1 = -zapas, -zapas, w + zapas, h + zapas
    pts = []
    for cx, cy, a0 in ((x1 - r, y0 + r, -90), (x1 - r, y1 - r, 0), (x0 + r, y1 - r, 90), (x0 + r, y0 + r, 180)):
        for i in range(n + 1):
            a = np.radians(a0 + 90 * i / n)
            pts.append((cx + r * np.cos(a), cy + r * np.sin(a)))
    res = []
    for x, y in pts:
        u, v, t = m @ np.array([x, y, 1.0])
        res.append((u / t, v / t))
    return res


def css_poly(pts):
    return 'polygon(' + ','.join(f'{x:.1f}px {y:.1f}px' for x, y in pts) + ')'


def maska_rulya(rul, mesto):
    m = Image.new('L', (W, H), 0)
    if rul:
        poly = list(rul) + [(rul[-1][0] - 1200, rul[-1][1]), (rul[0][0] - 1200, rul[0][1])]
        ImageDraw.Draw(m).polygon(poly, fill=255)
        ramka = Image.new('L', (W, H), 0)
        ImageDraw.Draw(ramka).rectangle((mesto[0], mesto[1], mesto[0] + mesto[2] - 1, mesto[1] + mesto[3] - 1), fill=255)
        m = Image.composite(m, Image.new('L', (W, H), 0), ramka).filter(ImageFilter.GaussianBlur(1.3))
    return m


def sohr(im, imya):
    RAB.mkdir(parents=True, exist_ok=True)
    put = RAB / imya
    im.save(put, quality=93) if put.suffix == '.jpg' else im.save(put)
    return put.as_uri()


def sloy_rulya(fon, kadr, imya):
    im = fon.convert('RGBA')
    im.putalpha(maska_rulya(kadr.rul, kadr.mesto))
    return sohr(im, imya)


def razmytie(fon, radius, zatemnit=0.0, yarkost=1.0, tsvet=(10, 12, 16)):
    im = fon.filter(ImageFilter.GaussianBlur(radius))
    if yarkost != 1.0:
        im = ImageEnhance.Brightness(im).enhance(yarkost)
    return Image.blend(im, Image.new('RGB', im.size, tsvet), zatemnit) if zatemnit else im


def shrift(ves, fajl, semya='IT'):
    return f'@font-face{{font-family:{semya};font-weight:{ves};src:url("{(FONTS / fajl).as_uri()}")}}'


CSS = '\n'.join([
    shrift(300, 'InterTight-Light.ttf'), shrift(500, 'InterTight-Medium.ttf'), shrift(600, 'InterTight-SemiBold.ttf'),
    shrift(800, 'InterTight-ExtraBold.ttf'), shrift(900, 'InterTight-Black.ttf'),
    shrift(900, 'Druk Cyr Heavy.otf', 'Druk'),
    f'html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:{TEMNYY}}}',
    '*{box-sizing:border-box}',
    f'.l{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}',
    '.pl{position:absolute;left:0;top:0;transform-origin:0 0}',
    '.t{white-space:nowrap;position:absolute}',
    '.c{position:absolute;inset:0;display:flex;align-items:center}',
])


def sloy(url, dop=''):
    return f'<div class="l" style="background:url(\'{url}\') 0 0/{W}px {H}px no-repeat;{dop}"></div>'


def v_a():
    """А. Сильная: яркая плашка TEYES по корпусу экрана, почти во всю ширину баннера."""
    k = Kadr('kam', (85, 180, 1685, 1380))
    fon = k.holst()
    w, h = 1400, 628
    return f'''{sloy(sohr(fon, 'a-fon.jpg'))}
<div class="l" style="background:radial-gradient(ellipse 80% 75% at 50% 50%,rgba(0,0,0,0) 48%,rgba(0,0,0,.55) 100%)"></div>
<div class="pl" style="width:{w}px;height:{h}px;transform:{matrix3d(gomografiya(w, h, k.quad))}">
 <div style="position:absolute;inset:-10px;border-radius:54px;background:{GRAD};overflow:hidden;
  box-shadow:0 34px 80px rgba(0,0,0,.6),inset 0 0 0 3px rgba(255,255,255,.3)">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.22),rgba(255,255,255,0) 44%)"></div>
  <div style="position:absolute;right:-6px;top:-150px;font:900 880px/1 IT;color:rgba(255,255,255,.14)">?</div>
  <div class="c" style="padding-left:84px"><div class="t" data-maxw="1250" data-maxh="600"
   style="position:static;font:900 178px/.98 IT;color:#fff;letter-spacing:-.012em;text-shadow:0 4px 0 rgba(0,20,80,.18)">Что станет<br>со штатным<br>меню BMW?</div></div>
 </div>
</div>'''


def v_b():
    """Б. Сильная: красная лента-пломба наискось через весь баннер, экран под ней заглушён."""
    k = Kadr('navi', (0, 0, 2560, 1920))
    fon = k.holst()
    cx = sum(p[0] for p in k.quad) / 4
    cy = sum(p[1] for p in k.quad) / 4
    ly = cy + (cx - W / 2) * np.tan(np.radians(7.5))  # центр ленты – середина баннера, линия идёт через центр экрана
    return f'''{sloy(sohr(fon, 'b-fon.jpg'))}
{sloy(sohr(razmytie(fon, 20, 0.62), 'b-blur.jpg'), 'clip-path:' + css_poly(kontur(1150, 500, k.quad, zapas=4)))}
<img class="l" src="{sloy_rulya(fon, k, 'b-rul.png')}">
<div class="l" style="background:linear-gradient(180deg,rgba(0,0,0,.25),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 70%,rgba(0,0,0,.35))"></div>
<div style="position:absolute;left:{cx - 1200:.0f}px;top:{cy - 34 + 40:.0f}px;width:2400px;height:68px;transform:rotate(15deg);
 background:repeating-linear-gradient(-45deg,#FFD21F 0 30px,#16181d 30px 60px);box-shadow:0 10px 26px rgba(0,0,0,.55)"></div>
<div style="position:absolute;left:{W / 2 - 1200:.0f}px;top:{ly - 92:.0f}px;width:2400px;height:184px;transform:rotate(-7.5deg);
 background:linear-gradient(180deg,#F1323B,#D8141F);box-shadow:0 16px 36px rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center">
 <div style="position:absolute;left:0;right:0;top:12px;border-top:4px dashed rgba(255,255,255,.6)"></div>
 <div style="position:absolute;left:0;right:0;bottom:12px;border-top:4px dashed rgba(255,255,255,.6)"></div>
 <div class="t" data-maxw="1540" data-maxh="150" style="position:static;font:900 122px/1 Druk;color:#fff;letter-spacing:.022em;
  text-transform:uppercase;padding-top:6px">Что станет со штатным меню BMW?</div>
</div>'''


def v_c():
    """В. Чисто закрывает: матовое стекло точно по корпусу экрана, в перспективе; вопрос на нём."""
    k = Kadr('menu', (150, 480, 1750, 1680))
    fon = k.holst()
    w, h = 1150, 560
    return f'''{sloy(sohr(fon, 'c-fon.jpg'))}
{sloy(sohr(razmytie(fon, 34, 0.56, tsvet=(18, 24, 34)), 'c-blur.jpg'), 'clip-path:' + css_poly(kontur(w, h, k.quad, zapas=3)))}
<div class="pl" style="width:{w}px;height:{h}px;transform:{matrix3d(gomografiya(w, h, k.quad))}">
 <div style="position:absolute;inset:-3px;border-radius:44px;overflow:hidden;
  box-shadow:inset 0 0 0 3px rgba(255,255,255,.30),inset 0 0 60px rgba(255,255,255,.07);
  background:linear-gradient(118deg,rgba(255,255,255,.20) 0%,rgba(255,255,255,.03) 26%,rgba(255,255,255,0) 60%,rgba(255,255,255,.08) 100%)">
  <div style="position:absolute;left:-10%;top:-40%;width:42%;height:180%;transform:rotate(18deg);
   background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.10),rgba(255,255,255,0))"></div>
  <div class="c" style="padding-left:70px;padding-bottom:26px"><div class="t" data-maxw="1030" data-maxh="420"
   style="position:static;font:800 172px/1.0 IT;color:#fff;letter-spacing:-.012em">А штатное<br><span style="color:{GOLUBOY}">меню BMW?</span></div></div>
  <div class="t" data-maxw="700" data-maxh="50" style="left:74px;bottom:38px;font:600 36px/1 IT;color:rgba(255,255,255,.62)">BMW X5 E70 · Teyes 12″</div>
 </div>
</div>'''


def v_d():
    """Г. Чисто закрывает: экран в пикселях, на нём маленький знак вопроса; вопрос – полосой под кадром."""
    vf = 900
    k = Kadr('salon', (660, 190, 2560, 190 + round(1900 * vf / W)), (0, 0, W, vf))
    fon = k.holst()
    blok = 30
    mel = fon.resize((W // blok + 1, H // blok + 1), Image.BOX).resize(((W // blok + 1) * blok, (H // blok + 1) * blok), Image.NEAREST).crop((0, 0, W, H))
    mel = Image.blend(mel, Image.new('RGB', (W, H), (12, 14, 20)), 0.12)
    m = Image.new('L', (W, H), 0)
    ImageDraw.Draw(m).polygon(kontur(1150, 500, k.quad, zapas=4), fill=255)
    m = Image.composite(Image.new('L', (W, H), 0), m, maska_rulya(k.rul, k.mesto)).filter(ImageFilter.GaussianBlur(1.2))
    fon.paste(mel, (0, 0), m)
    cx = sum(p[0] for p in k.quad) / 4 + 14
    cy = sum(p[1] for p in k.quad) / 4
    return f'''{sloy(sohr(fon, 'd-fon.jpg'))}
<div style="position:absolute;left:{cx - 62:.0f}px;top:{cy - 62:.0f}px;width:124px;height:124px;border-radius:50%;background:#fff;
 box-shadow:0 10px 30px rgba(0,0,0,.55),0 0 0 8px rgba(255,255,255,.22);display:flex;align-items:center;justify-content:center;
 font:900 92px/1 IT;color:{TEMNYY}">?</div>
<div style="position:absolute;left:0;top:{vf}px;width:{W}px;height:{H - vf}px;background:{TEMNYY}">
 <div style="position:absolute;left:0;top:0;width:100%;height:10px;background:{GRAD}"></div>
 <div class="c" style="padding:10px 0 0 60px"><div class="t" data-maxw="1490" data-maxh="{H - vf - 30}"
  style="position:static;font:900 124px/1.03 IT;color:#fff;letter-spacing:-.01em">Что станет со штатным<br><span style="color:{GOLUBOY}">меню BMW?</span></div></div>
</div>'''


def v_e():
    """Д. Слабая: полупрозрачное стекло, тонкий текст, карта на экране угадывается."""
    k = Kadr('navi', (860, 300, 2460, 1500))
    fon = k.holst()
    w, h = 1150, 500
    return f'''{sloy(sohr(fon, 'e-fon.jpg'))}
{sloy(sohr(razmytie(fon, 7, 0.46, tsvet=(14, 18, 26)), 'e-blur.jpg'), 'clip-path:' + css_poly(kontur(w, h, k.quad, zapas=2)))}
<div class="pl" style="width:{w}px;height:{h}px;transform:{matrix3d(gomografiya(w, h, k.quad))}">
 <div style="position:absolute;inset:-2px;border-radius:42px;box-shadow:inset 0 0 0 2px rgba(255,255,255,.42);
  background:linear-gradient(120deg,rgba(255,255,255,.14),rgba(255,255,255,0) 35%)">
  <div class="c" style="justify-content:flex-end;padding-right:76px"><div class="t" data-maxw="820" data-maxh="430"
   style="position:static;font:300 108px/1.1 IT;color:#fff;letter-spacing:-.005em;text-align:left">Что станет<br>со штатным<br>меню BMW?</div></div>
 </div>
</div>
<img class="l" src="{sloy_rulya(fon, k, 'e-rul.png')}">'''


def v_f():
    """Е. Без плашки: кадр затемнён, экран – световое пятно, крупный вопрос по центру баннера."""
    k = Kadr('salon', (0, 0, 2560, 1920))
    fon = k.holst()
    w, h = 1150, 500
    cx = sum(p[0] for p in k.quad) / 4
    cy = sum(p[1] for p in k.quad) / 4
    return f'''{sloy(sohr(fon, 'f-fon.jpg'))}
<div class="pl" style="width:{w}px;height:{h}px;transform:{matrix3d(gomografiya(w, h, k.quad))}">
 <div style="position:absolute;inset:20px;border-radius:40px;box-shadow:0 0 150px 70px rgba(150,175,255,.55)"></div></div>
{sloy(sohr(razmytie(fon, 30, yarkost=1.5), 'f-blur.jpg'), 'clip-path:' + css_poly(kontur(w, h, k.quad, zapas=4)))}
<img class="l" src="{sloy_rulya(fon, k, 'f-rul.png')}">
<div class="l" style="background:radial-gradient(ellipse 560px 330px at {cx:.0f}px {cy:.0f}px,rgba(6,8,12,0) 0%,rgba(6,8,12,.18) 45%,rgba(6,8,12,.80) 100%)"></div>
<div class="l" style="background:linear-gradient(180deg,rgba(6,8,12,0) 46%,rgba(6,8,12,.55) 70%,rgba(6,8,12,.78) 100%)"></div>
<div class="l" style="top:652px;height:{H - 652}px;display:flex;justify-content:center;align-items:flex-start"><div class="t" data-maxw="1500" data-maxh="530"
 style="position:static;text-align:center;font:900 172px/1.0 IT;color:#fff;letter-spacing:-.012em;text-shadow:0 6px 30px rgba(0,0,0,.6)">Что станет<br>со штатным<br><span style="color:{GOLUBOY}">меню BMW?</span></div></div>'''


def marker_ellips(cx, cy, rx, ry, naklon=-2.0):
    """Обводка «от руки»: эллипс чуть больше оборота, радиус плывёт."""
    pts = []
    for i in range(0, 141):
        t = -2.2 + (2 * np.pi + 0.55) * i / 140
        kf = 1 + 0.045 * (i / 140) - 0.012 * np.sin(3 * t)
        x, y = rx * kf * np.cos(t), ry * kf * np.sin(t)
        a = np.radians(naklon)
        pts.append((cx + x * np.cos(a) - y * np.sin(a), cy + x * np.sin(a) + y * np.cos(a)))
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)


def v_g():
    """Ж. Без плашки: вопрос сверху, маркер обводит экран и стрелкой показывает на него."""
    k = Kadr('kam', (0, 0, 1920, 1440))
    fon = k.holst()
    cx = sum(p[0] for p in k.quad) / 4
    cy = sum(p[1] for p in k.quad) / 4
    kr = '#FF3B2F'
    return f'''{sloy(sohr(fon, 'g-fon.jpg'))}
<div class="l" style="background:linear-gradient(180deg,rgba(8,10,14,.90) 0%,rgba(8,10,14,.78) 22%,rgba(8,10,14,0) 37%,rgba(8,10,14,0) 80%,rgba(8,10,14,.5) 100%)"></div>
<svg class="l" viewBox="0 0 {W} {H}" fill="none" stroke="{kr}" stroke-linecap="round" stroke-linejoin="round">
 <path d="{marker_ellips(cx, cy + 4, 632, 300)}" stroke-width="15"/>
 <path d="M664 300 C 800 318, 980 316, 1128 286" stroke-width="15"/>
 <path d="M1262 226 C 1420 236, 1500 300, 1452 398" stroke-width="15"/>
 <path d="M1406 356 L1448 404 L1508 366" stroke-width="15"/>
</svg>
<div class="t" data-maxw="1500" data-maxh="290" style="left:62px;top:36px;font:900 126px/1.04 IT;color:#fff;letter-spacing:-.012em">Что станет со штатным<br><span style="padding-left:600px">меню BMW?</span></div>'''


def v_h():
    """З. «Было → стало?»: слева штатный экран (картинка 1), справа Teyes под плашкой со знаком вопроса."""
    bylo = Image.open(OUT / '1-shtatnaya-nsk-a.webp').convert('RGB')
    bw, bh = bylo.size
    bylo = bylo.crop((bw // 2, 0, bw, bh)).resize((W // 2, H), Image.LANCZOS)
    k = Kadr('salon', (1280, 0, 2560, 1920), (W // 2, 0, W // 2, H))
    fon = k.holst()
    fon.paste(bylo, (0, 0))
    w, h = 1150, 500
    plash = 'display:inline-block;padding:14px 30px 16px;border-radius:999px;font:900 50px/1 IT;letter-spacing:.06em;color:#fff'
    return f'''{sloy(sohr(fon, 'h-fon.jpg'))}
<div class="pl" style="width:{w}px;height:{h}px;transform:{matrix3d(gomografiya(w, h, k.quad))}">
 <div style="position:absolute;inset:-8px;border-radius:50px;background:{GRAD};overflow:hidden;
  box-shadow:0 26px 60px rgba(0,0,0,.6),inset 0 0 0 3px rgba(255,255,255,.3)">
  <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(255,255,255,.22),rgba(255,255,255,0) 44%)"></div>
  <div class="c" style="justify-content:center;padding-left:90px"><div class="t" data-maxw="500" data-maxh="520"
   style="position:static;font:900 470px/1 IT;color:#fff;text-shadow:0 6px 0 rgba(0,20,80,.2)">?</div></div>
 </div>
</div>
<img class="l" src="{sloy_rulya(fon, k, 'h-rul.png')}">
<div class="l" style="background:linear-gradient(180deg,rgba(6,8,12,.55) 0%,rgba(6,8,12,0) 17%,rgba(6,8,12,0) 58%,rgba(6,8,12,.88) 80%,rgba(6,8,12,.96) 100%)"></div>
<div style="position:absolute;left:{W // 2 - 4}px;top:0;width:8px;height:{H}px;background:#fff"></div>
<div style="position:absolute;left:{W // 2 - 62}px;top:520px;width:124px;height:124px;border-radius:50%;background:#fff;
 box-shadow:0 8px 28px rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;font:900 84px/1 IT;color:{TEMNYY};padding-bottom:10px">→</div>
<div class="t" data-maxw="400" data-maxh="90" style="left:40px;top:40px;{plash};background:rgba(14,16,20,.82)">БЫЛО</div>
<div class="t" data-maxw="400" data-maxh="90" style="left:{W // 2 + 44}px;top:40px;{plash};background:{GRAD}">СТАЛО</div>
<div class="l" style="top:918px;height:{H - 918}px;display:flex;justify-content:center;align-items:flex-start"><div class="t" data-maxw="1500" data-maxh="270"
 style="position:static;text-align:center;font:900 124px/1.04 IT;color:#fff;letter-spacing:-.012em">Что станет со штатным<br><span style="color:{GOLUBOY}">меню BMW?</span></div></div>'''


VARIANTY = {'a': v_a, 'b': v_b, 'c': v_c, 'd': v_d, 'e': v_e, 'f': v_f, 'g': v_g, 'h': v_h}

PROVERKA_JS = '''async () => {
  await document.fonts.ready;
  const plohie = [...document.fonts].filter(f => f.status === 'error').map(f => f.family + ' ' + f.weight);
  const net = [...document.querySelectorAll('.t')].map(e => getComputedStyle(e)).filter(c => !document.fonts.check(c.fontWeight + ' 40px ' + c.fontFamily)).map(c => c.fontWeight + ' ' + c.fontFamily);
  const tesno = [...document.querySelectorAll('.t')].filter(e => e.offsetWidth > +e.dataset.maxw || e.offsetHeight > +e.dataset.maxh)
    .map(e => e.textContent.trim().slice(0, 24) + ': ' + e.offsetWidth + '×' + e.offsetHeight + ' при поле ' + e.dataset.maxw + '×' + e.dataset.maxh);
  return {plohie, net, tesno, polya: document.querySelectorAll('.t').length};
}'''


def brauzer_put():
    """Свежий уже скачанный headless-Chromium Playwright: версия пакета Python может не совпасть с кэшем."""
    kesh = Path.home() / 'Library/Caches/ms-playwright'
    est = sorted(kesh.glob('chromium_headless_shell-*/chrome-headless-shell-mac-arm64/chrome-headless-shell'))
    return {'executable_path': str(est[-1])} if est else {}


def main(bukvy):
    RAB.mkdir(parents=True, exist_ok=True)
    brauzer = None
    with sync_playwright() as p:
        try:
            brauzer = p.chromium.launch(headless=True, **brauzer_put())
            str_ = brauzer.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            for b in bukvy:
                telo = VARIANTY[b]()
                if '—' in telo:
                    raise SystemExit(f'{b}: длинное тире, только «–»')
                html = RAB / f'{b}.html'
                html.write_text(f'<!doctype html><html lang="ru"><meta charset="utf-8"><style>{CSS}</style><body>{telo}</body></html>', encoding='utf-8')
                str_.goto(html.as_uri())
                str_.wait_for_load_state('networkidle')
                itog = str_.evaluate(PROVERKA_JS)
                if itog['plohie'] or itog['net'] or itog['tesno'] or not itog['polya']:
                    raise SystemExit(f'{b}: проверка вёрстки не пройдена: {itog}')
                png = RAB / f'{b}.png'
                str_.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': W, 'height': H})
                im = Image.open(png).convert('RGB')
                put = OUT / f'2-plashka-v2-{b}.webp'
                im.save(put, 'WEBP', quality=88, method=6)
                im.resize((390, 293), Image.LANCZOS).save(RAB / f'{b}-390.png')
                print(f'{put.name}: {im.size[0]}×{im.size[1]}, {put.stat().st_size // 1024} КБ, текстовых полей {itog["polya"]}')
        finally:
            if brauzer:
                brauzer.close()


if __name__ == '__main__':
    bukvy = sys.argv[1:] or list(VARIANTY)
    if any(b not in VARIANTY for b in bukvy):
        raise SystemExit(f'буквы: {" ".join(VARIANTY)}')
    main(bukvy)
