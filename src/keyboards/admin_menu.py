from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

circle_settings = KeyboardButton('Настройка цикла запуска')
admin_settings = KeyboardButton('Настройка списка администраторов')
subscriber_settings = KeyboardButton('Настройки цикла подписки')

start_bot = KeyboardButton('Запуск бота')
stop_bot = KeyboardButton('Остановка бота')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(circle_settings, admin_settings, subscriber_settings, start_bot, stop_bot)