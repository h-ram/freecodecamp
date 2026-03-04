function countPerfectCubes(a, b) {
  const smallest = Math.min(a, b);
  const largest = Math.max(a, b);
  let num = Math.floor(Math.cbrt(smallest));
  let perfectCubes = 0;
  while (num * num * num <= largest) {
    if (num * num * num >= smallest) {
      perfectCubes++;
    }
    num++;
  }

  return perfectCubes;
}

const test1 = countPerfectCubes(3, 30);
const test2 = countPerfectCubes(1, 30);
const test3 = countPerfectCubes(30, 0);
const test4 = countPerfectCubes(-64, 64);
const test5 = countPerfectCubes(9214, -8127);

const check1 = 2;
const check2 = 3;
const check3 = 4;
const check4 = 9;
const check5 = 41;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
