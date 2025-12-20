class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")

acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(3000)
