'''
Dice Roll Game Program:
-------------------------------------------------------------
This program simulates the rolling of one or two dice.
1. display a welcome message.
2. The user is asked how many dice they want to roll.
3. The `roll_dice` function is called to initiate the dice rolling process.
4. Inside the function:
    - A while loop continues the dice rolling process until the user decides to exit.
    - The `num_die` function validates the user's input for the number of dice to roll.
    - Depending on the user's choice, one or two dice are rolled, and the result is displayed.
    - The user is then asked if they want to roll again.
    - The console is cleared before each roll.
    - A goodbye message is displayed when the user exits the program.

-------------------------------------------------------------
To Do:
    - Add a message to display the total number and highest number of rolls for each game.
    
    - Add a mode that allows the user to compete against the computer.
        - The computer should roll the dice after the user.
        - The computer should win if it gets a higher total value.

    - Add a mode that allows the user to compete against another player.
        - ask for the number of players, and then ask for the name of each player.
'''

import random  # Importing the random module to generate random numbers.
import os  # Importing the os module to clear the console.
import time  # Importing the time module to create delays for better user experience.

def num_die():
    # This function validates the user input for the number of dice to roll.
    while True:
        try:
            num_dice = input('Number of dice(1 or 2)? ')
            valid_responses = ['1', 'one', 'two', '2']
            if num_dice not in valid_responses:
                raise ValueError('1 or 2 only')  # Raises a ValueError if input is invalid.
            else:
                return num_dice  # Returns the valid input.
        except ValueError as err: # Catches the ValueError.
            print(err)  # Prints the error message.

def roll_dice():
    min_val = 1  # Minimum value of a die.
    max_val = 6  # Maximum value of a die.
    roll_again = 'y'  # Initial value to enter the while loop.

    # 1. start the game: display a welcome message
    print('Welcome to the Dice Rolling Simulator!')
    # draw a dice with 5 dot
    print('''
               _______
              | .   . |
              |   .   |
              | .   . |
               -------
    ''')

    # add a delay
    time.sleep(2)  # Pauses the execution for 2 seconds.

    # 2. ask the user how many dice they want to roll
    while roll_again.lower() == 'yes' or roll_again.lower() == 'y':  # Continues rolling until user decides to exit.
        
        # 3. clear the screen and call the `num_die` function to get the number of dice to roll
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console before each roll. 'cls' for windows, 'clear' for mac/linux. os.name is used to check the name of the operating system.
        amount = num_die()  # Calls the num_die function to get the number of dice to roll.

        # 4. roll the dice and display the result
        # If two dice are to be rolled.
        if amount == '2' or amount == 'two':  
            print('Rolling the dice...')
            time.sleep(2) # Pauses the execution for 2 seconds. 
            dice_1 = random.randint(min_val, max_val)  # Rolls the first die.
            dice_2 = random.randint(min_val, max_val)  # Rolls the second die.

            # Prints the values of the two dice.
            print('The values are:')
            print('Dice One: ', dice_1)
            print('Dice Two: ', dice_2)
            print('Total value: ', dice_1 + dice_2) 

            # 5. ask the user if they want to roll again and store the response in the `roll_again` variable
            roll_again = input('Roll Again? (y/n)')

        # If one die is to be rolled.
        else:  
            print('Rolling the die...') # Prints the message.
            time.sleep(2) # Pauses the execution for 2 seconds. 
            dice_1 = random.randint(min_val, max_val)  # Rolls the die.

            print(f'The value is: {dice_1}')  # Prints the value of the die.

            # 5. ask the user if they want to roll again and store the response in the `roll_again` variable
            roll_again = input('Roll Again? (y/n) ')

    # 6. if the user decides to exit, display a goodbye message
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console before exiting the program.
    print('Thanks for playing!')  
    # draw a dice with 5 dot and a big smile
    print('''
               _______
              | .   . |
              |   .   |
              | .   . |
               -------
    ''')
    # add a delay
    time.sleep(1)  # Pauses the execution for 1 seconds.


if __name__ == '__main__': 
    roll_dice()  # Calls the roll_dice function to initiate the process.
