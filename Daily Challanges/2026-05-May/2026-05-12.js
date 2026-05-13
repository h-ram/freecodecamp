function getFrequency(str) {
  const counter = {};
  for (const char of str) {
    if (!counter.hasOwnProperty(char)) counter[char] = 1;
    else counter[char] += 1;
  }
  return counter;
}

console.log(getFrequency("test"));
console.log(getFrequency("mississippi"));
