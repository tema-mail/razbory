"""Карточки моделей по образцу карточки Zeekr 8X: data/<проект>.json + кадры конфигуратора -> <модель>/index.html.
Запуск: python3 tools/gen.py [проект ...]  (без аргументов – все, у кого есть data/*.json и проверка данных OK)."""
import json, os, sys, html, datetime
sys.path.insert(0, os.path.dirname(__file__))
from kadry import kadry
from proverka_dannyh import check

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
K = {m['proj']: m for m in json.load(open(f'{R}/tools/konfiguratory.json'))}
KURS = {'usd': 3.0026, 'eur': 3.3312, 'cny': 0.45143}   # НБРБ на 15.11.2026; на странице подтягивается свежий
KURS_DATE = '15.11.2026'
TODAY = datetime.date.today().strftime('%d.%m.%Y')
E = html.escape
TYPE = {'bev': 'Электромобиль', 'phev': 'Подключаемый гибрид', 'erev': 'Последовательный гибрид'}
TYPE_S = {'bev': 'Электро', 'phev': 'Гибрид', 'erev': 'Гибрид'}
FUEL_LD = {'bev': 'Электричество', 'phev': 'Подключаемый гибрид (PHEV)', 'erev': 'Последовательный гибрид (EREV)'}
REF_8X = 'https://tema-mail.github.io/razbory/evolutioncar-zeekr-8x-d2effe31/prototip/'


def sp(n):
    return f'{round(n):,}'.replace(',', ' ')


def slug(proj):
    return proj[:-len('-konfigurator')]


def load(proj):
    return json.load(open(f'{R}/data/{proj}.json'))


def min_price(d):
    ps = [x['price'] for v in d['versions'] for x in v['variants'] if x.get('price')]
    return min(ps) if ps else None


def max_price(d):
    ps = [x['price'] for v in d['versions'] for x in v['variants'] if x.get('price')]
    return max(ps) if ps else None


def card_url(proj):
    """адрес карточки соседа: 8X – готовая ручная карточка, остальные – наши"""
    return REF_8X if proj == 'zeekr-8x-konfigurator' else f'../{slug(proj)}/'


def alpha(url):
    """кадр без фона (RGBA) вписываем целиком, студийный и фото салона – обрезаем по рамке"""
    from PIL import Image
    p = os.path.expanduser('~/Sites/') + url.split('tema-mail.github.io/', 1)[1]
    try: return Image.open(p).mode in ('RGBA', 'LA', 'P')
    except Exception: return True


def esc_t(s):
    return E(str(s)) if s is not None else '<span class="ask w-ask">[уточнить]</span>'


