def flatten(arr):
    result = []
    def flatten_helper(item):
        if isinstance(item, list):
            for element in item:
                flatten_helper(element)
        else:
            result.append(item)
    
    flatten_helper(arr)
    return result

test1 = flatten([1, [2, 3], 4])
test2 = flatten([5, [4, [3, 2]], 1])
test3 = flatten(["A", [[[["B"]]]], "C"])
test4 = flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])
test5 = flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])

check1 = [1, 2, 3, 4]
check2 = [5, 4, 3, 2, 1]
check3 = ["A", "B", "C"]
check4 = ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
check5 = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")