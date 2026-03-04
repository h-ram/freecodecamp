import math
def count_perfect_cubes(a, b):
    smallest = min(a,b)
    largest = max(a,b)
    perfect_cubes = 0
    num = math.floor(math.cbrt(smallest))
    
    while num*num*num <= largest:
        if num*num*num >= smallest:
            perfect_cubes += 1
        num +=1
        
    return perfect_cubes

test1 = count_perfect_cubes(3, 30)
test2 = count_perfect_cubes(1, 30)
test3 = count_perfect_cubes(30, 0)
test4 = count_perfect_cubes(-64, 64)
test5 = count_perfect_cubes(9214, -8127)

check1 = 2
check2 = 3
check3 = 4
check4 = 9
check5 = 41

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")