from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from core.config import settings


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(bot)

