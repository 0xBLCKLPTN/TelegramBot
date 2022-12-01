from keyboards.response import *
from utils import validator
from utils import dataspace
from models.models import Users
from keyboards.start_menu import *


@dp.message_handler(text="Регистрация", state="*")
async def name_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        await message.answer(text='Введите ваше ФИО:')
        await Registration.uname.set()


@dp.message_handler(state=Registration.uname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        username = message.text.title()
        if await validator.check_name(username):
            await state.update_data(username=message.text.title())

            await message.answer(text='Введите номер телефона:')
            await Registration.phone.set()
        else:
            await message.reply('Неверно введено ФИО')


@dp.message_handler(state=Registration.phone, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        number = message.text
        if await validator.check_revenue(number):
            await state.update_data(phone=message.text)
            await message.answer(text='Введите ваш Email:')
            await Registration.email.set()
        else:
            await message.reply('Введите число')


@dp.message_handler(state=Registration.email, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        email = message.text
        if await validator.check_email(email):
            await state.update_data(email=message.text)
            await message.answer(text='Введите наименование компании:')
            await Registration.cname.set()
        else:
            await message.reply('Неверно введет Email')


@dp.message_handler(state=Registration.cname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        await state.update_data(cname=message.text)
        await message.answer(text='Введите выручку компании:')
        await Registration.revueu.set()


@dp.message_handler(state=Registration.revueu, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    if core.config.Bot_on:
        revueu = message.text
        if await validator.check_revenue(revueu):
            await state.update_data(revueu=message.text)
            await message.answer(text='Готово!', reply_markup=main_kb)
            await Registration.revueu.set()
            user_data = await state.get_data()
            await state.finish()
            
            name_list = user_data['username'].split(' ')
            user = Users(
                FirstName = name_list[1],
                MiddleName = name_list[2],
                LastName = name_list[0],

                username = message.from_user.username,
                user_id = message.from_user.id,
                phone_number = user_data['phone'],
                email = user_data['email'],

                company_name = user_data['cname'],
                revenue = user_data['revueu']
            )
            dataspace.ManageUsers().add_user(user)
            
        else:
            await message.reply('Введите число')