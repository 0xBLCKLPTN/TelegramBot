from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

circle_settings = KeyboardButton('Настройка цикла запуска')
admin_settings = KeyboardButton('Настройка списка администраторов')
subscriber_settings = KeyboardButton("Настройка цикла подписки")

start_bot = KeyboardButton('Запуск бота')
stop_bot = KeyboardButton('Остановка бота')

admin_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(circle_settings, admin_settings, subscriber_settings, start_bot, stop_bot)

button_return = KeyboardButton("Назад")

back_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(button_return)

admin_add = KeyboardButton('Добавить администратора')
admin_remove = KeyboardButton('Удалить администратора')

admin_settings_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(admin_add, admin_remove, button_return)

inline_btn_1 = InlineKeyboardButton('Подтвердить оплату', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)