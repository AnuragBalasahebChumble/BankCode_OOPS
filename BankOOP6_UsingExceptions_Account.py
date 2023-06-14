# Account class
# Errors indicated by "raise" statements

# Define a custom exception
class AbortTransaction(Exception):
    """Raise this exception to abort bank transaction"""
    pass

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an Integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def checkPasswordMatch(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')

    def deposit(self, amountToDeposit):
        amountToDeposit = self.validateAmount(amountToDeposit)
        self.balance = self.balance + amountToDeposit
        return self.balance

    def getBalance(self):
        return self.balance

    def withdraw(self, amountToWithdraw):
        amountToWithdraw = self.ValidateAmount(amountToWithdraw)
        if amountToWithdraw > self.balance:
            raise AbortTransaction('Not sufficient funds')
        self.balance = self.balance - amountToWithdraw
        return self.balance

    # Added for debugging

    def show(self):
        print(f'Name: {self.name}')
        print(f"Balance: {self.balance}")
        print(f"Password: {self.password}")

anurag = Account(name='chiku', balance=1, password='chiku@123')
anurag.checkPasswordMatch('chiku')

