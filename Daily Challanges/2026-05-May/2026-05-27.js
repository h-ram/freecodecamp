function getPizzasToOrder(hoursWorked) {
  let slices = 0;
  for (const hours of hoursWorked) {
    slices += Math.max(2, Math.ceil(hours / 3));
  }
  return Math.ceil(slices / 8);
}

console.log(getPizzasToOrder([8, 8, 8]));
console.log(getPizzasToOrder([10, 9, 8, 2, 2, 6, 10]));
console.log(getPizzasToOrder([1, 2, 3, 4, 5]));
console.log(getPizzasToOrder([8, 8, 8, 8, 8, 8, 8, 8]));
console.log(getPizzasToOrder([9, 9, 6]));
console.log(getPizzasToOrder([10, 12, 16, 9, 8, 11, 15, 8, 0]));
