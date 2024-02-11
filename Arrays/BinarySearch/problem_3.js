function findMaxProfit(priceArr){
    let min_price = Infinity
    let max_profit = 0
    for(let i=0;i<(priceArr.length);i++){
        if(priceArr[i]<min_price){
            min_price=priceArr[i]
        }else if(priceArr[i]-min_price>max_profit){
            max_profit = priceArr[i]-min_price
        }
    }
    return max_profit
    
}


const priceArr = [7,4,5,3,6,1,6]


const maxProfitValue = findMaxProfit(priceArr)
console.log(maxProfitValue)