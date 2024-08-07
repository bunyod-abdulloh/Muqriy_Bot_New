from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "onkechabir")
async def onkechabir_rtr(call: types.CallbackQuery):
    pass
