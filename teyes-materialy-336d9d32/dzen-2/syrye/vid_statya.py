#!/usr/bin/env python3
"""Вид статьи как на Дзене: statya.md → vid/<slug>/index.html (читалка) и lenta.html (карточка в ленте, 2 обложки).
Вёрстка скопирована с принятого образца vid/dzen-accord7 (читалка и лента Дзена, тёмная тема, кнопка «Тема»).
Запуск: python3 vid_statya.py <slug> [<slug> ...]   (из любой папки)
"""
import html
import re
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
OBRAZEC = KOREN.parent / 'vid/dzen-accord7'
MARKA = {'xtrail-t32': 'Nissan', 'note-e12': 'Nissan', 'juke-f15': 'Nissan', 'lc200': 'Toyota',
         'solaris-2': 'Hyundai', 'shuttle': 'Honda'}
POISK = {'xtrail-t32': 'магнитола ниссан х трейл', 'note-e12': 'магнитола ниссан ноут', 'juke-f15': 'магнитола ниссан жук',
         'lc200': 'магнитола ленд крузер 200', 'solaris-2': 'магнитола хендай солярис', 'shuttle': 'магнитола хонда шаттл'}


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
               lambda m: f'<a href="{m.group(2).replace("&amp;", "&").replace("&", "&amp;")}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    t = re.sub(r'(?<![*\w])\*([^*]+)\*(?!\*)', r'<em>\1</em>', t)
    return t


def razobrat(put):
    tekst = put.read_text(encoding='utf-8')
    tekst = re.sub(r'<!--.*?-->', '', tekst, flags=re.S)
    _, fm, telo = tekst.split('---', 2)
    meta = {}
    for s in fm.strip().splitlines():
        if ':' in s:
            k, v = s.split(':', 1)
            meta[k.strip()] = v.strip()
    return meta, telo.strip()


def v_html(telo, slug):
    stroki = telo.splitlines()
    out, toc, i, n_h2 = [], [], 0, 0
    while i < len(stroki):
        s = stroki[i].rstrip()
        if not s or s.startswith('# '):
            i += 1
            continue
        if s.startswith('## '):
            n_h2 += 1
            zag = s[3:].strip()
            toc.append((n_h2, zag))
            out.append(f'<h2 id="h{n_h2}">{inline(zag)}</h2>')
            i += 1
            continue
        m = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', s)
        if m:
            alt, src = m.group(1), m.group(2)
            cap = ''
            if i + 1 < len(stroki) and re.match(r'^\*[^*].*\*$', stroki[i + 1].strip()):
                cap = stroki[i + 1].strip()[1:-1]
                i += 1
            out.append(f'<figure><img src="../../{slug}/{src}" alt="{html.escape(alt)}" loading="lazy">'
                       + (f'<figcaption>{inline(cap)}</figcaption>' if cap else '') + '</figure>')
            i += 1
            continue
        if re.match(r'^[-–] ', s) or re.match(r'^\d+\. ', s):
            tag = 'ol' if re.match(r'^\d+\. ', s) else 'ul'
            items = []
            while i < len(stroki) and (re.match(r'^[-–] ', stroki[i]) or re.match(r'^\d+\. ', stroki[i])):
                items.append(re.sub(r'^([-–]|\d+\.) ', '', stroki[i].strip()))
                i += 1
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')
            continue
        par = [s]
        i += 1
        while i < len(stroki) and stroki[i].strip() and not re.match(r'^(## |!\[|[-–] |\d+\. )', stroki[i]):
            par.append(stroki[i].strip())
            i += 1
        out.append(f'<p>{inline(" ".join(par))}</p>')
    return ''.join(out), toc


def css_iz_obrazca(f):
    t = (OBRAZEC / f).read_text(encoding='utf-8')
    return re.search(r'<style>(.*?)</style>', t, re.S).group(1)


SCRIPT = """<script>
(function(){var r=document.documentElement,k='dzen2-theme';try{var s=localStorage.getItem(k);if(s)r.dataset.theme=s;}catch(e){}
if(!r.dataset.theme){var h=new Date().getHours();if(h>=19||h<7)r.dataset.theme='dark';}
document.getElementById('t').onclick=function(){var d=r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');r.dataset.theme=d==='dark'?'light':'dark';try{localStorage.setItem(k,r.dataset.theme)}catch(e){}};})();
</script>"""


