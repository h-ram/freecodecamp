function sortAndSwap(arr) {
  arr.sort((a, b) => a - b);
  for (let i = 1; i < arr.length; i++) {
    if (i % 3 == 0) [arr[i], arr[i - 1]] = [arr[i - 1], arr[i]];
  }
  return arr;
}

console.log(sortAndSwap([3, 1, 2, 4, 6, 5]));
