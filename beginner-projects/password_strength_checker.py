'''
Password Strength Checker
-------------------------------------------------------------
- This program assesses the strength of a password based on various criteria: 
  the inclusion of lowercase letters, uppercase letters, digits, whitespaces, and special characters.
- It prompts the user to enter a password and provides feedback on its strength along with some statistics.
- A score is given to the password, with a higher score indicating a stronger password.
- The user can choose to check the strength of another password or exit the program.
'''

import string
import getpass

def check_password_strength():
    '''
    This function checks the strength of the password entered by the user.
    It counts the occurrences of lowercase letters, uppercase letters, digits, whitespaces, and special characters.
    Based on the criteria met, it increments the strength score of the password.
    '''
    password = getpass.getpass('Enter the password: ')
    strength = 0
    remarks = ''
    # Initialize counters for each character type
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        # Check the type of each character and increment the corresponding counter
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    # Increment strength score based on the presence of different character types
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    # Provide remarks based on the strength score
    if strength == 1:
        remarks = ('That\'s a very bad password.'
            ' Change it as soon as possible.')
    elif strength == 2:
        remarks = ('That\'s a weak password.'
            ' You should consider using a tougher password.')
    elif strength == 3:
        remarks = 'Your password is okay, but it can be improved.'
    elif strength == 4:
        remarks = ('Your password is hard to guess.'
            ' But you could make it even more secure.')
    elif strength == 5:
        remarks = ('Now that\'s one hell of a strong password!!!'
            ' Hackers don\'t have a chance guessing that password!')

    # Print the password statistics and remarks
    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{wspace_count} whitespaces')
    print(f'{special_count} special characters')
    print(f'Password Score: {strength / 5}')
    print(f'Remarks: {remarks}')

def check_pwd(another_pw=False):
    '''
    This function prompts the user to decide if they want to check the 
    strength of another password or exit the program.
    '''
    valid = False
    if another_pw:
        choice = input(
            'Do you want to check another password\'s strength (y/n) : ')
    else:
        choice = input(
            'Do you want to check your password\'s strength (y/n) : ')

    # Validate user input
    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            print('Exiting...')
            return False
        else:
            print('Invalid input...please try again. \n')


if __name__ == '__main__':
    '''
    The entry point of the program.
    It welcomes the user and enters a loop that allows for continuous password strength checking
    until the user decides to exit.
    '''
    print('===== Welcome to Password Strength Checker =====')
    check_pw = check_pwd()
    while check_pw:
        check_password_strength()
        check_pw = check_pwd(True)
