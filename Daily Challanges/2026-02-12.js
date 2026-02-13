function largestDifference(skater1, skater2) {
  let largestLap = 0;
  let largestLapTime = 0;
  for (let i = 0; i < skater1.length; i++) {
    const diff = Math.abs(skater1[i] - skater2[i]);
    if (diff > largestLapTime) {
      largestLap = i + 1;
      largestLapTime = diff;
    }
  }
  return largestLap;
}

const test1 = largestDifference(
  [26.11, 25.8, 25.92, 26.23, 26.07],
  [25.93, 25.74, 26.53, 26.11, 26.3],
);
const test2 = largestDifference(
  [27.04, 25.94, 26.22, 26.07, 26.18],
  [25.59, 25.8, 26.11, 26.01, 26.23],
);
const test3 = largestDifference(
  [25.82, 25.9, 26.05, 26.0, 26.48],
  [25.85, 25.92, 26.07, 25.98, 25.95],
);
const test4 = largestDifference(
  [25.88, 26.1, 25.95, 26.05, 26.0],
  [25.9, 26.55, 25.92, 26.03, 26.01],
);
const test5 = largestDifference(
  [25.92, 26.01, 26.05, 25.88, 26.12],
  [25.95, 26.0, 26.03, 26.45, 26.1],
);

const check1 = 3;
const check2 = 1;
const check3 = 5;
const check4 = 2;
const check5 = 4;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
