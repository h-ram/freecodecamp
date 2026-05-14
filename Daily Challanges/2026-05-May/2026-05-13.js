function findOffender(arr) {
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < arr[i - 1]) {
      if (i - 2 >= 0 && arr[i] < arr[i - 2]) return i;
      return i - 1;
    }
  }
  return -1;
}

console.log(findOffender([1, 6, 2, 3, 4, 5]));
console.log(findOffender([1, 2, 3, 5, 4, 5]));
console.log(findOffender([2, 4, 1, 6, 8]));
