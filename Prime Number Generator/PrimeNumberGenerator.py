def genPrimes():
    p = [2]
    next = 2
    yield next
    next +=1
    bool = True
    
    while True:
        for i in p:        
            if next % i == 0:
                bool = False 
        
        if bool == False:
            next += 1
            bool = True
        else:
            p.append(next)
            yield next
            next += 1
    
Prime = genPrimes()    
print(Prime.next())
print(Prime.next())    
print(Prime.next())
print(Prime.next())    
print(Prime.next())
print(Prime.next())    