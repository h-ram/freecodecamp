function mirror(str) {
  return str + str.split('').reverse().join('');
}

const test1 = mirror("freeCodeCamp");
const test2 = mirror("RaceCar");
const test3 = mirror("helloworld");
const test4 = mirror("The quick brown fox...");

const check1 = "freeCodeCamppmaCedoCeerf";
const check2 = "RaceCarraCecaR";
const check3 = "helloworlddlrowolleh";
const check4 = "The quick brown fox......xof nworb kciuq ehT";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);