function guessNumber(secret, guess) {
  return secret === guess ? "you got it!" : secret > guess ? "higher" : "lower";
}

console.log(guessNumber(50, 30));
console.log(guessNumber(85, 99));
console.log(guessNumber(2026, 2026));
console.log(guessNumber(2026, 2026));
