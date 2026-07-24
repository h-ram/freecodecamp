function isGoldenRatio(a, b) {
  const ratio = Math.max(a, b) / Math.min(a, b);
  return Math.abs(ratio - 1.618) <= 0.01;
}

console.log(isGoldenRatio(21, 34));
console.log(isGoldenRatio(15, 20));
console.log(isGoldenRatio(8, 13));
console.log(isGoldenRatio(10, 16));
console.log(isGoldenRatio(1618, 1000));
console.log(isGoldenRatio(88, 55));
