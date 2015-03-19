import string


def checker(s, current = "", longest = "", position = 0): 
    """
    This is a function that will examine a string argument to determine the
    longest substring which is in alphabetical order
    """
    #An ordered alphabetical string is created for comparison
    alpha = string.ascii_lowercase
    
    # If s is an empty string, inform the user of the error
    if s == "":
        return "The string you entered has no length"
    # Otherwise perform the tasks of the checker function
    else:    
        # If this is the first time through, add the first character to current
        if current == "":
            current += s[0]
            if len(s) >= 2:
                return checker(s[1:], current, current, alpha.find(s[0]))
            else: # If s only contains 1 character, return longest string
                return current
    
        # Check the order of the last current letter and first s letter  
        elif position <= alpha.find(s[0]):
            current += s[0]
            if len(current) > len(longest):
                longest = current
            if len(s) >= 2: 
                return checker(s[1:], current, longest, alpha.find(s[0]))
            # If s only contains 1 character, return longest string
            elif len(current) > len(longest):
                return current
            else:
                return longest
            
        # If the next letter is earlier in alpha:
        else:
            if len(current) > len(longest):
                longest = current
            current = s[0]
            if len(s) >= 2:
                return checker(s[1:], current, longest, alpha.find(s[0]))
            # If s only contains 1 character, return longest string
            else:
                return longest

#The user is asked to enter a string for testing
answer = checker(s = raw_input("Please enter a string: "))

#After the function has completed, the longest substring is displayed
print("Longest substring in alphabetical order is: %s" % (answer))