function getDueDate(dateStr) {
  let [year, month, day] = dateStr.split("-").map(Number);

  let totalMonths = month - 1 + 9;
  let targetYear = year + Math.floor(totalMonths / 12);
  let targetMonth = (totalMonths % 12) + 1;

  function isLeap(y) {
    return (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0;
  }

  const daysInMonth = [
    31,
    isLeap(targetYear) ? 29 : 28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
  ];

  let maxDay = daysInMonth[targetMonth - 1];
  let targetDay = Math.min(day, maxDay);

  let y = targetYear;
  let m = String(targetMonth).padStart(2, "0");
  let d = String(targetDay).padStart(2, "0");

  return `${y}-${m}-${d}`;
}

console.log(getDueDate("2025-03-30"));
console.log(getDueDate("2025-05-31"));
console.log(getDueDate("2025-04-27"));
