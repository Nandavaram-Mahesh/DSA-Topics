
// function insertionSort(arr){
//     for(let i=1;i<(arr.length);i++){
//         let key = arr[i]
//         let j
//         for( j=i-1;j>=0 && arr[j]>key;j--){
//             arr[j+1]=arr[j]
//         }
//     arr[j+1]=key
//     }
// return arr
// }

/*
1ST-step [60,30,80,70,20,5,15]
          0  1  2  3  4  5  6 
          j   i

    key = arr[i] = 30   
    while j>=0 and key<arr[j]:
       arr[j+1] = arr[j]
       j = j-1
    arr[j+1]=key


2ndStep [30,60,80,70,20,5,15]
         0  1  2  3  4  5  6 
            j  i

    key = arr[i] = 80   
    while j>=0 and key<arr[j]:
       arr[j+1] = arr[j]
       j = j-1
    arr[j+1]=key

3rdStep [30,60,80,70,20,5,15]
         0  1  2  3  4  5  6 
               j  i

    key = arr[i] = 70        
    while j>=0 and key<arr[j]:
       arr[j+1] = arr[j]
       j = j-1
    arr[j+1]=key

    [30,60,80,80,20,5,15]
     0  1  2  3  4  5  6 
           j  j+1
    [30,60,70,80,20,5,15]
     0  1  2  3  4  5  6
           |     
        j+1 = key

4th Step [30,60,70,80,20,5,15]
          0  1  2  3  4  5  6 
                   j  i

    key = arr[i] = 20        
    while j>=0 and key<arr[j]:
       arr[j+1] = arr[j]
       j = j-1
    arr[j+1]=key

    [30,60,70,80,80,5,15]
     0  1  2  3  4  5  6 
              j  j+1

    [30,60,70,70,80,5,15]
     0  1  2  3  4  5  6 
           j  j+1

    [30,60,60,70,80,5,15]
     0  1  2  3  4  5  6 
        j  j+1

    [30,30,60,70,80,5,15]
     0  1  2  3  4  5  6 
    j  j+1

    [20,30,60,70,80,5,15]
     0  1  2  3  4  5  6
     | 
    j+1 = key

5th Step [20,30,60,70,80,5,15]
          0  1  2  3  4  5  6 
                      j  i
         key = arr[i] = 5    
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1]=key

        [20,30,60,70,80,80,15]
                      j j+1   
        [20,30,60,70,70,80,15]
                   j j+1
        [20,30,60,60,70,80,15]
                j j+1     
        [20,30,30,60,70,80,15]
             j j+1        
        [20,20,30,60,70,80,15]
          j j+1  
        [5,20,30,60,70,80,15]
         |
        j+1=key

6th Step [5,20,30,60,70,80,15]
          0  1  2  3  4  5  6 
                         j  i

         key = arr[i] = 15    
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1]=key
                      
        [5,20,30,60,70,80,80]
                       j j+1   
        [5,20,30,60,70,70,80]
                    j j+1
        [5,20,30,60,60,80,80]
                 j j+1     
        [5,20,30,30,60,70,80]
              j j+1        
        [5,20,20,30,60,70,80]
           j j+1  
        [5,15,20,30,60,70,80]
           |
         j+1=key

   

*/

// Time Complexity -O(N^2)

function insertionSort(arr){

    for(let i=1;i<arr.length;i++){
        let key = arr[i]
        let j=i-1
        while(j>=0 && key<arr[j]){
            arr[j+1]=arr[j]
            j=j-1
        }
    arr[j+1]=key    
    }
return arr
}







const unsortedArr = [30,60,80,70,20,5,15]

const result = insertionSort(unsortedArr)

console.log(result )