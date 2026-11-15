/* Варианты ритма страницы на выбор владельцу (15.11.2026: «сплошняком один текст без перебоя, дай выходы»).
   Включается только параметром ?ritm=a|b|c, без него страница не меняется.
   a – зебра: блоки чередуют фон, ключевые (цена, сервис) – светлые;
   (вариант b «главы» снят владельцем 15.11.2026: «какая нахуй глава… полная ненужная хуйня»);
   c – удары: между текстовыми блоками – крупная цифра на зелёном фоне. */
(function () {
  var m = (location.search.match(/[?&]ritm=([ac])/) || [])[1]; if (!m) return;
  var d = document, $ = function (s) { return d.querySelector(s) };
  var LIGHT = '--acc-t:#2f6966;--acc-s:rgba(47,105,102,.12);--bg:#f4f4f2;--bg2:#ecebe8;--sf:#fff;--sf2:#f6f6f4;--line:#e3e2de;--line2:#d2d1cc;--tx:#141414;--tx2:#3a3a38;--tx3:#6d6c68';
  var css = '.sec{padding-bottom:72px}@media(max-width:760px){.sec{padding-bottom:48px}}';
  if (m === 'a') {
    css += '#test-drive,#sravnenie,#lizing,#riski,#voprosy,#pohozhie{background:var(--sf2)}' +
      '#cena,#servis{' + LIGHT + ';background:var(--bg);color:var(--tx)}' +
      '.sec{border-top:1px solid var(--line)}';
  }
  if (m === 'c') {
    var U = [['obzor', '660 кВт', 'и 3,7 с до сотни – 898 л.с. в семейном кроссовере'],
      ['sravnenie', 'до 1416 км', 'на одном баке и заряде по CLTC'],
      ['lizing', 'от 356 800 ¥', 'цена Max в Китае – дальше считаем под ключ в BYN'],
      ['vydachi', 'Машерова, 15/4', 'сервис для машин из Китая – в том же здании, что и салон']];
    css += '.udar{margin-top:96px;background:#2f6966;color:#fff;padding:36px 0}' +
      '.udar strong{display:block;font:700 clamp(40px,10vw,72px)/1 var(--fd);letter-spacing:-.02em}' +
      '.udar span{display:block;margin-top:10px;font-size:17px;color:#e6f2f1;max-width:520px}' +
      '@media(max-width:760px){.udar{margin-top:56px;padding:28px 0}.udar + .sec{padding-top:48px}}';
    U.forEach(function (u) {
      var s = d.getElementById(u[0]); if (!s) return;
      var el = d.createElement('div'); el.className = 'udar';
      el.innerHTML = '<div class="w-wrap"><strong>' + u[1] + '</strong><span>' + u[2] + '</span></div>';
      s.after(el);
    });
  }
  var st = d.createElement('style'); st.textContent = css; d.head.appendChild(st);
})();
