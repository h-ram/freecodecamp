function groundhogDayPrediction(appearance) {
  if(appearance === true){
    return "Looks like we'll have six more weeks of winter."
  }
  if(appearance === false){
    return "It's going to be an early spring."
  }
  return "No prediction this year.";
}

const test1 = groundhogDayPrediction(true);
const test2 = groundhogDayPrediction(false);
const test3 = groundhogDayPrediction(null);
const test4 = groundhogDayPrediction(" ");
const test5 = groundhogDayPrediction("True");

const check1 = "Looks like we'll have six more weeks of winter.";
const check2 = "It's going to be an early spring.";
const check3 = "No prediction this year.";
const check4 = "No prediction this year.";
const check5 = "No prediction this year.";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);