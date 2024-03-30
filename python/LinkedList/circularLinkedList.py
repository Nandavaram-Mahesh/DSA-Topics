class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None

    
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insertAtEnd(self,data):
        # Create a new Node
        new_node = Node(data)

        # If head is None then assing new node to head and also tail
        if  self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            # Set nextPtr of tail to point to new_node 
            self.tail.nextPtr = new_node
            
            # Set the tail to the new node
            self.tail = new_node

            # Set next of tail to head
            self.tail.nextPtr = self.head

    def deleteNode(self,nodeData):
        # check if there is no node
        if self.head is None:
            return
        # check if there is only one node and check if the node data is same as nodeData to be deleted
        if(self.head == self.tail and self.head.data ==nodeData):
                self.head = None
                self.tail = None
                return 

         # if the target is at head set head to second element and set tail's next to the new head
        temp = self.head
        if(self.head.data==nodeData):
            self.head =temp.nextPtr
            self.tail.nextPtr = self.head
        # Now iterate over the linked list till you reach the tail and check if the next node is target
        # If it is, set current nodes next to the next of the next node and break.
            
            while temp.nextPtr is not None and temp!=self.tail:
                pass
            
            # temp = self.head
            # prev = self.head
            # next = self.head
        
        
            #     while temp:
            #         if(temp.data==nodeData):
            #             pass
            #         next = temp.nextPtr
            #         prev = temp
            #         temp = temp.nextPtr





        
    def printCircularLinkedList(self):
        temp=self.head
        while temp:
            temp = temp.nextPtr
            print(temp.data)


CLL = CircularLinkedList()

CLL.insertAtEnd(20)
CLL.insertAtEnd(30)
CLL.insertAtEnd(40)
CLL.insertAtEnd(50)

CLL.printCircularLinkedList()
