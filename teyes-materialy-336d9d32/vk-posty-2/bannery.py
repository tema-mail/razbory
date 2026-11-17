#!/usr/bin/env python3
"""Обложка 1 – баннер в четырёх вариантах (В1–В4) для каждого из 10 постов. Вёрстка HTML → PNG через Playwright.
Мало текста: маленький логотип, заголовок-мысль, марка-модель с работой; без нижней плашки, без ряда преимуществ, без строки у логотипа.
Кадры – только реальные фото работы (номера закрыты в prep2.py), машин не рисуем.

Запуск: python3 bannery.py [номер поста …]  →  <папка поста>/banner-v1…v4.webp
В1 – «после» во весь кадр, «до» маленькой вставкой; В2 – главный кадр на 2/3, внизу узкая полоса из двух кадров;
В3 – заголовок и один кадр «после»; В4 – разрез по диагонали.
"""
import sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
from posty import POSTY, KESH, put

TUT = Path(__file__).resolve().parent
FONTS = Path.home() / 'Library/Fonts'
LOGO = KESH / 'logo/logo.svg'
W, H = 1086, 1448
RAB = KESH / 'card2'


def shrift(semya, ves, fajl):
    return f'@font-face{{font-family:{semya};font-weight:{ves};src:url("{(FONTS / fajl).as_uri()}")}}'


def zagolovok(stroki):
    out = []
    for s in stroki:
        while '*' in s:
            s = s.replace('*', '<b>', 1).replace('*', '</b>', 1)
        out.append(s)
    return '<br>'.join(out)


def brauzer_put():
    for p in sorted((Path.home() / 'Library/Caches/ms-playwright').glob('chromium_headless_shell-*/*/chrome-headless-shell'), reverse=True):
        return {'executable_path': str(p)}
    return {}


def css(a):
    return '\n'.join([
        shrift('G', 800, 'Gilroy-ExtraBold.otf'), shrift('IT', 500, 'InterTight-Medium.ttf'), shrift('B', 700, 'BebasNeue Bold.otf'),
        f'''*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#0d0f12;color:#fff;font-family:IT,sans-serif}}
.ram{{position:absolute;overflow:hidden;background:#000}}
.ram img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.sh{{position:absolute;left:0;width:{W}px}}
.logo{{position:absolute;left:56px;top:50px;width:176px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.6))}}
h1{{position:absolute;left:54px;font:800 88px/.98 G;letter-spacing:-.022em;text-shadow:0 3px 30px rgba(0,0,0,.7)}}
h1 b{{color:{a};font-weight:800}}
.model{{position:absolute;left:56px;font:700 58px/1 B;letter-spacing:.03em;text-shadow:0 2px 18px rgba(0,0,0,.7)}}
.model small{{display:block;margin-top:8px;font:500 26px/1.18 IT;letter-spacing:0;color:rgba(255,255,255,.9)}}
.k{{border-radius:18px;border:2.5px solid rgba(255,255,255,.9);box-shadow:0 16px 44px rgba(0,0,0,.6)}}
.ya{{position:absolute;left:0;top:0;height:42px;padding:0 18px 0 14px;display:flex;align-items:center;font:700 24px/1 B;letter-spacing:.1em;border-radius:0 0 14px 0;background:rgba(14,16,20,.9);white-space:nowrap;z-index:2}}
.ya.a{{background:{a};color:#0d0f12}}
.pil{{position:absolute;height:48px;padding:0 20px;display:flex;align-items:center;font:700 27px/1 B;letter-spacing:.1em;border-radius:24px;background:rgba(14,16,20,.86);white-space:nowrap}}
.pil.a{{background:{a};color:#0d0f12}}'''])


def kadr(f, poz, zum=1.0, stil='', klass='ram', podpis='', akc=False):
    tr = f'transform:scale({zum});transform-origin:{poz};' if zum != 1 else ''
    ya = f'<span class="ya{" a" if akc else ""}">{podpis}</span>' if podpis else ''
    return f'<div class="{klass}" style="{stil}"><img src="{put(f).as_uri()}" style="object-position:{poz};{tr}">{ya}</div>'


def shapka(p, top=150):
    return f'<img class="logo" src="{LOGO.as_uri()}"><h1 style="top:{top}px">{zagolovok(p["zag"])}</h1>'


def model(p, top, dop=''):
    return f'<div class="model" style="top:{top}px;{dop}">{p["model"]}<small>{p["pod"]}</small></div>'


def strelka(x, y, w=96):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.6))" viewBox="0 0 128 76">'
            '<path d="M6 14c18 44 56 54 100 40" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
            '<path d="M90 30l22 22-28 12" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def podpisi(p):
    return ('ДО', 'ПОСЛЕ') if p['para'] else (p['do'][2], p['posle_podpis'])


