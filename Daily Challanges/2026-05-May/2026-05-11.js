function getOldest(people) {
  let oldestAge = 0;
  let oldestPeople = [];
  for (const { name, age } of people) {
    if (age > oldestAge) {
      oldestPeople = [name];
      oldestAge = age;
    } else if (age == oldestAge) {
      oldestPeople.push(name);
    }
  }
  return oldestPeople;
}

console.log(getOldest([{ name: "Brenda", age: 40 }]));
console.log(
  getOldest([
    { name: "Alice", age: 30 },
    { name: "Bob", age: 25 },
  ]),
);
console.log(
  getOldest([
    { name: "Allison", age: 25 },
    { name: "Bill", age: 30 },
    { name: "Carol", age: 30 },
  ]),
);
