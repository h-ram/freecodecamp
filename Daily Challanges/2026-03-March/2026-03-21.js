function rotateGrid(grid) {
  return Array.from({ length: 6 }, (_, i) =>
    Array.from({ length: 6 }, (_, j) => grid[5 - j][i]).join(""),
  );
}

function isValid(grid) {
  function isBlock(i, j) {
    for (let x = 0; x < 2; x++) {
      for (let y = 0; y < 2; y++) {
        if (grid[i + x][j + y] !== "1") return false;
      }
    }
    return true;
  }
  return isBlock(0, 0) && isBlock(0, 4) && isBlock(4, 0);
}

function decodeQr(qrCode) {
  for (let k = 0; k < 4; k++) {
    if (isValid(qrCode)) {
      let result = [];
      for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 6; j++) {
          if ((i < 2 && j < 2) || (i < 2 && j >= 4) || (i >= 4 && j < 2)) {
            continue;
          }
          result.push(qrCode[i][j]);
        }
      }
      return result.join("");
    }
    qrCode = rotateGrid(qrCode);
  }
}

console.log(
  decodeQr(["110011", "110011", "000000", "000000", "110000", "110001"]),
);
