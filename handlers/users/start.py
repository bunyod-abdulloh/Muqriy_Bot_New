from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.client.session.middlewares.request_logging import logger
from loader import db

start_router = Router()


@start_router.message(CommandStart())
async def do_start(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    user = None
    try:
        user = await db.add_user(telegram_id=telegram_id, username=username)
    except Exception as error:
        logger.info(error)
    await message.answer(text="Assalomu alaykum!")
