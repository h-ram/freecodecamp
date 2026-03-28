function pascalRow(n) {
  let row = [1];
  for (let i = 0; i < n - 1; i++) {
    let newRow = [1];
    for (let j = 0; j < row.length - 1; j++) {
      newRow.push(row[j] + row[j + 1]);
    }
    newRow.push(1);
    row = newRow;
  }
  return row;
}

console.log(pascalRow(1));
console.log(pascalRow(2));
console.log(pascalRow(3));
console.log(pascalRow(5));
