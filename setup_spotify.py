import os
from dotenv import load_dotenv, set_key
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

_SCOPE = "user-read-currently-playing user-read-playback-state"

auth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback"),
    scope=_SCOPE,
    open_browser=False,
)

print("\nоткрой эту ссылку в браузере:\n")
print(auth.get_authorize_url())
print()
url = input("вставь адрес, на который тебя перенаправило: ").strip()
code = auth.parse_response_code(url)
token = auth.get_access_token(code, as_dict=True)

set_key(".env", "SPOTIPY_REFRESH_TOKEN", token["refresh_token"])
print("\n✅ готово — SPOTIPY_REFRESH_TOKEN сохранён в .env")
print("теперь можно деплоить на хост, браузер больше не нужен")

