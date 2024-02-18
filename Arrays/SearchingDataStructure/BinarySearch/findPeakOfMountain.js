
function findMountainPeak(arr,leftIndex,rightIndex){

    while(leftIndex<=rightIndex){
        let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)
        if(arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]){      /*  */
            return arr[mid]
        }
        else if(arr[mid]>arr[mid-1] && arr[mid]<arr[mid+1]){
            leftIndex = mid+1
        }
        else if(arr[mid]>arr[mid+1] && arr[mid]<arr[mid-1]){
            rightIndex = mid-1
        }
    return -1
    }

}


const mountainArray = [1,2,3,4,5,6,55,51,50,49,48,45,42,40]

const result = findMountainPeak(mountainArray,leftIndex=0,rightIndex=(mountainArray.length-1))

console.log(result)