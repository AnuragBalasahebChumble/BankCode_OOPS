# Bank that manages dictionary of 'Account Objects'


import logging
logging.basicConfig(filename="oop5.logs", level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')


from Account import *

class Bank():
    def __init__(self):
        self.accountDict = {}
        self.nextAccountNumber = 0

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        logging.info(f"new Account is {newAccountNumber} created")
        return newAccountNumber

    def openAccount(self):
        print('Open Account')
        userName = input("Enter usr name: ")
        userStartingAmount = input('What is the starting amount for this account? ')
        userPassword = input("Password: ")
        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print(f"Your new account number is {userAccountNumber}")

    def closeAccount(self):
        print('Close Account')
        userAccountNumber = input('What is your Account number? ')
        userAccountNumber = int(userAccountNumber)
        userPassword = input('What is your Password? ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userPassword)
        if theBalance is not None:
            print(f'You had {theBalance} in your account which is being returned to you.')
            # remove users account from the dictionary of Accounts
            del self.accountDict[userAccountNumber]
            logging.info(f"Account is {userAccountNumber} deleted")
            print('Your account is now closed')

    def balance(self):
        print('Get Balance')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input('Please enter the password')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'You have {theBalance} in your account.')

    def deposit(self):
        print('Deposit')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        depositAmount = int('enter the amount to deposit: ')
        depositAmount = int(depositAmount)
        userAccountPassword = input('Please enter the password')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.deposit(userAccountNumber, userAccountPassword)
        if theBalance is not None:
            print(f'You have {theBalance} in your account.')

    def show(self):
        print('Show')
        for userAccountNumber in self.accountDict:
            oAccount = self.accountDict[userAccountNumber]
            print(f"Account: {userAccountNumber}")
            oAccount.show()


    def withdraw(self):
        print('Withdraw')
        userAccountNumber = input('Please enter your account Number: ')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('PLease enter the password: ')
        oAccount = self.accountDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print(f'Withdrew: {theBalance}')
            print(f'Your new balance is {theBalance}')
