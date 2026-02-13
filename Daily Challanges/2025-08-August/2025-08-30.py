def find_duplicates(arr):
    counts = {}
    duplicates = []

    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    for x, c in counts.items():
        if c > 1:
            duplicates.append(x)

    return sorted(duplicates)

test1 = find_duplicates([1, 2, 3, 4, 5])
test2 = find_duplicates([1, 2, 3, 4, 1, 2])
test3 = find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4])

check1 = []
check2 = [1, 2]
check3 = [-6, 0, 2, 4, 5, 23]

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")