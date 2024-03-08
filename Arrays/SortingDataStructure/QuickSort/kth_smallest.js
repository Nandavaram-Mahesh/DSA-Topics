function partitionAlgorithm(arr, leftIndex, rightIndex) {

  let pivotElem = arr[leftIndex]; 

  let i = leftIndex;

  for (let j = i + 1; j < rightIndex + 1; j++) {
    if (arr[j] < pivotElem) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i], arr[leftIndex]] = [arr[leftIndex], arr[i]];

  return i;
}

function quickSort(arr, leftIndex, rightIndex) {
  if (leftIndex < rightIndex) {
    let mid = partitionAlgorithm(arr, leftIndex, rightIndex);
    
    quickSort(arr, 0, mid - 1);
    quickSort(arr, mid + 1, rightIndex);
  }
  return arr
}

const arr = [40, 25, 20,5, 68, 79, 52, 66, 89, 97]; /* 25 40 52 66 68 79 89 97 */
const k = 2;

const sortedArray = quickSort(arr, 0, arr.length - 1);

const result = sortedArray[k-1]     /* o(1) */
console.log(result);
