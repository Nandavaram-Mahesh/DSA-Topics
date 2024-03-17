function countPairs (nums, target) {
    nums.sort((a, b) => a-b); // sort the vector nums
    let count = 0; // variable to store the count
    let left = 0; // variable to store the left
    let right = nums.length-1; // variable to store the right
    while(left < right){ // loop until left is less than right
        if(nums[left] + nums[right] < target){ // if nums[left] + nums[right] is less than target
            count += right-left; // update the count
            left++; // increment the left
        }
        else{ // else
            right--; // decrement the right
        }
    }
    return count; // return the count
};


// function getCountPairs(nums,target){
//     let count=0
//     let left =0
//     let right = nums.length -1 
// // step 1 : Sort the array
//     nums.sort((a, b) => a-b)
// //  loop through the array till left_index < right_index  
    
//     while(left<right){

//         if(nums[left]+nums[right]<target){
//             count+=right-left
//             left++
//         }
//         else{
//              right--
//         }
   
//     }
//     return count 
// }

let nums = [-6,2,5,-2,-7,-1,3]
let target = -2

result = countPairs(nums,target)
console.log(result)

// result =getCountPairs(nums,target)

// console.log(result)