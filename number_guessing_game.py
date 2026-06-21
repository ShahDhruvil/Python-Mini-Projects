import random

random_number = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        if guess > random_number:
            print('Too high')
        elif guess < random_number:
            print('Too low')
        else:
            print('Correct')
            break

    except ValueError:
        print('Please enter a valid number')

