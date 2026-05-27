def sum_of_differences(arr):
    diffs = [] 
    for i in range(len(arr)-1):
        diffs.append(arr[i+1]-arr[i])
    return sum(diffs)

print(sum_of_differences([1, 3, 4]))
print(sum_of_differences([5, -3, 3, 9, 10]))
print(sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]))
print(sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]))