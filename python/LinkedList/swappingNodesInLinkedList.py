class Node:
    def __init__(self,nodeData):
        self.nextPtr = None
        self.nodeData = nodeData

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,nodeData):
        
        new_node = Node(nodeData)

        if self.head is None:
            self.head = new_node
            return 

        temp = self.head

        while temp.nextPtr:
            temp = temp.nextPtr
        
        temp.nextPtr = new_node


    # def swappingNodes(self,k):
    #     # count the no of nodes in the linked list
        
    #     # k - kth node from the start
         
    #     temp = self.head
    #     count = 0
    #     while temp:
    #         temp = temp.nextPtr
    #         count+=1
        
    #     # Find the kth node from the last

    #     k_node_from_last = count-k

    #     # loop till kth node from start
    #     prev1 = None
    #     temp1 = self.head
        
    #     for i in range(k-1):

    #         prev1 = temp1
    #         temp1=temp1.nextPtr
        
        
    #     temp1_nextPtr = temp1.nextPtr

    #     # return prev1.nodeData , temp1.nodeData,temp1_nextPtr.nodeData           
    #     # ---- result -(1,5,8)

    #     # #loop till the kth node from last

    #     prev2 = None
    #     temp2 = self.head
        
    #     for i in range(k_node_from_last):
    #         prev2 = temp2
    #         temp2 = temp2.nextPtr
        
    #     temp2_nextPtr = temp2.nextPtr

    #     # return prev2.nodeData,temp2.nodeData , temp2_nextPtr.nodeData   
        
    #     # -------- Result- (7,4,6)

    #     prev2.nextPtr = temp1
    #     temp1.nextPtr = temp2_nextPtr
    #     prev1.nextPtr = temp2
    #     temp2.nextPtr = temp1_nextPtr
    
    # Time Complexity - O(N) , space Complexity - O(1)
    def swappingNodesEffectively(self,k):

        front = None
        end = None
        curr = self.head

        count = 0
        while curr:
            count+=1
            if end is not None:
                end = end.nextPtr
            
            if count==k:
                front = curr
                end = self.head
            curr= curr.nextPtr

        #swapping nodes
        temp = front.nodeData
        front.nodeData = end.nodeData
        end.nodeData = temp 

    # print LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.nodeData)
            temp = temp.nextPtr



llist1 = LinkedList()
llist1.insertAtEnd(7)
llist1.insertAtEnd(4)
llist1.insertAtEnd(6)
llist1.insertAtEnd(1)
llist1.insertAtEnd(5)
llist1.insertAtEnd(8)

llist1.printList()

print("----------------------------")


# result = llist1.swappingNodes(5)
# print(result)
llist1.swappingNodesEffectively(5)
llist1.printList()