def is_leap_year(year):
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0);

test1 = is_leap_year(2024)
test2 = is_leap_year(2023)
test3 = is_leap_year(2100)
test4 = is_leap_year(2000)
test5 = is_leap_year(1999)
test6 = is_leap_year(2040)
test7 = is_leap_year(2026)

check1 = True
check2 = False
check3 = False
check4 = True
check5 = False
check6 = True
check7 = False

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")