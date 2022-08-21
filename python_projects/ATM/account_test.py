from unittest import TestCase
from atm_account import Account

class TestAccount(TestCase):
    def setUp(self):
        self.b=Account()
        
    def test_deposit(self):
        self.b.deposit(2000)
        self.assertTrue(2000,self.b.balance())

    def test_withdraw(self):
        self.b.withdraw(1000)
        self.b.deposit(3000)
        self.b.withdraw(1000)
        self.assertTrue(1000,self.b.balance())