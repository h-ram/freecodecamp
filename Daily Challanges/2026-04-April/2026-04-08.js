function fizzBuzz(num){
  let answer = ""
  if(num % 3 == 0) answer += "Fizz";
  if(num % 5 == 0) answer += "Buzz";
  return answer ? answer : num;
}
function isFizzBuzz(arr) {
  const size = arr.length
  let first_number;
  for(let i=0; i<=size; i++){
    if(typeof arr[i] === "number"){
      first_number = arr[i] - i 
    }
  }
  for(let i = 0; i<size ;i++){
    if(arr[i] != fizzBuzz(first_number))
      return false
    first_number += 1
  }
  return true;
}

console.log(isFizzBuzz([1, 2, "Fizz", 4, "Buzz"]))
console.log(isFizzBuzz([13, 14, "FizzBuzz", 16, 17]))
console.log(isFizzBuzz([1, 2, "Fizz", 4, 5]))
console.log(isFizzBuzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]))