/* Прототип карточки Zeekr 8X под заказ. Основа – v3 карточки 9X; добавлены версии с батареей, сравнение комплектаций,
   обзор с фото, тест-драйв и лизинг, конфигуратор без 3D со сборкой в форму. Без библиотек. */
(function () {
  var d = document, root = d.documentElement;
  var $ = function (s, r) { return (r || d).querySelector(s) }, $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)) };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  var mob = function () { return innerWidth <= 760 }, E = 'cubic-bezier(.32,.72,0,1)';
  var store = { get: function (k) { try { return JSON.parse(localStorage.getItem(k)) } catch (e) { return null } }, set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)) } catch (e) {} } };
  var fmt = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') };
  function lock(on) { root.style.overflow = on ? 'hidden' : '' }
  function seen(el, fn, th) { new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting, e) }) }, { threshold: th || .3 }).observe(el) }

  /* состояние страницы: что выбрал человек – уходит в форму */
  var S = { goal: 'raschet', ver: '', bat: '', color: 'Чёрный «Полярная ночь»', build: '', tdModel: 'Zeekr 8X', lzA: '20', lzT: '36' };

  /* ---------- тема ---------- */
  var tb = $('#tema');
  function tIcon() { tb.textContent = root.getAttribute('data-theme') === 'dark' ? '☀' : '☾' }
  tb.addEventListener('click', function () { var n = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', n); try { localStorage.setItem('tema-z8x', n) } catch (e) {} tIcon() }); tIcon();

  /* ---------- логика блоков, метки, SEO-паспорт ---------- */
  $$('[data-q]').forEach(function (s, i) {
    var l = $('.logic', s); if (!l) return;
    l.innerHTML = '<b>Блок ' + (i + 1) + '.</b> Вопрос клиента: «' + s.dataset.q + '»' + (s.dataset.why ? '<br>Зачем: ' + s.dataset.why : '');
  });
  $('#n-ask').textContent = $$('main .ask, .sticky .ask').length;
  $('#sw-logic').addEventListener('change', function (e) { d.body.classList.toggle('show-logic', e.target.checked) });
  var seo = $('#seo');
  function seoOpen(o) { seo.classList.toggle('open', o); seo.setAttribute('aria-hidden', !o); lock(o) }
  $('#sw-seo').addEventListener('click', function () { seoOpen(true) });
  $('[data-seo-close]').addEventListener('click', function () { seoOpen(false) });
  seo.addEventListener('click', function (e) { if (e.target === seo) seoOpen(false) });

  /* ---------- появление ---------- */
  if (!reduce) {
    var io = new IntersectionObserver(function (es) {
      es.filter(function (e) { return e.isIntersecting }).forEach(function (e, i) { io.unobserve(e.target); e.target.style.transitionDelay = i * 90 + 'ms'; e.target.classList.add('in') });
    }, { rootMargin: '0px 0px -10% 0px' });
    $$('.rv').forEach(function (el) { io.observe(el) });
  } else $$('.rv').forEach(function (el) { el.classList.add('in') });
  $$('[data-n]').forEach(function (el, i) {
    var n = +el.dataset.n; if (reduce) return; el.textContent = 0;
    setTimeout(function () { var t0 = performance.now(); (function tick(t) { var k = Math.min(1, (t - t0) / 1600); k = 1 - Math.pow(1 - k, 4); el.textContent = Math.round(n * k); if (k < 1) requestAnimationFrame(tick) })(t0) }, 900 + i * 120);
  });

  /* ---------- витрина: цвет кузова ---------- */
  var C = [['008', 'Чёрный «Полярная ночь»', '#3b5bff'], ['009', 'Белый «Полярный день»', '#8fb0ff'], ['010', 'Светло-серый «Базальт»', '#9fb3cc'],
    ['011', 'Тёмно-серый «Лунное море»', '#6b84a8'], ['012', 'Янтарно-красный', '#c0405a']];
  var car = $('#car'), refl = $('.refl', car), dots = $('#sw .dots');
  dots.innerHTML = C.map(function (c, i) { return '<button type="button" role="radio" aria-label="' + c[1] + '" data-c="' + c[0] + '" style="background-image:url(img/s-' + c[0] + '.webp)"' + (i ? ' aria-checked="false"' : ' class="on" aria-checked="true"') + '></button>' }).join('');
  C.forEach(function (c) { if (c[0] !== '008') { var im = new Image(); im.src = 'img/c-' + c[0] + '.webp' } });
  function paint(code, first) {
    var c = C.filter(function (x) { return x[0] === code })[0]; if (!c) return;
    root.style.setProperty('--glow', c[2]); S.color = c[1];
    $$('button', dots).forEach(function (b) { var on = b.dataset.c === code; b.classList.toggle('on', on); b.setAttribute('aria-checked', on) });
    $('#cn').textContent = c[1];
    [car, refl].forEach(function (box) {
      var old = $('img.on', box); if (old && old.dataset.c === code) return;
      var im = new Image(); im.src = 'img/c-' + code + '.webp'; im.alt = box === car ? 'Zeekr 8X 2026, цвет ' + c[1] + ', официальный рендер' : ''; im.dataset.c = code; im.width = 1600; im.height = 725;
      box.appendChild(im); requestAnimationFrame(function () { requestAnimationFrame(function () { im.classList.add('on'); if (old) { old.classList.remove('on'); setTimeout(function () { old.remove() }, 1400) } }) });
    });
    $('#cv-img').src = 'img/c-' + code + '.webp'; $('#cv-c').textContent = c[1];
    if (!first) store.set('z8x-color', code);
  }
  dots.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) paint(b.dataset.c) });
  var saved = store.get('z8x-color'); if (saved && saved !== '008') paint(saved, true);
  if (fine && !reduce) {
    var big = $('#big9'), sc = $('#scene');
    sc.addEventListener('mousemove', function (e) { var r = sc.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      big.style.transform = 'translate(calc(-50% + ' + (-x * 30) + 'px),calc(-50% + ' + (-y * 16) + 'px))'; car.style.transform = 'translateX(calc(-50% + ' + (x * 14) + 'px))' });
    big.style.transition = car.style.transition = 'transform 1.2s ' + E;
  }
  if (!reduce) { $('#h1').animate([{ opacity: 0, transform: 'translateY(40px)', filter: 'blur(10px)' }, { opacity: 1, transform: 'none', filter: 'none' }], { duration: 1300, easing: E, fill: 'both', delay: 150 });
    car.animate([{ opacity: 0, transform: 'translateX(-38%) scale(.97)' }, { opacity: 1, transform: 'translateX(-50%)' }], { duration: 1800, easing: 'cubic-bezier(.16,1,.3,1)', delay: 300, fill: 'backwards' }) }

  /* ---------- шоурум: проезд при прокрутке ---------- */
  var show = $('#show'), road = $('#road'), specs = $$('#specs > div'), tick = false;
  function showUpd() {
    tick = false; var r = show.getBoundingClientRect(), total = show.offsetHeight - innerHeight, p = Math.min(1, Math.max(0, -r.top / total));
    var w = road.offsetWidth, vw = innerWidth, k = Math.min(1, p / .55), ease = 1 - Math.pow(1 - k, 3);
    var start = vw + 40, end = (vw - w) / 2, x = start + (end - start) * ease - Math.max(0, p - .7) / .3 * (vw * .25);
    road.style.setProperty('--x', x.toFixed(1));
    specs.forEach(function (s, i) { s.classList.toggle('on', p > .15 + i * .18) });
  }
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(showUpd) } }, { passive: true }); addEventListener('resize', showUpd); showUpd();

  /* ---------- навигация ---------- */
  var nav = $('#nav'), hero = $('#hero'), sticky = $('#sticky'), mnav = $('#mnav'), form = $('#raschet');
  function pb() { root.style.setProperty('--pb', $('.pbar').offsetHeight + 'px') } pb(); addEventListener('resize', pb);
  var otabs = $$('#otabs a');
  function onScroll() {
    d.body.classList.toggle('pbar-on', scrollY < 30);
    var past = hero.getBoundingClientRect().bottom < innerHeight * .3, fr = form.getBoundingClientRect(), atForm = fr.top < innerHeight && fr.bottom > 0;
    sticky.classList.toggle('on', past && !atForm); mnav.classList.toggle('on', past); d.body.classList.toggle('tb', past);
    var on = null; $$('.ln a', nav).forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 160) on = a }); $$('.ln a', nav).forEach(function (a) { a.classList.toggle('on', a === on) });
    var oo = otabs[0]; otabs.forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 220) oo = a });
    otabs.forEach(function (a) { a.classList.toggle('on', a === oo) });
    var cmp = $('#cmp'), th = $('#cmp thead'); if (cmp && th) { var cr = cmp.getBoundingClientRect(); cmp.classList.toggle('stuck', cr.top < 60 && cr.bottom > 300) }
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var mm = $('#mm');
  function menu(o) { d.body.classList.toggle('menu-open', o); mm.setAttribute('aria-hidden', !o); lock(o); $$('a', mm).forEach(function (a, i) { a.style.transitionDelay = o ? 100 + i * 50 + 'ms' : '0ms' }) }
  $('#bur').addEventListener('click', function () { menu(!d.body.classList.contains('menu-open')) });
  $$('a', mm).forEach(function (a) { a.addEventListener('click', function () { menu(false) }) });

  /* ---------- версии: 4 карточки, батарея меняет цену и запас ---------- */
  var V = [
    { id: '67', n: 'Max', img: 'v-max', tag: 'Начальная', b: { 55: [356800, 320, 1362], 70: [371800, 410, 1416] }, def: '55', li: ['один экран 16″', 'диски 21″, Brembo', 'пневмоподвеска', 'H7, 1 лидар'] },
    { id: '68', n: 'Ultra', img: 'v-ultra', tag: 'Самая сбалансированная', b: { 55: [376800, 318, 1357], 70: [391800, 410, 1416] }, def: '70', li: ['второй экран для пассажира', 'аудиосистема Naim', 'потолочный экран 17″', 'автодвери'] },
    { id: '69', n: 'Ultra+', img: 'v-ultraplus', tag: 'Лучшее шасси', b: { 55: [411800, 318, null], 70: [426800, 410, 1416] }, def: '70', li: ['диски 22″', 'амортизаторы CCD', 'активный стабилизатор', 'всё из Ultra'] },
    { id: '70', n: 'Shadow', img: 'v-shadow', tag: '3 мотора, 1030 кВт', b: { 70: [500800, 330, 1210] }, def: '70', li: ['2,96 с до 100', 'H9, 5 лидаров, ночное видение', 'кованые 22″, Brembo 6 поршней', 'спортивные ковши'] }
  ];
  var vb = $('#vers');
  vb.innerHTML = V.map(function (v, i) {
    var bats = Object.keys(v.b);
    return '<div class="bz v4 rv" data-i="' + i + '"><div class="core">' +
      '<div class="vi"><img src="img/' + v.img + '.webp" alt="Zeekr 8X ' + v.n + '" width="1600" height="725" loading="lazy"></div>' +
      '<div class="nm">' + v.n + '</div><div class="tg">' + v.tag + '</div>' +
      (bats.length > 1 ? '<div class="bt">' + bats.map(function (b) { return '<button type="button" data-b="' + b + '"' + (b === v.def ? ' class="on"' : '') + '>' + b + ' кВт·ч</button>' }).join('') + '</div>' : '<div class="bt"><button type="button" class="on" data-b="70" disabled>70 кВт·ч</button></div>') +
      '<div class="cn"><span data-p></span><small>цена в Китае</small></div>' +
      '<div class="tk">Под ключ в Минске: <span class="ask">[запросить: $]</span></div>' +
      '<div class="rn"><div><b data-e></b>на электричестве</div><div><b data-t></b>всего, CLTC</div></div>' +
      '<ul>' + v.li.map(function (x) { return '<li>' + x + '</li>' }).join('') + '</ul>' +
      '<a class="btn acc go" href="#konfigurator" data-cfg="' + v.id + '">Собрать ' + v.n + '<b><svg width="16" height="16"><use href="#ar"/></svg></b></a>' +
      '</div></div>';
  }).join('');
  if (!reduce) $$('.v4.rv', vb).forEach(function (el) { io.observe(el) }); else $$('.v4', vb).forEach(function (el) { el.classList.add('in') });
  $('#n-ask').textContent = $$('main .ask, .sticky .ask').length;
  var cards = $$('.v4', vb);
  function cardUpd(card, b) {
    var v = V[+card.dataset.i], x = v.b[b]; card.dataset.b = b;
    $$('.bt button', card).forEach(function (bt) { bt.classList.toggle('on', bt.dataset.b === b) });
    $('[data-p]', card).textContent = fmt(x[0]) + ' ¥'; $('[data-e]', card).textContent = x[1] + ' км'; $('[data-t]', card).textContent = x[2] ? x[2] + ' км' : '–';
  }
  cards.forEach(function (c) { cardUpd(c, V[+c.dataset.i].def) });
  function pickVer(i, b, fromForm) {
    var v = V[i]; S.ver = v.n; S.bat = b;
    cards.forEach(function (c, k) { c.classList.toggle('on', k === i) });
    $('#ck-h').textContent = 'Zeekr 8X ' + v.n + ' ' + b; $('#ck-p').textContent = fmt(v.b[b][0]) + ' ¥';
    $('#cn-p').textContent = 'Цена версии у дилера в Китае на дату расчёта. Для 8X ' + v.n + ' ' + b + ' кВт·ч – ' + fmt(v.b[b][0]) + ' ¥.';
    $('#st-t').textContent = 'Zeekr 8X ' + v.n + ' · в Китае ' + fmt(v.b[b][0]) + ' ¥';
    if (!fromForm) $$('#seg button').forEach(function (x) { x.classList.toggle('on', x.dataset.v === v.n) });
    $('#cv-v').textContent = 'Zeekr 8X ' + v.n + ' · ' + b + ' кВт·ч';
  }
  vb.addEventListener('click', function (e) {
    var card = e.target.closest('.v4'); if (!card) return; var i = +card.dataset.i, bt = e.target.closest('.bt button');
    if (bt && !bt.disabled) cardUpd(card, bt.dataset.b);
    pickVer(i, card.dataset.b);
  });

  /* ---------- сравнение комплектаций ---------- */
  var cmp = $('#cmp');
  $$('#cmp tbody:not(.extra) tr:not(.gh)').forEach(function (tr) {
    var tds = $$('td', tr).slice(1);
    tds.forEach(function (td) { var t = td.textContent.trim(); if (t === '✓') td.classList.add('yes'); if (t === '–') td.classList.add('no') });
    if (tds.length === 4) { var t0 = tds[0].textContent.trim(); if (tds.every(function (td) { return td.textContent.trim() === t0 })) tr.classList.add('same') }
    if (tds.length === 1 && tds[0].getAttribute('colspan')) tr.classList.add('same');
  });
  $('#only-diff').addEventListener('change', function (e) { cmp.classList.toggle('diff', e.target.checked) });
  $$('#cmp tbody[data-g]').forEach(function (tb, i) {
    if (i > 2 && mob()) tb.classList.add('cl');
    $('.gh button', tb).addEventListener('click', function () { tb.classList.toggle('cl') });
  });
  $('#all-open').addEventListener('click', function () { var any = $$('#cmp tbody.cl').length; $$('#cmp tbody[data-g]').forEach(function (tb) { tb.classList.toggle('cl', !any) }); this.textContent = any ? 'Свернуть все группы' : 'Раскрыть все группы' });

  /* ---------- конфигуратор: фрейм с того же домена, сборка уходит в форму ---------- */
  var cfg = $('#cfg'), frame = null, cfgVer = '68';
  function hook() {
    try {
      var w = frame.contentWindow, doc = frame.contentDocument; if (!doc || !doc.body) return;
      var fit = function () { frame.style.height = Math.max(640, doc.documentElement.scrollHeight) + 'px' };
      fit(); if (w.ResizeObserver) new w.ResizeObserver(fit).observe(doc.body);
      var take = function (det) { if (!det) return; S.build = det.text || ''; $('#build-t').textContent = (det.lines || []).map(function (l) { return l[1] }).join(' · ') || det.text; $('#cv-b').textContent = 'Сборка из конфигуратора приложена к заявке' };
      doc.addEventListener('zeekr:change', function (e) { take(e.detail) });
      if (w.ZeekrCfg) take(w.ZeekrCfg.get());
    } catch (e) { /* другой домен – фрейм работает сам по себе, без связи с формой */ }
  }
  function loadCfg(id) {
    cfgVer = id || cfgVer; $$('#cfg-seg button').forEach(function (b) { b.classList.toggle('on', b.dataset.v === cfgVer) });
    var url = cfg.dataset.src + '?v=' + cfgVer + '#v=' + cfgVer;
    if (!frame) { frame = d.createElement('iframe'); frame.title = 'Конфигуратор Zeekr 8X'; frame.loading = 'lazy'; frame.onload = function () { var w = $('.wait', cfg); if (w) w.remove(); hook() }; cfg.appendChild(frame) }
    frame.src = url;
  }
  var cio = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; cio.disconnect(); if (!frame) loadCfg() }, { rootMargin: '500px 0px' });
  cio.observe(cfg);
  $$('#cfg-seg button').forEach(function (b) { b.addEventListener('click', function () { loadCfg(b.dataset.v) }) });
  d.addEventListener('click', function (e) { var a = e.target.closest('[data-cfg]'); if (!a) return; loadCfg(a.dataset.cfg); cio.disconnect() });

  /* ---------- чек цены ---------- */
  var T = [['Цена в Китае', ''], ['Экспорт и логистика', 'Оформление экспорта и доставка Хоргос → СВХ в Минске. Сумма: [запросить].'],
    ['Таможня гибрида', 'Пошлина и сборы на гибрид на дату и курс. Сумма: [запросить].'], ['ЭПТС и учёт', 'Электронный паспорт и постановка на учёт в Минске. Сумма: [запросить].'],
    ['Наша работа', 'Подбор, выкуп, проверка, сопровождение до выдачи. Сумма: [запросить].']];
  var rows = $$('#check .r'), ci = 0, cT = 0, cVis = false, cUser = false;
  function row(n) {
    ci = (n + rows.length) % rows.length; rows.forEach(function (r, k) { r.classList.toggle('on', k === ci) });
    $('#cn-n').textContent = '0' + (ci + 1); $('#cn-h').textContent = T[ci][0];
    if (ci) $('#cn-p').innerHTML = T[ci][1].replace(/\[запросить[^\]]*\]/, '<span class="ask">$&</span>');
    else $('#cn-p').textContent = 'Цена версии у дилера в Китае на дату расчёта: ' + $('#ck-h').textContent + ' – ' + $('#ck-p').textContent + '.';
    if (!reduce) $('#cn-n').animate([{ opacity: 0, transform: 'translateY(24px)' }, { opacity: 1, transform: 'none' }], { duration: 700, easing: E });
    clearTimeout(cT); if (cVis && !cUser && !reduce) cT = setTimeout(function () { row(ci + 1) }, 3200);
  }
  rows.forEach(function (r, k) { r.addEventListener('click', function () { cUser = true; row(k) }); if (fine) r.addEventListener('mouseenter', function () { cUser = true; if (k !== ci) row(k) }) });
  seen($('#check'), function (v) { cVis = v; row(ci) });

  /* ---------- шаги и вопросы ---------- */
  var st = $$('#steps .st'), fill = $('#fill');
  var sio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) e.target.classList.add('on') }); var n = st.filter(function (s) { return s.classList.contains('on') }).length; fill.style.setProperty('--s', n ? (st[n - 1].offsetTop + 10) / $('#steps').offsetHeight : 0) }, { rootMargin: '0px 0px -40% 0px' });
  st.forEach(function (s) { sio.observe(s) });
  $$('#qa details').forEach(function (det) {
    var sum = $('summary', det), body = $('.a', det), busy = false;
    sum.addEventListener('click', function (e) {
      e.preventDefault(); if (busy) return; busy = true;
      if (reduce) { det.open = !det.open; busy = false; return }
      if (!det.open) { det.open = true; var h = body.scrollHeight; body.animate([{ height: 0, opacity: 0 }, { height: h + 'px', opacity: 1 }], { duration: 600, easing: E }).onfinish = function () { busy = false } }
      else { var h2 = body.scrollHeight; body.animate([{ height: h2 + 'px', opacity: 1 }, { height: 0, opacity: 0 }], { duration: 480, easing: E }).onfinish = function () { det.open = false; busy = false } }
    });
  });

  /* ---------- тест-драйв и лизинг ---------- */
  function chips(id, key, after) { $$('#' + id + ' button').forEach(function (b) { b.addEventListener('click', function () { $$('#' + id + ' button').forEach(function (x) { x.classList.toggle('on', x === b) }); S[key] = b.dataset[Object.keys(b.dataset)[0]]; if (after) after() }) }) }
  chips('td-m', 'tdModel'); chips('lz-a', 'lzA', lzUpd); chips('lz-t', 'lzT', lzUpd);
  function lzUpd() { $('#lz-s').textContent = 'аванс ' + S.lzA + ' %, ' + ({ 24: '2 года', 36: '3 года', 60: '5 лет' })[S.lzT] }

  /* ---------- форма ---------- */
  var fm = $('#fm'), tel = fm.tel;
  var GOAL = { raschet: 'Получить расчёт Zeekr 8X', test: 'Записаться на тест-драйв', lizing: 'Получить график лизинга' };
  function setGoal(g) { S.goal = g; $$('#goal button').forEach(function (b) { b.classList.toggle('on', b.dataset.g === g) }); $('.t', fm).textContent = GOAL[g] }
  $$('#goal button').forEach(function (b) { b.addEventListener('click', function () { setGoal(b.dataset.g) }) });
  d.addEventListener('click', function (e) { var a = e.target.closest('[data-goal]'); if (a) setGoal(a.dataset.goal) });
  $$('#seg button').forEach(function (b) { b.addEventListener('click', function () {
    $$('#seg button').forEach(function (x) { x.classList.toggle('on', x === b) });
    var i = -1; V.forEach(function (v, k) { if (v.n === b.dataset.v) i = k });
    if (i > -1) pickVer(i, cards[i].dataset.b, true); else { S.ver = ''; $('#cv-v').textContent = 'Zeekr 8X' }
  }) });
  function mask(v) { var x = v.replace(/\D/g, ''); if (x.indexOf('375') === 0) x = x.slice(3); x = x.slice(0, 9); var r = '+375'; if (x.length) r += ' (' + x.slice(0, 2); if (x.length >= 2) r += ')'; if (x.length > 2) r += ' ' + x.slice(2, 5); if (x.length > 5) r += '-' + x.slice(5, 7); if (x.length > 7) r += '-' + x.slice(7, 9); return r }
  tel.addEventListener('focus', function () { if (!tel.value) tel.value = '+375 (' });
  tel.addEventListener('blur', function () { if (tel.value.replace(/\D/g, '').length <= 3) tel.value = '' });
  tel.addEventListener('input', function () { tel.value = mask(tel.value); tel.closest('.fld').classList.remove('bad') });
  fm.agree.addEventListener('change', function () { fm.agree.closest('.ok').classList.remove('bad') });
  function bad(el) { el.classList.remove('bad'); void el.offsetWidth; el.classList.add('bad') }
  fm.addEventListener('submit', function (e) {
    e.preventDefault(); var ok = true;
    if (tel.value.replace(/\D/g, '').length < 12) { bad(tel.closest('.fld')); ok = false }
    if (!fm.agree.checked) { bad(fm.agree.closest('.ok')); ok = false }
    if (!ok || fm.classList.contains('busy')) return;
    if (fm.website.value) { fm.classList.add('sent'); return }
    var utm = []; new URLSearchParams(location.search).forEach(function (v, k) { if (k.indexOf('utm_') === 0 || k === 'yclid' || k === 'gclid') utm.push(k + '=' + v) });
    var parts = [({ raschet: 'Расчёт под ключ', test: 'Тест-драйв ' + S.tdModel, lizing: 'Лизинг: аванс ' + S.lzA + ' %, ' + S.lzT + ' мес' })[S.goal],
      S.ver ? 'Zeekr 8X ' + S.ver + ' ' + S.bat + ' кВт·ч' : 'версия не выбрана', S.color, S.build ? 'сборка: ' + S.build : '', fm.city.value, tel.value];
    fm.classList.add('busy'); $('.t', fm).textContent = 'Отправляем…';
    setTimeout(function () { fm.classList.remove('busy'); fm.classList.add('sent'); $('#done-v').textContent = 'В заявке: ' + parts.filter(Boolean).join(' · ') + ' · страница ' + location.pathname + (utm.length ? ' · ' + utm.join(', ') : '') + ' (в прототипе никуда не уходит)' }, 1200);
  });

  /* ---------- окно «Связаться» ---------- */
  function closeS() { $$('.sheet.open').forEach(function (s) { s.classList.remove('open'); s.setAttribute('aria-hidden', 'true') }); lock(false) }
  $$('[data-sheet]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); var s = $('#sh-' + b.dataset.sheet); closeS(); s.classList.add('open'); s.setAttribute('aria-hidden', 'false'); lock(true) }) });
  $$('.sheet [data-close]').forEach(function (b) { b.addEventListener('click', closeS) });
  $$('.sh-box').forEach(function (b) { var y0 = 0; b.addEventListener('touchstart', function (e) { y0 = e.touches[0].clientY }, { passive: true }); b.addEventListener('touchend', function (e) { if (e.changedTouches[0].clientY - y0 > 80) closeS() }) });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeS(); menu(false); seoOpen(false) } });
})();
