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

    if root:
        print(root.nodeData)
        preOrderTraversal(root.left)
        preOrderTraversal(root.right) 
    
def inOrderTraversal(root):
    
    if root:
        inOrderTraversal(root.left)
        print(root.nodeData)
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.nodeData)

node = Node(10)

root_node_left = insertNodeIntoSubTree(node,20,leftSubTreeflag=True)
root_node_right = insertNodeIntoSubTree(node,30,leftSubTreeflag=False)

root_node_left_left = insertNodeIntoSubTree(root_node_left,40,leftSubTreeflag=True)
root_node_left_right = insertNodeIntoSubTree(root_node_left,50,leftSubTreeflag=False)

root_node_right_left = insertNodeIntoSubTree(root_node_right,60,leftSubTreeflag=True)
root_node_right_right = insertNodeIntoSubTree(root_node_right,70,leftSubTreeflag=False)

# Output: 10 20 40 50 30 60 70
# preOrderTraversal(node)

# Output: 40 20 50 10 60 30 70
# inOrderTraversal(node)

# OutPut: 40 50 20 60 70 30 10
postOrderTraversal(node)