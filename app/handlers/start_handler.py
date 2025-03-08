from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.logger import logger

router = Router()

@router.message(Command("start"))
async def start_cmd(msg: Message):
    await msg.answer("Добрый день юный подаван")
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) отправил: /start")
