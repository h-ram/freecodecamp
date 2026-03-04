function isFlat(arr) {
  return arr.every((i) => !Array.isArray(i));
}

const test1 = isFlat([1, 2, 3, 4]);
const test2 = isFlat([1, [2, 3], 4]);
const test3 = isFlat([1, 0, false, true, "a", "b"]);
const test4 = isFlat(["a", [0], "b", true]);
const test5 = isFlat([1, [2, [3, [4, [5]]]], 6]);

const check1 = true;
const check2 = false;
const check3 = true;
const check4 = false;
const check5 = false;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
