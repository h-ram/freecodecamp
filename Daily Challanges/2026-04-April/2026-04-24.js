function compress(str) {
  let found = {};
  let compressed = [];
  let words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (word in found) {
      compressed.push(found[word]);
    } else {
      found[word] = String(i + 1);
      compressed.push(word);
    }
  }
  return compressed.join(" ");
}

console.log(
  compress("practice makes perfect and perfect practice makes perfect"),
);
console.log(compress("hello hello hello"));
