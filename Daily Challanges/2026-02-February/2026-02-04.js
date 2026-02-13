function truncateText(text) {
  return text.length <= 20 ? text : text.slice(0, 17) + "...";
}

const test1 = truncateText("Hello, world!");
const test2 = truncateText("This string should get truncated.");
const test3 = truncateText("Exactly twenty chars");
const test4 = truncateText(".....................");

const check1 = "Hello, world!";
const check2 = "This string shoul...";
const check3 = "Exactly twenty chars";
const check4 = "....................";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
