function transpose(matrix) {
  const m = matrix.length;
  const n = matrix[0].length;
  const transposedMatrix = [];
  for (let i = 0; i < n; i++) {
    const temp = [];
    for (let j = 0; j < m; j++) {
      temp.push(matrix[j][i]);
    }
    transposedMatrix.push(temp);
  }
  return transposedMatrix;
}

console.log(
  transpose([
    [1, 2, 3],
    [4, 5, 6],
  ]),
);
console.log(
  transpose([
    [1, 2],
    [3, 4],
    [5, 6],
  ]),
);
