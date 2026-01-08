def is_sorted(arr):
    
    ascending = sorted(arr)
    descending = sorted(arr, reverse=True)

    if arr == ascending:
        return "Ascending"
    elif arr == descending:
        return "Descending"
    else:
        return "Not sorted"


test1 = is_sorted([1, 2, 3, 4, 5])
test2 = is_sorted([10, 8, 6, 4, 2])
test3 = is_sorted([1, 3, 2, 4, 5])
test4 = is_sorted([3.14, 2.71, 1.61, 0.57])
test5 = is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9])
test6 = is_sorted([0.4, 0.5, 0.3])

check1 = "Ascending"
check2 = "Descending"
check3 = "Not sorted"
check4 = "Descending"
check5 = "Ascending"
check6 = "Not sorted"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")