import asyncio
import logging

# import time
from aiogram import Bot, Dispatcher, types
from bot.routers import setup_main_routers
from aiogram.client.default import DefaultBotProperties
from configuration import Configuration

logging.basicConfig(level=logging.INFO)


bot = Bot(token=Configuration.bot_token, default=DefaultBotProperties(parse_mode='HTML'))

dispatcher = Dispatcher()


async def main():
    setup_main_routers(dispatcher=dispatcher)
    await dispatcher.start_polling(
        bot
    )

if __name__ == "__main__":
    asyncio.run(main())
