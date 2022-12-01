from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_reg = KeyboardButton("Регистрация")
button_price = KeyboardButton("Расценки")
button_description = KeyboardButton("Описание")

start_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_reg, button_price, button_description)


button_return = KeyboardButton("Вернуться")

return_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_return)

button_pay = KeyboardButton("Оплата")
button_instruction = KeyboardButton("Инструкция по настройке")
button_cookies = KeyboardButton("Загрузить cookies")
button_id_company = KeyboardButton("Загрузить id company")
button_recomendation = KeyboardButton("Загрузить рекомендации к товарам")
button_list = KeyboardButton("Загрузить список товаров")
button_questions = KeyboardButton("Вопросы и пожелания")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_pay, button_instruction, button_cookies, button_id_company, button_recomendation, button_list, button_questions)