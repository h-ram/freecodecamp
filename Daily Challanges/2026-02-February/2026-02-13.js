function getFastestSpeed(times) {
  const speeds = [
    320 / times[0],
    280 / times[1],
    350 / times[2],
    300 / times[3],
    250 / times[4],
  ];

  const fastestSpeed = Math.max(...speeds);
  const fastestSeg = speeds.indexOf(fastestSpeed) + 1;

  const result = `The luger's fastest speed was ${fastestSpeed.toFixed(2)} m/s on segment ${fastestSeg}.`;
  return result;
}

const test1 = getFastestSpeed([9.523, 8.234, 10.012, 9.001, 7.128]);
const test2 = getFastestSpeed([9.381, 7.417, 9.912, 8.815, 7.284]);
const test3 = getFastestSpeed([8.89, 7.601, 9.093, 8.392, 6.912]);
const test4 = getFastestSpeed([8.49, 7.732, 10.103, 8.489, 6.84]);
const test5 = getFastestSpeed([8.204, 7.23, 9.673, 7.645, 6.508]);

const check1 = "The luger's fastest speed was 35.07 m/s on segment 5.";
const check2 = "The luger's fastest speed was 37.75 m/s on segment 2.";
const check3 = "The luger's fastest speed was 38.49 m/s on segment 3.";
const check4 = "The luger's fastest speed was 37.69 m/s on segment 1.";
const check5 = "The luger's fastest speed was 39.24 m/s on segment 4.";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
