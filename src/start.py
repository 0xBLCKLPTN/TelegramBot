from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from keyboards.start_menu import *

bot = Bot(token="5843120216:AAEKuj9NkCahZM5Mu1-lQDoBfQ7lGXkEeJk")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("hui", reply_markup=start_kb)



if __name__ == '__main__':
    executor.start_polling(dp)
    pass