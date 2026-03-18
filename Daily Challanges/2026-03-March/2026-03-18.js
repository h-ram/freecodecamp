function largestNumber(s) {
  const separators = ",;:!?";
  const numbers = [];
  let current = "";
  for (let char of s) {
    if (separators.includes(char)) {
      numbers.push(Number(current));
      current = "";
    } else {
      current += char;
    }
  }
  numbers.push(Number(current));
  return Math.max(...numbers);
}

console.log(largestNumber("1,2"));
