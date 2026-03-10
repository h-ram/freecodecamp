def sum_array(numbers):
    return sum(numbers)

test1 = sum_array([1, 2, 3, 4, 5])
test2 = sum_array([42])
test3 = sum_array([5, -2, 7, -3])
test4 = sum_array([203, 145, -129, 6293, 523, -919, 845, 2434])
test5 = sum_array([0, 0])

check1 = 15
check2 = 42
check3 = 7
check4 = 9395
check5 = 0

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")