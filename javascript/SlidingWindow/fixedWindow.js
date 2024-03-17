// BruteForce Approach
// Time Complexity - O(N*k)

function findMaximumAverageSubaaray(arr,k){

let maxAvg= -Infinity /* we are initializing this  for what If the subarray's average is -ve value , if we had initialized with zero then we would return 0 if the subrrays averages are -ve */

for(let i=0;i<arr.length;i++){
    let subarraySum=0  
    for(let j=0;j<k;j++){
        if(!((i+(k-1))>arr.length-1)){             /* this is for checking the subarray doesn't overflow main array ,if it doesn't overflow then calculate sum*/
            subarraySum+=arr[i+j]
        }else{
            break
        }
    }

    if(subarraySum!=0){
        maxAvg = Math.max(maxAvg,subarraySum/k)      /*This is for checking the max Average, we are comparing the consecutive averages here and taking maxAvg */
    }
}

if(maxAvg ==-Infinity){
    return 0
}
return maxAvg

}



// Sliding Window Technique

function MaxAvgUsingSlidingWindow(arr,k){
let windowSum = 0
let start = 0
let maxAvg = -Infinity

for(let end=0;end<arr.length;end++){
    windowSum+=arr[end]

    if(end-start+1 ==k){
        maxAvg = Math.max(maxAvg,windowSum/k)
        windowSum-=arr[start]
        start+=1
    }
   
}
return maxAvg
}


// Driver code
const arr = [1,12,-5,-6,50,3]

let k = 4

const bruteForceResult = findMaximumAverageSubaaray(arr,k)

const SlidingWindowResult = MaxAvgUsingSlidingWindow(arr,k)

console.log(bruteForceResult)
console.log(SlidingWindowResult)