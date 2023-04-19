from aiogram.dispatcher import FSMContext
from classes.fsm import UserStatus
from aiogram import types
from config import dp
from functions.check_date import verification_date
from classes.database import UserData as us


@dp.message_handler(commands=['add'])
async def add_event(message: types.Message):
    await UserStatus.add_date.set()

    await message.answer('<b>Введи дату</b>, в формате <em>"ДД.ММ.ГГГГ"</em>:', parse_mode='HTML')


@dp.message_handler(state=UserStatus.add_date)
async def add_data(message: types.Message, state: FSMContext):
    date = verification_date(message.text)
    if date:
        await state.update_data(data_event=date[0])
        await message.answer('Введи комментарий:') 
        await UserStatus.add_comment.set()
    else:
        await message.answer('Что-то пошло не так, попробуй еще раз!')


@dp.message_handler(state=UserStatus.add_comment)
async def add_comment(message: types.Message, state: FSMContext):
    await state.update_data(comm_event=message.text)
    data = await state.get_data()
    us(message).new_event((data['data_event'], data['comm_event'], ))
    await message.answer('Событие добавлено!')
    await state.finish()