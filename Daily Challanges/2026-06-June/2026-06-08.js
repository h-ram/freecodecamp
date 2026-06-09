function getJetLagHours(departureCity, arrivalCity, flightDuration, direction) {
  const offsets = {
    "Los Angeles": -8,
    "New York": -5,
    London: 0,
    Istanbul: 3,
    Dubai: 4,
    "Hong Kong": 8,
    Tokyo: 9,
  };

  const timezoneDifference = Math.abs(
    offsets[arrivalCity] - offsets[departureCity],
  );

  const multiplier = direction === "east" ? 1.5 : 1.0;

  return Number(
    (timezoneDifference + flightDuration * 0.1 * multiplier).toFixed(1),
  );
}

console.log(getJetLagHours("Istanbul", "Hong Kong", 10, "east"));
console.log(getJetLagHours("London", "New York", 8, "west"));
console.log(getJetLagHours("Hong Kong", "Tokyo", 4, "east"));
console.log(getJetLagHours("Dubai", "London", 7, "west"));
console.log(getJetLagHours("Los Angeles", "Hong Kong", 15, "west"));
console.log(getJetLagHours("Tokyo", "Dubai", 9, "west"));
console.log(getJetLagHours("New York", "Istanbul", 10, "east"));
