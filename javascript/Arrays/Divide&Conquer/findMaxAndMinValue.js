function findMaxAndMinValue(arr,startIndex,endIndex,minVal,maxVal){

    if(startIndex==endIndex){           /* If there is only one element in an array then that elem is min and max both */
        minVal=arr[startIndex]
        maxVal=arr[startIndex]
        return [minVal,maxVal]
    }
    else if(startIndex==endIndex-1){   /* [0,1]  - if two elements in array
                                           0 1         where startIndex = 0 , endIndex = 1  =>  startIndex = endIndex-1 = 1-1 = 0 */                                
            
            if(arr[startIndex]<arr[endIndex]){
                minVal = arr[startIndex]
                maxVal = arr[endIndex]
                return [minVal,maxVal]
            }
            else{
                minVal = arr[endIndex]
                maxVal = arr[startIndex]
                return [minVal,maxVal]
            }
    }
    else{
         let midVal = Math.floor(startIndex+(endIndex-startIndex)/2)

         let [minVal1,maxVal1] = findMaxAndMinValue(arr,startIndex,midVal,minVal,maxVal)
         let [minVal2,maxVal2] = findMaxAndMinValue(arr,midVal+1,endIndex,minVal,maxVal)
        
         if(minVal1<minVal2){
            minVal = minVal1
         }else{
          minVal = minVal2  
         }

         if(maxVal1<maxVal2){
            maxVal = maxVal2
         }else{
            maxVal = maxVal1
         }

        return [minVal,maxVal]

    }
}


const unsortedArray = [90,39,45,65,21,44,20,92]
let minValue = Infinity
let maxValue = 0
const [min,max] = findMaxAndMinValue(unsortedArray,startIndex=0,endIndex=(unsortedArray.length)-1,minValue,maxValue )
console.log(`minValue:${min} , maxValue:${max}`)