class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Bad Password')
            return None
        if amountToDeposit < 0:
            print('Amount should be positive')

        self.balance = self.balance + amountToDeposit
        return self.balance

    def withdraw(self, amounntToWithDraw, password):
        if password != self.password:
            print("Bad Password")
            return None
        if amounntToWithDraw < 0:
            print("ENter positive amount")
            return None
        if amounntToWithDraw > self.balance:
            print("More than balance amount is requested")
            return None
        self.balance = self.balance - amounntToWithDraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Bad Password")
            return None
        return self.balance

    def show(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Password: {self.password}")
        