function getHillRating(drop, distance, type) {
  const typeConverter = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0
    }
    const steepness = drop / distance
    const adjustedSteepness = steepness * typeConverter[type]
    
    if(adjustedSteepness <= 0.1){
      return "Green"
    }
    if(adjustedSteepness <= 0.25){
      return "Blue"
    }
    return "Black"
}

const test1 = getHillRating(95, 900, "Slalom");
const test2 = getHillRating(620, 2800, "Downhill");
const test3 = getHillRating(420, 1680, "Giant Slalom");
const test4 = getHillRating(250, 3000, "Downhill");
const test5 = getHillRating(110, 900, "Slalom");
const test6 = getHillRating(380, 1500, "Giant Slalom");

const check1 = "Green";
const check2 = "Black";
const check3 = "Blue";
const check4 = "Green";
const check5 = "Blue";
const check6 = "Black";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);