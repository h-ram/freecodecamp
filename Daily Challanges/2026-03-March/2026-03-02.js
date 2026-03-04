function sumLetters(s) {
  let total = 0;

  for (let char of s.toLowerCase()) {
    if (/[a-z]/.test(char)) {
      total += char.charCodeAt(0) - 96;
    }
  }

  return total;
}
const test1 = sumLetters("Hello");
const test2 = sumLetters("freeCodeCamp");
const test3 = sumLetters("The quick brown fox jumps over the lazy dog.");
const test4 = sumLetters(
  "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.",
);
const test5 = sumLetters("</404>");

const check1 = 52;
const check2 = 94;
const check3 = 473;
const check4 = 1681;
const check5 = 0;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
