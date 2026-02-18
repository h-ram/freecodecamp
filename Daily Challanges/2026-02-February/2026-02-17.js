function checkEligibility(athleteWeights, sledWeight) {
  const nAthletes = athleteWeights.length
  const sumWeights = athleteWeights.reduce((acc, value) => acc + value, 0);

  switch(nAthletes){
    case 1:
      if(sledWeight < 162){return "Not Eligible"}
      if(sumWeights + sledWeight > 247){return "Not Eligible"}
      break;
    case 2:
      if(sledWeight < 170){return "Not Eligible"}
      if(sumWeights + sledWeight > 390){return "Not Eligible"}
      break;
    case 4:
      if(sledWeight < 210){return "Not Eligible"}
      if(sumWeights + sledWeight > 630){return "Not Eligible"}
      break;
    default:
      return "Not Eligible" 
  }
  return "Eligible";
}

const test1 = checkEligibility([78], 165);
const test2 = checkEligibility([80], 160);
const test3 = checkEligibility([80], 170);
const test4 = checkEligibility([85, 90], 170);
const test5 = checkEligibility([85, 95], 168);
const test6 = checkEligibility([112, 97], 185);
const test7 = checkEligibility([110, 102, 90, 106], 222);
const test8 = checkEligibility([106, 99, 90, 88], 205);
const test9 = checkEligibility([106, 99, 103, 96], 227);

const check1 = "Eligible";
const check2 = "Not Eligible";
const check3 = "Not Eligible";
const check4 = "Eligible";
const check5 = "Not Eligible";
const check6 = "Not Eligible";
const check7 = "Eligible";
const check8 = "Not Eligible";
const check9 = "Not Eligible";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);
console.log(`Test8: ${test8 === check8}`);
console.log(`Test9: ${test9 === check9}`);