function findMaxAndMinValueRevision(arr,leftIndex,rightIndex,minVal,maxVal){

    if(leftIndex==rightIndex){
        return [minVal=maxVal=arr[leftIndex]]
    }else if(leftIndex = rightIndex-1){
        if(arr[rightIndex]<arr[leftIndex]){
            minVal = arr[rightIndex]
            maxVal = arr[leftIndex]
        }else{
            maxVal = arr[rightIndex]
            minVal = arr[leftIndex]
        }
        return [minVal,maxVal]
    }else{

            let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)

            let[minVal1,maxVal1] = findMaxAndMinValueRevision(arr,leftIndex,mid)
            let[minVal2,maxVal2] = findMaxAndMinValueRevision(arr,leftIndex,mid)

            if(minVal1<minVal2){
                minVal=minVal1
            }else{
                minVal=minVal2
            }

            if(maxVal1>maxVal2){
                maxVal = maxVal1
            }else{
                maxVal = maxVal2
            }
            return [minVal,maxVal]
        
    }
}

const unsortedArray = [90,39,45,65,21,44,20,92]
let minValue = Infinity
let maxValue = 0
const [min,max] = findMaxAndMinValueRevision(unsortedArray,startIndex=0,endIndex=(unsortedArray.length)-1,minValue,maxValue )
console.log(`minValue:${min} , maxValue:${max}`)