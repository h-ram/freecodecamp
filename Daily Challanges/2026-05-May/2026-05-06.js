function getAllergenFriendlyMeals(meals, allergens) {
  let safeMeals = [];
  const avoid = new Set(allergens);
  for (const [mealName, mealAllergens] of meals) {
    const hasBadAllergen = mealAllergens.some((allergen) =>
      avoid.has(allergen),
    );
    if (!hasBadAllergen) safeMeals.push(mealName);
  }
  return safeMeals;
}

console.log(
  getAllergenFriendlyMeals(
    [
      ["pasta", ["wheat", "milk"]],
      ["salad", ["nuts"]],
    ],
    ["milk"],
  ),
);
console.log(
  getAllergenFriendlyMeals(
    [
      ["steak", ["soy"]],
      ["fried rice", []],
      ["fish tacos", ["fish", "wheat"]],
      ["chicken parmesan", ["wheat", "milk"]],
    ],
    ["soy", "fish"],
  ),
);
