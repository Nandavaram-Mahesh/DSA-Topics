class MaxHeap:
    def __init__(self):
        self.heap=[]

    # Inserting the values into the heap
    # Time Complexity - O(log n)
    def insert(self, val):
        # here we are appending value to the leaf node 
        self.heap.append(val)
        # then we are performing the percolateUp from bottom to top to ge the maxHeap property
        self.__percolateUp(len(heap)-1)
    
    # Get the max val from the heap(i.e the top most element)
    # Time Complexity-O(1)
    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    # Delete the max val from the heap
    # Time Complexity-O(log n)
    def removeMax(self):
        # if there is more than one node
        if(len(self.heap)>1):
            maxVal = self.heap[0]
            # here we are swapping  the root node with the last node  
            self.heap[0] = self.heap[-1]
            # then deleting the last node
            del self.heap[-1]
            # then performing heapify from top to bottom to get a valid Maxheap
            self.__maxHeapify(0)

            return maxVal
        # if there is exactly one node
        elif(len(self.heap)==1):
            maxVal = self.heap[0]
            del self.heap[0]
            return maxVal
        # if there is no node
        else:
            return None
        
    # restoring the heap property by gng from node to the root (bottom to top)
    # Time Complexity- O(log n)
    def __percolateUp(self, index):
        # To the parent node
        parent = (index-1)//2
        # Base case condition
        if (index<=0):
            return
        elif(self.heap[parent]<self.heap[index]):
            # storing the parent value in a tmp variable
            tmp = self.heap[parent]
            # swapping the parent with the child 
            self.heap[parent] = self.heap[index]
            # setting child to parent data
            self.heap[index] = tmp

            # recursively call the function till it reaches the root node
            self.__percolateUp(parent)
    
    # restores the heap property from given node to the leaf nodes (top to bottom)
    # Time Complexity-O(log n)
    def __maxHeapify(self, index):
        # left node index
        left = (2*index)+1
        # right node index
        right = (2*index)+2
        # a var to store the parent node value 
        largest = index

        # we are checking if the parent node has a left child 
        # If the left child is greater than parent then we are storing largest = leftChild index
        if(len(self.heap)>left and self.heap[largest]<self.heap[left]):
            largest = left
        
        # we are checking if the parent node has a right child 
        # If the right child is greater than parent then we are storing largest = rightChild index
        if(len(self.heap)>right and self.heap[largest]<self.heap[right]):
            largest = right
        
        # Checking if parent node is not the max value 
        if largest!=index:
            
            # storing the parent node value in temp variable
            tmp = self.heap[index]
            
            # swapping the parent node with the largest value 
            self.heap[index] = self.heap[largest]

            # changing the largest value  to the parent value   
            self.heap[largest] = tmp

            self.__maxHeapify(largest)

    # Building the heap from a given Array
    # Time Complexity - O(n)
    def buildHeap(self, arr):
        self.heap = arr
        for i in range((len(arr)-1),-1,-1):
            self.__maxHeapify(i)



heap = MaxHeap()

heap.buildHeap([10,20,30,40,50,60,70,80,90,100])

print(heap.heap)