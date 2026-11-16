"""Снимки и проверка карточек в Playwright: python3 tools/snimki.py <slug> [...] -> /tmp-папка снимков, ошибки консоли, битые картинки.
Отдаёт папку через свой http-сервер (корень – razbory), браузер закрывается в finally."""
import sys, os, threading, http.server, functools, json
from playwright.sync_api import sync_playwright

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(R)
OUT = os.environ.get('OUT', '/private/tmp/claude-502/-Users-artemgalimov/be8751b5-290a-4024-b785-80c960c42911/scratchpad/snimki')
os.makedirs(OUT, exist_ok=True)


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def main(slugs, shots=True):
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=ROOT))
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f'http://127.0.0.1:{port}/{os.path.basename(R)}/'
    res = {}
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.path.expanduser('~/Library/Caches/ms-playwright/chromium_headless_shell-1248/chrome-headless-shell-mac-arm64/chrome-headless-shell'))
        try:
            for sl in slugs:
                r = res[sl] = {'errors': [], 'broken': []}
                for name, vp in (('pk', {'width': 1440, 'height': 900}), ('tel', {'width': 390, 'height': 844})):
                    ctx = b.new_context(viewport=vp, device_scale_factor=1)
                    pg = ctx.new_page()
                    pg.on('pageerror', lambda e: r['errors'].append(str(e)))
                    pg.on('console', lambda m: r['errors'].append(m.text) if m.type == 'error' and 'favicon' not in m.text else None)
                    pg.goto(base + sl + '/', wait_until='networkidle', timeout=60000)
                    # прокрутить, чтобы ленивые картинки загрузились
                    pg.evaluate('document.querySelectorAll("img[loading=lazy]").forEach(i=>i.loading="eager")'); pg.evaluate('async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}scrollTo(0,0)}')
                    pg.wait_for_load_state('networkidle'); pg.wait_for_timeout(800)
                    br = pg.evaluate('[...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.getAttribute("src")).map(i=>i.getAttribute("src"))')
                    r['broken'] += br
                    if name == 'tel':
                        r['hscroll'] = pg.evaluate('document.documentElement.scrollWidth>innerWidth+1')
                    if shots:
                        pg.screenshot(path=f'{OUT}/{sl}-{name}.png', full_page=True)
                    ctx.close()
        finally:
            b.close(); srv.shutdown()
    print(json.dumps(res, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main(sys.argv[1:], shots=os.environ.get('NOSHOT') != '1')
