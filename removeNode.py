##  Name:  Jesus Ivan Gonzalez
##  Date:  August 30th, 2015
##  Description:  This is a linked list using Python.  In this script, the remove() method
##  removes a node with specific data, d.


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

    def printList(self):
        thisNode = self.root
        while thisNode:
            print(thisNode.get_data())
            thisNode = thisNode.get_nextNode()


myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(6)
myList.add(4)
myList.printList()
print('='*10)
myList.add(5)
myList.add(8)
myList.add(4)
myList.remove(2)
myList.add(12)
myList.add(3)
myList.add(4)
myList.remove(1)
myList.add(5)
myList.add(4)
myList.printList()
print('='*10)
myList.printList()

