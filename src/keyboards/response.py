from dispatcher import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.start_menu import *

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("hui", reply_markup=start_kb)

@dp.message(Text(text="Регистарция"))
async def description(message: types.Message):
    await message.reply("Текст описания")

@dp.message(Text(text="Расценки"))
async def description(message: types.Message):
    await message.reply("Текст расценок", reply_markup=return_kb)
    
@dp.message(Text(text="Оплата"))
async def description(message: types.Message):
    await message.reply("Текст описания", reply_markup=return_kb)

@dp.message(Text(text="Инструкция по настройке"))
async def description(message: types.Message):
    await message.reply("Текст Инструкции", reply_markup=return_kb)

@dp.message(Text(text="Загрузить cookies"))
async def description(message: types.Message):
    await message.reply("Вам необходимо загрузить документ формата .json, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message(Text(text="Загрузить id company"))
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать company id, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message(Text(text="Загрузить рекомендации к товарам"))
async def description(message: types.Message):
    await message.reply("Текст Инструкции", reply_markup=return_kb)

@dp.message(Text(text="Загрузить список товаров"))
async def description(message: types.Message):
    await message.reply("Текст Инструкции", reply_markup=return_kb)

@dp.message(Text(text="Вопросы и пожелания"))
async def description(message: types.Message):
    await message.reply("Текст Инструкции", reply_markup=return_kb)