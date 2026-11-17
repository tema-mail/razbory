#!/usr/bin/env python3
"""Новые баннеры (обложка 1) – четыре варианта вёрстки с меньшим текстом, на трёх постах для выбора.
Убрано: нижняя плашка, ряд преимуществ, строка у логотипа. Осталось: маленький логотип, заголовок-мысль,
марка-модель, кадр крупно, «до/после» мельче. Кадры – только реальные фото работы (номера закрыты), машин не рисуем.

Запуск: python3 bannery.py  →  bannery/<пост>-v1…v4.webp
В1 – «после» во весь кадр, «до» маленькой вставкой; В2 – главный кадр на 2/3, внизу узкая полоса «до → после»;
В3 – заголовок и один кадр «после»; В4 – разрез по диагонали «до | после».
"""
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
from kartochka import FONTS, LOGO, RAB, W, H, brauzer_put, shrift, zagolovok
from posty import REAL, ZEL, SIN

TUT = Path(__file__).resolve().parent
VYH = TUT / 'bannery'

# kadr: (файл, высота картинки на баннере в px, сдвиг x, сдвиг y) – картинка ставится фоном нужного размера
PRIMERY = [
    dict(papka='04-honda-cr-v', model='HONDA CR-V', rabota='Teyes CC2 Plus', akcent=SIN,
         zag=['Экран новый.', 'Штатное –', '*на месте*'],
         posle='223-04', do='223-02', mash='223-05', do_podpis='ДО', vt_podpis='БЫЛО',
         v1=('223-04', 1560, -60, -20), v1vst=('223-02', '50% 24%'),
         v2=('223-05', 1500, -40, -190), v2a=('223-02', '50% 22%'), v2b=('223-04', '55% 36%'),
         v3=('223-04', '52% 38%'),
         v4l=('223-02', 1500, -292, -40), v4p=('223-04', 1500, 181, -170)),
    dict(papka='01-toyota-rav4', model='TOYOTA RAV4', rabota='Teyes LUXONE', akcent=ZEL,
         zag=['RAV4', 'заговорил', '*по-русски*'],
         posle='220-03', do='220-01', mash=None, do_podpis='ДО', vt_podpis='БЫЛО',
         v1=('220-02', 1448, -800, 70), v1vst=('220-01', '78% 40%'),
         v2=('220-02', 1300, -630, 70), v2a=('220-01', '78% 38%'), v2b=('220-03', '50% 12%'),
         v3=('220-02', '74% 48%'),
         v4l=('220-01', 1100, -845, 0), v4p=('220-02', 1100, -285, 0)),
    dict(papka='07-hyundai-h-1', model='HYUNDAI H-1', rabota='Teyes CC4, камера на экране', akcent=ZEL,
         zag=['Задний ход', 'без просьбы', '*«Выйди, посмотри»*'],
         posle='226-04', do='226-02', mash='226-02', do_podpis='МАШИНА', vt_podpis='В СЕРВИСЕ',
         v1=('226-04', 1640, -900, -150), v1vst=('226-02', '50% 60%'),
         v2=('226-02', 1010, -150, -20), v2a=('226-04', '68% 55%'), v2b=('226-03', '82% 42%'),
         v3=('226-04', '68% 55%'),
         v4l=('226-02', 1100, -390, -120), v4p=('226-04', 1500, -530, -335)),
]


def u(imya):
    return (REAL / f'{imya}.jpg').as_uri()


