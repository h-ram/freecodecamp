function findSignal(grid) {
  const rows = grid.length;
  const cols = grid[0].length;
  const towers = [];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (grid[r][c] > 0) {
        towers.push([r, c, grid[r][c]]);
      }
    }
  }

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      let valid = true;

      for (const [tr, tc, d] of towers) {
        if (Math.max(Math.abs(r - tr), Math.abs(c - tc)) !== d) {
          valid = false;
          break;
        }
      }

      if (valid) {
        return [r, c];
      }
    }
  }
}

console.log(
  findSignal([
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 1],
  ]),
);
console.log(
  findSignal([
    [0, 2, 0],
    [1, 0, 0],
    [0, 0, 1],
  ]),
);
console.log(
  findSignal([
    [0, 0, 2, 0],
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 1],
  ]),
);
console.log(
  findSignal([
    [0, 3, 0, 0, 0],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
  ]),
);
console.log(
  findSignal([
    [3, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 2],
  ]),
);
