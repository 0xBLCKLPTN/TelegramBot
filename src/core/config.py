from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DB_USERNAME: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str

    BOT_TOKEN: str
    DATA_STORAGE: str
    INSTRUCTIONS_FILE: str
    CARD_NUMBER: str
    PRICE: str

Bot_on = True
START_LOOP = 20 # настройка цикла подписки в секундах
START_BOT = 0

settings = Settings()