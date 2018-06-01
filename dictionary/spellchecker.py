# -----------------------------------------------------------------------------
# Name:        spellcheck
# -----------------------------------------------------------------------------
"""
A rudimentary spell checker

Prompt the user to enter a reference file name and an input file name.
This can be any text file in any language.
The program detects spelling errors in the input file name
and prints them out.
The program determines that a word is an error if it has not been seen
it in the reference.
"""
import string
def get_words(filename):
    """
    Get the words from a file

    Parameter: (string) file name
    Returns: (set of strings) a set containing all the words in that file
    """
    words_set = set()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower() #  convert the line to lower case
            for word in line.split():  #  then split it into words
                # take out leading and trailing special characters
                word = word.strip(string.punctuation + string.digits)
                if word:   # if word is not an empty string
                  words_set.add(word)  # add the word to our set
    return words_set


def flag_misspellings(words, ref):
    """
    Identify misspellings in a set of words based on a reference set.

    Parameters:
    words:  (set of strings) set of input words
    ref: (set of strings) set of reference words - these are correctly spelled words

    Returns: None
    """
    misspellings = words - ref  # get the misspelled words
    if misspellings:   # if the set is not empty
        print ('The following words may have been misspelled:')
        for word in misspellings:
            print (word)


def main():
    ref_name = input('Please enter the reference file name: ')
    reference = get_words(ref_name)   # get the reference words
    input_name = input('Please enter the input file name: ')
    input_words = get_words(input_name)  # get the input words
    flag_misspellings(input_words, reference)


if __name__ == '__main__':
    main()
