function getUniqueClimbs(steps) {
  let table = [1, 2];
  for (let i = 2; i < steps; i++) table.push(table.at(-2) + table.at(-1));
  return table.at(-1);
}

console.log(getUniqueClimbs(4));
console.log(getUniqueClimbs(5));
console.log(getUniqueClimbs(10));
