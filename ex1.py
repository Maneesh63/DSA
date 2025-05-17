from tkinter.font import names


class Bank:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = 0

    def list(self):
        print("User details:", self.name, self.age)

    def deposit_amount(self, amount):
        if amount < 0:
            print("Amount cant be Negative")

        self.balance += amount
        print("Your amount has been deposited")
        print("Balance is", self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough money to make a withdrawal")

        else:
            self.balance -= amount
            print("Withdrawn amount:", amount)
            print("Balance is", self.balance)

    def balance_check(self):
        print("Checking balance")
        print("Your current balance is:", self.balance)


instance = Bank("John", 20)
instance.deposit_amount(2000)
instance.withdraw(100)








