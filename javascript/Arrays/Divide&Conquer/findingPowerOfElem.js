function findPowerOfElement(num,power){

    if(power===0){
        return 1        /* Anything power Zero is 1 => a^0 = 1 */
    }
    else if (power===1){
        return num     /* Any num power one is num => a^1 = a */
    }
    else{

        let mid  = Math.floor(power/2) 

        let value = findPowerOfElement(num,mid)

        let result = value*value

        if(power%2===0){   
            return result
        }
        else{
            return result*num          /*When power is odd  => (2^17) can be written as => (2^16) * 2   */
        }
    }
}



const result = findPowerOfElement(num=2,power=17)

console.log(`PowerOfElement:${result}`)