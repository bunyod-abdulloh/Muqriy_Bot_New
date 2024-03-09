from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="All users")
        ],
        [
            KeyboardButton(text="Reklama")
        ],
        [
            KeyboardButton(text="Clean DB")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
