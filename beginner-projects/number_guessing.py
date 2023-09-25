'''
Number Guessing Game:
-------------------------------------------------------------
This program generates a random number between 1 and 10,
and prompts the user to guess the number.
It keeps track of the number of attempts and maintains a
high score (lowest number of attempts to guess correctly).
'''

import random  # Importing the random module for generating random numbers

attempts_list = []  # List to keep track of the number of attempts for each game


def show_score():
    # Function to display the current high score (minimum number of attempts to guess correctly)
    if not attempts_list:  # Checking if the attempts list is empty
        print('There is currently no high score, it\'s yours for the taking!')
    else:
        print(f'The current high score is {min(attempts_list)} attempts')  # Displaying the current high score


def start_game():
    # Main function to control game logic
    attempts = 0  # Counter for number of attempts in current game
    rand_num = random.randint(1, 10)  # Generating a random number between 1 and 10
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()  # Exiting the program if the user doesn't want to play
    else:
        show_score()  # Displaying the high score if the user wants to play

    while wanna_play.lower() == 'yes':
        # Loop to keep the game running as long as the user wants to play
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                # Checking if the guess is within the allowed range
                raise ValueError('Please guess a number within the given range')

            attempts += 1  # Incrementing the attempts counter
            attempts_list.append(attempts)  # Adding the current attempts count to the attempts list

            if guess == rand_num:
                # Checking if the guess is correct
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break  # Exiting the loop if the user doesn't want to play again
                else:
                    attempts = 0  # Resetting the attempts counter for a new game
                    rand_num = random.randint(1, 10)  # Generating a new random number
                    show_score()  # Showing the high score
                    continue  # Continuing to the next game
            else:
                # Giving the user a hint if the guess is wrong
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            # Handling invalid input (non-integer or out-of-range values)
            print('Oh no!, that is not a valid value. Try again...')
            print(err)  # Displaying the error message


if __name__ == '__main__':
    start_game()  # Starting the game when the script is run
