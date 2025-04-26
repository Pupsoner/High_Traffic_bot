from typing import List

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


class MenuFactory(CallbackData, prefix="m"):
    action: str
    value: str = "-"

    @staticmethod
    def main() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        # builder.button(
        #     text="🤖➕ додати бота",
        #     callback_data=MenuFactory(action="add_bot")
        # )

        builder.button(
            text="Меню ботів",
            callback_data=MenuFactory(action="menu-bots")
        )

        builder.button(
            text="Адміни",
            callback_data=MenuFactory(action="admins")
        )

        builder.adjust(1)

        return builder.as_markup(resize_keyboard=True)


class UserFactory(CallbackData, prefix="u"):
    action: str
    value: str = "-"

    @staticmethod
    def confirm_join_button() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(
            text='Подтвердить',
            callback_data=UserFactory(action="confirm_join")
        )

        builder.adjust(1)

        return builder.as_markup(resize_keyboard=True)

class AdminFactory(CallbackData, prefix="a"):
    @staticmethod
    def admins_menu() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()
        builder.button(
            text='Список админов',
            callback_data=AdminFactory(action="admins_list")
        )

        builder.adjust(1)

        return builder.as_markup(resize_keyboard=True)
