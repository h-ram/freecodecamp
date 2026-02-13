def daylight_hours(latitude):
    table = {
        -90: 24,
        -75: 23,
        -60: 21,
        -45: 15,
        -30: 13,
        -15: 12,
         0: 12,
         15: 11,
         30: 10,
         45: 9,
         60: 6,
         75: 2,
         90: 0
    }

    closest = min(table.keys(), key=lambda k: abs(k - latitude))
    return table[closest]

test1 = daylight_hours(45)
test2 = daylight_hours(0)
test3 = daylight_hours(-90)
test4 = daylight_hours(-10)
test5 = daylight_hours(23)
test6 = daylight_hours(88)
test7 = daylight_hours(-33)
test8 = daylight_hours(70)

check1 = 9
check2 = 12
check3 = 24
check4 = 12
check5 = 10
check6 = 0
check7 = 13
check8 = 2
print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")
print(f"Test8: {test8==check8}")
