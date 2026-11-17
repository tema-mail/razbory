#!/usr/bin/env python3
"""Страница просмотра 10 постов ВК (макет ленты, вёрстка взята из ../vid/vk/index.html) и кусок общей страницы.
Запуск: python3 stranitsa.py  →  index.html, stranitsa-chast.md"""
import html
import re
from pathlib import Path
from PIL import Image
from posty import POSTY, ssylka

TUT = Path(__file__).resolve().parent
PODPISI = ['1 – как раньше', '2 – ситуация', '3 – в сервисе']
ALT = ['карточка «до и после» в прежнем стиле', 'жизненная ситуация', 'машина в боксе TEYES Sibir']

CSS = '''*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%}
body{min-width:0;overflow-x:hidden}
img{display:block;max-width:100%}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit}
a{text-decoration:none}
.pv{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:8px 16px;background:#1b1d22;color:#d9dade;font:13px/1.3 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;position:relative;z-index:50}
.pv b{color:#fff;font-weight:600}
.pv .tag{background:#3a2f12;color:#f3d98b;border-radius:6px;padding:2px 7px;font-size:12px}
.pv .lbl{flex:1 1 auto;min-width:0}
.pv #tema-btn{width:30px;height:30px;border-radius:50%;background:#33363d;color:#fff;font-size:15px;flex:none}
.ava{display:block;border-radius:50%;overflow:hidden;flex:none}
.ava svg{width:100%;height:100%;display:block}
.lb{position:fixed;inset:0;background:rgba(0,0,0,.9);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}
.lb.on{display:flex}
.lb img{max-width:100%;max-height:100%;object-fit:contain;border-radius:4px}
.lb button{position:absolute;top:10px;right:12px;width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,.14);color:#fff;font-size:26px;line-height:44px}
.zoom{cursor:zoom-in}
:root{--bg:#edeef0;--card:#fff;--tx:#000;--sec:#818c99;--link:#2688eb;--line:#e7e8ec;--hd:#fff;--inp:#edeef0;--ic:#99a2ad;--chip:#f0f2f5}
html[data-theme=dark]{--bg:#141414;--card:#222222;--tx:#e1e3e6;--sec:#76787a;--link:#71aaeb;--line:#363738;--hd:#222222;--inp:#2c2d2e;--ic:#828282;--chip:#2c2d2e;color-scheme:dark}
body{background:var(--bg);color:var(--tx);font:13px/1.38 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.hd{background:var(--hd);border-bottom:1px solid var(--line);height:48px;position:sticky;top:0;z-index:20}
.hd .in{max-width:1076px;margin:0 auto;height:100%;display:flex;align-items:center;gap:16px;padding:0 16px}
.hd .sq{width:120px;height:20px;border-radius:5px;background:var(--chip)}
.hd .srch{display:flex;align-items:center;gap:8px;background:var(--inp);border-radius:8px;height:32px;padding:0 10px;color:var(--ic);width:230px}
.hd .ttl{display:none;font-weight:600;font-size:16px}
.hd .me{margin-left:auto;width:32px;height:32px;border-radius:50%;background:var(--chip)}
.wrap{max-width:1076px;margin:0 auto;padding:16px;display:grid;grid-template-columns:160px minmax(0,550px) 1fr;gap:16px;align-items:start}
.menu a{display:flex;align-items:center;gap:10px;padding:6px 8px;border-radius:8px;color:var(--tx);font-size:13px}
.menu a i{width:20px;height:20px;border-radius:6px;background:var(--chip);flex:none}
.menu a.on{background:var(--card)}
.side{background:var(--card);border-radius:12px;padding:8px;max-width:260px;position:sticky;top:64px}
.side a{display:block;padding:7px 10px;border-radius:8px;color:var(--tx)}
.side a:hover{background:var(--chip)}
.side .h{padding:6px 10px 4px;color:var(--sec);font-size:12px}
main{display:flex;flex-direction:column;gap:16px;min-width:0}
.post{background:var(--card);border-radius:12px;box-shadow:0 0 0 .5px rgba(0,0,0,.06),0 1px 3px rgba(0,0,0,.05);scroll-margin-top:60px}
.ph{display:flex;align-items:center;gap:12px;padding:12px 16px 8px}
.ph .ava{width:40px;height:40px}
.ph .nm{font-weight:600;font-size:13.5px;color:var(--tx)}
.ph .tm{color:var(--sec);font-size:12.5px;margin-top:1px}
.ph .dt{color:var(--ic)}
.pt{padding:0 16px 10px;font-size:14px;line-height:1.43}
.pt p{margin:0 0 1.15em}
.pt p:last-of-type{margin-bottom:0}
.pt .more{display:none}
.pt.open .more{display:block}
.pt.open .vk-more{display:none}
.pt p:nth-of-type(2){margin-bottom:0}
.pt.open p:nth-of-type(2){margin-bottom:1.15em}
.vk-more{color:var(--link);font-weight:500;padding:2px 0 0;display:block}
.pt a{color:var(--link)}
.pt a.u{word-break:break-all}
.sec{padding:10px 16px 6px;color:var(--sec);font-size:12.5px;font-weight:500;border-top:1px solid var(--line)}
.obl{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;padding:0 16px 12px}
.obl figure{min-width:0}
.obl img{width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:8px;background:var(--chip)}
.obl figcaption{padding-top:5px;font-size:12px;line-height:1.25;color:var(--tx);font-weight:500}
.grid{display:flex;flex-direction:column;gap:2px}
.grid .row{display:flex;gap:2px;width:100%}
.grid .c{min-width:0;overflow:hidden;background:var(--chip)}
.grid img{width:100%;height:100%;object-fit:cover}
.act{display:flex;align-items:center;gap:8px;padding:10px 12px 12px}
.act .b{display:flex;align-items:center;gap:6px;height:32px;padding:0 12px 0 10px;border-radius:16px;background:var(--chip);color:var(--sec);font-weight:500;font-size:13px}
.act .vw{margin-left:auto;display:flex;align-items:center;gap:5px;color:var(--sec);font-size:12.5px}
@media(max-width:1000px){.wrap{grid-template-columns:160px minmax(0,1fr)}.side{display:none}}
@media(max-width:700px){.wrap{grid-template-columns:1fr;padding:8px 0}.menu,.hd .sq,.hd .srch{display:none}
.post{border-radius:0}.hd .in{justify-content:space-between}.hd .ttl{display:block}.pv .note{display:none}
.obl{padding:0 10px 12px;gap:5px}.obl figcaption{font-size:11.5px}}'''

