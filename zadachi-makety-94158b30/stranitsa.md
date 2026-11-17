# Виджет задач: 3 раскладки дня, 3 вида таймеров и 3 варианта чёлки – выбери по одному

Нарисовала в стиле виджета, который у тебя стоит сейчас: те же вкладки, плашки проектов, кружки и корзины. Макеты живые: разделитель двигается, таймеры идут и перетаскиваются, чёлка раскрывается. Это только вид. Собирать начну после твоего выбора.

<style>
.zv-stage,.zt-stage,.zn-scr{--f:-apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif}
.zv-stage{border-radius:16px;padding:22px 12px;margin:10px 0 6px;background:#cdd3da;overflow-x:auto}
html[data-theme=dark] .zv-stage,html[data-theme=dark] .zt-stage{background:#2b2f36}
.zv-sw{display:flex;gap:8px;margin:14px 0 0}
.zv-sw button{font:13px/1 inherit;padding:8px 12px;border-radius:9px;border:1px solid var(--ln);background:var(--card);color:var(--tx);cursor:pointer}
.zv-sw button.zv-on{border-color:var(--ac);box-shadow:inset 0 0 0 1px var(--ac)}
.zv-sw button:focus-visible{outline:2px solid var(--ac);outline-offset:2px}
.zv-cap{font-size:14px;color:var(--mut);margin:6px 0 0}
.zv-win{width:340px;max-width:100%;height:580px;margin:0 auto;background:#fff;color:#1b1c1e;border-radius:22px;box-shadow:0 18px 44px rgba(20,24,32,.24),0 0 0 1px rgba(0,0,0,.06);font:13.5px/1.3 var(--f);display:flex;flex-direction:column;overflow:hidden;container-type:inline-size;text-align:left}
.zv-win.zv-a3{width:540px;max-width:none}
.zv-win.wide{width:100%;max-width:100%}
.zv-win.zv-a3.wide{min-width:540px}
.zv-head{display:flex;align-items:center;gap:14px;padding:13px 16px 11px;border-bottom:1px solid #ececee;flex:none}
.zv-tab{font-weight:700;font-size:15.5px;color:#c5c5c8;white-space:nowrap}.zv-tab b{font-weight:500;margin-left:4px}
.zv-tab.on{color:#111}.zv-tab.on b{color:#8e8e93}
.zv-x{margin-left:auto;width:22px;height:22px;border-radius:50%;background:#ededee;display:grid;place-items:center;flex:none}
.zv-x svg{width:12px;height:12px;stroke:#5c5c60;stroke-width:2.4;fill:none;stroke-linecap:round}
.zv-top{flex:0 0 var(--top,300px);overflow:auto;min-height:0}
.zv-day{flex:1 1 0;overflow:auto;min-height:0}
.zv-cols{display:flex;flex:1 1 0;min-height:0}.zv-cols .zv-top{flex:0 0 var(--left,300px);min-width:0}
.zv-split{flex:none;height:13px;cursor:row-resize;display:grid;place-items:center;background:#f7f7f8;border-top:1px solid #ececee;border-bottom:1px solid #ececee;touch-action:none}
.zv-vsplit{flex:none;width:13px;cursor:col-resize;display:grid;place-items:center;background:#f7f7f8;border-left:1px solid #ececee;border-right:1px solid #ececee;touch-action:none}
.zv-split i{width:38px;height:4px;border-radius:2px;background:#c4c4c8}.zv-vsplit i{width:4px;height:38px;border-radius:2px;background:#c4c4c8}
.zv-split:hover i,.zv-vsplit:hover i{background:#8e8e93}
.zv-foot{flex:none;display:flex;align-items:center;gap:10px;padding:11px 16px 13px;border-top:1px solid #ececee;font-size:13.5px;color:#2c2c2e}
.zi{display:inline-grid;place-items:center;width:18px;height:18px;flex:none}
.zi svg{width:100%;height:100%;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.zv-foot .zi{color:#6c6c70}
.zv-sec{display:flex;align-items:center;gap:7px;padding:13px 16px 3px;font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#8e8e93}
.zv-dot{width:7px;height:7px;border-radius:50%;flex:none}
.zv-dot.g,.zb.g{--c:#e8a400}.zv-dot.d,.zb.d{--c:#22a652}.zv-dot.r,.zb.r{--c:#3d6fd8}.zv-dot.o{--c:#b4b4b9}.zv-dot{background:var(--c)}
.zv-ost{padding-bottom:13px}.zv-ost .zi{margin-left:auto;width:14px;height:14px;color:#b4b4b9}
.zv-fire{color:#ff3b30;letter-spacing:.02em;margin-left:4px}
.zv-row{display:grid;grid-template-columns:22px 1fr auto;gap:0 11px;padding:8px 14px 8px 16px;align-items:start}
.zv-ch{width:17px;height:17px;border-radius:50%;border:1.6px solid #8e8e93;margin-top:1px}
.zv-b{min-width:0}
.zv-pill{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.07em;color:#77777c;background:#ededee;border-radius:6px;padding:2.5px 7px}
.zv-tt{font-size:13.5px;line-height:1.28;margin-top:5px;color:#111}
.l-g .zv-tt{font-size:14.5px;font-weight:600}
.zv-sub{font-size:11.5px;color:#8e8e93;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.zv-r{display:flex;flex-direction:column;align-items:flex-end;gap:7px}
.zv-r1{display:flex;align-items:center;gap:9px}.zv-r1 .zi{color:#8e8e93;width:17px;height:17px}
.zv-due{font-size:12px;font-weight:700;white-space:nowrap}.zv-due.red{color:#ff3b30}.zv-due.or{color:#ff9500}
.zv-r2{display:flex;align-items:center;gap:8px;font-size:11.5px;font-weight:600;font-variant-numeric:tabular-nums}
.zv-act{color:#b4b4b9;width:17px;height:17px;cursor:pointer}.zv-row:hover .zv-act{color:#55555a}
.zv-run{display:inline-flex;align-items:center;gap:4px;color:#1d8f45}.zv-run b{width:6px;height:6px;border-radius:50%;background:#22a652}
.zv-pom{display:inline-flex;align-items:center;gap:2px;color:#e0352b}.zv-pom .zi{width:14px;height:14px}
.zv-run em,.zv-pom em{font-style:normal}
.zv-add{display:flex;align-items:center;gap:8px;margin:2px 16px 4px 16px;padding:7px 10px;border:1px dashed #d4d4d8;border-radius:9px;font-size:12px;color:#a0a0a5}
.zv-add .zi{width:13px;height:13px}
@container (min-width:640px){.zv-layers{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-areas:"g d r" "o d r";align-content:start}
.l-g{grid-area:g}.l-d{grid-area:d;border-left:1px solid #f0f0f2}.l-r{grid-area:r;border-left:1px solid #f0f0f2}.l-o{grid-area:o}}
.zv-dsec{padding-top:10px;padding-bottom:6px}
.zd{position:relative;display:grid;grid-template-columns:50px 1fr;grid-auto-rows:15px;margin:6px 14px 12px 0;background:repeating-linear-gradient(to bottom,#ececef 0 1px,transparent 1px 30px) right top/calc(100% - 50px) 100% no-repeat}
.zd time{grid-column:1;font-size:10.5px;color:#8e8e93;text-align:right;padding-right:9px;transform:translateY(-6px);font-variant-numeric:tabular-nums}
.zb{grid-column:2;margin:2px 0 1px 2px;border-radius:6px;border-left:3px solid var(--c);background:color-mix(in srgb,var(--c) 16%,#fff);padding:0 8px;font-size:11.5px;line-height:26px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#1b1c1e;cursor:grab}
.znow{position:absolute;left:46px;right:0;border-top:1.5px solid #ff3b30}.znow::before{content:"";position:absolute;left:0;top:-4.5px;width:8px;height:8px;border-radius:50%;background:#ff3b30}
.zr{padding:10px 14px 0;overflow-x:auto}
.zr-in{position:relative;display:grid;grid-template-columns:repeat(24,minmax(27px,1fr));grid-template-rows:17px 32px;min-width:648px;background:repeating-linear-gradient(to right,#ececef 0 1px,transparent 1px calc(100% / 12)) left 17px/100% 32px no-repeat}
.zr-in time{grid-row:1;font-size:10.5px;color:#8e8e93;font-variant-numeric:tabular-nums}
.zr-in .zb{grid-row:2;grid-column-start:auto;margin:2px 1px 2px 2px;line-height:28px}
.zr-now{position:absolute;top:13px;bottom:-3px;border-left:1.5px solid #ff3b30}.zr-now::before{content:"";position:absolute;left:-4.75px;top:-4px;width:8px;height:8px;border-radius:50%;background:#ff3b30}
.zr-cap{padding:9px 16px 10px;font-size:12px;color:#1b1c1e}.zr-cap b{font-weight:700;margin-right:5px}.zr-cap span{color:#8e8e93;margin-left:8px}
.zt-stage{position:relative;border-radius:16px;margin:10px 0 6px;background:#cdd3da;overflow:hidden;font-family:var(--f)}
.zt-drag{position:absolute;touch-action:none;cursor:grab;user-select:none;-webkit-user-select:none;color:#1b1c1e;background:#fff;box-shadow:0 10px 26px rgba(20,24,32,.22),0 0 0 1px rgba(0,0,0,.06)}
.zt-drag b{font-variant-numeric:tabular-nums;font-weight:600}
.zt-live{width:8px;height:8px;border-radius:50%;background:#22a652;flex:none;display:inline-block}
.zt-n{font-size:11.5px;color:#8e8e93;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.zt-cap{display:flex;align-items:center;gap:9px;height:38px;padding:0 12px 0 14px;border-radius:19px;max-width:92%}
.zt-cap b{font-size:15px}.zt-cap .zi{color:#6c6c70;width:17px;height:17px}.zt-cap .zi.red{color:#e0352b}.zt-cap .zi.on,.zt-kh .zi.on{color:#3d6fd8}
.zt-cap .zt-n{flex:1;min-width:0}
.zt-kart{width:158px;border-radius:16px;padding:10px 12px 10px}
.zt-kh{display:flex;align-items:center;gap:6px;font-size:9.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#8e8e93}
.zt-kh span:first-child{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.zt-kh .zi{width:15px;height:15px;color:#b4b4b9}
.zt-kart>b{display:block;font-size:28px;line-height:1.15;margin-top:5px;letter-spacing:-.01em}
.zt-kart .zt-n{margin-top:1px;height:15px}
.zt-bar{height:4px;border-radius:2px;background:#ededee;margin:7px 0 5px;overflow:hidden}.zt-bar i{display:block;height:100%;background:#ff3b30;border-radius:2px}
.zt-kb{display:flex;gap:6px;margin-top:8px}.zt-kb .zi{width:30px;height:26px;border-radius:8px;background:#f2f2f4;color:#3a3a3e;padding:5px 7px;box-sizing:border-box}
.zt-ring{width:118px;height:118px;border-radius:30px;display:grid;place-items:center;text-align:center}
.zt-ring svg{grid-area:1/1;width:98px;height:98px;transform:rotate(-90deg)}.zt-ring circle{fill:none;stroke-width:5.5;stroke-linecap:round}.zt-ring .t{stroke:#ededee}
.zt-ring b{grid-area:1/1;font-size:20px;margin-top:-8px}.zt-ring span{grid-area:1/1;font-size:10.5px;color:#8e8e93;margin-top:30px}
.zs-wrap{display:flex;gap:14px;flex-wrap:wrap;margin:12px 0 4px}
.zs{flex:1 1 250px;max-width:330px;background:#fff;color:#1b1c1e;border-radius:14px;box-shadow:0 8px 24px rgba(20,24,32,.16),0 0 0 1px rgba(0,0,0,.07);font:13px/1.3 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;padding:6px 0}
.zs-h{font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#8e8e93;padding:8px 14px 6px}
.zs-r{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:7px 14px;border-top:1px solid #f0f0f2}
.zs-a{color:#3d6fd8}
.zs-st{display:inline-flex;align-items:center;background:#f2f2f4;border-radius:8px;font-variant-numeric:tabular-nums}
.zs-st em{font-style:normal;width:26px;text-align:center;color:#6c6c70;font-size:15px;line-height:26px}.zs-st b{font-weight:600;min-width:62px;text-align:center}
.zs-t{width:36px;height:22px;border-radius:11px;background:#d9d9de;position:relative;flex:none}.zs-t i{position:absolute;top:2px;left:2px;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.25)}
.zs-t.on{background:#34c759}.zs-t.on i{left:16px}
.zn-scr{position:relative;height:306px;border-radius:16px;overflow:hidden;background:#b7c1cc;margin:10px 0 6px;font:12px/1.25 var(--f);container-type:inline-size;text-align:left}
html[data-theme=dark] .zn-scr{background:#3a4048}
.zn-bar{height:32px;display:flex;justify-content:space-between;align-items:center;padding:0 14px;background:rgba(255,255,255,.46);color:#1b1c1e;font-size:12.5px}
.zn-bar b{font-weight:700;margin-right:14px}.zn-bar i{font-style:normal;margin-right:14px}
@media(max-width:640px){.zn-bar i,.zn-bar b{display:none}.zn-bar{justify-content:flex-end;font-size:11px;padding:0 8px}}
.zn{position:absolute;top:0;left:50%;transform:translateX(-50%);width:180px;height:32px;background:#000;color:#fff;border-radius:0 0 12px 12px;overflow:hidden;cursor:pointer;transition:width .26s cubic-bezier(.2,.8,.2,1),height .26s cubic-bezier(.2,.8,.2,1),border-radius .26s}
.zn.ears{width:330px}.zn.line{height:38px}
.zn.line::after{content:"";position:absolute;left:14px;bottom:3px;height:3px;width:calc((100% - 28px) * .26);background:#ff453a;border-radius:2px}
.zn.line::before{content:"";position:absolute;left:14px;right:14px;bottom:3px;height:3px;background:#2c2c2e;border-radius:2px}
.zn:hover,.zn.open{width:min(var(--w),100cqw - 16px);height:var(--h);border-radius:0 0 24px 24px}
@media(max-width:640px){.zn:hover,.zn.open{height:var(--hm)}}
.zn:hover::after,.zn.open::after,.zn:hover::before,.zn.open::before{display:none}
.zn-ears{position:absolute;inset:0 0 auto 0;height:32px;display:flex;justify-content:space-between;align-items:center;padding:0 12px;font-size:12px;font-weight:600;font-variant-numeric:tabular-nums;transition:opacity .12s}
.zn-ears span{display:inline-flex;align-items:center;gap:5px}.zn-ears em{font-style:normal}.zn-ears .zi{width:14px;height:14px;color:#ff453a}
.zn:hover .zn-ears,.zn.open .zn-ears{opacity:0}
.zn-in{position:absolute;top:0;left:50%;transform:translateX(-50%);width:min(var(--w),100cqw - 16px);box-sizing:border-box;padding:42px 16px 16px;opacity:0;transition:opacity .12s}
.zn:hover .zn-in,.zn.open .zn-in{opacity:1;transition:opacity .18s .12s}
.zn-f{display:flex;gap:16px;flex-wrap:wrap;justify-content:center;align-items:flex-start}
.zn-col{display:flex;flex-direction:column;gap:8px;flex:1 1 200px;min-width:0}
.zn-rw{display:flex;gap:8px;flex:1 1 300px;min-width:0}.zn-rw .zn-t{flex:1 1 0}
.zn-w100{flex:1 1 100%}
.zn-t{position:relative;background:#1c1c1e;border-radius:14px;padding:9px 12px 10px;min-width:0}
.zn-tl{font-size:9.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#8e8e93;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;padding-right:44px}
.zn-t>b{display:block;font-size:23px;font-weight:600;font-variant-numeric:tabular-nums;line-height:1.2;margin-top:3px}
.zn-ts{font-size:11px;color:#8e8e93;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.zn-tb{position:absolute;top:8px;right:9px;display:flex;gap:5px}.zn-tb .zi{width:17px;height:17px;color:#d1d1d6}
.zn-ch{grid-column:1/-1;font-size:9.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#8e8e93;text-align:left;margin-bottom:5px}
.zn-cal{display:grid;grid-template-columns:repeat(7,30px);gap:1px 0;text-align:center;font-size:11.5px;font-variant-numeric:tabular-nums}
.zn-cal em{font-style:normal;color:#8e8e93;font-size:10px;height:18px}
.zn-cal i{font-style:normal;height:21px;line-height:21px;border-radius:50%;width:21px;margin:0 auto;position:relative}
.zn-cal .off{color:#48484a}.zn-cal .now{background:#fff;color:#000;font-weight:700}
.zn-cal .ev::after{content:"";position:absolute;left:50%;bottom:0;width:3px;height:3px;margin-left:-1.5px;border-radius:50%;background:#ff9f0a}
.zn-ag{flex:1 1 190px;min-width:0;font-size:12.5px}.zn-ag>div:not(.zn-ch){display:flex;gap:10px;padding:4px 0;border-top:1px solid #2c2c2e}
.zn-ag time,.zn-nx time{color:#8e8e93;font-variant-numeric:tabular-nums}
.zn-wk{display:flex;justify-content:space-between;gap:2px}
.zn-wk span{flex:1;text-align:center;font-size:12.5px;padding:4px 0 5px;border-radius:9px;font-variant-numeric:tabular-nums}
.zn-wk em{display:block;font-style:normal;font-size:9.5px;color:#8e8e93;margin-bottom:1px}
.zn-wk .now{background:#fff;color:#000;font-weight:700}.zn-wk .now em{color:#6c6c70}
.zn-nx{margin-top:8px;font-size:12.5px;display:flex;gap:10px}
.zn-hint{position:absolute;left:0;right:0;bottom:12px;text-align:center;font-size:12px;color:rgba(20,24,32,.55)}
html[data-theme=dark] .zn-hint{color:rgba(255,255,255,.5)}
@media(prefers-reduced-motion:reduce){.zn,.zn-in,.zn-ears{transition:none!important}}
</style>

## 1. Задачи и день – три раскладки

Во всех трёх одинаково:

- **Слои:** главная – 1, денежные – 3, рабочие – 3, остальные свёрнуты строкой с числом.
- **В строке задачи** справа два значка: таймер задачи и помидор. У главной они уже запущены.
- **День** с 10:00 до 22:00, красная линия – сейчас. Задачу ставишь в час перетаскиванием.
- **Разделитель** между задачами и днём двигается – попробуй потянуть.

### А1. День внизу, списком по часам

<p class="zv-sw"><button data-shir="za1" data-v="0" class="zv-on">Узкий, как сейчас</button><button data-shir="za1" data-v="1">На весь стол</button></p><div class="zv-stage"><div class="zv-win" id="za1" style="--top:292px"><div class="zv-head"><span class="zv-tab on">Мои<b>7</b></span><span class="zv-tab">Команда<b>3</b></span><span class="zv-tab">Штаб<b>1</b></span><span class="zv-x"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17"/></svg></span></div><div class="zv-top"><div class="zv-layers"><div class="zv-layer l-g"><div class="zv-sec"><i class="zv-dot g"></i>Главная</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Структура страниц, показать заказчику</div><div class="zv-sub">Таймер идёт · помидор 2 из 4</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zv-run"><b></b><em data-up="m">42:10</em></span><span class="zv-pom"><span class="zi "><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span><em data-dn>18:24</em></span></div></div></div></div><div class="zv-layer l-d"><div class="zv-sec"><i class="zv-dot d"></i>Денежные · 2 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">MDS</span><div class="zv-tt">КП – отправить клиенту</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Цены для франчайзи с Денисом</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-add"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> денежная задача</div></div><div class="zv-layer l-r"><div class="zv-sec"><i class="zv-dot r"></i>Рабочие · 3 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ALEX KROWN</span><div class="zv-tt">Доступ Ирине к стенду</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">BALANCE</span><div class="zv-tt">Обсудить решение</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ФЛОРА</span><div class="zv-tt">Запросить интеграцию баллов</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div></div><div class="zv-layer l-o"><div class="zv-sec zv-ost"><i class="zv-dot o"></i>Остальные · 14<span class="zv-fire">1 горит</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></span></div></div></div></div><div class="zv-split"><i></i></div><div class="zv-day"><div class="zv-sec zv-dsec">День · вт, 17 нояб.</div><div class="zd"><time style="grid-row:1/span 2">10:00</time><time style="grid-row:3/span 2">11:00</time><time style="grid-row:5/span 2">12:00</time><time style="grid-row:7/span 2">13:00</time><time style="grid-row:9/span 2">14:00</time><time style="grid-row:11/span 2">15:00</time><time style="grid-row:13/span 2">16:00</time><time style="grid-row:15/span 2">17:00</time><time style="grid-row:17/span 2">18:00</time><time style="grid-row:19/span 2">19:00</time><time style="grid-row:21/span 2">20:00</time><time style="grid-row:23/span 2">21:00</time><span class="zb g" style="grid-row:1/5">Структура страниц</span><span class="zb d" style="grid-row:5/7">КП MDS</span><span class="zb r" style="grid-row:9/11">Доступ Ирине к стенду</span><span class="zb r" style="grid-row:11/13">Баланс – решение</span><span class="zb d" style="grid-row:13/16">Цены для франчайзи</span><span class="zb r" style="grid-row:17/19">Флора – баллы</span><i class="znow" style="top:70px"></i></div></div><div class="zv-foot"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> Новая задача</div></div></div>

<p class="zv-cap">Ближе всего к нынешнему виджету. В узком окне видно 4–5 часов, остальные прокруткой.</p>

### А2. День внизу, лентой слева направо

<p class="zv-sw"><button data-shir="za2" data-v="0" class="zv-on">Узкий, как сейчас</button><button data-shir="za2" data-v="1">На весь стол</button></p><div class="zv-stage"><div class="zv-win" id="za2" style="--top:376px"><div class="zv-head"><span class="zv-tab on">Мои<b>7</b></span><span class="zv-tab">Команда<b>3</b></span><span class="zv-tab">Штаб<b>1</b></span><span class="zv-x"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17"/></svg></span></div><div class="zv-top"><div class="zv-layers"><div class="zv-layer l-g"><div class="zv-sec"><i class="zv-dot g"></i>Главная</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Структура страниц, показать заказчику</div><div class="zv-sub">Таймер идёт · помидор 2 из 4</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zv-run"><b></b><em data-up="m">42:10</em></span><span class="zv-pom"><span class="zi "><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span><em data-dn>18:24</em></span></div></div></div></div><div class="zv-layer l-d"><div class="zv-sec"><i class="zv-dot d"></i>Денежные · 2 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">MDS</span><div class="zv-tt">КП – отправить клиенту</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Цены для франчайзи с Денисом</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-add"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> денежная задача</div></div><div class="zv-layer l-r"><div class="zv-sec"><i class="zv-dot r"></i>Рабочие · 3 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ALEX KROWN</span><div class="zv-tt">Доступ Ирине к стенду</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">BALANCE</span><div class="zv-tt">Обсудить решение</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ФЛОРА</span><div class="zv-tt">Запросить интеграцию баллов</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div></div><div class="zv-layer l-o"><div class="zv-sec zv-ost"><i class="zv-dot o"></i>Остальные · 14<span class="zv-fire">1 горит</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></span></div></div></div></div><div class="zv-split"><i></i></div><div class="zv-day"><div class="zr"><div class="zr-in"><time style="grid-column:1/span 2">10</time><time style="grid-column:3/span 2">11</time><time style="grid-column:5/span 2">12</time><time style="grid-column:7/span 2">13</time><time style="grid-column:9/span 2">14</time><time style="grid-column:11/span 2">15</time><time style="grid-column:13/span 2">16</time><time style="grid-column:15/span 2">17</time><time style="grid-column:17/span 2">18</time><time style="grid-column:19/span 2">19</time><time style="grid-column:21/span 2">20</time><time style="grid-column:23/span 2">21</time><span class="zb g" style="grid-column:1/5">Структура страниц</span><span class="zb d" style="grid-column:5/7">КП MDS</span><span class="zb r" style="grid-column:9/11">Доступ Ирине к стенду</span><span class="zb r" style="grid-column:11/13">Баланс – решение</span><span class="zb d" style="grid-column:13/16">Цены для франчайзи</span><span class="zb r" style="grid-column:17/19">Флора – баллы</span><i class="zr-now" style="left:19.58%"></i></div></div><div class="zr-cap"><b>Сейчас</b> КП MDS до 13:00 <span>дальше – Доступ Ирине к стенду, 14:00</span></div></div><div class="zv-foot"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> Новая задача</div></div></div>

<p class="zv-cap">День занимает одну строку, задачам остаётся больше места. На весь стол видны все 12 часов сразу. В узком окне лента листается вбок и сама встаёт на текущий час.</p>

### А3. День справа, колонкой

<p class="zv-sw"><button data-shir="za3" data-v="0" class="zv-on">Средний</button><button data-shir="za3" data-v="1">На весь стол</button></p><div class="zv-stage"><div class="zv-win zv-a3" id="za3" style="--left:300px"><div class="zv-head"><span class="zv-tab on">Мои<b>7</b></span><span class="zv-tab">Команда<b>3</b></span><span class="zv-tab">Штаб<b>1</b></span><span class="zv-x"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17"/></svg></span></div><div class="zv-cols"><div class="zv-top"><div class="zv-layers"><div class="zv-layer l-g"><div class="zv-sec"><i class="zv-dot g"></i>Главная</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Структура страниц, показать заказчику</div><div class="zv-sub">Таймер идёт · помидор 2 из 4</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zv-run"><b></b><em data-up="m">42:10</em></span><span class="zv-pom"><span class="zi "><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span><em data-dn>18:24</em></span></div></div></div></div><div class="zv-layer l-d"><div class="zv-sec"><i class="zv-dot d"></i>Денежные · 2 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">MDS</span><div class="zv-tt">КП – отправить клиенту</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">GRAFIT</span><div class="zv-tt">Цены для франчайзи с Денисом</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due red">15 нояб.</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-add"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> денежная задача</div></div><div class="zv-layer l-r"><div class="zv-sec"><i class="zv-dot r"></i>Рабочие · 3 из 3</div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ALEX KROWN</span><div class="zv-tt">Доступ Ирине к стенду</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">BALANCE</span><div class="zv-tt">Обсудить решение</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div><div class="zv-row"><i class="zv-ch"></i><div class="zv-b"><span class="zv-pill">ФЛОРА</span><div class="zv-tt">Запросить интеграцию баллов</div></div><div class="zv-r"><div class="zv-r1"><span class="zv-due or">сегодня</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M4.5 7h15M9.5 7V4.8h5V7M6.5 7l.9 12.2h9.2L17.5 7M10 10.5v5.5M14 10.5v5.5"/></svg></span></div><div class="zv-r2"><span class="zi zv-act"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z"/></svg></span><span class="zi zv-act"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span></div></div></div></div><div class="zv-layer l-o"><div class="zv-sec zv-ost"><i class="zv-dot o"></i>Остальные · 14<span class="zv-fire">1 горит</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></span></div></div></div></div><div class="zv-vsplit"><i></i></div><div class="zv-day"><div class="zv-sec zv-dsec">День · вт, 17 нояб.</div><div class="zd"><time style="grid-row:1/span 2">10:00</time><time style="grid-row:3/span 2">11:00</time><time style="grid-row:5/span 2">12:00</time><time style="grid-row:7/span 2">13:00</time><time style="grid-row:9/span 2">14:00</time><time style="grid-row:11/span 2">15:00</time><time style="grid-row:13/span 2">16:00</time><time style="grid-row:15/span 2">17:00</time><time style="grid-row:17/span 2">18:00</time><time style="grid-row:19/span 2">19:00</time><time style="grid-row:21/span 2">20:00</time><time style="grid-row:23/span 2">21:00</time><span class="zb g" style="grid-row:1/5">Структура страниц</span><span class="zb d" style="grid-row:5/7">КП MDS</span><span class="zb r" style="grid-row:9/11">Доступ Ирине к стенду</span><span class="zb r" style="grid-row:11/13">Баланс – решение</span><span class="zb d" style="grid-row:13/16">Цены для франчайзи</span><span class="zb r" style="grid-row:17/19">Флора – баллы</span><i class="znow" style="top:70px"></i></div></div></div><div class="zv-foot"><span class="zi "><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></span> Новая задача</div></div></div>

<p class="zv-cap">Задачи и день видны одновременно. Нужна ширина от 540 точек: узким столбиком, как сейчас, такой виджет не поставить.</p>

## 2. Таймеры – отдельные окошки

Во всех трёх одинаково:

- **Два таймера:** таймер задачи считает, сколько ты на ней сидишь; помидор отсчитывает отрезок работы и отдыха.
- **Запуск:** значком в строке задачи или отдельно, без задачи. Каждый выключается сам по себе.
- **Помидор:** минуты работы и отдыха задаёшь сам.
- **Поверх всех окон:** переключатель у каждого таймера, сразу включён.
- **Окошко ставишь куда хочешь** – в макете их тоже можно таскать.

### Б1. Капсула

<div class="zt-stage" style="height:124px"><div class="zt-cap zt-drag" style="left:4%;top:16px"><i class="zt-live"></i><b data-up="h">00:42:10</b><span class="zt-n">Структура страниц</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><rect x="6.5" y="6.5" width="11" height="11" rx="2"/></svg></span><span class="zi on"><svg viewBox="0 0 24 24"><path d="M9 4h6l-.8 6 3 3.2H6.8l3-3.2zM12 13.2V20"/></svg></span></div><div class="zt-cap zt-drag" style="left:4%;top:68px"><span class="zi red"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span><b data-dn>18:24</b><span class="zt-n">работа · 2 из 4</span><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M6 5.5v13l9-6.5zM18 5.5v13"/></svg></span><span class="zi on"><svg viewBox="0 0 24 24"><path d="M9 4h6l-.8 6 3 3.2H6.8l3-3.2zM12 13.2V20"/></svg></span></div></div>

<p class="zv-cap">Самый маленький, 38 точек в высоту: не закрывает работу. Цифры, название и кнопки в одну строку.</p>

### Б2. Карточка

<div class="zt-stage" style="height:150px"><div class="zt-kart zt-drag" style="left:4%;top:16px"><div class="zt-kh"><span>Задача</span><span class="zi on"><svg viewBox="0 0 24 24"><path d="M9 4h6l-.8 6 3 3.2H6.8l3-3.2zM12 13.2V20"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><circle cx="6" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="18" cy="12" r="1.2"/></svg></span></div><b data-up="h">00:42:10</b><div class="zt-n">Структура страниц</div><div class="zt-kb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><rect x="6.5" y="6.5" width="11" height="11" rx="2"/></svg></span></div></div><div class="zt-kart zt-drag" style="left:52%;top:16px"><div class="zt-kh"><span>Помидор · 2 из 4</span><span class="zi on"><svg viewBox="0 0 24 24"><path d="M9 4h6l-.8 6 3 3.2H6.8l3-3.2zM12 13.2V20"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><circle cx="6" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="18" cy="12" r="1.2"/></svg></span></div><b data-dn>18:24</b><div class="zt-bar"><i style="width:26%"></i></div><div class="zt-kb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M6 5.5v13l9-6.5zM18 5.5v13"/></svg></span></div></div></div>

<p class="zv-cap">Крупные цифры, кнопки всегда на виду. У помидора полоска – сколько прошло.</p>

### Б3. Кольцо

<div class="zt-stage" style="height:150px"><div class="zt-ring zt-drag" style="left:4%;top:16px"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" class="t"/><circle cx="50" cy="50" r="44" style="stroke:#22a652;stroke-dasharray:193.5 276.5" class="p"/></svg><b data-up="m">42:10</b><span>Графит</span></div><div class="zt-ring zt-drag" style="left:calc(4% + 132px);top:16px"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" class="t"/><circle cx="50" cy="50" r="44" style="stroke:#ff3b30;stroke-dasharray:71.9 276.5" class="p"/></svg><b data-dn>18:24</b><span>работа</span></div></div>

<p class="zv-cap">Кольцо показывает остаток: у помидора – до конца отрезка, у задачи – один оборот за час. Кнопки появляются при наведении.</p>

### Настройки – одинаковые для любого вида

<div class="zs-wrap"><div class="zs"><div class="zs-h">Помидор</div><div class="zs-r">Работа<span class="zs-st"><em>–</em><b>25 мин</b><em>+</em></span></div><div class="zs-r">Отдых<span class="zs-st"><em>–</em><b>5 мин</b><em>+</em></span></div><div class="zs-r">Длинный отдых<span class="zs-st"><em>–</em><b>15 мин</b><em>+</em></span></div><div class="zs-r">Длинный после<span class="zs-st"><em>–</em><b>4 кругов</b><em>+</em></span></div><div class="zs-r">Поверх всех окон<span class="zs-t on"><i></i></span></div><div class="zs-r">Звук в конце<span class="zs-t on"><i></i></span></div><div class="zs-r zs-a">Убрать в чёлку</div><div class="zs-r zs-a">Выключить помидор</div></div><div class="zs"><div class="zs-h">Таймер задачи</div><div class="zs-r">Поверх всех окон<span class="zs-t on"><i></i></span></div><div class="zs-r">Показывать название<span class="zs-t on"><i></i></span></div><div class="zs-r">Напомнить, если забыл остановить<span class="zs-t"><i></i></span></div><div class="zs-r zs-a">Убрать в чёлку</div><div class="zs-r zs-a">Выключить таймер</div></div></div>

## 3. Чёлка – таймеры и календарь при наведении

Чёлка твоего MacBook Air M2 – 179 на 32 точки, нарисовала в настоящем размере. Во всех трёх одинаково:

- **Подвёл мышь к чёлке** – панель выехала. Убрал – спряталась.
- **Таймер в чёлку:** перетащил окошко к чёлке или нажал «Убрать в чёлку». Обратно – стрелкой на плитке таймера.
- **В панели только таймеры и календарь**, задач там нет. События в календаре – пример.

### В1. Тихая: в покое чёлка пустая, внутри таймеры и месяц

<div class="zn-scr"><div class="zn-bar"><span><b>Задачи</b><i>Файл</i><i>Правка</i><i>Вид</i></span><span>вт 17 нояб.&nbsp; 12:21</span></div><div class="zn " style="--w:560px;--h:214px;--hm:392px"><div class="zn-in"><div class="zn-f"><div class="zn-col"><div class="zn-t"><div class="zn-tl">Задача</div><b data-up="h">00:42:10</b><div class="zn-ts">Структура страниц</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div><div class="zn-t"><div class="zn-tl">Помидор · 2 из 4</div><b data-dn>18:24</b><div class="zn-ts">работа</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div></div><div class="zn-cal"><div class="zn-ch">Ноябрь 2026</div><em>пн</em><em>вт</em><em>ср</em><em>чт</em><em>пт</em><em>сб</em><em>вс</em><i class="off">26</i><i class="off">27</i><i class="off">28</i><i class="off">29</i><i class="off">30</i><i class="off">31</i><i class="">1</i><i class="">2</i><i class="">3</i><i class="">4</i><i class="">5</i><i class="">6</i><i class="">7</i><i class="">8</i><i class="">9</i><i class="">10</i><i class="">11</i><i class="">12</i><i class="">13</i><i class="">14</i><i class="">15</i><i class="">16</i><i class="now">17</i><i class="ev">18</i><i class="">19</i><i class="ev">20</i><i class="">21</i><i class="">22</i><i class="">23</i><i class="ev">24</i><i class="">25</i><i class="">26</i><i class="">27</i><i class="">28</i><i class="">29</i><i class="">30</i><i class="off">1</i><i class="off">2</i><i class="off">3</i><i class="off">4</i><i class="off">5</i><i class="off">6</i></div></div></div></div><div class="zn-hint">наведи на чёлку · на телефоне нажми</div></div>

<p class="zv-cap">В покое чёлка выглядит как обычно, ничего не отвлекает.</p>

### В2. Живая: время видно по бокам чёлки, внутри встречи дня

<div class="zn-scr"><div class="zn-bar"><span><b>Задачи</b><i>Файл</i><i>Правка</i><i>Вид</i></span><span>вт 17 нояб.&nbsp; 12:21</span></div><div class="zn ears" style="--w:600px;--h:172px;--hm:318px"><div class="zn-ears"><span><i class="zt-live"></i><em data-up="m">42:10</em></span><span><span class="zi red"><svg viewBox="0 0 24 24"><circle cx="12" cy="14" r="7"/><path d="M12 7V4M12 7c-1.4-1.6-3-1.8-4.2-1.3M12 7c1.4-1.6 3-1.8 4.2-1.3"/></svg></span><em data-dn>18:24</em></span></div><div class="zn-in"><div class="zn-f"><div class="zn-rw"><div class="zn-t"><div class="zn-tl">Задача</div><b data-up="h">00:42:10</b><div class="zn-ts">Структура страниц</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div><div class="zn-t"><div class="zn-tl">Помидор · 2 из 4</div><b data-dn>18:24</b><div class="zn-ts">работа</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div></div><div class="zn-ag"><div class="zn-ch">Сегодня</div><div><time>14:00</time>Созвон с клиентом</div><div><time>15:00</time>Планёрка Евы</div><div><time>20:00</time>Итог дня</div></div></div></div></div><div class="zn-hint">наведи на чёлку · на телефоне нажми</div></div>

<p class="zv-cap">Время обоих таймеров видно всегда, без наведения. Чёлка становится шире на 75 точек с каждой стороны.</p>

### В3. Полоска: под чёлкой линия помидора, внутри неделя

<div class="zn-scr"><div class="zn-bar"><span><b>Задачи</b><i>Файл</i><i>Правка</i><i>Вид</i></span><span>вт 17 нояб.&nbsp; 12:21</span></div><div class="zn line" style="--w:400px;--h:196px;--hm:290px"><div class="zn-in"><div class="zn-f zn-nar"><div class="zn-rw"><div class="zn-t"><div class="zn-tl">Задача</div><b data-up="h">00:42:10</b><div class="zn-ts">Структура страниц</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div><div class="zn-t"><div class="zn-tl">Помидор · 2 из 4</div><b data-dn>18:24</b><div class="zn-ts">работа</div><div class="zn-tb"><span class="zi "><svg viewBox="0 0 24 24"><path d="M8.5 5.5v13M15.5 5.5v13"/></svg></span><span class="zi "><svg viewBox="0 0 24 24"><path d="M9 6h9v9M18 6L7 17"/></svg></span></div></div></div><div class="zn-w100"><div class="zn-wk"><span class=""><em>пн</em>16</span><span class="now"><em>вт</em>17</span><span class=""><em>ср</em>18</span><span class=""><em>чт</em>19</span><span class=""><em>пт</em>20</span><span class=""><em>сб</em>21</span><span class=""><em>вс</em>22</span></div><div class="zn-nx"><time>15:00</time>Планёрка Евы</div></div></div></div></div><div class="zn-hint">наведи на чёлку · на телефоне нажми</div></div>

<p class="zv-cap">Самая маленькая панель. В покое только тонкая линия под чёлкой: сколько прошло от помидора.</p>

### Что есть готового и почему делаем своё

- [boring.notch](https://github.com/TheBoredTeam/boring.notch) – бесплатная, с открытым кодом: раскрывается при наведении, музыка, календарь, полка файлов. Таймеров задач нет.
- [DynamicNotch](https://github.com/jackson-storm/dynamicnotch) – бесплатная: музыка, загрузки, системные таймеры.
- [DynamicNotchKit](https://github.com/MrKai77/DynamicNotchKit) – заготовка для разработчиков: окно в чёлке на Swift.
- NotchNook – известная, но по ней данных не нашла, не проверяла.

Ни одна не знает про наши задачи. Поэтому окно под чёлкой делаю внутри нашего приложения «Задачи»: один и тот же таймер виден в виджете, в окошке и в чёлке. Перед сборкой проверю маленькой пробой, что окно встаёт поверх строки меню на твоей macOS 26.6.

## Нужно от тебя

1. Раскладка: А1, А2 или А3.
2. Таймеры: Б1, Б2 или Б3.
3. Чёлка: В1, В2 или В3.
4. Календарь в чёлке: откуда брать встречи – Google Календарь или календарь мака?

Можно одной строкой, например: «А2 Б1 В2, Google».

## Что раскрыть

- как таймер считает время по задаче и куда его пишет;
- как таймер прячется в чёлку и выходит обратно;
- порядок сборки после выбора.

<script>
(function(){
var q=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
q('[data-shir]').forEach(function(b){b.addEventListener('click',function(){var id=b.getAttribute('data-shir');
document.getElementById(id).classList.toggle('wide',b.getAttribute('data-v')==='1');
q('[data-shir="'+id+'"]').forEach(function(x){x.classList.toggle('zv-on',x===b)})})});
q('.zv-split,.zv-vsplit').forEach(function(s){s.addEventListener('pointerdown',function(e){
var w=s.closest('.zv-win'),v=s.classList.contains('zv-vsplit'),r=s.previousElementSibling.getBoundingClientRect();
s.setPointerCapture(e.pointerId);
function mv(ev){var val=v?ev.clientX-r.left:ev.clientY-r.top,max=v?w.clientWidth-150:w.clientHeight-170;
w.style.setProperty(v?'--left':'--top',Math.max(v?170:80,Math.min(max,val))+'px')}
function up(){s.removeEventListener('pointermove',mv);s.removeEventListener('pointerup',up);s.removeEventListener('pointercancel',up)}
s.addEventListener('pointermove',mv);s.addEventListener('pointerup',up);s.addEventListener('pointercancel',up);e.preventDefault()})});
q('.zt-drag').forEach(function(t){t.addEventListener('pointerdown',function(e){
var st=t.parentNode.getBoundingClientRect(),r=t.getBoundingClientRect(),dx=e.clientX-r.left,dy=e.clientY-r.top;
t.setPointerCapture(e.pointerId);t.style.cursor='grabbing';
function mv(ev){t.style.left=Math.max(0,Math.min(st.width-r.width,ev.clientX-st.left-dx))+'px';
t.style.top=Math.max(0,Math.min(st.height-r.height,ev.clientY-st.top-dy))+'px'}
function up(){t.style.cursor='';t.removeEventListener('pointermove',mv);t.removeEventListener('pointerup',up);t.removeEventListener('pointercancel',up)}
t.addEventListener('pointermove',mv);t.addEventListener('pointerup',up);t.addEventListener('pointercancel',up);e.preventDefault()})});
q('.zn').forEach(function(n){n.addEventListener('click',function(){n.classList.toggle('open')})});
if(/otkryt/.test(location.hash))q('.zn').forEach(function(n){n.classList.add('open')});
if(/shir/.test(location.hash))q('[data-shir][data-v="1"]').forEach(function(b){b.click()});
q('.zr').forEach(function(z){z.scrollLeft=Math.max(0,z.scrollWidth*0.196-60)});
function p(x){return(x<10?'0':'')+x}
function f(n,h){var s=n%60,m=Math.floor(n/60);return h?p(Math.floor(m/60))+':'+p(m%60)+':'+p(s):p(m)+':'+p(s)}
var up=2530,dn=1104;
setInterval(function(){up++;dn=dn>0?dn-1:1500;
q('[data-up]').forEach(function(e){e.textContent=f(up,e.getAttribute('data-up')==='h')});
q('[data-dn]').forEach(function(e){e.textContent=f(dn,false)})},1000);
})();
</script>
