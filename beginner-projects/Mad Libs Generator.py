'''
Mad Libs Generator Program:
-------------------------------------------------------------
This program takes user input to fill in the blanks of a pre-defined story, 
creating a unique, personalized version of the story each time.
'''

# Prompting the user to provide various words to be used in the story
noun = input('Choose a noun: ')  # User provides a singular noun
p_noun = input('Choose a plural noun: ')  # User provides a plural noun
noun2 = input('Choose a noun: ')  # User provides another singular noun
place = input('Name a place: ')  # User provides a place name
adjective = input('Choose an adjective (Describing word): ')  # User provides an adjective
noun3 = input('Choose a noun: ')  # User provides yet another singular noun

# Printing the user-customized story to the console
print('------------------------------------------')  # Print a line for visual separation

# Following lines construct the story using user-provided words.
# String concatenation is used to insert user input into the pre-defined text.
print('Be kind to your', noun, '- footed', p_noun)
print('For a duck may be somebody\'s', noun2, ',')
print('Be kind to your', p_noun, 'in', place)
print('Where the weather is always', adjective, '. \n')
print('You may think that is this the', noun3, ',')
print('Well it is.')

print('------------------------------------------')  # Print a line for visual separation
