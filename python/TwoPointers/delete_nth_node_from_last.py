class Node:
    # Node will have Data and NextPointer , so we are initializing the node with these
    def __init__(self,data,nextPtr=None):
        self.data = data
        self.nextPtr =nextPtr


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.nodesCount=0

   
    # Time Complexity - O(1)
    def insertAtEnd(self,data):
        new_node = Node(data)

        # check if nodes exists

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.nodesCount+=1
            return
        else:
            self.tail.nextPtr = new_node
            self.tail = new_node
            self.nodesCount+=1
            

            # while self.tail.nextPtr is not None:
            #     self.tail = self.tail.nextPtr

            # self.tail.nextPtr = new_node
            # self.tail = new_node 

            # return self.tail.data
   
    #Time Complexity -O(N)    
    def deleteFromEnd(self,node_position):
        
        pointer1 = self.head
        pointer2 = self.head

        

        for i in range(node_position):
            pointer2 = pointer2.nextPtr

        if not pointer2:
            self.head = self.head.nextPtr
        
        while pointer2.nextPtr is not None:
            pointer1 = pointer1.nextPtr
            pointer2 = pointer2.nextPtr

        pointer1.nextPtr = pointer1.nextPtr.nextPtr


    def printLinkedList(self):
        # create a temp pointer to traverse the linked list
        temp = self.head
        
        #Traverse till the temp is not None 
        while temp:
            print(temp.data)
            temp = temp.nextPtr


LL=LinkedList()



# Insert at End working Perfect
LL.insertAtEnd(23)
LL.insertAtEnd(28)
LL.insertAtEnd(10)
LL.insertAtEnd(5)
LL.insertAtEnd(67)
LL.insertAtEnd(39)
LL.insertAtEnd(70)

LL.printLinkedList()

print("--------------------------------------------------")

# LL.deleteFromEnd(3)

LL.printLinkedList()

print("--------------------------------------------------")

LL.deleteFromEnd(7)

LL.printLinkedList()



 