# Given a linked list of 0s, 1s and 2s, sort it.

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
    
    # sort  0's - in front , 1's- middle , 2's - end of the LinkedList 
    def sortLinkedList(self):
        
        temp = self.head
        
        count0=0
        count1=0
        count2=0

        # Here we are counting the no of 0's,1's,2's
        while temp:
            if(temp.data==0):
                count0+=1
            elif(temp.data==1):
                count1+=1
            else:
                count2+=1
            temp = temp.nextPtr
        
        temp = self.head
        # Here we are checking the 0's,1's,2's count and based on that we are sorting them 
        while temp:
            if count0>0:
                temp.data = 0
                count0-=1
            elif count1>0:
                temp.data=1
                count1-=1
            else:
                temp.data=2
                count2-=1
            temp = temp.nextPtr
    

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
print("--------------------------------")
llist.sortLinkedList()
llist.printLinkedList()
