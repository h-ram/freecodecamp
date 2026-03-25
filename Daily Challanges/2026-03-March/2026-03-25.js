function canRetake(finishTime, currentTime) {
  const fDate = new Date(finishTime);
  const cDate = new Date(currentTime);
  return cDate - fDate >= 48 * 60 * 60 * 1000;
}

console.log(canRetake("2026-03-23T08:00:00", "2026-03-25T14:00:00"));
console.log(canRetake("2026-03-24T14:00:00", "2026-03-25T10:00:00"));
