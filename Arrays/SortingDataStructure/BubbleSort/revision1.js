
// ["Mahesh","Aravind","Sai","Pavan","Claudia","Richard","David"]
//     j         j+1


function sortContanctsByName(arr){
    let n = arr.length
    for(let i = 0;i<n-1;i++){
        for(let j=0;j<n-i-1;j++){           /*Since the last value is sorted in every iteration we reduce the size of the array with n-i-1  */
            if(arr[j]>arr[j+1]){
                [arr[j],arr[j+1]]=[arr[j+1],arr[j]]
            }
        }
    }
    return arr
}









const contacts = ["Mahesh","Aravind","Sai","Pavan","Claudia","Richard","David"]

const result = sortContanctsByName(contacts)
console.log(result)