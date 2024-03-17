
function mergeProcedure(arr,leftIndex,mid,rightIndex){
    // no.of elements in the leftSubArray(leftIndex,mid)
    let n1 = mid-leftIndex+1 /*HigherIndex-lowerIndex+1 */
    // no.of elements in the rightSubArray(mid+1,rightIndex)
    let n2 = rightIndex-mid
    
    let leftSubArray = new Array(n1)
    let rightSubArray = new Array(n2)

    


    for(let i=0;i<n1;i++){      /* loop till is endElement of leftSubArray */
        leftSubArray[i] = arr[leftIndex+i]
    }
    for(let j=0;j<n2;j++){  /* loop till is endElement of leftSubArray */
        rightSubArray[j] = arr[mid+1+j] 
    }
    
    let leftPointer= 0 /*pointer for leftSubArray */
    let rightPointer= 0 /*pointer for rightSubArray */
    let k = leftIndex /*pointer for finalSortedArray */
    
    let finalSortedArray = new Array(arr.length)

    while(leftPointer<n1 && rightPointer<n2){
        
        if(leftSubArray[leftPointer]<rightSubArray[rightPointer]){
            finalSortedArray[k] = leftSubArray[leftPointer]
            leftPointer+=1
        }else{
            finalSortedArray[k] = rightSubArray[rightPointer]
            rightPointer+=1
        }
        k+=1
    }

    while(leftPointer<n1){
        finalSortedArray[k] = leftSubArray[leftPointer]
        leftPointer+=1
        k+=1
    }
    while(rightPointer<n2){
        finalSortedArray[k] = rightSubArray[rightPointer]
        rightPointer+=1
        k+=1
    }

    return finalSortedArray
}

function mergeSort(arr,leftIndex,rightIndex){
    // If there is only one element
    if(leftIndex == rightIndex){
        return arr[leftIndex]
    }
    else{
        // Dividing part
        let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)
        // Conquering Part
        mergeSort(arr,leftIndex,mid)

        mergeSort(arr,mid+1,rightIndex)

        let mergedArray= mergeProcedure(arr,leftIndex,mid,rightIndex)
        
        return mergedArray 
    }
}

const numsArray = [10,20,30,40,11,21,31,41]

const combinedSortedArray = mergeSort(numsArray,leftIndex=0,rightIndex=((numsArray.length)-1)) 

console.log(combinedSortedArray)