#!/usr/bin/env python3
"""Вордстат через XMLRiver (wordstat/new/json), НСК=65, РФ=225, кэш ws-raw/. 25 ₽ за 1000. Потолок 20 ₽ на задачу.
python3 ws.py zaprosy.txt  -> печатает: запрос | НСК | РФ (головная строка или >=N)"""
import hashlib, json, pathlib, subprocess, sys, time, urllib.parse
P = pathlib.Path(__file__).resolve().parent
RAW = P / 'ws-raw'; RAW.mkdir(exist_ok=True)
SCHET = P / 'ws-schet.json'
LIMIT = 800  # обращений = 20 ₽
def env():
    t = pathlib.Path('~/.config/xmlriver/xmlriver.env').expanduser().read_text()
    return dict(l.split('=', 1) for l in t.split() if '=' in l)
def schet():
    return json.loads(SCHET.read_text()) if SCHET.exists() else {'obrashcheniy': 0}
def snyat(z, reg):
    f = RAW / (hashlib.sha1(f'{z}|{reg}'.encode()).hexdigest()[:16] + '.json')
    if f.exists(): return json.loads(f.read_text())
    s = schet()
    if s['obrashcheniy'] >= LIMIT: return {'error': 'потолок 20 ₽'}
    e = env()
    url = 'https://xmlriver.com/wordstat/new/json?' + urllib.parse.urlencode({'user': e['XMLRIVER_USER'], 'key': e['XMLRIVER_KEY'], 'query': z, 'regions': reg})
    for _ in range(2):
        s['obrashcheniy'] += 1; SCHET.write_text(json.dumps(s))
        r = subprocess.run(['curl', '-sS', '--max-time', '120', '-K', '-'], input=f'url = "{url}"', capture_output=True, text=True)
        try: d = json.loads(r.stdout)
        except ValueError: d = {}
        if 'popular' in d:
            out = {'query': z, 'region': reg, 'taken': time.strftime('%Y-%m-%d %H:%M'), 'totalValue': d.get('totalValue'),
                   'popular': [{'text': x['text'], 'value': int(x['value'])} for x in d['popular']]}
            f.write_text(json.dumps(out, ensure_ascii=False)); return out
        time.sleep(4)
    return {'error': str(d)[:120] or 'пусто'}
def chislo(o, z):
    if 'error' in o: return 'нет данных'
    pop = o.get('popular') or []
    if not pop: return 0
    if pop[0]['text'].strip().lower() == z.strip().lower() or len(pop[0]['text'].split()) <= len(z.split()): return pop[0]['value']
    return f'>={pop[0]["value"]}'
if __name__ == '__main__':
    for z in [l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip() and not l.startswith('#')]:
        n, r = snyat(z, '65'), snyat(z, '225')
        print(f'{z} | {chislo(n, z)} | {chislo(r, z)}', flush=True)
    s = schet(); print(f'# обращений всего {s["obrashcheniy"]} ≈ {s["obrashcheniy"]*0.025:.2f} ₽')
