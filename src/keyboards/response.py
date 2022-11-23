from dispatcher import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.start_menu import *
from aiogram.dispatcher import FSMContext 
from keyboards.states import *
from utils import validator
@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("hui", reply_markup=start_kb)

#############################
@dp.message_handler(text="Регистрация", state="*")
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='Введите ваше ФИО:')
    await Registration.uname.set()


@dp.message_handler(state=Registration.uname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    username = message.text.title()
    if await validator.check_name(username):
        await state.update_data(username=username)
        await message.answer(text='Введите номер телефона:')
        await Registration.phone.set()
    else:
        await message.reply('Неправильное ФИО, проверьте еще раз')


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
        await message.reply('Неправильный формат электронной почты. Попробуйте еще раз')


@dp.message_handler(state=Registration.cname, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    revueu = message.text.title()
    if validator.check_revenue(revueu):
        await message.answer(text='Введите выручку компании:')
        await Registration.revueu.set()
    else:
        await message.reply('Введите число')

@dp.message_handler(state=Registration.revueu, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    await state.update_data(revueu=message.text.title())
    await message.answer(text='Поздравляем с успешной регистрацией!')
    await Registration.revueu.set()
    user_data = await state.get_data()
    await state.finish()
    print(user_data)
#############################

@dp.message_handler(text="Расценки")
async def description(message: types.Message):
    await message.reply("Текст расценок", reply_markup=return_kb)

@dp.message_handler(text="Описание")
async def description(message: types.Message):
    await message.reply("Текст описания", reply_markup=return_kb)
    


@dp.message_handler(text="Оплата")
async def description(message: types.Message):
    await message.reply("Текст описания", reply_markup=return_kb)

@dp.message_handler(text="Инструкция по настройке")
async def description(message: types.Message):
    await message.reply("Текст Инструкции", reply_markup=return_kb)

@dp.message_handler(text="Загрузить cookies")
async def description(message: types.Message):
    await message.reply("Вам необходимо загрузить документ формата .json, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Загрузить id company")
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать company id, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Загрузить рекомендации к товарам")
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать файл «рекомендации к товарам» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Загрузить список товаров")
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать файл «список товаров» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Вопросы и пожелания")
async def description(message: types.Message):
    await message.reply("Вы можете написать свой вопрос или пожелание по работе бота, мы постараемся ответит Вам в ближайшее время", reply_markup=return_kb)

@dp.message_handler(text="Вернуться")
async def description(message: types.Message):
    await message.answer("Привет!",reply_markup=return_kb)