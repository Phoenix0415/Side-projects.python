'''
Countdown Timer Program:
-------------------------------------------------------------
This program demonstrates a simple countdown timer functionality.
1. The user is prompted to enter the desired countdown time in seconds.
2. The `countdown` function takes this time as an argument and initiates a countdown.
3. Inside the function:
    - A while loop iterates until the time reaches zero.
    - The divmod function is used to calculate minutes and seconds from the total seconds.
    - The formatted time is printed to the console on the same line (end='\r').
    - The program sleeps for 1 second using time.sleep before decrementing the countdown time by 1.
4. When the time reaches zero, a 'Lift off!' message is displayed.
'''

import time  # Importing the time module to use the sleep function.

def countdown(user_time):
    while user_time >= 0:  # Loop continues until time reaches zero.
        mins, secs = divmod(user_time, 60)  # Calculating minutes and seconds from the total seconds.
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Formatting the time in mm:ss format.
        print(timer, end='\r')  # Printing the time on the same line.
        time.sleep(1)  # Pausing the execution for 1 second.
        user_time -= 1  # Decrementing the countdown time by 1.
    print('Lift off!')  # Displaying the lift off message when the time reaches zero.

if __name__ == '__main__':
    user_time = int(input("Enter a time in seconds: "))  # Prompting the user to enter the countdown time in seconds.
    countdown(user_time)  # Calling the countdown function with the user provided time as an argument.
