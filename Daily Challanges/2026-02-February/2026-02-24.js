function countBusinessDays(start, end) {
  let startDate = new Date(start);
  let endDate = new Date(end);

  let count = 0;
  let current = new Date(startDate);
  while (current <= endDate) {
    const day = current.getDay(); // 0=sunday
    if (day !== 0 && day !== 6) {
      count++;
    }
    current.setDate(current.getDate() + 1);
  }
  return count;
}
const test1 = countBusinessDays("2026-02-24", "2026-02-26");
const test2 = countBusinessDays("2026-02-24", "2026-02-28");
const test3 = countBusinessDays("2026-02-21", "2026-03-01");
const test4 = countBusinessDays("2026-03-08", "2026-03-17");
const test5 = countBusinessDays("2026-02-24", "2027-02-24");

const check1 = 3;
const check2 = 4;
const check3 = 5;
const check4 = 7;
const check5 = 262;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
