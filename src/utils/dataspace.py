from db import db
from models.models import Admins, Users
from sqlalchemy.exc import NoResultFound
from datetime import datetime, timedelta
from core import config
session = db.create_database()

class ManageAdmins:

    def set_default_admin(self):
        try:
            qw = Admins(user_id = 123)
            session.add(qw)
        except:
            pass
    def remove_admin(self, user_id: int):
        try:
            asd = session.query(Admins).filter(Admins.user_id == user_id).one()
            session.delete(asd)
            session.commit()
        except:
            pass

    def add_admin(self, user: Admins):
        try:
            session.add(user)
            session.commit()
        except:
            pass

    def check_admin(self, user_id) -> bool:
        try:
            session.query(Admins).filter(Admins.user_id == user_id).one()
            return True

        except NoResultFound:
            return False
    
    def get_all_admins(self) -> list:
        record = session.query(Admins).all()
        return record


class ManageUsers:
    def add_user(self, user: Users):
        session.add(user)
        session.commit()

    def check_user(self, user_id: int) -> bool:
        try:
            record = session.query(Users).filter(Users.user_id == user_id).one()
            #record.execute()
            return True
        except NoResultFound:
            return False

    def get_user(self, user_id: int) -> bool:
        try:
            record = session.query(Users).filter(Users.user_id == user_id).one()
            return record
        except NoResultFound as ex:
            return False

    def new_pay(self, user_id: str):
        dt = datetime.utcnow() + timedelta(seconds=config.START_LOOP)
        session.query(Users).filter(Users.user_id == user_id).update({'last_buy': dt})
        session.commit()

    def load_cookies(self, user_id: int, dest):
        try:
            session.query(Users).filter(Users.user_id == user_id).update({'cookies_file': dest})
            session.commit()
        except:
            pass

    def load_recomendations(self, user_id: int, dest):
        try:
            session.query(Users).filter(Users.user_id == user_id).update({'recomendations_file': dest})
            session.commit()
        except:
            pass
    
    def load_list_of_products(self, user_id: str, dest):
        # Загрузить файл списка продуктов
        try:
            session.query(Users).filter(Users.user_id == user_id).update({'list_of_products_file': dest})
            session.commit()
        except:
            pass
    
    def load_cid(self, user_id: str, cid: str):
        # Обновить company_id у пользователя с user_id
        try:
            session.query(Users).filter(Users.user_id == user_id).update({'company_id': cid})
            session.commit()
        except:
            pass
    
    def get_all_payers(self) -> None:
        # Получить всех пользователей у которых есть подписка
        try:
            record = session.query(Users).filter(Users.last_buy != None).all()
            return record
        except:
            pass
    

    
    def set_sub_end(self, user_id: str) -> None:
        # Если заходите поставить last_buy пользователя, у которого законичилась подписка на None.
        try:
            session.query(Users).filter(Users.user_id == user_id).update({'last_buy': None })
            session.commit()
        except:
            pass

