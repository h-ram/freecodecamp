function fizzBuzzCount(start, end) {
  const counts = {
    fizz: 0,
    buzz: 0,
  };
  for (let num = start; num <= end; num++) {
    if (num % 3 === 0) counts.fizz += 1;
    if (num % 5 === 0) counts.buzz += 1;
  }
  return counts;
}

console.log(fizzBuzzCount(1, 11));
