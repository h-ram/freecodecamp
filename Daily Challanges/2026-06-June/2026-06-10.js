function getItineraryCount(stops) {
  const n = stops.length;
  let fact = 1;
  for (let i = 2; i <= n; i++) fact *= i;
  return (2 * n - 3) * fact;
}

console.log(getItineraryCount(["library", "park"]));
console.log(getItineraryCount(["library", "park", "arcade"]));
console.log(getItineraryCount(["library", "park", "arcade", "store"]));
console.log(getItineraryCount(["library", "park", "arcade", "store", "cafe"]));
console.log(
  getItineraryCount([
    "library",
    "park",
    "arcade",
    "store",
    "cafe",
    "market",
    "museum",
  ]),
);
