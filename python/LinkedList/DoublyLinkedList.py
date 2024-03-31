class Node:
    def __init__(self,data,prevPtr=None,nextPtr=None):
        self.data = data
        self.prevPtr = prevPtr
        self.nextPtr = nextPtr
    
class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    # Time Complexity - O(1) 
    def insertAtEnd(self,data):
        new_node = Node(data)
        
        # If no nodes are present
        if self.head is None:
            # setting the head to the new_node
            self.head = new_node
            # setting the tail to the new_node/head
            self.tail = self.head
            return
        else:
            # set tails nextPtr to new_node 
            self.tail.nextPtr = new_node
            # set new_nodes prevPtr to tail
            new_node.prevPtr = self.tail
            # change the tail to new_node
            self.tail = new_node
        return self.tail.data
   
    # Time Complexity- O(1)
    def insertAtFront(self,data):
        new_node = Node(data)
        # if no nodes
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        else:
            # setting head prevPtr to new_node, so prev first element is pointint to new_node now
            self.head.prevPtr = new_node
            #setting new_node nextPtr to head , so that new_node to pointing to the head  
            new_node.nextPtr = self.head
            # then changing the head to the new_node
            self.head = new_node 
            
    # Time Complexity - O(n)
    def insertAtAnotherNode(self,data,index):
        new_node = Node(data)

        temp = self.head

        for i in range(0,(index-1)):
            temp = temp.nextPtr
        
        new_node.nextPtr = temp.nextPtr

        temp.nextPtr = new_node
        new_node.prevPtr = temp
        next_Node = new_node.nextPtr
        next_Node.prevPtr = new_node
    
    #Time Complexity - O(1) 
    def deleteFromFront(self):
        
        if self.head is None:
            return
        else:
            self.head = self.head.nextPtr
            self.head.prevPtr = None
    
    # Need to work on this
    def deleteFromEnd(self):
        if self.head is None:
            return
        else:
            self.tail = self.tail.prevPtr
            self.tail.nextPtr = None
    
    # Time Complexity - O(n)
    def deleteAfterNode(self,index):
        
        # Base case
        if self.head is None:
            return
        
        temp = self.head
        for i in range(0,(index-1)):
            temp = temp.nextPtr

        temp.nextPtr = temp.nextPtr.nextPtr
        next = temp.nextPtr.nextPtr
        next.prevPtr = None


    
    def printLinkedList(self):
        # create a temp pointer to traverse the linked list
        temp = self.head
        
        #Traverse till the temp is not None 
        while temp:
            print(temp.data)
            temp = temp.nextPtr


DL = DoublyLinkedList()
# DL.insertAtEnd(100)
# DL.insertAtEnd(200)
# DL.insertAtEnd(300)
# DL.insertAtEnd(400)
# result =DL.insertAtEnd(500)

# print("Tail:",result)\
DL.insertAtFront(70)
DL.insertAtFront(60)
DL.insertAtFront(50)
DL.insertAtFront(40)
DL.insertAtFront(30)
DL.insertAtFront(20)
DL.insertAtFront(10)

# DL.deleteFromFront()
# DL.deleteFromFront()
# DL.deleteFromEnd()
# DL.deleteFromEnd()
# DL.deleteFromEnd()
# DL.deleteFromEnd()
# DL.deleteFromEnd()
# DL.deleteFromEnd()

# DL.deleteAfterNode(2)

DL.insertAtAnotherNode(25,2)

DL.printLinkedList()