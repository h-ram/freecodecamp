function capitalizeFibonacci(s) {
  const n = s.length;
  const fib = new Set();
  let a = 0,
    b = 1;
  while (a < n) {
    fib.add(a);
    [a, b] = [b, a + b];
  }
  let res = "";
  for (let i = 0; i < n; i++) {
    const c = s[i];
    if (/[a-zA-Z]/.test(c)) {
      if (fib.has(i)) res += c.toUpperCase();
      else res += c.toLowerCase();
    } else {
      res += c;
    }
  }
  return res;
}
