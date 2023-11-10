import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


logging.basicConfig(level=logging.INFO)

bot = Bot(token="6563322621:AAHv9zDSPU5JBikI73DG1ks6o123123123")    #ТОКЕН СЮДА!!!

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Відкрити сторінку магазину", web_app=WebAppInfo(url="https://123123123.com"))    #САЙТ СЮДА!!!
    )

    await message.answer(
        'Вітаю у боті! Натисни на кнопку, щоб перейти до магазину',
        reply_markup=builder.as_markup()
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
