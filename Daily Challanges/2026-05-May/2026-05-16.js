function getLongestChain(dominoes) {
  function search(last, used) {
    let best = [];
    for (let i = 0; i < dominoes.length; i++) {
      if (!used.has(i)) {
        const d = dominoes[i];
        const options = [d, [d[1], d[0]]];
        for (const tile of options) {
          if (tile[0] === last) {
            const newUsed = new Set(used);
            newUsed.add(i);
            const rest = search(tile[1], newUsed);
            if (rest.length + 1 > best.length) {
              best = [tile, ...rest];
            }
          }
        }
      }
    }

    return best;
  }

  let best = [];

  for (let i = 0; i < dominoes.length; i++) {
    const d = dominoes[i];
    const options = [d, [d[1], d[0]]];

    for (const tile of options) {
      const used = new Set([i]);

      const result = [tile, ...search(tile[1], used)];

      if (result.length > best.length) {
        best = result;
      }
    }
  }

  return best;
}

console.log(
  getLongestChain([
    [1, 2],
    [4, 5],
    [2, 3],
  ]),
);
console.log(
  getLongestChain([
    [2, 1],
    [4, 3],
    [5, 3],
  ]),
);
