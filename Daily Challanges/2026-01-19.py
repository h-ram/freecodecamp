def compare_energy(calories_burned, watt_hours_used):
    cal = calories_burned * 4184
    wat = watt_hours_used * 3600

    if cal > wat:
        return "Workout"
    elif cal < wat:
        return "Devices"
    else: 
        return "Equal"

    return calories_burned

test1 = compare_energy(250, 50)
test2 = compare_energy(100, 200)
test3 = compare_energy(450, 523)
test4 = compare_energy(300, 75)
test5 = compare_energy(200, 250)
test6 = compare_energy(900, 1046)

check1 = "Workout"
check2 = "Devices"
check3 = "Equal"
check4 = "Workout"
check5 = "Devices"
check6 = "Equal"

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")