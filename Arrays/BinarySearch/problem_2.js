// Two Pointer Approach


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



const sortedArray = [20,40,60,80,90,120,240]


result = findpairs(sortedArray,left=0,right=(sortedArray.length)-1,sum_value=210)
console.log(result)