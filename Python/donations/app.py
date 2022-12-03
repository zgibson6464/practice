from donations_pkg import homepage, user

database = {'admin': 'password123'}
donations = []
authorized_user = ''
total = 0

homepage.show_homepage()
if authorized_user == '':
    print('You must be logged in to donate.')
elif authorized_user != '':
    print(f'Logged in as: {authorized_user}')

while True:
    choice = input('Choose an option: ')
    homepage.show_homepage()
    if choice == '1':
        username = input('Enter Username: ')
        password = input('Enter your Password: ')
        authorized_user = user.login(database, username, password)
    elif choice == '2':
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        authorized_user = user.register(database, username)
        if username and password != '':
            database[username] = password
    elif choice == '3':
        if authorized_user == '':
            print('You are not logged in.')
        else:
            donation_string = homepage.donate(authorized_user)
            # donate_amt = homepage.donate(authorized_user)
            # total += donate_amt
            donations.append(donation_string)
    elif choice == '4':
        homepage.show_donations(donations)
    elif choice == '5':
        print('Goodbye')
        break
