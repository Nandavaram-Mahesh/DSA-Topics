class Node:
    # Node will have Data and NextPointer , so we are initializing the node with these
    def __init__(self,data,nextPtr=None):
        self.data = data
        self.nextPtr =nextPtr


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    # Time Complexity - O(1)
    def insertAtBegining(self,data):
        # create new node to insert
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # setting tail to the head to get circular property
            self.tail.nextPtr = self.head
            
        else:
            # copy the head to the new_node next pointer
            new_node.nextPtr = self.head

            # Set the head and tail to point to new_node
            self.head = new_node

            # set tail nextPtr to the new_node/self.head

            self.tail.nextPtr = self.head
        
        return self.tail.data
        # # set the tail to the head nextPointer
        # self.tail = self.head.nextPtr

    # Time Complexity - O(1)
    def insertAtEnd(self,data):
        new_node = Node(data)

        # If no nodes exists 
        if self.head is None:
            # setting head and tail to the new_node
            self.head = new_node
            self.tail = new_node
            # setting the tail nextPtr to the head to get circular property
            self.tail.nextPtr = self.head

            return
        else:
            
            # if there is a node then setting tails nextPtr to the new_node 
            self.tail.nextPtr = new_node
            # then changing tail to the new_node
            self.tail = new_node
            # setting the tail nextPtr to the head to get circular property
            self.tail.nextPtr = self.head



            # while self.tail.nextPtr is not None:
            #     self.tail = self.tail.nextPtr

            # self.tail.nextPtr = new_node
            # self.tail = new_node 

            # return self.tail.data
    

    # Time Complexity - O(n)
    def insertAfterAnotherNode(self,data,index):
        new_node = Node(data)
        temp = self.head
        for i in range(0,(index-1)):
            temp = temp.nextPtr

        new_node.nextPtr = temp.nextPtr
        temp.nextPtr = new_node


    # Need to work on this
    # Time Complexity - O(n)
    def deleteAtEnd(self):
        # dummy_node = Node(nextPtr=self.head)
        # check if nodes exists
        if self.head is None:
            return
        
        curr = self.head
        next = self.head
        prev = self.head
        
        while curr.nextPtr is not self.tail:
            next = curr.nextPtr
            prev = curr
            curr = next
        
        prev.nextPtr = self.head
        self.tail = prev
        
        
        return self.tail
    
   
    # Time Complexity- O(1)
    def deleteFromBegining(self):
        
        if self.head is None:
            return
        
        self.head = self.head.nextPtr
        self.tail.nextPtr = self.head
        
        
    def printLinkedList(self):
        # create a temp pointer to traverse the linked list
        temp = self.head
        
        #Traverse till the temp is not None 
        while temp:
            print(temp.data)
            temp = temp.nextPtr


LL=LinkedList()

# Insert at Begining Working Perfect

LL.insertAtBegining(20)
LL.insertAtBegining(30)
LL.insertAtBegining(40)
LL.insertAtBegining(50)
LL.insertAtBegining(60)
result = LL.insertAtBegining(70)
# print("Tail:",result)

# Insert at End working Perfect
# LL.insertAtEnd(20)
# LL.insertAtEnd(30)
# LL.insertAtEnd(40)
# LL.insertAtEnd(50)
# LL.insertAtEnd(60)
# LL.insertAtEnd(70)


# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# result2 = LL.deleteAtEnd()
# print("Tail is at:",result2)


# Delete from begining is Working Perfect

# LL.deleteFromBegining()
# LL.deleteFromBegining()
# LL.deleteFromBegining()
# LL.deleteFromBegining()
# LL.deleteFromBegining()
# LL.deleteFromBegining()
LL.insertAfterAnotherNode(65,1)
LL.printLinkedList()





    






 