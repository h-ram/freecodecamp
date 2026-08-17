def get_food_chain(pairs):
    next_animal = {}
    predators = set()
    prey = set()

    for predator, target in pairs:
        next_animal[predator] = target
        predators.add(predator)
        prey.add(target)

    current = (predators - prey).pop()
    output = []

    while current in next_animal:
        output.append(current)
        current = next_animal[current]

    output.append(current)
    return output


print(get_food_chain([["cat", "mouse"]]))
print(get_food_chain([["wolf", "deer"], ["deer", "grass"]]))
print(get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]))
print(get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]))
print(get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]))