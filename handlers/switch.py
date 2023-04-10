from aiogram import types
from config import dp
from classes.init import bd

@dp.message_handler(commands=['switch'])
async def switch(message: types.Message):
    state = bd.switch(message.from_user.id)
    if state: 
        await message.answer('Оповещения включены.')
    else:
        await message.answer('Оповещения отключены.')
