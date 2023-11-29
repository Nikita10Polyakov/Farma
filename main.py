from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

#TOKEN
TOKEN = ""
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Відкрити сторінку магазину", web_app=WebAppInfo(url="https://"))) #Сайт СЮДИ!!!
    await message.answer("Вітаю у боті! Натисни на кнопку, щоб перейти до магазину", reply_markup=markup)

executor.start_polling(dp)
