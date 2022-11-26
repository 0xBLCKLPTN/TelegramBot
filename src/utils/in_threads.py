from threading import Thread
from time import sleep
from datetime import datetime, timedelta
from core import config
from utils import dataspace

class Subscriber:
    def check(self):
        while True:
            sleep(4)
            payers = dataspace.ManageUsers().get_all_payers()
            if payers != None:
                for user in payers:
                    if user.last_buy > datetime.utcnow():
                        pass # У пользователей еще не закончилась подписка
                    else:
                        print(user.last_buy, datetime.utcnow())
                        print(f"У пользователя {user.user_id} закончилась подписка")
                        dataspace.ManageUsers().set_sub_end(user.user_id)  # Устанавливаем подписку пользователя на None, тк она закончилась
            sleep(1)


class BotTime:
    def __init__(self):
        self.seconds = config.START_BOT
        self.need_s = datetime.now() + timedelta(seconds=self.seconds)
    def check(self):
        while True:
            
            if self.seconds != config.START_BOT:
                self.seconds = config.START_BOT
                self.need_s = datetime.now() + timedelta(seconds=self.seconds)
            
            if datetime.now() >= self.need_s:
                pass

                self.need_s = datetime.now() + timedelta(seconds=self.seconds)
            sleep(1)
        


def start_threads():
    sc = Subscriber()
    bt = BotTime()

    th1 = Thread(target=sc.check)
    th2 = Thread(target=bt.check)

    th1.start()
    th2.start()