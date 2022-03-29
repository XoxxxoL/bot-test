from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.main_callback import profile_callback


def profile_keyb():
    keyb = InlineKeyboardMarkup(row_width=2)
    keys = InlineKeyboardButton('🗃 Кейсы', callback_data=profile_callback.new(event='keys'))
    donat = InlineKeyboardButton('🛒 Магазин', callback_data=profile_callback.new(event='donat'))
    top = InlineKeyboardButton('🏆 Топ игроков', callback_data=profile_callback.new(event='top'))
    refferal = InlineKeyboardButton('Рефералы', callback_data=profile_callback.new(event='ref'))
    settings = InlineKeyboardButton('Настройки', callback_data=profile_callback.new(event='settings'))
    keyb.add(keys, donat)
    keyb.add(top, refferal)
    keyb.add(settings)
    return keyb


async def workers_keyboard():
    menu = InlineKeyboardMarkup()
    add = InlineKeyboardButton('Нанять', callback_data=profile_callback.new(event='add_workers'))
    menu.add(add)
    return menu


async def open_keys_keyboard():
    menu = InlineKeyboardMarkup()
    open = InlineKeyboardButton('Открыть кейс', callback_data=profile_callback.new(event='open_keys'))
    menu.add(open)
    return menu


async def settings_keyboard(open: bool):
    menu = InlineKeyboardMarkup(row_width=1)
    open_profile = InlineKeyboardButton('Открыть профиль', callback_data=profile_callback.new(event='open_profile'))
    close_profile = InlineKeyboardButton('Закрыть профиль', callback_data=profile_callback.new(event='close_profile'))
    change_photo = InlineKeyboardButton('Изменить фон', callback_data=profile_callback.new(event='change_photo'))
    change_name = InlineKeyboardButton('Изменить имя', callback_data=profile_callback.new(event='change_name'))
    if open:
        menu.add(open_profile)
    else:
        menu.add(close_profile)
    menu.add(change_photo, change_name)
    return menu