function isValidHSL(str) {
  const regex =
    /^hsl\(\s*(\d{1,3})\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%\s*\)\s*;?$/;

  const match = str.match(regex);
  if (!match) return false;

  const h = Number(match[1]);
  const s = Number(match[2]);
  const l = Number(match[3]);

  return h >= 0 && h <= 360 && s >= 0 && s <= 100 && l >= 0 && l <= 100;
}

const test1 = isValidHSL("hsl(240, 50%, 50%)");
const test2 = isValidHSL("hsl( 200 , 50% , 75% )");
const test3 = isValidHSL("hsl(99,60%,80%);");
const test4 = isValidHSL("hsl(0, 0%, 0%) ;");
const test5 = isValidHSL("hsl( 10 , 20% , 30% ) ;");
const test6 = isValidHSL("hsl(361, 50%, 80%)");
const test7 = isValidHSL("hsl(300, 101%, 70%)");
const test8 = isValidHSL("hsl(200, 55%, 75)");
const test9 = isValidHSL("hsl (80, 20%, 10%)");

const check1 = true;
const check2 = true;
const check3 = true;
const check4 = true;
const check5 = true;
const check6 = false;
const check7 = false;
const check8 = false;
const check9 = false;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);
console.log(`Test8: ${test8 === check8}`);
console.log(`Test9: ${test9 === check9}`);
