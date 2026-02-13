def pairwise(arr, target):  
    sum_ = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                sum_ += i + j
    return sum_

test1 = pairwise([2, 3, 4, 6, 8], 10)
test2 = pairwise([4, 1, 5, 2, 6, 3], 7)
test3 = pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20)
test4 = pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24)

check1 = 9
check2 = 15
check3 = 22
check4 = 10

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")