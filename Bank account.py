class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)

account = BankAccount("Satvika", 1000)

account.deposit(500)
account.show_balance()