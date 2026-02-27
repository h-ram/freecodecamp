function shiftMatrix(matrix, shift) {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const total = rows * cols;

  // flatten
  let flat = [];
  for (let row of matrix) {
    flat.push(...row);
  }

  shift = shift % total;
  flat = flat.slice(-shift).concat(flat.slice(0, -shift));

  // rebuild matrix
  const result = [];
  for (let i = 0; i < rows; i++) {
    result.push(flat.slice(i * cols, (i + 1) * cols));
  }

  return result;
}

const test1 = shiftMatrix([[1, 2, 3], [4, 5, 6]], 1);
const test2 = shiftMatrix([[1, 2, 3], [4, 5, 6]], -1);
const test3 = shiftMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5);
const test4 = shiftMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6);
const test5 = shiftMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7);
const test6 = shiftMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54);

const check1 = [[6, 1, 2], [3, 4, 5]];
const check2 = [[2, 3, 4], [5, 6, 1]];
const check3 = [[5, 6, 7], [8, 9, 1], [2, 3, 4]];
const check4 = [[7, 8, 9], [1, 2, 3], [4, 5, 6]];
const check5 = [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]];
const check6 = [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]];

console.log(`Test1: ${JSON.stringify(test1) === JSON.stringify(check1)}`);
console.log(`Test2: ${JSON.stringify(test2) === JSON.stringify(check2)}`);
console.log(`Test3: ${JSON.stringify(test3) === JSON.stringify(check3)}`);
console.log(`Test4: ${JSON.stringify(test4) === JSON.stringify(check4)}`);
console.log(`Test5: ${JSON.stringify(test5) === JSON.stringify(check5)}`);
console.log(`Test6: ${JSON.stringify(test6) === JSON.stringify(check6)}`);