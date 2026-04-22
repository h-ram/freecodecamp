function getOddWords(str) {
  const words = str.split(" ");
  return words.filter((word) => word.length % 2 === 1).join(" ");
}

console.log(getOddWords("This is a super good test"));
console.log(getOddWords("one two three four"));
