function getFoodChain(pairs) {
  const nextAnimal = {};
  const predators = new Set();
  const prey = new Set();

  for (const [predator, target] of pairs) {
    nextAnimal[predator] = target;
    predators.add(predator);
    prey.add(target);
  }

  let current;
  for (const animal of predators) {
    if (!prey.has(animal)) {
      current = animal;
      break;
    }
  }

  const output = [];

  while (current in nextAnimal) {
    output.push(current);
    current = nextAnimal[current];
  }

  output.push(current);
  return output;
}

console.log(getFoodChain([["cat", "mouse"]]));
console.log(
  getFoodChain([
    ["wolf", "deer"],
    ["deer", "grass"],
  ]),
);
console.log(
  getFoodChain([
    ["hawk", "snake"],
    ["snake", "frog"],
    ["frog", "fly"],
  ]),
);
console.log(
  getFoodChain([
    ["rabbit", "grass"],
    ["fox", "rabbit"],
    ["eagle", "fox"],
  ]),
);
console.log(
  getFoodChain([
    ["seal", "salmon"],
    ["herring", "shrimp"],
    ["orca", "seal"],
    ["shrimp", "plankton"],
    ["salmon", "herring"],
  ]),
);
