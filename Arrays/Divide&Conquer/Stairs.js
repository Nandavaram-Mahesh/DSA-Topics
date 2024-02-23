function findWaysToClimbStairs(n){
    
    if(n<=1){
        return 1 
    }else if(n==2){
        return 2
    }
    else{
         
        return findWaysToClimbStairs(n-1)+findWaysToClimbStairs(n-2)
    }
}










const no_of_stairs = 7

const result = findWaysToClimbStairs(no_of_stairs)
console.log(result)