from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

TOKEN1 = "your telegram token " # Токен anapaWeather_bot


bot = Bot(token=TOKEN1)
dp = Dispatcher(bot, storage=storage)
