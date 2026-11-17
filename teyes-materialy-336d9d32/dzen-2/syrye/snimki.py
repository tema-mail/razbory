#!/usr/bin/env python3
"""Снимки видов 390 и 1440 (вся страница, WebP рядом с html) + проверка горизонтальной прокрутки.
Запуск: ~/Sites/teyes-keysy/.venv/bin/python snimki.py <html> [<html> ...]
Браузер закрывается в finally (брошенный headless перехватывает обычный Chrome)."""
import io
import sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright


def main(fayly):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=str(Path.home() / 'Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell'))
        try:
            for f in fayly:
                f = Path(f).resolve()
                for w in (390, 1440):
                    pg = b.new_page(viewport={'width': w, 'height': 900}, device_scale_factor=1)
                    pg.emulate_media(color_scheme='light')
                    pg.goto(f.as_uri())
                    pg.evaluate("document.documentElement.dataset.theme='light'")
                    pg.wait_for_timeout(700)
                    over = pg.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
                    png = pg.screenshot(full_page=True)
                    im = Image.open(io.BytesIO(png)).convert('RGB')
                    if im.height > 12000:
                        im = im.crop((0, 0, im.width, 12000))
                    imya = f.parent / f'snimok-{f.stem}-{w}.webp'
                    im.save(imya, 'WEBP', quality=70)
                    print(f'{imya.relative_to(f.parent.parent.parent)} {im.size} прокрутка вбок: {over}px')
                    pg.close()
        finally:
            b.close()


if __name__ == '__main__':
    main(sys.argv[1:])
