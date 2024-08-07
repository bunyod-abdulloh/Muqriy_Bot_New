from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "quransuhbattavsiya")
async def quransuhbattavsiya_rtr(call: types.CallbackQuery):
    pass
