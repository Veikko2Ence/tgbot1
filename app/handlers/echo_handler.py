from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.logger import logger

router = Router()

@router.message()
async def start_cmd(msg: types.Message):
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) отправил: {msg.text}")
    await msg.answer(f"Ты написал: {msg.text}")
