from itertools import permutations

def is_prime(num):
    n_divisors = 2
    for i in range(2,num):
        if num % i == 0:
            n_divisors += 1

    return n_divisors == 2

def get_rotations(n):
    s = str(n)
    length = len(s)
    rotations = []
    
    for i in range(length):
        rotated = s[i:] + s[:i]
        rotations.append(int(rotated))
    
    return rotations

def is_circular_prime(n):
    
    rotations = get_rotations(n)

    for rotation in rotations:
        if not is_prime(rotation):
            return False
    return True


test1 = is_circular_prime(197)
test2 = is_circular_prime(23)
test3 = is_circular_prime(13)
test4 = is_circular_prime(89)
test5 = is_circular_prime(1193)

check1 = True
check2 = False
check3 = True
check4 = False
check5 = True


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")