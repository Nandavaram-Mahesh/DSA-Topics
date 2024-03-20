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
        # create three pointers curr, next, prev

        curr = self.head
        next = None
        prev = None
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



def isPalindrome(head1,head2):
    temp1 = head1
    temp2 = head2
    count = 0
    while temp1:
        if(temp1.nodeData==temp2.nodeData):
            count+=1
            temp1 = temp1.nextPtr
            temp2 = temp2.nextPtr
    if(count!=0):
        return True
    else:
        return False    


llist1 = LinkedList()
llist1.insertAtEnd(1)
llist1.insertAtEnd(2)
llist1.insertAtEnd(2)
llist1.insertAtEnd(3)
llist1.printList()

print('-------------------------')

llist2 = LinkedList()
llist2.insertAtEnd(1)
llist2.insertAtEnd(2)
llist2.insertAtEnd(2)
llist2.insertAtEnd(1)

llist2.reversalOfLinkedList()
llist2.printList()


result = isPalindrome(llist1.head,llist2.head)
print(result)
