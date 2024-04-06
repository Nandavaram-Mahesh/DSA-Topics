class Node:
    def __init__(self,data,prevPtr=None,nextPtr=None):
        self.data= data
        self.prevPtr = prevPtr
        self.nextPtr = nextPtr
    
class DoublyCircularLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def insertAtFront(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.nextPtr = self.head
            self.tail.prevPtr = self.head
            return

        self.head.prevPtr = new_node
        self.tail.nextPtr = new_node
        new_node.nextPtr = self.head
        new_node.prevPtr = self.tail
        self.head = new_node



    def insertAtEnd(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.nextPtr = self.head
            new_node.prevPtr = self.head
            return
        # setting heads prevPtr to new_node
        self.head.prevPtr = new_node
        # setting tail NextPtr to new_node
        self.tail.nextPtr = new_node
        # setting new_node PrevPtr to tail , since tail is the prev node
        new_node.prevPtr = self.tail
        # setting new_node nextPtr to head , since its circular
        new_node.nextPtr = self.head
        # Finally shifting tail to new_node so that it stays at end node
        self.tail = self.tail.nextPtr
        

    def insertAfterNode(self,data,index):
        
        new_node = Node(data)

        temp = self.head

        for i in range(0,(index-1)):
            temp = temp.nextPtr
        new_node.nextPtr = temp.nextPtr
        temp.nextPtr = new_node
        new_node.prevPtr = temp
        next_node = new_node.nextPtr
        next_node.prevPtr = new_node

    def deleteAtFront(self):
        
        if self.head is None:
            return
        
        self.head = self.head.nextPtr
        self.head.prevPtr = self.tail
        self.tail.nextPtr = self.head

    def deleteAtEnd(self):
        pass

    def deleteAfterNode(self):
        pass

    def printLinkedList(self):
        # create a temp pointer to traverse the linked list
        temp = self.head
        
        #Traverse till the temp is not None 
        while temp:
            print(temp.data)
            temp = temp.nextPtr



DCLL = DoublyCircularLinkedList()

DCLL.insertAtEnd(10)
DCLL.insertAtEnd(20)
DCLL.insertAtEnd(30)
DCLL.insertAtEnd(40)

# DCLL.insertAtFront(10)
# DCLL.insertAtFront(20)
# DCLL.insertAtFront(30)
# DCLL.insertAtFront(40)

DCLL.insertAfterNode(25,2)
DCLL.deleteAtFront()
DCLL.printLinkedList()