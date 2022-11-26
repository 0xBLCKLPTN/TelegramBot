from utils.dataspace import *
from keyboards.admin_menu import *
from dispatcher import dp
from keyboards.states import *
from aiogram.dispatcher import FSMContext 
from aiogram import types

from core.config import *
from core import config

@dp.message_handler(text="Настройка списка администраторов")
async def process_admin_list(message: types.Message):
    text = ""
    for i in ManageAdmins().get_all_admins():
        text +=f"\n{i.username} {i.user_id}"
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply(text=f"Список администраторов: {text}", reply_markup = admin_settings_keyboard)

@dp.message_handler(text="Добавить администратора")
async def process_admin_add(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("Введите id", reply_markup = back_kb)
        await AdminAdd.id.set()

@dp.message_handler(state=AdminAdd.id)
async def process_admin_delete(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        admin = Admins(
    user_id = message.text.title()
)
        ManageAdmins().add_admin(admin)
        await state.finish()
        await message.reply("Администратор добавлен", reply_markup = admin_settings_keyboard)


@dp.message_handler(text="Удалить администратора")
async def process_admin_delete(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("Введите id", reply_markup = back_kb)
        await AdminDelete.id.set()

@dp.message_handler(state=AdminDelete.id)
async def process_admin_delete(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        ManageAdmins().remove_admin(user_id=message.text.title())
        await state.finish()
        await message.reply("Администратор удалён", reply_markup = admin_settings_keyboard)

@dp.message_handler(text="Запуск бота")
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        config.Bot_on = True
        print(config.Bot_on)
        await message.reply("Бот запущен", reply_markup = admin_keyboard)

@dp.message_handler(text="Остановка бота")
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        config.Bot_on = False
        await message.reply("Бот остановлен", reply_markup = admin_keyboard)

@dp.message_handler(text="Назад")
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("admin", reply_markup = admin_keyboard)


@dp.message_handler(text="Настройка цикла запуска")
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply('Введите цикл в минутаз')
        await StartBot.start.set()
        
@dp.message_handler(content_types=types.ContentTypes.TEXT, state=StartBot.start)
async def some_func(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        config.START_BOT = (((int(message.text) *60) ))
        await message.reply(f'Цикл запуска установлен на: {str(config.START_BOT / 60)} минут')
        await state.finish()

@dp.message_handler(text="Настройка цикла подписки", state="*")
async def process_admin_delete(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply('Введите цикл в днях')
        await SubTime.get_sub_from_user.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=SubTime.get_sub_from_user)
async def some_func(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        config.START_LOOP = (((int(message.text) * 24) * 60) * 60)
        await message.reply(f'Цикл подписки установлен до: {str(int(((config.START_LOOP / 60)/60) / 24 ))} дней')
        await state.finish()

@dp.message_handler(text="Настройка цикла запуска", state='*')
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply('Возвращаемся!', reply_markup=button_return)