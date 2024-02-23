
function partitionAlgorithm(arr,leftIndex,rightIndex){
                                     /*  0, 1, 2, 3, 4, 5, 6, 7, 8 */  
    let pivotElem = arr[leftIndex]   /*[50,40,70,10,30,90,45,67,79] */
                                    /*  P  j           */
                                    /*  i           */
    let i= leftIndex

    for(let j = i+1;j<rightIndex+1;j++){
        if(arr[j]<pivotElem){
            i++
            [arr[i],arr[j]] = [arr[j],arr[i]]
        }
        
    }
    [arr[i],arr[leftIndex]] = [arr[leftIndex],arr[i]]

    return i


}


function quickSort(arr,leftIndex,rightIndex){

    if(leftIndex<rightIndex){
        let mid = partitionAlgorithm(arr,leftIndex,rightIndex)
        quickSort(arr,0,mid-1)
        quickSort(arr,mid+1,rightIndex)
    }
    return arr
}





const arr = [50,40,70,10,30,90,45,67,79]

const result =  quickSort(arr,0,(arr.length)-1) 
console.log(result)

