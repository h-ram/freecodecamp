function bucketFill(grid, start, newValue) {
  const rows = grid.length;
  const cols = grid[0].length;
  const [row, col] = start;
  const oldValue = grid[row][col];

  if (oldValue === newValue) {
    return grid;
  }

  const stack = [[row, col]];

  while (stack.length) {
    const [r, c] = stack.pop();

    if (r < 0 || r >= rows || c < 0 || c >= cols) {
      continue;
    }

    if (grid[r][c] !== oldValue) {
      continue;
    }

    grid[r][c] = newValue;

    stack.push([r + 1, c]);
    stack.push([r - 1, c]);
    stack.push([r, c + 1]);
    stack.push([r, c - 1]);
  }

  return grid;
}

console.log(
  bucketFill(
    [
      ["R", "G"],
      ["R", "G"],
    ],
    [0, 1],
    "B",
  ),
);
console.log(
  bucketFill(
    [
      ["Y", "G", "G"],
      ["Y", "Y", "Y"],
      ["B", "Y", "R"],
    ],
    [1, 2],
    "B",
  ),
);
console.log(
  bucketFill(
    [
      ["O", "O", "P"],
      ["P", "O", "O"],
      ["P", "P", "O"],
    ],
    [2, 0],
    "R",
  ),
);
console.log(
  bucketFill(
    [
      ["T", "T", "R", "T"],
      ["R", "T", "R", "T"],
      ["R", "T", "R", "T"],
      ["T", "T", "T", "T"],
    ],
    [0, 3],
    "Y",
  ),
);
console.log(
  bucketFill(
    [
      ["G", "B", "G", "B"],
      ["R", "B", "B", "G"],
      ["B", "G", "B", "R"],
      ["B", "G", "G", "B"],
    ],
    [2, 2],
    "G",
  ),
);
