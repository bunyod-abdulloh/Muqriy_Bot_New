from aiogram import Router, types, F
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from loader import db

router = Router()

category_one_list = []


async def user_main_menu_buttons():
    # buttons_text = ["📖 Qur'oni Karim", "☀️ Siyrat", "🌕 Ramazon", "📚 Ilmiy suhbatlar",
    #                 "☪️ Tahorat, namoz va zikrlar", "❓ Savol yuborish"]
    # for category in buttons_text:
    #     await db.add_category_one(category_one=category)
    buttons = await db.select_main_buttons()

    builder = ReplyKeyboardBuilder()
    for button in buttons:
        category_one_list.append(button[0])
        builder.add(KeyboardButton(text=button[0]))
    builder.adjust(2, 2, 1, 1)
    return builder.as_markup(resize_keyboard=True)


@router.message(F.text.in_(category_one_list))
async def category_one(message: types.Message):
    await message.answer('bor')


@router.message(F.photo)
async def get_photo_id(message: types.Message):
    pass
    