AVA = ('<span class="ava"><svg viewBox="0 0 398 398" aria-hidden="true"><defs><linearGradient id="lg{n}" x1="0" y1="0" x2="420" y2="25" gradientUnits="userSpaceOnUse">'
       '<stop stop-color="#009AE7"/><stop offset="1" stop-color="#9A00E7"/></linearGradient></defs><circle cx="199" cy="199" r="199" fill="url(#lg{n})"/>'
       '<path d="M86.1 147.8c.4-2 2.5-9.7 4.3-17.1L94.1 117h117.5c110.8 0 117.3.2 116.3 3.6-.4 1.8-2.3 9.5-7.2 30.6l-80.6 1L202 306h-35.8c-33.2 0-35.9-.2-35-3.4.6-2 9.4-36.2 19.600-76 10-39.800 18.500-73 18.500-73.800 0-1-18.900-1.600-42-1.600-38.900 0-42-.2-41.200-3.400Z" fill="#fff"/></svg></span>')

JS = '''(function(){var b=document.getElementById('tema-btn');function upd(){var d=document.documentElement.getAttribute('data-theme')==='dark';b.textContent=d?'☀':'☾';b.title=d?'Светлая тема':'Тёмная тема';b.setAttribute('aria-label',b.title)}
b.onclick=function(){var n=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',n);try{localStorage.setItem('tema',n)}catch(e){}upd()};upd()})();
(function(){var lb=document.createElement('div');lb.className='lb';lb.innerHTML='<button type="button" aria-label="Закрыть">×</button><img alt="">';
document.body.appendChild(lb);var im=lb.querySelector('img');
document.addEventListener('click',function(e){var m=e.target.closest('.vk-more');if(m){m.parentNode.classList.add('open');return}
var t=e.target.closest('.zoom');if(t){im.src=t.getAttribute('src');im.alt=t.alt;lb.classList.add('on');return}
if(lb.classList.contains('on')&&(e.target===lb||e.target.closest('.lb button')||e.target===im))lb.classList.remove('on')});
document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.classList.remove('on')})})();'''


