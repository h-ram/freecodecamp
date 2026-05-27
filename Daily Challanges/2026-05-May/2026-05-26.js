function sumOfDifferences(arr) {
  const diff = [];
  for (let i = 0; i < arr.length - 1; i++) {
    diff.push(arr[i + 1] - arr[i]);
  }
  return diff.reduce((sum, num) => sum + num);
}

console.log(sumOfDifferences([1, 3, 4]));
console.log(sumOfDifferences([5, -3, 3, 9, 10]));
console.log(sumOfDifferences([9, 6, 15, -20, 33, 14, 25, 16, -7]));
console.log(
  sumOfDifferences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]),
);
