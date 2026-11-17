#!/usr/bin/env python3
"""Вид поста-карусели Дзена: вёрстка принятого образца vid/dzen-karusel/index.html, свои текст и карточки.
Запуск: python3 vid_karusel.py <папка карусели> "<слова-ссылка в посте>" "<дата для шапки поста>"
Берёт <папка>/post.txt, <папка>/ssylka.txt и карточки <папка>/NN-*.webp."""
import html
import re
import sys
from pathlib import Path

KOREN = Path(__file__).resolve().parent.parent
OBRAZEC = KOREN.parent / 'vid/dzen-karusel/index.html'


def main(papka, slova_ssylki, data):
    p = KOREN / papka
    post = (p / 'post.txt').read_text(encoding='utf-8').strip().split('\n\n')
    url = (p / 'ssylka.txt').read_text(encoding='utf-8').strip()
    zag, lead, ostal = post[0], post[1], post[2:]

    def abzac(t):
        t = html.escape(t, quote=False).replace('\n', '<br>')
        if slova_ssylki in t:
            t = t.replace(slova_ssylki, f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{slova_ssylki}</a>', 1)
        return t
    ptx = (f'<div class="ptx" id="kt"><h2>{html.escape(zag)}</h2><p class="lead">{abzac(lead)}</p>'
           + ''.join(f'<p class="more">{abzac(a)}</p>' for a in ostal) + '<button class="mbtn" type="button">ещё</button></div>')
    if slova_ssylki not in '\n'.join(post):
        raise SystemExit('слова ссылки не найдены в посте')
    kart = sorted(p.glob('[0-9][0-9]-*.webp'))
    slides = ''.join(f'<div class="sl"><img src="../../{papka}/{k.name}" alt="Карточка {i}" draggable="false"'
                     + (' loading=lazy' if i > 2 else '') + '></div>' for i, k in enumerate(kart, 1))
    dots = '<i class=on></i>' + '<i></i>' * (len(kart) - 1)
    t = OBRAZEC.read_text(encoding='utf-8')
    t = re.sub(r'<div class="ptx" id="kt">.*?<button class="mbtn" type="button">ещё</button></div>', lambda m: ptx, t, flags=re.S)
    t = re.sub(r'(<div class="trk" id="trk">).*?(</div>\s*<span class="cnt")', lambda m: m.group(1) + slides + '</div>\n  <span class="cnt"', t, flags=re.S)
    t = re.sub(r'<span class="cnt" id="cnt">1 / \d+</span>', f'<span class="cnt" id="cnt">1 / {len(kart)}</span>', t)
    t = re.sub(r'<div class="dots" id="dots">.*?</div>', f'<div class="dots" id="dots">{dots}</div>', t, flags=re.S)
    t = re.sub(r'<nav aria-label="Другие макеты">.*?</nav>', '<nav aria-label="Карусели"><a href="../karusel-kitay/index.html">Китай</a><a href="../karusel-sugrob/index.html">Сугроб</a><a href="../karusel-prisoska/index.html">Присоска</a></nav>', t, flags=re.S)
    t = t.replace(f'href="../{papka}/index.html"', f'href="../{papka}/index.html" class=on')
    t = re.sub(r'<div class="sb">[^<]*</div>', f'<div class="sb">{data}</div>', t, count=1)
    t = t.replace('<title>Карусель Дзена – вид</title>', f'<title>Карусель Дзена – {html.escape(zag[:40])}</title>')
    d = KOREN / 'vid' / papka
    d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(t, encoding='utf-8')
    print('ok', papka, len(kart), 'карточек')


if __name__ == '__main__':
    main(*sys.argv[1:4])
