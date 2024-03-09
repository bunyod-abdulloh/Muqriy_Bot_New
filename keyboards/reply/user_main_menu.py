from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def user_main_menu_buttons(buttons_text: list):
    builder = ReplyKeyboardBuilder()
    for text in buttons_text:
        builder.add(KeyboardButton(text=text[0]))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