def baza(a):
    return '\n'.join([
        shrift('G', 800, 'Gilroy-ExtraBold.otf'), shrift('IT', 500, 'InterTight-Medium.ttf'), shrift('B', 700, 'BebasNeue Bold.otf'),
        f'''*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#0d0f12;color:#fff;font-family:IT,sans-serif}}
.f{{position:absolute;left:0;top:0;width:{W}px;background-repeat:no-repeat}}
.logo{{position:absolute;left:56px;top:50px;width:176px;filter:drop-shadow(0 2px 10px rgba(0,0,0,.6))}}
h1{{position:absolute;left:54px;font:800 92px/.97 G;letter-spacing:-.022em;text-shadow:0 3px 30px rgba(0,0,0,.7)}}
h1 b{{color:{a};font-weight:800}}
.model{{position:absolute;left:56px;font:700 58px/1 B;letter-spacing:.03em;text-shadow:0 2px 18px rgba(0,0,0,.7)}}
.model small{{display:block;margin-top:8px;font:500 27px/1.15 IT;letter-spacing:0;color:rgba(255,255,255,.9)}}
.k{{position:absolute;border-radius:18px;overflow:hidden;border:2.500px solid rgba(255,255,255,.9);background:#000;box-shadow:0 16px 44px rgba(0,0,0,.6)}}
.k img{{width:100%;height:100%;object-fit:cover;display:block}}
.ya{{position:absolute;left:0;top:0;height:44px;padding:0 20px 0 16px;display:flex;align-items:center;font:700 25px/1 B;letter-spacing:.1em;border-radius:0 0 16px 0;background:rgba(14,16,20,.9);white-space:nowrap}}
.ya.a{{background:{a};color:#0d0f12}}
.pil{{position:absolute;height:50px;padding:0 22px;display:flex;align-items:center;font:700 29px/1 B;letter-spacing:.1em;border-radius:25px;background:rgba(14,16,20,.86);white-space:nowrap}}
.pil.a{{background:{a};color:#0d0f12}}'''])


def strelka(x, y, w=110):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{w}px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.6))" viewBox="0 0 128 76">'
            '<path d="M6 14c18 44 56 54 100 40" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
            '<path d="M90 30l22 22-28 12" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def fon(k, vys=H, dop=''):
    f, h, x, y = k
    return f'<div class="f" style="height:{vys}px;background-image:url(\'{u(f)}\');background-size:auto {h}px;background-position:{x}px {y}px;{dop}"></div>'


def shapka(p, top=150):
    return f'<img class="logo" src="{LOGO.as_uri()}"><h1 style="top:{top}px">{zagolovok(p["zag"])}</h1>'


def model(p, top):
    return f'<div class="model" style="top:{top}px">{p["model"]}<small>{p["rabota"]}</small></div>'


def v1(p):
    """«После» во весь кадр, заголовок сверху, «до» маленькой вставкой в углу со стрелкой."""
    f, fok = p['v1vst']
    return (fon(p['v1'])
            + '<div class="f" style="height:700px;background:linear-gradient(180deg,rgba(9,11,14,.92) 0,rgba(9,11,14,.74) 52%,rgba(9,11,14,0) 100%)"></div>'
            + f'<div class="f" style="top:1040px;height:{H - 1040}px;background:linear-gradient(180deg,rgba(9,11,14,0) 0,rgba(9,11,14,.9) 78%)"></div>'
            + shapka(p) + model(p, 1300)
            + f'<div class="k" style="left:730px;top:1118px;width:310px;height:262px"><img src="{u(f)}" style="object-position:{fok}"><span class="ya">{p["vt_podpis"]}</span></div>'
            + ('<svg style="position:absolute;left:596px;top:1006px;width:130px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.6))" viewBox="0 0 130 120">'
               '<path d="M122 104C70 104 26 76 20 18" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
               '<path d="M4 40 20 14l22 22" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>' if p['do_podpis'] == 'ДО' else ''))


def v2(p):
    """Главный кадр на 2/3, заголовок поверх, внизу узкая полоса из двух небольших кадров."""
    (fa, foka), (fb, fokb) = p['v2a'], p['v2b']
    para = p['do_podpis'] == 'ДО'
    return (fon(p['v2'], 1010)
            + '<div class="f" style="height:1010px;background:linear-gradient(180deg,rgba(9,11,14,.9) 0,rgba(9,11,14,.6) 36%,rgba(9,11,14,0) 62%,rgba(13,15,18,.2) 86%,#0d0f12 100%)"></div>'
            + shapka(p) + model(p, 1150)
            + f'<div class="k" style="left:498px;top:1066px;width:256px;height:214px"><img src="{u(fa)}" style="object-position:{foka}"><span class="ya">{"ДО" if para else "КАМЕРА"}</span></div>'
            + f'<div class="k" style="left:782px;top:1056px;width:270px;height:234px"><img src="{u(fb)}" style="object-position:{fokb}"><span class="ya a">{"ПОСЛЕ" if para else "ЭКРАН"}</span></div>'
            + (strelka(712, 1196, 86) if para else ''))


