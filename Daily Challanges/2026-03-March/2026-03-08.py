import re
def is_valid_hsl(hsl):
    pattern = r'^hsl\(\s*(\d{1,3})\s*,\s*(\d{1,3})%\s*,\s*(\d{1,3})%\s*\)\s*;?$'
    m = re.match(pattern, hsl)
    if not m:
        return False
    h = int(m.group(1))
    sat = int(m.group(2))
    light = int(m.group(3))
    return 0 <= h <= 360 and 0 <= sat <= 100 and 0 <= light <= 100

test1 = is_valid_hsl("hsl(240, 50%, 50%)")
test2 = is_valid_hsl("hsl( 200 , 50% , 75% )")
test3 = is_valid_hsl("hsl(99,60%,80%);")
test4 = is_valid_hsl("hsl(0, 0%, 0%) ;")
test5 = is_valid_hsl("hsl( 10 , 20% , 30% ) ;")
test6 = is_valid_hsl("hsl(361, 50%, 80%)")
test7 = is_valid_hsl("hsl(300, 101%, 70%)")
test8 = is_valid_hsl("hsl(200, 55%, 75)")
test9 = is_valid_hsl("hsl (80, 20%, 10%)")

check1 = True
check2 = True
check3 = True
check4 = True
check5 = True
check6 = False
check7 = False
check8 = False
check9 = False

print(f"Test1: {test1 == check1}")
print(f"Test2: {test2 == check2}")
print(f"Test3: {test3 == check3}")
print(f"Test4: {test4 == check4}")
print(f"Test5: {test5 == check5}")
print(f"Test6: {test6 == check6}")
print(f"Test7: {test7 == check7}")
print(f"Test8: {test8 == check8}")
print(f"Test9: {test9 == check9}")