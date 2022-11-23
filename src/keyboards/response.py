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