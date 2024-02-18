
function mergeProcedure(arr,leftIndex,mid,rightIndex){

    let noOfLSAElements = mid-leftIndex+1
    let noOfRSAElements = rightIndex-mid

    let leftSubArray = [0]*noOfLSAElements
    let rightSubArray=[0]*noOfRSAElements


    //  copy the elements from an array to the subarrays
    for(let m=0;m<noOfLSAElements;m++){
        leftSubArray[m]=arr[leftIndex+m]
    }
        
    
    for(let n=0;n<noOfRSAElements;n++){
        rightSubArray[n]=arr[mid+1+n]
    }

    let leftPointer =0
    let rightPointer = 0
    let k = 0

    while(leftPointer<noOfLSAElements && rightPointer<noOfRSAElements){

            if(leftSubArray[leftPointer]<rightSubArray[rightPointer]){
                arr[k] = leftSubArray[leftPointer]
                leftPointer+=1
                
            }
            else{
                arr[k] = rightSubArray[rightPointer]
                rightPointer+=1
                
            }
            k+=1
    }

    while(leftPointer<noOfLSAElements){
        arr[k] = leftSubArray[leftPointer]
        leftPointer+=1
        k+=1
    }
    while(rightPointer<noOfRSAElements){
        arr[k] = rightSubArray[rightPointer]
        rightPointer+=1
        k+=1
    }

    return arr

}

function mergeSort(arr,leftIndex,rightIndex){

    // small problem
    if(leftIndex == rightIndex){
        return arr[leftIndex]
    }

    else{
        // Dividing Part
        let mid =Math.floor(leftIndex+(rightIndex-leftIndex)/2)
        // Conquering Part 
        mergeSort(arr,leftIndex,mid)

        mergeSort(arr,mid+1,rightIndex)

        //  combining Part 
        let mergedArray = mergeProcedure(arr,leftIndex,mid,rightIndex)
        
        return mergedArray
    }
}

const numsArray = [10,20,30,40,11,21,31,41]

const combinedSortedArray = mergeSort(numsArray,leftIndex=0,rightIndex=((numsArray.length)-1)) 
console.log(combinedSortedArray)