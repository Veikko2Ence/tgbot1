from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()

@router.message()
async def start_cmd(msg: Message):
    await msg.answer(msg.text)
