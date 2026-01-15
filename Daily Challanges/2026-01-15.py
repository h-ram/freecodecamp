def array_swap(arr):
    return [arr[1], arr[0]]

test1 = array_swap(["A", "B"])
test2 = array_swap([25, 20])
test3 = array_swap([True, False])
test4 = array_swap(["1", 1])


check1 = ["B", "A"]
check2 = [20, 25]
check3 = [False, True]
check4 = [1, "1"]

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")