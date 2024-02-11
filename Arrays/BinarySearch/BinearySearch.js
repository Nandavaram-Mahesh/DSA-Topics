function binarySearch(arr, left, right, searchValue) {
    let mid = Math.floor(left + (right - left) / 2)
    console.log(`mid:${mid}`)
    // If array has only one element 
    if (arr.length === 1 ) {
        if (arr[left] == searchValue) return 0
        return -1
    }
    // if array has multiple elements 
    else {
        while (left <= right) {

            if (arr[0] == searchValue) {
                return 0
            }
            else {
                if (arr[mid] == searchValue) {
                    return mid
                }
                else if (arr[mid] < searchValue) {
                    return binarySearch(arr, mid + 1, right, searchValue)
                }
                else {
                    return binarySearch(arr, left, mid - 1, searchValue)
                }
            }
            return -1
        }
    }
}



// function binarySearch(arr,left,right,searchValue){
//     let mid = Math.floor(left+(right-left)/2)
//     console.log(`mid:${mid}`)
//  // If array has only one element 
//     if(left==right){          
//         if(arr[left]==searchValue) return searchValue
//         return -1
//     }
//     // if array has multiple elements 
//     else{
//         while (left<=right){

//             if(arr[mid]==searchValue){
//                 return mid
//             }
//             else if(arr[mid]<searchValue){
//                left=mid+1
//             }
//             else{
//                right=mid-1
//             }
//         return -1 
//         }
//     }



const sameElemSortedArray = [80, 80, 80, 80]

const singleElemArray = [70]

const diffElemArray = [10,20,30,40,50,60,70]

const sameElementsResult = binarySearch(sameElemSortedArray, left = 0, right = 4, searchValue = 80)

const singleElemResult = binarySearch(singleElemArray, left = 0, right = 0, searchValue = 80)

const diffElemResult = binarySearch(diffElemArray, left = 0, right = 6, searchValue = 50)

console.log(sameElementsResult)
console.log(singleElemResult)
console.log(diffElemResult)
