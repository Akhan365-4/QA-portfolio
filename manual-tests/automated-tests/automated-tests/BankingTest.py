import pytest

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw():
    account = BankAccount(200)
    account.withdraw(50)
    assert account.balance == 150
