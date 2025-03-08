import logging
import utils.config as config
import asyncio
from redis.asyncio import Redis
from handlers import start_handler, echo_handler, reg_handler
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from utils.logger import logger
from utils.commands import set_bot_commands
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import sql


async def main():
    bot = Bot(
        token=config.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage)
    dp.include_routers(
        start_handler.router,
        reg_handler.router,
        echo_handler.router,
    )

    await sql.create_tables()
    await set_bot_commands(bot)
    logger.info("start polling")
    await dp.start_polling(bot)

asyncio.run(main())