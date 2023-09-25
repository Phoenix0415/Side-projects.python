'''
Rock Paper Scissors Game
-------------------------------------------------------------
- A simple game of Rock, Paper, Scissors against the computer.
- The user is prompted to choose a weapon: Rock, Paper, or Scissors.
- The computer randomly selects its weapon.
- The winner is determined based on traditional Rock, Paper, Scissors rules.
- The user has the option to play again or exit the game.
'''

import random
import os
import re

def check_play_status():
    '''
    This function checks if the user wants to play again or exit the game.
    It keeps prompting the user until a valid response is provided.
    '''
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)

def play_rps():
    '''
    The main function to play the Rock, Paper, Scissors game.
    The user's and computer's choices are compared and the winner is determined.
    The game continues as long as the user wants to play again.
    '''
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print('')
        print('Rock, Paper, Scissors - Shoot!')

        # Prompt the user to choose a weapon
        user_choice = input('Choose your weapon'
                            ' [R]ock], [P]aper, or [S]cissors: ')

        # Validate the user's choice
        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        print(f'You chose: {user_choice}')

        choices = ['R', 'P', 'S']  # List of possible weapons
        opp_choice = random.choice(choices)  # Randomly choose a weapon for the computer

        print(f'I chose: {opp_choice}')

        # Determine the winner
        if opp_choice == user_choice.upper():
            print('Tie!')
            play = check_play_status()
        elif opp_choice == 'R' and user_choice.upper() == 'S':
            print('Rock beats scissors, I win!')
            play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'P':
            print('Scissors beats paper! I win!')
            play = check_play_status()
        elif opp_choice == 'P' and user_choice.upper() == 'R':
            print('Paper beats rock, I win!')
            play = check_play_status()
        else:
            print('You win!\n')
            play = check_play_status()

if __name__ == '__main__':
    '''
    The entry point of the program.
    Calls the function to start the Rock, Paper, Scissors game.
    '''
    play_rps()
