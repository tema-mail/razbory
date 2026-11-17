#!/usr/bin/env python3
"""Снимки страницы просмотра на 390 и 1440 px (тёмная тема) и проверка горизонтальной прокрутки."""
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
from kartochka import brauzer_put

TUT = Path(__file__).resolve().parent
with sync_playwright() as pw:
    br = None
    try:
        br = pw.chromium.launch(headless=True, **brauzer_put())
        for shir, vys in ((390, 844), (1440, 900)):
            k = br.new_context(viewport={'width': shir, 'height': vys}, device_scale_factor=2 if shir == 390 else 1)
            k.add_init_script("try{localStorage.setItem('tema','dark')}catch(e){}")
            s = k.new_page()
            s.goto((TUT / 'index.html').as_uri())
            s.wait_for_load_state('networkidle')
            s.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
            s.wait_for_timeout(1200)
            sw, cw = s.evaluate('[document.documentElement.scrollWidth, document.documentElement.clientWidth]')
            bit = s.evaluate("[...document.images].filter(i=>!i.complete||!i.naturalWidth).length")
            vsego = s.evaluate('document.images.length')
            print(shir, 'scrollWidth', sw, 'clientWidth', cw, 'прокрутка вбок:', 'ЕСТЬ' if sw > cw else 'нет', '| картинок', vsego, 'битых', bit, '| тема', s.evaluate("document.documentElement.dataset.theme"))
            for i, sel in enumerate(('#p1', '#p6'), 1):
                png = TUT / f'snimok-{shir}-{i}.png'
                s.locator(sel).scroll_into_view_if_needed()
                s.evaluate(f"document.querySelector('{sel} .vk-more') && document.querySelector('{sel} .vk-more').click()") if i == 2 else None
                s.wait_for_timeout(600)
                y = s.evaluate(f"document.querySelector('{sel}').getBoundingClientRect().top + scrollY - 60")
                s.evaluate(f'scrollTo(0,{y})')
                s.wait_for_timeout(500)
                if shir == 390:
                    s.set_viewport_size({'width': 390, 'height': 1500})
                    s.wait_for_timeout(300)
                s.screenshot(path=str(png))
                Image.open(png).convert('RGB').save(png.with_suffix('.webp'), 'WEBP', quality=82)
                png.unlink()
                if shir == 390:
                    s.set_viewport_size({'width': 390, 'height': 844})
            k.close()
    finally:
        if br:
            br.close()
