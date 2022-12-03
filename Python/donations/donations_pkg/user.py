def login(database, username, password):
    if (username in database) and (password == database[username]):
        print(f'Welcome {username}')
        return username
    elif username not in database:
        print('Could not find user, please try again')
        return ''
    elif (username in database) and (password != database[username]):
        print('Password does not match, please try again.')
        return ''


def register(database, username):
    if username in database:
        print('Username already registered')
        return ''
    else:
        print(f'{username} has been registered')
        return username
