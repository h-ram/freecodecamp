function getBingoRange(letter) {
  if (letter === "B") {
    return Array.from({ length: 15 }, (_, i) => i + 1);
  } else if (letter === "I") {
    return Array.from({ length: 15 }, (_, i) => i + 16);
  } else if (letter === "N") {
    return Array.from({ length: 15 }, (_, i) => i + 31);
  } else if (letter === "G") {
    return Array.from({ length: 15 }, (_, i) => i + 46);
  } else {
    return Array.from({ length: 15 }, (_, i) => i + 61);
  }
}

console.log(getBingoRange("B"));
console.log(getBingoRange("I"));
console.log(getBingoRange("N"));
console.log(getBingoRange("G"));
console.log(getBingoRange("O"));
