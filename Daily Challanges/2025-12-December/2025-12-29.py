import math
def fuel_to_add(current_gallons, required_liters):
    required_gallons = required_liters * 0.264172
    to_add = math.ceil(required_gallons - current_gallons)
    return max(0, to_add)


test1 = fuel_to_add(0, 1)
test2 = fuel_to_add(5, 40)
test3 = fuel_to_add(10, 30)
test4 = fuel_to_add(896, 20500) 
test5 = fuel_to_add(1000, 50000)

check1 = 1
check2 = 6
check3 = 0
check4 = 4520
check5 = 12209


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
