from aiogram import types
from dispatcher import *
from keyboards.start_menu import *


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("hui", reply_markup=start_kb)



if __name__ == '__main__':
    executor.start_polling(dp)
    pass