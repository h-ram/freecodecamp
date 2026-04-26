function decompress(str) {
  let mapper = {};
  let decompressed = [];
  const words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    if (/^\d+$/.test(word)) {
      decompressed.push(mapper[word]);
    } else {
      mapper[`${i + 1}`] = word;
      decompressed.push(word);
    }
  }
  return decompressed.join(" ");
}

console.log(decompress("practice makes perfect and 3 1 2 3"));
