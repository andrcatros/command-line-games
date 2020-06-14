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


# tic tac toe
def tic_tac_toe():
    board = {'Top-L': ' ', 'Top-M': ' ', 'Top-R': ' ',
             'Mid-L': ' ', 'Mid-M': ' ', 'Mid-R': ' ',
             'Bottom-L': ' ', 'Bottom-M': ' ', 'Bottom-R': ' '}

    def generate_board():
        print(board['Top-L'], '|', board['Top-M'], '|', board['Top-R'])
        print(board['Mid-L'], '|', board['Mid-M'], '|', board['Mid-R'])
        print(board['Bottom-L'], '|', board['Bottom-M'], "|", board['Bottom-R'])

    def validate_choice(choice):
        if choice in board.keys():
            board[choice] = 'X'
        else:
            print('Please pick a valid code!')

    def computer_play():
        print('My turn now :)')
        turn = 0

        if turn == 0:
            if board['Top-L'] == ' ':
                board['Top-L'] = 'O'
            else:
                board['Top-R'] = 'O'
            turn += 1
        elif turn == 1:
            if board['Mid-M'] == ' ':
                board['Mid-M'] = 'O'
            else:
                board['Bottom-R'] = 'O'
                turn += 1
        else:
            print("Game over :(")

        generate_board()

    def play():
        print('Make your choice.')
        choice = input()
        validate_choice(choice)
        generate_board()
        computer_play()


    def play_preamble():
        print('I\'ll let you make the first move.')
        generate_board()
        print('Choose where to place an X by typing one of the following codes, each corresponding to one square on '
              'the board: [Top-L], [Top-M], [Top-R], [Mid-L], [Mid-M], [Mid-R], [Bottom-L], [Bottom-M] OR [Bottom-R]')
        play()

    play_preamble()


# game choice function
def choose_game():
    print('[1] Guess the number [2] Tic tac toe [3] Hangman')
    choice = int(input())
    if choice == 1:
        number_game()
    elif choice == 2:
        tic_tac_toe()
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
