/* Прототип карточки Zeekr 8X в дизайне EV Car. Без библиотек. Курс НБРБ и цены в Китае – на 15.11.2026. */
(function () {
  var d = document, root = d.documentElement;
  var $ = function (s, r) { return (r || d).querySelector(s) }, $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)) };
  var mob = function () { return innerWidth <= 760 };
  var fmt = function (n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') };
  var store = { get: function (k) { try { return localStorage.getItem(k) } catch (e) { return null } }, set: function (k, v) { try { localStorage.setItem(k, v) } catch (e) {} } };
  function lock(on) { root.style.overflow = on ? 'hidden' : '' }

  /* курс НБРБ на 15.11.2026: 1 USD = 3,0026 BYN; 1 EUR = 3,3312 BYN; 10 CNY = 4,5143 BYN */
  var K = { cny: 0.45143, usd: 3.0026, eur: 3.3312 }, CC = 1969;
  var toUsd = function (y) { return y * K.cny / K.usd }, toEur = function (y) { return y * K.cny / K.eur };
  /* таможня РБ, физлицо, новая машина: 48 % от стоимости, не меньше 7,5 €/см³ (стоимость 42 300 – 84 500 €); проверено калькулятором ГТК 15.11.2026 */
  function duty(y) { var e = toEur(y); var rate = e > 84500 ? [0.48, 20] : e > 42300 ? [0.48, 7.5] : e > 16950 ? [0.48, 5.5] : e > 8475 ? [0.48, 3.5] : [0.54, 2.5]; return Math.max(e * rate[0], CC * rate[1]) }

  var S = { goal: 'raschet', ver: '', bat: '', color: 'Чёрный «Полярная ночь»', build: '', td: 'Zeekr 8X', lzA: '20', lzT: '36' };

  /* тема */
  var tb = $('#tema');
  function tIcon() { tb.textContent = root.getAttribute('data-theme') === 'dark' ? '☀' : '☾' }
  tb.addEventListener('click', function () { var n = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', n); store.set('tema-ev8x', n); tIcon() }); tIcon();

  /* логика блоков и цепочка */
  var blocks = $$('main .w-block');
  blocks.forEach(function (b) {
    var l = $('.logic', b); if (!l) return;
    l.innerHTML = '<b>Блок ' + b.dataset.n + '.</b> Вопрос клиента: «' + b.dataset.question + '»<br><b>Нам:</b> ' + (b.dataset.us || '') + '<br><b>Клиенту:</b> ' + (b.dataset.client || '') +
      '<br><b>Опора:</b> ' + (b.dataset.proof || '') + (b.dataset.next ? '<br><b>Ведёт к вопросу:</b> «' + b.dataset.next + '»' : '');
  });
  $('#sw-logic').addEventListener('change', function (e) { d.body.classList.toggle('show-logic', e.target.checked) });
  var seoD = {}; try { seoD = JSON.parse($('#w-seo').textContent) } catch (e) {}
  $('#seo-chain').innerHTML = '<h3 style="margin-top:20px">Мета</h3><p>title: ' + seoD.title + '<br>description: ' + seoD.description + '<br>H1: ' + seoD.h1 + '<br>адрес: ' + seoD.url + '</p>' +
    '<h3 style="margin-top:20px">Запросы, Wordstat 11.11.2026, Минск / Беларусь</h3><p>' + (seoD.keys || []).join('<br>') + '</p>' +
    '<h3 style="margin-top:20px">Цепочка блоков</h3><table><tr><th>№</th><th>Вопрос клиента</th><th>Нам</th><th>Клиенту</th></tr>' +
    blocks.map(function (b) { return '<tr><td>' + b.dataset.n + '</td><td>' + b.dataset.question + '</td><td>' + (b.dataset.us || '') + '</td><td>' + (b.dataset.client || '') + '</td></tr>' }).join('') + '</table>';
  var seo = $('#seo');
  function seoOpen(o) { seo.classList.toggle('open', o); seo.setAttribute('aria-hidden', !o); lock(o) }
  $('#sw-seo').addEventListener('click', function () { seoOpen(true) });
  $('[data-seo-close]').addEventListener('click', function () { seoOpen(false) });
  seo.addEventListener('click', function (e) { if (e.target === seo) seoOpen(false) });

  /* цвет кузова */
  var C = [['008', 'Чёрный «Полярная ночь»'], ['009', 'Белый «Полярный день»'], ['010', 'Светло-серый «Базальт»'], ['011', 'Тёмно-серый «Лунное море»'], ['012', 'Янтарно-красный']];
  var stage = $('#stage'), dots = $('#dots');
  dots.innerHTML = C.map(function (c, i) { return '<button type="button" role="radio" aria-label="' + c[1] + '" aria-checked="' + !i + '" data-c="' + c[0] + '" style="background-image:url(img/s-' + c[0] + '.webp)"' + (i ? '' : ' class="on"') + '></button>' }).join('');
  function paint(code) {
    var c = C.filter(function (x) { return x[0] === code })[0]; if (!c) return; S.color = c[1];
    $$('button', dots).forEach(function (b) { var on = b.dataset.c === code; b.classList.toggle('on', on); b.setAttribute('aria-checked', on) });
    $('#cname').textContent = c[1];
    var old = $('img.on', stage); if (old && old.dataset.c === code) return;
    var im = new Image(); im.src = 'img/c-' + code + '.webp'; im.alt = 'Zeekr 8X 2026, ' + c[1].toLowerCase() + ', официальный рендер'; im.width = 1600; im.height = 725; im.dataset.c = code;
    stage.appendChild(im); requestAnimationFrame(function () { requestAnimationFrame(function () { im.classList.add('on'); if (old) { old.classList.remove('on'); setTimeout(function () { old.remove() }, 700) } }) });
    formNote(); store.set('ev8x-color', code);
  }
  dots.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) paint(b.dataset.c) });
  var sc = store.get('ev8x-color'); if (sc && sc !== '008') paint(sc);

  /* подсветка разделов в шапке и во вкладках обзора */
  var otabs = $$('#otabs a');
  /* на телефоне обзор – вкладки: показан один раздел, страница не растягивается на 6 экранов */
  function obAct(id) { $$('.ob').forEach(function (o) { o.classList.toggle('act', o.id === id) }); otabs.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + id) }) }
  obAct('o-ext');
  otabs.forEach(function (a) { a.addEventListener('click', function (e) { if (!mob()) return; e.preventDefault(); obAct(a.getAttribute('href').slice(1)); $('#otabs').scrollIntoView({ block: 'start' }) }) });
  function onScroll() {
    var on = null; $$('.hd-nav a').forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 140) on = a }); $$('.hd-nav a').forEach(function (a) { a.classList.toggle('on', a === on) });
    if (!mob()) { var oo = otabs[0]; otabs.forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 200) oo = a }); otabs.forEach(function (a) { a.classList.toggle('on', a === oo) }) }
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* версии */
  var V = [
    { id: '67', n: 'Max', img: 'v-max', tag: 'Начальная', b: { 55: [356800, 320, 1362], 70: [371800, 410, 1416] }, def: '55', li: ['один экран 16″', 'диски 21″, Brembo', 'пневмоподвеска', 'H7, один лидар'] },
    { id: '68', n: 'Ultra', img: 'v-ultra', tag: 'Сбалансированная', b: { 55: [376800, 318, 1357], 70: [391800, 410, 1416] }, def: '70', li: ['экран для пассажира', 'аудиосистема Naim', 'потолочный экран 17″', 'автодвери'] },
    { id: '69', n: 'Ultra+', img: 'v-ultraplus', tag: 'Лучшее шасси', b: { 55: [411800, 318, null], 70: [426800, 410, 1416] }, def: '70', li: ['диски 22″', 'амортизаторы CCD', 'активный стабилизатор', 'всё из Ultra'] },
    { id: '70', n: 'Shadow', img: 'v-shadow', tag: '3 мотора, 1030 кВт', b: { 70: [500800, 330, 1210] }, def: '70', li: ['2,96 с до 100', 'H9, 5 лидаров, ночное видение', 'кованые 22″, Brembo 6 поршней', 'спортивные ковши'] }
  ];
  var vb = $('#vers');
  vb.innerHTML = V.map(function (v, i) {
    var bats = Object.keys(v.b);
    return '<div class="w-card v4" data-i="' + i + '">' +
      '<div class="vi"><img src="img/' + v.img + '.webp" alt="Zeekr 8X ' + v.n + '" width="1600" height="725" loading="lazy"></div>' +
      '<div class="nm">' + v.n + '</div><div class="tg">' + v.tag + '</div>' +
      '<div class="bt">' + bats.map(function (b) { return '<button type="button" data-b="' + b + '"' + (b === v.def ? ' class="on"' : '') + (bats.length < 2 ? ' disabled' : '') + '>' + b + ' кВт·ч</button>' }).join('') + '</div>' +
      '<div class="cn"><span data-p></span><small data-u></small></div>' +
      '<div class="tk">Под ключ в Минске: <span class="ask w-ask">[запросить]</span></div>' +
      '<div class="rn"><div><b data-e></b>на электричестве</div><div><b data-t></b>всего, CLTC</div></div>' +
      '<ul>' + v.li.map(function (x) { return '<li>' + x + '</li>' }).join('') + '</ul>' +
      '<a class="w-btn sm wide" href="#konfigurator" data-cfg="' + v.id + '">Собрать ' + v.n + '</a></div>';
  }).join('');
  $('#n-ask').textContent = $$('main .w-ask').length;
  var cards = $$('.v4', vb);
  function cardUpd(card, b) {
    var x = V[+card.dataset.i].b[b]; card.dataset.b = b;
    $$('.bt button', card).forEach(function (bt) { bt.classList.toggle('on', bt.dataset.b === b) });
    $('[data-p]', card).textContent = fmt(x[0]) + ' ¥'; $('[data-u]', card).textContent = 'в Китае · ≈ ' + fmt(toUsd(x[0])) + ' $';
    $('[data-e]', card).textContent = x[1] + ' км'; $('[data-t]', card).textContent = x[2] ? x[2] + ' км' : '–';
  }
  cards.forEach(function (c) { cardUpd(c, V[+c.dataset.i].def) });
  function pickVer(i, b, fromForm) {
    var v = V[i], y = v.b[b][0], t = duty(y); S.ver = v.n; S.bat = b;
    cards.forEach(function (c, k) { c.classList.toggle('on', k === i) });
    $('#ck-h').textContent = 'Zeekr 8X ' + v.n + ' ' + b; $('#ck-p').textContent = fmt(y) + ' ¥'; $('#ck-usd').textContent = '≈ ' + fmt(toUsd(y)) + ' $';
    $('#ck-t').textContent = '≈ ' + fmt(t) + ' €'; $('#ck-tb').textContent = '≈ ' + fmt(t * K.eur) + ' BYN';
    if (!fromForm) $$('#seg button').forEach(function (x) { x.classList.toggle('on', x.dataset.v === v.n) });
    formNote();
  }
  vb.addEventListener('click', function (e) {
    var card = e.target.closest('.v4'); if (!card) return; var bt = e.target.closest('.bt button');
    if (bt && !bt.disabled) cardUpd(card, bt.dataset.b);
    pickVer(+card.dataset.i, card.dataset.b);
  });
  pickVer(1, '70'); cards[1].classList.remove('on'); S.ver = ''; $$('#seg button').forEach(function (x, k) { x.classList.toggle('on', k === 0) });

  /* сравнение */
  var cmp = $('#cmp');
  $$('#cmp tbody[data-g] tr:not(.gh)').forEach(function (tr) {
    var tds = $$('td', tr).slice(1);
    tds.forEach(function (td) { var t = td.textContent.trim(); if (t === '✓') td.classList.add('yes'); if (t === '–') td.classList.add('no') });
    var t0 = tds[0] && tds[0].textContent.trim(); if (tds.length === 4 && tds.every(function (td) { return td.textContent.trim() === t0 })) tr.classList.add('same');
  });
  $('#only-diff').addEventListener('change', function (e) { cmp.classList.toggle('diff', e.target.checked) });
  if (mob()) $$('#cmp tbody[data-g]').forEach(function (g, i) { if (i) g.classList.add('cl') });
  $$('#cmp tbody[data-g]').forEach(function (g) { $('.gh button', g).addEventListener('click', function () { g.classList.toggle('cl') }) });
  $('#all-open').addEventListener('click', function () { var any = $$('#cmp tbody.cl').length; $$('#cmp tbody[data-g]').forEach(function (g) { g.classList.toggle('cl', !any) }); this.textContent = any ? 'Свернуть все группы' : 'Раскрыть все группы' });

  /* конфигуратор: фрейм с того же домена tema-mail.github.io – сборка уходит в чек и форму */
  var cfg = $('#cfg'), frame = null, cfgVer = '68';
  function hook() {
    try {
      var w = frame.contentWindow, doc = frame.contentDocument; if (!doc || !doc.body) return;
      var fit = function () { frame.style.height = mob() ? Math.max(640, doc.documentElement.scrollHeight) + 'px' : Math.min(900, Math.max(700, innerHeight - 110)) + 'px' };
      fit(); addEventListener('resize', fit); if (w.ResizeObserver) new w.ResizeObserver(fit).observe(doc.body);
      var take = function (det) {
        if (!det) return; S.build = det.text || '';
        $('#build-t').textContent = (det.lines || []).map(function (l) { return l[1] }).join(' · ') || det.text;
        V.forEach(function (v, k) { if (v.id === String(det.version)) { var bl = (det.lines || []).filter(function (l) { return /батаре/i.test(l[0]) })[0], bb = bl && (bl[1].match(/55|70/) || [])[0]; if (bb) cardUpd(cards[k], bb); pickVer(k, bb || cards[k].dataset.b) } });
      };
      doc.addEventListener('zeekr:change', function (e) { take(e.detail) });
      if (w.ZeekrCfg) take(w.ZeekrCfg.get());
    } catch (e) { /* фрейм с другого адреса – работает сам, без связи с формой */ }
  }
  function loadCfg(id) {
    cfgVer = id || cfgVer; $$('#cfg-seg button').forEach(function (b) { b.classList.toggle('on', b.dataset.v === cfgVer) });
    if (!frame) { frame = d.createElement('iframe'); frame.title = 'Конфигуратор Zeekr 8X'; frame.onload = function () { var w = $('.wait', cfg); if (w) w.remove(); hook() }; cfg.appendChild(frame) }
    frame.src = cfg.dataset.src + '?v=' + cfgVer + '#v=' + cfgVer;
  }
  var cio = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { cio.disconnect(); if (!frame) loadCfg() } }, { rootMargin: '600px 0px' });
  cio.observe(cfg);
  $$('#cfg-seg button').forEach(function (b) { b.addEventListener('click', function () { loadCfg(b.dataset.v) }) });
  d.addEventListener('click', function (e) { var a = e.target.closest('[data-cfg]'); if (a) { cio.disconnect(); loadCfg(a.dataset.cfg) } });

  /* тест-драйв и лизинг */
  function chips(id, key, after) { $$('#' + id + ' button').forEach(function (b) { b.addEventListener('click', function () { $$('#' + id + ' button').forEach(function (x) { x.classList.toggle('on', x === b) }); var k = Object.keys(b.dataset)[0]; S[key] = b.dataset[k]; if (after) after() }) }) }
  chips('lz-a', 'lzA', lz); chips('lz-t', 'lzT', lz);
  function lz() { $('#lz-s').textContent = 'аванс ' + S.lzA + ' %, ' + ({ 24: '2 года', 36: '3 года', 60: '5 лет' })[S.lzT] }

  /* форма: кнопка активна только с галочкой; цель, версия, цвет и сборка уходят в заявку */
  var fm = $('#fm'), tel = fm.tel, sub = $('button[type=submit]', fm);
  var GOAL = { raschet: 'Получить расчёт Zeekr 8X', test: 'Уточнить наличие и тест-драйв', lizing: 'Получить график лизинга', kredit: 'Получить расчёт кредита' };
  function setGoal(g) { S.goal = g; $$('#goal button').forEach(function (b) { b.classList.toggle('on', b.dataset.g === g) }); $('.t', fm).textContent = GOAL[g]; $('#goal-w').hidden = g === 'test' }
  function formNote() { $('#cv-t').textContent = 'Zeekr 8X' + (S.ver ? ' ' + S.ver + ' ' + S.bat + ' кВт·ч' : '') + ' · ' + S.color.toLowerCase() + (S.build ? ' · сборка из конфигуратора приложена' : ' · сборка из конфигуратора будет приложена') }
  $$('#goal button').forEach(function (b) { b.addEventListener('click', function () { setGoal(b.dataset.g) }) });
  d.addEventListener('click', function (e) { var a = e.target.closest('[data-goal]'); if (a) setGoal(a.dataset.goal) });
  $$('#seg button').forEach(function (b) { b.addEventListener('click', function () {
    $$('#seg button').forEach(function (x) { x.classList.toggle('on', x === b) });
    var i = -1; V.forEach(function (v, k) { if (v.n === b.dataset.v) i = k });
    if (i > -1) pickVer(i, cards[i].dataset.b, true); else { S.ver = ''; formNote() }
  }) });
  function mask(v) { var x = v.replace(/\D/g, ''); if (x.indexOf('375') === 0) x = x.slice(3); x = x.slice(0, 9); var r = '+375'; if (x.length) r += ' (' + x.slice(0, 2); if (x.length >= 2) r += ')'; if (x.length > 2) r += ' ' + x.slice(2, 5); if (x.length > 5) r += '-' + x.slice(5, 7); if (x.length > 7) r += '-' + x.slice(7, 9); return r }
  tel.addEventListener('focus', function () { if (!tel.value) tel.value = '+375 (' });
  tel.addEventListener('blur', function () { if (tel.value.replace(/\D/g, '').length <= 3) tel.value = '' });
  tel.addEventListener('input', function () { tel.value = mask(tel.value); tel.closest('.w-field').classList.remove('bad') });
  fm.agree.addEventListener('change', function () { sub.disabled = !fm.agree.checked });
  fm.addEventListener('submit', function (e) {
    e.preventDefault();
    if (tel.value.replace(/\D/g, '').length < 12) { tel.closest('.w-field').classList.add('bad'); tel.focus(); return }
    if (fm.website.value) return;
    var utm = []; new URLSearchParams(location.search).forEach(function (v, k) { if (/^utm_|yclid|gclid/.test(k)) utm.push(k + '=' + v) });
    var parts = [({ raschet: 'Расчёт под ключ', test: 'Тест-драйв: ' + S.td, lizing: 'Лизинг: аванс ' + S.lzA + ' %, ' + S.lzT + ' мес', kredit: 'Кредит' })[S.goal],
      S.ver ? 'Zeekr 8X ' + S.ver + ' ' + S.bat + ' кВт·ч' : 'версия не выбрана', S.color, S.build ? 'сборка: ' + S.build : '', tel.value];
    $('.w-success', fm).hidden = false; sub.hidden = true;
    $('#done-v').textContent = 'В заявке: ' + parts.filter(Boolean).join(' · ') + ' · страница ' + location.pathname + (utm.length ? ' · ' + utm.join(', ') : '') + ' (в прототипе никуда не уходит)';
  });

  /* окно «Связаться» */
  function closeS() { $$('.sheet.open').forEach(function (s) { s.classList.remove('open'); s.setAttribute('aria-hidden', 'true') }); lock(false) }
  $$('[data-sheet]').forEach(function (b) { b.addEventListener('click', function () { var s = $('#sh-' + b.dataset.sheet); s.classList.add('open'); s.setAttribute('aria-hidden', 'false'); lock(true) }) });
  $$('.sheet [data-close]').forEach(function (b) { b.addEventListener('click', closeS) });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeS(); seoOpen(false) } });
})();

