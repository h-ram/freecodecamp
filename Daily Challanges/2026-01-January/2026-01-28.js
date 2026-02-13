function flatten(arr) {
  const result = [];

  function flattenHelper(item) {
    if (Array.isArray(item)) {
      for (const element of item) {
        flattenHelper(element);
      }
    } else {
      result.push(item);
    }
  }

  flattenHelper(arr);
  return result;
}

const test1 = flatten([1, [2, 3], 4]);
const test2 = flatten([5, [4, [3, 2]], 1]);
const test3 = flatten(["A", [[[["B"]]]], "C"]);
const test4 = flatten([
  ["L", "M", "N"],
  ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]],
  "V",
  ["W", ["X", ["Y", ["Z"]]]],
]);
const test5 = flatten([
  ["red", ["blue", ["green", ["yellow", ["purple"]]]]],
  "orange",
  ["pink", ["brown"]],
]);

const check1 = [1, 2, 3, 4];
const check2 = [5, 4, 3, 2, 1];
const check3 = ["A", "B", "C"];
const check4 = [
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];
const check5 = [
  "red",
  "blue",
  "green",
  "yellow",
  "purple",
  "orange",
  "pink",
  "brown",
];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);
