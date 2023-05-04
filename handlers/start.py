from aiogram import types
from config import dp
from classes.database import UserData as us


@dp.message_handler(commands=['start'])
async def start(message: types.Message ):

    result = us(message).check_in_db()
    if not result:
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!')
    else:
        await message.answer('Чё надо?')