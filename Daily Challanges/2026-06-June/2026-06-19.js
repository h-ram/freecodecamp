function getRentalCost(rented, returned, tier) {
  const pricing = {
    1: { base: 4.99, late: 3.99 },
    3: { base: 3.99, late: 2.99 },
    7: { base: 2.99, late: 0.99 },
  };

  const rentedDate = new Date(rented);
  const returnedDate = new Date(returned);

  const dueDate = new Date(
    Date.UTC(
      rentedDate.getUTCFullYear(),
      rentedDate.getUTCMonth(),
      rentedDate.getUTCDate() + tier,
      12,
      0,
      0,
      0,
    ),
  );

  let lateDays = 0;

  if (returnedDate > dueDate) {
    lateDays = Math.ceil((returnedDate - dueDate) / (1000 * 60 * 60 * 24));
  }

  const total = pricing[tier].base + lateDays * pricing[tier].late;

  return `$${total.toFixed(2)}`;
}

console.log(getRentalCost("2026-06-18T18:30:00Z", "2026-06-19T10:30:00Z", 1));
console.log(getRentalCost("2026-06-18T14:30:00Z", "2026-06-20T12:30:00Z", 1));
console.log(getRentalCost("2026-06-18T10:15:00Z", "2026-06-18T19:45:00Z", 3));
console.log(getRentalCost("2026-06-18T15:20:00Z", "2026-06-23T08:10:00Z", 3));
console.log(getRentalCost("2026-06-18T12:00:00Z", "2026-06-25T12:00:00Z", 7));
console.log(getRentalCost("2026-06-18T08:00:00Z", "2027-06-18T14:00:00Z", 7));
