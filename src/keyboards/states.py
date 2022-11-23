from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    uname = State()
    phone = State()
    email = State()
    cname = State()
    revueu = State()
    done = State()


class LoadFiles(StatesGroup):
    json_file = State()
    excel_file = State()
    recs_file = State()
    cid = State()