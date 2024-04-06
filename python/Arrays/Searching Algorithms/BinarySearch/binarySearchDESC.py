
def binarySearch(arr,left ,right,target):
    
    # Desc Order
    if not arr[0]<arr[-1]: 
        
        while left<=right:
            #calculating the mid value in every iteration 
            mid = left+(right-left)//2
            
            # If mid value is target then return  index
            if(arr[mid]==target):
                return mid
            # If mid value is greater than target then search right SubArray
            elif(arr[mid]>target):
                left = mid+1
            # If mid value is less than target then search left SubArray
            else:
                right = mid-1
        # If the target value is not found in the array then return -1    
        return -1
    # ASC Order
    else:
        while left<=right:

            mid = left+(right-left)//2

            if(arr[mid]==target):
                return mid
            # If mid value is greater than target then search left SubArray
            elif(arr[mid]>target):
                right = mid-1
             # If mid value is less than target then search right SubArray
            else:
                left = mid+1                
        return -1




# Driver Code

descArr = [40,20,15,10,1]

ascArr = [ 1,10,15,20,40]

result1 = binarySearch(descArr,left = 0,right=len(descArr)-1,target = 10)

result2 = binarySearch(ascArr,left = 0,right=len(descArr)-1,target = 10)

print(result1)

print(result2)