def build(proj):
    d, k, kd = load(proj), K[proj], kadry(proj)
    N, brand = d['name'], k['brand']
    model = k['model']
    sl = slug(proj)
    bslug, mslug = proj.split('-', 1)[0], sl.split('-', 1)[1]
    url = f'/catalog/{bslug}/{mslug}/'
    T = d['type']
    vers = d['versions']
    vnames = [v['name'] for v in vers]
    mp, xp = min_price(d), max_price(d)
    usd = lambda y: y * KURS['cny'] / KURS['usd']
    cfg_def = kd['def_version'] if kd['def_version'] in [v['cfg'] for v in vers] else vers[0]['cfg']
    vimg = {vid: v['hero'] for vid, v in kd['versions'].items()}
    colors = kd['colors'] or [(None, '', vimg[cfg_def], None)]
    hero0 = colors[0][2]
    types = sorted({v.get('type', T) for v in vers})
    type_txt = TYPE[T] if len(types) == 1 else 'Электромобиль и последовательный гибрид' if set(types) == {'bev', 'erev'} else ' и '.join(TYPE[t].lower() for t in types).capitalize()
    is_hyb = any(t != 'bev' for t in types)
    price_txt = f'от {sp(mp)} ¥' if mp else '[уточнить]'
    vers_txt = ' · '.join(vnames) if len(vnames) <= 4 else f'{len(vnames)} версий: {vnames[0]} – {vnames[-1]}'
    title = f'{N} под заказ в Минск – цена под ключ, комплектации {d["year"]}'
    desc = f'{N} {d["year"]} под заказ из Китая: {len(vers)} {"версия" if len(vers) == 1 else "версии" if len(vers) < 5 else "версий"} с ценой, сравнение комплектаций, конфигуратор, тест-драйв и лизинг. Расчёт под ключ в Минске.'
    h1 = f'{N} под заказ из Китая в Минск'

    # данные для скрипта
    CAR = {
        'proj': proj, 'name': N, 'type': T, 'cc': d.get('cc') or 0, 'kurs': dict(KURS), 'kursDate': KURS_DATE, 'cfgDef': cfg_def, 'minPrice': mp,
        'colors': [[c[0], c[1], c[2], c[3]] for c in colors],
        'versions': [{'id': v['cfg'], 'n': v['name'], 'tag': v.get('tag', ''), 'type': v.get('type', T), 'img': vimg.get(v['cfg']), 'def': v.get('def', 0), 'li': v.get('li', []),
                      'b': [{'l': x.get('label') or '', 'p': x.get('price'), 'e': x.get('e'), 't': x.get('total')} for x in v['variants']]} for v in vers],
        'sources': d.get('sources', []), 'notes': d.get('notes', ''),
    }

    seo = {'url': url, 'title': title, 'description': desc, 'h1': h1, 'keys': []}

    # разметка
    faq3 = d['faq'][:3]
    ld = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Главная', 'item': 'https://evolutioncar.by/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Каталог', 'item': 'https://evolutioncar.by/catalog/'},
            {'@type': 'ListItem', 'position': 3, 'name': brand, 'item': f'https://evolutioncar.by/catalog/{bslug}/'},
            {'@type': 'ListItem', 'position': 4, 'name': N, 'item': f'https://evolutioncar.by{url}'}]},
        {'@type': 'Car', 'name': f'{N} {d["year"]}', 'brand': {'@type': 'Brand', 'name': brand}, 'model': model, 'modelDate': d['year'], 'bodyType': d['body'],
         'fuelType': FUEL_LD[T], 'vehicleSeatingCapacity': d['seats'], 'image': [hero0],
         'offers': {'@type': 'AggregateOffer', 'priceCurrency': 'USD', 'lowPrice': 'ЗАПРОСИТЬ', 'highPrice': 'ЗАПРОСИТЬ', 'offerCount': sum(len(v['variants']) for v in vers),
                    'availability': 'https://schema.org/PreOrder', 'seller': {'@type': 'AutoDealer', 'name': 'Evolution Car'}}},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq3]}]}

    # обзор: картинки – ракурсы и салон из конфигуратора
    dv = kd['versions'][cfg_def]
    ext_imgs = [(a[2], a[1]) for a in dv['angles']]
    for c in colors[1:]:
        if len(ext_imgs) >= 3: break
        ext_imgs.append((c[2], c[1]))
    int_imgs = [(i[2], i[1]) for i in dv['ints']]
    if not int_imgs:
        for vv in kd['versions'].values():
            if vv['ints']: int_imgs = [(i[2], i[1]) for i in vv['ints']]; break

    def fig(item, img, alt, big=False):
        if img:
            return (f'<figure class="of{" big" if big else ""}{" r" if alpha(img) else ""}"><img src="{img}" alt="{E(alt)}" loading="lazy">'
                    f'<figcaption><b>{E(item["b"])}</b>{E(item["p"])}</figcaption></figure>')
        return f'<figure class="of t"><figcaption><b>{E(item["b"])}</b>{E(item["p"])}</figcaption></figure>'

    def section(items, imgs, what):
        first = fig(items[0], imgs[0][0] if imgs else None, f'{N}: {what}, {imgs[0][1].lower()}' if imgs else '', big=True)
        rest = ''.join(fig(it, imgs[i + 1][0] if len(imgs) > i + 1 else None, f'{N}: {what}, {imgs[i + 1][1].lower()}' if len(imgs) > i + 1 else '') for i, it in enumerate(items[1:]))
        return first + (f'<div class="og m-lane" data-mob="lenta">{rest}</div>' if rest else '')

    o = d['obzor']
    stats = lambda st: '<div class="stats">' + ''.join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in st) + '</div>'
    obzor = (f'<div class="ob" id="o-ext"><h3>Экстерьер</h3>{section(o["ext"], ext_imgs, "кузов")}</div>'
             f'<div class="ob" id="o-int"><h3>Салон</h3>{section(o["int"], int_imgs[:1] + int_imgs[1:], "салон")}</div>'
             f'<div class="ob" id="o-mm"><h3>Экраны и звук</h3>{section(o["mm"], int_imgs[1:2], "экраны")}</div>'
             f'<div class="ob" id="o-pw"><h3>Силовая установка</h3><p class="lead">{E(o["pw"]["p"])}</p>{stats(o["pw"]["stats"])}</div>'
             f'<div class="ob" id="o-sf"><h3>Шасси и безопасность</h3><p class="lead">{E(o["sf"]["p"])}</p>{stats(o["sf"]["stats"])}</div>')
    n_photo = len(ext_imgs) + len(int_imgs)

    # сравнение версий
    def vmin(v):
        ps = [x['price'] for x in v['variants'] if x.get('price')]
        return f'от {sp(min(ps))} ¥' if ps else 'цена – уточнить'
    head = ''.join(f'<th>{f"<img src=\"{vimg[v["cfg"]]}\" alt=\"{E(N)} {E(v["name"])}\" loading=\"lazy\">" if vimg.get(v["cfg"]) else ""}<b>{E(v["name"])}</b><small>{vmin(v)}</small><a class="go" href="#konfigurator" data-cfg="{v["cfg"]}">Собрать →</a></th>' for v in vers)
    pay = ''.join(f'<td>{E(p)}</td>' for p in d['pay'])
    groups = ''.join(f'<tbody data-g="{E(g["g"])}"><tr class="gh"><td colspan="{len(vers) + 1}"><button type="button">{E(g["g"])}<i>+</i></button></td></tr>'
                     + ''.join('<tr>' + ''.join(f'<td>{esc_t(c)}</td>' for c in r) + '</tr>' for r in g['rows']) + '</tbody>' for g in d['cmp'])

    # соперники
    riv = [r for r in d['rivals'] if r in K]
    def rname(r):
        try: return load(r)['name']
        except Exception: return K[r]['car']
    vs_head = f'<tr><th></th><th class="hi">{E(N)}</th>' + ''.join(f'<th>{E(rname(r))}</th>' for r in riv) + '</tr>'
    vs_rows = ''.join('<tr><td>' + E(r[0]) + '</td>' + ''.join(f'<td{" class=\"hi\"" if i == 0 else ""}>{esc_t(c)}</td>' for i, c in enumerate(r[1:])) + '</tr>' for r in d['vs'])
    vs_btn = ''.join(f'<a class="w-btn ghost" href="{card_url(r)}">Карточка {E(rname(r))}</a>' for r in riv)
    vs_names = ', '.join(rname(r) for r in riv[:-1]) + (' и ' if len(riv) > 1 else '') + rname(riv[-1]) if riv else ''

    # похожие: соперники + соседи по марке
    sims = list(riv)
    for p in K:
        if len(sims) >= 3: break
        if p != proj and p not in sims and p.split('-', 1)[0] == proj.split('-', 1)[0]: sims.append(p)
    def sim_card(p):
        kk = kadry(p); img = kk['versions'][kk['def_version']]['hero']
        try:
            dd = load(p); mp2 = min_price(dd); nm = dd['name']; ty = TYPE_S[dd['type']]; yr = dd['year']
        except Exception:
            mp2, nm, ty, yr = None, K[p]['car'], '', ''
        return (f'<a class="w-card" href="{card_url(p)}"><img src="{img}" alt="{E(nm)}" loading="lazy"><small>Китай{" · " + ty if ty else ""}{" · " + yr if yr else ""}</small>'
                f'<b>{E(nm)}</b><span class="pr">{"в Китае от " + sp(mp2) + " ¥" if mp2 else "цена – уточнить"}</span><span class="w-btn wide sm">Смотреть {E(nm)}</span></a>')
    sim = ''.join(sim_card(p) for p in sims[:3])

    faq = ''.join(f'<details{" open" if i == 0 else ""}><summary>{E(q)}</summary><p>{E(a)}</p></details>' for i, (q, a) in enumerate(d['faq']))
    nums = ''.join(f'<div><b>{E(a)}</b><span>{E(b)}</span></div>' for a, b in d['nums'])
    seg_cfg = ''.join(f'<button type="button" data-v="{v["cfg"]}"{" class=\"on\"" if v["cfg"] == cfg_def else ""}>{E(v["name"])}</button>' for v in vers)
    seg_form = '<button type="button" class="on" data-v="">Не решил</button>' + ''.join(f'<button type="button" data-v="{E(v["name"])}">{E(v["name"])}</button>' for v in vers)
    src_txt = '; '.join(f'{s[0]} – {s[1].split("/")[2] if "//" in s[1] else s[1]}, {s[2]}' for s in d.get('sources', [])[:4])
    batt_txt = 'Переключите батарею – цена и запас хода пересчитаются. ' if any(len(v['variants']) > 1 for v in vers) else ''
    t_hint = {'bev': 'Электромобиль: пошлина 15 % (квота 2026 для физлиц выбрана), НДС 0 % для машины до 5 лет – Указ № 428.',
              'erev': 'Последовательный гибрид: пошлина 15 % и НДС 20 % – с 2026 года льгота для гибридов отменена (Указ № 428).',
              'phev': 'Подключаемый гибрид: по формуле ГТК – единая ставка 48 %, не меньше 7,5 € за кубик; дилеры с 2026 года считают 15 % + НДС 20 % – вариант подтверждает брокер.'}
    cost_p = ' '.join(t_hint[t] for t in types)
    srv_bat = 'Диагностика и ремонт высоковольтной батареи, инвертора и электромоторов' + (' и двигателя-генератора.' if is_hyb else '.')

    page = f'''<!doctype html>
<html lang="ru" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="https://evolutioncar.by{url}">
<script>(function(){{var t;try{{t=localStorage.getItem('tema-evk')}}catch(e){{}}if(!t){{var h=new Date().getHours();t=(h>=19||h<7)?'dark':'light'}}document.documentElement.setAttribute('data-theme',t)}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700&family=Inter:wght@500;600;700;800&display=swap">
<link rel="preload" as="image" href="{hero0}">
<link rel="stylesheet" href="../ev.css?v=17">
<link rel="stylesheet" href="../karta.css?v=2">
<script type="application/json" id="w-seo">{json.dumps(seo, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="ph" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
  <symbol id="tg" viewBox="0 0 24 24"><path d="M21 4 3 11l6 2 2 6 3-4 5 4z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
  <symbol id="car" viewBox="0 0 24 24"><path d="M4 16v-4l2-5h12l2 5v4M4 16h16M7 16v2M17 16v2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
  <symbol id="key" viewBox="0 0 24 24"><circle cx="8" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 12h9M18 12v3M21 12v2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
  <symbol id="calc" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 8h8M8 13h2M14 13h2M8 17h2M14 17h2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></symbol>
  <symbol id="chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></symbol>
</svg>

<!-- служебная полоса прототипа: на сайт не идёт -->
<div class="w-bar"><div class="w-wrap">
  <b>Прототип</b> · {E(N)} под заказ · по образцу карточки Zeekr 8X · {url} · {TODAY}
  <label><input type="checkbox" id="sw-logic"> Логика блоков</label>
  <button type="button" id="sw-seo">Цепочка, SEO и источники</button>
  <span>Меток «запросить»: <b id="n-ask">0</b></span>
  <a href="../">Все карточки</a>
</div></div>

<header class="hd" id="hd"><div class="w-wrap hd-in">
  <a class="logo" href="#top"><img src="../img/logo-evolution-car.webp" alt="Evolution Car" width="720" height="37"></a>
  <nav class="hd-nav" aria-label="Разделы карточки"><a href="#obzor">Обзор</a><a href="#versii">Версии и цены</a><a href="#konfigurator">Конфигуратор</a><a href="#cena">Цена под ключ</a><a href="#zakaz">Как заказать</a><a href="#servis">Сервис</a><a href="#voprosy">Вопросы</a></nav>
  <div class="hd-ph"><a href="tel:+375291358888">+375 (29) 135-88-88</a><small>Ежедневно 09:00 – 18:00</small></div>
  <a class="hd-ic" href="tel:+375291358888" aria-label="Позвонить"><svg width="18" height="18"><use href="#ph"/></svg></a>
  <a class="hd-ic" href="#" aria-label="Telegram"><svg width="18" height="18"><use href="#tg"/></svg></a>
  <a class="w-btn sm hd-cta" href="#raschet" data-goal="raschet"><span class="hd-full">Расчёт под ключ</span><span class="hd-short">Расчёт</span></a>
</div></header>

<main id="top">

<section class="w-block hero" id="hero" data-n="1"
  data-question="Можно ли купить {E(N)} в Минске и сколько он будет стоить?"
  data-next="Что это за машина и стоит ли она этих денег?"
  data-proof="Цена в Китае: {E(src_txt)}; курс НБРБ; официальные рендеры из нашего конфигуратора"
  data-us="Ловим запрос «{E(N.lower())}»: H1 и ответ в первом абзаце для Яндекса, Google, Алисы и нейросетей. Две двери в заявку сразу."
  data-client="За 5 секунд понимает: машину везут, сколько примерно стоит, сколько ждать, и может сразу попросить расчёт или тест-драйв.">
<div class="w-wrap">
  <nav class="crumbs" aria-label="Хлебные крошки"><a href="#">Главная</a> / <a href="#">Каталог автомобилей</a> / <a href="#">{E(brand)}</a> / {E(N)}</nav>
  <div class="logic"></div>
  <div class="hero-g">
    <div class="hero-m">
      <div class="stage" id="stage"><img class="on" src="{hero0}" alt="{E(N)} {d["year"]}, {E(colors[0][1].lower())}, официальный рендер" data-c="{colors[0][0] or ""}" fetchpriority="high"></div>
      <div class="sw"><div class="dots" id="dots" role="radiogroup" aria-label="Цвет кузова"></div><span id="cname">{E(colors[0][1])}</span></div>
    </div>
    <div class="hero-i">
      <span class="tag">[ Китай · под заказ ]</span>
      <h1>{E(h1)}</h1>
      <p class="ans">{E(d["lead"])} Выкупаем у дилера в Китае, везём, растаможиваем и ставим на учёт – машина приезжает к вам в Минск.</p>
      <div class="tiles">
        <div class="tile acc"><small>Под ключ в Минске</small><b>от <span class="ask w-ask">[запросить: $]</span></b></div>
        <div class="tile"><small>В Китае</small><b>{price_txt}</b><em id="hero-usd">{"≈ " + sp(usd(mp)) + " $ по курсу НБРБ на " + KURS_DATE if mp else ""}</em></div>
        <div class="tile"><small>Срок до ключей</small><b><span class="ask w-ask">[запросить: дней]</span></b></div>
        <div class="tile"><small>Версии</small><b>{E(vers_txt)}</b></div>
      </div>
      <div class="w-actions"><a class="w-btn" href="#raschet" data-goal="raschet">Получить расчёт на свою сборку</a><a class="w-btn ghost" href="#test-drive" data-goal="test">Уточнить тест-драйв</a></div>
    </div>
  </div>
  <div class="nums">{nums}</div>
</div>
</section>

<section class="w-block sec" id="obzor" data-mob="vkladki" data-n="2"
  data-question="Что это за машина и стоит ли она этих денег?"
  data-next="Можно ли прокатиться, прежде чем решать?"
  data-proof="Характеристики производителя ({E(src_txt)}); кадры – официальные рендеры из нашего конфигуратора ({n_photo} шт.); пресс-фото и видео марки – следующим шагом"
  data-us="Желание и время на странице. Большой текст в HTML закрывает «характеристики», «салон», «фото», «интерьер»."
  data-client="Видит машину снаружи и внутри, экраны, силовую установку, безопасность. Понимает, за что такие деньги.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Обзор {E(N)}</span>
  <h2>Полный обзор возможностей {E(N)}</h2>
  <nav class="otabs" id="otabs" aria-label="Разделы обзора"><a href="#o-ext" class="on">Экстерьер</a><a href="#o-int">Салон</a><a href="#o-mm">Экраны и звук</a><a href="#o-pw">Силовая установка</a><a href="#o-sf">Безопасность</a></nav>
  {obzor}
</div>
</section>

<section class="w-block sec" id="test-drive" data-n="3"
  data-question="Можно ли прокатиться, прежде чем решать?"
  data-next="Какую версию выбрать и сколько стоит каждая?"
  data-proof="Наличие {E(N)} для тест-драйва – запросить у Evolution; в карточке модели – только эта модель (владелец 15.11.2026)"
  data-us="Самая горячая заявка: человек, который сел в машину, покупает в разы чаще. Стоит сразу после обзора – на пике желания."
  data-client="Снимает главный страх покупки под заказ – «плачу за машину, которую не трогал». Честно предупреждаем: наличие уточняет менеджер.">
<div class="w-wrap">
  <div class="logic"></div>
  <div class="td w-card">
    <div class="td-car"><img src="{vimg[cfg_def]}" alt="{E(N)} – тест-драйв в Минске" loading="lazy"></div>
    <div class="td-t">
      <h2>Тест-драйв {E(N)} в Минске</h2>
      <p>Проехать на {E(N)}, посидеть в салоне, проверить экраны и разгон – до того, как платить за заказ.</p>
      <p class="td-note">Машины для тест-драйва и в наличии меняются: мы не гарантируем, что {E(N)} стоит в салоне прямо сейчас. Оставьте заявку – менеджер проверит наличие, подберёт время и перезвонит.</p>
      <a class="w-btn" href="#raschet" data-goal="test">Уточнить наличие и тест-драйв у менеджера</a>
    </div>
  </div>
</div>
</section>

<section class="w-block sec" id="versii" data-n="4"
  data-question="Какую версию выбрать и сколько стоит каждая?"
  data-next="Чем именно отличаются версии – за что я доплачиваю?"
  data-proof="Официальные цены в Китае: {E(src_txt)}; курс НБРБ"
  data-us="Цены по каждой версии – козырь против Атланта (у них цен нет). Человек сам делит себя по бюджету – менеджер получает уже выбранную версию."
  data-client="Видит цену в юанях и в долларах, запас хода и что главное в каждой версии.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Комплектации и цены {E(N)}</span>
  <h2>Цены на {E(N)} во всех комплектациях</h2>
  <p class="lead">{batt_txt}Официальные цены в Китае, курс НБРБ на <span data-kurs>{KURS_DATE}</span>.</p>
  <div class="vers w-grid" id="vers"></div>
</div>
</section>

<section class="w-block sec" id="sravnenie" data-mob="akkordeon" data-n="5"
  data-question="Чем именно отличаются версии – за что я доплачиваю?"
  data-next="Как будет выглядеть моя машина с моим цветом и опциями?"
  data-proof="Комплектации производителя: {E(src_txt)}"
  data-us="Приём из сравнения Атлант-М + строка «за доплату». Меньше вопросов менеджеру, чаще берут версию выше. Таблица в HTML – робот читает её без скриптов."
  data-client="Видит разницу без чтения длинных таблиц: галочка «только различия», группы сворачиваются, строка «что я получу за доплату».">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Сравнение комплектаций {E(N)}</span>
  <h2>Чем отличаются комплектации {E(N)}</h2>
  <div class="cmp-bar"><label class="tgl"><input type="checkbox" id="only-diff"><i></i>Только различия</label><button type="button" class="lnk" id="all-open">Свернуть все группы</button></div>
  <div class="cmp" id="cmp"><table>
    <thead><tr><th class="c0">{E(N)} {d["year"]}</th>{head}</tr></thead>
    <tbody class="extra"><tr class="pay"><td>За доплату к соседней версии</td>{pay}</tr></tbody>
    {groups}
  </table></div>
</div>
</section>

<section class="w-block sec" id="konfigurator" data-mob="ekran" data-n="6"
  data-question="Как будет выглядеть моя машина с моим цветом и опциями?"
  data-next="Сколько будет стоить моя сборка в Минске со всеми платежами?"
  data-proof="Наш конфигуратор {E(N)}: официальные рендеры производителя и правила совместимости"
  data-us="Вовлечение и точная заявка: менеджер получает не «хочу {E(model)}», а полную сборку. Своего конфигуратора нет ни у Атланта, ни у voltauto."
  data-client="Видит именно свою машину: цвет, диски, салон, опции. Сборка сама уходит в расчёт ниже – ничего не надо переписывать.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Конфигуратор {E(N)}</span>
  <h2>Соберите свой {E(N)}</h2>
  <p class="lead">Официальные рендеры производителя на каждую сборку. Несовместимые опции подстроятся сами, как у завода.</p>
  <div class="seg" id="cfg-seg">{seg_cfg}</div>
  <button type="button" class="cfg-open w-card" id="cfg-open" aria-controls="cfg"><span class="cfg-shot"><img src="{hero0}" alt="Конфигуратор {E(N)}" loading="lazy"><span class="cfg-tag">Конфигуратор · нажмите, чтобы открыть</span></span><span class="w-btn wide">Открыть конфигуратор</span><small>Версия, цвет, диски и салон – на официальных рендерах</small></button>
  <div class="cfg w-card" id="cfg" data-src="https://tema-mail.github.io/{proj}/"><button type="button" class="cfg-x" id="cfg-x" aria-label="Закрыть конфигуратор">×</button><div class="wait">Конфигуратор загрузится, когда блок окажется на экране</div></div>
  <div class="build"><span>Ваша сборка:</span> <b id="build-t">соберите машину выше</b><a class="w-btn sm" href="#cena">Посчитать эту сборку</a></div>
</div>
</section>

<section class="w-block sec" id="cena" data-n="7"
  data-question="Сколько будет стоить моя сборка в Минске со всеми платежами?"
  data-next="Можно ли не платить всю сумму сразу?"
  data-proof="Курс НБРБ; таможня – наш калькулятор растаможки РБ (формула ГТК customs.gov.by/calc + Указ № 428)"
  data-us="Прозрачность цены = доверие. Таможню считаем по правилам ГТК; доставку и работу дают Evolution."
  data-client="Видит, из чего цена, и что скрытых платежей нет. Строки пересчитываются под выбранную версию.">
<div class="w-wrap">
  <div class="logic"></div>
  <div class="cost">
    <div class="check w-card" id="check">
      <div class="ck-h"><b id="ck-h">{E(N)}</b><small>Минск · под ключ · курс НБРБ на <span data-kurs>{KURS_DATE}</span></small></div>
      <div class="r"><span>1. Цена в Китае</span><span id="ck-p"></span></div>
      <div class="r sub"><span>то же в долларах</span><span id="ck-usd"></span></div>
      <div class="r"><span>2. Доставка Китай → Минск</span><span class="ask w-ask">[запросить]</span></div>
      <div class="r"><span id="ck-tl">3. Таможня</span><span id="ck-t"></span></div>
      <div class="r sub"><span>то же в евро</span><span id="ck-te"></span></div>
      <div class="r sub" id="ck-alt" hidden><span>второй вариант: 15 % + НДС 20 %</span><span id="ck-a"></span></div>
      <div class="r"><span>4. Утильсбор и таможенный сбор</span><span>≈ 745 BYN <span class="ask w-ask">[сверить]</span></span></div>
      <div class="r"><span>5. Работа Evolution, ЭПТС, учёт</span><span class="ask w-ask">[запросить]</span></div>
      <div class="r tot"><span>Итого под ключ</span><span class="ask w-ask">[запросить]</span></div>
      <div class="ck-n" id="ck-note"></div>
    </div>
    <div class="cost-t">
      <span class="kicker">Растаможка {E(N)}</span>
      <h2>Из чего складывается цена {E(N)} под ключ</h2>
      <p>{E(cost_p)} Курс – НБРБ на день расчёта, оплата в BYN.</p>
      <p class="mut">Версия в чеке меняется, когда вы выбираете версию выше или собираете машину в конфигураторе.</p>
      <a class="w-btn" href="#raschet" data-goal="raschet">Получить точный расчёт в BYN</a>
    </div>
  </div>
</div>
</section>

<section class="w-block sec" id="lizing" data-n="8"
  data-question="Можно ли не платить всю сумму сразу?"
  data-next="Как я плачу за машину, которой ещё нет, и когда её получу?"
  data-proof="Лизинг у Evolution есть – подтвердил владелец 15.11.2026; условия партнёра – запросить"
  data-us="Расширяет круг покупателей: кто не готов отдать всю сумму сразу, остаётся. Отдельная цель в Метрике."
  data-client="Видит платёж в месяц под свой аванс и срок – решение «по карману» вместо «слишком дорого».">
<div class="w-wrap">
  <div class="logic"></div>
  <div class="lz w-card">
    <div><span class="kicker">Расчёт лизинга на {E(N)}</span><h2>Вы можете приобрести {E(N)} в лизинг или в кредит</h2><p>Оставьте заявку – просчитаем условия под ваш аванс и срок. Для физлиц и компаний. Партнёры: <span class="ask w-ask">[запросить]</span></p></div>
    <div>
      <span class="lb">Аванс</span><div class="chips" id="lz-a"><button type="button" data-a="10">10 %</button><button type="button" class="on" data-a="20">20 %</button><button type="button" data-a="30">30 %</button><button type="button" data-a="50">50 %</button></div>
      <span class="lb">Срок</span><div class="chips" id="lz-t"><button type="button" data-t="24">2 года</button><button type="button" class="on" data-t="36">3 года</button><button type="button" data-t="60">5 лет</button></div>
      <div class="lz-out"><small>Платёж в месяц</small><b><span class="ask w-ask">[ставка партнёра]</span></b><small id="lz-s">аванс 20 %, 3 года</small></div>
      <a class="w-btn" href="#raschet" data-goal="lizing">Получить график платежей</a>
    </div>
  </div>
</div>
</section>

<section class="w-block sec" id="zakaz" data-n="9"
  data-question="Как я плачу за машину, которой ещё нет, и когда её получу?"
  data-next="Что будет, если что-то пойдёт не так?"
  data-proof="Договор с ООО «Тренд Экспресс Авто», УНП 193710155; сроки и этапы оплаты – запросить"
  data-us="Убирает «а что дальше после оплаты» – меньше звонков с одним и тем же вопросом, меньше отказов на этапе договора."
  data-client="Шесть шагов со сроком и оплатой на каждом. Знает, когда платит и когда получит ключи.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Как заказать {E(N)} из Китая</span>
  <h2>Новый автомобиль у вас уже через <span class="ask w-ask">[N]</span> дней</h2>
  <ol class="steps w-steps m-lane" data-mob="lenta">
    <li><b>01</b><h3>Расчёт и выбор сборки</h3><p>В конфигураторе или с менеджером. Расчёт в $ и BYN – в течение часа</p></li>
    <li><b>02</b><h3>Договор и предоплата</h3><p>Договор с ООО «Тренд Экспресс Авто». Предоплата <span class="ask w-ask">[запросить: %]</span>, цена фиксируется <span class="ask w-ask">[запросить: в чём]</span></p></li>
    <li><b>03</b><h3>Выкуп у дилера в Китае</h3><p>Фото машины с вашей сборкой и VIN до отправки</p></li>
    <li><b>04</b><h3>Доставка до Минска</h3><p>Отчёт на каждой точке пути. Срок <span class="ask w-ask">[запросить]</span></p></li>
    <li><b>05</b><h3>Таможня, ЭПТС, учёт</h3><p>Оплата остатка <span class="ask w-ask">[запросить: когда]</span></p></li>
    <li><b>06</b><h3>Выдача в Минске</h3><p>Проспект Машерова, 15/4. Русификация и подготовка к зиме – до выдачи</p></li>
  </ol>
</div>
</section>

<section class="w-block sec" id="riski" data-n="10"
  data-question="Что будет, если что-то пойдёт не так?"
  data-next="Кто уже получил машину через вас?"
  data-proof="Условия договора Evolution – запросить по каждому риску"
  data-us="Отвечаем на возражения до того, как их задали менеджеру. У конкурентов этого блока нет."
  data-client="Получает честные ответы на четыре страха: курс, повреждение, срок, не та комплектация.">
<div class="w-wrap">
  <div class="logic"></div>
  <h2>Что будет, если при заказе что-то пойдёт не так</h2>
  <div class="risk w-grid m-lane" data-mob="lenta">
    <div class="w-card"><h3>Курс вырастет – цена вырастет?</h3><p><span class="ask w-ask">[запросить: что фиксируем в договоре]</span></p></div>
    <div class="w-card"><h3>Машину повредят в дороге?</h3><p><span class="ask w-ask">[запросить: страховка груза, кто платит]</span></p></div>
    <div class="w-card"><h3>Срок сорвётся?</h3><p><span class="ask w-ask">[запросить: что обещаем при задержке]</span></p></div>
    <div class="w-card"><h3>Привезут не ту комплектацию?</h3><p>Сборка из конфигуратора – часть договора, сверяем по фото и VIN до отправки. <span class="ask w-ask">[запросить: что если не совпало]</span></p></div>
  </div>
  <div class="w-actions"><a class="w-btn ghost" href="#raschet" data-goal="raschet">Получить образец договора</a></div>
</div>
</section>

<section class="w-block sec" id="vydachi" data-n="11"
  data-question="Кто уже получил машину через вас?"
  data-next="Кто будет обслуживать и ремонтировать машину из Китая?"
  data-proof="Фото выдач клиентам (номер размыт по рамке) и отзывы со ссылкой на площадку – запросить"
  data-us="Доказательство, что машины доходят. Только реальные выдачи и отзывы со ссылкой; рейтинг компании на модель не вешаем."
  data-client="Видит живых людей и машины, а не обещания.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Отзывы клиентов о работе Evolution Car</span>
  <h2>Выдачи автомобилей клиентам Evolution Car</h2>
  <div class="proof w-grid m-lane" data-mob="lenta">
    <div class="w-card ph"><div class="w-media">Фото выдачи {E(brand)} клиенту в Минске, номер размыт по рамке</div><p><span class="ask w-ask">[запросить: фото и дата]</span></p></div>
    <div class="w-card ph"><div class="w-media">Машина клиента на СВХ в Минске – путь из Китая</div><p><span class="ask w-ask">[запросить: фото]</span></p></div>
    <div class="w-card"><span class="q">“</span><p><span class="ask w-ask">[запросить: отзыв, имя, дата]</span></p><small>★★★★★ Яндекс Карты</small></div>
    <div class="w-card"><span class="q">“</span><p><span class="ask w-ask">[запросить: отзыв, имя, дата]</span></p><small>★★★★★ Google</small></div>
  </div>
</div>
</section>

<section class="w-block sec" id="servis" data-n="12"
  data-question="Кто будет обслуживать и ремонтировать машину из Китая?"
  data-next="Может, мне больше подойдёт {E(vs_names) or "другая модель"}?"
  data-proof="Evolution Car Service, Машерова 15/4: только китайские электромобили и гибриды от 2022 года; фото – реальный сервис"
  data-us="Главное преимущество перед импортёрами: покупка, русификация, ТО и ремонт в одном месте."
  data-client="Не надо искать мастера, который знает китайские машины: свой сервис в том же здании, где выдача.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Русификация, обслуживание и ремонт {E(N)} в Минске</span>
  <h2>Собственный сервис для автомобилей из Китая</h2>
  <p class="lead">Evolution Car Service – в том же здании на Машерова, 15/4. Работает только с китайскими электромобилями и гибридами от 2022 года. Ваш {E(N)} русифицируем до выдачи, а дальше обслуживаем и ремонтируем у себя.</p>
  <div class="srv">
    <figure class="of srv-ph"><img src="../img/serv-lift.webp" alt="Сервис Evolution Car в Минске: автомобили из Китая на подъёмниках" width="932" height="1243" loading="lazy"><figcaption>Сервис Evolution Car, Минск, проспект Машерова, 15/4</figcaption></figure>
    <div class="srv-g w-grid m-lane" data-mob="lenta">
      <div class="w-card"><h3>Русификация и ПО</h3><p>Русский язык, приложения, обновления, связь и мастер-аккаунт. Если язык слетит после обновления по воздуху – восстановим.</p></div>
      <div class="w-card"><h3>ТО по регламенту {E(brand)}</h3><p>Гарантия завода на привозные машины в Беларуси обычно не действует, поэтому ТО делаем по регламенту производителя и записываем работы в отчёт.</p></div>
      <div class="w-card"><h3>Тяговая батарея и электрика</h3><p>{E(srv_bat)}</p></div>
      <div class="w-card"><h3>Подвеска и ходовая</h3><p>Ремонт и адаптация подвески, в том числе пневматической, амортизаторы, тормоза.</p></div>
      <div class="w-card"><h3>Камеры и помощники водителя</h3><p>Калибровка камер и радаров после ремонта или замены стекла.</p></div>
      <div class="w-card"><h3>Запчасти из Китая</h3><p>Подбираем по VIN и заказываем напрямую у поставщиков: оригинал, стёкла, кузовные детали.</p></div>
    </div>
  </div>
  <div class="w-actions"><a class="w-btn" href="#raschet" data-goal="raschet">Узнать цену русификации и ТО {E(N)}</a><a class="w-btn ghost" href="https://evolutioncar.by/servis/">Подробнее о сервисе Evolution</a></div>
</div>
</section>

<section class="w-block sec" id="vs" data-n="13" data-mob="skryt"
  data-question="Может, мне больше подойдёт {E(vs_names)}?"
  data-next="Остались вопросы по деталям – где ответы?"
  data-proof="Данные соперников – из их карточек (те же источники, ноябрь 2026)"
  data-us="Сомневающийся не уходит к конкурентам, а идёт на нашу же карточку соседа. Перелинковка для SEO."
  data-client="Короткое сравнение машин одного класса и кому какая подходит.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Сравнение {E(N)}, {E(vs_names)}</span>
  <h2>Чем {E(N)} отличается от {E(vs_names)}</h2>
  <div class="w-table-wrap"><table class="vs">{vs_head}{vs_rows}</table></div>
  <div class="w-actions">{vs_btn}</div>
</div>
</section>

<section class="w-block sec" id="voprosy" data-mob="akkordeon" data-n="14"
  data-question="Остались вопросы по деталям – где ответы?"
  data-next="Как получить точный расчёт на мою сборку?"
  data-proof="Ответы – по данным производителя; вопросы – типовые по карточке 8X, Wordstat по этой модели снять отдельно"
  data-us="Хвосты поиска и быстрые ответы Яндекса и нейросетей (разметка FAQ). Последние возражения перед формой."
  data-client="Короткий ответ на свой вопрос в первой фразе, без звонка.">
<div class="w-wrap">
  <div class="logic"></div>
  <span class="kicker">Вопрос-ответ</span>
  <h2>Частые вопросы о {E(N)}</h2>
  <div class="qa" id="qa">{faq}</div>
</div>
</section>

<section class="w-block sec" id="raschet" data-n="15"
  data-question="Как получить точный расчёт на мою сборку?"
  data-next="Что ещё посмотреть, если {E(model)} не подошёл?"
  data-proof="Форма берёт версию, батарею, цвет и сборку со страницы; источник заявки и метки уходят вместе с ней"
  data-us="Заявка с полной сборкой и целью: расчёт, лизинг или кредит. Цели в Метрике раздельно. Картинки машины здесь нет: она уже была в первом экране и конфигураторе."
  data-client="Один телефон – и расчёт в BYN на свою машину, без пересказа менеджеру.">
<div class="w-wrap">
  <div class="logic"></div>
  <div class="fm-g w-card">
    <div class="fm-l">
      <span class="kicker">Стоимость {E(N)} в Беларуси</span>
      <h2>Рассчитаем точную стоимость под желаемую комплектацию и сборку</h2>
      <p class="mut" id="cv-t">{E(N)}</p>
    </div>
    <form class="w-form" id="fm" novalidate>
      <div id="goal-w"><span class="lb">Что нужно</span>
      <div class="seg" id="goal"><button type="button" class="on" data-g="raschet">Расчёт под ключ</button><button type="button" data-g="lizing">Лизинг</button><button type="button" data-g="kredit">Кредит</button></div></div>
      <span class="lb">Версия</span>
      <div class="seg" id="seg">{seg_form}</div>
      <label class="w-field"><span class="lb">Телефон</span><input name="tel" type="tel" inputmode="tel" autocomplete="tel" placeholder="+375 (__) ___-__-__"></label>
      <input type="text" name="website" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
      <label class="w-check"><input type="checkbox" name="agree"><span>Согласен на обработку <a href="#">персональных данных</a></span></label>
      <button class="w-btn wide" type="submit" disabled><span class="t">Получить расчёт {E(N)}</span></button>
      <p class="w-hint">Менеджер пришлёт расчёт с разбивкой по строкам в течение часа – звонком или в Telegram.</p>
      <div class="w-success" hidden><b>Заявка принята</b><p>Менеджер Evolution свяжется в течение часа в рабочее время 09:00 – 18:00. Срочно – звоните +375 (29) 135-88-88. Подготовьте: какую версию и цвет хотите, бюджет, нужен ли лизинг.</p><p class="mut" id="done-v"></p></div>
    </form>
  </div>
</div>
</section>

<section class="w-block sec" id="pohozhie" data-n="16"
  data-question="Что ещё посмотреть, если {E(model)} не подошёл?"
  data-proof="Карточки соседних моделей из этого набора"
  data-us="Не отпускаем человека с сайта: соседние модели, перелинковка."
  data-client="Похожие машины в один клик.">
<div class="w-wrap">
  <div class="logic"></div>
  <h2>Похожие автомобили</h2>
  <div class="sim w-grid m-lane" data-mob="lenta">{sim}</div>
  <p class="src">Обновлено {TODAY} · Проверил: <span class="ask w-ask">[запросить: имя и роль эксперта Evolution]</span></p>
</div>
</section>
</main>

<footer class="w-footer ft"><div class="w-wrap">
  <img src="../img/logo-evolution-car.webp" alt="Evolution Car" width="720" height="37">
  <p><a href="tel:+375291358888">+375 (29) 135-88-88</a> · ежедневно 09:00 – 18:00 · г. Минск, проспект Машерова, 15/4</p>
  <p class="mut">ООО «Тренд Экспресс Авто», УНП 193710155 · <a href="#">Политика обработки персональных данных</a> · <a href="#">Cookie</a></p>
  <div class="ft-big" aria-hidden="true">EVOLUTION CAR</div>
</div></footer>

<nav class="w-sticky tabbar" aria-label="Быстрое меню">
  <a href="#versii"><svg width="20" height="20"><use href="#car"/></svg>Версии</a>
  <a href="#test-drive" data-goal="test"><svg width="20" height="20"><use href="#key"/></svg>Тест-драйв</a>
  <a href="#raschet" data-goal="raschet"><svg width="20" height="20"><use href="#calc"/></svg>Расчёт</a>
  <button type="button" data-sheet="call"><svg width="20" height="20"><use href="#chat"/></svg>Связаться</button>
</nav>
<div class="sheet" id="sh-call" aria-hidden="true"><div class="sh-bg" data-close></div><div class="sh-box"><button class="sh-x" type="button" data-close aria-label="Закрыть">×</button>
  <b>Связаться с Evolution Car</b>
  <a class="sh-row" href="tel:+375291358888"><b>+375 (29) 135-88-88</b><small>ежедневно 09:00 – 18:00</small></a>
  <a class="sh-row" href="#"><b>Telegram</b><small>ответим в рабочее время</small></a>
  <a class="w-btn wide" href="#raschet" data-close data-goal="raschet">Получить расчёт под ключ</a>
</div></div>

<aside class="seo" id="seo" aria-hidden="true"><div class="seo-in">
  <button type="button" class="sh-x" data-seo-close aria-label="Закрыть">×</button>
  <h2>Цепочка блоков, SEO и источники</h2>
  <p class="mut">Для команды. На боевую страницу не идёт.</p>
  <div id="seo-chain"></div>
</div></aside>

<button id="tema" type="button" aria-label="Сменить тему">☀</button>
<script>window.CAR={json.dumps(CAR, ensure_ascii=False)};</script>
<script src="../calc.js?v=1"></script>
<script src="../karta.js?v=1"></script>
</body>
</html>
'''
    assert '—' not in page, 'длинное тире'
    os.makedirs(f'{R}/{sl}', exist_ok=True)
    open(f'{R}/{sl}/index.html', 'w').write(page)
    return {'proj': proj, 'slug': sl, 'name': N, 'min': mp, 'max': xp, 'versions': len(vers), 'ask': page.count('w-ask')}


if __name__ == '__main__':
    todo = sys.argv[1:] or sorted(f[:-5] for f in os.listdir(f'{R}/data') if f.endswith('.json'))
    done = []
    for p in todo:
        e = check(p)
        if e:
            print('ПРОПУСК', p, '; '.join(e[:3])); continue
        r = build(p); done.append(r)
        print('OK', r['slug'], r['name'], 'цены', r['min'], '–', r['max'], 'версий', r['versions'])
    json.dump(done, open(f'{R}/tools/sobrano.json', 'w'), ensure_ascii=False, indent=1) if not sys.argv[1:] else None
