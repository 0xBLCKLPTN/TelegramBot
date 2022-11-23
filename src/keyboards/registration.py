from keyboards.response import *

@dp.message_handler(text="Регистрация", state="*")
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='Введите ваше ФИО:')
    await Registration.uname.set()


@dp.message_handler(state=Registration.uname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text.title())
    await message.answer(text='Введите номер телефона:')
    await Registration.phone.set()


@dp.message_handler(state=Registration.phone, content_types=types.ContentTypes.TEXT)
async def age_step(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text.title())
    await message.answer(text='Введите ваш Email:')
    await Registration.email.set()


@dp.message_handler(state=Registration.email, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text.title())
    await message.answer(text='Введите наименование компании:')
    await Registration.cname.set()


@dp.message_handler(state=Registration.cname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(cname=message.text.title())
    await message.answer(text='Введите выручку компании:')
    await Registration.revueu.set()

@dp.message_handler(state=Registration.revueu, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(revueu=message.text.title())
    await message.answer(text='Готово!')
    await Registration.revueu.set()
    user_data = await state.get_data()
    await state.finish()
    print(user_data)