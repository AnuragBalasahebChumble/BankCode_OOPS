import logging
logging.basicConfig(filename="dictVersion3.log", level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')

# Version 3, using dictionary of accounts

# Bring in all the code from the Account class file

from Account import *

accountDict = {}

nextAccountNumber = 0

# Create two Accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber

accountDict[joesAccountNumber] = oAccount # Adding key value pair to dictionary
logging.info(f"Joes Account number is {joesAccountNumber}")

nextAccountNumber += 1 # increasing the counter value

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountDict[marysAccountNumber] = oAccount # Adding key value pair to dictionary
nextAccountNumber = nextAccountNumber + 1

logging.info(f"Account number of mary is {marysAccountNumber}")

logging.info(accountDict[joesAccountNumber].show())

logging.info(accountDict[marysAccountNumber].show())

# call methods on the different accounts

print('Calling methods of the two accounts.....')

accountDict[joesAccountNumber].deposit(50, 'JoesPassword')
accountDict[marysAccountNumber].withdraw(345, 'MarysPassword')
accountDict[marysAccountNumber].deposit(100, 'MarysPassword')

# Show the accounts

accountDict[joesAccountNumber].show()
accountDict[marysAccountNumber].show()

# create another account with information from user
print()

userName = input('usrName: ')
userBalance = input('usrBalance: ')
userBalance = int(userBalance)
userPassword = input('Passwrd: ')
oAccount = Account(userName, userBalance, userPassword)

newAccountNumber = nextAccountNumber
accountDict[newAccountNumber] = oAccount
print(f'Account number of new account is {newAccountNumber}')

nextAccountNumber += 1

# show the newly created user account

accountDict[newAccountNumber].show()

# Let's deposit 100 in to the new account

accountDict[newAccountNumber].deposit(100, userPassword)
userBalance = accountDict[newAccountNumber].getBalance(userPassword)
print()
print(f"After depositing 100, the user's balance is: {userBalance}")

# show the new account

accountDict[newAccountNumber].show()


















