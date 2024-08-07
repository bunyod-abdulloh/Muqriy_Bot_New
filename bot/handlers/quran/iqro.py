from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "quraniqro")
async def quraniqro_rtr(call: types.CallbackQuery):
    pass
