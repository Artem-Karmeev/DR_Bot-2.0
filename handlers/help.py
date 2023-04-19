# from aiogram import types
# from config import dp

# from classes.user import UserData as us

# @dp.message_handler(commands=['help'])
# async def help(message: types.Message):

#     text = 'отключить оповещения' if us(message.from_user.id).check_user() else 'включить оповещения'
#     await message.answer(f'{list_command}{text}', parse_mode='HTML')
