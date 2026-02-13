def convert_to_km(miles):
    km = miles * 1.60934
    return round(km, 2)


test1 = convert_to_km(1)
test2 = convert_to_km(21)
test3 = convert_to_km(3.5)
test4 = convert_to_km(0)
test5 = convert_to_km(0.621371)

check1 = 1.61
check2 = 33.8
check3 = 5.63
check4 = 0
check5 = 1

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")