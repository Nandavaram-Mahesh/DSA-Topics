
 
function findCandidate(arr){
    let candidate = null
    let count = 0

    for (let i = 0;i<arr.length; i++){
  
        if (count===0){
            candidate=arr[i]

        }else{
            let value =(arr[i]===candidate)? 1 :-1 
            count+=value
        }
    }
    return candidate
}

function isMajorityElement(arr,candidate){
    
    let count = 0
    let size = arr.length

    for(let i=0;i<size;i++){
        if(arr[i]===candidate){
            count+=1
        }
    }
    if(count>Math.floor(size/2)){
        return 1
    }else{
        return 0
    }
}

//  finding majarity element by its occurence in the array
function printMajorityElementByOccurence(arr){

    let cand = findCandidate(arr)
    
    if(isMajorityElement(arr,cand)){
        console.log('Majority Elemenr is: ',cand)
    }else{
        console.log("No Majority element exists in an array")
    }
    
}







// Driver Code

const arr = [2,2,1,1,1,2,2]

printMajorityElementByOccurence(arr)

