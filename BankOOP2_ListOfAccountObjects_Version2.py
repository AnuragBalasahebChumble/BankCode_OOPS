import logging
logging.basicConfig(filename="list.Version1.logs", level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')

"""
In this version of the test code, we'll start with an empty list of Account objects.
Every tie user opens Account, we'll instantiate an Account object and append the resulting object
onto our list.
The Account number for any given Account will be the Index of the Account in the list, starting with 0.
"""

# Bring all the code from the Account class file.

from Account import *

# starts off with an empty list of accounts
accountsList = []

# Create two accounts
oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's Account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's Account number is 1")

accountsList[0].show()
accountsList[1].show()
print()

# Call some methods on the different accounts

print('Calling methods on the different accounts ....')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'marysPassword')

# Show the accounts
accountsList[0].show()
accountsList[1].show()

# create another account from information from the user
print()

userName = input("UsrName: ")
userBalance = input("UsrBalance: ")
userBalance = int(userBalance)
userPassword = input("UsrPassword: ")
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

# show newly created user Account
print("Created new account, account number is 2")
accountsList[2].show()

# Let's deposit 100 into the new account

accountsList[2].deposit(100, userPassword)
userBalance = accountsList[2].getBalance(userPassword)
print()
print(f"after depositing 100 the user's balance is: {userBalance}")

# Show the new Account
accountsList[2].show()



"""
- Now we are using only the single global variable accountList
- We have taken important steps in reducing the number of global variable
- As each object acts as a global variable. Here we are accessing object via list.
- If we assume code of Account class takes care of details related to an individual 
account, we can concentrate on ways to make the main code better.
"""


