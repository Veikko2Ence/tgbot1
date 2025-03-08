from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils.logger import logger

router = Router()

class Registration(StatesGroup):
    name = State()
    age = State()
    about = State()



@router.message(Command("reg"))
async def register_cmd(msg: Message, state: FSMContext):
    await msg.answer("Как тебя зовут?")
    await state.set_state(Registration.name)
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) начал регистрацию.")


@router.message(Registration.name)
async def get_name(msg: Message, state: FSMContext):
    user_name = msg.text.strip() 
    await state.set_data({"name": msg.text})
    await msg.answer(f"Приятно познакомиться, {user_name}!\nТеперь введи возраст")
    await state.set_state(Registration.age)
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) ввёл имя: {user_name}")


@router.message(Registration.age)
async def get_age(msg: Message, state: FSMContext):
    # age = int(msg.text)

    try:
        age = int(msg.text)
    except ValueError:
        await msg.answer("Надо число вводить!!!")
        return
    

    await state.update_data({"age": age})
    await msg.answer(f"Теперь расскажи о себе")
    await state.set_state(Registration.about)
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) ввёл возраст: {age}")



@router.message(Registration.about)
async def get_about(msg: Message, state: FSMContext):
    user_about = msg.text.strip()   

    await state.update_data({"about": msg.text})
    data = await state.get_data()
    await msg.answer(
        (
            "Готово!\n"
            f"Ваше имя: {data['name']}\n"
            f"Ваш возраст: {data['age']}\n"
            f"Ваше описание: {data['about']}\n"
            )
    )
    await state.clear()
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) Рассказал о себе: {user_about}")
    logger.info(f"Пользователь {msg.from_user.id} ({msg.from_user.username}) успешно зарегистрировался")



