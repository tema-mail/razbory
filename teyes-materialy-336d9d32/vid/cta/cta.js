/* Призывы TEYES Sibir: метка источника при клике, конструктор запроса, «сейчас на связи», промокод, липкая полоса.
   Адрес ссылки остаётся чистым – метка дописывается в момент клика и снимается (правило скрытой метки). */
(function () {
  var COUNTER = 99532918; // Метрика TEYES Sibir: цель уходит только там, где счётчик стоит (в бою)
  var TG = /^https:\/\/t\.me\/[A-Za-z0-9_]+\/?$/;

  function pageName() {
    var h1 = document.querySelector('h1');
    return (h1 && h1.textContent.trim()) || document.title;
  }

  function channelOf(href) {
    if (href.indexOf('https://t.me/') === 0) return 'telegram';
    if (href.indexOf('https://max.ru/') === 0) return 'max';
    if (href.indexOf('tel:') === 0) return 'phone';
    if (href.indexOf('#popup:') === 0) return 'form';
    if (/yandex\.ru\/maps|2gis\.ru/.test(href)) return 'map';
    return 'link';
  }

  function remember(id, channel) {
    var data = { cta: id, channel: channel, page: location.pathname, at: Date.now() };
    try { localStorage.setItem('lead_cta', JSON.stringify(data)); } catch (e) { /* без памяти браузера метка уйдёт только в цель */ }
    try { if (typeof window.ym === 'function') window.ym(COUNTER, 'reachGoal', 'cta_click', data); } catch (e) { /* счётчика нет – это копия */ }
  }

  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[data-cta]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var id = a.getAttribute('data-cta');
    remember(id, channelOf(href));
    if (TG.test(href)) {
      var text = a.getAttribute('data-tg-text') || ('Здравствуйте! Пишу со страницы «' + pageName() + '».');
      a.setAttribute('href', href.replace(/\/$/, '') + '?text=' + encodeURIComponent(text + ' [' + id + ']'));
      setTimeout(function () { a.setAttribute('href', href); }, 1500);
    }
  }, true);

  // Конструктор запроса: собирает сообщение менеджеру из того, что отметил человек
  function builder(root) {
    var out = root.querySelector('[data-tcta-out]');
    var btn = root.querySelector('a[data-cta]');
    var model = root.getAttribute('data-model') || 'машина';
    function update() {
      var sel = root.querySelector('select');
      var gen = sel ? sel.value : '';
      var keep = [].map.call(root.querySelectorAll('input:checked'), function (i) { return i.value; });
      var msg = 'Здравствуйте! Подберите Teyes на ' + model + (gen ? ' (' + gen + ')' : '') + '.';
      msg += keep.length ? ' Важно сохранить: ' + keep.join(', ') + '.' : ' Что сохранить из штатного – подскажите.';
      msg += ' Фото панели пришлю.';
      if (out) out.textContent = msg;
      if (btn) btn.setAttribute('data-tg-text', msg);
    }
    root.addEventListener('change', update);
    update();
  }

  // Новосибирск: UTC+7, пн–пт 11:00–19:00
  function status(el) {
    var now = new Date();
    var nsk = new Date(now.getTime() + now.getTimezoneOffset() * 60000 + 7 * 3600000);
    var d = nsk.getDay(), h = nsk.getHours() + nsk.getMinutes() / 60;
    var work = d >= 1 && d <= 5;
    if (work && h >= 11 && h < 19) {
      el.textContent = 'Сейчас на связи, до 19:00 по Новосибирску';
      el.classList.add('is-open');
    } else {
      var next = (work && h < 11) ? 'сегодня с 11:00' : (d === 5 || d === 6 || d === 0) ? 'в понедельник с 11:00' : 'завтра с 11:00';
      el.textContent = 'Сейчас не работаем – ответим ' + next + ' по Новосибирску';
      el.classList.add('is-closed');
    }
  }

  function copy(btn) {
    btn.addEventListener('click', function () {
      var code = btn.getAttribute('data-copy');
      var done = function () { btn.textContent = 'Скопировано'; setTimeout(function () { btn.textContent = 'Скопировать'; }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, done); else done();
    });
  }

  function sticky(bar) {
    // Обёртка поста Тильды задаёт transform – внутри неё fixed едет вместе со статьёй, поэтому полосу выносим в body
    if (bar.parentElement !== document.body) document.body.appendChild(bar);
    document.body.classList.add('tcta-has-sticky');
    var stop = document.querySelectorAll('[data-tcta-hide-sticky]');
    var hidden = false;
    if ('IntersectionObserver' in window && stop.length) {
      var seen = new Set();
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) seen.add(e.target); else seen.delete(e.target); });
        hidden = seen.size > 0; tick();
      });
      stop.forEach(function (s) { io.observe(s); });
    }
    function tick() { bar.classList.toggle('is-visible', window.scrollY > 500 && !hidden); }
    window.addEventListener('scroll', tick, { passive: true });
    tick();
  }

  function init() {
    document.querySelectorAll('[data-tcta-builder]').forEach(builder);
    document.querySelectorAll('[data-tcta-status]').forEach(status);
    document.querySelectorAll('[data-copy]').forEach(copy);
    document.querySelectorAll('.tcta-sticky:not(.tcta-sticky--demo)').forEach(sticky);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
