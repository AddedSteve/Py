def semordnilap(str1, str2):
    '''
    A "semordnilap" is defined as a pair of words of which each word is the 
    reverse of the other word. For example: "pan" and "nap" are semordnilap.
    
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    
    # Check if the lengths are the same
    if len(str1) != len(str2):
        return False
    
    # Check if we can't minimise the string any further
    elif len(str1) == 1:
        
        # Return boolean value for final characters' equality
        return str1 == str2
            
    # Check equality and resend shorter strings        
    elif str1[-1] == str2[0]:
        
        return semordnilap(str1[:-1], str2[1:])
        
    else:
        return False
        
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
    
    
# ==== Below are example prints to check that the program is working ====    
    
a1 = "and"
a2 = "dna"
b1 = "stab"
b2 = "bats"
c1 = "bold"
c2 = "bolder"
        
print("Are %s and %s Semordnilap?\nAnswer: %s\n" % 
(a1, a2, semordnilapWrapper(a1, a2)))
print("Are %s and %s Semordnilap?\nAnswer: %s\n" % 
(b1, b2, semordnilapWrapper(b1, b2)))
print("Are %s and %s Semordnilap?\nAnswer: %s\n" % 
(c1, c2, semordnilapWrapper(c1, c2)))