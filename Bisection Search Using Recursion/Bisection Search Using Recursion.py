def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    alpha = "abcdefghijklmnopqrstuvwxyz"

    
    if aStr == "":
        return False
    elif char == aStr:
        return True
    else:
        middle = int(len(aStr)/2)
        midLetter = aStr[middle]
        
        if midLetter == char:
            return True
        else: 
            base = 0
            top = -1  
            #print("middle position number in new string is " + str(middle))
            #print("middle letter is " + str(midLetter))
            base = 0
            top = -1
    
            position = alpha.find(char)
            position2 = alpha.find(midLetter)       


            if position < position2:
                top = middle
                #print("top is now " + str(top))
                return isIn(char, aStr[:top])
            if position > position2:
                base = middle + 1
                #print("base is now " + str(base))
                return isIn(char, aStr[base:])
        
            else:
                return False
    
        
    
print("is it in there? Answer: " + str(isIn('y', 'abdhjkopqruvwxyz')))
