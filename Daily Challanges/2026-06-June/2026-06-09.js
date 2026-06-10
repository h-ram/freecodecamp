function getRoommates(people) {
  const groups = new Map();
  for (const person of people) {
    const g = person.group;
    if (!groups.has(g)) groups.set(g, []);
    groups.get(g).push(person.name);
  }

  const rooms = [];
  for (const names of groups.values()) {
    let i = 0;
    while (i + 1 < names.length) {
      rooms.push(`${names[i]} and ${names[i + 1]}`);
      i += 2;
    }
    if (i < names.length) rooms.push(names[i]);
  }

  return rooms;
}

console.log(
  getRoommates([
    { name: "Alice", group: "A" },
    { name: "Bob", group: "B" },
    { name: "Carol", group: "A" },
  ]),
);

console.log(
  getRoommates([
    { name: "John", group: "C" },
    { name: "Julia", group: "C" },
    { name: "Jim", group: "C" },
  ]),
);

console.log(
  getRoommates([
    { name: "Adam", group: "D" },
    { name: "Abraham", group: "E" },
    { name: "Austin", group: "E" },
    { name: "Augustus", group: "D" },
    { name: "Angelica", group: "D" },
    { name: "Aaron", group: "E" },
  ]),
);

console.log(
  getRoommates([
    { name: "Frank", group: "A" },
    { name: "Emitt", group: "B" },
    { name: "Daria", group: "F" },
    { name: "Charles", group: "D" },
    { name: "Bailey", group: "A" },
    { name: "Albert", group: "F" },
  ]),
);

console.log(
  getRoommates([
    { name: "Kevin", group: "A" },
    { name: "Yuri", group: "A" },
    { name: "Hugo", group: "B" },
    { name: "Violet", group: "A" },
    { name: "Brett", group: "A" },
    { name: "Wayne", group: "B" },
  ]),
);
