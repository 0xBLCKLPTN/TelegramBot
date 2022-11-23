from dispatcher import dp, bot
from aiogram import types
from utils.dataspace import *
from keyboards.start_menu import *
from aiogram.dispatcher import FSMContext 
from keyboards.states import *
from keyboards.admin_menu import *
from utils import validator
from core.config import settings
from keyboards.load_files import *

@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    if ManageAdmins().check_admin(user_id = str(message.from_user.id)):
        await message.reply("admin", reply_markup=admin_keyboard)
    else:
        await message.reply("Привет! Тебе нужно зарегестрироваться!", reply_markup=start_kb)

@dp.message_handler(commands=["add"])
async def process_start_command(message: types.Message):
    admin = Admins(
    user_id = message.from_user.id
)
    ManageAdmins().add_admin(admin)





@dp.message_handler(text="Расценки", state='unreg')
async def description(message: types.Message):
    await message.reply("Текст расценок", reply_markup=return_kb)

@dp.message_handler(text="Описание", state='unreg')
async def description(message: types.Message):
    await message.reply("Текст описания", reply_markup=return_kb)
    

PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=4200000)

@dp.message_handler(text="Оплата", state='*')
async def description(message: types.Message):
    await message.reply("Текст описания", reply_markup=return_kb)
    await bot.send_invoice(
        message.chat.id,
        title='welcome',
        description='simple description',
        provider_token=settings.PAYMENT_TOKEN,
        currency='rub',
        #photo_url=TIME_MACHINE_IMAGE_URL,
        #photo_height=512,  # !=0/None, иначе изображение не покажется
        #photo_width=512,
        #photo_size=512,
        is_flexible=False,  # True если конечная цена зависит от способа доставки
        prices=[PRICE],
        start_parameter='time-machine-example',
        payload='some-invoice-payload-for-our-internal-use'
)



@dp.message_handler(text="Инструкция по настройке", state='*')
async def description(message: types.Message):
    with open(settings.INSTRUCTIONS_FILE) as file:
        text = file.read()

    await message.reply(text, reply_markup=return_kb)

@dp.message_handler(text="Загрузить id company", state='*')
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать company id, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Загрузить рекомендации к товарам", state='*')
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать файл «рекомендации к товарам» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Загрузить список товаров", state='*')
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать файл «список товаров» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)

@dp.message_handler(text="Вопросы и пожелания", state='*')
async def description(message: types.Message):
    await message.reply("Вы можете написать свой вопрос или пожелание по работе бота, мы постараемся ответит Вам в ближайшее время", reply_markup=return_kb)

@dp.message_handler(text="Вернуться", state='*')
async def description(message: types.Message):
    await message.answer("Привет!",reply_markup=main_kb)