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

    def reversalOfLinkedList(self):
        prev = None
        curr = self.head
        next = self.head

        while curr:
            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next
        
        self.head = prev
        

    # print LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.nodeData)
            temp = temp.nextPtr




llist1 = LinkedList()
llist1.insertAtEnd(1)
llist1.insertAtEnd(2)
llist1.insertAtEnd(2)
llist1.insertAtEnd(3)
llist1.printList()
print("----------------------------")
result = llist1.reversalOfLinkedList()
llist1.printList()