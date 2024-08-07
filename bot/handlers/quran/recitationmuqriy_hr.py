from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "recitationmuqriy")
async def recitationmuqriy_rtr(call: types.CallbackQuery):
    pass
