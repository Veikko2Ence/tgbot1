import logging
import sqlalchemy
import config
import asyncio
from handlers import start_handler, echo_handler
# from utils import logger
from aiogram import Dispatcher, Bot, types
from aiogram.types import Message
from aiogram.filters import Command
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.logger import logger
# from aiogram.utils import executor

async def main():  
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start_handler.router,
        echo_handler.router,
    )

    logger.info("start polling")
    await dp.start_polling(bot)

asyncio.run(main())