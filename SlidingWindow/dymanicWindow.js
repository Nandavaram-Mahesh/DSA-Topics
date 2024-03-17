function fruitIntoBaskets(arr){
    let treeTypes={}
    let start = 0
    let max = 0
    let count = 0
    for(let i = 0;i<arr.length;i++){

        if(count<2 && !treeTypes[arr[i]]){
            treeTypes[arr[i]] = true
            max = Math.max(max,(i-start+1))
            count+=1
        }else if(treeTypes[arr[i]]){
            max = Math.max(max,(i-start+1))
        }else{
            treeTypes={}
            treeTypes[arr[i-1]] = true
            treeTypes[arr[i]] = true
            start = i-1 

            while(arr[start]==arr[start-1]){
                start--
            }
            max = Math.max(max,(i-start+1))
        }
    }
    return max

}




let fruits = [1,2,1,3,4,6,6,6,6]
const result = fruitIntoBaskets(fruits)
console.log(result)