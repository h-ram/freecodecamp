def squares_with_three(n):
    count = 0
    for i in range(3, n+1):
        if '3' in str(i*i):
            count += 1

    return count

test1 = squares_with_three(1)
test2 = squares_with_three(10)
test3 = squares_with_three(100)
test4 = squares_with_three(1000)
test5 = squares_with_three(10000)

check1 = 0
check2 = 1
check3 = 19
check4 = 326
check5 = 4531

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
