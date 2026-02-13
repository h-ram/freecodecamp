def nth_fibonacci(n):
    fibs = [0,1]

    if n < 2:
        return fibs[n]

    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
        
    return fibs[n-1]


test1 = nth_fibonacci(4)
test2 = nth_fibonacci(10)
test3 = nth_fibonacci(15)
test4 = nth_fibonacci(40)
test5 = nth_fibonacci(75)

check1 = 2
check2 = 34
check3 = 377
check4 = 63245986
check5 = 1304969544928657   

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
