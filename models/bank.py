import datetime
import pytz

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        #self.account_holder = first
        #self.account_number = account_number


    def create_account(self):
        new_account = Bank(self.name)
        x = [new_account for ac in self.accounts]
        self.accounts.append(new_account)
        print(f'Account was created for {self.name}')


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []

    def __repr__(self):
        return f'User("{self.first_name}","{self.last_name}",{self.accounts})'

    def create_account(self):
        first_name = input('Enter your first name')
        last_name = input('Enter your last name')
        new_bankholder = first_name, last_name
        self.accounts.append(new_bankholder)
        print(f'Account created for {first_name}, {last_name}')
        print(self.account)

    def account(self):
        return self.account


class BankAccount:
    @staticmethod
    def _show_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, amount: float, currency: str,
                 opening_balance: float = 0.0):
        self.amount = amount
        self.currency = currency
        self._balance = opening_balance
        self.transactions = []
        self.account = []
        ban = self.account.append(BankAccount)


    def deposit(self, amount: float):
        if amount > 0.0:
            self._balance += amount
            self.show_balance()
            self.transactions.append((BankAccount._show_time(), amount))
            print(f"Amount Deposited:{amount}")
        return self._balance


    def withdraw(self, amount:float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f'Amount withdrawn:{amount}')
        else:
            print('Not enough funds to make this withdrawl')

    def show_balance(self):
        print(f'Balance on account is {self._balance}')

    def show_transactions(self):
        for date, amount in self.transactions:
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = 'withdraw'
                amount += -1
            print(f'{amount}, {trans_type}, local time {date}')

