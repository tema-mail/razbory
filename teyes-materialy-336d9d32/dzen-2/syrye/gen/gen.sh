#!/bin/bash
# gen.sh <имя> <файл промта> [референсы...] – одна картинка через codex exec (Sol, low), бесплатно по подписке
G="$(cd "$(dirname "$0")" && pwd)"; name=$1; pf=$2; shift 2
args=(); for r in "$@"; do args+=(-i "$G/ref/$r"); done
out="$G/out/$name.png"
if [ ${#args[@]} -gt 0 ]; then pre="Референсы приложены: роли у них описаны в промте (reference image 1, 2 – по порядку приложения)."; else pre="Референсов нет: генерируй только по тексту, ничего не прикладывай и не запрашивай."; fi
prompt="Сгенерируй ОДНУ картинку встроенным imagegen. $pre
Скопируй текст между маркерами в imagegen дословно, символ в символ. Не перефразируй, не сокращай, не дополняй.
=== НАЧАЛО ПРОМТА ===
$(cat "$pf")
=== КОНЕЦ ПРОМТА ===
Сохрани результат как $out (PNG). Затем приведи точную строку, которую передал в imagegen."
printf "%s" "$prompt" > "$G/out/$name.prompt"
codex exec -m gpt-5.6-sol -c model_reasoning_effort="low" -s workspace-write -C "$G" "${args[@]}" -- - < "$G/out/$name.prompt" > "$G/out/$name.log" 2>&1
if [ -s "$out" ]; then echo "OK $name"; else echo "FAIL $name"; tail -5 "$G/out/$name.log"; fi
