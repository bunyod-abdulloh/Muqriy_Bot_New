from aiogram import F, types

router = Router()


@router.callback_query(F.data == "onkechaikki")
async def onkechaikki_rtr(call: types.CallbackQuery):
    pass
