function getDayOfWeek(timestamp) {
  const days = [
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
  ];
  const daysSinceEpoch = Math.floor(timestamp / (1000 * 60 * 60 * 24));
  return days[daysSinceEpoch % 7];
}
