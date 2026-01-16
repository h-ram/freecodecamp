import math

def is_integer_hypotenuse(a, b):
    c = math.sqrt(a*a + b*b)
    return c == int(c)

test1 = is_integer_hypotenuse(3, 4)
test2 = is_integer_hypotenuse(2, 3)
test3 = is_integer_hypotenuse(5, 12)
test4 = is_integer_hypotenuse(10, 10)
test5 = is_integer_hypotenuse(780, 1040)
test6 = is_integer_hypotenuse(250, 333)

check1 = True
check2 = False
check3 = True
check4 = False
check5 = True
check6 = False

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")