class Node:
    # Node will have Data and NextPointer , so we are initializing the node with these
    def __init__(self,data):
        self.data = data
        self.nextPtr =None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtBegining(self,data):
        # create new node to insert
        new_node = Node(data)

        # copy the head to the new_node next pointer
        new_node.nextPtr = self.head

        # Set the head and tail to point to new_node
        self.head = new_node
        
        # # set the tail to the head nextPointer
        # self.tail = self.head.nextPtr

    
    def insertAtEnd(self,data):
        new_node = Node(data)
        #  If no nodes are present
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr
             
        temp.nextPtr = new_node

       





    def printLinkedList(self):
        # create a temp pointer to traverse the linked list
        temp = self.head
        
        #Traverse till the temp is not None 
        while temp:
            print(temp.data)
            temp = temp.nextPtr


LL=LinkedList()

# LL.insertAtBegining(20)
# LL.insertAtBegining(30)
# LL.insertAtBegining(40)
# LL.insertAtBegining(50)
LL.insertAtEnd(20)
LL.insertAtEnd(30)
LL.insertAtEnd(40)
LL.insertAtEnd(50)
LL.insertAtEnd(60)
LL.insertAtEnd(70)

LL.printLinkedList()



    






 