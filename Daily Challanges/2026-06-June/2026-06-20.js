function primeFactorization(n) {
  const factors = [];
  let d = 2;

  while (d * d <= n) {
    while (n % d === 0) {
      factors.push(d);
      n = Math.floor(n / d);
    }
    d++;
  }

  if (n > 1) {
    factors.push(n);
  }

  return factors;
}

console.log(primeFactorization(20));
console.log(primeFactorization(17));
console.log(primeFactorization(15));
console.log(primeFactorization(35));
console.log(primeFactorization(999));
console.log(primeFactorization(360));
console.log(primeFactorization(510510));
