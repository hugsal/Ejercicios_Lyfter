class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
        super().__init__()

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print("This transaction exceeds the minimum amount")
        else:
            super().withdraw(amount)


account = SavingsAccount(500)
account.deposit(1000)
account.withdraw(400)
account.withdraw(300)
print(account.balance)
