import asyncio
import logging
import aiohttp
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest, UpdateStatusRequest
from .weather import fetch_weather
from .spotify import fetch_spotify
from .bio import now_parts, secs_to_next_minute, format_bio

log = logging.getLogger(__name__)


async def update_bio(client: TelegramClient, bio: str) -> None:
    try:
        await client(UpdateProfileRequest(about=bio))
        await client(UpdateStatusRequest(offline=True))
        log.info("bio → %s", bio)
    except Exception as e:
        log.error("обновление не удалось: %s", e)


async def live_loop(client: TelegramClient) -> None:
    async with aiohttp.ClientSession() as session:
        while True:
            weather, spotify = await asyncio.gather(
                fetch_weather(session),
                fetch_spotify(),
            )
            day, time_str = now_parts()
            bio = format_bio(weather, day, time_str, spotify)
            await update_bio(client, bio)
            await asyncio.sleep(secs_to_next_minute())

