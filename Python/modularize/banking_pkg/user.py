def validate_register():
    while True:
        name = input('Enter name to register: ')
        if len(name) <= 1 or len(name) >= 10:
            print('Name must be more than 1 character and less than 10 characters')
        else:
            break
    return name


def validate_pin():
    while True:
        pin = input('Enter PIN: ')
        if len(pin) != 4:
            print('Pin must be 4 numbers')
        else:
            break
    return pin
