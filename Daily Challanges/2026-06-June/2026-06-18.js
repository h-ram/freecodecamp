function getStreamingBill(cart, subscription) {
  const pricesInCents = {
    HD_rent: 399,
    HD_buy: 1299,
    "4K_rent": 599,
    "4K_buy": 1999,
  };

  const discounts = {
    none: 0.0,
    basic: 0.1,
    premium: 0.25,
  };

  const totalCents = cart.reduce(
    (sum, item) => sum + pricesInCents[`${item.format}_${item.type}`],
    0,
  );

  let total = totalCents / 100;
  total *= 1 - discounts[subscription];

  return `$${total.toFixed(2)}`;
}

console.log(getStreamingBill([{ format: "HD", type: "rent" }], "none"));
console.log(
  getStreamingBill(
    [
      { format: "HD", type: "rent" },
      { format: "HD", type: "buy" },
    ],
    "premium",
  ),
);

console.log(
  getStreamingBill(
    [
      { format: "HD", type: "rent" },
      { format: "HD", type: "rent" },
      { format: "HD", type: "buy" },
    ],
    "basic",
  ),
);

console.log(
  getStreamingBill(
    [
      { format: "4K", type: "buy" },
      { format: "4K", type: "buy" },
    ],
    "premium",
  ),
);

console.log(
  getStreamingBill(
    [
      { format: "HD", type: "rent" },
      { format: "4K", type: "rent" },
      { format: "HD", type: "buy" },
      { format: "4K", type: "buy" },
    ],
    "none",
  ),
);

console.log(
  getStreamingBill(
    [
      { format: "HD", type: "rent" },
      { format: "4K", type: "rent" },
      { format: "HD", type: "buy" },
      { format: "4K", type: "buy" },
      { format: "HD", type: "buy" },
    ],
    "basic",
  ),
);
