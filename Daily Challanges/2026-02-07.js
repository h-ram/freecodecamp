function getLandingStance(startStance, rotation) {
  const trimmed_rotation = Math.abs(rotation) % 360

  if(trimmed_rotation < 180){
    return startStance;
  }else{
    return startStance == "Goofy" ? "Regular" : "Goofy";
  }
}

const test1 = getLandingStance("Regular", 90);
const test2 = getLandingStance("Regular", 180);
const test3 = getLandingStance("Goofy", -270);
const test4 = getLandingStance("Regular", 2340);
const test5 = getLandingStance("Goofy", 2160);

const check1 = "Regular";
const check2 = "Goofy";
const check3 = "Regular";
const check4 = "Goofy";
const check5 = "Goofy";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);