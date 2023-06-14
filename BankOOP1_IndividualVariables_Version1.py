import logging
logging.basicConfig(filename="globalVariableVersion1.logs", level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')


# Test program using accounts
# Version 1, using explicit variables for each Account Object
# Bringing all the code from the Account Class File



from Account import *

# create two accounts

oJoesAccount = Account('Joe', 100, 'JoesPassword')
logging.info("Created Account for Joe")

oMarysAccount = Account('Mary', 12345, 'Maryspassword')
logging.info("Created Account for Mary")

oJoesAccount.show()
oMarysAccount.show()

# call some methods on the different accounts
print('Calling methods of the two accounts  ....')

oJoesAccount.deposit(50, 'JoesPassword')
oMarysAccount.withdraw(345, 'MarysPassword')
oMarysAccount.deposit(100, 'MarysPassword')

# Show the accounts

oJoesAccount.show()
oMarysAccount.show()

#create another acccount with information from the user

userName = input('Name for the new user Account: ')
userBalance = input('What is the starting balance for this account: ')
userBalance = int(userBalance)
userPassword = input("What is the password you want to use for this account: ")
oNewAccount = Account(userName, userBalance, userPassword)

# Show the newly created user Account
oNewAccount.show()

# let's deposit 100 into the new Account

oNewAccount.deposit(100, userPassword)
usersBalance = oNewAccount.getBalance(userPassword)
print()

print(f"After depositing 100 the user's balance is {usersBalance}")

# Show the newAccount

oNewAccount.show()