/* видео: preload="none" + постер; src ставится, когда блок в 300 px от экрана; вне экрана – пауза.
   Экономия трафика или «меньше движения» – без автозапуска, кнопка «смотреть». */
(function () {
  var vids = [].slice.call(document.querySelectorAll('video[data-src]')); if (!vids.length) return;
  var save = navigator.connection && navigator.connection.saveData, still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function load(v) { if (!v.src) { v.src = (innerWidth <= 760 && v.dataset.srcM) ? v.dataset.srcM : v.dataset.src; v.load() } }
  vids.forEach(function (v) {
    var fig = v.closest('.vid'), btn = fig && fig.querySelector('.vplay');
    if (save || still) { fig.classList.add('manual'); if (btn) btn.addEventListener('click', function () { load(v); v.play(); fig.classList.remove('manual') }); return }
    new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { load(v); var p = v.play(); if (p && p.catch) p.catch(function () { fig.classList.add('manual') }) } else if (v.src) v.pause() }) }, { rootMargin: '300px 0px', threshold: 0 }).observe(v);
  });
})();

/* ===== Мобильная вёрстка: ленты со счётчиком, сравнение двух версий, конфигуратор на весь экран ===== */
(function () {
  var d = document, $ = function (s, r) { return (r || d).querySelector(s) }, $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)) };
  var mob = function () { return innerWidth <= 760 };
  // «8X, 9X или L9» на телефоне не показываем (владелец 15.11.2026), таблица только на десктопе
  // счётчик «1 / N» и точки под каждой лентой
  $$('.m-lane').forEach(function (lane) {
    var items = [].slice.call(lane.children); if (items.length < 2) return;
    var meta = d.createElement('div'); meta.className = 'lane-meta';
    meta.innerHTML = '<span><b>1</b> / ' + items.length + ' · листайте вбок →</span><span class="lane-dots">' + items.map(function (_, i) { return '<i' + (i ? '' : ' class="on"') + '></i>' }).join('') + '</span>';
    lane.after(meta);
    var tick = false;
    lane.addEventListener('scroll', function () { if (tick) return; tick = true; requestAnimationFrame(function () {
      tick = false; var w = items[0].getBoundingClientRect().width + 12, k = Math.min(items.length - 1, Math.round(lane.scrollLeft / w));
      $('b', meta).textContent = k + 1; $$('.lane-dots i', meta).forEach(function (x, j) { x.classList.toggle('on', j === k) });
    }) }, { passive: true });
  });
  // сравнение комплектаций: на телефоне две версии рядом
  var cmp = $('#cmp');
  if (cmp) {
    var names = $$('thead th', cmp).slice(1).map(function (th) { return $('b', th).textContent });
    var pick = d.createElement('div'); pick.className = 'cmp-pick';
    pick.innerHTML = '<span class="lb" style="width:100%;margin:0 0 4px">Сравнить две версии</span>' + names.map(function (n, i) { return '<button type="button" data-i="' + i + '"' + (i < 2 ? ' class="on"' : '') + '>' + n + '</button>' }).join('');
    cmp.before(pick);
    var sel = [0, 1];
    function apply() {
      cmp.classList.toggle('two', mob());
      $$('tr', cmp).forEach(function (tr) {
        if (tr.classList.contains('gh')) return;
        var cells = [].slice.call(tr.children).slice(1);
        cells.forEach(function (c, i) { c.classList.toggle('off', cells.length === 4 && sel.indexOf(i) < 0) });
      });
      $$('button', pick).forEach(function (b) { b.classList.toggle('on', sel.indexOf(+b.dataset.i) > -1) });
    }
    pick.addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; var i = +b.dataset.i; if (sel.indexOf(i) > -1) return; sel = [sel[1], i]; apply() });
    apply(); addEventListener('resize', apply);
  }
  // конфигуратор на весь экран: фрейм грузится только по нажатию
  var open = $('#cfg-open'), cfg = $('#cfg'), x = $('#cfg-x');
  if (open && cfg) {
    open.addEventListener('click', function () { cfg.classList.add('full'); d.documentElement.style.overflow = 'hidden'; var b = $('#cfg-seg button.on'); if (b) b.click(); else if (!$('iframe', cfg)) { var s = $('[data-cfg="68"]'); if (s) s.click() } });
    x.addEventListener('click', function () { cfg.classList.remove('full'); d.documentElement.style.overflow = ''; });
  }
})();
/* нижняя панель на телефоне появляется, когда первый экран ушёл вверх – не закрывает его кнопки */
(function () {
  var hero = document.getElementById('hero'); if (!hero) return;
  function upd() { document.body.classList.toggle('tb', hero.getBoundingClientRect().bottom < innerHeight * 0.4) }
  addEventListener('scroll', upd, { passive: true }); upd();
})();
