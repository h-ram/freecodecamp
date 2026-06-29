function connectThree(board) {
  if (!board.length || !board[0].length) return [];

  const rows = board.length;
  const cols = board[0].length;
  const directions = [
    [0, 1],
    [1, 0],
    [1, 1],
    [1, -1],
  ];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (board[r][c] === "") continue;

      for (const [dr, dc] of directions) {
        const cells = [];

        for (let k = 0; k < 3; k++) {
          const nr = r + dr * k;
          const nc = c + dc * k;

          if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) break;
          if (board[nr][nc] !== board[r][c]) break;

          cells.push([nr, nc]);
        }

        if (cells.length === 3) {
          cells.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
          return [board[r][c], ...cells];
        }
      }
    }
  }

  return [];
}

console.log(
  connectThree([
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "Y", "", ""],
    ["Y", "R", "R", "R"],
  ]),
);

console.log(
  connectThree([
    ["", "", "", ""],
    ["", "Y", "Y", ""],
    ["", "Y", "R", "R"],
    ["", "Y", "R", "R"],
  ]),
);

console.log(
  connectThree([
    ["", "", "Y", "R"],
    ["", "Y", "R", "Y"],
    ["", "R", "Y", "R"],
    ["", "R", "Y", "R"],
  ]),
);

console.log(
  connectThree([
    ["", "Y", "", ""],
    ["", "Y", "Y", ""],
    ["", "R", "R", "Y"],
    ["R", "R", "Y", "R"],
  ]),
);

console.log(
  connectThree([
    ["Y", "R", "R", "Y"],
    ["R", "Y", "Y", "R"],
    ["Y", "R", "R", "Y"],
    ["R", "Y", "Y", "R"],
  ]),
);
