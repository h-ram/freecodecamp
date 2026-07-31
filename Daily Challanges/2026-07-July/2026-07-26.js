function letterDistance(s1, s2) {
  let total = 0;

  for (let i = 0; i < s1.length; i++) {
    const diff = Math.abs(s1.charCodeAt(i) - s2.charCodeAt(i));
    total += Math.min(diff, 26 - diff);
  }

  return total;
}

console.log(letterDistance("abc", "bcd"));
console.log(letterDistance("abc", "xyz"));
console.log(letterDistance("encrypt", "decrypt"));
console.log(letterDistance("algorithm", "codeblock"));
console.log(letterDistance("lobster", "penguin"));
console.log(letterDistance("alligator", "crocodile"));
