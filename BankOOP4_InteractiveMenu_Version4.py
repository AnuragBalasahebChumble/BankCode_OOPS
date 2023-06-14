import logging
logging.basicConfig(filename="dictVersion4.log", level=logging.INFO,
                    format='%(levelname)s: %(asctime)s: %(message)s')

from Account import *

accountDict = {}

nextAccountNumber = 0

# Create two Accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber

accountDict[joesAccountNumber] = oAccount # Adding key value pair to dictionary
logging.info(f"Joes Account number is {joesAccountNumber}")

nextAccountNumber += 1  # increasing the counter value

oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountDict[marysAccountNumber] = oAccount  # Adding key value pair to dictionary
nextAccountNumber = nextAccountNumber + 1

logging.info(f"Account number of mary is {marysAccountNumber}")

while True:
    print()
    print('Press b to get the balance')
    print('Press d to get the deposit')
    print('Press o to open new account')
    print('Press w to make a withdraw')
    print('Press s to show all accounts')
    print('Press q to quit')
    print()


    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]

    if action == 'b':
        print('Get Balance')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the passwd: ")
        oAccount = accountDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')

    elif action == 'd':
        print('Deposit')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the passwd: ")
        userDepositAmount = input("Please enter amount to deposit: ")
        oAccount = accountDict[userAccountNumber]
        theBalance = oAccount.deposit(userDepositAmount, userAccountPassword)
        if theBalance is not None:
            print(f'Your balance is: {theBalance}')


    elif action == 'o':
        print('Open Account')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance? ')
        userStartingAmount = int(userStartingAmount)
        userAccountPassword = input("Please enter the Passwd: ")
        oAccount = Account(userName, userStartingAmount, userAccountPassword)
        print(f"Your new Account number is {nextAccountNumber}")
        accountDict[nextAccountNumber] = oAccount
        nextAccountNumber += 1

    elif action == 's':
        print('Show: ')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userAccountPassword = input("Please enter the passwd: ")
        if userAccountNumber in accountDict:
            oAccount = accountDict[userAccountNumber]
            oAccount.show()
        else:
            print("Account not available")
            break

    elif action == 'q':
        break

    elif action == 'w':
        print('WithDraw')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithDrawalAmount = input('Enter the amount to withdraw: ')
        userWithDrawalAmount = int(userWithDrawalAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = accountDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithDrawalAmount, userAccountPassword)
        if theBalance is not None:
            print(f'Withdrew: {userWithDrawalAmount}')
            print(f'Your balance is {theBalance}')
    else:
        print('Not a valid action')
print('Done')