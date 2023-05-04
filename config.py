from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



bot = Bot(token='5688981493:AAEVZtJ4DFiQ7dH7tmKcXj8Ze3I8RcSCeAU')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


link_db = r'C:\Users\79996\Desktop\full_prod\db\db_v1.1.db'