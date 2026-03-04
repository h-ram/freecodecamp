def is_flat(arr):
    return all([type(item) != list for item in arr])

test1 = is_flat([1, 2, 3, 4])
test2 = is_flat([1, [2, 3], 4])
test3 = is_flat([1, 0, False, True, "a", "b"])
test4 = is_flat(["a", [0], "b", True])
test5 = is_flat([1, [2, [3, [4, [5]]]], 6])

check1 = True
check2 = False
check3 = True
check4 = False
check5 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")