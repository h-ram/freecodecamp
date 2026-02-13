def sum_of_squares(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i*i
    return sum_

test1 = sum_of_squares(5)
test2 = sum_of_squares(10)
test3 = sum_of_squares(25)
test4 = sum_of_squares(500)
test5 = sum_of_squares(1000)

check1 = 55
check2 = 385
check3 = 5525
check4 = 41791750
check5 = 333833500


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")