from aiogram import F, types, Router

router = Router()


@router.callback_query(F.data == "onkechauch")
async def onkechauch_rtr(call: types.CallbackQuery):
    pass
