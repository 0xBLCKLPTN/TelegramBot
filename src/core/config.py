"""
config.py gets your configuration data from the environment.

Written by: Daniil ( blcklptn ) Ermolaev.
"""

from dotenv import load_dotenv 
from pydantic import BaseSettings

load_dotenv() # Initialize your env data.

class Settings(BaseSettings):
    '''
    Base settings for programm.

    Args:
        BaseSettings - pydantic object
    '''
    DB_USERNAME: str  # Username for database
    DB_NAME: str  # Name of database
    DB_PASSWORD: str  # Database password
    TDB_PORT: str  # Database port 5432 by default
    TDB_HOST: str  # Database host. localhost by default
    DB_HOST: str
    DB_PORT: str
    BOT_TOKEN: str  # Telegram bot token
    DATA_STORAGE: str  # Path to data_storage
    INSTRUCTIONS_FILE: str  # Path to instructions
    CARD_NUMBER: str
    PRICE: str

    TEST_COMPANY_ID: str

Bot_on = True  # The bot is run by defaultю
START_LOOP = 200  # Subscription duration
START_BOT = 20  # Every n times bot will stop

settings = Settings()  # Initalizing this class object.