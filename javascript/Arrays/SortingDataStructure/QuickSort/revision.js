function partition(arr, startIndex, endIndex) {
  let pivot = arr[startIndex];
  let i = startIndex;
  for (let j = i + 1; j < endIndex+1; j++) {
    if (arr[j] < pivot) {
      i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }
  [arr[i], arr[startIndex]] = [arr[startIndex], arr[i]];
  return i;
}

function quickSort(arr, startIndex, endIndex) {
  //  if startIndex==EndIndex then return arr   (i.e there is only one element in arr)

  //  if startIndex<EndIndex then do the sorting logic
  // find mid value
  // Here we find midValue using partition Algorithm
  // set pivot element, 'i'  as first element in array
  // set j = i+1 , loop through the array from j till the end of the array
  // if arr[j]<pivot:
  // i++
  // [arr[j],arr[i]]= [arr[i],arr[j]]
  // j++
  // else j++
  // [arr[i],arr[pivotElem]] = [arr[pivotElem],arr[i]]
  // return pivotElemetIndex

  if (startIndex < endIndex) {
    let mid = partition(arr, startIndex, endIndex);
    quickSort(arr, startIndex, mid - 1);
    quickSort(arr, mid + 1, endIndex);
   
  }
  return arr;
}

const arr = [50, 40, 70, 10, 30, 90, 45, 67, 79];

const result = quickSort(arr, 0, arr.length - 1);
console.log(result);
