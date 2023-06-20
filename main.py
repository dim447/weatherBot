import logging
from aiogram import executor
from create_bot import dp
from weather import get_weather


async def on_startup(dp):
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)


##############################################################
if __name__ == '__main__':
    print('Бот погоды запущен!')
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
##############################################################
