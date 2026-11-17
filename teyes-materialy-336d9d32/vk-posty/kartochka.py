#!/usr/bin/env python3
"""Сборщик постов ВК TEYES Sibir: карточка-обложка 1 «как раньше» (вёрстка HTML → PNG через Playwright,
текст рисует вёрстка, не нейросеть), обложки 2 и 3 из картинок Codex, фото работы в webp.

Запуск:  python3 kartochka.py            – все 10 постов
         python3 kartochka.py 3 7        – только посты 3 и 7
Данные – posty.py. Исходники: ~/.cache/teyes-vk-posty (реальные фото с закрытыми номерами и картинки Codex).
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
from playwright.sync_api import sync_playwright
from posty import POSTY, KESH, GEN, RAZMYT, put_kadra

TUT = Path(__file__).resolve().parent
FONTS = Path.home() / 'Library/Fonts'
LOGO = KESH / 'logo/logo.svg'          # логотип с сайта: teyes-sibir-kod/public/assets/…/IMG_5765_1_layerstyl.svg
W, H = 1086, 1448
RAB = KESH / 'card'

IKONKI = {  # контурные значки 24×24, цвет – акцент карточки
 'ekran': '<rect x="2.5" y="5" width="19" height="12.5" rx="2"/><path d="M8 20.5h8M6.5 9.5h4M6.5 13h7"/>',
 'shirokiy': '<rect x="1.5" y="7" width="21" height="10" rx="2"/><path d="M5 12h3M5 12l1.6-1.6M5 12l1.6 1.6M19 12h-3M19 12l-1.6-1.6M19 12l-1.6 1.6"/>',
 'yazyk': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.800 0 18M12 3c-3 3.2-3 14.800 0 18"/>',
 'nav': '<path d="M12 21s-6.500-6-6.500-10.500a6.500 6.500 0 0 1 13 0C18.500 15 12 21 12 21Z"/><circle cx="12" cy="10.500" r="2.300"/>',
 'android': '<path d="M5 10.500a7 7 0 0 1 14 0v6.500a1.500 1.500 0 0 1-1.500 1.500h-11A1.500 1.500 0 0 1 5 17Z"/><path d="M5 12.500h14M8 4.500 6.600 2.500M16 4.500l1.400-2M9 21.500v-3M15 21.500v-3"/><circle cx="9.200" cy="8.300" r=".6"/><circle cx="14.800" cy="8.300" r=".6"/>',
 'muzyka': '<path d="M9 18V5.500l10-2V16"/><circle cx="6.500" cy="18" r="2.500"/><circle cx="16.500" cy="16" r="2.500"/>',
 'potolok': '<path d="M3 3.500h18M9 3.500v3h6v-3"/><rect x="5" y="6.500" width="14" height="10" rx="1.500"/><path d="m10.500 9.500 4 2-4 2Z"/>',
 'dva': '<rect x="2" y="4" width="13" height="9" rx="1.500"/><rect x="9" y="11" width="13" height="9" rx="1.500"/>',
 'verh': '<rect x="6" y="3.500" width="12" height="6" rx="1.500"/><rect x="3" y="12" width="18" height="8.500" rx="1.500"/><path d="M9 6.500h6"/>',
 'klimat': '<path d="M12 2.500v19M4 7l16 10M20 7 4 17M9.500 4.500 12 7l2.500-2.500M9.500 19.500 12 17l2.500 2.500"/>',
 'kamera': '<path d="M3.500 8.500a2 2 0 0 1 2-2H8l1.500-2h5l1.500 2h2.500a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2Z"/><circle cx="12" cy="12.500" r="3.300"/>',
 'registrator': '<path d="M8 3h8l1 4H7Z"/><rect x="4.500" y="7" width="15" height="10" rx="2"/><circle cx="12" cy="12" r="2.800"/><path d="M12 17v4"/>',
 'glaz': '<path d="M2.500 12S6 5.500 12 5.500 21.500 12 21.500 12 18 18.500 12 18.500 2.500 12 2.500 12Z"/><circle cx="12" cy="12" r="3"/>',
 'shchit': '<path d="M12 2.500 4.500 5.500v6c0 4.700 3.200 8.300 7.500 10 4.300-1.700 7.500-5.300 7.500-10v-6Z"/><path d="m8.800 12 2.300 2.300 4.300-4.600"/>',
 'gsm': '<path d="M4 20v-3M9 20v-7M14 20V9M19 20V4"/>',
 'gps': '<circle cx="12" cy="12" r="6.500"/><circle cx="12" cy="12" r="1.800"/><path d="M12 2v3.500M12 18.500V22M2 12h3.500M18.500 12H22"/>',
 'linii': '<path d="M5 21 9 4M19 21 15 4M7 13.500h10M8.200 8.500h7.600"/>',
 'parktronik': '<path d="M3 9h9.500l3 3.500v3H3Z"/><path d="M17.500 9.500a4.500 4.500 0 0 1 0 6M20 7a8 8 0 0 1 0 11"/><circle cx="6.500" cy="16.500" r="1.800"/>',
 'mikrofon': '<rect x="9" y="2.500" width="6" height="11.500" rx="3"/><path d="M5.500 11.500a6.500 6.500 0 0 0 13 0M12 18v3.500M8.500 21.500h7"/>',
 'dinamik': '<rect x="5" y="2.500" width="14" height="19" rx="2.500"/><circle cx="12" cy="14.500" r="3.800"/><circle cx="12" cy="6.800" r="1.500"/>',
}


def shrift(semya, ves, fajl):
    return f'@font-face{{font-family:{semya};font-weight:{ves};src:url("{(FONTS / fajl).as_uri()}")}}'


def css(a):
    return '\n'.join([
        shrift('G', 800, 'Gilroy-ExtraBold.otf'), shrift('G', 300, 'Gilroy-Light.otf'),
        shrift('IT', 400, 'InterTight-Regular.ttf'), shrift('IT', 500, 'InterTight-Medium.ttf'), shrift('IT', 600, 'InterTight-SemiBold.ttf'),
        shrift('B', 700, 'BebasNeue Bold.otf'),
        f'''*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:#0d0f12;color:#fff;font-family:IT,sans-serif}}
.fon{{position:absolute;left:0;top:0;width:{W}px;height:800px;overflow:hidden}}
.fon .raz{{position:absolute;inset:-40px;background-size:cover;background-position:50% 40%;filter:blur(26px) brightness(.5)}}
.fon .mash{{position:absolute;background-repeat:no-repeat;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 100%),linear-gradient(180deg,transparent 0,#000 9%,#000 100%);-webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent 0,#000 16%,#000 100%),linear-gradient(180deg,transparent 0,#000 9%,#000 100%);mask-composite:intersect}}
.fon .t1{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(9,11,14,.86) 0,rgba(9,11,14,.62) 34%,rgba(9,11,14,.08) 62%,rgba(9,11,14,0) 100%)}}
.fon .t2{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(9,11,14,.55) 0,rgba(9,11,14,0) 20%,rgba(9,11,14,0) 68%,#0d0f12 100%)}}
.niz{{position:absolute;left:0;top:780px;width:{W}px;height:{H - 780}px;background:radial-gradient(120% 70% at 50% 0,#191c21 0,#0d0f12 70%)}}
.logo{{position:absolute;left:60px;top:54px;width:236px}}
.slogan{{position:absolute;left:330px;top:46px;padding-left:26px;border-left:1.500px solid rgba(255,255,255,.4);font:500 16.500px/1.42 IT;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.8)}}
h1{{position:absolute;left:58px;top:158px;font:800 78px/.98 G;letter-spacing:-.022em;text-shadow:0 3px 26px rgba(0,0,0,.55)}}
h1 b{{color:{a};font-weight:800}}
.model{{position:absolute;left:60px;top:476px;font:700 66px/1 B;letter-spacing:.02em;text-shadow:0 2px 18px rgba(0,0,0,.6)}}
.pod{{position:absolute;left:60px;top:548px;font:400 27px/1.2 IT;color:rgba(255,255,255,.92);text-shadow:0 2px 14px rgba(0,0,0,.7)}}
.kadr{{position:absolute;border-radius:16px;overflow:hidden;border:2px solid rgba(255,255,255,.85);background:#000;box-shadow:0 14px 40px rgba(0,0,0,.55)}}
.kadr img{{width:100%;height:100%;object-fit:cover;display:block}}
.yarlyk{{position:absolute;left:0;top:0;height:50px;padding:0 26px 0 22px;display:flex;align-items:center;font:700 27px/1 B;letter-spacing:.09em;border-radius:0 0 20px 0;background:rgba(18,20,24,.88);color:#fff;white-space:nowrap}}
.yarlyk.a{{background:{a};color:#0d0f12}}
.strelka{{position:absolute;left:426px;top:968px;width:128px;height:76px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.6))}}
.ik{{position:absolute;left:44px;top:1142px;width:{W - 88}px;display:flex}}
.ik div{{flex:1 1 0;padding:0 16px;border-left:1.500px solid rgba(255,255,255,.2);font:500 19.500px/1.22 IT;color:rgba(255,255,255,.94)}}
.ik div:first-child{{border-left:0}}
.ik svg{{display:block;width:42px;height:42px;margin-bottom:10px;fill:none;stroke:{a};stroke-width:1.700;stroke-linecap:round;stroke-linejoin:round}}
.cherta{{position:absolute;left:52px;top:1288px;width:{W - 104}px;height:1.500px;background:rgba(255,255,255,.22)}}
.logo2{{position:absolute;left:60px;top:1334px;width:206px}}
.pv1{{position:absolute;left:300px;top:1322px;padding-left:28px;border-left:1.500px solid rgba(255,255,255,.4);font:500 17px/1.45 IT;letter-spacing:.13em;text-transform:uppercase;color:rgba(255,255,255,.85)}}
.pv2{{position:absolute;right:58px;top:1324px;display:flex;gap:26px;font:500 17px/1.3 IT;color:rgba(255,255,255,.9)}}
.pv2 span{{display:flex;align-items:center;gap:12px}}
.pv2 span+span{{padding-left:26px;border-left:1.500px solid rgba(255,255,255,.22)}}
.pv2 svg{{width:38px;height:38px;fill:none;stroke:#fff;stroke-width:1.600;stroke-linecap:round;stroke-linejoin:round;flex:none}}'''])


def zagolovok(stroki):
    out = []
    for s in stroki:
        while '*' in s:
            s = s.replace('*', '<b>', 1).replace('*', '</b>', 1)
        out.append(s)
    return '<br>'.join(out)


def kadry_html(p):
    k, vid = p['kadry'], p['vid']
    def blok(i, x, y, w, h, akc):
        f, podpis, fokus = k[i]
        return (f'<div class="kadr" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{put_kadra(f).as_uri()}" style="object-position:{fokus}">'
                f'<span class="yarlyk{" a" if akc else ""}">{podpis}</span></div>')
    if vid == 'odin':
        return blok(0, 36, 712, W - 72, 392, True)
    html = blok(0, 32, 706, 462, 386, False) + blok(1, 508, 712, 546, 398, True)
    if vid == 'do-posle':
        html += ('<svg class="strelka" viewBox="0 0 128 76"><path d="M6 14c18 44 56 54 100 40" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
                 '<path d="M90 30l22 22-28 12" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return html


def html(p):
    f, shir, dx, dy = p['geroy']
    g = put_kadra(f).as_uri()
    ik = ''.join(f'<div><svg viewBox="0 0 24 24">{IKONKI[i]}</svg>{t}</div>' for i, t in p['ikonki'])
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><style>{css(p["akcent"])}</style></head><body>
<div class="fon"><div class="raz" style="background-image:url('{g}')"></div>
<div class="mash" style="left:{dx}px;top:{dy}px;width:{shir}px;height:1400px;background-image:url('{g}');background-size:{shir}px auto"></div>
<div class="t1"></div><div class="t2"></div></div><div class="niz"></div>
<img class="logo" src="{LOGO.as_uri()}"><div class="slogan">{p["slogan"]}</div>
<h1>{zagolovok(p["zag"])}</h1><div class="model">{p["model"]}</div><div class="pod">{p["pod"]}</div>
{kadry_html(p)}
<div class="ik">{ik}</div><div class="cherta"></div>
<img class="logo2" src="{LOGO.as_uri()}"><div class="pv1">Teyes Sibir<br>Новосибирск</div>
<div class="pv2"><span><svg viewBox="0 0 24 24"><path d="M14.500 6.500a4.500 4.500 0 0 0-6 5.600L3 17.600V21h3.400l5.500-5.500a4.500 4.500 0 0 0 5.600-6l-2.800 2.800-2.300-.6-.6-2.300Z"/></svg>Установка<br>в сервисном центре</span>
<span><svg viewBox="0 0 24 24"><path d="M4.500 18.500 6 15a7.500 7.500 0 1 1 3 2.600Z"/><path d="M9 11h6M9 14h4"/></svg>Подбор по фото<br>панели</span></div>
</body></html>'''


def brauzer_put():
    kesh = Path.home() / 'Library/Caches/ms-playwright'
    for put in sorted(kesh.glob('chromium_headless_shell-*/*/chrome-headless-shell'), reverse=True):
        return {'executable_path': str(put)}
    return {}


def webp(src, dst, maks=None, q=88):
    im = Image.open(src).convert('RGB')
    if maks:
        im.thumbnail((maks, maks), Image.LANCZOS)
    im.save(dst, 'WEBP', quality=q, method=6)


def oblozhka_iz_kartinki(src, dst, ramki=()):
    """Картинку Codex приводим к 1086×1448 (3:4) без текста; таблички номеров из ramki размываем по рамке."""
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


def main():
    nuzhny = {int(a) for a in sys.argv[1:]} or {p['n'] for p in POSTY}
    RAB.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        br = None
        try:
            br = pw.chromium.launch(headless=True, **brauzer_put())
            str_ = br.new_page(viewport={'width': W, 'height': H}, device_scale_factor=1)
            for p in POSTY:
                if p['n'] not in nuzhny:
                    continue
                papka = TUT / p['papka']
                papka.mkdir(exist_ok=True)
                h = RAB / f'{p["papka"]}.html'
                h.write_text(html(p), encoding='utf-8')
                str_.goto(h.as_uri())
                str_.evaluate('document.fonts.ready')
                str_.wait_for_timeout(250)
                png = RAB / f'{p["papka"]}.png'
                str_.screenshot(path=str(png), clip={'x': 0, 'y': 0, 'width': W, 'height': H})
                webp(png, papka / 'oblozhka-1.webp', q=90)
                for i, zad in ((2, 'sit'), (3, 'srv')):
                    src = GEN / f'{p["n"]:02d}-{zad}' / 'out.png'
                    if src.exists():
                        oblozhka_iz_kartinki(src, papka / f'oblozhka-{i}.webp', RAZMYT.get(f'{p["n"]:02d}-{zad}', ()))
                for st in papka.glob('foto-*.webp'):
                    st.unlink()
                for i, f in enumerate(p['foto'], 1):
                    webp(put_kadra(f), papka / f'foto-{i}.webp', maks=1600, q=84)
                print(p['papka'], sorted(x.name for x in papka.iterdir()))
        finally:
            if br:
                br.close()


if __name__ == '__main__':
    main()