def abzacy(t):
    return [a.strip() for a in t.strip().split('\n\n') if a.strip()]


def tekst_html(t):
    out = []
    for i, a in enumerate(abzacy(t)):
        s = html.escape(a).replace('\n', '<br>')
        s = re.sub(r'(https://teyes-sibir\.ru/\S+)', r'<a class="u" href="\1" target="_blank" rel="noopener">\1</a>', s)
        s = re.sub(r'(?<![/\w])(vk\.me/teyes\.magnitola)', r'<a href="https://\1" target="_blank" rel="noopener">\1</a>', s)
        out.append(f'<p{" class=more" if i > 1 else ""}>{s}</p>')
        if i == 1:
            out.append('<button class="vk-more" type="button">Показать ещё</button>')
    return ''.join(out)


def setka(papka, n):
    """Фото работы рядами, как вложения в ленте ВК: высота ряда общая, ширина – по пропорциям."""
    fajly = sorted(papka.glob('foto-*.webp'), key=lambda f: int(f.stem.split('-')[1]))
    razm = []
    for f in fajly:
        with Image.open(f) as im:
            razm.append(im.width / im.height)
    ryady, i = [], 0
    po = [2, 3] if len(fajly) >= 5 else [len(fajly)] if len(fajly) <= 3 else [2, 2]
    for kol in po:
        ryady.append(list(range(i, min(i + kol, len(fajly)))))
        i += kol
    if i < len(fajly):
        ryady.append(list(range(i, len(fajly))))
    out = []
    for ryad in ryady:
        if not ryad:
            continue
        summa = sum(razm[k] for k in ryad)
        kl = ''.join(f'<div class="c" style="flex:{razm[k]:.4f} 1 0"><img class="zoom" src="{papka.name}/{fajly[k].name}" alt="Фото работы: {n}, кадр {k + 1}" loading="lazy"></div>' for k in ryad)
        out.append(f'<div class="row" style="aspect-ratio:{summa:.4f}">{kl}</div>')
    return f'<div class="grid">{"".join(out)}</div>'


def post_html(p):
    papka = TUT / p['papka']
    t = (papka / 'post.txt').read_text(encoding='utf-8')
    obl = ''.join(
        f'<figure><img class="zoom" src="{p["papka"]}/oblozhka-{i}.webp" alt="{html.escape(p["mashina"])}: {ALT[i - 1]}" loading="lazy"><figcaption>{PODPISI[i - 1]}</figcaption></figure>'
        for i in (1, 2, 3))
    return f'''<article class="post" id="p{p["n"]}">
 <div class="ph">{AVA.format(n=p["n"])}<div><div class="nm">TEYES Sibir</div><div class="tm">пост {p["n"]} из 10 · работа №{p["nomer"]} · {html.escape(p["mashina"])}</div></div>
  <span class="dt" style="margin-left:auto"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><circle cx="5" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="19" cy="12" r="1.8"/></svg></span></div>
 <div class="pt">{tekst_html(t)}</div>
 <div class="sec">Обложка – три варианта, выбрать один</div>
 <div class="obl">{obl}</div>
 <div class="sec">Фото работы – в карусель после обложки</div>
 {setka(papka, p["mashina"])}
 <div class="act"><span class="b"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 20s-7.500-4.600-7.500-10.200A4.300 4.300 0 0 1 12 7.300a4.300 4.300 0 0 1 7.500 2.500C19.500 15.400 12 20 12 20Z"/></svg></span><span class="b"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4.500 18.500 6 15a7.500 7.500 0 1 1 3 2.600Z" stroke-linejoin="round"/></svg></span><span class="b"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M13 5v4C7 9.500 4.500 13 4 19c2-3 4.600-4.400 9-4.500V19l7-7Z"/></svg></span>
  <span class="vw">не опубликовано</span></div>
</article>'''


