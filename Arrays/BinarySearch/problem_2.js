

/*
1. Given a sorted Array
2.Given a sum_value
3. Find the total_pairs whose sum is equal to sum_value


*/

// BruteForce Approach TimeComplexity-O(n**2)

function bruteForceFindingParis(arr,sum_value){
    let pairs=0
    for(let i=0;i<arr.length;i++){
        for(let j=i+1;j<arr.length;j++){
            if(arr[i]+arr[j]==sum_value){
                pairs+=1
            }
        }
    }
    return pairs

}

// Moderate Solution



// Optimized Way // Two Pointer Approach
function findpairs(arr,left,right,sum_value){

    while(left<=right){
        if(arr[left]+arr[right] === sum_value){
            return {[left]:arr[left],[right]:arr[right]}
        }
        else if(arr[left]+arr[right] > sum_value){
            right = right-1
            return findpairs(arr,left,right,sum_value)
        }else if(arr[left]+arr[right] < sum_value){
            left = left+1
            return findpairs(arr,left,right,sum_value)
        }
    return -1
    }

}



const sortedArray = [20,40,60,70,80,90,120,140,240]


const result = findpairs(sortedArray,left=0,right=(sortedArray.length)-1,sum_value=210)
// console.log(result)

const bruteForceResult = bruteForceFindingParis(sortedArray,sum_value=140)

console.log(`bruteForceResult:${bruteForceResult}`)

const moderateResult = moderateFindingPairs(sortedArray,left=0,right=(sortedArray.length)-1,sum_value=210)

console.log(`moderateResult:${moderateResult}`)