from aiogram import types
from config import dp
from text import list_command
from classes.init import bd

@dp.message_handler(commands=['list'])
async def help(message: types.Message):
    state = bd.return_flag(message.from_user.id)
    text = 'отключить оповещения' if state else 'включить оповещения'
    await message.answer(list_command + text, parse_mode='HTML')