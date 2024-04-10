
# Time Complexity - O(n^2)
# Space Complexity  if we are sorting then - O(n)
def findThreeSumPairs(arr,target):
    # If the array is not sorted then sort the array  
    for i in range(len(arr)):
        left = i+1
        right = len(arr)-1
        while left<right:
            if((arr[i]+arr[left]+arr[right]) ==target):
                    return [arr[i],arr[left],arr[right]]
            elif((arr[i]+arr[left]+arr[right])<target):
                 left+=1
            else:
                 right-=1
    




arr = [1,3,4,6,8,20]
target = 31
result = findThreeSumPairs(arr,target)
print(result)