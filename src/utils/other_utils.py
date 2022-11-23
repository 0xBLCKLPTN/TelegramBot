import os
from core.config import settings

async def create_dir(user_id: int):
    os.mkdir(settings.DATA_STORAGE + str(user_id))
