import os
from core.config import settings

async def create_dir(user_id: str):
    if user_id not in os.listdir(settings.DATA_STORAGE):
        os.mkdir(settings.DATA_STORAGE + str(user_id))

async def remove_old_json(user_id: str, ext: str):
    try:
        if user_id in os.listdir(settings.DATA_STORAGE):
            for i in os.listdir(settings.DATA_STORAGE + user_id):
                if i.split('.')[-1] == ext:
                    os.remove(settings.DATA_STORAGE + user_id + '/' + i)
    except:
        pass
