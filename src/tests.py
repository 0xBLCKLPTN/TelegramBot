import unittest
from utils import validator
from utils import dataspace

class TestValidator(unittest.TestCase):
    def test_name(self):
        name = 'Аргустян Валерий Ебанович'
        self.assertEqual(validator.check_name(name), True)
    
    def test_email(self):
        email = 'blcklptn@gmail.com'
        self.assertEqual(validator.check_email(email), True)

    def test_revenue(self):
        revenue = '123'
        self.assertEqual(validator.check_revenue(revenue), False)

