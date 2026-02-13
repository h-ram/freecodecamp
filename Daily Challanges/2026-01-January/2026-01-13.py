def odd_or_even(n):

    return "Odd" if n % 2 == 1 else "Even"


test1 = odd_or_even(1)
test2 = odd_or_even(2)
test3 = odd_or_even(13)
test4 = odd_or_even(196)
test5 = odd_or_even(123456789)


check1 = "Odd"
check2 = "Even"
check3 = "Odd"
check4 = "Even"
check5 = "Odd"

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")