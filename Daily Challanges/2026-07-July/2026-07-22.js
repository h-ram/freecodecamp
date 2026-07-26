function piggyBank(coins) {
  const total =
    (coins.pennies || 0) +
    (coins.nickels || 0) * 5 +
    (coins.dimes || 0) * 10 +
    (coins.quarters || 0) * 25;

  return `$${(total / 100).toFixed(2)}`;
}

console.log(piggyBank({ pennies: 3, nickels: 5, dimes: 2, quarters: 6 }));
console.log(piggyBank({ pennies: 1, nickels: 1, dimes: 1, quarters: 1 }));
console.log(piggyBank({ nickels: 8, dimes: 6, quarters: 5 }));
console.log(piggyBank({}));
console.log(piggyBank({ pennies: 146, nickels: 11, dimes: 0, quarters: 19 }));
