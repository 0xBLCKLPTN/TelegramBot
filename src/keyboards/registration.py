from keyboards.response import *
from utils import validator


@dp.message_handler(text="Регистрация", state="*")
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='Введите ваше ФИО:')
    await Registration.uname.set()


@dp.message_handler(state=Registration.uname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    username = message.text.title()
    if await validator.check_name(username):
        await state.update_data(username=message.text.title())

        await message.answer(text='Введите номер телефона:')
        await Registration.phone.set()
    else:
        await message.reply('Неверно введено ФИО')


@dp.message_handler(state=Registration.phone, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text.title())
    await message.answer(text='Введите ваш Email:')
    await Registration.email.set()


@dp.message_handler(state=Registration.email, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    email = message.text.title()
    if await validator.check_email(email):
        await state.update_data(email=message.text.title())
        await message.answer(text='Введите наименование компании:')
        await Registration.cname.set()
    else:
        await message.reply('Неверно введет Email')


@dp.message_handler(state=Registration.cname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(cname=message.text.title())
    await message.answer(text='Введите выручку компании:')
    await Registration.revueu.set()




@dp.message_handler(state=Registration.revueu, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    revueu = message.text.title()
    if validator.check_revenue(revueu):
        await state.update_data(revueu=message.text.title())
        await message.answer(text='Готово!')
        await Registration.revueu.set()
        user_data = await state.get_data()
        await state.finish()
        print(user_data)
    else:
        await message.reply('Введите число')