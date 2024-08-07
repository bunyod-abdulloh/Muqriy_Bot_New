from aiogram import Router, F, types

from bot.keyboards.inline.user_inline import quranibuttons

router = Router()


@router.message(F.text == "📖 Qur'oni Karim")
async def quranmain_rtr(message: types.Message):
    await message.answer(
        text="📖 Qur'oni Karim bo'limi", reply_markup=quranibuttons()
    )
