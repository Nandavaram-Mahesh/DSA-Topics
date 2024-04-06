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
    def insertAtBegining(self,data):
        # create new node to insert
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # copy the head to the new_node next pointer
            new_node.nextPtr = self.head

            # Set the head and tail to point to new_node
            self.head = new_node
        
        return self.tail.data
        # # set the tail to the head nextPointer
        # self.tail = self.head.nextPtr

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
   
    # Time Complexity - O(n)
    def insertAfeterAnotherNode(self,data,index):
        new_node = Node(data)
        temp = self.head
        for i in range(0,(index-1)):
            temp = temp.nextPtr

        new_node.nextPtr = temp.nextPtr
        temp.nextPtr = new_node

    # Time Complexity- O(n)
    def deleteAtEnd(self):
        dummy_node = Node(nextPtr=self.head)
        # check if nodes exists
        if self.head is None:
            return
        
        curr = dummy_node
        next = dummy_node
        prev = dummy_node
        
        while curr.nextPtr is not None:
            next = curr.nextPtr
            prev = curr
            curr = next
        
        prev.nextPtr = None
        self.tail = prev
        

        return self.tail
    
    #Time Complexity-O(1)    
    def deleteFromBegining(self):
        
        if self.head is None:
            return
        
        self.head = self.head.nextPtr
        

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
LL.insertAtBegining(50)
LL.insertAtBegining(60)
result = LL.insertAtBegining(70)
print("Tail:",result)

# Insert at End working Perfect
# LL.insertAtEnd(20)
# LL.insertAtEnd(30)
# LL.insertAtEnd(40)
# LL.insertAtEnd(50)
# LL.insertAtEnd(60)
# LL.insertAtEnd(70)

# print()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# LL.deleteAtEnd()
# result2 = LL.deleteAtEnd()
# print("Tail is at:",result2)


# Delete from begining is Working Perfect

LL.deleteFromBegining()
LL.deleteFromBegining()
LL.deleteFromBegining()
LL.deleteFromBegining()
LL.deleteFromBegining()
LL.deleteFromBegining()

# LL.insertAfeterAnotherNode(65,1)
LL.printLinkedList()





    






 