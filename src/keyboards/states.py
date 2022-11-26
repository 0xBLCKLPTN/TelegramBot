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

class AdminDelete(StatesGroup):
    id = State()

class AdminAdd(StatesGroup):
    id = State()


class SubTime(StatesGroup):
    get_sub_from_user = State()

class StartBot(StatesGroup):
    start = State()

class Payment(StatesGroup):
    qw = State()
    InputUserData = State()