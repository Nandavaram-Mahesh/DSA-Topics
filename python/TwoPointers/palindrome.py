
# Time Complexity -O(n/2)->O(n)
def two_pointers(array):
    left = 0
    right = len(array) - 1
    while left < right:

        if(array[left]!=array[right]):
            return False
        else:
            left = left + 1
            right = right -1
    return True 


str1 =["R","A","C","E","A","C","A","R"] 


str2=["R","A","C","E","C","A","R"]



result = two_pointers(str2)

print(result)