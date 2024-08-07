from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "qurantartil")
async def qurantartil_rtr(call: types.CallbackQuery):
    pass
