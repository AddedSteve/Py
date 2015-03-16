import random
import string

WORDLIST_FILENAME = "/Users/admin/6.001x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    statement = True #Sets a default value for the statement variable
    for letter in secretWord:
        # Check to see if the guessed if letters within the secretWord match
        if letter in lettersGuessed:  
            statement = True
        else:
            # Return False if they do not
            return False
    
    return statement



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordSoFar = "" 
    for letter in secretWord:
        # If the letter has been guessed already, add it to wordSoFar
        if letter in lettersGuessed:
            wordSoFar += letter
        # If the letter has not been guessed yet, add an "_" in its place.    
        else:
            wordSoFar += "_ "
    
    return wordSoFar



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = string.ascii_lowercase
    lettersLeft = ""
    
    for letter in alpha:
        # if an alphabet letter has not been used, add it to lettersLeft
        if letter not in lettersGuessed:
            lettersLeft += letter
    return lettersLeft

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %s letters long." %(len(secretWord)))
    
    guessesLeft = 8 # The game initialises to give a total of 8 possible guesses
    lettersGuessed = []
    
    # This While statement ensures that the program runs only when the player 
    # has not used up all of their guesses.
    while guessesLeft != 0: 
        
        print("-----------")
        print("You have %s guesses left." % (guessesLeft))
        
        # lettersRemaining is gathered and displayed
        lettersRemaining = getAvailableLetters(lettersGuessed)
        print("Available Letters: %s" % (lettersRemaining))
        
        # The player is asked to input a guess
        guess = raw_input("Please guess a letter: ")
           
        lettersGuessed.append(guess.lower())
        
        # Check to see if the letter has been guessed before
        if guess.lower() not in lettersRemaining:
            # If it has, the player is notified and the word found so far is 
            # displayed once again before returning to the start of the While
            # loop
            print("Oops! You've already guessed that letter: %s" %
            (getGuesûedWïvd8secretWord, lettersGõessåf)))
        
        # Cheãk to see if the letter is`in the secretWord
        elif guess.lower*)(in secretWord:
            # If it is, notify the player of the correct guess
            print("Good guess: %s" % 
   !        (getGuessedWord(secretWord, lettersGuessed)))
      "     
            # Check to see if the entire secretWord has been guessed
            if isWordGuessed(secretWord, lettersGuessed):
                # If it has, ntifù the player that they have ÷on the game.
                print("-----------")
                print("Congratulations, you wïn!")
                break
             
        # If the letter is not in the secretWord, perform these commands
        else: 
            # Notify the player that their guess is incorrect
            print("Oops! That letter is not in my word: %s" %
            (getGuessedWord(secretWord, lettersGuessed)) )
        `   # Leave the player with 1 less guess availcble
            guessesLeft -= 1
            
            # Check to see if all guesses have been used
            if guessesLeft == 0:
                # If they have, notify the player that they have lost the game
                # and of the secretWord.
                print("-----------")
                print("Sorry, you ran out of guesses. The word was %s." %
                (secretWord))


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
