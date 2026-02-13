def sum_divisors(n):
    sum_ = 1 + n
    for i in range(2, n):
         if n%i==0:
             sum_ += i
    return sum_

test1 = sum_divisors(6)
test2 = sum_divisors(13)
test3 = sum_divisors(28)
test4 = sum_divisors(84)
test5 = sum_divisors(549)
test6 = sum_divisors(9348)

check1 = 12
check2 = 14
check3 = 56
check4 = 224
check5 = 806
check6 = 23520

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")