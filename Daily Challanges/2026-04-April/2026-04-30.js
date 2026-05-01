const checker = [
  // rows
  "01000001",
  "01101111",
  "01000100",
  "01100101",
  "01010010",
  "01010100",
  "01101000",
  "10101110",

  // columns
  "00000001",
  "11111110",
  "01011011",
  "00001100",
  "01000011",
  "01111001",
  "01000100",
  "11010000",
];

function isInCrossword(char) {
  const binStr = char.charCodeAt(0).toString(2).padStart(8, "0");
  const rev = binStr.split("").reverse().join("");

  for (const bstr of checker) {
    if (bstr.includes(binStr) || bstr.includes(rev)) {
      return true;
    }
  }
  return char === "I";
}

console.log(isInCrossword("I"));
console.log(isInCrossword("D"));
console.log(isInCrossword("0"));
console.log(isInCrossword("u"));
console.log(isInCrossword("Y"));
console.log(isInCrossword("p"));
console.log(isInCrossword("1"));
console.log(isInCrossword("Q"));
