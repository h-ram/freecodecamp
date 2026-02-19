function avalancheRisk(snowDepth, slope) {
  if(snowDepth === "Shallow" || slope ==="Gentle"){
    return "Safe"
  }
  return "Risky";
}

const test1 = avalancheRisk("Shallow", "Gentle");
const test2 = avalancheRisk("Shallow", "Steep");
const test3 = avalancheRisk("Shallow", "Very Steep");
const test4 = avalancheRisk("Moderate", "Gentle");
const test5 = avalancheRisk("Moderate", "Steep");
const test6 = avalancheRisk("Moderate", "Very Steep");
const test7 = avalancheRisk("Deep", "Gentle");
const test8 = avalancheRisk("Deep", "Steep");
const test9 = avalancheRisk("Deep", "Very Steep");

const check1 = "Safe";
const check2 = "Safe";
const check3 = "Safe";
const check4 = "Safe";
const check5 = "Risky";
const check6 = "Risky";
const check7 = "Safe";
const check8 = "Risky";
const check9 = "Risky";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);
console.log(`Test8: ${test8 === check8}`);
console.log(`Test9: ${test9 === check9}`);