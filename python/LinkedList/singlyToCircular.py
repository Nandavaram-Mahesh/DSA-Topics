class Node:
    # Node will have Data and Pointer
    def __init__(self,nodeData):
        self.nodeData = nodeData
        self.nextPtr = None

class LinkedList:

    # Initially head is none
    def __init__(self):
        self.head = None
    
    # insert new_node at the end of the list 
    def insertAtEnd(self,nodeData):
        
        # create a new node
        new_node = Node(nodeData)
        
        # if no nodes exists assign the new node to the head 
        if self.head is None:
            self.head = new_node
            return
        
        #if nodes exists , then traverse till the end and insert the new node

        ## initialize a new pointer to traverse the list
        temp = self.head
        
        ##traverse till the end of the list and get the last node 
        while temp.nextPtr:
            temp = temp.nextPtr

        # assigning the last node next_pointer to the new_node address
        temp.nextPtr = new_node

    # conveert singly Linked List to Circular Linked List
    def convertSinglyToCircularLinkedList(self):
         
        if not self.head:
            return

        temp = self.head

        while temp.nextPtr:
            temp = temp.nextPtr
        #assigning the last node pointer with head , so it becomes circular  
        temp.nextPtr = self.head
        
    # print LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.nodeData)
            temp = temp.nextPtr



# Driver Code
    
llist = LinkedList()
llist.insertAtEnd(10)
llist.insertAtEnd(20)
llist.insertAtEnd(30)
llist.insertAtEnd(40)
llist.insertAtEnd(50)
llist.printList()

llist.convertSinglyToCircularLinkedList()
llist.printList()
