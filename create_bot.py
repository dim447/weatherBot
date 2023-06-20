from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN1 = "6004218271:AAEC3vQbTX5dh5RTC_f8Wjms5VT6q2KPMQQ"  # Токен телеграм AnapaTestBot


bot = Bot(token=TOKEN1)
dp = Dispatcher(bot, storage=storage)

