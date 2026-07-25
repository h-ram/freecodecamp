function blendWords(word1, word2) {
  const firstHalf = Math.floor(word1.length / 2);
  const secondHalf = Math.floor(word2.length / 2);
  return word1.slice(0, firstHalf) + word2.slice(secondHalf);
}

console.log(blendWords("turtle", "toucan"));
console.log(blendWords("chipmunk", "flamingo"));
console.log(blendWords("falcon", "pelican"));
console.log(blendWords("hyena", "iguana"));
console.log(blendWords("scorpion", "gorilla"));
console.log(blendWords("platypus", "wolverine"));
