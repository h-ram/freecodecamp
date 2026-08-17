function solveMagicSquare(grid) {
  const rowSums = grid.map((row) => row[0] + row[1] + row[2]);
  const target = Math.max(...rowSums);

  let r = -1;
  let c = -1;

  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      if (grid[i][j] === 0) {
        r = i;
        c = j;
      }
    }
  }

  const value = target - rowSums[r];

  if (value <= 0) {
    return "impossible";
  }

  grid[r][c] = value;

  const sum = grid[0][0] + grid[0][1] + grid[0][2];

  for (let i = 0; i < 3; i++) {
    if (grid[i][0] + grid[i][1] + grid[i][2] !== sum) {
      return "impossible";
    }
  }

  for (let j = 0; j < 3; j++) {
    if (grid[0][j] + grid[1][j] + grid[2][j] !== sum) {
      return "impossible";
    }
  }

  if (grid[0][0] + grid[1][1] + grid[2][2] !== sum) {
    return "impossible";
  }

  if (grid[0][2] + grid[1][1] + grid[2][0] !== sum) {
    return "impossible";
  }

  return value;
}

console.log(
  solveMagicSquare([
    [2, 7, 6],
    [9, 0, 1],
    [4, 3, 8],
  ]),
);
console.log(
  solveMagicSquare([
    [0, 14, 12],
    [18, 10, 2],
    [8, 6, 16],
  ]),
);
console.log(
  solveMagicSquare([
    [12, 17, 16],
    [19, 0, 10],
    [14, 13, 18],
  ]),
);
console.log(
  solveMagicSquare([
    [15, 35, 31],
    [43, 27, 11],
    [23, 19, 0],
  ]),
);
console.log(
  solveMagicSquare([
    [26, 41, 14],
    [47, 35, 0],
    [32, 29, 44],
  ]),
);
