class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw that amount ")
        else:
            self.balance -= amount


account = BankAccount(15)
print(f'The balance is {account.balance}')
account.deposit(20)
print(f'The balance is {account.balance}')
account.withdraw(40)
print(f'The balance is {account.balance}')
account.withdraw(25)
print(f'The balance is {account.balance}')