def v1(p):
    """«После» во весь кадр, заголовок сверху, «до» маленькой вставкой в правом нижнем углу."""
    f, poz, zum = p['posle']
    df, dpoz, _ = p['do']
    pd, _ = podpisi(p)
    return (kadr(f, poz, zum, f'left:0;top:0;width:{W}px;height:{H}px')
            + '<div class="sh" style="top:0;height:640px;background:linear-gradient(180deg,rgba(9,11,14,.93) 0,rgba(9,11,14,.72) 55%,rgba(9,11,14,0) 100%)"></div>'
            + f'<div class="sh" style="top:1020px;height:{H - 1020}px;background:linear-gradient(180deg,rgba(9,11,14,0) 0,rgba(9,11,14,.9) 75%)"></div>'
            + shapka(p) + model(p, 1290)
            + kadr(df, dpoz, p.get('dz', 1.0), 'left:756px;top:1150px;width:290px;height:240px', 'ram k', 'БЫЛО' if p['para'] else pd))


def v2(p):
    """Главный кадр на 2/3, заголовок поверх, внизу узкая полоса из двух небольших кадров."""
    gf, gpoz, gzum = p['glav']
    df, dpoz, _ = p['do']
    pf, ppoz, _ = p['posle']
    pd, pp = podpisi(p)
    return (kadr(gf, gpoz, gzum, f'left:0;top:0;width:{W}px;height:1010px')
            + '<div class="sh" style="top:0;height:1012px;background:linear-gradient(180deg,rgba(9,11,14,.9) 0,rgba(9,11,14,.6) 34%,rgba(9,11,14,0) 60%,rgba(13,15,18,.25) 86%,#0d0f12 100%)"></div>'
            + shapka(p) + model(p, 1150)
            + kadr(df, dpoz, p.get('dz', 1.0), 'left:520px;top:1080px;width:236px;height:196px', 'ram k', pd)
            + kadr(pf, ppoz, 1.0, 'left:790px;top:1070px;width:256px;height:216px', 'ram k', pp, True)
            + (strelka(722, 1214, 80) if p['para'] else ''))


def v3(p):
    """Только заголовок, марка-модель и один сильный кадр «после»."""
    f, poz = p['v3']
    _, pp = podpisi(p)
    return ('<div class="sh" style="top:0;height:1448px;background:radial-gradient(120% 60% at 30% 0,#1c2026 0,#0d0f12 70%)"></div>'
            + shapka(p) + model(p, 470)
            + kadr(f, poz, 1.0, f'left:40px;top:650px;width:{W - 80}px;height:750px;border-radius:24px', 'ram k',
                   'ПОСЛЕ УСТАНОВКИ' if p['para'] else pp, True))


def v4(p):
    """Разрез по диагонали: слева «до», справа «после»; заголовок над разрезом, подписи в углах."""
    (lf, lpoz, lzum), (rf, rpoz, rzum) = p['v4']
    pd, pp = podpisi(p)
    T, VYS = 470, H - 470

    def pol(f, poz, zum, klip):
        return kadr(f, poz, zum, f'left:0;top:0;width:{W}px;height:{VYS}px;clip-path:{klip}')
    return ('<div class="sh" style="top:0;height:1448px;background:radial-gradient(120% 60% at 30% 0,#1c2026 0,#0d0f12 70%)"></div>'
            + shapka(p) + f'<div class="model" style="top:58px;left:auto;right:52px;font-size:44px">{p["model"]}</div>'
            + f'<div style="position:absolute;left:0;top:{T}px;width:{W}px;height:{VYS}px;overflow:hidden">'
            + pol(lf, lpoz, lzum, 'polygon(0 0,62% 0,38% 100%,0 100%)') + pol(rf, rpoz, rzum, 'polygon(62% 0,100% 0,100% 100%,38% 100%)')
            + f'<svg style="position:absolute;inset:0" viewBox="0 0 {W} {VYS}"><line x1="{W * .62}" y1="0" x2="{W * .38}" y2="{VYS}" stroke="#fff" stroke-width="7"/></svg>'
            + '<div style="position:absolute;left:0;right:0;bottom:0;height:220px;background:linear-gradient(180deg,rgba(9,11,14,0) 0,rgba(9,11,14,.75) 80%)"></div>'
            + f'<div class="pil" style="left:40px;bottom:40px">{pd}</div>'
            + f'<div class="pil a" style="right:40px;bottom:40px">{pp}</div></div>')


VARIANTY = [('v1', v1), ('v2', v2), ('v3', v3), ('v4', v4)]


def main():
    nuzhny = {int(a) for a in sys.argv[1:]} or {p['n'] for p in POSTY}
    RAB.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        br = None
        try:
            br = pw.chromium.launch(headless=True, **brauzer_put())
            s = br.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            for p in POSTY:
                if p['n'] not in nuzhny:
                    continue
                papka = TUT / p['papka']
                papka.mkdir(exist_ok=True)
                for imya, fn in VARIANTY:
                    h = RAB / f'{p["papka"]}-{imya}.html'
                    h.write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{css(p["akcent"])}</style></head><body>{fn(p)}</body></html>', encoding='utf-8')
                    s.goto(h.as_uri())
                    s.evaluate('document.fonts.ready')
                    s.wait_for_timeout(250)
                    png = RAB / f'{p["papka"]}-{imya}.png'
                    s.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': W, 'height': H})
                    Image.open(png).convert('RGB').save(papka / f'banner-{imya}.webp', 'WEBP', quality=90, method=6)
                print(p['papka'], 'готово')
        finally:
            if br:
                br.close()


if __name__ == '__main__':
    main()
