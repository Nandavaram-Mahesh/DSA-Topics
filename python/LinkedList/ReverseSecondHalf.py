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

    def replaceSecondHalf(self):
        # step-1: Loop through the entire linkedList and count no of nodes

        temp = self.head
        count = 0
        
        while temp:
            temp = temp.nextPtr
            count+=1
        
        #step2: find Mid value
        
        left = 0
        right = count-1
        mid =  left+(right-left)//2

        # step3: Loop till mid and set curr, next,prev pointers

        temp = self.head

        for i in range(mid-1):
            temp = temp.nextPtr

        curr = temp.nextPtr
        next = temp.nextPtr
        prev = None

        # step4: Loop till curr is not none
        
        while curr:
            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next
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
llist1.printList()
print("----------------------------")
result = llist1.replaceSecondHalf()
llist1.printList()