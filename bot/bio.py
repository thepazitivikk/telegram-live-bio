from datetime import datetime
from .config import TZ, WEEKDAYS, MAX_BIO_LEN


def now_parts() -> tuple[str, str]:
    now = datetime.now(TZ)
    return WEEKDAYS[now.weekday()], now.strftime("%H:%M")


def secs_to_next_minute() -> float:
    now = datetime.now(TZ)
    return 60 - now.second - now.microsecond / 1_000_000


def format_bio(weather: str, day: str, time_str: str, spotify: str) -> str:
    return f"{weather} · {day} · {time_str} | {spotify}"[:MAX_BIO_LEN]

