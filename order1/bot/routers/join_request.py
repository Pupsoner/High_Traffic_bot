from aiogram import Bot, Router, F
from aiogram.types import Message, ChatJoinRequest, CallbackQuery
from bot.keyboards.factories import UserFactory

router = Router()


@router.chat_join_request()
async def join_request(event: ChatJoinRequest):
    await event.bot.send_message(
        chat_id=event.from_user.id,
        text=f'Приветствую, <b>{event.from_user.full_name}!</b>\nНажмите "Подтвердить", чтоб войти в канал!',
        reply_markup=UserFactory.confirm_join_button()
    )


@router.callback_query(UserFactory.filter(F.action == 'confirm_join'))
async def process_callback_query(
        callback_query: CallbackQuery,
        bot: Bot
):
    user_id = callback_query.from_user.id
    await bot.approve_chat_join_request(chat_id="-1002542714704", user_id=user_id)
