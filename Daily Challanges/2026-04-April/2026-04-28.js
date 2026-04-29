function numberToWords(n) {
  const ones = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
  ];

  const tens = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
  ];

  if (n < 20) {
    return ones[n];
  }

  if (n % 10 === 0) {
    return tens[Math.floor(n / 10)];
  }

  return tens[Math.floor(n / 10)] + "-" + ones[n % 10];
}
