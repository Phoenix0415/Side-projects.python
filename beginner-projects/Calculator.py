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
import os  

# Function to perform addition.
def addition():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen.
    print('Addition')  # Indicates the operation type to the user.

    continue_calc = 'y'  # A flag to continue or exit the loop based on user input.

    # Collecting initial two numbers from the user for addition.
    num_1 = float(input('Enter a number: '))
    num_2 = float(input('Enter another number: '))
    ans = num_1 + num_2  # Performing the addition.
    values_entered = 2  # Keeps track of the total numbers entered.
    print(f'Current result: {ans}')  # Displays the current sum to the user.

    # A loop to allow the user to continue adding numbers or exit.
    while continue_calc.lower() == 'y':
        continue_calc = input('Enter more (y/n): ')
        while continue_calc.lower() not in ['y', 'n']:  # Validates the input.
            print('Please enter \'y\' or \'n\'')
            continue_calc = input('Enter more (y/n): ')

        if continue_calc.lower() == 'n':  # Exits the loop if user enters 'n'.
            break
        num = float(input('Enter another number: '))  # Collects another number from the user.
        ans += num  # Adds the new number to the current sum.
        print(f'Current result: {ans}')  # Displays the updated sum.
        values_entered += 1  # Increments the count of total numbers entered.

    return [ans, values_entered]  # Returns the final sum and the total numbers entered.

# Function to perform subtraction.
def subtraction():
   os.system('cls' if os.name == 'nt' else 'clear') # Clears the console screen.
   print('Subtraction')  # Indicates the operation type to the user.

   continue_calc = 'y' # A flag to continue or exit the loop based on user input.

   num_1 = float(input('Enter a number: ')) # Collecting initial two numbers from the user for subtraction.
   num_2 = float(input('Enter another number: '))  
   ans = num_1 - num_2 # Performing the subtraction.
   values_entered = 2 # Keeps track of the total numbers entered.
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y': # A loop to allow the user to continue subtracting numbers or exit.
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']: # Validates the input.
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))
 
       if continue_calc.lower() == 'n': # Exits the loop if user enters 'n'.
           break
       num = float(input('Enter another number: ')) # Collects another number from the user.
       ans -= num
       print(f'Current result: {ans}')
       values_entered += 1  # Increments the count of total numbers entered.
   return [ans, values_entered]  # Returns the final difference and the total numbers entered.

# Function to perform multiplication.
def multiplication():
   os.system('cls' if os.name == 'nt' else 'clear') # Clears the console screen.
   print('Multiplication')

   continue_calc = 'y'  # A flag to continue or exit the loop based on user input.

   num_1 = float(input('Enter a number: ')) # Collecting initial two numbers from the user for multiplication.
   num_2 = float(input('Enter another number: '))
   ans = num_1 * num_2
   values_entered = 2 # Keeps track of the total numbers entered.
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y': # A loop to allow the user to continue multiplying numbers or exit.
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']: # Validates the input.
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n': # Exits the loop if user enters 'n'.
           break
       num = float(input('Enter another number: '))
       ans *= num
       print(f'Current result: {ans}')
       values_entered += 1
   return [ans, values_entered]  # Returns the final product and the total numbers entered.

# Function to perform division.
def division(): 
   os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console screen.
   print('Division')

   continue_calc = 'y'

   num_1 = float(input('Enter a number: '))
   num_2 = float(input('Enter another number: '))
   while num_2 == 0.0:  # Validates the input.
       print('Please enter a second number > 0')
       num_2 = float(input('Enter another number: '))

   ans = num_1 / num_2
   values_entered = 2
   print(f'Current result: {ans}')

   while continue_calc.lower() == 'y':  # A loop to allow the user to continue dividing numbers or exit.
       continue_calc = (input('Enter more (y/n): '))
       while continue_calc.lower() not in ['y', 'n']:  # Validates the input.
           print('Please enter \'y\' or \'n\'')
           continue_calc = (input('Enter more (y/n): '))

       if continue_calc.lower() == 'n':
           break
       num = float(input('Enter another number: '))
       while num == 0.0:  # Validates the input.
           print('Please enter a number > 0')
           num = float(input('Enter another number: '))
       ans /= num
       print(f'Current result: {ans}')
       values_entered += 1   # Increments the count of total numbers entered.
   return [ans, values_entered]  # Returns the final quotient and the total numbers entered.

# Main calculator function.
def calculator():
   quit = False  # A flag to exit the loop based on user input.
   while not quit:  # A loop to allow the user to continue performing operations or exit.
       results = []
       print('Simple Calculator in Python!')
       print('Enter \'a\' for addition')
       print('Enter \'s\' for substraction')
       print('Enter \'m\' for multiplication')
       print('Enter \'d\' for division')
       print('Enter \'q\' to quit')

       choice = input('Selection: ')

       if choice == 'q':  # Exits the loop if user enters 'q'.
           quit = True
           continue

       if choice == 'a':   # Calls the corresponding function based on user input.
           results = addition()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 's':   
           results = subtraction()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'm':
           results = multiplication()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       elif choice == 'd':
           results = division()
           print('Ans = ', results[0], ' total inputs: ', results[1])
       else:
           print('Sorry, invalid character')


if __name__ == '__main__':  # Calls the main calculator function.
   calculator()
