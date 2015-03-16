alpha = "abcdefghijklmnopqrstuvwxyz" #String containing the alphabet


def checker(s): 
    """
    This is a function that will examine a string argument to determine the
    longest substring which is in alphabetical order
    """
    
    #Initial values
    iter = 0
    number = 0 
    longeststring = ""
    save = ""
    
    #While loop plays until all characters in the string are examined
    while (int(iter) < int(len(s))):
        for letter in s:
            if save == "":
                save += letter #adds the current letter to the 'save' string
                position1 = alpha.find(letter) #assigns a number to the letter
                
                #This condition tests to see if current string is longest
                if len(save) > len(longeststring):
                        longeststring = save    #saves longest string so far
                                                #into object 'longeststring'
                        iter += 1
                else:
                    iter += 1
                    
            else:
                position2 = alpha.find(letter)
                
                if (position2 == position1): #compares the order of the two most
                    save += letter           #recent letters examined.
                    
                    if len(save) > len(longeststring):
                        longeststring = save
                        iter += 1
                    else:
                        iter += 1
                        
                elif (position2 > position1):
                    save += letter
                    position1 = position2
                    
                    if len(save) > len(longeststring):
                        longeststring = save
                        iter += 1
                    else:
                        iter += 1
                        
                elif (position2 < position1):
                    #if the new letter is alphabetically earlier than the old
                    #letter, a new search must begin
                    save = ""
                    save += letter
                    position1 = position2
                    iter += 1
                else:
                    return longeststring
                    
        return longeststring #returns the longest substring out of the function

#The user is asked to enter a string for testing
answer = checker(s = raw_input("Please enter a string: "))

#After the function has completed, the longest substring is displayed
print("Longest substring in alphabetical order is: %s" % (answer))