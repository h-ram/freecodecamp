function getLuckyNumber(name) {
  const [first, last] = name.split(" ");

  function counts(s) {
    let vowels = 0;
    let consonants = 0;

    for (const c of s.toLowerCase()) {
      if ("aeiou".includes(c)) {
        vowels++;
      } else if (/[a-z]/.test(c)) {
        consonants++;
      }
    }

    return [vowels, consonants, s.length];
  }

  const [v1, c1, l1] = counts(first);
  const [v2, c2, l2] = counts(last);

  const small = Math.min(v1, v2) * Math.min(c1, c2) * Math.min(l1, l2);
  const large = Math.max(v1, v2) * Math.max(c1, c2) * Math.max(l1, l2);

  const ans = large - small;
  return ans === 0 ? 13 : ans;
}

console.log(getLuckyNumber("John Doe"));
console.log(getLuckyNumber("Olivia Lewis"));
console.log(getLuckyNumber("James Wilson"));
console.log(getLuckyNumber("Elizabeth Hernandez"));
console.log(getLuckyNumber("Mike Walker"));
console.log(getLuckyNumber("Chloe Perez"));
