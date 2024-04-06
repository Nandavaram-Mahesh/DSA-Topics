
def recursiveBinarySearch(arr,left,right,target):
    # If the first element in array is not less than the last element then it is DESC order
    if not arr[0]<arr[-1]:
        
        if(left<=right):
            mid = left+(right-left)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                return recursiveBinarySearch(arr,mid+1,right,target)
            else:
                return recursiveBinarySearch(arr,left,mid-1,target)
        else:
            return -1

    # If first element is smaller than last element then it is ASC
    else:
        if(left<=right):
            mid = left+(right-left)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                return recursiveBinarySearch(arr,left,mid-1,target)
            else:
                return recursiveBinarySearch(arr,mid+1,right,target)
        else:
            return -1













# Driver Code

descArr = [40,20,15,10,1]

ascArr = [ 1,10,15,20,40]

result1 = recursiveBinarySearch(descArr,left = 0,right=len(descArr)-1,target = 11)

result2 = recursiveBinarySearch(ascArr,left = 0,right=len(descArr)-1,target = 15)

print(result1)

print(result2)