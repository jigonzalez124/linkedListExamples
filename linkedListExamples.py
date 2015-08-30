##  Name:  Jesus Ivan Gonzalez
##  Date:  August 30th, 2015
##  Description:  This is a linked list using Python.  In this script, nodes are created using
##  the Node class.  The LinkList class has a variety of options that adds, deletes, removes
##  duplicates, finds data, and prints the data in the linked list.


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

    def printList(self):        #prints linked list data
        thisNode = self.root
        while thisNode:
            print(thisNode.get_data())
            thisNode = thisNode.get_nextNode()

    def removeDups(self, d):    #removes all duplicates.  1st time occurances are skipped
        thisNode = self.root
        prevNode = None
        skip = 1
        while thisNode:
            if(thisNode.get_data() == d):
                if(skip == 1):
                    skip = 0
                    prevNode = thisNode
                    thisNode = thisNode.get_nextNode()
                else:
                    if prevNode:
                        prevNode.set_nextNode(thisNode.get_nextNode())
                        thisNode = thisNode.get_nextNode()
                    else:
                        self.root = thisNode
                    
                    self.size -= 1
            else:
                prevNode = thisNode
                thisNode = thisNode.get_nextNode()
                    

myList = LinkedList()
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.printList()
print('='*10)
myList.add(5)
myList.add(8)
myList.add(4)
myList.add(12)
myList.add(3)
myList.add(4)
myList.add(5)
myList.add(4)
myList.printList()
print('='*10)
myList.removeDups(4)
myList.printList()

