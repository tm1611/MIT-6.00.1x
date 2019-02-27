# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

import string

def getAvailableLetters(lettersGuessed):
    result = string.ascii_lowercase[:28]
    for item in lettersGuessed:
        result = result.replace(item,'')
    return result

def isWordGuessed(secretWord, lettersGuessed):
    secretList = list(secretWord)
    i = 0

    while (i < len(secretList)):
        if (secretList[i] in lettersGuessed): # is True
            i += 1
        else:
            return False
            break
    return True

def getGuessedWord(secretWord, lettersGuessed):
    i = 0
    # string is immutable to make a new variable to collect letters as a string object
    result = ''
    while (i < len(secretWord)):
        if (secretWord[i] in lettersGuessed): # if it  exists
            result += secretWord[i] # add it to result
        else: # if it does not exit then add an underscore
            result += '_ '
        i += 1 # add + 1 so that it breaks once it iterates the word
    return result

def isIn(secretWord, user_guess):
    if (user_guess in secretWord):
        return True
    return False

# PROBLEM SOLVING USING FUCNTIONS THAT I HAVE CREATED

def hangman(secretWord):
    mistakeMade = 0
    lettersGuessed = []
    availableLetters = string.ascii_lowercase

    # INTRO
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long')

    # ROUND
    while (mistakeMade < 8) and (not isWordGuessed(secretWord, lettersGuessed)):
        print('-----------')
        print('You have ' + str(8 - mistakeMade) + ' guesses left.')
        print('Available Letters : ', availableLetters)
        user_guess = input('please guess a letter: ') # ASK FOR AN INPUT GUESS
        lettersGuessed.append(user_guess)

        if (not user_guess in availableLetters): # LETTER HAS BEEN GUESSED
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))

        else: # LETTER HAS NOT BEEN GUESSED
            if (isIn(secretWord, user_guess)): # LETTER IS IN SECRETWORD
                print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))

            else: # LETTER IS NOT IN SECRET
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                mistakeMade += 1
        availableLetters = getAvailableLetters(lettersGuessed)

    print('-----------') # ONCE IT IS DONE
    if (isWordGuessed(secretWord, lettersGuessed)): # IF DONE BECAUSE THE WORD IS CORRECT
        print('Congratulations, you won!')
    else: # IF DONE BECAUSE MISTAKE > 8
        print('Sorry, you ran out of guesses. The word was else. ')
    return



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
