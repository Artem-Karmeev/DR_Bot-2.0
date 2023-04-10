from aiogram.dispatcher.filters.state import StatesGroup, State

class UserStatus(StatesGroup):
    get_date = State()
    get_comment = State()

    search = State()

    delete = State()