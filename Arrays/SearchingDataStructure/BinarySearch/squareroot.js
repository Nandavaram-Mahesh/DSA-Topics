function findingPerfectSquare(num){

    let leftIndex = 1
    let rightIndex = num
    
    while(leftIndex<rightIndex){
        let mid = Math.floor(leftIndex+(rightIndex-leftIndex)/2)
        let squareOfNum = mid**2
        if(squareOfNum==num){
            return true
        }
        else if(squareOfNum<num){
            leftIndex = mid+1
        }
        else{
            rightIndex = mid-1
        }
    }
    return false

}



const num = 15

const result  = findingPerfectSquare(num)

console.log(result)