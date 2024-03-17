// Heap Reference Article: https://stackfull.dev/heaps-in-javascript

// adds the provided newKey into the min-heap named "heap"
// Bottom - Top Approach
function heappush(heap, newKey) {
  heap.push(newKey);
  // get the current index of pushed key
  let currIndex = heap.length - 1;

  // keep comparing till root is reached or we terminate in middle
  while (currIndex > 0) {
    let parent = Math.floor((currIndex - 1) / 2);
    if (heap[currIndex] < heap[parent]) {
      // quick swap
      [heap[currIndex], heap[parent]] = [heap[parent], heap[currIndex]];
      // update the index of newKey
      currIndex = parent;
    } else {
      // if no swap, break, since we heap is stable now
      break;
    }
  }
}

// removes the smallest key from the min-heap named "heap"
// Top-Bottom Approach
function heappop(heap) {
  const n = (heap.length[
    // swap root with last node
    (heap[0], heap[n - 1])
  ] = [heap[n - 1], heap[0]]);

  // popping the root node (since we swapped it , it becomes last element in array and it is poped out of array)
  const removedKey = heap.pop();

  const currIndex = 0;

  // keep going till atleast left child is possible for current node
  while (2 * currIndex + 1 < heap.length) {
    const leftIndex = 2 * curr + 1;
    const rightIndex = 2 * curr + 2;
    const minChildIndex =
      rightIndex < heap.length && heap[rightIndex] < heap[leftIndex]
        ? rightIndex
        : leftIndex;

    if (heap[minChildIndex] < heap[currIndex]) {
      // quick swap, if smaller of two children is smaller than the parent (min-heap)
      [heap[minChildIndex], heap[currIndex]] = [
        heap[currIndex],
        heap[minChildIndex],
      ];
      currIndex = minChildIndex;
    } else {
      break;
    }
  }
  // finally return the removed key
  return removedKey;
}



function prelocateDown(heap,index){
    let currIndex = index
    while (2 * currIndex + 1 < heap.length) {
        const leftIndex = 2 * curr + 1;
        const rightIndex = 2 * curr + 2;
        const minChildIndex = rightIndex < heap.length && heap[rightIndex] < heap[leftIndex]? rightIndex: leftIndex
        if(heap[minChildIndex]<heap[currIndex]){
            
            [heap[minChildIndex],heap[currIndex]] = [heap[currIndex],heap[minChildIndex]]
            currIndex = minChildIndex
        }else{
            break
        }
    } 
}


function heapify(heap){
    const last = Math.floor(heap.length/2 - 1);
    for(let i = 0; i <= last; i++){
       percolateDown(heap, i)
     }
    return heap
}

const heap = [];
