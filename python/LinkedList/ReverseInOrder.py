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
    # Time Complexity - O(N) , Space Complexity-O(N)
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


    def inplaceReversalInOrder(self):

        # If no head
        if not self.head:
            return self.head

        ## Find the Middle Node of Linked List
        
        # Use Tortoise and Hare Approach

        tortoise = self.head
        hare = self.head

        while hare and hare.nextPtr:
            tortoise = tortoise.nextPtr
            hare = hare.nextPtr.nextPtr
    
        ## Reverse the second Half
        prev = None
        curr = tortoise
        next = tortoise

        while curr:

            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next
        
        ## Merge the First Half and the second Half
        
        # This points to the first element in the first half 
        first = self.head
        
        # This points to the first element in the second half that is rotated
        second = prev

        while second.nextPtr:
            temp = first.nextPtr
            prev = second.nextPtr
            first.nextPtr = second
            second.nextPtr = temp
            first = temp
            second = prev



    


    # print LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.nodeData)
            temp = temp.nextPtr


def reverseInOrder(head1,head2,llist3):

    # count the no of nodes in the Linked List
    temp = head1
    count = 0
    while temp:
        temp = temp.nextPtr
        count+=1
    
    
    
    temp1 = head1
    temp2 = head2
    while count>(count//2):
        if count%2==1:
          llist3.insertAtEnd(temp1.nodeData)
          temp1 = temp1.nextPtr
        else:
            llist3.insertAtEnd(temp2.nodeData)
            temp2 = temp2.nextPtr
        count-=1

    

llist1 = LinkedList()
llist1.insertAtEnd(1)
llist1.insertAtEnd(2)
llist1.insertAtEnd(3)
llist1.insertAtEnd(4)
llist1.insertAtEnd(5)
llist1.insertAtEnd(6)

llist1.printList()
# ------------------------
print("----------------------------")
# llist1.insertAtEnd(0)
# llist1.insertAtEnd(6)
# llist1.insertAtEnd(7)
llist1.inplaceReversalInOrder()
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
# print("-----------------------------")
# llist3 = LinkedList()
# reverseInOrder(llist1.head,llist2.head,llist3=llist3)
# llist3.printList()




