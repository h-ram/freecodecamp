def calculate_penalty_distance(rounds):
    distance = 0
    for rnd in rounds:
        distance += (5 - rnd) * 150
    return distance

test1 = calculate_penalty_distance([4, 4])
test2 = calculate_penalty_distance([5, 5])
test3 = calculate_penalty_distance([4, 5, 3, 5])
test4 = calculate_penalty_distance([5, 4, 5, 5])
test5 = calculate_penalty_distance([4, 3, 0, 3])

check1 = 300
check2 = 0
check3 = 450
check4 = 150
check5 = 1500

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")