/* Прототип v3 карточки Zeekr 9X: витрина с выбором цвета, шоурум с проездом, чек, лента, форма. Без библиотек. */
(function () {
  var d = document, root = d.documentElement;
  var $ = function (s, r) { return (r || d).querySelector(s) }, $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)) };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  var mob = function () { return innerWidth <= 760 }, BAZA = 'https://tema-mail.github.io/baza-blokov/', E = 'cubic-bezier(.32,.72,0,1)';
  var store = { get: function (k) { try { return JSON.parse(localStorage.getItem(k)) } catch (e) { return null } }, set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)) } catch (e) {} } };
  function lock(on) { root.style.overflow = on ? 'hidden' : '' }
  function seen(el, fn, th) { new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting, e) }) }, { threshold: th || .3 }).observe(el) }

  /* тема: тёмная по умолчанию (это витрина), кнопка переключает и запоминает */
  var tb = $('#tema');
  function tIcon() { tb.textContent = root.getAttribute('data-theme') === 'dark' ? '☀' : '☾' }
  tb.addEventListener('click', function () { var n = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', n); try { localStorage.setItem('tema-z9x3', n) } catch (e) {} tIcon() }); tIcon();

  /* логика блоков и счётчик меток */
  $$('[data-q]').forEach(function (s, i) {
    var l = $('.logic', s); if (!l) return; var b = s.dataset.baza;
    l.innerHTML = '<b>Блок ' + (i + 1) + '.</b> Вопрос клиента: «' + s.dataset.q + '»' + (b ? ' · из базы: <a href="' + BAZA + b + '" target="_blank" rel="noopener">' + b.replace(/^.*#/, '') + '</a>' : ' · свой блок проекта');
  });
  $('#n-ask').textContent = $$('.ask').length;
  $('#sw-logic').addEventListener('change', function (e) { d.body.classList.toggle('show-logic', e.target.checked) });

  /* появление: тяжёлый подъём с размытием, соседи с шагом 90 мс */
  if (!reduce) {
    var io = new IntersectionObserver(function (es) {
      es.filter(function (e) { return e.isIntersecting }).forEach(function (e, i) { io.unobserve(e.target); e.target.style.transitionDelay = i * 90 + 'ms'; e.target.classList.add('in') });
    }, { rootMargin: '0px 0px -10% 0px' });
    $$('.rv').forEach(function (el) { io.observe(el) });
  } else $$('.rv').forEach(function (el) { el.classList.add('in') });

  /* счётчики первого экрана */
  $$('[data-n]').forEach(function (el, i) {
    var n = +el.dataset.n; if (reduce) return; el.textContent = 0;
    setTimeout(function () { var t0 = performance.now(); (function tick(t) { var k = Math.min(1, (t - t0) / 1600); k = 1 - Math.pow(1 - k, 4); el.textContent = Math.round(n * k); if (k < 1) requestAnimationFrame(tick) })(t0) }, 900 + i * 120);
  });

  /* витрина: цвет кузова меняет машину, отражение и свечение; выбор запоминается и уходит в форму */
  var C = [
    ['002', 'Чёрный «Полярная ночь»', '#3b5bff'], ['003', 'Белый «Полярный день»', '#8fb0ff'], ['004', 'Серебристый «Ледник»', '#9fb3cc'],
    ['005', 'Серый «Звёздный свод»', '#6b84a8'], ['045', 'Коричневый «Исследователь»', '#c48a52'], ['006', 'Фиолетовый «Тёмная ночь»', '#7a5cff']
  ];
  var car = $('#car'), refl = $('.refl', car), dots = $('#sw .dots'), cur = '002';
  dots.innerHTML = C.map(function (c, i) { return '<button type="button" role="radio" aria-label="' + c[1] + '" data-c="' + c[0] + '" style="background-image:url(img/s-' + c[0] + '.webp)"' + (i ? '' : ' class="on" aria-checked="true"') + '></button>' }).join('');
  C.forEach(function (c) { if (c[0] !== '002') { var im = new Image(); im.src = 'img/c-' + c[0] + '.webp' } });
  function paint(code, first) {
    var c = C.filter(function (x) { return x[0] === code })[0]; if (!c) return; cur = code;
    root.style.setProperty('--glow', c[2]);
    $$('button', dots).forEach(function (b) { var on = b.dataset.c === code; b.classList.toggle('on', on); b.setAttribute('aria-checked', on) });
    $('#cn').textContent = c[1];
    [car, refl].forEach(function (box) {
      var old = $('img.on', box); if (old && old.dataset.c === code) return;
      var im = new Image(); im.src = 'img/c-' + code + '.webp'; im.alt = box === car ? 'Zeekr 9X, цвет ' + c[1] : ''; im.dataset.c = code; im.width = 1600; im.height = 725;
      box.appendChild(im); requestAnimationFrame(function () { requestAnimationFrame(function () { im.classList.add('on'); if (old) { old.classList.remove('on'); setTimeout(function () { old.remove() }, 1400) } }) });
    });
    $('#cv-img').src = 'img/c-' + code + '.webp'; $('#cv-c').textContent = c[1] + ' – цвет из первого экрана';
    if (!first) store.set('z9x-color', code);
  }
  dots.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) paint(b.dataset.c) });
  var saved = store.get('z9x-color'); if (saved && saved !== '002') paint(saved, true);
  /* глубина: «9X» и машина слегка расходятся за курсором (только мышь) */
  if (fine && !reduce) {
    var big = $('#big9'), sc = $('#scene');
    sc.addEventListener('mousemove', function (e) { var r = sc.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      big.style.transform = 'translate(calc(-50% + ' + (-x * 30) + 'px),calc(-50% + ' + (-y * 16) + 'px))'; car.style.transform = 'translateX(calc(-50% + ' + (x * 14) + 'px))' });
    big.style.transition = car.style.transition = 'transform 1.2s ' + E;
  }
  if (!reduce) { $('#h1').animate([{ opacity: 0, transform: 'translateY(40px)', filter: 'blur(10px)' }, { opacity: 1, transform: 'none', filter: 'none' }], { duration: 1300, easing: E, fill: 'both', delay: 150 });
    car.animate([{ opacity: 0, transform: 'translateX(-38%) scale(.97)' }, { opacity: 1, transform: 'translateX(-50%)' }], { duration: 1800, easing: 'cubic-bezier(.16,1,.3,1)', delay: 300, fill: 'backwards' }) }

  /* шоурум: машина проезжает при прокрутке, цифры загораются по очереди */
  var show = $('#show'), road = $('#road'), specs = $$('#specs > div'), tick = false;
  function showUpd() {
    tick = false; var r = show.getBoundingClientRect(), total = show.offsetHeight - innerHeight, p = Math.min(1, Math.max(0, -r.top / total));
    var w = road.offsetWidth, vw = innerWidth, k = Math.min(1, p / .55), ease = 1 - Math.pow(1 - k, 3);
    var start = vw + 40, end = (vw - w) / 2, x = start + (end - start) * ease - Math.max(0, p - .7) / .3 * (vw * .25);
    road.style.setProperty('--x', x.toFixed(1));
    specs.forEach(function (s, i) { s.classList.toggle('on', p > .15 + i * .18) });
  }
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(showUpd) } }, { passive: true }); addEventListener('resize', showUpd); showUpd();

  /* навигация: подсветка раздела, полоса прототипа уходит, мобильное меню */
  var nav = $('#nav'), hero = $('#hero'), sticky = $('#sticky'), mnav = $('#mnav'), form = $('#raschet');
  function pb() { root.style.setProperty('--pb', $('.pbar').offsetHeight + 'px') } pb(); addEventListener('resize', pb);
  function onScroll() {
    d.body.classList.toggle('pbar-on', scrollY < 30);
    var past = hero.getBoundingClientRect().bottom < innerHeight * .3, fr = form.getBoundingClientRect(), atForm = fr.top < innerHeight && fr.bottom > 0;
    sticky.classList.toggle('on', past && !atForm); mnav.classList.toggle('on', past); d.body.classList.toggle('tb', past);
    var on = null; $$('.ln a', nav).forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 160) on = a }); $$('.ln a', nav).forEach(function (a) { a.classList.toggle('on', a === on) });
  }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var mm = $('#mm');
  function menu(o) { d.body.classList.toggle('menu-open', o); mm.setAttribute('aria-hidden', !o); lock(o); $$('a', mm).forEach(function (a, i) { a.style.transitionDelay = o ? 100 + i * 50 + 'ms' : '0ms' }) }
  $('#bur').addEventListener('click', function () { menu(!d.body.classList.contains('menu-open')) });
  $$('a', mm).forEach(function (a) { a.addEventListener('click', function () { menu(false) }) });

  /* версии: выбор карточки, полосы вырастают при появлении */
  var vers = $$('.ver');
  seen($('#vers'), function (v) { if (v) $('#vers').classList.add('in') }, .25);
  vers.forEach(function (c) { c.addEventListener('click', function () { vers.forEach(function (x) { x.classList.toggle('on', x === c) }); var b = $$('#seg button')[+c.dataset.v + 1]; if (b) b.click() }) });

  /* конфигуратор: фрейм грузится заранее, за 500 px до блока */
  var cfg = $('#cfg');
  var cio = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; cio.disconnect(); var f = d.createElement('iframe'); f.src = cfg.dataset.src; f.title = 'Конфигуратор Zeekr 9X'; f.onload = function () { var w = $('.wait', cfg); if (w) w.remove() }; cfg.appendChild(f) }, { rootMargin: '500px 0px' });
  cio.observe(cfg);

  /* чек: строки подсвечиваются по очереди раз в 3,2 с, пока чек на экране; нажатие или наведение – выбор */
  var T = [['Цена в Китае', 'Цена версии у дилера в Китае на дату расчёта. Для 9X Max – 465 900 ¥.'], ['Экспорт и логистика', 'Оформление экспорта и доставка Хоргос → СВХ в Минске. Сумма: [запросить].'],
    ['Таможня гибрида', 'Пошлина и сборы на гибрид на дату и курс. Сумма: [запросить].'], ['ЭПТС и учёт', 'Электронный паспорт и постановка на учёт в Минске. Сумма: [запросить].'],
    ['Наша работа', 'Подбор, проверка, сопровождение сделки до выдачи. Сумма: [запросить].']];
  var rows = $$('#check .r'), ci = 0, cT = 0, cVis = false, cUser = false;
  function row(n) {
    ci = (n + rows.length) % rows.length; rows.forEach(function (r, k) { r.classList.toggle('on', k === ci) });
    $('#cn-n').textContent = '0' + (ci + 1); $('#cn-h').textContent = T[ci][0]; $('#cn-p').innerHTML = T[ci][1].replace(/\[запросить[^\]]*\]/, '<span class="ask">$&</span>');
    if (!reduce) $('#cn-n').animate([{ opacity: 0, transform: 'translateY(24px)' }, { opacity: 1, transform: 'none' }], { duration: 700, easing: E });
    clearTimeout(cT); if (cVis && !cUser && !reduce) cT = setTimeout(function () { row(ci + 1) }, 3200);
  }
  rows.forEach(function (r, k) { r.addEventListener('click', function () { cUser = true; row(k) }); if (fine) r.addEventListener('mouseenter', function () { cUser = true; if (k !== ci) row(k) }) });
  seen($('#check'), function (v) { cVis = v; row(ci) });

  /* лоты: рендеры разных цветов вместо фото из фида, вкладки, сердечко в сравнение */
  var L = [['new', '003', 'новый'], ['used', '002', 'с пробегом'], ['new', '004', 'новый'], ['used', '045', 'с пробегом'], ['new', '006', 'новый'], ['used', '005', 'с пробегом']];
  $('#loty-r').innerHTML = L.map(function (l, i) {
    return '<div class="bz lot" data-f="' + l[0] + '"><div class="core"><button class="heart" type="button" aria-pressed="false" aria-label="В сравнение" data-id="lot' + i + '"><svg width="18" height="18"><use href="#heart"/></svg></button>' +
      '<div class="vis"><img src="img/c-' + l[1] + '.webp" alt="Zeekr 9X, лот ' + (i + 1) + '" width="1600" height="725" loading="lazy"><small>фото лота – из фида · ' + l[2] + '</small></div>' +
      '<dl><dt>Версия</dt><dd>из фида</dd><dt>Год</dt><dd>из фида</dd><dt>Пробег</dt><dd>' + (l[0] === 'new' ? '0 км' : 'из фида') + '</dd><dt>Цена</dt><dd>¥ и под ключ $</dd><dt>Обновлено</dt><dd>дата из фида</dd></dl>' +
      '<a class="btn acc wide" href="#raschet">Забронировать<b><svg width="16" height="16"><use href="#ar"/></svg></b></a></div></div>';
  }).join('');
  var favs = store.get('z9x-fav') || [], favEl = $('#fav');
  function favPaint() { $$('.heart').forEach(function (h) { h.setAttribute('aria-pressed', favs.indexOf(h.dataset.id) > -1) }); $('b', favEl).textContent = favs.length; favEl.classList.toggle('has', favs.length > 0) }
  $$('.heart').forEach(function (h) { h.addEventListener('click', function () { var k = favs.indexOf(h.dataset.id); if (k > -1) favs.splice(k, 1); else favs.push(h.dataset.id); store.set('z9x-fav', favs); h.classList.remove('pop'); void h.offsetWidth; if (k < 0) h.classList.add('pop'); favPaint() }) });
  favPaint();
  $$('#lot-tabs button').forEach(function (t) { t.addEventListener('click', function () {
    $$('#lot-tabs button').forEach(function (x) { x.classList.toggle('on', x === t) });
    var vis = []; $$('.lot').forEach(function (c) { var ok = t.dataset.f === 'all' || c.dataset.f === t.dataset.f; c.classList.toggle('hide', !ok); if (ok) vis.push(c) });
    $('#loty-r').scrollTo({ left: 0, behavior: 'smooth' });
    if (!reduce) vis.forEach(function (c, i) { c.animate([{ opacity: 0, transform: mob() ? 'none' : 'translateY(24px)' }, { opacity: 1, transform: 'none' }], { duration: 800, delay: i * 60, easing: E, fill: 'backwards' }) });
    prog($('#loty-r'));
  }) });
  function prog(r) { var p = $('#loty-p'); if (!p) return; var vis = r.clientWidth / r.scrollWidth, max = r.scrollWidth - r.clientWidth, k = max > 0 ? r.scrollLeft / max : 1; p.style.width = Math.min(100, (vis + k * (1 - vis)) * 100) + '%' }
  var lr = $('#loty-r'); lr.addEventListener('scroll', function () { prog(lr) }, { passive: true }); addEventListener('resize', function () { prog(lr) }); prog(lr);
  $$('[data-rib]').forEach(function (b) { b.addEventListener('click', function () { var r = $('#' + b.dataset.rib), ch = r.children, w = ch.length > 1 ? ch[1].offsetLeft - ch[0].offsetLeft : r.clientWidth; r.scrollBy({ left: +b.dataset.d * w * (mob() ? 1 : 2), behavior: 'smooth' }) }) });
  if (fine) $$('.rib').forEach(function (r) { var dn = false, sx = 0, sl = 0, mv = 0;
    r.addEventListener('pointerdown', function (e) { if (e.target.closest('a,button')) return; dn = true; mv = 0; sx = e.clientX; sl = r.scrollLeft; r.style.scrollSnapType = 'none' });
    addEventListener('pointermove', function (e) { if (!dn) return; mv = Math.abs(e.clientX - sx); r.scrollLeft = sl - (e.clientX - sx) });
    addEventListener('pointerup', function () { if (dn) { dn = false; r.style.scrollSnapType = '' } });
    r.addEventListener('click', function (e) { if (mv > 6) { e.preventDefault(); e.stopPropagation(); mv = 0 } }, true) });

  /* шаги: линия заполняется до последнего видимого шага */
  var st = $$('#steps .st'), fill = $('#fill');
  var sio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) e.target.classList.add('on') }); var n = st.filter(function (s) { return s.classList.contains('on') }).length; fill.style.setProperty('--s', n ? (st[n - 1].offsetTop + 10) / $('#steps').offsetHeight : 0) }, { rootMargin: '0px 0px -40% 0px' });
  st.forEach(function (s) { sio.observe(s) });

  /* вопросы: раскрытие с анимацией высоты */
  $$('#qa details').forEach(function (det) {
    var sum = $('summary', det), body = $('.a', det), busy = false;
    sum.addEventListener('click', function (e) {
      e.preventDefault(); if (busy) return; busy = true;
      if (reduce) { det.open = !det.open; busy = false; return }
      if (!det.open) { det.open = true; var h = body.scrollHeight; body.animate([{ height: 0, opacity: 0 }, { height: h + 'px', opacity: 1 }], { duration: 600, easing: E }).onfinish = function () { busy = false } }
      else { var h2 = body.scrollHeight; body.animate([{ height: h2 + 'px', opacity: 1 }, { height: 0, opacity: 0 }], { duration: 480, easing: E }).onfinish = function () { det.open = false; busy = false } }
    });
  });

  /* форма: версия, цвет из витрины, маска +375, пустая галочка, ловушка; ничего не отправляется */
  var fm = $('#fm'), tel = fm.tel, ver = 'Ещё не решил';
  $$('#seg button').forEach(function (b) { b.addEventListener('click', function () { $$('#seg button').forEach(function (x) { x.classList.toggle('on', x === b) }); ver = b.dataset.v; $('#cv-v').textContent = ver === 'Ещё не решил' ? 'Zeekr 9X' : 'Zeekr ' + ver }) });
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
    var cn = C.filter(function (x) { return x[0] === cur })[0][1], utm = [];
    new URLSearchParams(location.search).forEach(function (v, k) { if (k.indexOf('utm_') === 0 || k === 'yclid') utm.push(k + '=' + v) });
    fm.classList.add('busy'); $('.t', fm).textContent = 'Отправляем…';
    setTimeout(function () { fm.classList.remove('busy'); fm.classList.add('sent'); $('#done-v').textContent = 'В заявке: ' + ver + ', ' + cn + ', ' + fm.city.value + ', ' + tel.value + ' · страница ' + location.pathname + (utm.length ? ' · ' + utm.join(', ') : '') + ' (в прототипе никуда не уходит)' }, 1200);
  });

  /* окно «Связаться» на телефоне */
  function closeS() { $$('.sheet.open').forEach(function (s) { s.classList.remove('open'); s.setAttribute('aria-hidden', 'true') }); lock(false) }
  $$('[data-sheet]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); var s = $('#sh-' + b.dataset.sheet); closeS(); s.classList.add('open'); s.setAttribute('aria-hidden', 'false'); lock(true) }) });
  $$('.sheet [data-close]').forEach(function (b) { b.addEventListener('click', closeS) });
  $$('.sh-box').forEach(function (b) { var y0 = 0; b.addEventListener('touchstart', function (e) { y0 = e.touches[0].clientY }, { passive: true }); b.addEventListener('touchend', function (e) { if (e.changedTouches[0].clientY - y0 > 80) closeS() }) });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') { closeS(); menu(false) } });
})();