def slov(telo):
    chist = re.sub(r'!\[[^\]]*\]\([^)]*\)|\]\([^)]*\)|[#*\[\]]', ' ', telo)
    return len(chist.split())


def sobrat(slug):
    meta, telo = razobrat(KOREN / slug / 'statya.md')
    title = meta['title']
    telo_html, toc = v_html(telo, slug)
    minut = max(3, round(slov(telo) / 180))
    marka = MARKA.get(slug, '')
    css = css_iz_obrazca('index.html')
    toc_html = '<div class="toc"><b>Оглавление</b><ol>' + ''.join(
        f'<li><a href="#h{n}">{inline(z)}</a></li>' for n, z in toc) + '</ol></div>'
    d = KOREN / 'vid' / slug
    d.mkdir(parents=True, exist_ok=True)
    stranica = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Дзен {html.escape(title[:60])}</title>
<style>{css}</style></head><body>
<nav class="side"><i class="logo"></i><i></i><i></i><i></i><i></i><i></i></nav>
<div class="badge">Макет: так статья будет выглядеть на Дзене. Черновик, не опубликовано · <a href="lenta.html" style="color:#000">карточка в ленте</a></div>
<header class="top"><span class="logo"></span><div class="search">Найти в Дзене</div><button class="tbtn" id="t" type="button">Тема</button></header>
<div class="wrap"><article class="art">
<div class="ch"><div class="av">TS</div><div><b>TEYES Сибирь</b><small>561 подписчик</small></div><button class="sub" type="button">Подписаться</button></div>
<h1>{html.escape(title)}</h1>
<div class="meta"><span>черновик</span><span>{minut} мин</span></div>
{toc_html}
<figure class="cover"><img src="../../{slug}/oblozhka-1-vs.webp" alt="Обложка: {html.escape(title)}"></figure>
{telo_html}
<div class="end"><span>&#9825; Нравится</span><span>Комментарии</span><span>Поделиться</span></div>
</article>
<aside class="aside"><div class="topic"><b>{marka}</b><small>тема Дзена</small><div>Следить за темой</div></div></aside></div>
{SCRIPT}</body></html>'''
    (d / 'index.html').write_text(stranica, encoding='utf-8')

    css_l = css_iz_obrazca('lenta.html')
    opis = html.escape(meta.get('description', ''))
    kartochki = ''
    for f, podpis in (('oblozhka-1-vs.webp', 'Основная – «год VS 2026»'), ('oblozhka-2-zapas.webp', 'Запасная – салон вечером')):
        if not (KOREN / slug / f).exists():
            continue
        kartochki += f'''<section><h2>{podpis}</h2><a class="card" href="index.html">
<img src="../../{slug}/{f}" alt="{podpis}"><div class="cb"><div class="ch"><span class="av">TS</span><span>TEYES Сибирь</span></div>
<b>{html.escape(title)}</b><p>{opis}</p><small>Статья · {minut} мин</small></div></a></section>'''
    lenta = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Лента Дзена {html.escape(title[:50])}</title>
<style>{css_l}</style></head><body>
<nav class="side"><i class="logo"></i><i></i><i></i><i></i><i></i><i></i></nav>
<div class="badge">Макет ленты Дзена: одна статья, две обложки</div>
<header class="top"><span class="logo"></span><div class="search">{POISK.get(slug, '')}</div><button class="tbtn" id="t" type="button">Тема</button></header>
<main><p class="note">Так карточка выглядит в ленте и в поиске Дзена. Нажмите карточку – откроется статья.</p><div class="grid">{kartochki}</div></main>
{SCRIPT}</body></html>'''
    (d / 'lenta.html').write_text(lenta, encoding='utf-8')
    print('ok', slug, len(toc), 'разделов,', minut, 'мин')


if __name__ == '__main__':
    for s in sys.argv[1:]:
        sobrat(s)
