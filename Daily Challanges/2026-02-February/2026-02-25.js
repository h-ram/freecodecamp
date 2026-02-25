function findDifferences(arr) {
  let distances = [];
  for (let i = 1; i < arr.length; i++) {
    distances.push(arr[i] - arr[i - 1]);
  }
  distances.push(0);
  return distances;
}

const test1 = findDifferences([1, 2, 4, 7]);
const test2 = findDifferences([10, 15, 19, 22, 24, 25]);
const test3 = findDifferences([25, 20, 16, 13, 11, 10]);
const test4 = findDifferences([0, 1, 2, 2, 3, 3, 4, 5]);
const test5 = findDifferences([
  1, 2, 5, 12, 34, -15, -1, 41, 113, -222, -99, -40, 10, -18, -6, -2, -1,
]);

const check1 = [1, 2, 3, 0];
const check2 = [5, 4, 3, 2, 1, 0];
const check3 = [-5, -4, -3, -2, -1, 0];
const check4 = [1, 1, 0, 1, 0, 1, 1, 0];
const check5 = [
  1, 3, 7, 22, -49, 14, 42, 72, -335, 123, 59, 50, -28, 12, 4, 1, 0,
];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);
