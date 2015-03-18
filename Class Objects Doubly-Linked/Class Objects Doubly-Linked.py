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
    CurrentPersonName = CurrentPerson.name.lower()
    newLinkedPersonName = newLinkedPerson.name.lower()
    
    list = [CurrentPersonName, newLinkedPersonName]
    list.sort()
    
    if list[0] == CurrentPersonName:
        if CurrentPerson.after == None:
            CurrentPerson.setAfter(newLinkedPerson)
            newLinkedPerson.setBefore(CurrentPerson)
        else:
            otherLinkedPerson = CurrentPerson.after
            saveLinkedPerson = CurrentPerson
            
            while otherLinkedPerson != None:
                if otherLinkedPerson.name.lower() == newLinkedPersonName:
                    saveLinkedPerson.setAfter(newLinkedPerson)
                    newLinkedPerson.setBefore(saveLinkedPerson)
                    newLinkedPerson.setAfter(otherLinkedPerson)
                    otherLinkedPerson.setBefore(newLinkedPerson)
                    break
                else:
                    list = [newLinkedPersonName, otherLinkedPerson.name.lower()]
                    list.sort()
                    if list[0] == newLinkedPersonName:
                        saveLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(saveLinkedPerson)
                        newLinkedPerson.setAfter(otherLinkedPerson)
                        otherLinkedPerson.setBefore(newLinkedPerson)
                        break
                    elif list[1] == newLinkedPersonName and otherLinkedPerson.after != None:
                        saveLinkedPerson = otherLinkedPerson
                        otherLinkedPerson = otherLinkedPerson.after
                    else:
                        otherLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(otherLinkedPerson)
                        break
                        
    else: 
        if CurrentPerson.before == None:
            newLinkedPerson.setAfter(CurrentPerson)
            CurrentPerson.setBefore(newLinkedPerson)
        else:
            otherLinkedPerson = CurrentPerson.before
            saveLinkedPerson = CurrentPerson
            
            while otherLinkedPerson != None:
                if otherLinkedPerson.name.lower() == newLinkedPersonName:
                    otherLinkedPerson.setAfter(newLinkedPerson)
                    newLinkedPerson.setBefore(otherLinkedPerson)
                    newLinkedPerson.setAfter(saveLinkedPerson)
                    saveLinkedPerson.setBefore(newLinkedPerson)
                    break
                else:
                    list = [newLinkedPersonName, otherLinkedPerson.name.lower()]
                    list.sort()
                    if list[0] == otherLinkedPerson.name.lower():
                        otherLinkedPerson.setAfter(newLinkedPerson)
                        newLinkedPerson.setBefore(otherLinkedPerson)
                        newLinkedPerson.setAfter(saveLinkedPerson)
                        saveLinkedPerson.setBefore(newLinkedPerson)
                        break
                    elif list[1] == otherLinkedPerson.name.lower() and otherLinkedPerson.before != None:
                        saveLinkedPerson = otherLinkedPerson
                        otherLinkedPerson = otherLinkedPerson.before
                    else:
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
        