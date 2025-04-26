from aiogram import Dispatcher
from aiogram import Router
from . import start, join_request

router = Router()

def setup_main_routers(dispatcher: Dispatcher) -> None:
    router.include_router(start.router)
    router.include_router(join_request.router)
    dispatcher.include_router(router)

__all__ = [
    'setup_main_routers'
]
