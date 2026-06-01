function getCombinations(n) {
  let result = 1;
  for (let i = 0; i < n; i++) {
    result = (result * (2 * n - i)) / (i + 1);
  }
  return Math.round(result / (n + 1));
}

console.log(getCombinations(0)); // 1
console.log(getCombinations(1)); // 1
console.log(getCombinations(2)); // 2
console.log(getCombinations(3)); // 5
console.log(getCombinations(4)); // 14
