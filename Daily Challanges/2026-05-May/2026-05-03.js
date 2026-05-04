function getGreeting(time) {
  const [h, m] = time.split(":").map((item) => Number(item));
  if (h >= 5 && h <= 11) return "Good morning";
  if (h >= 12 && h <= 17) return "Good afternoon";
  if (h >= 18 && h <= 21) return "Good evening";
  return "Good night";
}

console.log(getGreeting("06:30"));
console.log(getGreeting("12:00"));
console.log(getGreeting("21:59"));
console.log(getGreeting("00:01"));
console.log(getGreeting("11:30"));
