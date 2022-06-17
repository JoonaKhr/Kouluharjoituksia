import csv
from datetime import datetime

class BankAccount():
    service_fee = 7

    def __init__(self, owner, balance, account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    @classmethod
    def set_service_fee(cls, amount):
        cls.service_fee = amount

    def set_owner(self, new_owner):
        self.owner = new_owner

    def set_balance(self, new_balance):
        self.balance = new_balance

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

    @classmethod
    def from_csv(cls, filename):
        with open(filename, "r", encoding="utf8") as f:
            #row = next(csv.reader(f))
            row = csv.reader(f).__next__()
            owner, account_number, balance = row
            return cls(owner, int(balance), account_number)

    @staticmethod
    def get_date():
        print(datetime.now())

    # Print olio hakee nyt tämän
    def __str__(self):
        return f"""
                Bank Account:
                Owner: {self.owner}
                Balance: {self.balance}
                """
    # Tarkoitus antaa suuntaa muille ohjelmoijille
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}' balance={self.balance})"

# Kannattaa tehdä staattisia metodeita asioista mitä kokee tarvitsevan usein
class Utilities:
    @staticmethod
    # 5/5 esimerkki Kallelta, kun ei keksinyt parempaa
    def add(x,y):
        print(x+y)

Utilities.add(5, 2)

BankAccount.get_date()
myAccount = BankAccount.from_csv(r"S:\koulu\OOP\Kouluharjoituksia\classes\accounts.csv")
print(myAccount)