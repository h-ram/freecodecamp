function sortNumbers(s) {
  return s
    .split(",")
    .map(Number)
    .sort((a, b) => a - b);
}

console.log(sortNumbers("3,1,2"));
console.log(sortNumbers("5,3,8,1,9,2"));
console.log(sortNumbers("12,61,49,80,19,50,77,38"));
console.log(sortNumbers("0,6,-19,44,-2,7,0"));
