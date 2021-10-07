from models.models import Bank


def main():
    bank = Bank('Bank of America')
    bank.create_account()

    bank.bank_accounts[0].deposit()
    bank.bank_accounts[0].withdraw()
    bank.search()


if __name__ == '__main__':
    main()
