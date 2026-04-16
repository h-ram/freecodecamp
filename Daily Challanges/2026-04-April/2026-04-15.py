def sort_and_swap(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if i % 3 == 0:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
    return arr

print(sort_and_swap([3, 1, 2, 4, 6, 5]))