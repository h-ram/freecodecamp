function zipStrings(a, b) {
  let result = [];
  let min_len = Math.min(a.length, b.length);
  for (let i = 0; i < min_len; i++) {
    result.push(a[i]);
    result.push(b[i]);
  }
  result.push(a.slice(min_len));
  result.push(b.slice(min_len));
  return result.join("");
}

console.log(zipStrings("abc", "123"));
console.log(zipStrings("day", "night"));
