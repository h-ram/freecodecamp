def find_differences(arr):
    distances = []
    for i in range(len(arr)-1):
        distances.append(arr[i+1] - arr[i])
    distances.append(0)
    return distances

test1 = find_differences([1, 2, 4, 7])
test2 = find_differences([10, 15, 19, 22, 24, 25])
test3 = find_differences([25, 20, 16, 13, 11, 10])
test4 = find_differences([0, 1, 2, 2, 3, 3, 4, 5])
test5 = find_differences([1, 2, 5, 12, 34, -15, -1, 41, 113, -222, -99, -40, 10, -18, -6, -2, -1])

check1 = [1, 2, 3, 0]
check2 = [5, 4, 3, 2, 1, 0]
check3 = [-5, -4, -3, -2, -1, 0]
check4 = [1, 1, 0, 1, 0, 1, 1, 0]
check5 = [1, 3, 7, 22, -49, 14, 42, 72, -335, 123, 59, 50, -28, 12, 4, 1, 0]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")