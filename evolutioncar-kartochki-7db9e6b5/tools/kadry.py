"""Кадры для карточки из данных конфигуратора – та же логика, что в js/konfigurator.js движка.
kadry(proj) -> {base, versions: {id: {hero, angles: [(shot, label, url)], ints: [...]}}, colors: [(code, name, url, swatch)], def_version}
Все пути – абсолютные адреса tema-mail.github.io/<proj>/..., существование файла сверяется по диску ~/Sites/<proj>."""
import json, os

S = os.path.expanduser('~/Sites')


def load(proj):
    return json.loads(open(f'{S}/{proj}/js/zeekr-data.js').read().split('window.ZEEKR_CFG = ', 1)[1].rstrip().rstrip(';'))


def kadry(proj):
    D = load(proj)
    base = f'https://tema-mail.github.io/{proj}/'
    O = D['options']
    INT = set(D['int'])
    has_ang = bool(D.get('ang'))
    shots = D['shots']
    is_int = lambda sid: any(s['id'] == sid and (sid == 'int' or s.get('kind') == 'int') for s in shots)
    label = {s['id']: s['label'] for s in shots}

    def groups(V):
        return V['level'] + V['secs']

    def defaults(V):
        sel = {}
        for g in groups(V):
            if g.get('role') == 'extra':
                o = g['opts'][0]
                sel[g['sku']] = o['id'] if (o.get('def') or o.get('pre')) else None
            else:
                d = [o['id'] for o in g['opts'] if o.get('def')]
                sel[g['sku']] = d[0] if d else (g['opts'][0]['id'] if g['opts'] else None)
        return sel

    def code_for(sel, skus, drop=()):
        return '_'.join(x for x in (None if s in drop else sel.get(s) for s in skus) if x)

    def ext_code(V, sel, strict=False):
        pre = V.get('codePrefix') or ''
        c = pre + code_for(sel, V['vehicleSkus'])
        if c in D['have']: return c
        if strict: return None
        tail = '_' + code_for(sel, V['vehicleSkus'][1:])
        for k in D['have']:
            if k.endswith(tail) and k.startswith(pre): return k
        return None

    def int_code(V, sel):
        pre = V.get('codePrefix') or ''
        c = pre + code_for(sel, V.get('interiorSkus', []))
        if c in INT: return c
        extras = [s for s in V.get('interiorSkus', []) if any(g['sku'] == s and g.get('role') == 'extra' for g in groups(V))]
        c = pre + code_for(sel, V.get('interiorSkus', []), extras)
        return c if c in INT else None

    def ang(V, sel):
        if has_ang and V.get('angleSkus'):
            c = (V.get('codePrefix') or '') + code_for(sel, V['angleSkus'])
            return (c, D['ang'][c]) if c in D['ang'] else (None, [])
        c = ext_code(V, sel)
        return (c, [s for s in D['have'].get(c, []) if s != 'hero'])

    def url(kind, code, shot):
        p = D['paths'][kind].replace('{code}', code).replace('{shot}', shot)
        return base + p if os.path.exists(f'{S}/{proj}/{p}') else None

    out = {'base': base, 'versions': {}, 'colors': []}
    for V in D['versions']:
        sel = defaults(V)
        hc = ext_code(V, sel)
        ac, alist = ang(V, sel)
        ic = int_code(V, sel)
        angles = [(s, label.get(s, s), url('ext', ac or hc, s)) for s in alist if not is_int(s)]
        ints = [(s['id'], s['label'], url('int', ic, s['id'])) for s in shots if is_int(s['id'])] if ic else []
        out['versions'][V['id']] = {'name': V['name'], 'hero': url('ext', hc, 'hero') if hc else None,
                                    'angles': [a for a in angles if a[2]], 'ints': [i for i in ints if i[2]]}
    # версия по умолчанию – как в движке: Ultra или первая
    dv = next((V for V in D['versions'] if V['name'] == 'Ultra'), D['versions'][0])
    out['def_version'] = dv['id']
    # цвета: берём версию, где цветов больше всего (обычно все одинаковые)
    def paint_group(V):
        return next((g for g in V['secs'] if g.get('role') == 'paint'), None)
    cv = max(D['versions'], key=lambda V: len((paint_group(V) or {}).get('opts', [])))
    pg = paint_group(cv)
    if pg:
        for o in pg['opts']:
            sel = defaults(cv); sel[pg['sku']] = o['id']
            c = ext_code(cv, sel, strict=True)
            if not c:  # ближайшая сборка с этим цветом
                pre = cv.get('codePrefix') or ''
                cands = [k for k in D['have'] if k.startswith(pre) and o['id'] in k.split('_') or (o['id'] in k and k.startswith(pre))]
                c = cands[0] if cands else None
            u = url('ext', c, 'hero') if c else None
            if u:
                icon = O[o['id']].get('icon')
                out['colors'].append((o['id'], O[o['id']]['name'], u, base + icon if icon and os.path.exists(f'{S}/{proj}/{icon}') else None))
        out['color_version'] = cv['id']
    return out


if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    K = json.load(open(os.path.join(os.path.dirname(__file__), 'konfiguratory.json')))
    for m in K:
        k = kadry(m['proj'])
        vs = k['versions']
        nohero = [v['name'] for v in vs.values() if not v['hero']]
        print(m['proj'][:-13].ljust(18), 'цветов', len(k['colors']), '| версий', len(vs), 'без hero', nohero,
              '| ракурсы', len(vs[k['def_version']]['angles']), '| салон', len(vs[k['def_version']]['ints']))
