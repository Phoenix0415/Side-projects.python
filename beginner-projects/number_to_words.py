'''
Numbers To Words:
-------------------------------------------------------------
- This program takes a numeric input from the user and converts it to words. 
  For instance, 1234 would be converted to "One Thousand Two Hundred Thirty Four".

- The conversion is carried out by defining tuples for single digits, two digits, tens, 
  and large number suffixes, and then utilizing functions to process segments of the 
  number and translate them to words. 

- Each function has a specific role in converting a particular segment of the number to words.

The tuples defined below act as a dictionary that the functions reference to get the 
word equivalent of a numeric value:
'''

# Tuple containing words for single-digit numbers
ones = (
   'Zero', 'One', 'Two', 'Three', 'Four',
   'Five', 'Six', 'Seven', 'Eight', 'Nine'
   )

# Tuple containing words for two-digit numbers from 10 to 19
twos = (
   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
   )

# Tuple containing words for the tens place in two-digit numbers (20, 30, ... 90)
tens = (
   'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety', 'Hundred'
   )

# Tuple containing suffixes for large numbers (Thousand, Million, Billion)
suffixes = (
   '', 'Thousand', 'Million', 'Billion'
   )

def fetch_words(number, index):
    """
    Returns the word representation of a three-digit number along with the
    appropriate suffix (Thousand, Million, Billion).
    """
    if number == '0': return 'Zero'

    # Ensure the number has three digits by prepending zeros if necessary
    number = number.zfill(3)
    # Splitting the digits of the number for processing
    hundreds_digit = int(number[0])
    tens_digit = int(number[1])
    ones_digit = int(number[2])

    words = '' if number[0] == '0' else ones[hundreds_digit]

    # Processing the hundreds place
    if words != '':
        words += ' Hundred '

    # Processing the tens place
    if tens_digit > 1:
        words += tens[tens_digit - 2]
        words += ' '
        words += ones[ones_digit]
    elif(tens_digit == 1):
        words += twos[((tens_digit + ones_digit) % 10) - 1]
    elif(tens_digit == 0):
        words += ones[ones_digit]

    # Removing the word 'Zero' if it appears at the end of the words
    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    # Adding the appropriate suffix (Thousand, Million, Billion)
    if len(words) != 0:
        words += suffixes[index]
      
    return words

def convert_to_words(number):
    """
    Converts a number into its word representation by processing it three digits at a time.
    """
    length = len(str(number))

    # Check if the number is too large for this program
    if length > 12:
        return 'This program supports a maximum of 12 digit numbers.'

    # Determine how many groups of three digits there are
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    # Process each group of three digits
    for i in range(length - 1, -1, -3):
        words.append(fetch_words(
            str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1

    # Reversing the order of words to form the final word representation
    final_words = ''
    for s in reversed(words):
        final_words += (s + ' ')

    return final_words

if __name__ == '__main__':
    number = int(input('Enter any number: '))
    print('%d in words is: %s' %(number, convert_to_words(number)))  # Outputting the word representation of the number
