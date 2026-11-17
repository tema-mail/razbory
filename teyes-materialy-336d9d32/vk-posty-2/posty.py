"""Данные 10 постов ВК TEYES Sibir, вторая десятка: работы №241–251 (№242 пропущена – один кадр с лицом сотрудника, без «до»).
Факты – только из записи мастера (cases.json, поле work) и из того, что видно на фото работы.
Фото – фотобанк (копия выгрузки Telegram на маке, md5 как на Диске), папки по data/fotobank-ruchnye.json: сдвиг 230–234 учтён."""
from pathlib import Path

KESH = Path.home() / '.cache/teyes-vk-posty'
REAL = KESH / 'work/real2'         # реальные фото, номера закрыты (prep2.py)
GEN = KESH / 'jobs2'               # картинки Codex: jobs2/<задание>/out.png
SAYT = 'https://teyes-sibir.ru'
UTM = 'utm_source=vk&utm_medium=social&utm_campaign=keys&utm_content='
ZEL, SIN = '#7BD35A', '#3FA7FF'

# Баннер: posle – (кадр, object-position, масштаб) во весь баннер В1; do – (кадр, позиция, подпись) – вставка В1 и левый кадр В2/В4;
# para – True, если do/posle это настоящие «до → после» (стрелка, подписи ДО/ПОСЛЕ); иначе подписи из do[2] и posle_podpis.
# glav – главный кадр В2 (машина или панель крупно); v3 – кадр В3; v4 – (левый, правый) кадры разреза.
POSTY = [
 dict(n=1, nomer=241, papka='01-toyota-prado-150', mashina='Toyota Land Cruiser Prado 150', rabota='Teyes CC4 Pro вместо штатного экрана',
      zag=['Prado:', 'экран во всю', '*нишу панели*'], model='TOYOTA PRADO 150', pod='Teyes CC4 Pro', akcent=ZEL, rul='левый',
      posle=('241-02', '50% 34%', 1.0), do=('241-01', '80% 45%', 'ДО'), dz=1.6, para=True, posle_podpis='ПОСЛЕ',
      glav=('241-02', '50% 30%', 1.0), v3=('241-02', '50% 36%'), v4=(('241-01', '82% 46%', 1.5), ('241-02', '50% 40%', 1.0)),
      foto=['241-01', '241-02'], url='/store/catalog/toyota', metka='241_toyota_prado_150'),
 dict(n=2, nomer=243, papka='02-kia-k5', mashina='Kia K5 (Optima)', rabota='Teyes CC3 2K',
      zag=['K5 из Кореи:', 'кнопки остались,', 'экран – *новый*'], model='KIA K5', pod='Teyes CC3 2K', akcent=SIN, rul='левый',
      posle=('243-02', '80% 40%', 1.0), do=('243-01', '50% 30%', 'ДО'), dz=1.25, para=True, posle_podpis='ПОСЛЕ',
      glav=('243-02', '78% 40%', 1.0), v3=('243-02', '78% 38%'), v4=(('243-01', '50% 34%', 1.0), ('243-02', '80% 40%', 1.15)),
      foto=['243-01', '243-02'], url='/store/catalog/kia', metka='243_kia_k5'),
 dict(n=3, nomer=244, papka='03-honda-vezel', mashina='Honda Vezel', rabota='Teyes CC2 Plus',
      zag=['Vezel 2026:', 'правый руль,', 'меню *по-русски*'], model='HONDA VEZEL', pod='Teyes CC2 Plus', akcent=ZEL, rul='правый',
      posle=('244-03', '24% 50%', 1.0), do=('244-01', '32% 30%', 'ДО'), dz=1.35, para=True, posle_podpis='ПОСЛЕ',
      glav=('244-03', '22% 50%', 1.0), v3=('244-03', '22% 52%'), v4=(('244-02', '22% 55%', 1.2), ('244-03', '18% 55%', 1.2)),
      foto=['244-01', '244-02', '244-03'], url='/store/catalog/honda', metka='244_honda_vezel'),
 dict(n=4, nomer=245, papka='04-nissan-juke', mashina='Nissan Juke', rabota='штатный круговой обзор на Teyes CC3 2K',
      zag=['Сменили', 'магнитолу. Обзор', '*360° остался*'], model='NISSAN JUKE', pod='Штатный круговой обзор<br>на Teyes CC3 2K', akcent=SIN, rul='правый',
      posle=('245-02', '28% 58%', 1.0), do=('245-01', '14% 62%', 'МЕНЮ TEYES'), para=False, posle_podpis='КРУГОВОЙ ОБЗОР',
      glav=('245-02', '26% 60%', 1.0), v3=('245-02', '28% 62%'), v4=(('245-01', '14% 62%', 1.3), ('245-02', '28% 60%', 1.3)),
      foto=['245-01', '245-02'], url='/store/catalog/nissan', metka='245_nissan_juke'),
 dict(n=5, nomer=246, papka='05-honda-cr-v', mashina='Honda CR-V', rabota='врезной микрофон в потолок',
      zag=['«Вас не слышно»', 'больше', '*не говорят*'], model='HONDA CR-V', pod='Врезной микрофон в потолок', akcent=ZEL, rul='левый',
      posle=('246-01', '50% 30%', 1.0), do=('246-03', '60% 70%', 'САЛОН'), para=False, posle_podpis='МИКРОФОН',
      glav=('246-01', '50% 30%', 1.0), v3=('246-02', '50% 30%'), v4=(('246-03', '62% 70%', 1.0), ('246-02', '50% 30%', 1.0)),
      foto=['246-01', '246-02', '246-03'], url='/services/installation_teyes', metka='246_honda_cr-v'),
 dict(n=6, nomer=247, papka='06-toyota-highlander', mashina='Toyota Highlander', rabota='Teyes CC4 Pro, цифровой микрофон, регистратор, задняя камера',
      zag=['Highlander:', 'четыре работы', '*за один заезд*'], model='TOYOTA HIGHLANDER', pod='Teyes CC4 Pro, камера,<br>регистратор, микрофон', akcent=SIN, rul='левый',
      posle=('247-02', '50% 30%', 1.0), do=('247-01', '72% 40%', 'ДО'), dz=1.6, para=True, posle_podpis='ПОСЛЕ',
      glav=('247-05', '50% 62%', 1.0), v3=('247-02', '50% 28%'), v4=(('247-01', '70% 45%', 1.3), ('247-03', '62% 42%', 1.3)),
      foto=['247-01', '247-02', '247-03', '247-04', '247-05', '247-06', '247-07'], url='/services/dashcam', metka='247_toyota_highlander'),
 dict(n=7, nomer=248, papka='07-toyota-prius', mashina='Toyota Prius', rabota='Teyes CC2 7 дюймов, нестандартная установка',
      zag=['Prius: климат', 'на месте,', 'Teyes – *под ним*'], model='TOYOTA PRIUS', pod='Teyes CC2, 7 дюймов', akcent=ZEL, rul='левый',
      posle=('248-02', '55% 50%', 1.0), do=('248-01', '70% 52%', 'ДО'), dz=1.4, para=True, posle_podpis='ПОСЛЕ',
      glav=('248-03', '76% 55%', 1.0), v3=('248-02', '55% 55%'), v4=(('248-01', '68% 60%', 1.3), ('248-03', '72% 60%', 1.3)),
      foto=['248-01', '248-02', '248-03'], url='/store/catalog/toyota', metka='248_toyota_prius'),
 dict(n=8, nomer=249, papka='08-hyundai-creta', mashina='Hyundai Creta', rabota='Teyes CC2, камера заднего вида, регистратор',
      zag=['Назад – по', 'картинке, вперёд –', '*с записью*'], model='HYUNDAI CRETA', pod='Teyes CC2, камера,<br>регистратор', akcent=SIN, rul='левый',
      posle=('249-01', '74% 48%', 1.0), do=('249-04', '80% 45%', 'РЕГИСТРАТОР'), para=False, posle_podpis='КАМЕРА НА ЭКРАНЕ',
      glav=('249-05', '50% 8%', 1.4), v3=('249-01', '74% 50%'), v4=(('249-05', '45% 50%', 1.0), ('249-01', '76% 50%', 1.2)),
      foto=['249-01', '249-03', '249-04', '249-05'], url='/store/catalog/hyundai', metka='249_hyundai_creta'),
 dict(n=9, nomer=250, papka='09-toyota-rav4', mashina='Toyota RAV4', rabota='Teyes LUXONE',
      zag=['RAV4: экран', 'переехал', '*наверх*'], model='TOYOTA RAV4', pod='Teyes LUXONE', akcent=ZEL, rul='левый',
      posle=('250-02', '70% 40%', 1.0), do=('250-01', '74% 50%', 'ДО'), dz=1.7, para=True, posle_podpis='ПОСЛЕ',
      glav=('250-02', '70% 38%', 1.0), v3=('250-02', '72% 40%'), v4=(('250-01', '76% 50%', 1.5), ('250-02', '70% 45%', 1.25)),
      foto=['250-01', '250-02'], url='/store/catalog/toyota', metka='250_toyota_rav4'),
 dict(n=10, nomer=251, papka='10-subaru-outback', mashina='Subaru Outback', rabota='Teyes CC4L',
      zag=['Outback:', 'вместо экрана', 'с ладонь – *Teyes*'], model='SUBARU OUTBACK', pod='Teyes CC4L', akcent=SIN, rul='левый',
      posle=('251-02', '50% 30%', 1.0), do=('251-01', '72% 45%', 'ДО'), dz=1.7, para=True, posle_podpis='ПОСЛЕ',
      glav=('251-03', '72% 45%', 1.0), v3=('251-02', '50% 32%'), v4=(('251-01', '74% 48%', 1.5), ('251-03', '72% 50%', 1.3)),
      foto=['251-01', '251-02', '251-03'], url='/store/catalog/subaru', metka='251_subaru_outback'),
]

PROPUSK = [(242, 'Nissan Qashqai J10', 'в папке работы (по фотобанку – «231_Kia optima») один кадр: экран TeyesOS, справа сотрудник с лицом; кадра «до» нет, на баннер «до/после» и четыре варианта не хватает')]


def ssylka(p):
    return f"{SAYT}{p['url']}?{UTM}{p['metka']}"


def put(imya):
    return REAL / f'{imya}.jpg'
