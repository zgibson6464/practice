import random

# credit to Kyle Ying


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    number_of_guesses = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        number_of_guesses += 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(
        f'Congrats! You have guessed the number {random_number} correctly.\nIt took you {number_of_guesses} guesses to get it right.')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too High (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number {guess}, correctly.')


computer_guess(5000)
