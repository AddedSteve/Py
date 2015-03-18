def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # Ordered alphabet string

    # If aStr is empty, char must not be in the string
    if aStr == "":
        return False
    # If aStr is equal to char, then char is in the string
    elif char == aStr:
        return True
    
    # Otherwise, some calculations are needed
    else:
        # find the middle letter of the string
        middle = int(len(aStr)/2)
        midLetter = aStr[middle]
        
        # Check to see if this is the char
        if midLetter == char:
            return True
        
        # If it is not,
        else: 
            base = 0
            top = -1  
            
            # Delete the '#"s below to enable the print statements in testing
            #print("middle position number in new string is " + str(middle))
            #print("middle letter is " + str(midLetter))
    
            # Determine the position of the char in the alphabet
            position = alpha.find(char)
            # Determine the position of the middle letter in the alphabet
            position2 = alpha.find(midLetter)       

            # If char is earlier in the alphabet, change the top parameter
            if position < position2:
                top = middle
                #print("top is now " + str(top))
                
                # call isIn recursively with the new bisected string
                return isIn(char, aStr[:top])
            
             # If char is later in the alphabet, change the base parameter
            elif position > position2:
                base = middle + 1
                #print("base is now " + str(base))
                
                # call isIn recursively with the new bisected string
                return isIn(char, aStr[base:])
            
            # If all attempts to locate the char fail, return False
            else:
                return False
    
        
# ==== Below are example prints to check that the program is working ====

character = 'y'
character2 = 't'
string = 'abdhjkopqruvwxyz'

print("Is %s in %s?\nAnswer: " % (character, string) 
+ str(isIn(character, string)))

print("\nIs %s in %s?\nAnswer: " % (character2, string) 
+ str(isIn(character2, string)))

