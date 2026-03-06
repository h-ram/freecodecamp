function smallestGap(str) {
  const lastSeen = {};
  let minGap = str.length;
  let smallestSubstring = "";
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    if (lastSeen.hasOwnProperty(char)) {
      const gap = i - lastSeen[char];
      if (gap < minGap) {
        minGap = gap;
        smallestSubstring = str.slice(lastSeen[char] + 1, i);
      }
    }
    lastSeen[char] = i;
  }
  return smallestSubstring;
}

const test1 = smallestGap("ABCDAC");
const test2 = smallestGap("racecar");
const test3 = smallestGap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4");
const test4 = smallestGap("Hello World");
const test5 = smallestGap("The quick brown fox jumps over the lazy dog.");

const check1 = "DA";
const check2 = "e";
const check3 = "#q6e&rkf(p";
const check4 = "";
const check5 = "fox";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
