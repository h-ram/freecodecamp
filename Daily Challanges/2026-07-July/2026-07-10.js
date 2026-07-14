function exactChange(amount) {
  const coins = [1, 5, 10, 25];
  const dp = new Array(amount + 1).fill(0);
  dp[0] = 1;

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] += dp[i - coin];
    }
  }

  return dp[amount];
}

console.log(exactChange(3));
console.log(exactChange(9));
console.log(exactChange(17));
console.log(exactChange(39));
console.log(exactChange(61));
console.log(exactChange(99));
