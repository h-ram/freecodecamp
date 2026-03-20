function invertMatrix(matrix) {
  let values = new Set();
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      values.add(matrix[i][j]);
    }
  }

  const [a, b] = values;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      matrix[i][j] = matrix[i][j] === a ? b : a;
    }
  }
  return matrix;
}

console.log(
  invertMatrix([
    ["a", "b"],
    ["a", "a"],
  ]),
);
