from aiogram import types
from config import dp
from classes.init import bd

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    state = bd.check(message.from_user.id)
    if not state:
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!\n\n /list – список команд')
        data = (message.from_user.id, message.from_user.username, message.from_user.full_name, )
        bd.get_user(data)
    else:
        await message.answer('Че надо?')