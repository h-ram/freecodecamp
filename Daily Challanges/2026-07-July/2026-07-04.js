function kaprekar(number) {
  let count = 0;

  while (number !== 6174) {
    let digits = number.toString().padStart(4, "0").split("");
    let large = parseInt([...digits].sort((a, b) => b - a).join(""));
    let small = parseInt([...digits].sort((a, b) => a - b).join(""));
    number = large - small;
    count++;
  }

  return count;
}

console.log(kaprekar(1234));
console.log(kaprekar(2025));
console.log(kaprekar(7173));
console.log(kaprekar(3164));
console.log(kaprekar(8082));
