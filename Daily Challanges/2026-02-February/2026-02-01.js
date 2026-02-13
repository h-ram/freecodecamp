function digitalDetox(logs) {
  const times = logs
    .map(t => new Date(t.replace(" ", "T")))
    .sort((a, b) => a - b);

  for (let i = 1; i < times.length; i++) {
    if (times[i] - times[i - 1] < 4 * 60 * 60 * 1000) {
      return false;
    }
  }

  const perDay = {};
  for (const t of times) {
    const day = t.toISOString().slice(0, 10);
    perDay[day] = (perDay[day] || 0) + 1;
    if (perDay[day] > 2) {
      return false;
    }
  }

  return true;
}


const test1 = digitalDetox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]);
const test2 = digitalDetox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]);
const test3 = digitalDetox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]);
const test4 = digitalDetox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]);
const test5 = digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]);
const test6 = digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]);

const check1 = true;
const check2 = false;
const check3 = true;
const check4 = false;
const check5 = true;
const check6 = false;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);