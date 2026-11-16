"""Проверка data/<proj>.json против схемы и конфигуратора. Запуск: python3 tools/proverka_dannyh.py [proj ...]  (без аргументов – все файлы)."""
import json, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = {m['proj']: m for m in json.load(open(f'{R}/tools/konfiguratory.json'))}
HAN = re.compile(r'[一-鿿]')


def check(proj):
    err = []
    p = f'{R}/data/{proj}.json'
    if not os.path.exists(p):
        return ['нет файла']
    raw = open(p).read()
    if '—' in raw: err.append('длинное тире')
    if HAN.search(raw): err.append('иероглифы: ' + HAN.search(raw).group(0))
    d = json.loads(raw)
    k = K[proj]
    for f in ['name', 'year', 'body', 'seats', 'type', 'cc', 'lead', 'nums', 'versions', 'pay', 'cmp', 'obzor', 'faq', 'rivals', 'vs', 'sources']:
        if f not in d: err.append(f'нет поля {f}')
    if err: return err
    if d['type'] not in ('bev', 'phev', 'erev'): err.append('type не bev/phev/erev')
    ids = [v['id'] for v in k['versions']]
    got = [v['cfg'] for v in d['versions']]
    if got != ids: err.append(f'версии {got} != конфигуратор {ids}')
    n = len(d['versions'])
    if len(d['pay']) != n: err.append(f'pay {len(d["pay"])} != версий {n}')
    for v in d['versions']:
        if not v.get('variants'): err.append(f'{v["name"]}: нет variants')
        for x in v.get('variants', []):
            if x.get('price') is not None and not (30000 <= x['price'] <= 3000000): err.append(f'{v["name"]} {x.get("label")}: цена {x["price"]} вне 30 тыс.–3 млн ¥')
        if not (0 <= v.get('def', 0) < len(v.get('variants', [1]))): err.append(f'{v["name"]}: def вне variants')
        if v.get('type', d['type']) not in ('bev', 'phev', 'erev'): err.append(f'{v["name"]}: type')
    for g in d['cmp']:
        for r in g['rows']:
            if len(r) != n + 1: err.append(f'cmp «{g["g"]}» / «{r[0]}»: {len(r) - 1} значений, версий {n}')
    for r in d['rivals']:
        if r not in K or r == proj: err.append(f'соперник {r} не из списка')
    for r in d['vs']:
        if len(r) != 2 + len(d['rivals']): err.append(f'vs «{r[0]}»: длина {len(r)}')
    o = d['obzor']
    for s, nn in [('ext', 3), ('int', 3), ('mm', 2)]:
        if len(o.get(s, [])) < nn: err.append(f'obzor.{s} меньше {nn}')
    for s in ('pw', 'sf'):
        if len(o.get(s, {}).get('stats', [])) != 4: err.append(f'obzor.{s}.stats не 4')
    if len(d['nums']) != 4: err.append('nums не 4')
    if not 4 <= len(d['faq']) <= 8: err.append('faq не 4–8')
    if d['type'] != 'bev' and not d['cc']: err.append('у гибрида нет cc')
    return err


if __name__ == '__main__':
    todo = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(f'{R}/data') if f.endswith('.json'))
    bad = 0
    for p in todo:
        e = check(p)
        print(('OK  ' if not e else 'ОШИБКИ ') + p + ('' if not e else '\n   ' + '\n   '.join(e)))
        bad += bool(e)
    sys.exit(1 if bad else 0)
