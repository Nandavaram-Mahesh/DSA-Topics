
// Time Complexity - O(n^2)

function sortArray(arr){
    let n = arr.length
    for(let i=0;i<n;i++){
        for(let j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
                
            }
        }
    }
    return arr
}








const unsortedArr = [30,60,80,70,20,5,15]

const result = sortArray(unsortedArr)
console.log(result)