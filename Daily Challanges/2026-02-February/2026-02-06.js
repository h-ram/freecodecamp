function getFlag(code) {
  code = code.toUpperCase();
  return [...code].map(c => String.fromCodePoint(c.charCodeAt(0) + 127397)).join('');
}

const test1 = getFlag("AL");
const test2 = getFlag("AD");
const test3 = getFlag("AR");
const test4 = getFlag("AM");
const test5 = getFlag("AU");

const check1 = "🇦🇱";
const check2 = "🇦🇩";
const check3 = "🇦🇷";
const check4 = "🇦🇲";
const check5 = "🇦🇺";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);