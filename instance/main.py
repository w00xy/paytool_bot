import logging
import os

import asyncio

from aiogram.client.default import DefaultBotProperties

from instance.config import TOKEN
from instance.handlers.routers import routers
from instance.utils.add_product import orm_test_products
from instance.utils.logger import setup_logging
from instance.utils.private import private
from middlewares.db import DataBaseSession

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from database.engine import create_db, drop_db, session_maker

allowed_updates = ['message, edited_message']


async def on_startup():

    run_param = False
    if run_param:
        await drop_db()

    await create_db()

    async with session_maker() as session:
        await orm_test_products(session)


async def on_shutdown():
    logging.info("Bot started")


async def main():

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))

    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates=True)

    for router in routers:
        dp.include_router(router)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=allowed_updates)

if __name__ == "__main__":
    setup_logging()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot was closed!")
