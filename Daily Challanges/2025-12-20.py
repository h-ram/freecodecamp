from collections import Counter

def purge_most_frequent(arr):

    most_common = Counter(arr).most_common(1)[0][0]

    result = [n for n in arr if n != most_common]

    return result


test1 = purge_most_frequent([1, 2, 2, 3])
test2 = purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"])
test3 = purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"])
test4 = purge_most_frequent([5, 5, 5, 5])


check1 = [1, 3]
check2 = ["a", "b", "b", "c", "c", "c"]
check3 = ["red", "green", "red", "green"]
check4 = []


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
