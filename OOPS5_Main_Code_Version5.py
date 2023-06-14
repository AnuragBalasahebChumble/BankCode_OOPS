# Main program for controlling a bank made up of Accounts.

# Bring in all the code of the Bank Class

from BankkOOP5_SeparateBankClass import *

# create an instance of Bank
oBank = Bank()

# Main Code
# Create two test account

joesAccountNumber = oBank.createAccount('Joe', 100, 'JoesPassword')
print(f"Joe's account number is {joesAccountNumber}")

marysAccountNumber = oBank.createAccount('Mary', 12345, 'MarysPassword')
print(f"Marys account number is {marysAccountNumber}")

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('TO make deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')


    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]

    if action == 'b':
        oBank.balance()

    elif action == 'c':
        oBank.closeAccount()

    elif action == 'd':
        oBank.deposit()

    elif action == 'o':
        oBank.openAccount()

    elif action == 's':
        oBank.show()

    elif action == 'q':
        break

    elif action == 'w':
        oBank.withdraw()

    else:
        print('Sorry, that was not valid action PLease try again')

print('done')