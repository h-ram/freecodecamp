function petYears(pet, age) {
  const multipliers = {
    dog: 7,
    cat: 6,
    rabbit: 8,
    hamster: 30,
    "guinea pig": 12,
    goldfish: 6,
    bird: 5,
  };

  return age * multipliers[pet];
}

console.log(petYears("dog", 5));
console.log(petYears("cat", 9));
console.log(petYears("rabbit", 3));
console.log(petYears("hamster", 4));
console.log(petYears("guinea pig", 5));
console.log(petYears("goldfish", 2));
console.log(petYears("bird", 1));
