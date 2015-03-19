# -*- coding: utf-8 -*-
class LinkedPerson(object):
    '''
    A LinkedPerson is an object with a name, and a link to an object before and
    after itself in a doubly-linked list.
    '''
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
        
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
        
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
        
    def getBefore(self):
        # Returns the place in memory of the left-hand LinkedPerson
        return self.before
        
    def getAfter(self):
        # Returns the place in memory of the right-hand LinkedPerson
        return self.after
        
    def myName(self):
        # Returns the name of the LinkedPerson
        return self.name
        
        
def insert(CurrentPerson, newLinkedPerson):
    """
    CurrentPerson: a LinkedPerson that is part of a doubly linked list
    newLinkedPerson:  a LinkedPerson with no links 
    This procedure appropriately inserts newLinkedPerson into the linked list that CurrentPerson is a part of.    
    """
    # Ensure that each Person's name is lower case for comparisons
    CurrentPersonName = CurrentPerson.name.lower()
    newLinkedPersonName = newLinkedPerson.name.lower()
    
    # Create a list containing the two names to sort alphabetically
    list = [CurrentPersonName, newLinkedPersonName]
    list.sort()
    
    # If the CurrentPerson's name is alphabetically before the newLinkedPerson's
    # name, perform the following commands
    if list[0] == CurrentPersonName:
        
        # If CurrentPerson is last in the list, 
        if CurrentPerson.after == None:
            # The newLinkedPerson is placed after CurrentPerson
            CurrentPerson.setAfter(newLinkedPerson)
            newLinkedPerson.setBefore(CurrentPerson)
            
        # If CurrentPerson is not last in the list,
        else:
            # Save the next LinkedPerson as otherLinkedPerson and save the 
            # CurrentPerson as saveLinkedPerson
            otherLinkedPerson = CurrentPerson.after
            saveLinkedPerson = CurrentPerson
            
            # Perform the following commands until you reach the end of the list
            while otherLinkedPerson != None:
            
                # If the next LinkedPerson has the same name as newLinkedPerson
                if otherLinkedPerson.name.lower() == newLinkedPersonName:
                    # Place the newLinkedPerson after the saveLinkedPerson and 
                    # before the otherLinkedPerson
                    saveLinkedPerson.setAfter(newLinkedPerson)
                    newLinkedPerson.setBefore(saveLinkedPerson)
                    newLinkedPerson.setAfter(otherLinkedPerson)
                    otherLinkedPerson.setBefore(newLinkedPerson)
                    break
                    
                # If the next LinkedPerson's name differs from newLinkedPerson
                else:
                    # Create an alphabetical list containing the two names
                    list = [newLinkedPersonName, otherLinkedPerson.name.lower()]
                    list.sort()
                    
                    # If the newLinkedPerson's name is alphabetically before the 
                    # next LinkedPerson's name:
                    if list[0] == newLinkedPersonName:
                        # Place the newLinkedPerson after the saveLinkedPerson
                        # and before the otherLinkedPerson
                        saveLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(saveLinkedPerson)
                        newLinkedPerson.setAfter(otherLinkedPerson)
                        otherLinkedPerson.setBefore(newLinkedPerson)
                        break
                    
                    # If the newLinkedPerson's name is alphabetically after the 
                    # next LinkedPerson's name, and the next LinkedPerson is not
                    # the last one in the list:    
                    elif (list[1] == newLinkedPersonName 
                          and otherLinkedPerson.after != None):
                        # Save the next LinkedPerson in the list as the current 
                        # person to look at, and save the LinkedPerson after the 
                        # next LinkedPerson as the new "next LinkedPerson"
                        saveLinkedPerson = otherLinkedPerson
                        otherLinkedPerson = otherLinkedPerson.after
                        
                    # If the newLinkedPerson's name is alphabetically after the 
                    # next LinkedPerson's name, and the next LinkedPerson is the
                    # last one in the list:   
                    else:
                        # Place the newLinkedPerson after the next LinkedPerson
                        otherLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(otherLinkedPerson)
                        break
    
    # If the CurrentPerson's name is alphabetically after the newLinkedPerson's
    # name, perform the following commands                
    else: 
        # If CurrentPerson is first in the list, 
        if CurrentPerson.before == None:
            # The newLinkedPerson is placed before CurrentPerson
            newLinkedPerson.setAfter(CurrentPerson)
            CurrentPerson.setBefore(newLinkedPerson)
            
        # If CurrentPerson is not first in the list,
        else:
            # Save the previous LinkedPerson as otherLinkedPerson and save the 
            # CurrentPerson as saveLinkedPerson
            otherLinkedPerson = CurrentPerson.before
            saveLinkedPerson = CurrentPerson
            
            # Perform the following commands until you reach the end of the list
            while otherLinkedPerson != None:
                
                # If the next LinkedPerson has the same name as newLinkedPerson
                if otherLinkedPerson.name.lower() == newLinkedPersonName:
                    # Place the newLinkedPerson before the saveLinkedPerson and 
                    # after the otherLinkedPerson
                    otherLinkedPerson.setAfter(newLinkedPerson)
                    newLinkedPerson.setBefore(otherLinkedPerson)
                    newLinkedPerson.setAfter(saveLinkedPerson)
                    saveLinkedPerson.setBefore(newLinkedPerson)
                    break
                    
                # If the next LinkedPerson's name differs from newLinkedPerson
                else:
                    # Create an alphabetical list containing the two names
                    list = [newLinkedPersonName, otherLinkedPerson.name.lower()]
                    list.sort()
                    
                    # If the newLinkedPerson's name is alphabetically after the 
                    # next LinkedPerson's name:
                    if list[0] == otherLinkedPerson.name.lower():
                        # Place the newLinkedPerson before the saveLinkedPerson
                        # and after the otherLinkedPerson
                        otherLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(otherLinkedPerson)
                        newLinkedPerson.setAfter(saveLinkedPerson)
                        saveLinkedPerson.setBefore(newLinkedPerson)
                        break
                        
                    # If the newLinkedPerson's name is alphabetically before the 
                    # next LinkedPerson's name, and the next LinkedPerson is not
                    # the first one in the list:      
                    elif (list[1] == otherLinkedPerson.name.lower() 
                        # Save the next LinkedPerson in the list as the current 
                        # person to look at, and save the LinkedPerson before 
                        # the next LinkedPerson as the new "next LinkedPerson"
                        and otherLinkedPerson.before != None):
                        saveLinkedPerson = otherLinkedPerson
                        otherLinkedPerson = otherLinkedPerson.before
                        
                    # If the newLinkedPerson's name is alphabetically before the 
                    # next LinkedPerson's name, and the next LinkedPerson is the
                    # first one in the list:  
                    else:
                        # Place the newLinkedPerson before the next LinkedPerson
                        otherLinkedPerson.setBefore(newLinkedPerson)
                        newLinkedPerson.setAfter(otherLinkedPerson)
                        break

