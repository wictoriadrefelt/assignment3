

amount = 0
customerNames = []
customerPins = []
customerBalances = [0]
deposition = 0
withdrawal = 0
balance = 0
transactions = []
counter_11 = 1
counter_22 = 1
i = 0




def dummy_customer():
    """
    creates a dummy customer before we create out own.
    """
    dummy_name = 'John Doe'
    dummy_pin = '111'
    dummy_balance = 0
    customerNames.append(dummy_name)
    customerPins.append(dummy_pin)
    customerBalances.append(dummy_balance)
    return customerNames, customerPins, customerBalances


def create_account():
    """
    function to let a customer create a bank account through input.

    """
    dummy_customer()
    name = input("Input your name to create an account : ")
    customerNames.append(name)
    pin = str(input("Please input a pin of your choice : "))
    customerPins.append(pin)
    balance = 0
    deposition = eval(input("Please input a value to deposit to start an account : "))
    balance = balance + deposition
    customerBalances.append(balance)
    print(f"Name of account holder: {name} ")
    print(f"Your personal pin: {pin} ")
    print("Account balance=", end=" ")
    print(customerBalances[-1], end=" ")
    print("$")
    print(f"Thank you {name}, your account was successfully created")
    print(customerNames)


def search_account_holder():
    """
    function to allow bank to search for account holder by typing in first and last name.
    Runs until j = 1 which is set when either customer is found or bank chooses to stop search.
    """
    j = 0
    while j < 1:
        name = input("Please input name to search for: ")

        if name in customerNames:
            print(f'Customer {name} was found in system')
            j = j + 1

        else:
            print(f'The search for customer {name} gave no result')
            choice = input('would you like to try another name? y/n')
            if choice == "y":
                j = 0
            else:
                print('Thank you for using the service')


def deposit_money():
    """
    function to allow account holder to make a deposit to account.
    Updates previous balance from before.

    """
    n = 0
    while n < 1:
        k = -1
        name = input("Please input your full-name : ")
        pin = input("Pin required. Please enter your pin : ")
        while k < len(customerNames) - 1:
            k = k + 1
            if name == customerNames[k]:
                if pin == customerPins[k]:
                    n = n + 1
                    print(f"Your Current Balance: {customerBalances[k]}$")
                    balance = (customerBalances[k])
                    deposition = eval(input("Enter the value you want to deposit : "))
                    balance = balance + deposition
                    customerBalances[k] = balance
                    print(f"Deposit successful. Your New Balance: {balance}$")

        if n < 1:
            print("Wrong pin entered. Please try again\n")
            retry = input('Retry? y/n: ')
            if retry == 'y':
                n = 0
            else:
                print('Have a good day. Thank you for using our services')
                n = 1


def main():
    create_account()
    search_account_holder()
    deposit_money()


if __name__ == '__main__':
    main()
