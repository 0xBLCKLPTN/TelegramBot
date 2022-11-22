from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: str
    DB_HOST: str
    

settings = Settings()