def v3(p):
    """Только заголовок и один сильный кадр «после»."""
    f, fok = p['v3']
    return ('<div class="f" style="height:1448px;background:radial-gradient(120% 60% at 30% 0,#1c2026 0,#0d0f12 70%)"></div>'
            + shapka(p) + model(p, 470)
            + f'<div class="k" style="left:40px;top:640px;width:{W - 80}px;height:760px;border-radius:24px"><img src="{u(f)}" style="object-position:{fok}"><span class="ya a" style="height:50px;font-size:28px">ПОСЛЕ УСТАНОВКИ</span></div>')


def v4(p):
    """Разрез по диагонали: слева «до», справа «после»; заголовок над разрезом, подписи в углах."""
    para = p['do_podpis'] == 'ДО'
    T, VYS = 470, H - 470

    def pol(k, klip):
        f, h, x, y = k
        return (f'<div style="position:absolute;inset:0;background:url(\'{u(f)}\') {x}px {y}px/auto {h}px no-repeat #0d0f12;clip-path:{klip}"></div>')
    return ('<div class="f" style="height:1448px;background:radial-gradient(120% 60% at 30% 0,#1c2026 0,#0d0f12 70%)"></div>'
            + shapka(p)
            + f'<div style="position:absolute;left:0;top:{T}px;width:{W}px;height:{VYS}px;overflow:hidden">'
            + pol(p['v4l'], 'polygon(0 0,64% 0,36% 100%,0 100%)') + pol(p['v4p'], 'polygon(64% 0,100% 0,100% 100%,36% 100%)')
            + f'<svg style="position:absolute;inset:0" viewBox="0 0 {W} {VYS}"><line x1="{W * .64}" y1="0" x2="{W * .36}" y2="{VYS}" stroke="#fff" stroke-width="7"/></svg>'
            + f'<div style="position:absolute;left:0;right:0;bottom:0;height:240px;background:linear-gradient(180deg,rgba(9,11,14,0) 0,rgba(9,11,14,.8) 80%)"></div>'
            + f'<div class="pil" style="left:40px;bottom:40px">{"ДО" if para else p["model"]}</div>'
            + f'<div class="pil a" style="right:40px;bottom:40px">{"ПОСЛЕ" if para else "КАМЕРА НА ЭКРАНЕ"}</div></div>'
            + (f'<div class="model" style="top:1296px;left:auto;right:44px;text-align:right;font-size:46px">{p["model"]}</div>' if para else ''))


VARIANTY = [('v1', v1), ('v2', v2), ('v3', v3), ('v4', v4)]


def main():
    VYH.mkdir(exist_ok=True)
    RAB.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        br = None
        try:
            br = pw.chromium.launch(headless=True, **brauzer_put())
            s = br.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            for p in PRIMERY:
                for imya, fn in VARIANTY:
                    h = RAB / f'b-{p["papka"]}-{imya}.html'
                    h.write_text(f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{baza(p["akcent"])}</style></head><body>{fn(p)}</body></html>', encoding='utf-8')
                    s.goto(h.as_uri())
                    s.evaluate('document.fonts.ready')
                    s.wait_for_timeout(250)
                    png = RAB / f'b-{p["papka"]}-{imya}.png'
                    s.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': W, 'height': H})
                    Image.open(png).convert('RGB').save(VYH / f'{p["papka"]}-{imya}.webp', 'WEBP', quality=90, method=6)
                print(p['papka'], 'готово')
        finally:
            if br:
                br.close()


if __name__ == '__main__':
    main()
