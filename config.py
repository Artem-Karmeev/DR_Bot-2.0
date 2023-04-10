from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3


bot = Bot(token='')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


link_bd = r''
connect = sqlite3.connect(link_bd)
cursor = connect.cursor()

print(type(cursor), type(connect))