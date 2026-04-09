import os
import pytz
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "userbot")
CITY = os.getenv("CITY", "Yekaterinburg")
TZ = pytz.timezone(os.getenv("TIMEZONE", "Asia/Yekaterinburg"))
MAX_BIO_LEN = int(os.getenv("MAX_BIO_LEN", "140"))
BIO_SUFFIX = os.getenv("BIO_SUFFIX", "")
WEEKDAYS = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://127.0.0.1:8888/callback")

