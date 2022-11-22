from db import db
from models.models import Admins, Users
from sqlalchemy.exc import NoResultFound

session = db.create_database()

class ManageAdmins:
    def remove_admin(self):
        pass

    def add_admin(self):
        pass

    def check_admin(self, user_id) -> bool:
        try:
            record = session.query(Admins).filter(Admins.user_id == user_id).one()
            return True

        except NoResultFound:
            return False


class ManageUsers:
    def add_user(self, user: Users):
        pass

    def check_user(self, user_id: int) -> bool:
        try:
            record = session.query(Users).filter(Users.user_id == user_id).one()
            return True
        except NoResultFound:
            return False



