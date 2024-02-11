// Scenario 1
/*
1. Given an array  
2. The array is not sorted
3. After some elements in the array all are infinites
4. Find the first infinite Index in the array

*/

// Scenario 2
/*
same as scenario 1 but here the array length is unknown and u cant use any arry length methods to find it.
*/


// assume "&" = infinite
// BruteForce Solution

function bruteForceFindIndex(arr,searchValue){

    for(let i=0;i<arr.length;i++){
        if (arr[i]==searchValue){
            return i
        }else if(i===(arr.length-1) && arr[i]!=searchValue){
            return `search value not found`
        }
    }
}

// Scenario 1 Solution
function findIndex(arr,left,right,searchValue){
    let mid=Math.floor(left+(right-left)/2)

    if(left===right && arr[mid]==searchValue){
        return mid
    }else if(left===right && arr[mid]!=searchValue){
        return -1
    }
    else{
        while(left<=right){
            if(arr[mid]==searchValue && typeof(arr[mid-1])=='number'){
                 return mid
            }else if(arr[mid]!=searchValue){
                left=mid+1
                return findIndex(arr,left,right,searchValue)
            }else if(arr[mid]==searchValue && typeof(arr[mid-1])!='number'){
                right = mid-1
                return findIndex(arr,left,right,searchValue)
            }
        return -1
        }
    }
   

}

// scenario 2 Solution - Where the length of the array is unknown 

function findIndexInUnknowArrLength(){
    
}



const unsortedArray =[-23,45,78,56,1,2,-6,8,9,"&","&","&","&","&","&","&","&","&","&","&","&","&","&","&","&","&","&"]

const bruteArray=[1,"&"]



const result  = findIndex(unsortedArray,left=0,right=25,searchValue="&")
// result  = findIndex(unsortedArray,left=0,right=0,searchValue="&")

console.log(`The index of the first Infinite is : ${result}`)



const bruteForceResult = bruteForceFindIndex(bruteArray,searchValue="&")

console.log(`bruteForeceSolution: ${bruteForceResult}`)


