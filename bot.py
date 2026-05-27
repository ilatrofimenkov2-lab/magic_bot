import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

TOKEN = "8956006401:AAEUArB7IsF-ceqJoaTyOajUC_XMdLJ3s2M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Купить"),
            KeyboardButton(text="📦 Тарифы"),
        ],
        [
            KeyboardButton(text="⭐ Отзывы"),
            KeyboardButton(text="📖 FAQ"),
        ],
        [
            KeyboardButton(text="📞 Поддержка"),
        ]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Kraks Store\n\n"
        "💎 Premium Product\n\n"
        "⚡ Быстрая выдача\n"
        "⚡ Поддержка 24/7\n"
        "⚡ Постоянные обновления\n\n"
        "👇 Выберите действие:",
        reply_markup=menu
    )

@dp.message()
async def menu_handler(message: Message):

    if message.text == "🛒 Купить":
        await message.answer(
            "💰 Для покупки напишите:\n"
            "@No_Fake_Kraks"
        )

    elif message.text == "📦 Тарифы":
        await message.answer(
            "📦 Тарифы:\n\n"
            "💎 1 День — 280₽\n"
            "💎 7 Дней — 1200₽\n"
            "💎 30 Дней — 3500₽"
        )

    elif message.text == "⭐ Отзывы":
        await message.answer(
            "⭐ Отзывы клиентов:\n\n"
            "✅ Отличная поддержка\n"
            "✅ Быстрая выдача\n"
            "✅ Удобный сервис"
        )

    elif message.text == "📖 FAQ":
        await message.answer(
            "📖 FAQ:\n\n"
            "❓ Как купить?\n"
            "— Напишите в поддержку\n\n"
            "❓ Как получить доступ?\n"
            "— После оплаты"
        )

    elif message.text == "📞 Поддержка":
        await message.answer(
            "📩 Поддержка:\n@No_Fake_Kraks"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())