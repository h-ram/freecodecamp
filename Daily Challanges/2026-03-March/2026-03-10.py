def insert_into_array(arr, value, index):
    arr.insert(index, value);
    return arr

test1 = insert_into_array([2, 4, 8, 10], 6, 2)
test2 = insert_into_array(["the", "quick", "fox"], "brown", 2)
test3 = insert_into_array([], 0, 0)
test4 = insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5)

check1 = [2, 4, 6, 8, 10]
check2 = ["the", "quick", "brown", "fox"]
check3 = [0]
check4 = [0, 1, 1, 2, 3, 5, 8, 13]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
