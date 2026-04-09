from datetime import datetime
from .config import TZ, WEEKDAYS, MAX_BIO_LEN, BIO_SUFFIX


def now_parts() -> tuple[str, str]:
    now = datetime.now(TZ)
    return WEEKDAYS[now.weekday()], now.strftime("%H:%M")


def secs_to_next_minute() -> float:
    now = datetime.now(TZ)
    return 60 - now.second - now.microsecond / 1_000_000


def format_bio(weather: str, day: str, time_str: str, spotify: str) -> str:
    parts = [f"{weather} · {day} · {time_str}", spotify]
    if BIO_SUFFIX:
        parts.append(BIO_SUFFIX)
    return " | ".join(parts)[:MAX_BIO_LEN]

