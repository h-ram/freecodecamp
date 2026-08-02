function getContrastRating(ratio, large) {
  ratio = Number(ratio);

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

console.log(getContrastRating("7.5", false));
console.log(getContrastRating("4.8", false));
console.log(getContrastRating("4.2", false));
console.log(getContrastRating("4.5", true));
console.log(getContrastRating("3.0", true));
console.log(getContrastRating("2.7", false));
