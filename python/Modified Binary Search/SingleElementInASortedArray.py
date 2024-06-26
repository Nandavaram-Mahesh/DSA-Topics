
from collections import deque



def findSingleElement(nums,left,right):
    
    # Two pointers Approach - Time Complexity - O(N)

    # while right<len(arr):

    #     if len(arr)==1:
    #         return 0
        
    #     if(len(arr)<3):
    #         if(arr[left]==arr[right]):
    #             return None
    #         else:
    #             return[0,1]

    #     if(arr[left]==arr[right]):
    #         if(left==len(arr)-3):
    #              return right+1
    #         left = right+1
    #         right = left+1
    #     else:
    #         return left

    # ----------------------------------------------------------------------

    # HashMap Approach - Time Complexity - O(N) , Space Complexity - O(N) 
        
        # hashMap = {}
        # for i in arr:
        #     if i in hashMap:
        #           hashMap[i] += 1
        #     else:
        #           hashMap[i] = 1 
        
        # # return hashMap
        # singleElem = 0
        # for key in hashMap.keys():
        #       if(hashMap[key]==1):
        #         singleElem = key
        
        # return arr[singleElem]

   
    #  -------------------------------------------------------------------------

    # Stack Approach - Time Complexity - O(N) , space Complexity -O(N)
    
    # stack = deque()

    # for i in arr:
    #     if i not in stack:
    #         stack.append(i)
    #     else:
    #         stack.pop()

    # return stack[-1] 

    left = 0
    right = len(nums)-1

    while left!=right:

        mid = left+(right-left)//2

        if(mid%2==1):
            mid-=1

        if(nums[mid]==nums[mid+1]):
            left = mid+2
        else:
            right = mid

    return nums[left]






# Driver Code
arr = [1,1,2,3,3,4,4,5,5]
arr1=[1,1,3]
arr2 =[3,1]

left = 0

right = 1

result = findSingleElement(arr,left,right)

print(result)










