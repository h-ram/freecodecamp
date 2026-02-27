function countLettersAndNumbers(str) {
  let letterCount = 0;
  let numberCount = 0;
  for(const character of str){
    if(/^[a-zA-Z]$/.test(character)){letterCount++}
    if(/^[0-9]$/.test(character)){numberCount++}
  }
  const adj1 = letterCount === 1 ? "letter" : "letters";
  const adj2 = numberCount === 1 ? "number" : "numbers";
  const result = `The string has ${letterCount} ${adj1} and ${numberCount} ${adj2}.`
  return result;
}

const test1 = countLettersAndNumbers("helloworld123");
const test2 = countLettersAndNumbers("Catch 22");
const test3 = countLettersAndNumbers("A1!");
const test4 = countLettersAndNumbers("12345");
const test5 = countLettersAndNumbers("password");

const check1 = "The string has 10 letters and 3 numbers.";
const check2 = "The string has 5 letters and 2 numbers.";
const check3 = "The string has 1 letter and 1 number.";
const check4 = "The string has 0 letters and 5 numbers.";
const check5 = "The string has 8 letters and 0 numbers.";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);
console.log(`Test5: ${test5 === check5}`);