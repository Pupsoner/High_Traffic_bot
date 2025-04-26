from aiogram import Router

from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.keyboards.factories import MenuFactory, AdminFactory
from configuration import Configuration

router = Router()

@router.message(CommandStart())
async def process_message(
        message: Message
):
    user_id = message.from_user.id
    if user_id in Configuration.admins:
        await message.answer(
            text="<b>Админ панель</b>",
            reply_markup=AdminFactory.admins_menu(),
        )
    else:
        await message.answer(
            text="<b>Ви в меню</b>",
            reply_markup=MenuFactory.main(),
        )
