function isNarcissistic(n) {
  const digits = String(n)
    .split("")
    .map((item) => Number(item));
  const n_digits = digits.length;
  const raised_sum = digits.reduce((sum, digit) => sum + digit ** n_digits, 0);
  console.log(raised_sum);
  return raised_sum == n;
}

console.log(isNarcissistic(153));
console.log(isNarcissistic(154));
