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

    # def reversalOfLinkedList(self):
    #     prev = None
    #     curr = self.head
    #     next = self.head

    #     while curr:
    #         next = curr.nextPtr
    #         curr.nextPtr = prev
    #         prev = curr
    #         curr = next
        
    #     self.head = prev
        
    def reverseFromLeftToRight(self,left,right):
        
        
        temp = self.head
        for i in range(1,left-1):
            temp = temp.nextPtr
        
        prev = None
        curr = temp.nextPtr
        next = temp.nextPtr

        # return prev.nodeData , curr.nodeData , next.nodeData
        for i in range(1,right):
            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next

        firstNode = temp.nextPtr
        firstNode.nextPtr = curr
        temp.nextPtr = prev
        

    # print LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.nodeData)
            temp = temp.nextPtr



llist1 = LinkedList()
llist1.insertAtEnd(1)
llist1.insertAtEnd(2)
llist1.insertAtEnd(3)
llist1.insertAtEnd(4)
llist1.insertAtEnd(5)
llist1.insertAtEnd(4)
llist1.insertAtEnd(3)
llist1.insertAtEnd(2)
llist1.insertAtEnd(1)
# ------------------------

# llist1.insertAtEnd(7)
# llist1.insertAtEnd(4)
# llist1.insertAtEnd(6)
# llist1.insertAtEnd(1)
# llist1.insertAtEnd(5)
# llist1.insertAtEnd(8)
llist1.printList()
print("----------------------------")
# llist2 = LinkedList()
# llist2.insertAtEnd(4)
# llist2.insertAtEnd(2)
# llist2.insertAtEnd(7)
# llist2.insertAtEnd(8)
# llist2.insertAtEnd(9)
# llist2.insertAtEnd(0)
# llist2.insertAtEnd(2)

# llist2.insertAtEnd(0)
# llist2.insertAtEnd(6)
# llist2.insertAtEnd(7)

# llist2.reversalOfLinkedList()
# llist2.printList()

llist1.reverseFromLeftToRight(left=1,right=9)
llist1.printList()
# result = llist1.reverseFromLeftToRight(left=2,right=5)
# print(result)

print("-----------------------------")



