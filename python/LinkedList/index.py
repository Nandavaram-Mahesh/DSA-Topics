class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr= None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    # Insert new node at the start of the list

    def insertAtTheBegining(self, new_data):
        
        ## create a new node for the new_data
        new_node = Node(new_data)
        
        ## insertion at the beginning of the linked list
        new_node.nextPtr = self.head
        self.head = new_node
        print(new_node)
    
     ## insert the new node at the end of the linked list
    
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
    
    ## insert the new node after any of the previous node
    def insertAfterNode(self,prev_node,new_data):
        # Check if previous node is present , if not terminate.
        if prev_node is None:
            print("Given node must be available in your linked list")
            return
        
        ## create a new linked List
        new_node = Node(new_data)
        new_node.nextPtr = prev_node.nextPtr
        prev_node.nextPtr = new_node

    # Time Complexity -
        #  Worst Case (Element at end of Linked list) - O(n)
        #  Best Case (Element at begining of Linked list) - O(1)

    ## Delete the node at given position
    def deleteNode(self,pos):
        
        if self.head is None:
            return
        
        temp = self.head

        for i in range(pos-1):
            temp = temp.nextPtr
            if temp is None:
                return
        tempPtr = temp.nextPtr.nextPtr
        temp.nextPtr = None
        temp.nextPtr = tempPtr

    ## Count the no of nodes in the Linked List
    def countNodes(self):
        count = 0 
        temp = self.head
        while temp:
            count+=1
            temp = temp.nextPtr
        return count
    
    # Time Comeplexity -O(n) 
    ## Search Given Node in the Linked List
    def searchNode(self,nodeData):
       
        if self.head is None:
            return
        
        temp = self.head

        while temp:
            if (temp.data == nodeData):
                return True
            temp = temp.nextPtr
        return False

  
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextPtr


 ## Merge Two Sorted Linked List


# TIme Complexity - O(n)
def mergeLinkedList(head1,head2):
    temp = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1
    
    if head1.data<=head2.data:
        temp = head1
        temp.nextPtr = mergeLinkedList(head1.nextPtr,head2)
    else:
        temp = head2
        temp.nextPtr = mergeLinkedList(head1,head2.nextPtr)
    
    return temp

## Driver code
# llist = LinkedList()
# llist.insertAtTheBegining(50)
# llist.insertAtTheBegining(40)
# llist.insertAtTheBegining(30)
# llist.insertAtTheBegining(25)
# llist.insertAtTheBegining(20)
# llist.insertAtTheBegining(10)
# llist.printLinkedList()

 

# llist.insertAtEnd(500)
# llist.insertAtEnd(400)
# llist.insertAtEnd(300)
# llist.insertAtEnd(200)
# llist.insertAtEnd(100)
# llist.printLinkedList()


# llist.insertAfterNode(llist.head.nextPtr, 25)
# print("Insertion of nodes after second node of the linked list:")
# llist.printLinkedList()

# print("Deletion:")
# llist.deleteNode(1)
# llist.printLinkedList()

# countOfNodes = llist.countNodes()
# print("Nodes Count:",countOfNodes)

# nodeData = 700
# searchResult = llist.searchNode(nodeData)
# print(searchResult)

llist1 = LinkedList()
llist1.insertAtEnd(10)
llist1.insertAtEnd(20)
llist1.insertAtEnd(30)
llist1.insertAtEnd(40)
llist1.insertAtEnd(50)

llist2=LinkedList()
llist2.insertAtEnd(11)
llist2.insertAtEnd(22)
llist2.insertAtEnd(33)
llist2.insertAtEnd(44)
llist2.insertAtEnd(55)

# Merge LinkedList
llist3 = LinkedList()
llist3.head = mergeLinkedList(llist1.head,llist2.head)
llist3.printLinkedList()