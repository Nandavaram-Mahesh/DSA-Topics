function partitionAlgorithm(arr, leftIndex, rightIndex) {
    let pivotElem = arr[leftIndex];
  
    let i = leftIndex;
  
    for (let j = i + 1; j < rightIndex + 1; j++) {
      if (arr[j] > pivotElem) {
        i++;
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }
    }
    [arr[i], arr[leftIndex]] = [arr[leftIndex], arr[i]];
  
    return i + 1;
  }
  
  function quickSort(arr, leftIndex, rightIndex) {
    
     if (leftIndex < rightIndex) {
        
      let position = partitionAlgorithm(arr, leftIndex, rightIndex);
  
      let mid = position - 1;
  
      if (k === position) {
        return arr[mid];
      } else if (k < position) {
        return quickSort(arr, 0, mid - 1);
      } else if (k > position) {
        return quickSort(arr, mid + 1, rightIndex);
      }
    }
    else{
        return arr[leftIndex]
    }
  }
  
  const arr = [
    40, 25, 20, 5, 68, 79, 52, 66, 89, 97,
  ]; /* 5 20 25 40 52 66 68 79 89 97 */
  const k = 2;
//   const k = 3;
//   const k = 5;
  
  const arr2 = [7,10,4,3,20,15]/*3 4 7 10 15 20 */
  
  const arr3=[1]
  const result = quickSort(arr3, 0, arr3.length - 1);
  
  
  console.log(result);
  