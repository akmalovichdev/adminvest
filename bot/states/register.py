from aiogram.dispatcher.filters.state import State, StatesGroup

class UserForm(StatesGroup):
    fullname = State()
    contact = State()
    success = State()