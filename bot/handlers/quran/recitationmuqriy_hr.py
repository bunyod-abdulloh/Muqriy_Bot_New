from aiogram import Router, F, types

from bot.loader import db

router = Router()


@router.callback_query(F.data == "recitationmuqriy")
async def recitationmuqriy_rtr(call: types.CallbackQuery):
    get_quranapd = await db.get_quranapd()
    print(get_quranapd)
