function getOdds(dice, target) {
  let dp = new Array(target + 1).fill(0);
  dp[0] = 1;

  for (let i = 0; i < dice; i++) {
    const nextDp = new Array(target + 1).fill(0);

    for (let total = 0; total <= target; total++) {
      if (dp[total]) {
        for (let face = 1; face <= 6; face++) {
          if (total + face <= target) {
            nextDp[total + face] += dp[total];
          }
        }
      }
    }

    dp = nextDp;
  }

  const totalOutcomes = 6 ** dice;
  const ways = dp[target];
  const odds = Math.round(totalOutcomes / ways);

  return `1 in ${odds}`;
}

console.log(getOdds(1, 5));
console.log(getOdds(2, 4));
console.log(getOdds(3, 10));
console.log(getOdds(4, 7));
console.log(getOdds(5, 26));
console.log(getOdds(6, 35));
