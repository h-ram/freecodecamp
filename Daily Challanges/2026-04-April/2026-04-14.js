function getLastLetter(str) {
  let last = "";
  for (const char of str) {
    if (char.toUpperCase() > last.toUpperCase()) last = char;
  }
  return last;
}

console.log(getLastLetter("world"));
console.log(getLastLetter("Hello World"));
console.log(getLastLetter("The quick brown fox jumped over the lazy dog."));
