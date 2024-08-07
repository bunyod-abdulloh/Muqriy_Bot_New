from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "husarymuallim")
async def husarymuallim_rtr(call: types.CallbackQuery):
    pass
