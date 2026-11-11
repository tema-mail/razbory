/* Прототип v2 карточки Zeekr 9X: анимации и механики – из базы блоков (tema-mail.github.io/baza-blokov). Без библиотек. */
(function () {
  var d = document, root = d.documentElement;
  var $ = function (s, r) { return (r || d).querySelector(s) }, $$ = function (s, r) { return [].slice.call((r || d).querySelectorAll(s)) };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches, fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  var mob = function () { return innerWidth <= 760 };
  var EXPO = 'cubic-bezier(.16,1,.3,1)', BAZA = 'https://tema-mail.github.io/baza-blokov/';
  var store = { get: function (k) { try { return JSON.parse(localStorage.getItem(k)) } catch (e) { return null } }, set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)) } catch (e) {} } };
  function lock(on) { root.style.overflow = on ? 'hidden' : '' }
  function seen(el, fn, th) { var io = new IntersectionObserver(function (es) { es.forEach(function (e) { fn(e.isIntersecting) }) }, { threshold: th || .3 }); io.observe(el) }

  /* тема: вечером и при тёмной системе – тёмная, кнопка запоминает */
  var tb = $('#tema');
  function tIcon() { tb.textContent = root.getAttribute('data-theme') === 'dark' ? '☀' : '☾' }
  tb.addEventListener('click', function () { var n = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'; root.setAttribute('data-theme', n); try { localStorage.setItem('tema', n) } catch (e) {} tIcon() }); tIcon();

  /* панель прототипа: логика блоков, счётчик меток «запросить» */
  $$('[data-q]').forEach(function (s, i) {
    var l = $('.logic', s); if (!l) return;
    var b = s.dataset.baza;
    l.innerHTML = '<b>Блок ' + (i + 1) + '.</b> Вопрос клиента: «' + s.dataset.q + '»' + (b ? ' · блок из базы: <a href="' + BAZA + b + '" target="_blank" rel="noopener">' + b.replace(/^.*#/, '') + '</a>' : ' · свой блок проекта');
  });
  $('#n-ask').textContent = $$('.ask').length;
  $('#sw-logic').addEventListener('change', function (e) { d.body.classList.toggle('show-logic', e.target.checked) });

  /* появление при прокрутке: сдвиг 34 px + прозрачность, 1,1 с, соседи с шагом 80 мс */
  if (!reduce) {
    var items = $$('.rv');
    items.forEach(function (el) { el.style.opacity = 0; el.style.transform = 'translateY(34px)' });
    var io = new IntersectionObserver(function (es) {
      es.filter(function (e) { return e.isIntersecting }).forEach(function (e, i) {
        var el = e.target; io.unobserve(el);
        el.style.transition = 'opacity 1.1s ' + EXPO + ' ' + i * 80 + 'ms,transform 1.1s ' + EXPO + ' ' + i * 80 + 'ms';
        requestAnimationFrame(function () { el.style.opacity = ''; el.style.transform = '' });
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el) });
  }

  /* счётчики: досчитывают за 1,4 с, когда видны на 60 % */
  $$('[data-n]').forEach(function (el) {
    var n = +el.dataset.n; if (reduce) return; el.textContent = 0;
    var io = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; io.disconnect(); var t0 = performance.now();
      (function tick(t) { var k = Math.min(1, (t - t0) / 1400); k = 1 - Math.pow(1 - k, 4); el.textContent = Math.round(n * k); if (k < 1) requestAnimationFrame(tick) })(t0);
    }, { threshold: .6 });
    io.observe(el);
  });

  /* шапка: пилюли сливаются после 80 px, темнеют над тёмным блоком; липкая полоса и таб-бар – после первого экрана */
  var hdr = $('#hdr'), dark = $$('[data-tone="dark"]'), hero = $('#hero'), sticky = $('#sticky'), mnav = $('#mnav'), form = $('#raschet');
  function onScroll() {
    hdr.classList.toggle('one', scrollY > 80);
    var y = 40, on = false; dark.forEach(function (s) { var r = s.getBoundingClientRect(); if (r.top < y && r.bottom > y) on = true }); hdr.classList.toggle('dk', on);
    var past = hero.getBoundingClientRect().bottom < innerHeight * .35, fr = form.getBoundingClientRect(), atForm = fr.top < innerHeight && fr.bottom > 0;
    sticky.classList.toggle('on', past && !atForm); mnav.classList.toggle('on', past); d.body.classList.toggle('tb', past);
    var cur = ''; $$('.pill.menu a').forEach(function (a) { var t = $(a.getAttribute('href')); if (t && t.getBoundingClientRect().top < 140) cur = a }); $$('.pill.menu a').forEach(function (a) { a.classList.toggle('on', a === cur) });
  }
  addEventListener('scroll', onScroll, { passive: true }); addEventListener('resize', onScroll); onScroll();

  /* первый экран: строки заголовка снизу, подчёркивание прорисовывается; переключатель вариантов A / C */
  if (!reduce) $$('.h1 .ln>span').forEach(function (s, i) { s.animate([{ transform: 'translateY(110%)' }, { transform: 'none' }], { duration: 1100, delay: 200 + i * 90, easing: EXPO, fill: 'both' }) });
  setTimeout(function () { hero.classList.add('go') }, 100);
  $$('.vsw button').forEach(function (b) { b.addEventListener('click', function () {
    $$('.vsw button').forEach(function (x) { x.classList.toggle('on', x === b) });
    hero.classList.remove('v-a', 'v-c'); hero.classList.add(b.dataset.v); slide(0); hero.dataset.baza = b.dataset.v === 'v-c' ? 'pervyy-ekran.html#hero-foto-fon' : 'pervyy-ekran.html#hero-split';
    var l = $('.logic', hero); if (l) l.querySelector('a').href = BAZA + hero.dataset.baza, l.querySelector('a').textContent = hero.dataset.baza.replace(/^.*#/, '');
  }) });

  /* слайдер кадров: сам раз в 5 с, пока виден; точка, стрелка, свайп – останавливают */
  var fr = $$('#stage .fr'), dots = $$('#dots button'), cap = $('#stage .cap'), cnt = $('#stage .cnt b'), si = 0, sT = 0, sVis = false, sUser = false;
  function slide(n) {
    var nv = fr.filter(function (f) { return getComputedStyle(f).display !== 'none' }).length || fr.length;
    si = (n + nv) % nv; fr.forEach(function (f, k) { f.classList.toggle('on', k === si) }); dots.forEach(function (b, k) { b.classList.toggle('on', k === si) });
    cap.textContent = fr[si].dataset.cap; cnt.textContent = ('0' + (si + 1)).slice(-2);
    clearTimeout(sT); if (sVis && !sUser && !reduce) sT = setTimeout(function () { slide(si + 1) }, 5000);
  }
  function stopS() { sUser = true; clearTimeout(sT); $('#dots').classList.add('stop') }
  dots.forEach(function (b, k) { b.addEventListener('click', function () { stopS(); slide(k) }) });
  $('#stage .ar').addEventListener('click', function () { stopS(); slide(si + 1) });
  var x0 = 0; $('#stage').addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX }, { passive: true });
  $('#stage').addEventListener('touchend', function (e) { var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { stopS(); slide(si + (dx < 0 ? 1 : -1)) } });
  seen($('#stage'), function (v) { sVis = v; slide(si) });

  /* версии: вкладки сами листаются раз в 6 с с полоской, полосы сравнения вырастают */
  var V = [
    { n: '9X Max', p: '[запросить: под ключ Max, $]', bat: 55, km: 300, cny: 465900, pts: ['помощь водителю H7', 'второй ряд: [запросить]'] },
    { n: '9X Ultra', p: '[запросить: под ключ Ultra, $]', bat: 70, km: 380, cny: 485900, pts: ['помощь водителю H9', 'второй ряд: отдельные кресла с поворотом на 180°'] },
    { n: '9X Hyper', p: '[запросить: под ключ Hyper, $]', bat: 70, km: 380, cny: 559900, pts: ['помощь водителю H9', 'кресла с поворотом', 'отличия от Ultra: [запросить]'] }
  ];
  var vt = $$('.v-tab'), vi = 0, vT = 0, vVis = false, vUser = false;
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') }
  function ver(n) {
    vi = (n + V.length) % V.length; var v = V[vi];
    vt.forEach(function (b, k) { b.classList.toggle('on', k === vi) });
    $$('.v-tbl tr[data-r]').forEach(function (r) { r.querySelectorAll('td').forEach(function (c) { c.classList.toggle('hi', +r.dataset.r === vi) }) });
    $('#v-name').textContent = v.n; $('#v-price').textContent = v.p;
    $('#v-bat').textContent = v.bat + ' кВт·ч'; $('#v-km').textContent = v.km + ' км'; $('#v-cny').textContent = fmt(v.cny) + ' ¥';
    $('#c-bat').style.width = v.bat / 70 * 100 + '%'; $('#c-km').style.width = v.km / 380 * 100 + '%'; $('#c-cny').style.width = v.cny / 559900 * 100 + '%';
    $('#v-pts').innerHTML = v.pts.map(function (p) { return '<span class="chip">' + p.replace(/\[запросить[^\]]*\]/, '<span class="ask">$&</span>') + '</span>' }).join('');
    clearTimeout(vT); if (vVis && !vUser && !reduce) vT = setTimeout(function () { ver(vi + 1) }, 6000);
  }
  vt.forEach(function (b, k) { b.addEventListener('click', function () { vUser = true; $('#vtabs').classList.add('stop'); ver(k) }) });
  seen($('#vcard'), function (v) { vVis = v; ver(vi) });

  /* конфигуратор: фрейм грузится, когда блок рядом с экраном */
  var cfg = $('#cfg');
  var cio = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; cio.disconnect(); var f = d.createElement('iframe'); f.src = cfg.dataset.src; f.title = 'Конфигуратор Zeekr 9X'; f.loading = 'lazy'; f.onload = function () { var w = $('.wait', cfg); if (w) w.remove() }; cfg.appendChild(f) }, { rootMargin: '400px 0px' });
  cio.observe(cfg);

  /* из чего цена: строки по очереди раз в 3,2 с, наведение или нажатие выбирает */
  var C = [
    ['Цена в Китае', 'Цена версии у дилера в Китае на дату расчёта. Для 9X Max – 465 900 ¥.'],
    ['Экспорт и логистика', 'Оформление экспорта и доставка Хоргос → СВХ в Минске. Сумма: [запросить].'],
    ['Таможенные платежи гибрида', 'Пошлина и сборы на гибрид на дату и курс. Сумма: [запросить].'],
    ['ЭПТС и учёт', 'Электронный паспорт и постановка на учёт в Минске. Сумма: [запросить].'],
    ['Наша работа', 'Подбор, проверка, сопровождение сделки до выдачи. Сумма: [запросить].']
  ];
  var st = $$('#stack [data-i]'), ci = 0, cT = 0, cVis = false, cUser = false, cd = $('#cost-d');
  function cost(n) {
    ci = (n + C.length) % C.length; st.forEach(function (s, k) { s.classList.toggle('on', k === ci) });
    $('.n', cd).textContent = '0' + (ci + 1); $('h3', cd).textContent = C[ci][0];
    $('p', cd).innerHTML = C[ci][1].replace(/\[запросить[^\]]*\]/, '<span class="ask">$&</span>');
    if (!reduce) cd.animate([{ opacity: .3, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }], { duration: 500, easing: EXPO });
    clearTimeout(cT); if (cVis && !cUser && !reduce) cT = setTimeout(function () { cost(ci + 1) }, 3200);
  }
  st.forEach(function (s, k) { s.addEventListener('click', function () { cUser = true; cost(k) }); if (fine) s.addEventListener('mouseenter', function () { cUser = true; if (ci !== k) cost(k) }) });
  seen(cd, function (v) { cVis = v; cost(ci) });

  /* лоты: вкладки «новые / с пробегом», сердечко кладёт в сравнение (localStorage) */
  var L = [['new', 'новый'], ['used', 'с пробегом'], ['new', 'новый'], ['used', 'с пробегом'], ['new', 'новый'], ['used', 'с пробегом']];
  $('#loty-r').innerHTML = L.map(function (l, i) {
    return '<div class="lot" data-f="' + l[0] + '"><button class="heart glass" type="button" aria-pressed="false" aria-label="В сравнение" data-id="lot' + i + '"><svg width="18" height="18"><use href="#i-heart"/></svg></button>' +
      '<div class="ph" data-l="Фото лота с площадки Китая (из фида) · ' + l[1] + '"></div><dl><dt>Версия</dt><dd>из фида</dd><dt>Год</dt><dd>из фида</dd><dt>Пробег</dt><dd>' + (l[0] === 'new' ? '0 км' : 'из фида, км') + '</dd><dt>Цена</dt><dd>¥ и под ключ $</dd><dt>Обновлено</dt><dd>дата из фида</dd></dl>' +
      '<a class="btn wide" href="#raschet">Забронировать лот<b><svg width="16" height="16"><use href="#i-ar"/></svg></b></a></div>';
  }).join('');
  var favs = store.get('z9x-fav') || [], favEl = $('#fav');
  function favPaint() { $$('.heart').forEach(function (h) { h.setAttribute('aria-pressed', favs.indexOf(h.dataset.id) > -1) }); $('b', favEl).textContent = favs.length; favEl.classList.toggle('has', favs.length > 0) }
  $$('.heart').forEach(function (h) { h.addEventListener('click', function () {
    var k = favs.indexOf(h.dataset.id); if (k > -1) favs.splice(k, 1); else favs.push(h.dataset.id);
    store.set('z9x-fav', favs); h.classList.remove('pop'); void h.offsetWidth; if (k < 0) h.classList.add('pop'); favPaint();
  }) });
  favPaint();
  $$('#lot-tabs button').forEach(function (t) { t.addEventListener('click', function () {
    $$('#lot-tabs button').forEach(function (x) { x.classList.toggle('on', x === t) });
    var vis = []; $$('.lot').forEach(function (c) { var ok = t.dataset.f === 'all' || c.dataset.f === t.dataset.f; c.classList.toggle('hide', !ok); if (ok) vis.push(c) });
    $('#loty-r').scrollTo({ left: 0, behavior: 'smooth' });
    if (!reduce) vis.forEach(function (c, i) { c.animate([{ opacity: 0, transform: mob() ? 'none' : 'translateY(20px)' }, { opacity: 1, transform: 'none' }], { duration: 700, delay: i * 50, easing: EXPO, fill: 'backwards' }) });
    rib($('#loty-r'));
  }) });

  /* ленты: стрелки листают на 2 карточки (телефон – на 1), полоса прогресса, мышью можно тащить */
  function rib(r) { var p = $('#' + r.id.replace('-r', '-p')); if (!p) return; var vis = r.clientWidth / r.scrollWidth, max = r.scrollWidth - r.clientWidth, k = max > 0 ? r.scrollLeft / max : 1; p.style.width = Math.min(100, (vis + k * (1 - vis)) * 100) + '%' }
  $$('.rib').forEach(function (r) {
    if (r.id) { r.addEventListener('scroll', function () { rib(r) }, { passive: true }); addEventListener('resize', function () { rib(r) }); rib(r) }
    if (!fine) return; var dn = false, sx = 0, sl = 0, mv = 0;
    r.addEventListener('pointerdown', function (e) { if (e.target.closest('a,button')) return; dn = true; mv = 0; sx = e.clientX; sl = r.scrollLeft; r.style.scrollSnapType = 'none' });
    addEventListener('pointermove', function (e) { if (!dn) return; mv = Math.abs(e.clientX - sx); r.scrollLeft = sl - (e.clientX - sx) });
    addEventListener('pointerup', function () { if (dn) { dn = false; r.style.scrollSnapType = '' } });
    r.addEventListener('click', function (e) { if (mv > 6) { e.preventDefault(); e.stopPropagation(); mv = 0 } }, true);
  });
  $$('[data-rib]').forEach(function (b) { b.addEventListener('click', function () { var r = $('#' + b.dataset.rib), c = r.children[1] || r.children[0]; var w = (c.offsetLeft - r.children[0].offsetLeft) || r.clientWidth / 2; r.scrollBy({ left: +b.dataset.d * w * (mob() ? 1 : 2), behavior: 'smooth' }) }) });

  /* характеристики: «все характеристики» */
  $('#more-b').addEventListener('click', function () { var m = $('#spec-more'), o = m.classList.toggle('open'); this.textContent = o ? 'Свернуть ↑' : 'Все характеристики ↓' });

  /* вопросы: раскрытие с анимацией высоты (0,5 с открытие, 0,42 с закрытие) */
  $$('#qa details').forEach(function (det) {
    var sum = $('summary', det), body = $('.a', det), busy = false;
    sum.addEventListener('click', function (e) {
      e.preventDefault(); if (busy) return; busy = true;
      if (reduce) { det.open = !det.open; busy = false; return }
      if (!det.open) { det.open = true; var h = body.scrollHeight; body.animate([{ height: 0, opacity: 0 }, { height: h + 'px', opacity: 1 }], { duration: 500, easing: EXPO }).onfinish = function () { busy = false } }
      else { var h2 = body.scrollHeight; body.animate([{ height: h2 + 'px', opacity: 1 }, { height: 0, opacity: 0 }], { duration: 420, easing: EXPO }).onfinish = function () { det.open = false; busy = false } }
    });
  });

  /* форма: версия меняет кадр, маска +375, пустая галочка, ловушка, «принято» со следующим шагом (ничего не отправляется) */
  var fm = $('#fm'), tel = fm.tel, ver2 = 'Ещё не решил', IMG = { 'Ещё не решил': 'front34', '9X Max': 'side', '9X Ultra': 'rear34', '9X Hyper': 'salon' };
  $$('#seg button').forEach(function (b) { b.addEventListener('click', function () {
    $$('#seg button').forEach(function (x) { x.classList.toggle('on', x === b) }); ver2 = b.dataset.v;
    $('#calc-vb').textContent = ver2 === 'Ещё не решил' ? 'Версия не выбрана' : ver2;
    var im = $('#calc-img'); if (!reduce) im.animate([{ opacity: 0, transform: 'scale(1.06)' }, { opacity: 1, transform: 'none' }], { duration: 700, easing: EXPO }); im.src = 'img/' + IMG[ver2] + '.webp';
  }) });
  function mask(v) { var x = v.replace(/\D/g, ''); if (x.indexOf('375') === 0) x = x.slice(3); x = x.slice(0, 9); var r = '+375'; if (x.length) r += ' (' + x.slice(0, 2); if (x.length >= 2) r += ')'; if (x.length > 2) r += ' ' + x.slice(2, 5); if (x.length > 5) r += '-' + x.slice(5, 7); if (x.length > 7) r += '-' + x.slice(7, 9); return r }
  tel.addEventListener('focus', function () { if (!tel.value) tel.value = '+375 (' });
  tel.addEventListener('blur', function () { if (tel.value.replace(/\D/g, '').length <= 3) tel.value = '' });
  tel.addEventListener('input', function () { tel.value = mask(tel.value); tel.closest('.fld').classList.remove('bad') });
  fm.agree.addEventListener('change', function () { fm.agree.closest('.ok').classList.remove('bad') });
  fm.addEventListener('submit', function (e) {
    e.preventDefault(); var ok = true;
    if (tel.value.replace(/\D/g, '').length < 12) { var f1 = tel.closest('.fld'); f1.classList.remove('bad'); void f1.offsetWidth; f1.classList.add('bad'); ok = false }
    if (!fm.agree.checked) { var f2 = fm.agree.closest('.ok'); f2.classList.remove('bad'); void f2.offsetWidth; f2.classList.add('bad'); ok = false }
    if (!ok || fm.classList.contains('busy')) return;
    if (fm.website.value) { fm.classList.add('sent'); return }
    var utm = []; new URLSearchParams(location.search).forEach(function (v, k) { if (k.indexOf('utm_') === 0 || k === 'yclid') utm.push(k + '=' + v) });
    fm.classList.add('busy'); $('.t', fm).textContent = 'Отправляем…';
    setTimeout(function () {
      fm.classList.remove('busy'); fm.classList.add('sent');
      $('#done-v').textContent = 'В заявке: ' + ver2 + (fm.color.value ? ', ' + fm.color.value : '') + ', ' + fm.city.value + ', ' + tel.value + ' · страница ' + location.pathname + (utm.length ? ' · ' + utm.join(', ') : '') + ' (в прототипе никуда не уходит)';
    }, 1200);
  });

  /* нижние окна на телефоне */
  function closeS() { $$('.sheet.open').forEach(function (s) { s.classList.remove('open'); s.setAttribute('aria-hidden', 'true') }); lock(false) }
  $$('[data-sheet]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); var s = $('#sh-' + b.dataset.sheet); closeS(); s.classList.add('open'); s.setAttribute('aria-hidden', 'false'); lock(true) }) });
  $$('.sheet [data-close]').forEach(function (b) { b.addEventListener('click', closeS) });
  $$('.sh-box').forEach(function (b) { var y0 = 0; b.addEventListener('touchstart', function (e) { y0 = e.touches[0].clientY }, { passive: true }); b.addEventListener('touchend', function (e) { if (e.changedTouches[0].clientY - y0 > 80) closeS() }) });
  addEventListener('keydown', function (e) { if (e.key === 'Escape') closeS() });
})();
