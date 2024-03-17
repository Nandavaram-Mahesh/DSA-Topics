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
        
    
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.nextPtr

## Driver code
llist = LinkedList()
# llist.insertAtTheBegining(50)
# llist.insertAtTheBegining(40)
# llist.insertAtTheBegining(30)
# llist.insertAtTheBegining(25)
# llist.insertAtTheBegining(20)
# llist.insertAtTheBegining(10)
# llist.printLinkedList()

llist.insertAtEnd(500)
llist.insertAtEnd(400)
llist.insertAtEnd(300)
llist.insertAtEnd(200)
llist.insertAtEnd(100)
llist.printLinkedList()


llist.insertAfterNode(llist.head.nextPtr, 25)
print("Insertion of nodes after second node of the linked list:")
llist.printLinkedList()