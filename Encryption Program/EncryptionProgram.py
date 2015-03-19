import string 
import random

# The path for the words.txt file should be edited according to it's location
WORDLIST_FILENAME = "/Users/steveogallagher/Documents/\
Python-Programs/Encryption Program/words.txt"


# === The following functions were provided by MIT ===
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded.\n"
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/Users/admin/6.001x/Problem Set 5/story.txt", "r").read()


# === End of functions provided by MIT ===

# ===== My Encryption Functions =====

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    # Strings alphaU & alphaL are created in order to have an alphabetical 
    # reference point for the amount of encryption shift required.
    alphaU = string.ascii_uppercase
    alphaL = string.ascii_lowercase
    dict = {} 
    iter = 0 
    newIter = 0
    
    # The corresponding encrypted Uppercase letter is found for the given shift
    for letter in alphaU:
        # For each letter, apply the shift and store it in dict{}
        if iter + shift < 26:
            dict[letter] = alphaU[iter + shift]
            iter += 1
        else:
            # If the shift goes beyond 'Z', start at the beginning with newIter
            dict[letter] = alphaU[newIter]
            newIter += 1
    
    # Iteration values are reset
    iter = 0
    newIter = 0
    
    # The corresponding encrypted Lowercase letter is found for the given shift
    for letter in alphaL:
        # For each letter, apply the shift and store it in dict{}
        if iter + shift < 26:
            dict[letter] = alphaL[iter + shift]
            iter += 1
        else:
            # If the shift goes beyond 'z', start at the beginning with newIter
            dict[letter] = alphaL[newIter]
            newIter += 1
    
    # Return the dictionary containing the keys and values according to shift
    return dict 

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    dict = coder # dict is assigned to the dictionary created in buildCoder()
    newText = "" # newText is initialised
    
    # The coder is applied to each char (or letter) in text
    for char in text:
        if char in dict.keys():
            newText += dict[char]
        else:
            newText += char
    
    return newText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))


# ===== Decryption =====

def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    # Initial variables are set to 0
    testKey = 0
    savedBest = 0
    validWords = 0
    savedKey = 0
    
    while testKey < 26:
        # Start with test key of 0 and apply to each word in the text
        testString = applyShift(text, testKey)
        
        # Split the text into individual words and save them into a list
        testList = testString.split(" ")

        # For each word:
        for word in testList:
            #check to see if it is a word
            if isWord(wordList, word):
            #if it is a word, add 1 to a saved variable to count it
                validWords += 1

            
        # If this is the highest amount so far, save the key value and try 
        # another key.
        if validWords > savedBest:
            savedBest = validWords
            savedKey = testKey
            
            testKey += 1
            validWords = 0
        else:
            testKey += 1
            validWords = 0
    # Return the key which resulted in the most valid words
    return (savedKey)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()


# ==== Below are example prints to check that the program is working ====

PhraseToEncrypt = '"To iterate is human, to recurse divine." - L. Peter Deutsch'
print("Phrase To Encrypt: %s\n" % (PhraseToEncrypt))
EncryptedPhrase = applyShift(PhraseToEncrypt, 23)
print("Encrypted Phrase: %s\n" % (EncryptedPhrase))

DecryptedPhrase = applyShift(EncryptedPhrase, (findBestShift(wordList, EncryptedPhrase)))
print("Decrypted Phrase: %s" % (DecryptedPhrase))