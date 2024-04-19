class Node:
    def __init__(self,nodeData,right=None,left=None):
        self.right=right
        self.left = left
        self.nodeData = nodeData


def insertNodeIntoSubTree(node,new_node_data,leftSubTreeflag): 
    if node:
        if leftSubTreeflag:
            node.left = Node(new_node_data)
            return node.left
        else:
            node.right = Node(new_node_data)
            return node.right



def preOrderTraversal(root):
    
    # initializing an empty stack
    stack = []
    # appending root node to the stack
    stack.append(root)

    # loop till stack has elements in it
    while len(stack)>0:
        # pop the top element in stack
        popped = stack.pop()

        # assign the popped element to the current_node
        current_node = popped

        print(popped.nodeData)

        # check if current_node has a right node , if it has then append that right node to the stack
        if(current_node.right):
            stack.append(current_node.right)

        # check if current_node has a left node , if it has then append that left node to the stack
        if(current_node.left):
            stack.append(current_node.left)


def postOrderTraversal(root):
    stack1 = []
    stack2= []

    # Append the root node to the stack1
    stack1.append(root)

    while len(stack1)>0:

        # pop the top element from stack1
        popped = stack1.pop()

        current_node = popped

        # Append the popped element to the stack2
        stack2.append(current_node)

        # check if current_node has left node , if so append it to stack1 
        if(current_node.left):
            stack1.append(current_node.left)

        # check if current_node has right node , if so append it to stack1
        if(current_node.right):
            stack1.append(current_node.right)

    while len(stack2)>0:
        popped = stack2.pop()
        print(popped.nodeData)

def inOrderTraversal(root):

    stack=[]
    
    current_node = root

    condition = True
    
    while condition:
        
        if current_node:
            stack.append(current_node)
            current_node = current_node.left
    
        elif len(stack)>0:
            popped = stack.pop()
            print(popped.nodeData)
            current_node = popped.right
        
        # if stack is empty set condition to false
        elif not len(stack)>0:
            condition = False



# Driver Code
node = Node(10)

root_node_left = insertNodeIntoSubTree(node,20,leftSubTreeflag=True)
root_node_right = insertNodeIntoSubTree(node,30,leftSubTreeflag=False)

root_node_left_left = insertNodeIntoSubTree(root_node_left,40,leftSubTreeflag=True)
root_node_left_right = insertNodeIntoSubTree(root_node_left,50,leftSubTreeflag=False)

root_node_right_left = insertNodeIntoSubTree(root_node_right,60,leftSubTreeflag=True)
root_node_right_right = insertNodeIntoSubTree(root_node_right,70,leftSubTreeflag=False)

# output:10 20 40 50 30 60 70
# preOrderTraversal(node)

# outPut:40 50 20 60 70 30 10 
# postOrderTraversal(node)


inOrderTraversal(node)