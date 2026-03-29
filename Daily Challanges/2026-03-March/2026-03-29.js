function isValidIsbn10(s) {
  s = s.replace(/-/g, "");
  if (s.length !== 10) return false;
  let total = 0;
  for (let i = 0; i < 10; i++) {
    let value;
    if (i < 9) {
      if (!/^\d$/.test(s[i])) return false;
      value = Number(s[i]);
    } else {
      if (s[i] === "X") {
        value = 10;
      } else if (/^\d$/.test(s[i])) {
        value = Number(s[i]);
      } else {
        return false;
      }
    }
    total += value * (i + 1);
  }
  return total % 11 === 0;
}
