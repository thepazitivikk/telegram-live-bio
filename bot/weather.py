import logging
import aiohttp
from .config import CITY

log = logging.getLogger(__name__)


def _icon(code: int) -> str:
    if code == 113: return "☀️"
    if code == 116: return "⛅"
    if code in (119, 122): return "☁️"
    if code in (143, 248, 260): return "☂️"
    if code in (200, 386, 389, 392, 395): return "⛈️"
    if code in (227, 230, 323, 326, 329, 332, 335, 338, 368, 371): return "❄️"
    if code in (179, 317, 320, 350, 362, 365, 374, 377): return "🌨️"
    if code in (176, 263, 266, 353): return "🌦️"
    return "🌧️"


async def fetch_weather(session: aiohttp.ClientSession) -> str:
    try:
        async with session.get(
            f"https://wttr.in/{CITY}?format=j1",
            headers={"Accept": "application/json"},
        ) as r:
            data = await r.json(content_type=None)
        cond = data["current_condition"][0]
        temp = round(float(cond["temp_C"]))
        return f"{_icon(int(cond['weatherCode']))} {temp}°C"
    except Exception as e:
        log.warning("погода: %s", e)
        return "🌡️ --°C"

