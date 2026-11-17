#!/bin/bash
# ждём сброса лимита Codex (04:58 НСК) и догоняем очередь
cd "$(dirname "$0")"
while [ "$(date +%H%M)" -lt 0503 ] || [ "$(date +%H%M)" -gt 1200 ]; do sleep 60; done
cat jobs-rest.txt | xargs -P 3 -L 1 ./gen.sh > run-rest.log 2>&1
grep -c ^OK run-rest.log; grep ^FAIL run-rest.log
