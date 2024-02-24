

function sortContanctsByName(arr){
    let n = arr.length
    for(let i=0;i<n-1;i++){
        let minIndex =i
        for(let j=i+1;j<n-1;j++){
            if(arr[minIndex]>arr[j]){
                minIndex = j
            }
        } 
        [arr[i],arr[minIndex]]=[arr[minIndex],arr[i]]
    }
    return arr
}









const contacts = ["Mahesh","Aravind","Sai","Pavan","Claudia","Richard","David"]

const result = sortContanctsByName(contacts)

console.log(result)