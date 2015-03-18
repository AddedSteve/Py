def genPrimes():
    '''
    This is a generator function which returns prime numbers increasing in value
    '''
    
    p = [] # list keeping track of all prime numbers found
    next = 2 # 2 is the first prime number
    yield next
    
    p.append(next)
    
    next +=1
    bool = True
    
    # This loop will keep working until a prime number is yielded
    while True:
        # Checking by comparing each prime number found so far
        for i in p:        
            # if the current number 'next' is divisible by a known prime number
            if next % i == 0:
                # a prime number has not been found
                bool = False 
        
        if bool == False:
            next += 1 # Modify next to the next greatest integer
            bool = True # Ensure that the While loop continues working
            
        # If a prime number was found
        else:
            p.append(next) # Add this number for the p list
            yield next # Yield the latest prime number to be found
            next += 1
    
# ==== Below are example prints to check that the program is working ====
    
Prime = genPrimes()    
print(Prime.next())
print(Prime.next())    
print(Prime.next())
print(Prime.next())    
print(Prime.next())
print(Prime.next())    