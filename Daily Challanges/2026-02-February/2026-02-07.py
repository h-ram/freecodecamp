def get_landing_stance(start_stance, rotation):
    trimmed_rotation = abs(rotation) % 360

    if trimmed_rotation < 180:
        return start_stance
    else:
        return "Regular" if start_stance == "Goofy" else "Goofy"


test1 = get_landing_stance("Regular", 90)
test2 = get_landing_stance("Regular", 180)
test3 = get_landing_stance("Goofy", -270)
test4 = get_landing_stance("Regular", 2340)
test5 = get_landing_stance("Goofy", 2160)

check1 = "Regular"
check2 = "Goofy"
check3 = "Regular"
check4 = "Goofy"
check5 = "Goofy"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")