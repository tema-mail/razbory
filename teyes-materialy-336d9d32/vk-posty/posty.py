"""Данные 10 постов ВК TEYES Sibir (следующие работы после №230 УАЗ Профи): карточка, фото, ссылки.
Факты – только из записи мастера (поле work в cases.json) и из того, что видно на фото работы."""
from pathlib import Path

KESH = Path.home() / '.cache/teyes-vk-posty'
REAL = KESH / 'work/real'          # реальные фото, номера закрыты (prep.py)
GEN = KESH / 'jobs'                # картинки Codex: jobs/<задание>/out.png
SAYT = 'https://teyes-sibir.ru'
UTM = 'utm_source=vk&utm_medium=social&utm_campaign=keys&utm_content='
ZEL, SIN = '#7BD35A', '#3FA7FF'    # акцент как на карточках владельца: УАЗ – зелёный, Honda Fit – синий

# kadry: (файл, подпись, фокус object-position). vid: 'do-posle' – стрелка «до → после»; 'dva' – два кадра работы; 'odin' – один широкий
# geroy: (файл, ширина картинки в px на карточке, сдвиг x, сдвиг y) – машина крупно
POSTY = [
 dict(n=1, nomer=231, papka='01-toyota-rav4', mashina='Toyota RAV4', rabota='Teyes LUXONE вместо штатного экрана',
      zag=['RAV4 с экраном,', 'который говорит', '*по-русски*'], model='TOYOTA RAV4', pod='Установка мультимедиа<br>Teyes LUXONE', slogan='Современные<br>мультимедиа<br>для вашего авто',
      akcent=ZEL, vid='do-posle', geroy=('gen:01-hero', 900, 290, -180),
      kadry=[('220-01', 'ДО УСТАНОВКИ', '70% 45%'), ('220-02', 'ПОСЛЕ УСТАНОВКИ', '72% 48%')],
      ikonki=[('ekran', 'Teyes<br>LUXONE'), ('shirokiy', 'Широкий экран<br>вместо штатного'), ('yazyk', 'Меню<br>на русском'), ('nav', 'Навигация<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['220-01', '220-02', '220-03'], url='/store/catalog/toyota', metka='231_toyota_rav4'),
 dict(n=2, nomer=232, papka='02-honda-stepwgn', mashina='Honda Stepwgn', rabota='Teyes CC4 Pro и подключение потолочного монитора',
      zag=['Чтобы сзади', 'не спрашивали:', '*«Долго ещё?»*'], model='HONDA STEPWGN', pod='Teyes CC4 Pro<br>и потолочный монитор', slogan='Больше<br>возможностей<br>в каждой поездке',
      akcent=SIN, vid='do-posle', geroy=('gen:02-hero', 900, 250, -170),
      kadry=[('221-01', 'ДО УСТАНОВКИ', '18% 50%'), ('221-03', 'ПОСЛЕ УСТАНОВКИ', '30% 55%')],
      ikonki=[('ekran', 'Teyes<br>CC4 Pro'), ('potolok', 'Потолочный<br>монитор'), ('dva', 'Одна картинка<br>на двух экранах'), ('nav', 'Навигация<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['221-01', '221-03', '221-04', '221-05'], url='/services/ceiling-monitors', metka='232_honda_stepwgn'),
 dict(n=3, nomer=233, papka='03-honda-wr-v', mashina='Honda WR-V', rabota='Teyes CC3L',
      zag=['Навигатор', 'больше не живёт', '*в подстаканнике*'], model='HONDA WR-V', pod='Установка мультимедиа<br>Teyes CC3L', slogan='Профессиональная<br>установка<br>автомультимедиа',
      akcent=ZEL, vid='dva', geroy=('222-03', 560, 526, 10),
      kadry=[('222-02', 'ПРАВЫЙ РУЛЬ, ЭКРАН В ПАНЕЛИ', '25% 45%'), ('222-01', 'МЕНЮ НА РУССКОМ', '50% 32%')],
      ikonki=[('ekran', 'Teyes<br>CC3L'), ('yazyk', 'Меню<br>на русском'), ('muzyka', 'Радио<br>и музыка'), ('nav', 'Навигация<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['222-01', '222-02', '222-03', '222-04'], url='/store/catalog/honda', metka='233_honda_wr-v'),
 dict(n=4, nomer=234, papka='04-honda-cr-v', mashina='Honda CR-V', rabota='Teyes CC2 Plus, штатные функции сохранены',
      zag=['Экран новый.', 'Штатное –', '*на месте*'], model='HONDA CR-V', pod='Установка мультимедиа<br>Teyes CC2 Plus', slogan='Установка<br>с сохранением<br>штатных функций',
      akcent=SIN, vid='do-posle', geroy=('223-05', 800, 330, -120),
      kadry=[('223-02', 'ДО УСТАНОВКИ', '50% 22%'), ('223-04', 'ПОСЛЕ УСТАНОВКИ', '55% 38%')],
      ikonki=[('ekran', 'Teyes<br>CC2 Plus'), ('verh', 'Верхний<br>дисплей работает'), ('klimat', 'Климат<br>на экране'), ('kamera', 'Камера<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['223-01', '223-02', '223-03', '223-04', '223-05', '223-06'], url='/store/catalog/honda', metka='234_honda_cr-v'),
 dict(n=5, nomer=235, papka='05-honda-freed', mashina='Honda Freed', rabota='Teyes CC4 и видеорегистратор',
      zag=['В споре на дороге', 'прав тот,', 'у кого *запись*'], model='HONDA FREED', pod='Teyes CC4<br>и видеорегистратор', slogan='Для реальных<br>ситуаций<br>на дороге',
      akcent=ZEL, vid='dva', geroy=('224-01', 650, 440, 10),
      kadry=[('224-03', 'РЕГИСТРАТОР НА СТЕКЛЕ', '60% 35%'), ('224-04', 'ЕГО КАРТИНКА НА ЭКРАНЕ', '50% 25%')],
      ikonki=[('ekran', 'Teyes<br>CC4'), ('registrator', 'Видео-<br>регистратор'), ('glaz', 'Запись видна<br>на экране'), ('nav', 'Навигация<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['224-01', '224-02', '224-03', '224-04', '224-05', '224-06'], url='/services/dashcam', metka='235_honda_freed'),
 dict(n=6, nomer=236, papka='06-toyota-wish', mashina='Toyota Wish', rabota='Teyes CC4 и StarLine S96 GSM GPS',
      zag=['Пока вы', 'пьёте кофе,', 'машина *греется*'], model='TOYOTA WISH', pod='StarLine S96 GSM GPS<br>и мультимедиа Teyes CC4', slogan='Сигнализации<br>и мультимедиа<br>в одном сервисе',
      akcent=SIN, vid='odin', geroy=('225-01', 700, 400, -40),
      kadry=[('225-02', 'ПОСЛЕ УСТАНОВКИ: TEYES CC4', '40% 42%')],
      ikonki=[('shchit', 'StarLine<br>S96'), ('gsm', 'GSM-<br>модуль'), ('gps', 'GPS'), ('ekran', 'Teyes<br>CC4'), ('nav', 'Навигация<br>на экране')],
      foto=['225-01', '225-02'], url='/services/starline', metka='236_toyota_wish'),
 dict(n=7, nomer=237, papka='07-hyundai-h-1', mashina='Hyundai H-1', rabota='Teyes CC4',
      zag=['Задний ход', 'без просьбы', '*«Выйди, посмотри»*'], model='HYUNDAI H-1', pod='Установка мультимедиа<br>Teyes CC4', slogan='Профессиональная<br>установка<br>автомультимедиа',
      akcent=ZEL, vid='dva', geroy=('226-02', 1100, 120, 40),
      kadry=[('226-04', 'КАМЕРА ЗАДНЕГО ВИДА НА ЭКРАНЕ', '68% 55%'), ('226-03', 'TEYES CC4 В ПАНЕЛИ', '80% 40%')],
      ikonki=[('ekran', 'Teyes<br>CC4'), ('kamera', 'Камера<br>заднего вида'), ('linii', 'Линии<br>траектории'), ('nav', 'Навигация<br>на экране'), ('android', 'Android<br>и приложения')],
      foto=['226-01', '226-02', '226-03', '226-04'], url='/store/catalog/hyundai', metka='237_hyundai_h-1'),
 dict(n=8, nomer=238, papka='08-hyundai-solaris', mashina='Hyundai Solaris', rabota='Teyes CC3 2K, экран 11 дюймов',
      zag=['Навигатор', 'больше не падает', '*с присоски*'], model='HYUNDAI SOLARIS', pod='Teyes CC3 2K<br>с экраном 11 дюймов', slogan='Современные<br>мультимедиа<br>для вашего авто',
      akcent=SIN, vid='do-posle', geroy=('gen:08-hero', 900, 190, -180),
      kadry=[('227-03', 'ДО УСТАНОВКИ', '50% 30%'), ('227-01', 'ПОСЛЕ УСТАНОВКИ', '45% 28%')],
      ikonki=[('ekran', 'Teyes<br>CC3 2K'), ('shirokiy', 'Экран<br>11 дюймов'), ('nav', 'Карта<br>на экране'), ('muzyka', 'Музыка<br>и радио'), ('android', 'Android<br>и приложения')],
      foto=['227-01', '227-02', '227-03'], url='/store/catalog/hyundai', metka='238_hyundai_solaris'),
 dict(n=9, nomer=239, papka='09-toyota-highlander', mashina='Toyota Highlander', rabota='Teyes CC4 Pro, цифровой регистратор, камера заднего вида, парктроники на 8 датчиков, цифровой микрофон',
      zag=['Highlander', 'паркуется', '*по приборам*'], model='TOYOTA HIGHLANDER', pod='Teyes CC4 Pro, камера,<br>парктроники, регистратор', slogan='Мультимедиа<br>и доп. оборудование<br>в одном сервисе',
      akcent=ZEL, vid='dva', geroy=('228-01', 780, 350, -110),
      kadry=[('228-03', 'КАМЕРА ЗАДНЕГО ВИДА', '50% 30%'), ('228-04', 'РЕГИСТРАТОР ЗА ЗЕРКАЛОМ', '50% 62%')],
      ikonki=[('ekran', 'Teyes<br>CC4 Pro'), ('kamera', 'Камера<br>заднего вида'), ('parktronik', 'Парктроники:<br>8 датчиков'), ('registrator', 'Цифровой<br>регистратор'), ('mikrofon', 'Цифровой<br>микрофон')],
      foto=['228-01', '228-02', '228-03', '228-04', '228-05'], url='/store/catalog/toyota', metka='239_toyota_highlander'),
 dict(n=10, nomer=240, papka='10-suzuki-jimny', mashina='Suzuki Jimny', rabota='Teyes CC4, динамики в передние двери, камеры спереди и сзади, регистратор, микрофон, розетка-прикуриватель',
      zag=['В Jimny', 'наконец', '*слышно* музыку'], model='SUZUKI JIMNY', pod='Динамики в двери, камеры,<br>мультимедиа Teyes CC4', slogan='Автозвук<br>и мультимедиа<br>в одном сервисе',
      akcent=SIN, vid='do-posle', geroy=('gen:10-hero', 900, 250, -180),
      kadry=[('229-09', 'ДО: ШТАТНЫЙ ДИНАМИК', '80% 60%'), ('229-04', 'ПОСЛЕ: НОВЫЙ ДИНАМИК', '75% 55%')],
      ikonki=[('dinamik', 'Динамики<br>в дверях'), ('ekran', 'Teyes<br>CC4'), ('kamera', 'Камеры<br>спереди и сзади'), ('registrator', 'Видео-<br>регистратор'), ('mikrofon', 'Микрофон')],
      foto=['229-01', '229-02', '229-03', '229-04', '229-05', '229-06', '229-07', '229-09'], url='/services/installing_car_audio', metka='240_suzuki_jimny'),
]


def ssylka(p):
    return f"{SAYT}{p['url']}?{UTM}{p['metka']}"


def put_kadra(imya):
    """'220-01' – реальное фото; 'gen:01-hero' – картинка Codex."""
    return GEN / imya[4:] / 'out.png' if imya.startswith('gen:') else REAL / f'{imya}.jpg'


# Номера на сгенерированных сценах: если модель нарисовала на табличке знаки – размываем ровно по рамке (координаты в кадре 1086×1448)
RAZMYT = {
    '05-sit': [[(594, 638), (752, 638), (752, 694), (594, 694)]],
    '09-sit': [[(518, 726), (772, 716), (772, 798), (518, 808)]],
}
