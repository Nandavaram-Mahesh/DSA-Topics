from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr= None


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
    
    # check if the given LinkedList is palindrome
    def isPalindrome(self):
        # create a stack
        stack = deque()

        if self.head is None:
            return 
        
        temp1 = self.head

        while temp1:
            stack.append(temp1.data)
            temp1 = temp1.nextPtr
        

        temp2 = self.head
        while temp2:
            elem = stack.pop()
            if(elem != temp2.data):
                return False
            temp2 = temp2.nextPtr

        return True

    def isLinkedListpalindrome(self):
        tortoise = self.head
        hare = self.head

        while hare and hare.nextPtr:
            tortoise = tortoise.nextPtr
            hare = hare.nextPtr.nextPtr
        
        # return tortoise.data

        prev = None
        curr = tortoise.nextPtr
        next = tortoise.nextPtr

        while curr:
            next = curr.nextPtr
            curr.nextPtr = prev
            prev = curr
            curr = next

        tortoise.nextPtr = prev

        leftNode = self.head
        rightNode = tortoise.nextPtr

        while rightNode:
            if(leftNode.data!=rightNode.data):
                return False
            leftNode = leftNode.nextPtr
            rightNode = rightNode.nextPtr
        return True
    
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextPtr

## Driver code
llist = LinkedList()
llist.insertAtEnd(1)
llist.insertAtEnd(2)
llist.insertAtEnd(0)
llist.insertAtEnd(3)
llist.insertAtEnd(1)
# llist.printLinkedList()

result = llist.isLinkedListpalindrome()
print(result)
llist.printLinkedList()
