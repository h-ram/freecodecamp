function roundToNearestMultiple(n, m) {
  const lower = Math.floor(n / m) * m;
  const upper = lower + m;
  if (n - lower < upper - n) {
    return lower;
  }
  return upper;
}

console.log(roundToNearestMultiple(5, 3));
console.log(roundToNearestMultiple(17, 4));
console.log(roundToNearestMultiple(43, 5));
console.log(roundToNearestMultiple(38, 11));
console.log(roundToNearestMultiple(93, 12));
