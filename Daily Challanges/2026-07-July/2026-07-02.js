function getMaxProfit(prices, budget) {
  let minPrice = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; i++) {
    let price = prices[i];
    let shares = Math.floor(budget / minPrice);
    let profit = shares * (price - minPrice);

    if (profit > maxProfit) {
      maxProfit = profit;
    }

    if (price < minPrice) {
      minPrice = price;
    }
  }

  maxProfit = Math.floor(maxProfit * 100) / 100;
  return maxProfit.toFixed(2);
}

console.log(getMaxProfit([5, 6], 50));
console.log(getMaxProfit([8, 2, 5, 10], 20));
console.log(getMaxProfit([4, 5, 3, 6], 20));
console.log(getMaxProfit([54.4, 51.22, 53.99, 50.28, 53.01, 52.84], 200));
console.log(getMaxProfit([15.38, 15.01, 14.99, 14.62, 14.28], 80));
console.log(
  getMaxProfit(
    [121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33],
    1230.25,
  ),
);
