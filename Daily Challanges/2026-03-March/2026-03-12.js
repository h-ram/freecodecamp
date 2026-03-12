function isValidDominoChain(dominoes) {
  for (let i = 0; i < dominoes.length - 1; i++) {
    if (dominoes[i][1] != dominoes[i + 1][0]) {
      return false;
    }
  }
  return true;
}
console.log(
  isValidDominoChain([
    [1, 3],
    [3, 6],
    [6, 5],
  ]),
); // true
console.log(
  isValidDominoChain([
    [6, 2],
    [3, 4],
    [4, 1],
  ]),
); // false
