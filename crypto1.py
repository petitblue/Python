# -----------------------------------------------------------------------------
# Name:        crypto
# 
# Author: Luyan Deng

# -----------------------------------------------------------------------------
"""

"""

def starts_with_vowel(word):
    """
    parameter is word
    if the first letter of the word is within the string 'aeiou'
    return True
    """

    vowel = 'aeiou'
    fst_letter = word[0]
    if fst_letter in vowel:
        return True
    else:
        return False

    # return True if the word starts with a vowel and False otherwise

def encrypt(word):
    """
    Enter your function docstring here
    """
    # encrypt a single word into the secret language
    # call starts_with_vowel to decide which pattern to follow
    # return a single word (encrypted)
    fst_letter = word[0]
    encry_w = ''
    if fst_letter in vowel:
        encryted_wd = word+ 'ten'
    else:
        encryted_wd = word.remove(word[0])+word[0]+'est'
    return encryted_wd


def decrypt(word):
    """
    Enter your function docstring here
    """
    # decrypt a single word from the secret language
    # If the word is not a valid word in the secret language, return None
def decrypt(word):

    message = ''
    if word[-3:] == 'tan':
        message = word[:-3]
    elif word[-3:] == 'est':
        message = word[-4]+word[:-4]

    else:
        print('invalid')
    return message
def translate(text, mode):
    """
    Enter your function docstring here
    """
    # Translate (encrypt or decrypt) the whole message
    # Split the text into a list of words
    # if mode is 'E' encrypt each of the words in the list
    # if mode id 'D' decrypt each word in the list
    # Build a new list with these translated words
    # Reverse the list
    # join the list of reversed translated words into a single string
    # and return it

def choose_mode():
    """
    Enter your function docstring here
    """
    # Prompt the user for input repeatedly until they enter 'E' or 'D'.

    while True:
        prompt = 'Please type E to encrypt or D to decrypt a message: '
        user_input = input(prompt)
        if user_input == 'E':
            return True
        if user_input == 'D':
            return True
        else:
            print('Invalid')

    # Return the user's choice.

def main():
    # Get the user choice 'E' or 'D' and save it in a variable.
    # Prompt the user for the message to be translated.
    # Translate the message by calling translate - save result.
    # Print the result - or 'Invalid message' if applicable.

    mode = choose_mode()
    user_input = input('Please enter your message: ')
    if choose_mode():
        translate(text, mode)
    else:
        print('Invalid message')


if __name__ == '__main__':
    main()
