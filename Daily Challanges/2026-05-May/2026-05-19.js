function sleepDebt(hoursSlept, targetHours) {
  const debt = hoursSlept.reduce((sum, hour) => sum + targetHours - hour, 0);
  return Math.max(0, debt + targetHours);
}

console.log(sleepDebt([6, 6, 6, 6, 6, 6], 8));
console.log(sleepDebt([6, 7, 8, 4, 8, 6], 7));
console.log(sleepDebt([10, 10, 9, 10, 9, 11], 9));
console.log(sleepDebt([8, 7, 6, 7, 6, 8], 6));
console.log(sleepDebt([8, 9, 10, 9, 10, 7], 7));
