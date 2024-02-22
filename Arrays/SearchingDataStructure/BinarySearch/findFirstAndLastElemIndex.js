/*
 Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

 */


function binarySearch(nums,target,leftBias){
    let i = -1
    let leftIndex=0
    let rightIndex = (nums.length)-1

    while(leftIndex<=rightIndex){
        let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)
        if(nums[mid]>target){
            rightIndex = mid-1
        }else if(nums[mid]<target){
            leftIndex = mid+1
        }else{
             i = mid 
            if(leftBias){
                rightIndex = mid-1
            }else{
                leftIndex = mid+1
            }
        }
    }
    return i
}


const nums = [5,7,7,8,8,10]
const target = 8

const left = binarySearch(nums,target,true)
const right= binarySearch(nums,target,false)

console.log(left,right)