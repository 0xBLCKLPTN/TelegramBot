from core.config import settings
from keyboards.response import *
from utils import other_utils, validator
import io
from utils import dataspace

@dp.message_handler(text="Загрузить cookies", state='*')
async def load_json_file(message: types.Message, state: FSMContext):
    await message.reply("Вам необходимо загрузить документ формата .json, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)
    await LoadFiles.json_file.set()


@dp.message_handler(state=LoadFiles.json_file, content_types=types.ContentTypes.DOCUMENT)
async def fname_step(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await other_utils.create_dir(str(user_id))
    
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    destination = settings.DATA_STORAGE + user_id + "/" +file_path.split('/')[-1]
    await other_utils.remove_old_json(user_id, 'json')
    await bot.download_file(file_path, destination)
    print('Done!')
    dataspace.ManageUsers().load_cookies(user_id, destination)
    await state.finish()
    await message.reply('Готово!', reply_markup=main_kb)



@dp.message_handler(text="Загрузить рекомендации к товарам", state= '*')
async def description(message: types.Message, state: FSMContext):
    await message.reply("Вам необходимо прислать файл «рекомендации к товарам» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)
    await LoadFiles.excel_file.set()



@dp.message_handler(state=LoadFiles.excel_file, content_types=types.ContentTypes.DOCUMENT)
async def fname_step(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await other_utils.create_dir(str(user_id))
    
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    destination = settings.DATA_STORAGE + user_id + "/" +file_path.split('/')[-1]
    await bot.download_file(file_path, destination)
    print('Done!')
    dataspace.ManageUsers().load_recomendations(user_id, destination)
    await state.finish()
    await message.reply('Готово!', reply_markup=main_kb)



@dp.message_handler(text="Загрузить список товаров", state='*')
async def description(message: types.Message, state: FSMContext):
    await message.reply("Вам необходимо прислать файл «список товаров» в формате .xlsx, как сформировать такой файл можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)
    await LoadFiles.recs_file.set()


@dp.message_handler(state=LoadFiles.recs_file, content_types=types.ContentTypes.DOCUMENT)
async def fname_step(message: types.Message, state: FSMContext):
    user_id = str(message.from_user.id)
    await other_utils.create_dir(str(user_id))
    await state.finish()
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    destination = settings.DATA_STORAGE + user_id + "/" +file_path.split('/')[-1]
    await bot.download_file(file_path, destination)
    print('Done!')
    dataspace.ManageUsers().load_list_of_products(user_id, destination)
    
    await message.reply('Готово!', reply_markup=main_kb)


@dp.message_handler(text="Загрузить id company", state='*')
async def description(message: types.Message):
    await message.reply("Вам необходимо прислать company id, как его получить можете посмотреть в предыдущем меню, нажав на кнопку инструкция", reply_markup=return_kb)
    await LoadFiles.cid.set()


@dp.message_handler(state=LoadFiles.cid, content_types=types.ContentTypes.TEXT)
async def fname_step(message: types.Message, state: FSMContext):
    cid = message.text.title()
    user_id = message.from_user.id
    await state.finish() 
    dataspace.ManageUsers().load_cid(user_id, cid)
    await message.reply('Готово!', reply_markup=main_kb)