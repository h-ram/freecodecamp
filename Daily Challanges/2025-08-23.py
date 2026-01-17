def is_unnatural_prime(n):
    n = abs(n)
    if n == 0 or n == 1:
        return False
        
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

test1 = is_unnatural_prime(1)
test2 = is_unnatural_prime(-1)
test3 = is_unnatural_prime(19)
test4 = is_unnatural_prime(-23)
test5 = is_unnatural_prime(0)
test6 = is_unnatural_prime(97)
test7 = is_unnatural_prime(-61)
test8 = is_unnatural_prime(99)
test9 = is_unnatural_prime(-44)

check1 = False
check2 = False
check3 = True
check4 = True
check5 = False
check6 = True
check7 = True
check8 = False
check9 = False

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")
print(f"Test8: {test8==check8}")
print(f"Test9: {test9==check9}")
