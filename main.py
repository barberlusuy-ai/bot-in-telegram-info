import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder  

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

ADMIN_ID = 7580774097  
saved_news_variable = "" 
waiting_for_text = False 


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    
    builder = InlineKeyboardBuilder()

    # 1. Головна кнопка додатка (тепер правильно додається в builder)
    web_app = types.WebAppInfo(url="https://untitled-1222-2cr3alyuc-barberlusuy-6752s-projects.vercel.app/") 
    builder.add(
        types.InlineKeyboardButton(text="🏆 Відкрити додаток", web_app=web_app)
    )

    # 2. Інші кнопки з твоїми посиланнями
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
    
    # Вирівнюємо всі кнопки по одній в ряд
    builder.adjust(1)

    # Перша відповідь з посиланнями
    await message.reply(
        "ось посилання на наші офіційні чати і додаткові матеріали.",
        reply_markup=builder.as_markup(),
    )
    
    # Створюємо другу клавіатуру для новин
    builder2 = InlineKeyboardBuilder()
    builder2.add(types.InlineKeyboardButton(text="новости", callback_data="show_news"))
    
    # Друга відповідь з кнопкою новин
    await message.answer(
        "Якщо ви хочете отримувати новини від нашого посла, натисніть кнопку нижче.",
        reply_markup=builder2.as_markup(),
    )


@dp.message(lambda message: message.text == "Додати новость" and message.from_user.id == ADMIN_ID)
async def ask_for_news(message: types.Message):
    global waiting_for_text
    waiting_for_text = True  
    await message.answer("Ок, пиши")


@dp.message(lambda message: waiting_for_text and message.from_user.id == ADMIN_ID)
async def save_to_variable(message: types.Message):
    global saved_news_variable, waiting_for_text
    
    saved_news_variable = message.text 
    waiting_for_text = False 
    
    await message.answer(f"Успішно збережено в змінну! Ось твій текст:\n{saved_news_variable}")


@dp.callback_query(lambda c: c.data == "show_news")
async def process_show_news(callback_query: CallbackQuery):
    global saved_news_variable
    
    if saved_news_variable == "":
        await callback_query.message.answer("Новин поки немає, заходьте пізніше!")
    else:
        await callback_query.message.answer(f"Останні новини:\n\n{saved_news_variable}")
        
    await callback_query.answer()


async def main():
    print("Бот успішно запущений і готовий до роботи...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