def stranitsa():
    nav = ''.join(f'<a href="#p{p["n"]}">{p["n"]}. {html.escape(p["mashina"])}</a>' for p in POSTY)
    posty = '\n'.join(post_html(p) for p in POSTY)
    return f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>10 постов ВК – следующие работы TEYES Sibir</title>
<script>(function(){{var t;try{{t=localStorage.getItem('tema')}}catch(e){{}}
if(!t){{var h=new Date().getHours();t=(h>=19||h<7||(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches))?'dark':'light'}}
document.documentElement.setAttribute('data-theme',t)}})();</script>
<style>
{CSS}
</style></head>
<body>
<div class="pv"><span class="tag">Предпросмотр</span><span class="lbl"><b>10 постов ВК · TEYES Sibir</b><span class="note"> · работы №231–240, ничего не опубликовано</span></span><button id="tema-btn" type="button"></button></div>
<header class="hd"><div class="in"><span class="sq"></span><span class="ttl">Новости</span><label class="srch"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="6.500"/><path d="m16 16 4.500 4.500"/></svg><span>Поиск</span></label><span class="me"></span></div></header>
<div class="wrap">
<nav class="menu"><a href="#"><i></i>Моя страница</a><a href="#" class=on><i></i>Новости</a><a href="#"><i></i>Мессенджер</a><a href="#"><i></i>Друзья</a><a href="#"><i></i>Сообщества</a><a href="#"><i></i>Фотографии</a><a href="#"><i></i>Музыка</a><a href="#"><i></i>Видео</a><a href="#"><i></i>Клипы</a></nav>
<main>
{posty}
</main>
<aside class="side"><div class="h">Посты</div>{nav}</aside>
</div>
<script>{JS}</script>
</body></html>
'''


def chast():
    s = ['## 10 постов ВК: следующие кейсы', '',
         'Последний пост в сообществе – УАЗ Профи (23.10), это работа №230; перед ним Honda Fit – №229. Посты идут по порядку номеров, поэтому взяты следующие десять: №231–240. Ничего не опубликовано.', '',
         'Смотреть лентой: [vk-posty/index.html](vk-posty/index.html)', '',
         '| № поста | Работа | Машина | Что сделали | Заголовок поста |', '|---|---|---|---|---|']
    for p in POSTY:
        zag = (TUT / p['papka'] / 'post.txt').read_text(encoding='utf-8').split('\n')[0]
        s.append(f"| {p['n']} | №{p['nomer']} | {p['mashina']} | {p['rabota']} | {zag} |")
    s.append('')
    for p in POSTY:
        t = (TUT / p['papka'] / 'post.txt').read_text(encoding='utf-8').strip()
        zag, telo = t.split('\n', 1)
        s += [f"### Пост {p['n']}. {p['mashina']} (работа №{p['nomer']})", '']
        for i in (1, 2, 3):
            s += [f"![{p['mashina']}: {ALT[i - 1]}](vk-posty/{p['papka']}/oblozhka-{i}.webp)", f'**{PODPISI[i - 1]}**', '']
        s += [f'**{zag}**', '', telo.strip(), '']
    s.append((TUT / 'chto-proverit.md').read_text(encoding='utf-8').strip())
    return '\n'.join(s) + '\n'


if __name__ == '__main__':
    (TUT / 'index.html').write_text(stranitsa(), encoding='utf-8')
    (TUT / 'stranitsa-chast.md').write_text(chast(), encoding='utf-8')
    print('index.html', (TUT / 'index.html').stat().st_size, 'stranitsa-chast.md', (TUT / 'stranitsa-chast.md').stat().st_size)
