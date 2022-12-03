def show_homepage():
    print('       === DonateMe Homepage ===       ')
    print('---------------------------------------')
    print('| 1.   Login       | 2.   Register     |')
    print('---------------------------------------')
    print('| 3. Donate        | 4. Show Donations |')
    print('---------------------------------------')
    print('|               5. Exit                |')
    print('---------------------------------------')


def donate(username):
    while True:
        try:
            donate_amt = int(input('Enter amount to donate: '))
            if donate_amt <= 0:
                print('Invalid amount.')
            else:
                donation_string = f'{username} donated ${donate_amt}'
                print('Thank you for donating!')
                return donation_string
        except ValueError:
            print('Invalid input')


def show_donations(donations):
    print('\n--- All Donations---')
    if donations == '':
        print('Currently, there are no donations.')
    else:
        for donation in donations:
            print(donation)
        # print(f'Total: ${total}')
