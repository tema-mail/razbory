# Автопилот завода: выбери, как он ведёт сайт

Автопилот сам снимает спрос, пишет статью и выкладывает её на сайт без твоего «да». Кнопка включается, только когда у клиента заполнено всё нужное. Нужны 4 ответа буквами, например «1Б, 2А, 3А, 4В». Мой совет – в синей рамке. Первый шаг (проверка готовности клиента) делаю уже сейчас: он от ответов не зависит.

<style>
.kv{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:14px 0 30px}
@media(max-width:900px){.kv{grid-template-columns:minmax(0,1fr)}}
.v{min-width:0;border:1px solid var(--ln);border-radius:14px;background:var(--card);padding:12px}
.v.rec{border-color:var(--ac);box-shadow:0 0 0 2px var(--ac)}
.v h4{margin:0 0 10px;font-size:17px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.v h4 b{display:inline-flex;width:30px;height:30px;border-radius:9px;background:var(--ac);color:#fff;align-items:center;justify-content:center;flex:none}
.v h4 em{flex-basis:100%;order:-1;font-style:normal;font-size:12px;font-weight:700;color:var(--ac);text-transform:uppercase;letter-spacing:.04em}
.v>p{font-size:14px;margin:10px 0 0;color:var(--mut)}.v>p b{color:var(--tx)}
.m{background:#0b0e11;color:#e6efe9;border-radius:12px;padding:12px;font:500 13px/1.4 Inter,system-ui,sans-serif;min-height:170px;position:relative;overflow:hidden}
.m small{color:#8fa39a;font-size:11.5px}
.ok{color:#39ff88}.wa{color:#ffc24b}.bad{color:#ff5c6c}.mu{color:#8fa39a}
.bx{background:#141a20;border:1px solid #232c34;border-radius:10px;padding:9px 11px;margin:6px 0}
.btn{display:inline-block;padding:5px 10px;border-radius:8px;font-weight:700;font-size:12.5px;background:#3e7bff;color:#fff}
.btn.r{background:#ff5c6c}.btn.g{background:#39ff88;color:#04140b}.btn.n{background:#232c34;color:#8fa39a}
.lane{display:flex;justify-content:space-between;gap:4px;margin:10px 0 4px;position:relative}
.lane i{font-style:normal;flex:1;text-align:center;font-size:11px;padding:6px 2px;border-radius:7px;background:#141a20;border:1px solid #232c34}
.run{position:absolute;top:-6px;width:12px;height:12px;border-radius:50%;background:#39ff88;box-shadow:0 0 10px #39ff88;animation:run 4s linear infinite}
@keyframes run{0%{left:2%}100%{left:94%}}
.cd{height:7px;border-radius:4px;background:#232c34;overflow:hidden;margin:8px 0}.cd u{display:block;height:100%;background:#ffc24b;animation:cd 6s linear infinite}
@keyframes cd{0%{width:100%}100%{width:0}}
.blink{animation:bl 1.6s ease-in-out infinite}@keyframes bl{50%{opacity:.35}}
.sw{display:inline-block;width:42px;height:22px;border-radius:11px;background:#232c34;position:relative;vertical-align:middle;animation:swb 3s steps(1) infinite}
.sw::after{content:"";position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:#fff;animation:swk 3s ease-in-out infinite}
@keyframes swb{0%{background:#232c34}50%{background:#39ff88}}
@keyframes swk{0%,40%{left:3px}50%,100%{left:23px}}
.dots{display:flex;gap:5px;margin:8px 0}.dots u{width:22px;height:22px;border-radius:6px;background:#232c34;display:block}
.dots u.f{background:#39ff88}.dots u.p{background:#3e7bff;animation:bl 1.4s infinite}
.chips{display:flex;flex-wrap:wrap;gap:5px;margin-top:6px}.chips i{font-style:normal;font-size:11.5px;font-weight:700;padding:3px 7px;border-radius:6px}
.chips .on{background:#39ff88;color:#04140b}.chips .off{background:#151b20;color:#55635c;border:1px solid #232c34}.chips .wb{background:#ffc24b;color:#1d1400}
.big{font-size:26px;font-weight:800;margin:6px 0}
.bar{height:9px;border-radius:5px;background:#232c34;overflow:hidden;margin:6px 0}.bar u{display:block;height:100%;animation:fill 5s ease-in-out infinite}
@keyframes fill{0%{width:5%}80%,100%{width:var(--w)}}
.chain{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:10px 0}.chain i{font-style:normal;padding:7px 10px;border-radius:9px;background:#141a20;border:1px solid #232c34;font-size:12.5px}
.chain i.on{border-color:#39ff88;animation:glow 5s infinite}.chain b{color:#8fa39a}
.chain i:nth-of-type(2){animation-delay:1s}.chain i:nth-of-type(3){animation-delay:2s}.chain i:nth-of-type(4){animation-delay:3s}.chain i:nth-of-type(5){animation-delay:4s}
@keyframes glow{0%,15%{box-shadow:0 0 0 2px #39ff88;color:#39ff88}25%,100%{box-shadow:none;color:#e6efe9}}
</style>

## Как он будет работать

<div class="m" style="min-height:0">
<div class="chain"><i class="on">Спрос раз в квартал</i><b>→</b><i class="on">Карта тем</i><b>→</b><i class="on">Статья под свободный день</i><b>→</b><i class="on">Проверки: красный список, факты, «не как ИИ»</i><b>→</b><i class="on">Выкладка в день из календаря</i></div>
<small>Сам ставит себе паузу и пишет тебе в Telegram, если: деньги за месяц дошли до потолка; выкладка упала два раза подряд; проверки вернули одну статью второй раз; после его выкладки на сайте стало хуже по технике.</small>
</div>

Кнопка «Автопилот» загорается, когда у клиента есть всё: знакомство пройдено и факты утверждены, паспорт спроса, красный список, настроена выкладка на сайт, есть нейросеть, задан потолок денег, в карте есть темы. Не хватает – видно списком, чего.

## 1. Как «без да»

<div class="kv">
<div class="v"><h4><b>А</b>Сразу сам</h4>
<div class="m"><small>Статья «Замена масла Zeekr 001»</small>
<div class="lane"><span class="run"></span><i>написал</i><i>проверки</i><i>выложил</i></div>
<div class="bx"><span class="ok">✓ Вышла 10:00</span> <small>– ты узнаёшь из дайджеста утром</small></div></div>
<p><b>Совсем без тебя.</b> Ошибку увидишь уже на сайте. +0 ч.</p></div>
<div class="v rec"><h4><em>Мой совет</em><b>Б</b>Тихое окно 24 часа</h4>
<div class="m"><small>Календарь · завтра</small>
<div class="bx"><b>Замена масла Zeekr 001</b><br><span class="wa blink">Выйдет завтра в 10:00, если не остановишь</span><div class="cd"><u></u></div><span class="btn r">Стоп</span> <span class="btn n">Открыть</span></div>
<small>Молчишь – выходит сама.</small></div>
<p><b>Твоё «да» не нужно, но успеваешь глянуть и нажать «Стоп».</b> +2 ч.</p></div>
<div class="v"><h4><b>В</b>Первые 5 – с «да», потом сам</h4>
<div class="m"><small>Проверка новичка</small>
<div class="dots"><u class="f"></u><u class="f"></u><u class="f"></u><u class="p"></u><u></u></div>
<div class="bx">3 из 5 статей прошли с твоим «да».<br><span class="ok">После 5-й автопилот идёт сам.</span></div></div>
<p><b>Сначала доверяешь, потом отпускаешь.</b> Первые недели «да» нужно. +1 ч.</p></div>
</div>

## 2. Кто нажимает кнопку

<div class="kv">
<div class="v rec"><h4><em>Мой совет</em><b>А</b>Только ты</h4>
<div class="m"><small>Твой пульт · EV Sibir</small>
<div class="bx">Автопилот <span class="sw"></span></div>
<small>Кабинет клиента:</small><div class="bx"><span class="ok">● Автопилот ведёт сайт</span></div></div>
<p><b>Включаешь ты, клиент видит, что завод ведёт сайт сам.</b> +0 ч.</p></div>
<div class="v"><h4><b>Б</b>Клиент тоже</h4>
<div class="m"><small>Кабинет клиента · Баланс</small>
<div class="bx">Автопилот <span class="sw"></span><br><small class="wa">не хватает: потолок денег, красный список</small></div></div>
<p><b>Клиент сам заполняет недостающее и включает.</b> Ты узнаёшь из дайджеста. +2 ч.</p></div>
<div class="v"><h4><b>В</b>Клиент просит, ты подтверждаешь</h4>
<div class="m"><small>Твой пульт · Ждёт решения</small>
<div class="bx"><span class="blink">TEYES Sibir просит включить автопилот</span><br><span class="btn g">Да</span> <span class="btn n">Нет</span></div></div>
<p><b>Инициатива у клиента, последнее слово у тебя.</b> +3 ч.</p></div>
</div>

## 3. Что ведёт в первом заходе

<div class="kv">
<div class="v rec"><h4><em>Мой совет</em><b>А</b>Только сайт</h4>
<div class="m"><small>Автопилот ведёт:</small>
<div class="chips"><i class="on">Сайт</i><i class="off">ВК</i><i class="off">Telegram</i><i class="off">Дзен</i><i class="off">Яндекс Карты</i><i class="off">Google Карты</i></div>
<div class="bx">Статьи на сайт – по графику вт и пт</div></div>
<p><b>Самое ценное для поиска и без браузера.</b> ~29 ч всего.</p></div>
<div class="v"><h4><b>Б</b>Сайт + площадки с ключом</h4>
<div class="m"><small>Автопилот ведёт:</small>
<div class="chips"><i class="on">Сайт</i><i class="on">ВК</i><i class="on">Telegram</i><i class="off">Дзен</i><i class="off">Яндекс Карты</i><i class="off">Google Карты</i></div>
<div class="bx"><span class="wa">ВК: нужен ключ сообщества от тебя</span></div></div>
<p><b>Посты ВК и Telegram выходят сами.</b> +12 ч, нужен ключ ВК.</p></div>
<div class="v"><h4><b>В</b>Всё, и карты тоже</h4>
<div class="m"><small>Автопилот ведёт:</small>
<div class="chips"><i class="on">Сайт</i><i class="on">ВК</i><i class="on">Telegram</i><i class="wb">Дзен</i><i class="wb">Яндекс Карты</i><i class="wb">Google Карты</i></div>
<div class="bx"><span class="bad blink">Карты и Дзен – только через твой открытый Chrome</span></div></div>
<p><b>Полный охват, но ломается, когда мак закрыт.</b> +20 ч.</p></div>
</div>

## 4. Потолок денег на сайт в месяц

<div class="kv">
<div class="v"><h4><b>А</b>1 000 ₽</h4>
<div class="m"><small>Расход EV Sibir за ноябрь</small><div class="big">640 ₽</div><div class="bar"><u style="--w:64%;background:#ffc24b"></u></div><small>Хватает на снятие спроса раз в квартал и проверки.</small></div>
<p><b>Строго.</b> Квартальный спрос большой ниши может упереться. +0 ч.</p></div>
<div class="v"><h4><b>Б</b>3 000 ₽</h4>
<div class="m"><small>Расход EV Sibir за ноябрь</small><div class="big">640 ₽</div><div class="bar"><u style="--w:21%;background:#39ff88"></u></div><small>Запас под спрос и замер нейросетей.</small></div>
<p><b>Свободно, одна цифра на всех.</b> +0 ч.</p></div>
<div class="v rec"><h4><em>Мой совет</em><b>В</b>Свой у каждого, по умолчанию 2 000 ₽</h4>
<div class="m"><small>Пульт · потолок по клиентам</small>
<div class="bx">EV Sibir <b>2 000 ₽</b><div class="bar"><u style="--w:32%;background:#39ff88"></u></div></div>
<div class="bx">Баланс <b>1 500 ₽</b><div class="bar"><u style="--w:80%;background:#ffc24b"></u></div></div></div>
<p><b>Под размер клиента, меняешь в пульте.</b> +0 ч.</p></div>
</div>

Цифры расхода в макетах условные. Деньги здесь – XMLRiver и платные замеры; Claude по подписке в потолок не входит.

## Нужно от тебя

- Четыре буквы: 1 …, 2 …, 3 …, 4 … Мой совет – **1Б, 2А, 3А, 4В**.
- «Да» на выкладку завода на сервер: система прав остановила выкладку, без твоего слова не выкладываю. Поедут починка кнопки постов и шаг 1 автопилота.

## Шаг 1 сделан

Проверка «клиент готов» и включение автопилота – в коде (коммит ccb5abb), 810 тестов прошли. Восемь условий: факты утверждены, паспорт спроса, красный список, выкладка на сайт настроена так же строго, как её проверяет сама выкладка, боевой режим, нейросеть, потолок денег, темы в карте. Пока чего-то нет – кнопка не включается и показывает, чего. Включить в обход через общие настройки нельзя.

Независимый ревизор сначала нашёл дефект: факты утверждаются датой, а проверка ждала «да», и кнопка не включилась бы никогда. Исправлено, повторная проверка – PASS. Код в GitHub, на сервере – после твоего «да».

## Попутно починено

- Кнопка «Написать посты» в календаре отдавала ошибку: станции не было в списке пульта. Починено и закрыто тестом, который сам сверяет все кнопки пульта со списком станций (коммит 1b9964f). На сервер – вместе с шагом 1, после твоего «да».

## Что раскрыть

- Почему сейчас ничего не идёт само: каждое звено цепочки ставит человек – архитектура в репо завода, docs/avtopilot.md.
- Шаги и часы: готовность 4 ч, цепочка 6 ч, выкладка по календарю 5 ч, потолок и пауза 4 ч, пульт 6 ч, откат кнопкой 4 ч.
