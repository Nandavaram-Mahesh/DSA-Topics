/*
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad. Suppose you have n version and you want to find out the first bad one,
which causes all the following ones to be bad. Also, talk about the time complexity of
your code.

Test Cases:
Input: [0,0,0,1,1,1,1,1,1]
Output: 3
Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of
the first 1 is at 3. Thus, the output is 3

 */


// Brute Force Solution Time Complexity - O(n)

function findFirstFailedTest(arr,searchValue){

    for(let i=0;i<arr.length;i++){

        if(arr[i]==searchValue){
            return i
        }
    }
    return -1
}


const testsArray = [0,0,0,0,1,1,1,1,1]

const result = findFirstFailedTest(testsArray,searchValue=1)

console.log(result)



//  Optimized Solution Time Complexity-O(log n)
 
function findFirstFailedTestIndex(arr,left,right,searchValue){ 

    let mid = Math.floor(left+(right-left)/2)

    while(left<=right){

        if(arr[mid]===searchValue && arr[mid-1]!=searchValue){
            return mid
        }
        else if(arr[mid]===searchValue && arr[mid-1]===searchValue){
            right = mid-1
            return findFirstFailedTestIndex(arr,left,right,searchValue)
        }else if(arr[mid]!=searchValue){
            left = mid+1
            return findFirstFailedTestIndex(arr,left,right,searchValue)
        }
    return -1
    }

}


const optResult = findFirstFailedTestIndex(testsArray,left=0,right=(testsArray.length)-1,searchValue=1)

console.log(`optResult:${optResult}`)