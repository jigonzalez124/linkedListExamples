##  Name:  Jesus Ivan Gonzalez
##  Date:  August 30th, 2015
##  Description:  This is a linked list using Python.  In this script, it will return True
##  if the linked list is circular, otherwise False.


## Node structure
class Node(object):
    
    def __init__(self, d, nextNode = None):
        self.d = d
        self.nextNode = nextNode

    def get_data(self):
        return self.d

    def get_nextNode(self):
        return self.nextNode

    def set_data(self, d):
        self.d = d

    def set_nextNode(self, nextNode):
        self.nextNode = nextNode


##Linked List structure
class LinkedList(object):

    def __init__(self, r=None):     #initializes linked list
        self.root = r
        self.size = 0

    def get_root(self):         #returns root
        return self.root
    
    def get_size(self):         #returns size of list
        return self.size        

    def add(self, d):           #queues a node to the linked list
        newNode = Node(d, self.root)
        self.root = newNode
        self.size += 1

    def remove(self, d):        #starts at beginning of linked list and finds d, if exists
        thisNode = self.root
        prevNode = None
        while thisNode:
            if(thisNode.get_data() == d):       #true when d is in linked list
                if prevNode:            #not at beginning of linked list
                    prevNode.set_nextNode(thisNode.get_nextNode())
                else:       #at beginning of linked list
                    self.root = thisNode 
                self.size -= 1
                return True
            else:       #if d is not current node, shift prevNode and thisNode by one
                prevNode = thisNode
                thisNode = thisNode.get_nextNode()
        return False

    def find(self, d):      #returns if d is in linked list
        thisNode = self.root
        while thisNode:
            if(thisNode.get_data() == d):
                return True
            else:
                thisNode = thisNode.get_nextNode()
        return None

    def loopDetection(self):        #looks into linked list is it is circular
        listOfData = []
        thisNode = self.root
        while thisNode:
            if(thisNode.get_data() in listOfData):
                return True
            else:
                listOfData.append(thisNode.get_data())
                thisNode = thisNode.get_nextNode()
        return False


myList = LinkedList()
myList.add(1)
print(myList.loopDetection())
myList.add(2)
print(myList.loopDetection())
myList.add(3)
print(myList.loopDetection())
myList.add(4)
print(myList.loopDetection())
myList.add(5)
print(myList.loopDetection())
myList.add(8)
print(myList.loopDetection())
myList.add(4)
print(myList.loopDetection())
myList.add(12)
print(myList.loopDetection())
myList.remove(4)
print(myList.loopDetection())
myList.add(5)
print(myList.loopDetection())
myList.add(4)
print(myList.loopDetection())
