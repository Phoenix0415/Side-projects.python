'''
Calculator Program:
-------------------------------------------------------------
This program provides a simple calculator functionality allowing users to perform basic arithmetic operations.
The operations include addition, subtraction, multiplication, and division. 

1. Firstly, individual functions for each operation are defined.
2. Within each function:
    - The screen is cleared for better readability using os.system call.
    - Users are prompted to input numbers.
    - Basic error checking is performed to ensure valid inputs.
    - A while loop is used to allow users to continue performing operations or exit.
3. The main calculator function initializes a loop, providing a user interface to select the desired operation or quit the program.
4. Based on user input, the corresponding function is called, and the result is displayed.
'''
import os # Importing the os module to clear the console.

# Function to perform addition.
def addition():

    # This outer loop allows the user to start the addition process afresh.
    while True: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Addition')

        # Collecting initial two numbers from the user for addition.
        num_1 = float(input('Enter a number: '))
        num_2 = float(input('Enter another number: '))
        ans = num_1 + num_2
        values_entered = 2
        print(f'Current result: {ans}')

        # Prompt the user to continue or exit.
        continue_calc = input('Enter more (y/n): ')
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')
        
        # Breaks the loop if user enters 'n'.
        if continue_calc.lower() == 'n':
            break

    # Returns the final sum and the total numbers entered.
    return [ans, values_entered]

# Function to perform subtraction.
def subtraction():

    # This outer loop allows the user to start the subtraction process afresh.
    while True: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Subtraction')

        # Collecting initial two numbers from the user for subtraction.
        num_1 = float(input('Enter a number: '))
        num_2 = float(input('Enter another number: '))
        ans = num_1 - num_2
        values_entered = 2
        print(f'Current result: {ans}')

        # Prompt the user to continue or exit.
        continue_calc = input('Enter more (y/n): ')
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')
        
        # Breaks the loop if user enters 'n'.
        if continue_calc.lower() == 'n':
            break

    # Returns the final difference and the total numbers entered.
    return [ans, values_entered]

# Function to perform multiplication.
def multiplication():

    # This outer loop allows the user to start the multiplication process afresh.
    while True:  
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Multiplication')

        # Collecting initial two numbers from the user for multiplication.
        num_1 = float(input('Enter a number: '))
        num_2 = float(input('Enter another number: '))
        ans = num_1 * num_2
        values_entered = 2
        print(f'Current result: {ans}')

        # Prompt the user to continue or exit.
        continue_calc = input('Enter more (y/n): ')
        while continue_calc.lower() not in ['y', 'n']:
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')
        
        # Breaks the loop if user enters 'n'.
        if continue_calc.lower() == 'n':
            break

    # Returns the final product and the total numbers entered.
    return [ans, values_entered]

# Function to perform division.
def division(): 
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen.
    print('Division')

    # A flag to continue or exit the loop based on user input.
    continue_calc = 'y'

    # # The main loop for continuing or exiting the division process.
    while continue_calc.lower() == 'y':  

        # Collecting initial two numbers from the user for division.
        num_1 = float(input('Enter a number as the dividend: '))
        num_2 = float(input('Enter another number as the divisor: '))

        # Basic error checking to ensure valid inputs. 
        while num_2 == 0.0:  # if the divisor is 0, the user is prompted to enter a valid number.
                print('Please enter a divisor > 0') 
                num_2 = float(input('Enter another divisor: '))

        # Performing the division and displaying the result.
        ans = num_1 / num_2
        values_entered = 2
        print(f'Current result: {ans}')

        # Prompt the user to continue or exit.
        continue_calc = input('Enter more (y/n): ')
        while continue_calc.lower() not in ['y', 'n']:  # Validates the input.
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

    return [ans, values_entered]  # Returns the final quotient and the total numbers entered.


# Main calculator function.
def calculator():
    quit = False  # A flag to exit the loop based on user input.

    # 1. start the calculator: display a welcome message and instructions
    while not quit:  # A loop to allow the user to continue performing operations or exit.
        results = [] # A list to store the results of the operation and the total numbers entered.
       
        # 2. clear the screen and display the instructions
        print('Simple Calculator in Python!')
        print('1. Enter \'a\' for addition')
        print('2. Enter \'s\' for substraction')
        print('3. Enter \'m\' for multiplication')
        print('4. Enter \'d\' for division')
        print('5. Enter \'q\' to quit')

        # 3. ask the user to select an operation
        choice = input('Selection: ')

        # 4. clear the screen and call the corresponding function based on user input
        if choice == 'q':  # Exits the loop if user enters 'q'.
            quit = True
            continue

        # Calls the corresponding function based on user input.
        if choice == 'a':  
            results = addition()
            print(f'Final result: {results[0]}, Total values entered: {results[1]}')
        elif choice == 's':   
            results = subtraction()
            print(f'Final result: {results[0]}, Total values entered: {results[1]}')
        elif choice == 'm':
            results = multiplication()
            print(f'Final result: {results[0]}, Total values entered: {results[1]}')
        elif choice == 'd':
            results = division()
            print(f'Final result: {results[0]}, Total values entered: {results[1]}')
        else:
            print('Sorry, invalid character')


if __name__ == '__main__':  # Calls the main calculator function.
    calculator() # Calls the main calculator function.
