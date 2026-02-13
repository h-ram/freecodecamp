def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

test1 = factorial(0)
test2 = factorial(5)
test3 = factorial(20)

check1 = 1
check2 = 120
check3 = 2432902008176640000

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")