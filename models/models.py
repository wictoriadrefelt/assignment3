
class Bank:

    """
    Creates a bank object that holds name of bank and list of bank accounts.
    Allows a customer to create an account with the bank.
    """

    def __init__(self, name_of_bank):
        self.name_of_bank = name_of_bank
        self.bank_accounts = []

    def search(self):
        firstname = input('Enter first name of account holder: ')
        lastname = input('Enter last name of account holder: ')
        for acc in self.bank_accounts:
            if acc.first_name == firstname and acc.last_name == lastname:
                print(f"Account holder with name {firstname} {lastname} was found in system")
            else:
                print(f'No account holder with name {firstname} {lastname} was found')

    def create_account(self):
        first_name = input('Enter first name')
        last_name = input('Enter last name')
        user = BankAccount(first_name, last_name)
        self.bank_accounts.append(user)
        print(f'Account for {first_name} {last_name} was sucessfully created')


class User:

    """
    Only structure for what object user will consist of.
    Object is not initalized here as a User never exists without a
    bank account.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = self


class BankAccount(User):

    """
    Inherits from class User.
    """

    def __init__(self, first_name, last_name, balance=0, currency="$"):
        super().__init__(first_name, last_name)
        self.balance = balance
        self.currency = currency

    def deposit(self):

        """
        Asks for user input to make a deposit
        """

        amount = input('How much would you like to deposit? Enter amount: ')
        self.balance = self.balance + int(amount)
        print("Balance for bank account has been updated. Current balance is: ", self.balance, self.currency)

    def withdraw(self):

        """
        Asks for user input to make a withdrawl. Checks if balance is
        great enough to go through with transaction.
        """

        amount = input('How much would you like to withdraw? Enter amount: ')
        if int(amount) > self.balance:
            print(f"Your balance is too low. Current balance is {self.balance}")
        else:
            self.balance = self.balance - int(amount)
            print(f" Withdraw of {amount} {self.currency} successful! Updated balance is {self.balance} {self.currency}")

