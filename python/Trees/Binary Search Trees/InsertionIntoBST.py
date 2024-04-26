class Node:
    def __init__(self,data):
        self.left= None
        self.right=None
        self.data= data


# Time Complexity - O(log n)
def insertIntoBST(root,val):
    
    if not root:
        return root
    else:
        # checking if the value is less than the data  
        if val<root.data:
            #  checking if root's left node is present , if it is then traverse till we the last left node
            if root.left:
                insertIntoBST(root.left,val)
            # when we reach the last left node and there is no further left node then we create a left node for the root node
            else:
                root.left = Node(val)                    
        else:
            #  checking if root's right node is present , if it is then traverse till we the last right node
            if root.right:
                insertIntoBST(root.right,val)
              # when we reach the last right node and there is no further right node then we create a right node for the root node
            else:
                root.right = Node(val)    

                
# Search in Binary Tree



# Deletion in the Binary Tree

 

        


# To check if the tree we created is a Binary Tree , we can do Inorder Traversal on the tree and see if the output is sorted
# If the output is sorted then it is a Binary Tree
def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data)
        inOrderTraversal(root.right)
        


# Driver Code
root = Node(8)


insertIntoBST(root,3)
insertIntoBST(root,10)
insertIntoBST(root,1)
insertIntoBST(root,6)


inOrderTraversal(root)