function getContrastRating(light, dark, large) {
  const ratio = (light + 0.05) / (dark + 0.05);

  if (large) {
    if (ratio >= 4.5) {
      return "AAA";
    }
    if (ratio >= 3) {
      return "AA";
    }
  } else {
    if (ratio >= 7) {
      return "AAA";
    }
    if (ratio >= 4.5) {
      return "AA";
    }
  }

  return "Fail";
}

console.log(getContrastRating(1.0, 0.0, false));
console.log(getContrastRating(0.9015, 0.1364, false));
console.log(getContrastRating(0.8965, 0.1628, false));
console.log(getContrastRating(0.7469, 0.0957, true));
console.log(getContrastRating(0.7489, 0.2018, true));
console.log(getContrastRating(0.6571, 0.1974, true));
