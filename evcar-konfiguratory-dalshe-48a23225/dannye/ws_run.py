import json, sys, time
sys.path.insert(0, '.')
import ws as W
# марка: (формы латиницей, формы кириллицей, модели "лат[=кир]"; * в начале – модель уже есть у нас)
M = {
 'Zeekr': (['zeekr'], ['зикр'], '*9x *8x *7x *001 *009 *007 *x *mix'),
 'Li Auto': (['lixiang', 'li auto'], ['лисян', 'ликсян'], '*l9 *l8 *l6 l7 *i6 *i8 *mega'),
 'Xiaomi': (['xiaomi'], ['сяоми'], '*su7 *yu7 yu9'),
 'Avatr': (['avatr'], ['аватр'], '*07 *12 *06 11'),
 'Lynk & Co': (['lynk co'], ['линк ко'], '*900 *09 *08 *07 *z20 03 05 06 z10 01'),
 'Geely': (['geely'], ['джили'], '*galaxy+e5=галакси+e5 *xingyuan *starship+7 monjaro=монжаро galaxy+m9=галакси+m9 galaxy+l7=галакси+l7 galaxy+e8=галакси+e8 galaxy+a7=галакси+a7 starship+8 galaxy+starship=галакси+старшип ex5 xingyue+l'),
 'Xpeng': (['xpeng'], ['хпенг', 'сяопэн'], '*g6 *g9 *p7 *x9 *g7 *m03 *gx'),
 'BYD': (['byd'], ['бид', 'бид'], 'song+plus=сонг+плюс song+l=сонг+l song+pro=сонг+про seal=сил han=хан tang=танг tang+l yuan+plus=юань+плюс yuan+up=юань+ап seagull dolphin=дельфин sealion+07 sealion+06 sealion+05 sealion+8 qin+plus qin+l=цинь+l seal+06 seal+05 destroyer+05 xia=ся leopard+5=леопард+5 leopard+8=леопард+8 yangwang+u8 e2 atto+3 titanium+7 han+l'),
 'Fangchengbao': (['fangchengbao'], [], 'bao+5 bao+8 tai+7 tai+3'),
 'Yangwang': (['yangwang'], ['янгван'], 'u8 u7 u9'),
 'Denza': (['denza'], ['денза'], 'd9 n9 n8l z9 z9+gt n7 b5 b8'),
 'Voyah': (['voyah'], ['воя', 'вояж'], 'free=фри dream=дрим courage=кураж taishan=тайшань passion=пассион'),
 'Deepal': (['deepal'], ['дипал'], 's07 s09 s05 l07 l06 g318'),
 'Leapmotor': (['leapmotor'], ['липмотор'], 'c11 c10 c16 c01 b10 b01 d19'),
 'Aito': (['aito'], ['аито'], 'm5 m7 m8 m9'),
 'Nio': (['nio'], ['нио'], 'es8 es6 et5 et7 ec6 et9'),
 'Onvo': (['onvo'], [], 'l60 l90 l80'),
 'Hongqi': (['hongqi'], ['хунци', 'хонгчи'], 'hs5 hs7 hs3 h9 h5 eh7 ehs7 ehs9 guoya'),
 'Tank': (['tank'], ['танк'], '300 400 500 700'),
 'Wey': (['wey'], ['вей'], '07 05 gaoshan'),
 'IM': (['im motors', 'im'], [], 'ls6 ls7 ls9 l6'),
 'Luxeed': (['luxeed'], [], 'r7 s7'),
 'Stelato': (['stelato'], [], 's9'),
 'Maextro': (['maextro'], [], 's800'),
 'Exlantix': (['exlantix', 'exeed exlantix'], [], 'et es'),
 'Changan': (['changan'], ['чанган'], 'uni+k uni+z cs75+plus q07 a07 e07'),
 'GAC': (['gac'], ['гак'], 'aion+y aion+v gs8 m8 hyptec+ht s7'),
 'Dongfeng': (['dongfeng'], ['донгфенг'], 'mhero 007 nammi box'),
 'Jetour': (['jetour'], ['джетур'], 'traveller=тревеллер t2 g700 shanhai+l7 shanhai+t2'),
 'iCar': (['icar'], [], '03 v23 v27'),
 'BAIC': (['baic'], ['баик'], 'bj40 bj60'),
 'Volkswagen (Китай)': (['volkswagen', 'vw'], ['фольксваген'], 'id4 id+4 id6 id+6 id7 id+7 id+unyx id3 id+3'),
 'Toyota (Китай)': (['toyota'], ['тойота'], 'bz4x bz3x bz3 bz5 bz7'),
 'Honda (Китай)': (['honda'], ['хонда'], 'ens1 e+ns1 enp2 ens2 s7'),
 'Nissan (Китай)': (['nissan'], ['ниссан'], 'n7 n6'),
 'Mazda (Китай)': (['mazda'], ['мазда'], 'ez+6 ez+60 ez6 ez60'),
 'Audi (Китай)': (['audi'], ['ауди'], 'q4+e+tron q5+e+tron q6l+e+tron e5+sportback'),
 'BMW (Китай)': (['bmw'], ['бмв'], 'ix3 ix1 i3 i5'),
 'Mercedes (Китай)': (['mercedes'], ['мерседес'], 'eqe eqb eqa eqs'),
 'Kia (Китай)': (['kia'], ['киа'], 'ev5'),
 'Tesla': (['tesla'], ['тесла'], 'model+y model+3'),
 'Smart': (['smart'], ['смарт'], '1 3 5'),
 'Buick': (['buick'], [], 'electra+e5 electra+e4 e5'),
}
BRANDS = 'zeekr зикр lixiang лисян|ликсян avatr аватр xpeng хпенг byd denza денза voyah вояж|воях deepal дипал leapmotor липмотор aito аито hongqi хунци|хонгчи onvo yangwang fangchengbao luxeed stelato maextro exlantix jetour джетур exeed эксид changan чанган haval хавал chery чери jaecoo джейку omoda омода dongfeng донгфенг mhero wey'.split()
out = {'models': [], 'brands': []}
def head(q):
    t = W.ws(q)
    if t is None: return None, None
    tot, rows = t
    if not rows: return 0, True
    ok = len(rows[0][0].split()) <= len(q.split())
    return rows[0][1], ok
for b, (lat, cyr, models) in M.items():
    for m in models.split():
        ours = m.startswith('*'); m = m.lstrip('*')
        ml, _, mc = m.partition('='); ml = ml.replace('+', ' '); mc = (mc or ml).replace('+', ' ')
        forms = [f'{x} {ml}' for x in lat] + [f'{x} {mc}' for x in dict.fromkeys(cyr)]
        tot, det, bad = 0, {}, False
        for q in forms:
            v, ok = head(q)
            det[q] = v if ok is not False else f'{v}?'
            if v is None: bad = True
            elif ok: tot += v
        out['models'].append({'brand': b, 'model': ml, 'ours': ours, 'total': tot, 'err': bad, 'det': det})
        print(b, ml, tot, det, flush=True)
        json.dump(out, open('ws_itog.json', 'w'), ensure_ascii=False, indent=1)
for q in BRANDS:
    v, ok = head(q)
    out['brands'].append({'q': q, 'v': v, 'ok': ok}); print('МАРКА', q, v, ok, flush=True)
out['spent'] = W.spent
json.dump(out, open('ws_itog.json', 'w'), ensure_ascii=False, indent=1)
print('ЗАПРОСОВ', W.spent, 'цена ₽', round(W.spent * 25 / 1000, 2))
