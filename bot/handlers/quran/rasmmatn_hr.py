from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "quranrasm/matn")
async def quranrasm_matn_rtr(call: types.CallbackQuery):
    pass

