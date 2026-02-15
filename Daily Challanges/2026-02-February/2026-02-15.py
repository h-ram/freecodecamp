def get_hill_rating(drop, distance, hill_type):
    type_converter = {
        "Downhill": 1.2,
        "Slalom": 0.9,
        "Giant Slalom": 1.0
    }
    steepness = drop / distance
    adjusted_steepness = steepness * type_converter[hill_type]

    if adjusted_steepness <= 0.1:
        return "Green"
    if adjusted_steepness <= 0.25:
        return "Blue"
    return "Black"


test1 = get_hill_rating(95, 900, "Slalom")
test2 = get_hill_rating(620, 2800, "Downhill")
test3 = get_hill_rating(420, 1680, "Giant Slalom")
test4 = get_hill_rating(250, 3000, "Downhill")
test5 = get_hill_rating(110, 900, "Slalom")
test6 = get_hill_rating(380, 1500, "Giant Slalom")

check1 = "Green"
check2 = "Black"
check3 = "Blue"
check4 = "Green"
check5 = "Blue"
check6 = "Black"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")