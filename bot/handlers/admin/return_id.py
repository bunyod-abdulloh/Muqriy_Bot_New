from aiogram import Router, F, types

router = Router()


@router.message(F.content_type.in_({'photo', 'video', 'audio', 'document'}))
async def get_id_rtr(message: types.Message):
    # content type ni aniqlash
    content = getattr(message, message.content_type)

    # file_id ni olish
    if isinstance(content, list):  # ba'zi kontentlar ro'yxat bo'lishi mumkin (masalan, photo)
        file_id = content[-1].file_id
    else:
        file_id = content.file_id

    await message.answer(
        text=f'{message.content_type.upper()} ID:\n\n<code>{file_id}</code>'
    )
