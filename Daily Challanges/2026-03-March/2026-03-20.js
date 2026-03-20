function getShadow(time) {
  const [hours, minutes] = time.split(":").map((item) => Number(item));
  if (hours < 6 || hours >= 18 || hours == 12) {
    return "No shadow";
  }
  const h = hours + minutes / 60;
  const length = Math.abs(h - 12) ** 3;
  const direction = hours < 12 ? "west" : "east";
  return `${length}ft ${direction}`;
}

console.log(getShadow("10:00"));
console.log(getShadow("17:30"));
