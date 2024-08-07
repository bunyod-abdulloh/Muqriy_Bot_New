from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "quranhamnafas")
async def quranhamnafas_rtr(call: types.CallbackQuery):
    pass

