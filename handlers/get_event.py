from aiogram.dispatcher import FSMContext
from classes.fsm import UserStatus
from aiogram import types
from config import dp
from functions.check_date import verification_date
from classes.init import bd
from text import get_text


@dp.message_handler(commands=['get'])
async def add_event(message: types.Message):
    await UserStatus.get_date.set()
    await message.answer(get_text , parse_mode='HTML')


@dp.message_handler(state=UserStatus.get_date)
async def get_data(message: types.Message, state: FSMContext):
    date = verification_date(message.text)
    if date:
        await state.update_data(data_event=date[0])
        await message.answer('Введи комментарий:')
        await UserStatus.get_comment.set()
    else:
        await message.answer('Что-то пошло не так, попробуй еще раз!')


@dp.message_handler(state=UserStatus.get_comment)
async def get_comment(message: types.Message, state: FSMContext):
    await state.update_data(comm_event=message.text)
    data = await state.get_data()
    bd.get_event(message.from_user.id, (data['data_event'], data['comm_event'], ))
    await message.answer('Событие добавлено!\n/list - список команд')
    await state.finish()
