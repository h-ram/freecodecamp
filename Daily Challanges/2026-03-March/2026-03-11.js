function convertWords(str) {
  const words = str.split(" ");
  const lengths = words.map((word) => String(word.length));
  return lengths.join(" ");
}

console.log(convertWords("Hello World"));
