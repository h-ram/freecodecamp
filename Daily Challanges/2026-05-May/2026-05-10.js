function isValidIsbn13(str) {
  let sum = 0;
  let digit_count = 0;
  let is_even = false;
  for (const char of str) {
    if (char === "-") continue;
    if (!/[0-9]/.test(char)) return false;
    sum += Number(char) * (is_even ? 3 : 1);
    is_even = !is_even;
    digit_count += 1;
  }
  return digit_count === 13 && sum % 10 === 0;
}

console.log(isValidIsbn13("9780306406157"));
console.log(isValidIsbn13("97803064061570"));
