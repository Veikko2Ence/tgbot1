from aiogram.types import BotCommand
from aiogram import Bot


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Увидеть приветствие"),
        BotCommand(command="reg", description="Начать регистрацию"),
    ]
    await bot.set_my_commands(commands)