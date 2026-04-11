function rookAttack(rook1, rook2) {
  const [col1, row1] = rook1
  const [col2, row2] = rook2
  return col1 == col2 || row1 == row2;
}

console.log(rookAttack("A1", "A8"))
console.log(rookAttack("B4", "F4"))
console.log(rookAttack("E3", "D4"))