from db import db
from models.models import Admins, Users

session = db.create_database()

class ManageAdmins:
    def remove_admin(self):
        pass

    def add_admin(self):
        pass

class Registration:
    def add_user(self, user: Users):
        pass
    

