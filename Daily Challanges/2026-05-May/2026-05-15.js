const MENU = [
  ["cold brew", 4.5],
  ["oat latte", 5.0],
  ["cappuccino", 4.75],
  ["espresso", 3.0],
  ["vanilla syrup", 0.75],
  ["caramel drizzle", 0.6],
  ["extra shot", 0.5],
  ["oat milk", 0.75],
  ["cream", 0.75],
];

function formatCoffeeOrder(order) {
  const text = order.toLowerCase();
  const items = [];
  let total = 0;
  for (const [name, price] of MENU) {
    if (text.includes(name)) {
      items.push(name);
      total += price;
    }
  }
  return `${items.join(" + ")}: $${total.toFixed(2)}`;
}

console.log(
  formatCoffeeOrder(
    "I'd like an oat latte with vanilla syrup and an extra shot please.",
  ),
);
