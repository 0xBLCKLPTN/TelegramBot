from db import db
from models.models import Admins, Users
from sqlalchemy.exc import NoResultFound
from datetime import datetime


session = db.create_database()

class ManageAdmins:
    def remove_admin(self):
        pass

    def add_admin(self, user: Admins):
        session.add(user)
        session.commit()

    def check_admin(self, user_id) -> bool:
        try:
            session.query(Admins).filter(Admins.user_id == user_id).one()
            return True

        except NoResultFound:
            return False


class ManageUsers:
    def add_user(self, user: Users):
        session.add(user)
        session.commit()

    def check_user(self, user_id: int) -> bool:
        try:
            record = session.query(Users).filter(Users.user_id == user_id).one()
            record.execute()
            return True
        except NoResultFound:
            return False

    def get_user(self, user_id: int) -> bool:
        try:
            record = session.query(Users).filter(Users.user_id == user_id).one()
            return record
        except NoResultFound as ex:
            return False

    def new_pay(self, user_id: int):
        session.query(Users).filter(Users.user_id == user_id).update({'last_buy': datetime.utcnow() })
        session.commit()


