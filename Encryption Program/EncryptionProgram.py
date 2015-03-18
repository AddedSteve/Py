# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string 
import random

WORDLIST_FILENAME = "/Users/admin/6.001x/Problem Set 5/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    alphaU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphaL = 'abcdefghijklmnopqrstuvwxyz'
    dict = {}
    iter = 0
    newIter = 0
    
    for letter in alphaU:
        if iter + shift < 26:
            dict[letter] = alphaU[iter + shift]
            iter += 1
        else:
            dict[letter] = alphaU[newIter]
            newIter += 1
            
    iter = 0
    newIter = 0
    
    for letter in alphaL:
        if iter + shift < 26:
            dict[letter] = alphaL[iter + shift]
            iter += 1
        else:
            dict[letter] = alphaL[newIter]
            newIter += 1
            
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    dict = coder
    newText = ""
    
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

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    testKey = 0
    bestEffort = 0
    savedBest = 0
    validWords = 0
    savedKey = 0
    
    while testKey < 26:
        # Start with test key of 0 and apply to each word in the text
        testString = applyShift(text, testKey)
        
        # Split the text into individual words and save them into a list
        testList = testString.split(" ")
    
        # Save the length of the list
        listLength = len(testList)
    
        # For each word:
        for word in testList:
            #check to see if it is a word
            if isWord(wordList, word):
            #if it is a word, add 1 to a saved variable to count it
                validWords += 1
            
        bestEffort = validWords

            
        # If this is the highest amount so far, save the key value and try 
        # another key.
        if bestEffort > savedBest:
            savedBest = bestEffort
            savedKey = testKey
            
            testKey += 1
            validWords = 0
        else:
            testKey += 1
            validWords = 0
    # If none of the keys result in 100% correct words, return best case
    return (savedKey)


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    story = getStoryString()
    wordList = loadWords()
    return applyShift(story, findBestShift(wordList, story))

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()

PhraseToEncrypt = "Hello, world!"
print("Phrase To Encrypt: %s\n" % (PhraseToEncrypt))
EncryptedPhrase = applyShift(PhraseToEncrypt, 23)
print("Encrypted Phrase: %s\n" % (EncryptedPhrase))

DecryptedPhrase = applyShift(EncryptedPhrase, (findBestShift(wordList, EncryptedPhrase)))
print("Decrypted Phrase: %s" % (DecryptedPhrase))