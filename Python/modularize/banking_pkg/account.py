def show_balance(balance):
    # Show balance function
    print(f'Your balance is {format_currency(balance)}')


def deposit(balance):
    # Deposit amount function
    amount = input('Enter amount to deposit: ')
    balance += float(amount)
    return balance


def withdraw(balance):
    # Withdraw amount function
    amount = input('Enter amount to withdraw: ')
    balance -= float(amount)
    return balance


def logout(name):
    # Logout function
    print(f'Goodbye {name}')


def format_currency(balance):
    '''
    format float to currency string
    '''
    return f"${balance:,.2f}"