def findFront(start):
    """
    findFront is a recursive function that returns the name of the LinkedPerson
    who is at the start of the Doubly-Linked List
    
    start: a LinkedPerson that is part of a doubly linked list
    returns: the LinkedPerson at the beginning of the linked list 
    """
    
    if start.before == None:
        return start
    else:
        return findFront(start.before)


# ==== Below are example prints to check that the program is working ====

c = LinkedPerson("craig")
test_list = LinkedPerson("mark")
mar = LinkedPerson("martha")

insert(test_list, LinkedPerson("sam"))
insert(test_list, LinkedPerson("nick"))
insert(test_list, c)
insert(c, LinkedPerson("xanthi"))
insert(test_list, LinkedPerson("jayne"))
insert(c, mar)

print(test_list.before.name)
print(mar.before.name)

eric = LinkedPerson('Eric')
andrew = LinkedPerson('Andrew')
ruth = LinkedPerson('Ruth')
fred = LinkedPerson('Fred')
martha = LinkedPerson('martha')
zed = LinkedPerson('zed')
george = LinkedPerson('george')
brian = LinkedPerson('brian')
Zod = LinkedPerson('Zod')


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
insert(eric, LinkedPerson('martha'))
insert(ruth, zed)
insert(eric, george)
insert(martha, brian)
insert(Zod, brian)

print(LinkedPerson.getBefore(eric).name)

p = LinkedPerson('percival')
answer = findFront(p)   
print(answer.myName())                     
        