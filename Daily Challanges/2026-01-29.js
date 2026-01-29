function isDigit(char) {
    return char >= '0' && char <= '9';
}

function separateLettersAndNumbers(str) {
  let result = [str[0]]
  for(let i = 1; i < str.length ; i++){
     if(isDigit(str[i-1]) != isDigit(str[i])){
       result.push('-')
     }
     result.push(str[i])
  }
  return result.join('');
}

const test1 = separateLettersAndNumbers("ABC123");
const test2 = separateLettersAndNumbers("Route66");
const test3 = separateLettersAndNumbers("H3LL0W0RLD");
const test4 = separateLettersAndNumbers("a1b2c3d4");

const check1 = "ABC-123";
const check2 = "Route-66";
const check3 = "H-3-LL-0-W-0-RLD";
const check4 = "a-1-b-2-c-3-d-4";

console.log(`Test1: ${test1 === check1}`);
console.log(`Test2: ${test2 === check2}`);
console.log(`Test3: ${test3 === check3}`);
console.log(`Test4: ${test4 === check4}`);