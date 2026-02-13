def largest_difference(skater1, skater2):
    largest_lap = 0
    largest_lap_time = 0
    for i in range(len(skater1)):
        diff = abs(skater1[i] - skater2[i])
        if diff > largest_lap_time:
            largest_lap = i+1
            largest_lap_time = diff

    return largest_lap

test1 = largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30])
test2 = largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23])
test3 = largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95])
test4 = largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01])
test5 = largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10])

check1 = 3
check2 = 1
check3 = 5
check4 = 2
check5 = 4

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")