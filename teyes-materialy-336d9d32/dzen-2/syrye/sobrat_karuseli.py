#!/usr/bin/env python3
"""Карточки трёх каруселей: сцены из gen/out → istochniki, karusel.py (текст рисует скрипт) → jpg/ и NN-имя.webp."""
import shutil, subprocess
from pathlib import Path
from PIL import Image
K = Path(__file__).resolve().parent.parent
GEN = K / 'syrye/gen/out'
IMENA = {
 'karusel-kitay': ['oblozhka-iz-kitaya', 'navigator-v-pekin', 'pochemu-kitay', 'na-oshchup', 'rusifikaciya', 'cena-haval-h9', 'po-russki'],
 'karusel-sugrob': ['oblozhka-sugrob', 'nichego-ne-vidno', 'slepaya-zona', 'bamper', 'kamera-omyvatel', 'cena-x-trail', 'sugrob-szadi'],
 'karusel-prisoska': ['oblozhka-telefon', 'provod-prisoska', 'vse-v-telefone', 'sezd-pozadi', 'teyes-shtatno', 'cena-solaris', 'telefon-v-karmane'],
}
import sys
for k, imena in IMENA.items():
    if len(sys.argv) > 1 and k not in sys.argv[1:]:
        continue
    ist = K / k / 'istochniki'
    for png in GEN.glob(f'{k.split("-")[1][0]}[0-9].png'):
        shutil.copy(png, ist / png.name)
    jpg = K / k / 'jpg'
    subprocess.run(['python3', str(Path.home() / 'Sites/redakciya/scripts/karusel.py'), str(ist / 'karusel.json'), str(ist), str(jpg)], check=True)
    for f in K.joinpath(k).glob('[0-9][0-9]-*.webp'):
        f.unlink()
    for i, imya in enumerate(imena, 1):
        src = jpg / f'{i:02d}.jpg'
        dst = jpg / f'{i:02d}-{imya}.jpg'
        src.rename(dst)
        Image.open(dst).save(K / k / f'{i:02d}-{imya}.webp', 'WEBP', quality=84)
    print('ok', k)
