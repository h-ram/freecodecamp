function explodeFizzbuzz(targetZCount) {
  let letters = Array.from("fizzbuzz");
  let steps = 0;
  while (letters.filter((c) => c === "z").length < targetZCount) {
    steps++;
    let newLetters = [];
    for (let i = 0; i < letters.length; i++) {
      let pos = i + 1;
      if (pos % 15 === 0) {
        newLetters.push(..."fizzbuzz");
      } else if (pos % 3 === 0) {
        newLetters.push(..."fizz");
      } else if (pos % 5 === 0) {
        newLetters.push(..."buzz");
      } else {
        newLetters.push(letters[i]);
      }
    }
    letters = newLetters;
  }
  return steps;
}

console.log(explodeFizzbuzz(9));
console.log(explodeFizzbuzz(15));
console.log(explodeFizzbuzz(51));
console.log(explodeFizzbuzz(52));
