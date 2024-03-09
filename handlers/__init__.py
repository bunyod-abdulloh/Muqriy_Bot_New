from aiogram import Router

from filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import admin, start, help, echo
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.start_router.message.filter(ChatPrivateFilter(chat_type=["private"]))

    router.include_routers(admin.router, start.start_router, help.router, echo.router, error_handler.router)

    return router
