function insertIntoArray(arr, value, index) {
  arr.splice(index, 0, value);
  return arr;
}

const test1 = insertIntoArray([2, 4, 8, 10], 6, 2);
const test2 = insertIntoArray(["the", "quick", "fox"], "brown", 2);
const test3 = insertIntoArray([], 0, 0);
const test4 = insertIntoArray([0, 1, 1, 2, 3, 8, 13], 5, 5);

const check1 = [2, 4, 6, 8, 10];
const check2 = ["the", "quick", "brown", "fox"];
const check3 = [0];
const check4 = [0, 1, 1, 2, 3, 5, 8, 13];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
