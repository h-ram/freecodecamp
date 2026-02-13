def is_valid_number(n, base):

    if not (2 <= base <= 36):
        return False

    for ch in n.strip():
        if ch.isdigit():
            val = ord(ch) - ord('0')
        elif ch.isalpha():
            val = ord(ch.upper()) - ord('A') + 10
        else:
            return False
        if val >= base:
            return False
    return True

test1 = is_valid_number("10101", 2)
test2 = is_valid_number("10201", 2)
test3 = is_valid_number("76543210", 8)
test4 = is_valid_number("9876543210", 8)
test5 = is_valid_number("9876543210", 10)
test6 = is_valid_number("ABC", 10)
test7 = is_valid_number("ABC", 16)
test8 = is_valid_number("Z", 36)
test9 = is_valid_number("ABC", 20)
test10 = is_valid_number("4B4BA9", 16)
test11 = is_valid_number("5G3F8F", 16)
test12 = is_valid_number("5G3F8F", 17)
test13 = is_valid_number("abc", 10)
test14 = is_valid_number("abc", 16)
test15 = is_valid_number("AbC", 16)
test16 = is_valid_number("z", 36)


check1 = True
check2 = False
check3 = True
check4 = False
check5 = True
check6 = False
check7 = True
check8 = True
check9 = True
check10 = True
check11 = False
check12 = True
check13 = False
check14 = True
check15 = True
check16 = True

print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
print(f"Test7: {test7==check7}")
print(f"Test8: {test8==check8}")
print(f"Test9: {test9==check9}")
print(f"Test10: {test10==check10}")
print(f"Test11: {test11==check11}")
print(f"Test12: {test12==check12}")
print(f"Test13: {test13==check13}")
print(f"Test14: {test14==check14}")
print(f"Test15: {test15==check15}")
print(f"Test16: {test16==check16}")

