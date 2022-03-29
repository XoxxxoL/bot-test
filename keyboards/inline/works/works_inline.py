from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.works.works_data import works_data


async def works_menu(works):
    menu = InlineKeyboardMarkup(row_width=2)
