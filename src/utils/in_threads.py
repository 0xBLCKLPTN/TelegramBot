from threading import Thread
from time import sleep
from datetime import datetime, timedelta
from core import config
from utils import dataspace
from utils.ozon import refactor_logic
import asyncio
from dispatcher import bot
#rf_class = refactor_logic() # инициализация обьекта

class Subscriber:
    def check(self):
        while True:
            sleep(4)
            payers = dataspace.ManageUsers().get_all_payers()
            if payers != None:
                for user in payers:
                    if user.last_buy > datetime.utcnow():
                        #asyncio.run(rf_class.get_new_reviews_bot(user.user_id))
                        pass
                    else:
                        #return user # user - это объект, который мы возвращаем 
                        print(user.last_buy, datetime.utcnow())
                        print(f"У пользователя {user.user_id} закончилась подписка")
                        dataspace.ManageUsers().set_sub_end(user.user_id)  # Устанавливаем подписку пользователя на None, тк она закончилась
            sleep(1)


async def test():
    while True:
        payers = dataspace.ManageUsers().get_all_payers()
        if payers != None:
            for user in payers:
                if user.last_buy > datetime.utcnow():
                    await refactor_logic.GetReviews().get_new_reviews_bot(user.user_id, str(user.company_id), user.cookies_file, user.list_of_products_file, user.recomendations_file)
        print('Sleeps for n seconds!')
        await asyncio.sleep(config.START_BOT)

            
def start_async_func():
    print('here!')
    asyncio.run_coroutine_threadsafe(test(), config.loop)


def start_threads():
    print('now')
    sc = Subscriber()

    th1 = Thread(target=sc.check)
    #th2 = Thread(target=start_async_func)

    th1.start()
    #th2.start()
