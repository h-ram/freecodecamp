def find_offender(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            if i - 2 >= 0 and arr[i] < arr[i - 2]:
                return i
            return i - 1
    return -1


print(find_offender([1, 6, 2, 3, 4, 5]))
print(find_offender([1, 2, 3, 5, 4, 5]))
print(find_offender([2, 4, 1, 6, 8]))