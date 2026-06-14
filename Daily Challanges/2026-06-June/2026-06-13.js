function getZoneViolations(grid) {
  const violations = [];
  if (!grid || grid.length === 0 || grid[0].length === 0) {
    return violations;
  }

  const rows = grid.length;
  const cols = grid[0].length;
  const invalidAdj = {
    i: new Set(["R", "I"]),
    A: new Set(["C"]),
    R: new Set(["i", "C"]),
    I: new Set(["i"]),
    C: new Set(["R", "A"]),
    "": new Set(),
  };

  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const cell = grid[r][c];
      let isViolating = false;

      for (const [dr, dc] of directions) {
        const nr = r + dr;
        const nc = c + dc;

        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
          const neighbor = grid[nr][nc];
          if (invalidAdj[cell] && invalidAdj[cell].has(neighbor)) {
            isViolating = true;
            break;
          }
        }
      }

      if (isViolating) {
        violations.push([r, c]);
      }
    }
  }

  return violations;
}

console.log(
  getZoneViolations([
    ["R", "C"],
    ["", "C"],
  ]),
);
console.log(
  getZoneViolations([
    ["", "i"],
    ["", "R"],
    ["R", "I"],
  ]),
);
console.log(
  getZoneViolations([
    ["A", "i", "C"],
    ["A", "", "C"],
    ["R", "R", "I"],
  ]),
);
console.log(
  getZoneViolations([
    ["R", "R", "C", "R", "R"],
    ["R", "I", "C", "", "A"],
    ["R", "R", "", "i", "A"],
  ]),
);
console.log(
  getZoneViolations([
    ["R", "A", "A", "", "i", "i"],
    ["R", "I", "", "C", "i", "i"],
    ["R", "", "C", "C", "A", "A"],
    ["R", "R", "C", "I", "R", "R"],
  ]),
);
