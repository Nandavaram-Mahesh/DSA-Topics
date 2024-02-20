// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
/**
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
2 is the missing number in the range since it does not appear in nums.
 */

// BruteForce Approach
function findMissingElement(nums){
    let prevCount =0
    let currentCount=0
    for(let i=0;i<nums.length+1;i++){
        for(let j=0;j<nums.length+1;j++){
            if(i==nums[j]){
                currentCount+=1                /* if we find a num in the given array we are increasing the count and checking if the prev count is not equal to currentcount , 
                                                if it is equal it means we didn't find an element and we will return the element that  we didn't find*/
            }
        }
        if(currentCount!=prevCount+1){             
            return i
        }
        prevCount=currentCount
    } 
}


const nums=[1,0,3,2,5]
const result = findMissingElement(nums)
console.log(result)