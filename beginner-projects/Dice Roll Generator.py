'''
Dice Roll Generator Program:
-------------------------------------------------------------
This program simulates the rolling of one or two dice.
1. The user is asked how many dice they want to roll.
2. The `roll_dice` function is called to initiate the dice rolling process.
3. Inside the function:
    - A while loop continues the dice rolling process until the user decides to exit.
    - The `num_die` function validates the user's input for the number of dice to roll.
    - Depending on the user's choice, one or two dice are rolled, and the result is displayed.
    - The user is then asked if they want to roll again.
'''

import random  # Importing the random module to generate random numbers.
import os  # Importing the os module to clear the console.

def num_die():
    # This function validates the user input for the number of dice to roll.
    while True:
        try:
            num_dice = input('Number of dice: ')
            valid_responses = ['1', 'one', 'two', '2']
            if num_dice not in valid_responses:
                raise ValueError('1 or 2 only')  # Raises a ValueError if input is invalid.
            else:
                return num_dice  # Returns the valid input.
        except ValueError as err:
            print(err)  # Prints the error message.

def roll_dice():
    min_val = 1  # Minimum value of a die.
    max_val = 6  # Maximum value of a die.
    roll_again = 'y'  # Initial value to enter the while loop.

    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':  # Continues rolling until user decides to exit.
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console.
        amount = num_die()  # Calls the num_die function to get the number of dice to roll.

        if amount == '2' or amount == 'two':  # If two dice are to be rolled.
            print('Rolling the dice...')
            dice_1 = random.randint(min_val, max_val)  # Rolls the first die.
            dice_2 = random.randint(min_val, max_val)  # Rolls the second die.

            print('The values are:')
            print('Dice One: ', dice_1)
            print('Dice Two: ', dice_2)
            print('Total: ', dice_1 + dice_2)  # Prints the total of two dice.

            roll_again = input('Roll Again? ')
        else:  # If one die is to be rolled.
            print('Rolling the die...')
            dice_1 = random.randint(min_val, max_val)  # Rolls the die.

            print(f'The value is: {dice_1}')  # Prints the value of the die.

            roll_again = input('Roll Again? ')

if __name__ == '__main__':
    roll_dice()  # Calls the roll_dice function to initiate the process.
