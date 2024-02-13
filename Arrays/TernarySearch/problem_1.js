
// Brute Force

/*
    1. Loop through the array 
    2. check if the current element is equal to the given value 
    3. if it is equal then return the index of it
    4. else keep looping till the end of the arr
    5. if no element matches then finally return -1 
 */





// optimized solution
function findValueUsingTernarySearch(arr,left,right,searchValue){

    let mid1 = Math.floor(left+(right-left)/3)
    let mid2 = Math.floor(right-(right-left)/3)

    while(left<=right){
        if(arr[mid1]===searchValue){
            return mid1
        }
        else if(arr[mid2]===searchValue){
            return mid2
        }
        else if(arr[mid1]>searchValue){
            right = mid1-1
            return findValueUsingTernarySearch(arr,left,right,searchValue)
        }
        else if(arr[mid2]<searchValue){
            left = mid2+1
            return findValueUsingTernarySearch(arr,left,right,searchValue)
        }
        else if(arr[mid1]<searchValue<arr[mid2]){
            left = mid1+1
            right = mid2-1
            return findValueUsingTernarySearch(arr,left,right,searchValue)
        }
    }
    return -1
}

const sortedArray = [20,25,47,56,59,63,65,79,82]

const result = findValueUsingTernarySearch(sortedArray,left=0,right=(sortedArray.length)-1,searchValue=59)

console.log(`Result:${result}`)