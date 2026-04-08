function palindromeLocator(str) {
  const n = str.length;
  const mid = Math.floor(n / 2);
  const reverse = str.split("").reverse().join("");

  if (str !== reverse) return "none";

  if (n % 2 === 0) return str[mid - 1] + str[mid];
  return str[mid];
}

console.log(palindromeLocator("racecar"));
console.log(palindromeLocator("level"));
console.log(palindromeLocator("freecodecamp"));
console.log(palindromeLocator("noon"));
