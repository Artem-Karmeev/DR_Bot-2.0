from aiogram import types
from config import dp
from classes.database import UserData as us


@dp.message_handler(commands=['switch'])
async def switch(message: types.Message):
    us(message).switch()
    state = us(message).check_flag()
    if state: 
        await message.answer('Оповещения включены.')
    else:
        await message.answer('Оповещения отключены.')
