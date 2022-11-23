from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    uname = State()
    phone = State()
    email = State()
    cname = State()
    revueu = State()
    done = State()