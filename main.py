import asyncio
import logging
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError, AuthRestartError
from bot.config import API_ID, API_HASH, SESSION_NAME
from bot.core import live_loop

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


async def main() -> None:
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        phone = input("📱 Номер телефона: ")
        while True:
            try:
                await client.send_code_request(phone)
                break
            except AuthRestartError:
                pass
        try:
            await client.sign_in(phone, input("🔑 Код из Telegram: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("🔐 Пароль 2FA: "))

    log.info("авторизован · запускаю цикл")
    try:
        await live_loop(client)
    finally:
        await client.disconnect()
        log.info("отключён")


if __name__ == "__main__":
    asyncio.run(main())
