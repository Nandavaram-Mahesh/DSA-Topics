# Remove Nth Node From End of List

# Given a linked list of 0s, 1s and 2s, sort it.

class Node:
    def __init__(self,data,nextPtr=None):
        self.data = data
        self.nextPtr= nextPtr


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    # Insert the new node at the end of the list
    def insertAtEnd(self,new_data):
        
        ## create a new node for the new_data
        new_node = Node(new_data)
        
        ## check whether linked list is empty or different
        if self.head is None:
            self.head = new_node
            return
        
        ## insert the data at the end
        temp = self.head
        while temp.nextPtr:
            temp = temp.nextPtr

        temp.nextPtr = new_node  
    
    def deleteFromEnd(self,n):
        dummy_node = LinkedList(nextPtr = self.head)

        temp = self.head
        count = 0
        while temp:
            count+=1
            temp = temp.nextPtr
        noOfSteps = count-n

        temp = dummy_node
        while noOfSteps>0:
            noOfSteps-=1
            temp = temp.nextPtr
        temp.nextPtr = temp.nextPtr.nextPtr



    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextPtr

## Driver code
llist = LinkedList()
llist.insertAtEnd(1)
llist.insertAtEnd(0)
llist.insertAtEnd(1)
llist.insertAtEnd(0)
llist.insertAtEnd(2)
llist.printLinkedList()



# dummy_node = ListNode(next = head)
#         fastPtr = dummy_node
#         slowPtr = dummy_node
       
#         for i in range(1,n+2):
#             fastPtr = fastPtr.next
        
#         while fastPtr:
#             fastPtr = fastPtr.next
#             slowPtr = slowPtr.next
        
#         slowPtr.next = slowPtr.next.next
#         return head