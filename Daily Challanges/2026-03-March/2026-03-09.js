function sumArray(numbers) {
  return numbers.reduce((sum, num) => sum + num, 0);
}

const test1 = sumArray([1, 2, 3, 4, 5]);
const test2 = sumArray([42]);
const test3 = sumArray([5, -2, 7, -3]);
const test4 = sumArray([203, 145, -129, 6293, 523, -919, 845, 2434]);
const test5 = sumArray([0, 0]);

const check1 = 15;
const check2 = 42;
const check3 = 7;
const check4 = 9395;
const check5 = 0;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
