
// Time Complexity - O(n^2)
function sortArray(arr){
    let n = arr.length
    for (let i=0;i<n;i++){
        let min_indX=i
        for(let j=i+1;j<n;j++){
            if(arr[min_indX]>arr[j]){
                min_indX=j
            }
        }
        [arr[i],arr[min_indX]]=[arr[min_indX],arr[i]]
    }
    return arr
}








const unsortedArr = [30,60,80,70,20,5,15]

const result = sortArray(unsortedArr)
console.log(result)