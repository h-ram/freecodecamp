function hasNoRepeats(str) {
  for (let i = 0; i < str.length; i++) {
    if (str[i] === str[i - 1]) {
      return false;
    }
  }
  return true;
}

console.log(hasNoRepeats("The quick brown fox jumped over the lazy dog."));
