
// // Brute Force Solution      TimeComplexity-O(n^2)
// function findValue(arr,searchValue){
//     for(let i=0;i<arr.length;i++){
//         for(let j=0;j<arr.length;j++){
//             if(arr[i][j]==searchValue){
//                 return {row:i,column:j}
//             }
//         }
//     }
//     return -1
// }

// // Optimized Solution   TimeComplexity - O(log m*n )

// function searchValueInTwoDArray(arr,left,right,searchValue){
//     let mid = Math.floor(left+(right-left)/2)
//     let row_num = Math.floor(mid/n)
//     let column_num = mid%n
//     let mid_element =arr[row_num][column_num]
//     while (left<=right){
//         if(mid_element==searchValue){
//             return [row_num,column_num]
//         }
//         else if(mid_element<searchValue){
//             left = mid+1
//             return searchValueInTwoDArray(arr,left,right,searchValue)
//         }
//         else if(mid_element>searchValue){
//             right=mid-1
//             return searchValueInTwoDArray(arr,left,right,searchValue)
//         }
//     return -1
//     }

// }




// const twoDimensionalArray=[[1,2,3],[4,5,6],[7,8,9]]

// /*

//   0 1 2
// 0 1 2 3
// 1 4 5 6
// 2 7 8 9 

// */

// const result = findValue(twoDimensionalArray,searchValue=10)

// console.log(result)

// let m = twoDimensionalArray.length
// let n = twoDimensionalArray[0].length

// const twoDResult = searchValueInTwoDArray(twoDimensionalArray,left=0,right=(m*n)-1,searchValue=6)
// console.log(`twoDResult:${twoDResult}`)


let i=0
let j=5
function checkingReturn(){
while(i<j){
    if(i<j){
        i++
        // console.log('entering loop')
    } 
}
return -1
}

const result = checkingReturn()
console.log(result)
