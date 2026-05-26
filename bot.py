import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)

TOKEN = 8956006401:AAEUArB7IsF-ceqJoaTyOajUC_XMdLJ3s2M"

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💎 Купить MAGIC",
                url="https://t.me/No_Fake_Kraks"
            )
        ],
        [
            InlineKeyboardButton(
                text="📦 Тарифы",
                callback_data="prices"
            ),
            InlineKeyboardButton(
                text="⭐ Отзывы",
                callback_data="reviews"
            ),
        ],
        [
            InlineKeyboardButton(
                text="📖 Инструкция",
                callback_data="guide"
            ),
            InlineKeyboardButton(
                text="📞 Поддержка",
                url="https://t.me/No_Fake_Kraks"
            ),
        ],
    ]
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Добро пожаловать в Kraks Store\n\n"
        "💎 MAGIC для OXIDE\n"
        "💰 Цена: 280₽ / 1 день\n\n"
        "📞 Покупка: @No_Fake_Kraks",
        reply_markup=main_keyboard
    )

@dp.callback_query(F.data == "prices")
async def prices(callback: CallbackQuery):
    await callback.message.answer(
        "📦 Тарифы KRaks Store\n\n"
        "💎 1 День — 280₽\n"
        "💎 7 Дней — 1200₽\n"
        "💎 30 Дней — 3500₽"
    )

@dp.callback_query(F.data == "reviews")
async def reviews(callback: CallbackQuery):
    await callback.message.answer(
        "⭐ Отзывы скоро появятся."
    )

@dp.callback_query(F.data == "guide")
async def guide(callback: CallbackQuery):
    await callback.message.answer(
        "📖 Инструкция:\n\n"
        "1. Напишите в поддержку\n"
        "2. Оплатите товар\n"
        "3. Получите доступ"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())