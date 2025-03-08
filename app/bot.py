import logging
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, String
import utils.config as config
import asyncio
from redis.asyncio import Redis
from handlers import start_handler, echo_handler, reg_handler
from aiogram import Dispatcher, Bot, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message
from aiogram.filters import Command
from utils.logger import logger
# from sql.base import base
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# from middleware.middlewares import LoggingMiddleware


async def main():
    bot = Bot(
        token=config.TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)
    storage = RedisStorage(redis)
    dp = Dispatcher(storage=storage)
    # dp.update.middleware(LoggingMiddleware())
    dp.include_routers(
        start_handler.router,
        reg_handler.router,
        echo_handler.router,
    )

    # engine = create_engine(
    #     f"postgresql+psycopg2://{config.PSQL_USER}:{config.PSQL_PASS}@{config.PSQL_HOST}:{config.PSQL_PORT}/{config.PSQL_NAME}",
    #     echo = True,
    # )

    logger.info("start polling")
    await dp.start_polling(bot)

asyncio.run(main())