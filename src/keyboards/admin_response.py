from utils.dataspace import *
from keyboards.admin_menu import *
from dispatcher import dp
from aiogram.dispatcher import FSMContext 
from aiogram import types

@dp.message_handler(text="Настройка списка администраторов")
async def process_admin_list(message: types.Message):
    text = ""
    for i in ManageAdmins().get_all_admins():
        text +=f"\n{i.username} {i.user_id}"
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply(text=f"Список администраторов: {text}", reply_markup = admin_settings_keyboard)

@dp.message_handler(text="Добавить администратора")
async def process_admin_add(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("Введите id", reply_markup = back_kb)

@dp.message_handler(text="Удалить администратора")
async def process_admin_delete(message: types.Message, state: FSMContext):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("Введите id", reply_markup = back_kb)

@dp.message_handler(text="Назад")
async def process_admin_delete(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("admin", reply_markup = admin_keyboard)