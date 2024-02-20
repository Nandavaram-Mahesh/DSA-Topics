/*   Find the first and last occurence of x
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  
2 5
Explanation: 
First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5. 
 
 */


// Time Complexity - O(logN)

function findFirstLastIndex(arr,n,target){

    let startIndex=0
    let endIndex=0
    let leftIndex = 0
    let rightIndex = n-1
        while(leftIndex<=rightIndex){

            let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)

            if(!startIndex && (arr[mid]==target && arr[mid]==arr[mid-1])){
                rightIndex = mid-1
            }
            else if(arr[mid]==target && arr[mid]!=arr[mid-1]){
                 startIndex = mid
                 leftIndex = mid+1
                 rightIndex = (n)-1
            }
            else if( startIndex && (arr[mid]==target && arr[mid]==arr[mid-1])){
                leftIndex = mid+1
            }
            else if(startIndex && (arr[mid]!=target && arr[mid-1]==target)){
                 endIndex = mid-1
                 return [startIndex,endIndex]
            }
            else if(arr[mid]<target){
                leftIndex = mid+1
            }
            else if(arr[mid]>target){
                rightIndex = mid-1
            }
    
        }
    
        return -1
    
}





let n=9
let x=5
const arr = [1, 3, 5, 5, 5, 5, 67, 123, 125] 

const result = findFirstLastIndex(arr,n,target=x)

console.log(result)