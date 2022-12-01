from threading import Thread
from time import sleep
from datetime import datetime, timedelta
from core import config
from utils import dataspace
from utils.ozon import refactor_logic
import asyncio

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
                        """
                        из user можно вытащить все атрибуты, которые есть в models/models.py/Users:
                        - user.username
                        - user.user_id
                        - user.FirstName
                        - user.MiddleName
                        - user.LastName
                        - user.phone_number
                        - user.email
                        ...
                        и так далее.
                        полный список можно посмотреть в файле models.py и классе Users
                        """

                        #return user # user - это объект, который мы возвращаем 
                        print(user.last_buy, datetime.utcnow())
                        print(f"У пользователя {user.user_id} закончилась подписка")
                        dataspace.ManageUsers().set_sub_end(user.user_id)  # Устанавливаем подписку пользователя на None, тк она закончилась
            sleep(1)



class BotTime:
    def check(self):
        while True:
            sleep(config.START_BOT)
            
            

def start_threads():
    sc = Subscriber()
    bt = BotTime()

    th1 = Thread(target=sc.check)
    th2 = Thread(target=bt.check)

    th1.start()
    th2.start()
