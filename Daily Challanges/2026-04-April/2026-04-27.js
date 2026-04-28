function getWordScore(word) {
  const total = word
    .split("")
    .reduce((sum, char) => sum + char.toLowerCase().charCodeAt(0) - 96, 0);
  return total;
}

console.log(getWordScore("hi"));
console.log(getWordScore("hello"));
console.log(getWordScore("hippopotamus"));
