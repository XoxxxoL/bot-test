from aiogram.dispatcher.filters.state import StatesGroup, State

class SettingsState(StatesGroup):
    ChangeUserName = State()
    GetUserImage = State()