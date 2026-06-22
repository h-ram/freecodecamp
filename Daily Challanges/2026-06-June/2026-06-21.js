function getDaytimeHours(latitude) {
  const daylight = Math.round((12 + (latitude / 90) * 12) / 2) * 2;
  const sunrise = 12 - daylight / 2;
  const sunset = 12 + daylight / 2;

  let result = "";

  for (let h = 0; h < 24; h++) {
    result += h >= sunrise && h < sunset ? "☀️" : "🌑";
  }

  return result;
}

console.log(getDaytimeHours(0));
console.log(getDaytimeHours(90));
console.log(getDaytimeHours(-90));
console.log(getDaytimeHours(-33));
console.log(getDaytimeHours(66.5));
console.log(getDaytimeHours(40));
console.log(getDaytimeHours(-50));
