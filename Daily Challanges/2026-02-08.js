function calculatePenaltyDistance(rounds) {
  let distance = 0
  for(const rnd of rounds){
    distance += (5 - rnd) * 150
  }
  return distance;
}

const test1 = calculatePenaltyDistance([4, 4]);
const test2 = calculatePenaltyDistance([5, 5]);
const test3 = calculatePenaltyDistance([4, 5, 3, 5]);
const test4 = calculatePenaltyDistance([5, 4, 5, 5]);
const test5 = calculatePenaltyDistance([4, 3, 0, 3]);

const check1 = 300;
const check2 = 0;
const check3 = 450;
const check4 = 150;
const check5 = 1500;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);