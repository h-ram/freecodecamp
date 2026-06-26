function calculateBmi(weight, height) {
  return Math.round((weight / (height * height)) * 703 * 10) / 10;
}

console.log(calculateBmi(180, 70));
console.log(calculateBmi(140, 64));
console.log(calculateBmi(160, 76));
console.log(calculateBmi(200, 60));
console.log(calculateBmi(150, 68));
