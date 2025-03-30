import random


def number_predictor():
    number_random = random.randint(1, 100)
    while True:
        user_guess = int(input('Please enter an integer between 1 and 100'))
        if user_guess == number_random:
            print('Congratulations! You have guessed the right number!')
            break
        elif user_guess > number_random:
            print('The number guessed is too high!')
        elif user_guess < number_random:
            print('The number guessed is too low!')

number_predictor()
