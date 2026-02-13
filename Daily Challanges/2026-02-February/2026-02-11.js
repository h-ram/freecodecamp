function computeScore(judgeScores, ...penalties) {
      let baseScore = judgeScores
        .slice()
        .sort((a, b) => a - b)
        .slice(1, -1)
        .reduce((sum, score) => sum + score, 0);
  for(const penalty of penalties){
    baseScore -= penalty

  }
  return baseScore;
}

const test1 = computeScore([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1);
const test2 = computeScore([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]);
const test3 = computeScore([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1);
const test4 = computeScore([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0);
const test5 = computeScore([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5);

const check1 = 64;
const check2 = 80;
const check3 = 67;
const check4 = 67.5;
const check5 = 59;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);