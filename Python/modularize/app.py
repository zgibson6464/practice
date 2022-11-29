from banking_pkg import account
from banking_pkg import user


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = user.validate_register()
pin = user.validate_pin()
balance = 0
print(f'{name} has been registered with a starting balance of ${str(balance)}')

while True:
    print('LOGIN')
    name_to_validate = input('Enter your name: ')
    pin_to_validate = input('Enter your PIN: ')
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
        break
    else:
        print('Invalid credentials!')

while True:
    atm_menu(name)
    option = input('Choose an option: ')
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == '3':
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == '4':
        account.logout(name)
        break
