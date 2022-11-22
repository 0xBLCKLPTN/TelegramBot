#from db import db
#from models.models import Admins, Users
import unittest
from utils import validator
#session = db.create_database()

class TestValidator(unittest.TestCase):
    def test_name(self):
        name = 'Аргустян Валерий Ебанович'
        self.assertEqual(validator.check_name(name), True)
    
    def test_email(self):
        email = 'blcklptn@gmail.com'
        self.assertEqual(validator.check_email(email), True)