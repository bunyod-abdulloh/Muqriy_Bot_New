from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "qurantanishuv")
async def qurantanishuv_rtr(call: types.CallbackQuery):
    pass
