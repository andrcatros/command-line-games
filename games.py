# this is a series of command line games

import random


# guess the number game
def number_game():
    secret_number = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    guess = int(input())
    tries = 1
    while tries <= 6:
        if guess > secret_number:
            print('Your guess is too high.')
            guess = int(input())
            tries += 1
        elif guess < secret_number:
            print('Your guess is too low')
            guess = int(input())
            tries += 1
        else:
            print('Good job! You guessed correctly in ' + str(tries) + ' tries.')
            return rematch()

    print('You are out of guesses! The number I was thinking of was ' + str(secret_number) + '.')
    return rematch()



# game choice function
def choose_game():
    print('[1] Guess the number [2] Tic tac toe [3] Hangman')
    choice = int(input())
    if choice == 1:
        number_game()
    else:
        print('Please input a valid number.')
        choose_game()


# rematch function
def rematch():
    print('Would you like to play another game? [y/n]')
    answer = input()
    if answer == 'y':
        choose_game()
    else:
        print('No worries. See you again next time.')


# game preamble
def preamble():
    print('Hello. What is your name?')
    name = input()
    print('Welcome ' + name + '! What game would you like to play?')
    choose_game()


# initialise the game
preamble()
