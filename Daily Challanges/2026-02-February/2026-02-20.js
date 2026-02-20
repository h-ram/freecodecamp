function isValidTrick(trickName) {
  const validFirsts = [
    "Misty",
    "Ghost",
    "Thunder",
    "Solar",
    "Sky",
    "Phantom",
    "Frozen",
    "Polar"
  ];

  const validSeconds = [
    "Twister",
    "Icequake",
    "Avalanche",
    "Vortex",
    "Snowstorm",
    "Frostbite",
    "Blizzard",
    "Shadow"
  ];
  const [word1, word2] = trickName.split(' ')
  return validFirsts.includes(word1) && validSeconds.includes(word2);
}


const test1 = isValidTrick("Polar Vortex");
const test2 = isValidTrick("Solar Icequake");
const test3 = isValidTrick("Thunder Blizzard");
const test4 = isValidTrick("Phantom Frostbite");
const test5 = isValidTrick("Ghost Avalanche");
const test6 = isValidTrick("Snowstorm Shadow");
const test7 = isValidTrick("Solar Sky");

const check1 = true;
const check2 = true;
const check3 = true;
const check4 = true;
const check5 = true;
const check6 = false;
const check7 = false;

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);
console.log(`Test6: ${test6 === check6}`);
console.log(`Test7: ${test7 === check7}`);