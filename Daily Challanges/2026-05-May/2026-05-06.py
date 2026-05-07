def get_allergen_friendly_meals(meals, allergens):
    safe_meals = []
    allergens = set(allergens)
    for meal in meals:
        for allergen in meal[1]:
            if allergen in allergens:
                break;
        else:
            safe_meals.append(meal[0])
    return safe_meals

print(get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]))
print(get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]))