# -*- coding: utf-8 -*-

class Frob(object):
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
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    #Forby = start
    #while Forby.before != None:
    #    saveForby = Forby
    #    Forby = Forby.before
    
    if start.before == None:
        return start
    else:
        return findFront(start.before)
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    atMeName = atMe.name.lower()
    newFrobName = newFrob.name.lower()
    
    list = [atMeName, newFrobName]
    list.sort()
    
    if list[0] == atMeName:
        if atMe.after == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            otherFrob = atMe.after
            saveFrob = atMe
            iter = 0
            while otherFrob != None:
                if otherFrob.name.lower() == newFrobName:
                    saveFrob.setAfter(newFrob)
                    newFrob.setBefore(saveFrob)
                    newFrob.setAfter(otherFrob)
                    otherFrob.setBefore(newFrob)
                    break
                else:
                    list = [newFrobName, otherFrob.name.lower()]
                    list.sort()
                    if list[0] == newFrobName:
                        saveFrob.setAfter(newFrob)
                        newFrob.setBefore(saveFrob)
                        newFrob.setAfter(otherFrob)
                        otherFrob.setBefore(newFrob)
                        break
                    elif list[1] == newFrobName and otherFrob.after != None:
                        saveFrob = otherFrob
                        otherFrob = otherFrob.after
                    else:
                        otherFrob.setAfter(newFrob)
                        newFrob.setBefore(otherFrob)
                        break
                        
    else: 
        if atMe.before == None:
            newFrob.setAfter(atMe)
            atMe.setBefore(newFrob)
        else:
            otherFrob = atMe.before
            saveFrob = atMe
            iter = 0
            while otherFrob != None:
                if otherFrob.name.lower() == newFrobName:
                    otherFrob.setAfter(newFrob)
                    newFrob.setBefore(otherFrob)
                    newFrob.setAfter(saveFrob)
                    saveFrob.setBefore(newFrob)
                    break
                else:
                    list = [newFrobName, otherFrob.name.lower()]
                    list.sort()
                    if list[0] == otherFrob.name.lower():
                        otherFrob.setAfter(newFrob)
                        newFrob.setBefore(otherFrob)
                        newFrob.setAfter(saveFrob)
                        saveFrob.setBefore(newFrob)
                        break
                    elif list[1] == otherFrob.name.lower() and otherFrob.before != None:
                        saveFrob = otherFrob
                        otherFrob = otherFrob.before
                    else:
                        otherFrob.setBefore(newFrob)
                        newFrob.setAfter(otherFrob)
                        break




c = Frob("craig")
test_list = Frob("mark")
mar = Frob("martha")

insert(test_list, Frob("sam"))
insert(test_list, Frob("nick"))
insert(test_list, c)
insert(c, Frob("xanthi"))
insert(test_list, Frob("jayne"))
insert(c, mar)

print(test_list.before.name)
print(mar.before.name)

eric = Frob('Eric')
andrew = Frob('Andrew')
ruth = Frob('Ruth')
fred = Frob('Fred')
martha = Frob('martha')
zed = Frob('zed')
george = Frob('george')
brian = Frob('brian')
Zod = Frob('Zod')


insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
insert(eric, Frob('martha'))
insert(ruth, zed)
insert(eric, george)
insert(martha, brian)
insert(Zod, brian)


p = Frob('percival')
answer = findFront(p)   
print(answer.myName())                     
        