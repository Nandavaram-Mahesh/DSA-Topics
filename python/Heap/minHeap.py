class MinHeap:
    def __init__(self):
        self.heap = []
    
    # Inserting the values into the heap
    # Time Complexity - O(log n)
    def insert(self,val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap)-1)
    
    # Get the min val from the heap(i.e the top most element)
    # Time Complexity-O(1)
    def getMin(self):
        if self.heap:
            self.heap[0]
        return None

    # Delete the min val from the heap
    # Time Complexity-O(log n)
    def removeMin(self):
        
        # if there is more than one node
        if(len(self.heap)>1):
            minVal = self.heap[0]
            # here we are swapping  the root node with the last node  
            self.heap[0] = self.heap[-1]
            # then deleting the last node
            del self.heap[-1]
            # then performing heapify from top to bottom to get a valid Minheap
            self.__minHeapify(0)
            return minVal
        
        # if heap has only one element
        elif(len(self.heap)==1):
            minVal = self.heap[0]
            del self.heap[0]
            return minVal
        
        # if heap doesn't have any element
        else:
            return None
    # restoring the heap property by gng from node to the root (bottom to top)
    # Time Complexity- O(log n)    
    def __percolateUp(self,index):
        parent = (index-1//2)
         # Base case condition
        if (index<=0):
            return
        elif(self.heap[parent]>self.heap[index]):
            # storing the parent value in a tmp variable
            tmp = self.heap[parent]
            # swapping the parent with the child 
            self.heap[parent] = self.heap[index]
            # setting child to parent data
            self.heap[index] = tmp

            # recursively call the function till it reaches the root node
            self.__percolateUp(parent)

    def __minHeapify(self,index):
         # left node index
        left = (2*index)+1
        # right node index
        right = (2*index)+2
        # a var to store the parent node value 
        smallest = index

        # we are checking if the parent node has a left child 
        # If the left child is smaller than parent then we are storing smallest = leftChild index
        if(len(self.heap)>left and self.heap[smallest]>self.heap[left]):
            smallest = left
        
        # we are checking if the parent node has a right child 
        # If the right child is smaller than parent then we are storing smallest = rightChild index
        if(len(self.heap)>right and self.heap[smallest]>self.heap[right]):
            smallest = right
        
        # Checking if parent node is not the min value 
        if smallest!=index:
            
            # storing the parent node value in temp variable
            tmp = self.heap[index]
            
            # swapping the parent node with the smallest value 
            self.heap[index] = self.heap[smallest]

            # changing the smallest value  to the parent value   
            self.heap[smallest] = tmp

            self.__minHeapify(smallest)

    def buildHeap(self,arr):
        self.heap = arr
        for i in range((len(arr)-1),-1,-1):
            self.__minHeapify(i)




heap = MinHeap()

heap.buildHeap([10,20,30,40,50,60,70,80,90,100])

print(heap.heap)