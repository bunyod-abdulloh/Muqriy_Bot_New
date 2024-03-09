from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger

from keyboards.reply.user_main_menu import user_main_menu_buttons
from loader import db

start_router = Router()


@start_router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    buttons_text = ['button 1', 'button 2', 'button 3', 'button 4', 'button 5', 'button 6']
    for category in buttons_text:
        await db.add_category(category=category)
    buttons = await db.select_main_buttons()
    try:
        await db.add_user(telegram_id=telegram_id, username=username)
    except Exception as error:
        logger.info(error)
    await message.answer(text="Assalomu alaykum!",
                         reply_markup=user_main_menu_buttons(
                             buttons_text=buttons
                         ))
