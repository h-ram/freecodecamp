function fixNumerals(s) {
  const values = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let total = 0;

  for (const ch of s) {
    total += values[ch];
  }

  const roman = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
  ];

  let result = "";

  for (const [value, symbol] of roman) {
    while (total >= value) {
      result += symbol;
      total -= value;
    }
  }

  return result;
}

console.log(fixNumerals("XIIIII"));
console.log(fixNumerals("IIIILX"));
