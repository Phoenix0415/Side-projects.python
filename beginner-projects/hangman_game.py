'''
Hangman Game Program:
-------------------------------------------------------------
This program simulates the game of Hangman:
1. A list of words is defined for the game.
2. A random word is chosen from the list.
3. The player guesses one letter at a time, trying to discover the chosen word.
4. The player can continue playing new rounds or exit the game.
'''

import random  # Importing the random module to choose random words.
import time  # Importing the time module to create delays for better user experience.
import os  # Importing the os module to clear the console.

def play_again():
    # This function asks the player if they want to play again.
    question = 'Do You want to play again? y = yes, n = no \n'
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        return True
    else:
        return False

def hangman(word):
    # This function handles the main gameplay of Hangman.
    display = '_' * len(word)  # Initial display with underscores.
    count = 0  # Count of wrong guesses.
    limit = 5  # Limit of wrong guesses.
    letters = list(word)  # Convert the word to a list of letters.
    guessed = []  # List to store guessed letters.
    
    while count < limit:  # Main gameplay loop.
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        
        # Input validation loop.
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
            
        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue
        
        # Checking the guessed letter against the word.
        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index] + guess + display[index + 1:]
        else:
            guessed.append(guess)
            count += 1
            draw_hangman(count)  # Draw the hangman figure based on the count.
        
        if display == word:
            print(f'Congrats! You have guessed the word \'{word}\' correctly!')
            break

def draw_hangman(count):
    # This function draws the hangman figure based on the count of wrong guesses.
    hangman_stages = [
        '''
           _____ 
          |      
          |      
          |      
          |      
          |      
          |      
          __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |      
          |      
          |      
          |      
          __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |      
          |      
          |      
          __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |      
          |      
          __|__
        ''',
        '''
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |    /|\\ 
          |    / \\ 
          __|__
        '''
    ]
    time.sleep(1)
    print(hangman_stages[count-1])  # Print the corresponding hangman stage.
    print(f'Wrong guess: {5 - count} guesses remaining\n')

def play_hangman():
    # This function initializes the game and manages rounds of gameplay.
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console.

    words_to_guess = [
        'january', 'border', 'image', 'film', 'promise', 'kids',
        'lungs', 'doll', 'rhyme', 'damage', 'plants', 'hello', 'world'
    ]
    play = True  # Boolean to continue playing.
    while play:
        word = random.choice(words_to_guess)  # Choose a random word from the list.
        hangman(word)  # Call the hangman function to play the game.
        play = play_again()  # Ask the player if they want to play again.

    print('Thanks For Playing! We expect you back again!')
    exit()

if __name__ == '__main__':
    play_hangman()  # Call the play_hangman function to start the game.
