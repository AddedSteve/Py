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
        
        
def insert(CurrentPerson, newLinkedPerson, after = 0, before = 0):
    """
    CurrentPerson: a LinkedPerson that is part of a doubly linked list
    newLinkedPerson:  a LinkedPerson with no links 
    This procedure appropriately inserts newLinkedPerson into the linked list that CurrentPerson is a part of.    
    """
    
    # Ensure that each Person's name is lower case for comparisons
    CurrentPersonName = CurrentPerson.name.lower()
    newLinkedPersonName = newLinkedPerson.name.lower()
    
    # Save the next LinkedPerson as otherLinkedPerson
    afterLinkedPerson = CurrentPerson.after
    beforeLinkedPerson = CurrentPerson.before
    
    # Create a list containing the two names to sort alphabetically
    list = [CurrentPersonName, newLinkedPersonName]
    list.sort()
    
    # If the CurrentPerson's name is alphabetically before the newLinkedPerson's
    # name, perform the following commands
    if list[0] == CurrentPersonName:
        after = 1
        # If CurrentPerson is last in the list, 
        if CurrentPerson.after == None:
            # The newLinkedPerson is placed after CurrentPerson
            CurrentPerson.setAfter(newLinkedPerson)
            newLinkedPerson.setBefore(CurrentPerson)
        
        elif CurrentPerson.after.name.lower() == newLinkedPersonName:
            # Place the newLinkedPerson after the CurrentPerson and 
            # before the otherLinkedPerson
            CurrentPerson.setAfter(newLinkedPerson)
            newLinkedPerson.setBefore(CurrentPerson)
            newLinkedPerson.setAfter(afterLinkedPerson)
            afterLinkedPerson.setBefore(newLinkedPerson)
         
        elif before == 1 and after == 1: 
            # Place the newLinkedPerson after the CurrentPerson and 
            # before the otherLinkedPerson
            CurrentPerson.setAfter(newLinkedPerson)
            newLinkedPerson.setBefore(CurrentPerson)
            newLinkedPerson.setAfter(afterLinkedPerson)
            afterLinkedPerson.setBefore(newLinkedPerson)          
        else:
            after = 1
            insert(afterLinkedPerson, newLinkedPerson, after, before)
    
    # If the CurrentPerson's name is alphabetically after the newLinkedPerson's
    # name, perform the following commands                
    else: 
        before = 1
        # If CurrentPerson is first in the list, 
        if CurrentPerson.before == None:
            # The newLinkedPerson is placed before CurrentPerson
            CurrentPerson.setBefore(newLinkedPerson)
            newLinkedPerson.setAfter(CurrentPerson)
        
        elif CurrentPerson.before.name.lower() == newLinkedPersonName:
            # Place the newLinkedPerson before the CurrentPerson and 
            # after the otherLinkedPerson
            CurrentPerson.setBefore(newLinkedPerson)
            newLinkedPerson.setAfter(CurrentPerson)
            newLinkedPerson.setBefore(beforeLinkedPerson)
            beforeLinkedPerson.setAfter(newLinkedPerson)
            
        elif before == 1 and after == 1: 
            # Place the newLinkedPerson before the CurrentPerson and 
            # after the otherLinkedPerson
            CurrentPerson.setBefore(newLinkedPerson)
            newLinkedPerson.setAfter(CurrentPerson)
            newLinkedPerson.setBefore(beforeLinkedPerson)
            beforeLinkedPerson.setAfter(newLinkedPerson)          
        else:
            before = 1
            insert(beforeLinkedPerson, newLinkedPerson, after, before)  
            

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

# Create LinkedPerson class objects
eric = LinkedPerson('Eric')
andrew = LinkedPerson('Andrew')
ruth = LinkedPerson('Ruth')
fred = LinkedPerson('Fred')
martha = LinkedPerson('martha')
zed = LinkedPerson('zed')
george = LinkedPerson('george')
brian = LinkedPerson('brian')
Zod = LinkedPerson('Zod')

# Insert LinkedPerson objects into a doubly-linked list
print("Insert Andrew at Eric's point in the list")
insert(eric, andrew)
print("   - %s has been placed before %s." % 
    (LinkedPerson.getBefore(eric).name,
     LinkedPerson.getAfter(andrew).name))

print("Insert Ruth at Eric's point in the list")
insert(eric, ruth)
print("   - %s has been placed after %s." % 
    (LinkedPerson.getAfter(eric).name,
     LinkedPerson.getBefore(ruth).name))

print("Insert Fred at Eric's point in the list")
insert(eric, fred)
print("   - %s has been placed after %s and before %s." % 
    (LinkedPerson.getAfter(eric).name,
     LinkedPerson.getBefore(fred).name,
     LinkedPerson.getAfter(fred).name))

print("Insert martha at Ruth's point in the list")
insert(ruth, martha)
print("   - %s has been placed after %s and before %s." % 
    (LinkedPerson.getBefore(ruth).name,
     LinkedPerson.getBefore(martha).name,
     LinkedPerson.getAfter(martha).name))

print("Insert martha at Eric's point in the list")
insert(eric, LinkedPerson('martha'))
print("   - %s has been placed after %s and before %s." % 
    (martha.name,
     LinkedPerson.getBefore(martha).name,
     LinkedPerson.getAfter(martha).name))

print("Insert zed at Ruth's point in the list")
insert(ruth, zed)
print("   - %s has been placed after %s." % 
    (zed.name,
     LinkedPerson.getBefore(zed).name))

print("Insert george at Eric's point in the list")
insert(eric, george)
print("   - %s has been placed after %s and before %s." % 
    (george.name,
     LinkedPerson.getBefore(george).name,
     LinkedPerson.getAfter(george).name))

print("Insert brian at martha's point in the list")
insert(martha, brian)
print("   - %s has been placed after %s and before %s." % 
    (brian.name,
     LinkedPerson.getBefore(brian).name,
     LinkedPerson.getAfter(brian).name))

# Test the findFront() function
print("\nFind the LinkedPerson at the front of the list.")
answer = findFront(brian)   
print("The LinkedPerson at the front of the list is %s" % (answer.myName()))                    