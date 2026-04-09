# telegram-live-bio

юзербот который обновляет описание профиля каждую минуту

```
⛅ -15°C · пт · 03:44 | 🎵 1501 - они не ты · 0:15
```

если ничего не играет - пишет `🎵 ɪ'ᴍ ɴᴏᴛ ʟɪsᴛᴇɴɪɴɢ ᴛᴏ ᴍᴜsɪᴄ ɴᴏᴡ.`

погода с [wttr.in](https://wttr.in) - без ключей, просто работает

---

## стек

- [telethon](https://docs.telethon.dev) - telegram userbot
- [spotipy](https://spotipy.readthedocs.io) - spotify api
- [aiohttp](https://docs.aiohttp.org) - запросы к погоде
- [wttr.in](https://wttr.in) - погода без регистрации

---

## запуск

```bash
pip install -r requirements.txt
cp .env.example .env
```

заполняешь `.env`, потом просто:

```bash
python main.py
```

при первом запуске telethon спросит номер телефона + код, spotify откроет браузер для авторизации. после этого всё само, файлы сессий сохраняются локально.

---

## .env

```env
API_ID=             # my.telegram.org → apps
API_HASH=

SPOTIPY_CLIENT_ID=          # developer.spotify.com/dashboard
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback   # добавить в spotify dashboard

CITY=Yekaterinburg
TIMEZONE=Asia/Yekaterinburg

MAX_BIO_LEN=140     # 70 без premium, 140 с premium
```

---

## структура

```
├── main.py          — точка входа, авторизация
└── bot/
    ├── config.py    — все переменные окружения
    ├── weather.py   — погода через wttr.in
    ├── spotify.py   — текущий трек
    ├── bio.py       — форматирование строки, таймер
    └── core.py      — основной цикл обновления
```

---

## stealth

после каждого обновления бот вызывает `account.UpdateStatus(offline=True)` — аккаунт сразу уходит в оффлайн
