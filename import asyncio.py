import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder  # Інструмент для зручного створення кнопок

# Твій токен з файлу
bot = Bot(token="8885074317:AAGfmv0NIEQqZ7WgIc8zVQ7nO-cGd1DnZV4")
dp = Dispatcher()


# Обробник команди /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Створюємо будівельник клавіатури прямо тут
    builder = InlineKeyboardBuilder()

    builder.add(
        types.InlineKeyboardButton(
            text="Основний чат", url="https://t.me/+nnmnG7YHRYs5ODY6"
        )
    )

    builder.add(
        types.InlineKeyboardButton(
            text="спортивно аналітичний чат",
            url="https://t.me/+V9j3UpdyYKdkMDcy",
        )
    )

    # ПРИБРАНО ПРОБІЛ: тепер посилання починається суворо з "https"
    builder.add(
        types.InlineKeyboardButton(
            text="сайт", url="https://orange-nady-76.tiiny.site"
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="схема бою", url="https://drive.google.com/file/d/1BirlgU1RX_1x_sSH6hfY5sBvDIF2huVq/view?usp=sharing"
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="правила", url="https://t.me/geyboilink/7"
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text="спонсори", url="https://t.me/geyboilink/8"
        )
    )           



    # Робимо так, щоб кожна кнопка була красивою великою смужкою одна під одною
    builder.adjust(1)

    # Відправляємо повідомлення і прикріплюємо нашу створену кнопку
    await message.reply(
        "ось посилання на наші офіційні чати і додаткові матеріали.",
        reply_markup=builder.as_markup(),
    )


async def main():
    print("Бот успішно запущений і готовий до роботи...")
    await dp.start_polling(bot)


# Головна точка запуску
if __name__ == "__main__":
    asyncio.run(main())