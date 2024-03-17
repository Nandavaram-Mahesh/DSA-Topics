
function mergeProcedure(arr,leftIndex,mid,rightIndex){
    /* n1 -> number of elements in the left subarray(i, mid) */
    let n1 = mid-leftIndex+1 /*NoOfElements =  HigherIndex-lowerIndex+1*/
    /* n2 -> number of elements in the right subarray(mid+1, j)*/
    let n2 = rightIndex-mid /*NoOfElements =  HigherIndex-lowerIndex+1*/

    let leftSubArray = new Array(n1)
    let rightSubArray= new Array(n2)


    //  copy the elements from an array to the subarrays
    for(let m=0;m<n1;m++){
        leftSubArray[m]=arr[leftIndex+m]
    }
        
    
    for(let n=0;n<n2;n++){
        rightSubArray[n]=arr[mid+1+n]
    }

    let leftPointer =0
    let rightPointer = 0
    let k = leftIndex

    //  returning a sorted subarray
    while(leftPointer<n1 && rightPointer<n2){

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

    while(leftPointer<n1){
        arr[k] = leftSubArray[leftPointer]
        leftPointer+=1
        k+=1
    }
    while(rightPointer<n2){
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