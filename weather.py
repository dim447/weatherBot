from aiogram import types
import requests, json
import time
from create_bot import dp, bot


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'\nОтлично, _{message.from_user.username}_! \n'
                         f'Давайте посмотрим погоду в вашем городе \U00002600 \U000026C5 \U000026C8'
                         f'\nВведите название города...', parse_mode="Markdown")
    await message.delete()


@dp.message_handler()
async def city(message: types.Message):
    try:
        city_name = message.text
        all_data = get_weather(city_name)
        await bot.send_message(message.from_user.id, all_data)
        await message.answer(f'\n\n\U0001F609 Отлично, _{message.from_user.username}_! '
                             f'\n\U0001F50D Хотите еще узнать прогноз? \n'
                             f'\U0001F3D9 Введите название города...', parse_mode="Markdown")
    except:
        await message.answer('Вы ввели несуществующий город \U0001F914')
        await message.delete()


def get_weather(city):
    token2 = "9a9e959741f380a7acddf10b84428114"  # токен погоды
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    Weather_url = "http://openweathermap.org/img/wn/"

    URL = BASE_URL + "q=" + city + "&lang=ru&appid=" + token2  # upadting the URL
    code_smile = {
        "01d": "\U00002600",
        "02d": "\U000026C5",
        "03d": "\U00002601",
        "04d": "\U0001F325",
        "09d": "\U0001F327",
        "10d": "\U0001F326",
        "11d": "\U0001F329",
        "13d": "\U0001F328",
        "50d": "\U0001F32B"
    }

    response = requests.get(URL)  # HTTP request
    if response.status_code == 200:  # checking the status code of the request
        data = response.json()  # getting data in the json format
        # print (data)
        main = data['main']  # getting the main dict block
        wind1 = data['wind']
        time_set = data['sys']
        temperature = round(main['temp'] - 273, 0)  # getting temperature
        feels_like = round(main['feels_like'] - 273, 0)  # ощущается
        humidity = main['humidity']  # getting the humidity
        pressure = round(int(main['pressure']) / 1.333223684, 0)  # getting the pressure
        wind = round(wind1['speed'], 1)  # getting the wind
        sunrise = time.strftime("%H:%M:%S", time.localtime(time_set['sunrise']))
        sunset = time.strftime("%H:%M:%S", time.localtime(time_set['sunset']))
        deg = wind1['deg']
        if deg > 0 and deg < 90:
            deg1 = 'С/В'
        elif deg > 90 and deg < 180:
            deg1 = 'Ю/В'
        elif deg > 180 and deg < 270:
            deg1 = 'Ю/З'
        elif deg > 270 and deg < 360:
            deg1 = 'С/З'
        elif deg == 0 or deg == 360:
            deg1 = 'C'
        elif deg == 180:
            deg1 = 'Ю'
        elif deg == 270:
            deg1 = 'З'
        elif deg == 90:
            deg1 = 'B'
        report = data['weather']  # weather report
        description_weather = report[0]['description']
        icon_weather = data['weather'][0]['icon']
        if icon_weather in code_smile:
            icon = code_smile[icon_weather]
        else:
            icon = code_smile["50d"]
        result = (
            f"{city:-^30}\n\n \U0001F321 Температура:  {temperature} \U00002103\n \U0001F321 Ощущается как: {feels_like} \U00002103\n \U0001F4A7 Влажность: {humidity} %\n \U0001F50B Давление: {pressure} мм рт.ст.\n \U0001F4A8 Ветер: {wind} м/с Направление : {deg1}\n \U0001F305 Восход солнца : {sunrise}\n \U0001F307 Заход солнца: {sunset}\n Сейчас:  {icon}  -{description_weather}-")
        # print (result)
        # print(time_set['sunrise'], time.localtime(time_set['sunrise']))
        return result
    else:
        pass
