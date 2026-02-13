def tire_status(pressures_psi, range_bar):

    min_psi = range_bar[0] * 14.5038
    max_psi = range_bar[1] * 14.5038

    statuses = []
    for tire_pressure in pressures_psi:
        if tire_pressure < min_psi:
            statuses.append("Low")
        elif tire_pressure < max_psi:
            statuses.append("Good")
        else:
            statuses.append("High")
    return statuses


test1 = tire_status([32, 28, 35, 29], [2, 3])
test2 = tire_status([32, 28, 35, 30], [2, 2.3])
test3 = tire_status([29, 26, 31, 28], [2.1, 2.5])
test4 = tire_status([31, 31, 30, 29], [1.5, 2])
test5 = tire_status([30, 28, 30, 29], [1.9, 2.1])


check1 = ["Good", "Low", "Good", "Low"]
check2 = ["Good", "Low", "High", "Good"]
check3 = ["Low", "Low", "Good", "Low"]
check4 = ["High", "High", "High", "Good"]
check5 = ["Good", "Good", "Good", "Good"]


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
