def find_target(arr, target):

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
            
    return "Target not found"


test1 = find_target([2, 7, 11, 15], 9)
test2 = find_target([3, 2, 4, 5], 6)
test3 = find_target([1, 3, 5, 6, 7, 8], 15)
test4 = find_target([1, 3, 5, 7], 14)

check1 = [0, 1]
check2 = [1, 2]
check3 = [4, 5]
check4 = 'Target not found'

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
