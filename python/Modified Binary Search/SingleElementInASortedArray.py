
from collections import deque



def findSingleElement(arr,left,right):
    
    # Two pointers Approach - Time Complexity - O(N)

    while right<len(arr):

        if len(arr)==1:
            return 0
        
        if(len(arr)<3):
            if(arr[left]==arr[right]):
                return None
            else:
                return[0,1]

        if(arr[left]==arr[right]):
            if(left==len(arr)-3):
                 return right+1
            left = right+1
            right = left+1
        else:
            return left


    
    pass






# Driver Code
arr = [1,1,2,3,3,4,4,5,5]
arr1=[1,1,3]
arr2 =[3,1]

left = 0

right = 1

result = findSingleElement(arr,left,right)

print(result)










